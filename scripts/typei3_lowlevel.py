"""O72 (POINTWISE_TYPEI3 Prop 5.3): levels with alpha+2*gamma in {5,6} at the sign point x̂_w, w = 9 (16).
There 4*c~ = 2^(6-alpha-2gamma)*c_o is an integer, so the Vieta descent of Lemma 5.1 stays integral and every
divisor pair (F_i, F_{i+1}) with e-F = 4c~K delta lies on the chain from (K_0,F_0) = (delta, 1):
   F_{i+1} = F_i + 4c~ K_i delta,  K_{i+1} = F_{i+1} delta + K_i.
A certificate needs: delta odd; v_2(K_i) = alpha+2gamma-2 exactly (K = 2^(t-4) k); and the certificate
divisor (F_i or F_{i+1}) = -w (mod 2^t), the other = -w^{-1} (mod 2^t), t = 2+alpha+gamma.
This only depends on (4c~ mod 2^M, delta mod 2^M, i mod period).  We enumerate all residues and report
whether any admissible (i) exists.  Usage: typei3_lowlevel.py w [seven]  (w taken mod 2^M; with 'seven', c_o ranges over odd powers of 7 mod 2^M,
as forced by Prop 5.3)"""
import sys
M = 10
MOD = 1 << M
w = int(sys.argv[1]) if len(sys.argv) > 1 else 9
winv = pow(w, -1, MOD)

def v2(x):
    x %= MOD
    if x == 0:
        return M
    e = 0
    while x % 2 == 0:
        x //= 2; e += 1
    return e

levels = [(a, g) for a in range(0, 7) for g in range(0, 4) if a + 2 * g in (5, 6) and a + g >= 3]
total_hits = 0
for (al, ga) in levels:
    t = 2 + al + ga; tm = 1 << t
    s = al + 2 * ga
    hits = 0
    cos = sorted({pow(7, a, MOD) for a in range(1, 2 * MOD, 2)}) if 'seven' in sys.argv else range(1, MOD, 2)
    for co in cos:
        fc = ((1 << (6 - s)) * co) % MOD  # 4 c~
        for de in range(1, MOD, 2):
            F, K = 1, de
            Fn = (F + fc * K * de) % MOD
            seen = set()
            while (F, K) not in seen:
                seen.add((F, K))
                if v2(K) == s - 2:
                    for (A, B) in ((F, Fn), (Fn, F)):
                        if (A + w) % tm == 0 and (B * w + 1) % tm == 0:
                            hits += 1
                # step
                Kn = (Fn * de + K) % MOD
                F, K = Fn, Kn
                Fn = (F + fc * K * de) % MOD
    total_hits += hits
    print(f'level alpha={al} gamma={ga} (t={t}): admissible residue/index combinations: {hits}')
print('total', total_hits)
