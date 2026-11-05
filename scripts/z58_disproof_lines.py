# z58 DISPROOF §5.3: mass of the u-lines.  For primes p from an engine output file (exact R in col 9), compute
# N_u(p) := #{d | p + u : d = -1 (mod 4u), d >= 4u - 1} for u = 1..U (the ordered (★) solutions with first coordinate u;
# by the u <-> B symmetry the solutions with B = u are equinumerous), and report mean 2*N_u / mean R (share of R carried by
# the lines u and B = u; overlap u = B impossible for odd p), and P(N_u = 0).
# Run: uv run --with sympy python scripts/z58_disproof_lines.py FILE NPRIMES U
import sys
from sympy import divisors
fn, NP, U = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ps = []
for l in open(fn):
    if l.startswith('#'): continue
    f = l.split()
    if f[8] != '-': ps.append((int(f[0]), int(f[8])))
    if len(ps) >= NP: break
tot = sum(r for _, r in ps); S = [0] * (U + 1); Z = [0] * (U + 1)
for p, r in ps:
    for u in range(1, U + 1):
        c = sum(1 for d in divisors(p + u) if d % (4 * u) == 4 * u - 1)
        S[u] += 2 * c; Z[u] += (c == 0)
print(f"# {fn}: {len(ps)} primes, mean R = {tot/len(ps):.2f}")
acc = 0
for u in range(1, U + 1):
    acc += S[u]
    print(f"u={u:3d}: share of R in lines u and B=u: {S[u]/tot:.4f} (cumulative {acc/tot:.4f}); P(N_u=0) = {Z[u]/len(ps):.3f}")
