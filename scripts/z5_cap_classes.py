"""z5_cap_classes.py — class mass of the cap-e shot family at prime moduli (CAP_GROWING §1).

For primes l ≡ 3 (mod 4), K = (l+1)/4, cap e: the forced classes are n ≡ −4Q² (mod l) with Q odd, Q < l/2,
rad Q | K and v_s(Q) ≤ v_s(K) + e (EXPONENT_CAP Prop 1.2). omega_e(l) = their number (distinct: Q < l/2).
Prints S_e(X) = sum_{l ≤ X} omega_e(l)/l and S_e/(log X)^(e+1) at dyadic X; then verifies random shot
solutions exactly (Fractions + Def 1.1 prime by prime).
usage: z5_cap_classes.py X emax nverify
"""
import sys, math, random
from fractions import Fraction
from sympy import primerange, factorint

def boxQ(fK, e, bound):
    ps = [(s, v) for s, v in fK.items() if s != 2]
    out = [1]
    for s, v in ps:
        new = []
        for q in out:
            m = q
            for j in range(v + e + 1):
                if m >= bound: break
                new.append(m)
                m *= s
        out = new
    return out

def check(n, Q, g, e):
    # shot solution (UNIT_ORBIT Prop 2.1) and Def 1.1 of ES^{(y,e)}
    assert (n + 4 * Q * Q) % g == 0 and g % 4 == 3
    m = (n + 4 * Q * Q) // g
    x = Fraction(n + m, 4); y = Fraction(n * (g + 1), 4); z = n * x * (g + 1) / (4 * Q * Q)
    assert x.denominator == 1 and y.denominator == 1 and x > 0 and z > 0
    assert Fraction(4, n) == 1 / x + 1 / y + 1 / z
    d = z.denominator; r = math.isqrt(d); assert r * r == d and r % 2 == 1 and math.gcd(r, n) == 1
    for s, v in factorint(r).items():
        assert int(y) % s == 0 and v <= e
    return True

def main():
    X = int(sys.argv[1]); emax = int(sys.argv[2]); nver = int(sys.argv[3])
    S = [0.0] * (emax + 1); marks = []
    t = 1 << 10
    while t <= X: marks.append(t); t <<= 2
    samples = []
    for l in primerange(3, X + 1):
        if l % 4 != 3: continue
        fK = factorint((l + 1) // 4)
        for e in range(emax + 1):
            B = boxQ(fK, e, (l + 1) // 2)
            S[e] += len(B) / l
            if e == emax and nver and random.random() < 0.002:
                samples.append((l, random.choice(B)))
        if marks and l > marks[0]:
            L = math.log(marks[0])
            print(f"X=2^{int(math.log2(marks[0]))}", " ".join(f"S{e}={S[e]:.2f}({S[e]/L**(e+1):.3f})" for e in range(emax + 1)))
            marks.pop(0)
    L = math.log(X)
    print(f"X={X}", " ".join(f"S{e}={S[e]:.2f}({S[e]/L**(e+1):.3f})" for e in range(emax + 1)))
    ok = 0
    for l, Q in samples[:nver]:
        n = (-4 * Q * Q) % l
        while math.gcd(n, 2 * Q) != 1 or n < 3: n += l
        ok += check(n, Q, l, emax)
    print("verified exact solutions:", ok)

if __name__ == "__main__":
    main()
