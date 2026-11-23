"""Tests for scripts/licence-compat.py (stdlib unittest, offline)."""
import contextlib, importlib.util, io, itertools, os, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'scripts', 'licence-compat.py')


def load():
    cwd = os.getcwd()
    spec = importlib.util.spec_from_file_location('licence_compat', SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(mod)
    finally:
        os.chdir(cwd)
    return mod, buf.getvalue()


class LicenceCompat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m, cls.import_output = load()

    def test_import_has_no_side_effects(self):
        self.assertEqual(self.import_output, '')

    def test_public_api(self):
        for name in ('fam', 'verdict', 'main'):
            self.assertTrue(hasattr(self.m, name), name)

    def test_verdict_table(self):
        cases = [
            ('GPL-2.0-only', 'GPL-3.0-or-later', 'X'),
            ('GPL-2.0-only', 'GPL-3.0', 'X'),
            ('GPL-3.0-or-later', 'GPL-3.0-or-later', 'OK'),
            ('GPL-2.0-or-later', 'GPL-3.0', 'OK'),
            ('MIT', 'GPL-3.0-or-later', 'ONEWAY'),
            ('MIT', 'GPL-2.0-only', 'ONEWAY'),
            ('MIT OR Apache-2.0', 'GPL-2.0-only', 'ONEWAY'),
            ('MIT', 'MIT OR Apache-2.0', 'OK'),
            ('CUSTOM-NONCOMMERCIAL', 'MIT', 'ISO'),
            ('CUSTOM-NONCOMMERCIAL', 'GPL-3.0-or-later', 'ISO'),
            ('BSD-3-Clause', 'MIT', '?'),
        ]
        for a, b, want in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.m.verdict(a, b)[0], want)

    def test_dual_licence_text_points_to_mit_option_for_gpl2only(self):
        self.assertIn('MIT option', self.m.verdict('MIT OR Apache-2.0', 'GPL-2.0-only')[1])

    def test_symmetry(self):
        sample = ['GPL-2.0-only', 'GPL-2.0-or-later', 'GPL-3.0', 'GPL-3.0-or-later', 'MIT',
                  'MIT OR Apache-2.0', 'CUSTOM-NONCOMMERCIAL', 'BSD-3-Clause']
        for a, b in itertools.combinations(sample, 2):
            with self.subTest(a=a, b=b):
                self.assertEqual(self.m.verdict(a, b)[0], self.m.verdict(b, a)[0])

    def test_manifest_and_licence_data_agree(self):
        manifest = {}
        for line in open(os.path.join(ROOT, 'scripts', 'repos.txt')):
            if line.strip() and not line.startswith('#'):
                n, _u, cat, st = line.rstrip('\n').split('|')
                manifest[n] = (cat, st)
        import csv
        rows = {r['repo']: r['spdx_reported'] for r in csv.DictReader(open(os.path.join(ROOT, 'reports', 'licence-matrix.csv')))}
        allowed = {'REMOTE-VERIFIED-BY-TEAM', 'DIRECTORY-LISTED', 'RESTRICTED-LICENCE', 'UNVERIFIED'}
        for n, (cat, st) in manifest.items():
            self.assertIn(st, allowed, n)
            if st == 'RESTRICTED-LICENCE':
                self.assertTrue(rows.get(n, '').startswith('CUSTOM'), n)
            if st == 'REMOTE-VERIFIED-BY-TEAM' and cat != 'directory':
                self.assertIn(n, rows, f'{n} verified but has no licence row')
        for n in rows:
            self.assertIn(n, manifest, f'{n} in licence CSV but not in manifest')

    def test_aligned_pairs_that_must_never_be_ok(self):
        rows = {r['repo']: r['spdx_reported'] for r in self.m.load_rows()[0]}
        for gpl3 in ('Leonida', 'ProjectReCity', 'SixNG'):
            self.assertEqual(self.m.verdict(rows['AnyPS5'], rows[gpl3])[0], 'X', gpl3)
        for other in rows:
            if other != 'Percy6Stars':
                self.assertEqual(self.m.verdict(rows['Percy6Stars'], rows[other])[0], 'ISO', other)

    def test_main_output_matches_committed_report_and_docs(self):
        buf = io.StringIO()
        cwd = os.getcwd()
        try:
            with contextlib.redirect_stdout(buf):
                rc = self.m.main()
        finally:
            os.chdir(cwd)
        self.assertEqual(rc, 0)
        committed = open(os.path.join(ROOT, 'reports', 'licence-compat-output.txt')).read()
        self.assertEqual(buf.getvalue(), committed)
        self.assertIn(committed.strip(), open(os.path.join(ROOT, 'LICENSES.md')).read())


if __name__ == '__main__':
    unittest.main()
