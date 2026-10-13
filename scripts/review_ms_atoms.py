"""R197: falsification test of the §4.1 atoms (Type II (u,v,w): M = m*u*v*w - 1, v*n + u == 0 (mod M);
Type I (a,d,f): f | m*a^2*d + 1, n == -f (mod m*a*d)): no failing prime of m/p (own census lists) may lie in an
atom class.  usage: review_ms_atoms.py m failing_list_file MMAX"""
import sys

m, fl, MMAX = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
F = [int(x) for x in open(fl).read().split()]
hits = 0
natoms = 0
for u in range(1, MMAX):
    for v in range(1, MMAX // (m * u) + 2):
        for w in range(1, MMAX // (m * u * v) + 2):
            M = m * u * v * w - 1
            if M > MMAX or M < 2:
                continue
            natoms += 1
            for p in F:
                if (v * p + u) % M == 0:
                    hits += 1
                    print("TypeII atom hit", (u, v, w), p)
for a in range(1, MMAX):
    for d in range(1, MMAX // (m * a) + 1):
        K = m * a * d
        N = m * a * a * d + 1
        fs = [f for f in range(1, int(N ** .5) + 1) if N % f == 0]
        fs = set(fs + [N // f for f in fs])
        for f in fs:
            natoms += 1
            for p in F:
                if (p + f) % K == 0:
                    hits += 1
                    print("TypeI atom hit", (a, d, f), p)
print("m=%d atoms=%d failing primes=%d hits=%d" % (m, natoms, len(F), hits))
