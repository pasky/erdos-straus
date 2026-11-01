# z53 HCSHIFTS (Lemma C check): endpoint lines at primes q = 7 (mod 8): miss rate when the line is unconfinable
# ((p/q) = -1, so -1 lies in <p mod q>) versus confinable ((p/q) = +1).  Also: fraction of unconfinable lines that are
# nevertheless missed ("anatomy deficit"), and the level lines at the same q (always confinable).
import sys
C128 = [x for x in range(4, 129) if x % 4 == 0 or x % 8 == 7]
Q = [7, 23, 31, 47, 71, 79, 103, 127]
for fn in sys.argv[1:]:
    st = {q: [0, 0, 0, 0] for q in Q}   # [n(+1), miss(+1), n(-1), miss(-1)]
    for line in open(fn):
        if line.startswith('#'): continue
        f = line.split(); p = int(f[0]); mE = int(f[11], 16)
        for q in Q:
            i = C128.index(q); leg = pow(p, (q - 1) // 2, q)
            j = 0 if leg == 1 else 2
            st[q][j] += 1
            if not (mE >> i & 1): st[q][j + 1] += 1
    print("==", fn)
    for q in Q:
        a, b, c, d = st[q]
        print(f"  q={q:3d}: P(miss | (p/q)=+1, confinable) = {b/a:.3f}   P(miss | (p/q)=-1, unconfinable) = {d/c:.3f}")
