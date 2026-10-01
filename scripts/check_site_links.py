"""Check every local href/src and fragment in the built HTML site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1] / 'site'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links = set(), []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {'id','name'} and value:
                self.ids.add(value)
            if key in {'href','src'} and value:
                self.links.append(value)


def main():
    if not ROOT.exists():
        raise SystemExit('Build the site first: python -m mkdocs build --strict')
    pages = {p.resolve(): Page(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')}
    errors, checked = [], 0
    for source, page in pages.items():
        for destination in page.links:
            parts = urlsplit(destination)
            if parts.scheme or parts.netloc:
                continue
            # Search UI uses a bare # to target the current page.
            path = unquote(parts.path)
            if path.startswith('/'):
                target = (ROOT / path.lstrip('/')).resolve()
            else:
                target = (source.parent / path).resolve() if path else source
            if target.is_dir():
                target = target / 'index.html'
            checked += 1
            if not target.exists():
                errors.append(f'{source.relative_to(ROOT)} -> {destination}: missing file')
            elif parts.fragment and target.suffix == '.html':
                other = pages.get(target)
                if other and unquote(parts.fragment) not in other.ids:
                    errors.append(f'{source.relative_to(ROOT)} -> {destination}: missing anchor')
    print(f'{len(pages)} HTML pages; {checked} local links and asset references')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: built site destinations and anchors')
    return 0


if __name__ == '__main__':
    sys.exit(main())
