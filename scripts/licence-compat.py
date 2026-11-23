#!/usr/bin/env python3
"""Pairwise licence-combination triage from reports/licence-matrix.csv. Not legal advice.
Codes: OK same/compatible family | ONEWAY permissive code may go into the copyleft work (combined work follows the copyleft)
       X incompatible as one combined work | ISO restricted/non-commercial: isolate, no combined artifact | ? unknown"""
import csv, itertools, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, 'reports', 'licence-matrix.csv')


def load_rows():
    with open(CSV_PATH) as fh:
        allrows = list(csv.DictReader(fh))
    rows = [r for r in allrows if r['spdx_reported'] != 'UNKNOWN']
    unknown = [r['repo'] for r in allrows if r['spdx_reported'] == 'UNKNOWN']
    return rows, unknown


def fam(s):
    u = s.upper().strip()
    if u.startswith('CUSTOM') or 'NONCOMMERCIAL' in u or u.startswith('LICENSEREF'): return 'restricted'
    if u.startswith('GPL-2.0-ONLY'): return 'gpl2only'
    if u.startswith('GPL-2.0-OR-LATER') or u.startswith('GPL-2.0+'): return 'gpl2plus'
    if u.startswith('GPL-3.0'): return 'gpl3'
    if u == 'MIT': return 'mit'
    if u in ('MIT OR APACHE-2.0', 'APACHE-2.0 OR MIT'): return 'dual'
    return 'unknown'


def verdict(a, b):
    fa, fb = fam(a), fam(b)
    if 'restricted' in (fa, fb): return 'ISO', 'restricted/non-commercial terms add restrictions the other licence may not allow: keep isolated, no combined artifact'
    if 'unknown' in (fa, fb): return '?', 'read both licences'
    perm = {'mit', 'dual'}
    if fa in perm and fb in perm: return 'OK', 'both permissive; keep both notices'
    if fa in perm or fb in perm:
        p, g = (fa, fb) if fa in perm else (fb, fa)
        if p == 'dual' and g == 'gpl2only': return 'ONEWAY', 'use the MIT option (the Apache-2.0 option is not GPL-2.0-only compatible); combined work is GPL-2.0-only'
        return 'ONEWAY', f'permissive code may be included in the {g} work; keep notices; combined work follows the GPL side'
    if fa == fb: return 'OK', 'same licence family'
    s = {fa, fb}
    if s == {'gpl2only', 'gpl3'}: return 'X', 'GPL-2.0-only cannot be combined with GPL-3.x ("or-later" on the other side does not help)'
    if s == {'gpl2plus', 'gpl3'}: return 'OK', 'combined work under GPL-3.0'
    if s == {'gpl2only', 'gpl2plus'}: return 'OK', 'combined work under GPL-2.0-only'
    return '?', 'unclassified'


def main():
    rows, unknown = load_rows()
    names = [r['repo'] for r in rows]; lic = {r['repo']: r['spdx_reported'] for r in rows}
    print('Reported licences (file text NOT yet verified):')
    for r in rows:
        note = ' (ambiguous: confirm -only vs -or-later)' if r['spdx_reported'] in ('GPL-3.0', 'GPL-2.0') else ''
        print(f"  {r['repo']}: {r['spdx_reported']}{note}")
    print('  UNKNOWN (no licence reported): ' + ', '.join(unknown))
    print('\nMatrix (OK / ONEWAY / X / ISO / ?):')
    w = max(len(n) for n in names) + 1
    print(' ' * w + ' '.join(n[:6].ljust(6) for n in names))
    res = {}
    for x, y in itertools.combinations(names, 2): res[(x, y)] = res[(y, x)] = verdict(lic[x], lic[y])
    for x in names:
        print(x.ljust(w) + ' '.join(('-' if x == y else res[(x, y)][0]).ljust(6) for y in names))
    print('\nProblem pairs (X / ISO):')
    for (x, y), (c, t) in res.items():
        if x < y and c in ('X', 'ISO'): print(f'  {x} + {y}: {c}: {t}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
