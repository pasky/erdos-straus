"""zi_slicecheck.py (O244): brute-force check of FF_INVERSION_CHECK Lemmas 2.2-2.4 / Thm 2.5 on the slices.
Enumerates, by brute force in a degree box (a1, b1 monic coprime, deg <= D; E = every divisor of a1 + b1 with lc in {1, lc(a1+b1)}),
all Case A data with g = 1 (maximal balls; g != 1 only shrinks balls) valid somewhere on the slices
  k >= 2: u = 1 + cT + ... (c != 0);   k = 1: u(0) not in F_3^* (q = 3^r)
with ball depth k + alpha <= DMAX. For each datum:
  * I4 mirror (E monic, deg a1 != deg b1): ball u == -1/E (mod T^{k+alpha}), validity of I4(a1, b1, E) re-checked from Prop 1.4;
  * Lemma 2.3: the Case B datum (s = alpha + v, L' = H/b1, g' = a1') is built and E | D, D monic, E == -1 mod L', g' | L',
    depth k + j <= k + alpha are checked; Lemma 2.4: E' = D/E gives a Case B ball containing the I4 ball;
  * optional independent check: the I4 ball lies inside a ball of the Case B census (bsE_famcount ... print; prime q, k = 2).
usage: PYTHONPATH=scripts uv run python scripts/zi_slicecheck.py q k D DMAX [CENSUS|all]
("all": every unit u, not only the sterility slices; L23_na counts Case A data with alpha + v < k, outside Lemma 2.3)"""
import sys, re
from zi_gf import GF, T, vT, show

q, k, D, DMAX = (int(x) for x in sys.argv[1:5])
CEN = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] != "all" else None
ALL = "all" in sys.argv[5:]   # drop the slice restriction: every unit u (all slice points x_u)
F = GF(q)
F3 = {1, F.N[1]}  # F_3^* = {1, -1} inside F_q (q = 3^r)


def in_slice(u):
    if ALL:
        return u[0] != 0
    if k >= 2:
        return u[0] == 1 and u[1] != 0
    return u[0] not in F3


def ballc(E, d):  # centre -E mod T^d
    E = list(E) + [0] * d
    return tuple(F.N[E[i]] for i in range(d))


def tfree(a):
    return list(a[vT(a):])


polys = [p for d in range(D + 1) for p in F.monics(d)]
caseA = {}   # (a1, b1, E) -> (ball, depth)
stats = dict(pairs=0, A=0, Anonmonic=0, I4=0, L23_fail=0, L23_ok=0, alpha0=0, I4_not_A=0, cen_in=0, cen_out=0)
I4balls = set(); Aballs = set()
for a1 in polys:
    for b1 in polys:
        if vT(a1) and vT(b1):
            continue
        if len(F.gcd(a1, b1)) != 1:
            continue
        s = F.add(a1, b1)
        if not s:
            continue
        stats["pairs"] += 1
        al = vT(a1) + vT(b1)
        if k + al > DMAX:
            continue
        ab_t = tfree(F.mul(a1, b1))
        for Em in F.divisors(F.factor(s)) if len(s) > 1 else [[1]]:
            for lcE in {1, s[-1]}:
                E = F.scal(lcE, Em)
                if not E or E[0] == 0:
                    continue
                if F.mod(F.add(E, [1]), ab_t):
                    continue  # E == -1 mod (a1 b1)'
                d = k + al
                u = ballc(E, d)
                if not in_slice(u):
                    continue
                stats["A"] += 1
                Aballs.add(u)
                if E[-1] != 1:
                    stats["Anonmonic"] += 1
                    continue
                if al == 0:
                    stats["alpha0"] += 1
                    continue
                if len(E) == 1:   # E = 1: the constant family of FE Prop 1.4(i), ball u == -1, self-mirror
                    stats["Econst"] = stats.get("Econst", 0) + 1
                    continue
                # ---- Lemma 2.3 (labels: T^alpha || A1, T not| B1)
                A1, B1 = (a1, b1) if vT(a1) else (b1, a1)
                Ep1 = F.add(E, [1]); v = vT(Ep1); H = Ep1[v:]
                ok = False
                if not (al + v >= k and v <= k + al):
                    stats["L23_na"] = stats.get("L23_na", 0) + 1
                    continue
                if True:
                    sB = al + v; Lp = F.exact(H, B1); gp = A1[vT(A1):]
                    j = (sB - k + 1) // 2; ga = (sB - k) // 2
                    Dp = F.add([1], F.mul(T(sB), F.mul(Lp, gp)))
                    Ep = F.exact(Dp, E)
                    ok = (Lp is not None and F.exact(Lp, gp) is not None and Ep is not None and Ep[-1] == 1 and Dp[-1] == 1
                          and not F.mod(Ep1, Lp) and 0 <= ga <= j and k + j <= d)
                    if ok:  # Lemma 2.4: swapped ball contains the I4 ball
                        uI = tuple(F.inv_series(list(u), d))
                        ok = ballc(Ep, k + j) == uI[:k + j] and not F.mod(F.add(Ep, [1]), Lp)
                stats["L23_ok" if ok else "L23_fail"] += 1
                if not ok and "-v" in sys.argv:
                    print("  L23 fail:", show(a1), show(b1), show(E), "alpha", al, "v", v, "Lp", Lp and show(Lp), "Ep", Ep and show(Ep))
                # ---- I4 mirror
                if len(a1) != len(b1):
                    stats["I4"] += 1
                    uI = tuple(F.inv_series(list(u), d))
                    # re-check Prop 1.4 validity at x_{uI}: T^{k+alpha} | uI*E + 1, (ab)' | E + 1
                    prod = F.add(F.mul(list(uI), E), [1])
                    assert (not prod or vT(prod) >= d) and not F.mod(F.add(E, [1]), ab_t)
                    I4balls.add(uI)
cen = {}
if CEN:
    for line in open(CEN):
        m = re.match(r"s=(\d+) .*E=\[([0-9,]*)\]", line)
        if not m: continue
        s_ = int(m.group(1)); E = [int(x) for x in m.group(2).split(",")]
        dB = (s_ + k - 2 + 1) // 2 + 1
        cen.setdefault(dB, set()).add(ballc(E, dB))
    for uI in I4balls:
        hit = any(uI[:dB] in S for dB, S in cen.items() if dB <= len(uI))
        stats["cen_in" if hit else "cen_out"] += 1
stats["I4_not_A"] = len(I4balls - Aballs)
stats["A_balls"] = len(Aballs); stats["I4_balls"] = len(I4balls)
print(f"q={q} k={k} D={D} DMAX={DMAX}: " + ", ".join(f"{a}={b}" for a, b in stats.items()))
