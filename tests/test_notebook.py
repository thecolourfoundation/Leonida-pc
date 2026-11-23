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


if __name__ == '__main__':
    unittest.main()
