"""Offline checks for every local destination and resource record (Python 3.9+)."""
import json
import sys
from urllib.parse import urlsplit
from link_utils import ROOT, links_in, local_issue, markdown_files


def main():
    errors = []
    files = markdown_files()
    count = 0
    for path in files:
        for link in links_in(path):
            if urlsplit(link).scheme or urlsplit(link).netloc:
                continue
            count += 1
            issue = local_issue(path, link)
            if issue:
                errors.append(f'{path.relative_to(ROOT)} -> {link}: {issue}')
    topics = json.loads((ROOT / 'data/topics.json').read_text())
    slugs = {t['slug'] for t in topics}
    for topic in topics:
        if not (ROOT / 'docs/topics' / (topic['slug'] + '.md')).exists():
            errors.append(f"missing topic: {topic['slug']}")
        for prereq in topic['prerequisites']:
            if prereq not in slugs:
                errors.append(f'unknown prerequisite: {prereq}')
    records, ids = [], set()
    fields = {'id','title','url','kind','language','level','access','compute','why',
              'topics','checked_on','verification','evidence'}
    for path in sorted((ROOT / 'data').glob('resources-*.json')):
        for row in json.loads(path.read_text()):
            missing = fields - row.keys()
            if missing:
                errors.append(f"{path.name}: missing {missing}")
                continue
            if row['id'] in ids:
                errors.append(f"duplicate id: {row['id']}")
            ids.add(row['id'])
            if not set(row['topics']) <= slugs:
                errors.append(f"unknown topic: {row['id']}")
            if row['verification'] not in {'content-reviewed','search-verified'}:
                errors.append(f"invalid verification: {row['id']}")
            if urlsplit(row['url']).scheme not in {'https','http'}:
                errors.append(f"invalid resource URL: {row['id']}")
            records.append(row)
    covered = {s for r in records for s in r['topics']}
    for slug in slugs - covered:
        errors.append(f'no curated resources for {slug}')
    print(f'{len(files)} Markdown files; {count} local destinations; {len(records)} resource records')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: local files, filename case, Markdown anchors and resource metadata')
    return 0


if __name__ == '__main__':
    sys.exit(main())
