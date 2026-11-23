"""Static checks on .github/workflows: every `make X` step must exist in the Makefile; no risky triggers/secrets."""
import glob, os, re, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Workflows(unittest.TestCase):
    def setUp(self):
        self.files = sorted(glob.glob(os.path.join(ROOT, '.github', 'workflows', '*.yml')))
        self.makefile = open(os.path.join(ROOT, 'Makefile')).read()

    def test_workflows_exist(self):
        self.assertTrue(self.files)

    def test_make_targets_exist(self):
        targets = set(re.findall(r'^([a-z-]+):', self.makefile, re.M))
        for f in self.files:
            for t in re.findall(r'run:\s*make\s+([a-z-]+)', open(f).read()):
                with self.subTest(file=os.path.basename(f), target=t):
                    self.assertIn(t, targets)

    def test_hygiene(self):
        for f in self.files:
            txt = open(f).read()
            with self.subTest(file=os.path.basename(f)):
                self.assertNotIn('\t', txt)
                self.assertIn('permissions:\n  contents: read', txt)
                self.assertNotIn('pull_request_target', txt)
                self.assertNotIn('secrets.', txt)
                for u in re.findall(r'uses:\s*(\S+)', txt):
                    self.assertIn('@', u)

    def test_makefile_recipes_use_tabs(self):
        for line in self.makefile.splitlines():
            if line.startswith('    '):
                self.fail('space-indented recipe line: ' + line)


if __name__ == '__main__':
    unittest.main()
