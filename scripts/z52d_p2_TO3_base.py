"""Pass-2 batch TO3: base table for all primes <= 2e5 (U4 counts from the repo's count-program output + PARI arithmetic).

Output: data/z52b/pass2/TO3/base_primes_2e5.tsv
Columns: p mod4 U D O minz maxx minx nx k1 k2 k3 h4p (h(-4p) or h(-p) for p=3 mod 4) hreal (h(p), p=1 mod 4)
         Rreal (log eps_p) L1real (=2 h R/sqrt p) L1m4p (=pi h(-4p)/(2 sqrt p)) leastQNR leastprimroot ord2 leg2 leg3 leg5 leg7
         cfper (period length of CF of sqrt p, p=1 mod 4)

Run: uv run --with numpy --with cypari2 python scripts/z52d_p2_TO3_base.py
"""
import numpy as np, math, os, sys
import cypari2
pari = cypari2.Pari()
pari.allocatemem(10**9)
R = 'data/z52b/raw/'
OUT = 'data/z52b/pass2/TO3/base_primes_2e5.tsv'
os.makedirs(os.path.dirname(OUT), exist_ok=True)

F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64)
PR = np.loadtxt(R + 'pr_20001_200000.txt', dtype=np.int64)
isp = np.array([bool(pari.isprime(int(x))) for x in F[:, 0]])
A = np.vstack([F[isp], PR])
A = A[np.argsort(A[:, 0])]
A = A[np.concatenate([[True], np.diff(A[:, 0]) > 0])]
assert len(A) == len(set(A[:, 0].tolist()))
print('primes', len(A), 'max', A[-1, 0], flush=True)

def leg(a, p):
    return int(pari.kronecker(a, p))

rows = []
for r in A:
    p = int(r[0])
    U, D, O, minz, maxx, minx, nx, k1, k2, k3 = [int(x) for x in (r[1], r[2], r[3], r[4], r[7], r[8], r[9], r[10], r[11], r[12])]
    if p == 2:
        h4p = -1; hreal = None; Rreal = None; L1real = None; L1m4p = float('nan')
    elif p % 4 == 1:
        h4p = int(pari.qfbclassno(-4 * p))
        hreal = int(pari.quadclassunit(p)[0])
        Rreal = float(pari.log(pari.quadunit(p)))  # log of fundamental unit of Q(sqrt p)
        L1real = 2 * hreal * Rreal / math.sqrt(p)  # class number formula (real quadratic, p=1 mod 4)
        L1m4p = math.pi * h4p / (2 * math.sqrt(p))  # L(1,chi_{-4p}) = 2 pi h/(w sqrt(4p)), w=2
    else:
        h4p = int(pari.quadclassunit(-p)[0])  # h(-p), fundamental disc -p for p=3 mod 4
        hreal = None; Rreal = None; L1real = None
        L1m4p = math.pi * h4p / math.sqrt(p)  # L(1,chi_{-p}) = pi h/sqrt p  (w=2)
    lq = 2
    while p > 2 and leg(lq, p) != -1:
        lq = int(pari.nextprime(lq + 1))  # nextprime(x) returns the least prime >= x
    if p == 2:
        g, o2 = -1, -1
    else:
        g = int(pari.znprimroot(p))
        o2 = int(pari.znorder(pari.Mod(2, p)))
    rows.append((p, p % 4, U, D, O, minz, maxx, minx, nx, k1, k2, k3, h4p,
                 hreal if hreal is not None else -1,
                 f'{Rreal:.10g}' if Rreal is not None else 'NA',
                 f'{L1real:.10g}' if L1real is not None else 'NA',
                 f'{L1m4p:.10g}', lq, g, o2, leg(2, p), leg(3, p), leg(5, p), leg(7, p)))
    if len(rows) % 2000 == 0:
        print(len(rows), flush=True)

with open(OUT, 'w') as f:
    f.write('p\tmod4\tU\tD\tO\tminz\tmaxx\tminx\tnx\tk1\tk2\tk3\th4p\threal\tRreal\tL1real\tL1m4p\tleastQNR\tleastprimroot\tord2\tleg2\tleg3\tleg5\tleg7\n')
    for t in rows:
        f.write('\t'.join(str(x) for x in t) + '\n')
print('wrote', OUT, len(rows))
