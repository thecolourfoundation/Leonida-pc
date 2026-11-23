"""Sanity checks for the Colab notebook (cannot execute it offline)."""
import json, os, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Notebook(unittest.TestCase):
    def setUp(self):
        self.raw = open(os.path.join(ROOT, 'tools', 'colab', 'leonida_bringup.ipynb')).read()
        self.nb = json.loads(self.raw)

    def test_structure(self):
        self.assertEqual(self.nb['nbformat'], 4)
        self.assertTrue(any(c['cell_type'] == 'code' for c in self.nb['cells']))

    def test_safety(self):
        self.assertIn('--no-checkout', self.raw)
        self.assertIn('core.hooksPath=/dev/null', self.raw)
        self.assertNotIn('ghp_', self.raw)
        self.assertNotIn('GITHUB_TOKEN', self.raw)
        self.assertNotIn('ALLOW_UNVERIFIED', self.raw)



class PublishNotebook(unittest.TestCase):
    def test_token_never_printed_or_embedded(self):
        raw = open(os.path.join(ROOT, 'tools', 'colab', 'publish_to_github.ipynb')).read()
        json.loads(raw)
        for bad in ('ghp_', 'github_pat_', 'print(os.environ', "print(os.environ['GH_TOKEN']", 'echo $GH_TOKEN', 'x-access-token'):
            self.assertNotIn(bad, raw)
        self.assertIn('getpass', raw); self.assertIn('userdata', raw); self.assertIn('--dry-run', raw)



class ShipItCell(unittest.TestCase):
    def test_cell_parses_and_never_prints_token(self):
        import ast
        with open(os.path.join(ROOT, 'tools', 'colab', 'ship_it_cell.txt')) as fh:
            src = fh.read()
        ast.parse(src)
        for bad in ('print(os.environ', 'ghp_', 'github_pat_', 'x-access-token', 'echo $GH_TOKEN'):
            self.assertNotIn(bad, src)
        self.assertIn("'--dry-run'", src); self.assertLess(src.index("'--dry-run'"), src.index("'--yes'"))


if __name__ == '__main__':
    unittest.main()
