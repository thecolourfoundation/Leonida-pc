"""Dependency check: our original Python code must use only the standard library."""
import ast, os, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def py_files():
    for d in ('scripts', 'tests', 'tools'):
        for dp, _dn, fn in os.walk(os.path.join(ROOT, d)):
            for f in fn:
                if f.endswith('.py'):
                    yield os.path.join(dp, f)


class StdlibOnly(unittest.TestCase):
    def test_only_stdlib_imports(self):
        local = {'licence_compat'}
        for path in py_files():
            tree = ast.parse(open(path).read(), path)
            for node in ast.walk(tree):
                mods = []
                if isinstance(node, ast.Import):
                    mods = [a.name.split('.')[0] for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    mods = [node.module.split('.')[0]]
                for m in mods:
                    with self.subTest(file=os.path.relpath(path, ROOT), module=m):
                        self.assertTrue(m in sys.stdlib_module_names or m in local, m)


if __name__ == '__main__':
    unittest.main()
