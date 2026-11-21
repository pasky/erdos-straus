"""Opus cross-lab review of notes/z80/EXTREME.md: independent checks of panel.csv.
* factorizations (product + proven primality of each factor), primality flag,
  first inert prime (least q with Kronecker(n,q)=-1);
* the 1024-window counts by a DIFFERENT method from z80_extreme_panel.py: per x,
  enumerate ordered factorizations x=a*c*d (Type I: g=4x-p must divide 4a^2d+1,
  e=(4a^2d+1)/g, b=ce-a, triple (acd,bcd,pabd)) and x=a*b*d (Type II: e=g must
  divide a+b, c=(a+b)/g, triple (abd,pacd,pbcd)); keep sorted x<=y<=z, verify
  4xyz=p(xy+xz+yz) exactly, dedupe as a set of triples.
Usage: python -B z80_xr_opus_panel.py [n ...]   (default: a fixed subset)"""
import csv, sys
from cypari2 import Pari
P = Pari(); P.allocatemem(256000000, silent=True); P.default('factor_proven', 1)

def windows(p, W=1024):
    S = [set(), set()]
    for x in range(p//4+1, min(p//4+W, 3*p//4)+1):
        g = 4*x-p
        for a in P.divisors(x).python():
            for d in P.divisors(x//a).python():
                c = x//a//d
                # Type I with this (a,c,d)
                m = 4*a*a*d+1
                if m % g == 0:
                    e = m//g; b = c*e-a
                    if b >= 1:
                        t = tuple(sorted((a*c*d, b*c*d, p*a*b*d)))
                        if t[0] == x: S[0].add(t)
                # Type II with x=a*b'*d where b'=c here (rename)
                b = c
                if (a+b) % g == 0:
                    cc = (a+b)//g
                    t = tuple(sorted((a*b*d, p*a*cc*d, p*b*cc*d)))
                    if t[0] == x: S[1].add(t)
    for i in (0, 1):
        for x, y, z in S[i]:
            assert 4*x*y*z == p*(x*y+x*z+y*z)
            assert sum(v % p == 0 for v in (x, y, z)) == i+1
    return len(S[0]), len(S[1])

rows = {int(r['n']): r for r in csv.DictReader(open('data/z80/extreme/panel.csv'))}
recs = [int(s) for s in open('data/z60/ms105/pseudo/A002189.txt').read().split()]
assert len(recs) == len(set(recs)) == 52
bad = 0
for n, r in rows.items():
    F = P.factor(n); qs = [int(q) for q in F[0]]; es = [int(e) for e in F[1]]
    fac = '*'.join(str(q) for q, e in zip(qs, es) for _ in range(e))
    ok = fac == r['factorization'] and all(P.isprime(q) for q in qs) and int(P.isprime(n)) == int(r['prime'])
    q = 2
    while int(P.kronecker(n, q)) != -1: q = int(P.nextprime(q+1))
    ok &= q == int(r['first_inert'])
    if not ok: bad += 1; print('MISMATCH', n)
print('panel rows', len(rows), 'factor/primality/first-inert mismatches', bad,
      'record primes', sum(int(rows[n]['prime']) for n in recs))
todo = list(map(int, sys.argv[1:])) or [13649154491558298803281, 1000000037842000358005081,
        1000000037842000358013481, 1000006402010247241, 1000006402010250601, 8089, 1009]
for n in todo:
    I, II = windows(n)
    print(n, 'windows I,II =', I, II, 'panel', rows[n]['I_x1024'], rows[n]['II_x1024'],
          'OK' if (I, II) == (int(rows[n]['I_x1024']), int(rows[n]['II_x1024'])) else 'MISMATCH', flush=True)
