#!/usr/bin/env python3
"""Bounded static audit and exact arithmetic checks; NOT a Lean verification."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import re
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--oai-root', type=Path, default=Path('/home/pasky/projects/math/oai-math'))
ROOT = parser.parse_args().oai_root
OUT = Path('data/z48_oai003')
OUT.mkdir(parents=True, exist_ok=True)


def uncomment(s):
    out, i, depth = [], 0, 0
    while i < len(s):
        if s[i:i+2] == '/-':
            depth += 1
            i += 2
        elif depth and s[i:i+2] == '-/':
            depth -= 1
            i += 2
        elif depth:
            out.append('\n' if s[i] == '\n' else ' ')
            i += 1
        elif s[i:i+2] == '--':
            j = s.find('\n', i)
            i = len(s) if j < 0 else j
        else:
            out.append(s[i])
            i += 1
    return ''.join(out)


def closure(module):
    todo, seen, missing, hits, external = [module], set(), [], [], set()
    while todo:
        mod = todo.pop()
        if mod in seen:
            continue
        seen.add(mod)
        path = ROOT / 'lean' / (mod.replace('.', '/') + '.lean')
        if not path.is_file():
            missing.append(mod)
            continue
        text = uncomment(path.read_text())
        for n, line in enumerate(text.splitlines(), 1):
            if re.search(r'\b(sorry|admit|sorryAx|axiom)\b', line):
                hits.append([mod, n, line.strip()])
        for line in text.splitlines():
            if line.startswith('import '):
                for imported in line.split()[1:]:
                    if imported.startswith('OAI.'):
                        todo.append(imported)
                    else:
                        external.add(imported)
    return {'modules': len(seen), 'missing': missing, 'lexical_hits': hits,
            'unscanned_external_imports': sorted(external)}


def add(*ps):
    out = Counter()
    for p in ps:
        for k, v in p.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}


def mul(p, q):
    out = Counter()
    for (a, b), c in p.items():
        for (d, e), f in q.items():
            out[a+d, b+e] += c*f
    return {k: v for k, v in out.items() if v}


def c(n):
    return {(0, 0): F(n)}


def scale(n, p):
    return mul(c(n), p)


# Symbolic identity in y and delta from September source, endpoint certificate.
y, d = {(1, 0): F(1)}, {(0, 1): F(1)}
y2, y3, d2 = mul(y, y), mul(mul(y, y), y), mul(d, d)
v = add(c(51), scale(41, y))
poly = add(scale(10, add(c(37), scale(34, y))),
           scale(-8, mul(add(c(237), scale(377, y), scale(26, y2)), d)),
           scale(48, mul(add(c(51), scale(131, y), scale(94, y2), scale(32, y3)), d2)))
a = add(scale(4, mul(v, d)), c(-79))
rhs = add(mul(add(c(3), scale(5, y)), add(mul(a, a), c(49))),
          scale(4, mul(y, add(scale(4, mul(mul(v, d),
              add(mul(mul(add(c(1), scale(3, y)), add(c(15), scale(32, y))), d),
                  c(9), scale(-13, y)))), c(265), scale(3485, y)))))
# Derive that same quadratic from E(h), R_* and J, rather than only
# checking the sum-of-squares expansion copied from the source.
x = add(c(F(1, 2)), scale(-1, y))
Dx = add(c(3), scale(F(-17, 9), x))
Px = add(c(2), scale(F(-26, 9), x), scale(F(8, 9), mul(x, x)))
alpha_minus_d = add(c(F(5, 6)), scale(-1, d))
J = add(mul(alpha_minus_d, Dx), mul(d, Px))
h = F(13, 16)
negative_E_times_J = add(scale(F(1, 48), J),
    mul(mul(J, d), add(c(h-F(2, 3)), scale(F(-1, 6), x))),
    scale(-h/2, mul(mul(alpha_minus_d, d), Px)))
assert scale(10368, negative_E_times_J) == poly
assert mul(v, poly) == rhs
assert F(49, 440640) > F(1, 10000)
assert F(17, 48)/2 + F(1, 8)/12 == F(3, 16)

# A legal pair with a positive BM term, no hit, and NO nonreal characters.
p, u, w = 61, 2, 3
q, a = 4*u*w, -(u+w)
assert gcd(u, w) == 1 and (u+w) % 2 and q-u-w <= p
assert pow((-q) % p, (p-1)//2, p) == p-1
assert p % q != a % q
units = [x for x in range(q) if gcd(x, q) == 1]
assert all(x*x % q == 1 for x in units)
# All character values have square 1, so all characters are real.
nonreal = 0
pair_bm = F(2, len(units))
other_real = F(int(p % q == a % q)) - pair_bm
assert other_real == -F(1, 4)

# Finite one-sided counterexample: ordered pair count R(409)=0.
p0 = 409
pairs = []
for u in range(1, (p0+1)//3 + 1):
    for w in range(1, (p0+u)//(4*u-1) + 1):
        if gcd(u, w) == 1 and (u+w) % 2:
            pairs.append((u, w))
hits = sum((p0+u+w) % (4*u*w) == 0 for u, w in pairs)
assert hits == 0
bm = sum((F(1)-(-1 if pow((-4*u*w) % p0, (p0-1)//2, p0) == p0-1 else 1)) /
         sum(gcd(j, 4*u*w) == 1 for j in range(1, 4*u*w+1)) for u, w in pairs)
assert bm > 0

report = {'oai_commit': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip(),
          'audit_kind': 'static local OAI import closure, not compiler/kernel audit',
          'closures': {}, 'endpoint_polynomial_identity': True,
          'endpoint_margin': str(F(49, 440640)),
          'other_real_counterexample': {'p': 61, 'u': 2, 'v': 3, 'q': 24, 'BM': str(pair_bm), 'nonreal': nonreal, 'other_real': str(other_real)},
          'finite_lower_tail_control': {'p': p0, 'R': hits, 'M_BM_exact': str(bm), 'M_BM': float(bm)},
          'sources': {}}
for name in ['DirichletSevenEighths', 'QuasiRiemannHypothesis', 'HeckeSevenEighths', 'SiegelZeros']:
    cfg = json.loads((ROOT/'lean/ComparatorChallenges'/f'{name}.json').read_text())
    report['closures'][name] = {'config': cfg, **closure(cfg['solution_module'])}
for dirname, stem in [('The-Quasi-Riemann-Hypothesis-September-30-2026', 'paper'),
                      ('The-Quasi-Riemann-Hypothesis-October-5-2026', 'paper2'),
                      ('Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026', 'paper')]:
    for rel in [f'preprints/{dirname}/{stem}.pdf', f'preprints/{dirname}/build/{stem}.tex']:
        path = ROOT/rel
        report['sources'][rel] = {'sha256': sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
(OUT/'checks.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in ['sources', 'closures']}, indent=2))
for key, value in report['closures'].items():
    print(key, value['modules'], 'modules;', len(value['missing']), 'missing;', len(value['lexical_hits']), 'lexical hits')
assert all(not r['missing'] and not r['lexical_hits'] for r in report['closures'].values())
