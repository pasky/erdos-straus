"""O72 (POINTWISE_TYPEI3 Prop 5.5): checks for level alpha+2gamma=6 at the sign point x̂_9.
Chain (F,H) from (1,1): F' = F + D*H, H' = F' + H, D = 7^a*delta^2 (a odd, delta odd).
(a) finite 2-adic check: for D mod 32 in {7,15,23,31} (all values of 7^a*delta^2 mod 32), over a full period of the
    chain mod 32, v_2(H_i) = 4 implies m = i+1 is an odd multiple of 3;
(b) polynomial identity: X_i - 2 = D*U_m^2 with (D+3) | U_m for m = 3,9,...,33 (X_i = F_i + F_{i+1});
(c) brute force: a in {1,3,5}, delta odd < 150, i < 40: whenever v_2(H_i) = 4, some odd prime q != 7 divides both
    H_i and (D+3), and F_i = F_{i+1} = 1 (mod q)   (so the sign condition F = -1 (mod q) fails)."""
import sympy as sp

# (a)
for D in (7, 15, 23, 31):
    F, H, i, seen, bad = 1, 1, 0, {}, 0
    while (F, H) not in seen:
        seen[(F, H)] = i
        if H % 32 == 16 and not ((i + 1) % 2 == 1 and (i + 1) % 3 == 0):
            bad += 1
        Fn = (F + D * H) % 32
        F, H, i = Fn, (Fn + H) % 32, i + 1
    print(f'(a) D={D} mod 32: period {i - seen[(F, H)]} (pre-period {seen[(F, H)]}), violations {bad}')

# (b)
x = sp.symbols('D')
F, H = sp.Integer(1), sp.Integer(1); Fs, Hs = [F], [H]
for _ in range(34):
    Fn = sp.expand(F + x * H); F, H = Fn, sp.expand(Fn + H); Fs.append(F); Hs.append(H)
for m in range(3, 34, 6):
    i = m - 1
    X = sp.expand(2 * Fs[i] + x * Hs[i])
    Q, R = sp.div(sp.expand(X - 2), x)
    assert R == 0
    q2, r2 = sp.div(Q, (x + 3) ** 2)
    print(f'(b) m={m}: (X-2)/D divisible by (D+3)^2: {r2 == 0}')

# (c)
viol = cases = 0
for a in (1, 3, 5):
    for de in range(1, 150, 2):
        D = 7 ** a * de * de
        qs = [q for q in sp.primefactors(D + 3) if q not in (2, 7)]
        assert qs
        F, H = 1, 1
        for i in range(40):
            Fn = F + D * H
            if (H & -H) == 16:
                cases += 1
                ok = any(H % q == 0 and (F - 1) % q == 0 and (Fn - 1) % q == 0 for q in qs)
                viol += not ok
            F, H = Fn, Fn + H
print(f'(c) cases with v_2(H)=4: {cases}, violations: {viol}')
