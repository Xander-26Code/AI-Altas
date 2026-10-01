"""Audit all external Markdown, image and catalog URLs; keep inconclusive results.

Run from the repository root. Uses GET rather than assuming HEAD is supported.
Does not download models or datasets; response bodies are capped at 128 KiB.
"""
import argparse
import concurrent.futures
import datetime
import json
import re
import ssl
import threading
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from urllib.parse import urldefrag, urlsplit
from link_utils import ROOT, Destinations, links_in, markdown_files


def collect():
    sources = defaultdict(set)
    for path in markdown_files():
        for link in links_in(path):
            if urlsplit(link).scheme in {'http','https'}:
                sources[link].add(str(path.relative_to(ROOT)))
    for path in sorted((ROOT / 'data').glob('resources-*.json')):
        for row in json.loads(path.read_text()):
            sources[row['url']].add(f"{path.relative_to(ROOT)}:{row['id']}")
    config = ROOT / 'mkdocs.yml'
    if config.exists():
        for url in re.findall(r'^\s*-\s*(https?://\S+)\s*$', config.read_text(), re.M):
            sources[url].add('mkdocs.yml')
    for path in sorted((ROOT / 'site').rglob('*.html')):
        parser = Destinations()
        parser.feed(path.read_text(encoding='utf-8'))
        for link in parser.links:
            if urlsplit(link).scheme in {'http', 'https'}:
                sources[link].add(str(path.relative_to(ROOT)))
    return sources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--timeout', type=int, default=20)
    parser.add_argument('--retry-unresolved', action='store_true')
    args = parser.parse_args()
    sources = collect()
    previous = {}
    output = ROOT / 'data/link-check.json'
    if args.retry_unresolved and output.exists():
        previous = {r['url']: r for r in json.loads(output.read_text())['results']
                    if r['status'] in {'ok','local-preview'}}
    try:
        import certifi
        context = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        context = ssl.create_default_context()
    locks = {urlsplit(url).netloc: threading.Semaphore(2) for url in sources}

    def check(url):
        base, fragment = urldefrag(url)
        row = dict(url=url, sources=sorted(sources[url]), checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
        if urlsplit(url).hostname in {'127.0.0.1','localhost'}:
            row.update(status='local-preview', note='Local preview URL; not a public web resource')
            return row
        if url in previous:
            old = previous[url].copy()
            old['sources'] = row['sources']
            return old
        request = urllib.request.Request(base, headers={'User-Agent':'Mozilla/5.0 (compatible; AIAtlasLinkAudit/1.0)', 'Accept':'text/html,application/pdf,*/*'})
        try:
            with locks[urlsplit(url).netloc]:
                with urllib.request.urlopen(request, timeout=args.timeout, context=context) as response:
                    body = response.read(131072).decode('utf-8', errors='replace')
                    row.update(http_status=response.status, final_url=response.url, status='ok')
                    lower = body.lower()
                    # Avoid claiming anti-bot or soft-error pages are readable.
                    if '<title>just a moment' in lower or 'checking your browser before accessing' in lower:
                        row.update(status='restricted', note='Challenge page returned instead of resource')
                    elif '<title>404' in lower or '<title>page not found' in lower:
                        row.update(status='broken', note='Soft 404 page')
                    if fragment:
                        row['fragment_note'] = 'External page fragment not guaranteed by HTTP check; review original page'
        except urllib.error.HTTPError as exc:
            row.update(http_status=exc.code, status='broken' if exc.code in {404,410} else 'restricted' if exc.code in {401,403,429} else 'unresolved', note=str(exc))
        except Exception as exc:
            row.update(status='unresolved', note=f'{type(exc).__name__}: {exc}')
        return row

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(check, sorted(sources)))
    report = dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  scope='Markdown/image destinations, curated resource URLs, configured scripts and built HTML href/src when site exists; capped GET; external fragments need separate review',
                  counts=dict(Counter(r['status'] for r in results)), results=results)
    output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report['counts'], ensure_ascii=False))
    for row in results:
        if row['status'] not in {'ok','local-preview'}:
            print(row['status'], row.get('http_status',''), row['url'], row.get('note',''))
    if any(row['status'] == 'broken' for row in results):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
