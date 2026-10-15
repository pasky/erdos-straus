"""review_r241_k2parity.py (R241) — naive brute force check of FF_ODD_ABSENCE Cor 1.7 (k >= 2 pattern parity law).
Reduced Case B form (FF_STERILE_PUSH Lemma 1.1(iii)): m' w1 C1 = T^{s'} + v1, w1 + C1 = T g' v1, m', w1, C1 monic,
T not dividing m' w1 C1 v1 (g' any monic; a superset of the (B) tuples). Enumerates all monic T-free (m', w1, C1) with
total degree <= s' + 1. Claim: z = deg m', t' = deg v1 satisfy z == t' == s' (mod 2), and deg(m'w1C1) = s'.
usage: review_r241_k2parity.py p r s'max"""
import sys, itertools
import flint
p, r, smax = map(int, sys.argv[1:4])
F = flint.fq_default_ctx(p, r, 'g'); R = flint.fq_default_poly_ctx(F)
g0 = F.gen(); ELS = []
for cs in itertools.product(range(p), repeat=r):
    e = F(0)
    for i, c in enumerate(cs):
        e += F(c) * g0 ** i
    ELS.append(e)
NZ = [e for e in ELS if e != 0]
T = R([0, 1])
MON = {}
def monics(d):
    if d not in MON:
        MON[d] = [R([1])] if d == 0 else [R(list(cs) + [F(1)]) for cs in itertools.product(NZ, *([ELS] * (d - 1)))]
    return MON[d]
tot = bad = degbad = 0
for sp in range(1, smax + 1):
    n = 0; pats = set()
    for d in range(0, sp + 2):
        for z in range(d + 1):
            for a in range(d - z + 1):
                b = d - z - a
                for m in monics(z):
                    for w in monics(a):
                        mw = m * w
                        for C in monics(b):
                            v = mw * C - T ** sp
                            if v == 0 or v(F(0)) == 0:
                                continue
                            G, rr = divmod(w + C, T * v)
                            if rr != 0 or G == 0 or G.leading_coefficient() != 1:
                                continue
                            n += 1; t = v.degree()
                            if d != sp:
                                degbad += 1
                            if not (z % 2 == t % 2 == sp % 2):
                                bad += 1; print('PARITY_FAIL', sp, m, w, C)
                            pats.add((a, b, z, G.degree(), t))
    tot += n
    print(f"# s'={sp} tuples={n} patterns={len(pats)} parity_fail={bad} deg_ne={degbad}", flush=True)
print(f'# total={tot} parity_fail={bad} deg_ne={degbad}')
