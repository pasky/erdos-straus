"""review_fz1_tuples.py (R226): naive exact enumeration of the k = 1 Case B tuples (B^{k=1}) of FF_STERILE_SMALL §6
   m'wC = T^s + v, w + C = g'v, m', g', w, C monic, T not dividing m' g' w C v,
and test of Lemma 7.1 (i)-(ii) on every tuple found.
Enumeration: all monic T-free (m', g', w) with deg m' + deg w + deg g' <= D; E := m'g'w - 1 (L' = m'g');
for every s <= SMAX with E | g'T^s + w (iterated T^s mod E) put C := (g'T^s + w)/E and accept iff the tuple equations hold
with v := m'wC - T^s (checked directly). Completeness: every tuple satisfies EC = g'T^s + w (pure algebra:
EC = g'm'wC - C = g'(T^s + v) - C = g'T^s + w), and a tuple with a <= b has z + a + y <= s (y + t = b, Lemma 7.1(i)
— which is itself TESTED here: the enumeration does not assume deg(m'wC) = s; a <= b is only used for the completeness
claim, which we therefore state as: complete for patterns with a <= b and s <= D).
Output per pattern (s, a, z, y, t) with a <= b (a = b: both orders): total count and count with E(0) not in F_3 (char 3).
usage: review_fz1_tuples.py q D SMAX [outfile]"""
import sys, itertools
sys.path.insert(0, 'scripts')
from review_fz1_ff import GF

def main():
    q, D, SMAX = map(int, sys.argv[1:4]); out = sys.argv[4] if len(sys.argv) > 4 else None
    F = GF(q)
    mon = {d: list(F.polys(d, monic=True, Tfree=True)) for d in range(D + 1)}
    counts = {}; ntup = 0; fails = []
    F3 = F.F3star
    for z in range(D + 1):
        for a in range(D + 1 - z):
            for y in range(D + 1 - z - a):
                for m in mon[z]:
                    for g in mon[y]:
                        L = F.pmul(m, g)
                        for w in mon[a]:
                            E = F.psub(F.pmul(L, w), F.const(1))
                            if not E or F.deg(E) < 1: continue      # E = 1 (only if L'w = 2: impossible, monic) / E const
                            # iterate r = T^s mod E
                            r = F.pdivmod(F.T(1), E)[1]
                            for s in range(1, SMAX + 1):
                                if s > 1: r = F.pdivmod(F.pmul(r, F.T(1)), E)[1]
                                if F.padd(F.pmul(g, r), w) and F.pdivmod(F.padd(F.pmul(g, r), w), E)[1]: continue
                                num = F.padd(F.pmul(g, F.T(s)), w)
                                C, rem = F.pdivmod(num, E)
                                if rem or not C or C[-1] != 1 or C[0] == 0: continue
                                v = F.psub(F.pmul(F.pmul(m, w), C), F.T(s))
                                if not v or v[0] == 0: continue
                                if F.padd(w, C) != F.pmul(g, v): continue
                                b = F.deg(C); t = F.deg(v)
                                ntup += 1
                                # ---- Lemma 7.1 checks ----
                                chk = []
                                chk.append(('deg m\'wC = s', z + a + b == s))
                                chk.append(('y+t = max(a,b)', y + t == max(a, b)))
                                chk.append(('Ev = T^s + m\'w^2', F.pmul(E, v) == F.padd(F.T(s), F.pmul(m, F.pmul(w, w)))))
                                Ep = F.psub(F.pmul(L, C), F.const(1))
                                chk.append(('EE\' = 1 + T^s L\'g\'', F.pmul(E, Ep) == F.padd(F.const(1), F.pmul(F.T(s), F.pmul(L, g)))))
                                chk.append(('EC = g\'T^s + w', F.pmul(E, C) == num))
                                chk.append(('C = -w mod v', not F.pdivmod(F.padd(C, w), v)[1]))
                                chk.append(('w unit mod v', F.deg(F.pgcd(w, v)) == 0))
                                for D_ in (m, w, C, F.pmul(m, w), F.pmul(w, C), F.pmul(m, C)):
                                    if F.deg(D_) >= 1:
                                        chk.append(('v = -T^s mod D', F.pdivmod(F.padd(v, F.T(s)), D_)[1] == ()))
                                chk.append(('lc v = lc(w+C)', v[-1] == F.padd(w, C)[-1]))
                                for nm, ok in chk:
                                    if not ok: fails.append((nm, s, m, g, w, C))
                                if a <= b and s <= D:
                                    key = (s, a, z, y, t)
                                    c = counts.setdefault(key, [0, 0])
                                    c[0] += 1
                                    if F3 is not None and E[0] not in F3: c[1] += 1
    print(f"q={q} D={D} SMAX={SMAX}: tuples found {ntup}; Lemma 7.1 check failures: {len(fails)}")
    for f in fails[:10]: print("  FAIL", f)
    tot = {}
    for (s, *_), c in counts.items():
        tt = tot.setdefault(s, [0, 0]); tt[0] += c[0]; tt[1] += c[1]
    print("  per s (a<=b, complete for s<=D): " + " ".join(f"s={s}:{tot[s][0]}" + (f"/{tot[s][1]}" if F3 else "") for s in sorted(tot)))
    if out:
        with open(out, 'w') as fo:
            for k in sorted(counts): fo.write("%d %d %d %d %d %d %d\n" % (*k, *counts[k]))
    sys.exit(1 if fails else 0)

main()
