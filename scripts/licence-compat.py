#!/usr/bin/env python3
"""Pairwise licence-combination triage from reports/licence-matrix.csv. Not legal advice.
Rules: GPL-2.0-only + GPL-3.x = INCOMPATIBLE (combined work); MIT/permissive -> one-way into GPL; same family OK."""
import csv, itertools, os
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
rows = [r for r in csv.DictReader(open('reports/licence-matrix.csv')) if r['spdx_reported'] not in ('', 'UNKNOWN')]
def fam(s):
    s = s.upper()
    if s.startswith('GPL-2.0-ONLY'): return 'gpl2only'
    if s.startswith('GPL-2.0-OR-LATER') or s.startswith('GPL-2.0+'): return 'gpl2plus'
    if s.startswith('GPL-3.0'): return 'gpl3'
    if s == 'MIT': return 'mit'
    return 'unknown'
def verdict(a, b):
    fa, fb = fam(a), fam(b)
    if 'unknown' in (fa, fb): return 'UNKNOWN - read both licences'
    if fa == fb: return 'OK - same licence family'
    if 'mit' in (fa, fb):
        other = b if fa == 'mit' else a
        return f'OK one-way - MIT may be included in the {other} work; keep MIT notice; combined work follows {other}'
    if {fa, fb} == {'gpl2only', 'gpl3'}: return 'INCOMPATIBLE as one combined work (GPL-2.0-only cannot be combined with GPL-3.x; "or-later" does not help)'
    if {fa, fb} == {'gpl2plus', 'gpl3'}: return 'OK - combined work under GPL-3.0'
    if {fa, fb} == {'gpl2only', 'gpl2plus'}: return 'OK - combined work under GPL-2.0-only'
    return 'UNKNOWN'
print('Reported licences (file text NOT yet verified):')
for r in rows: print(f"  {r['repo']}: {r['spdx_reported']}")
print('\nPairwise:')
for x, y in itertools.combinations(rows, 2):
    print(f"  {x['repo']} + {y['repo']}: {verdict(x['spdx_reported'], y['spdx_reported'])}")
