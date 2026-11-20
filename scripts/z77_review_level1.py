"""Opus review (z77): independent level-1 union census (P and Q, K=k=1) by (a,c,d) triple enumeration."""
import sys
def census(r):
    W = r; cent = set(); nP = nQ = 0
    T = (r + 1) // 2           # P: acd <= (r/e+1)/2 <= (r+1)/2
    for a in range(1, T + 1):
        for c in range(1, T // a + 1):
            for d in range(1, T // (a * c) + 1):
                f = 4*a*c*d - 1
                if (r*c + a) % f: continue
                b = (r*c + a)//f
                if b < a or (a + b) % c: continue
                e = (a + b)//c
                if 4*a*b*d != r + e: continue
                if a % r == 0 or b % r == 0 or c % r == 0 or d % r == 0: continue
                nP += 1; x = (-a*pow(b, -1, r)) % r; cent.add(x); cent.add(pow(x, -1, r))
    TQ = (2*r + 2)//4          # Q: f = 4acd - F in [1, F+2]
    for a in range(1, TQ + 1):
        for c in range(1, TQ // a + 1):
            for d in range(1, TQ // (a*c) + 1):
                f = 4*a*c*d - r
                if f < 1: continue
                if (4*a*a*d + 1) % f or (a*r + c) % f: continue
                e = (4*a*a*d + 1)//f; b = (a*r + c)//f
                if b < a or a + b != c*e or 4*a*b*d != e*r + 1: continue
                if c % r == 0 or e % r == 0: continue
                nQ += 1; x = (-a*pow(b, -1, r)) % r; cent.add(x); cent.add(pow(x, -1, r))
    sq = {h*h % r for h in range(1, r)}
    return nP, nQ, len([x for x in cent if x not in sq])
for r in map(int, sys.argv[1:]):
    print(r, *census(r), flush=True)
