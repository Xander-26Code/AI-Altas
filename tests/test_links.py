import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from link_utils import ROOT, heading_ids, links_in, local_issue


class LinkTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(dir=ROOT)
        self.path = Path(self.directory.name)

    def tearDown(self):
        self.directory.cleanup()

    def test_extracts_image_html_and_balanced_url_ignores_code(self):
        source = self.path / 'page.md'
        source.write_text('![map](assets/map.svg)\n<a href="target.md">x</a>\n'
                          '[paper](https://example.org/book_(edition))\n'
                          '```md\n[example](missing.md)\n```\n'
                          '`[example](also-missing.md)`\n')
        self.assertEqual(set(links_in(source)), {'assets/map.svg','target.md','https://example.org/book_(edition)'})

    def test_anchors_preserve_unicode_and_inline_code(self):
        target = self.path / 'target.md'
        target.write_text('# 测试 `API`\n## More\n## More\n')
        self.assertEqual(heading_ids(target), {'测试-api','more','more-1'})
        self.assertIsNone(local_issue(target, '#测试-api'))
        self.assertEqual(local_issue(target, '#absent'), 'missing Markdown anchor')

    def test_missing_file_and_wrong_case(self):
        source = self.path / 'page.md'
        source.write_text('# Page\n')
        self.assertEqual(local_issue(source, 'missing.svg'), 'missing file')
        self.assertIsNone(local_issue(source, 'page.md'))
        self.assertIn(local_issue(source, 'PAGE.md'), {'missing file','filename case mismatch'})


if __name__ == '__main__':
    unittest.main()
