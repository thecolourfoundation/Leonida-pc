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


if __name__ == '__main__':
    unittest.main()
