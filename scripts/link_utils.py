"""Extract actual Markdown/HTML destinations, without scanning code examples."""
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def markdown_files():
    return sorted(list(ROOT.glob('*.md')) + list((ROOT / 'docs').rglob('*.md')))


def without_fences(text):
    return re.sub(r'^\s*(`{3,}|~{3,}).*?^\s*\1\s*$', '', text,
                  flags=re.M | re.S)


def strip_code(text):
    return re.sub(r'`[^`\n]+`', '', without_fences(text))


class Destinations(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {'href', 'src'} and value:
                self.links.append(value)


def links_in(path):
    text = strip_code(path.read_text(encoding='utf-8'))
    # Balanced parentheses in destinations such as URL_(edition).
    pattern = r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|(?:[^\s()]|\([^()]*\))+)\s*(?:"[^"]*")?\s*\)'
    links = [m.strip('<>') for m in re.findall(pattern, text)]
    links += re.findall(r'^\s*\[[^\]]+\]:\s*<?(\S+?)>?(?:\s+".*")?\s*$', text, re.M)
    parser = Destinations()
    parser.feed(text)
    return list(dict.fromkeys(links + parser.links))


def heading_ids(path):
    text = without_fences(path.read_text(encoding='utf-8')).replace('`', '')
    ids, seen = set(), {}
    for raw in re.findall(r'^#{1,6}\s+(.+?)(?:\s+#+)?$', text, re.M):
        raw = re.sub(r'!?\[([^\]]+)\]\([^)]+\)', r'\1', raw)
        raw = re.sub(r'<[^>]*>', '', raw).strip().lower()
        slug = re.sub(r'[^\w\-\s]', '', raw, flags=re.UNICODE).replace(' ', '-')
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        ids.add(slug if count == 0 else f'{slug}-{count}')
    ids.update(re.findall(r'(?:id|name)=["\']([^"\']+)', text))
    return ids


def local_issue(source, destination):
    parts = urlsplit(destination)
    if parts.scheme or parts.netloc:
        return None
    target = (source.parent / unquote(parts.path)).resolve() if parts.path else source
    if not target.is_relative_to(ROOT):
        return 'path outside repository'
    if not target.exists():
        return 'missing file'
    if target.is_dir():
        return None
    # GitHub is case-sensitive even when the developer's filesystem is not.
    current = ROOT
    for part in target.relative_to(ROOT).parts:
        if part not in {p.name for p in current.iterdir()}:
            return 'filename case mismatch'
        current = current / part
    if parts.fragment and target.suffix == '.md':
        if unquote(parts.fragment) not in heading_ids(target):
            return 'missing Markdown anchor'
    return None
