"""Z0524 summary: reads the per-n failure list written by z52d_p2_NC0_Z0524.c (/tmp/z52d_big/G1/Z0524_perN_fails.txt)
and, for each (q,r), counts failing n among the LOCALLY ADMISSIBLE n: gcd(n,q)=1 and 3n ≡ 4r (mod q) (needed when gcd(r,q)=1, 3∤q:
mod q, 1/x≡1/r for x≡r, so 4/n ≡ 3/r). Also reports failing n for r=0 / gcd(r,q)>1 cases."""
import sys, math, collections
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
path = "/tmp/z52d_big/G1/Z0524_perN_fails.txt"
fails = collections.defaultdict(list)
for line in open(path):
    n, qr, rr = line.split()
    q = int(qr[2:]); r = int(rr[2:])
    fails[(q, r)].append(int(n))
rows = []
for q in range(2, 13):
    for r in range(q):
        F = fails[(q, r)]
        if gcd_ := math.gcd(r, q) if r else q:
            pass
        g = math.gcd(r, q) if r else q
        if g == 1 and q % 3 != 0:
            inv3 = pow(3, -1, q)
            adm = [n for n in range(2, NMAX + 1) if math.gcd(n, q) == 1 and (3 * n - 4 * r) % q == 0]
            fs = set(F)
            fadm = [n for n in adm if n in fs]
            rows.append((q, r, "admissible", len(adm), len(fadm), fadm[:6]))
        else:
            rows.append((q, r, "inadmissible-or-gcd", 0, len(F), F[:6]))
for row in rows:
    q, r, kind, na, nf, ex = row
    print(f"q={q:2d} r={r:2d} {kind:20s} admissible_n={na:6d} failing_among_admissible={nf:6d} example_fails={ex}")
