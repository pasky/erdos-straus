# Z2741: Gross (trace-zero) lattice of the order Lambda_{d,m} = Z<u,v>, u^2=-d, v^2=-m, uv+vu=1  (QUATERNION_ES Lemma 1.2).
# Derivation (by hand, checked numerically below in quaternion arithmetic): trace-zero part of Lambda is
#   L = Z u + Z v + Z y,  y = 2uv - 1,  y^2 = 1 - 4dm,  u,v,y mutually orthogonal except u.v-cross term:
#   Q(b u + c v + k y) := nrd = d b^2 - b c + m c^2 + (4dm-1) k^2.   (binary of disc -(4dm-1)) (+) <4dm-1>.
# Here we (1) verify the formula with exact quaternion multiplication for small d,m, (2) test which primes
# p = 1 mod 24, p <= P, are represented by Q_{d,m} for d,m <= 20 (coverage), and (3) record discriminants.
import numpy as np, sys, itertools
from fractions import Fraction
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L

# (1) quaternion check: represent elements as 4-vectors over Q in basis 1,u,v,uv with relations u^2=-d, v^2=-m, vu=1-uv
def mul(x, y, d, m):
    # basis e0=1,e1=u,e2=v,e3=uv ; multiplication table computed from relations
    # products of basis: u*u=-d, v*v=-m, u*v=uv, v*u=1-uv, uv*u = u - u^2 v... compute via generic rules
    # represent element as dict over words in u,v; reduce with rules
    def red(w):  # w tuple of 'u','v' -> vector in basis (1,u,v,uv)
        # reduce using v u = 1 - u v, u u = -d, v v = -m
        vec = [Fraction(0)]*4
        stack = [(Fraction(1), w)]
        while stack:
            c, word = stack.pop()
            # find first occurrence pattern
            done = True
            for i in range(len(word)-1):
                a, b = word[i], word[i+1]
                if a == 'u' and b == 'u':
                    stack.append((c*(-d), word[:i]+word[i+2:])); done = False; break
                if a == 'v' and b == 'v':
                    stack.append((c*(-m), word[:i]+word[i+2:])); done = False; break
                if a == 'v' and b == 'u':
                    stack.append((c, word[:i]+('u','v')+word[i+2:]))  # placeholder replaced below
                    stack.pop()
                    stack.append((c, word[:i]+word[i+2:]))           # 1 part
                    stack.append((-c, word[:i]+('u','v')+word[i+2:]))  # -uv part
                    done = False; break
            if done:
                if word == (): vec[0] += c
                elif word == ('u',): vec[1] += c
                elif word == ('v',): vec[2] += c
                elif word == ('u','v'): vec[3] += c
                else: raise ValueError(word)
        return vec
    # expand x,y bilinearly over basis
    basis = [(), ('u',), ('v',), ('u','v')]
    out = [Fraction(0)]*4
    for i, a in enumerate(x):
        if a == 0: continue
        for j, b in enumerate(y):
            if b == 0: continue
            r = red(basis[i] + basis[j])
            for k in range(4): out[k] += a*b*r[k]
    return out

def nrd_quat(x, d, m):
    # reduced norm of a + b u + c v + e uv in B=(-d,-m)-type order: nrd = a^2 + d b^2 + m c^2 + dm e^2 - (cross from uv+vu=1) ...
    # use x * conj(x) with conj(u)=-u, conj(v)=-v, conj(uv)=vu = 1-uv  -> conj(uv) = v^- u^- = (-v)(-u)= vu
    conj = [x[0] + x[3]*0, -x[1], -x[2], None]
    # general: conj(a+bu+cv+euv) = a + tr-part...; compute via multiplication with conj basis: conj(uv)=vu = 1 - uv
    a, b, c, e = x
    cj = [a + e, -b, -c, -e]  # conj(x) = a + b*(-u) + c*(-v) + e*(vu) = a + e + (-b)u + (-c)v + (-e)uv
    p = mul(x, cj, d, m)
    assert p[1] == 0 and p[2] == 0 and p[3] == 0, p
    return p[0]

# verify Q on random elements of the trace-zero lattice L = {b u + c v + k y}
ok = True
for d, m in [(1,1),(2,3),(5,7),(3,11)]:
    for b, c, k in itertools.product(range(-2,3), repeat=3):
        y = [Fraction(-1), 0, 0, Fraction(2)]         # y = 2uv - 1
        x = [Fraction(k*-1), Fraction(b), Fraction(c), Fraction(2*k)]  # b u + c v + k(2uv-1)
        Qn = nrd_quat(x, d, m)
        Qf = d*b*b - b*c + m*c*c + (4*d*m-1)*k*k
        if Qn != Qf: ok = False
print("formula check (quaternion norm vs d b^2 - bc + m c^2 + (4dm-1)k^2):", ok)

P = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
D = int(sys.argv[2]) if len(sys.argv) > 2 else 20
pr = [p for p in L.primes_upto(P) if p % 24 == 1]
cover = {p: [] for p in pr}
rep_counts = {}
for d in range(1, D+1):
    for m in range(1, D+1):
        N = 4*d*m - 1
        B = int((4*P/ (4*d*m-1 + 0.0 + 1e-9))**0.5) + 60
        b = np.arange(-B, B+1)
        bb, cc, kk = np.meshgrid(b, b, np.arange(0, int((P/N)**0.5)+2), indexing='ij')
        val = d*bb*bb - bb*cc + m*cc*cc + N*kk*kk
        vals = val[(val > 0) & (val <= P)]
        rep = np.zeros(P+1, dtype=bool); rep[vals] = True
        hits = [p for p in pr if rep[p]]
        rep_counts[(d,m)] = len(hits)
        for p in hits: cover[p].append((d,m))
unc = [p for p in pr if not cover[p]]
print("primes p=1 mod 24, p<=%d: %d ; represented by some Q_{d,m} (d,m<=%d): %d ; uncovered: %d" % (P, len(pr), D, len(pr)-len(unc), len(unc)))
print("uncovered primes:", unc[:40])
best = sorted(rep_counts.items(), key=lambda kv: -kv[1])[:8]
print("most-representing (d,m):", best)
print("(d,m)=(1,1): disc -3 binary x <3>; fraction of pr represented:", round(rep_counts[(1,1)]/len(pr),3))
print("median fraction over (d,m):", round(float(np.median(list(rep_counts.values())))/len(pr),3))
