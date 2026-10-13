"""R181: from-scratch random test of DRINFELD_ES Prop 1.2 (k-th power law), Lemma 1.1 and Thm 1.3.
Random Type II data (a,b,c,d) monic, gcd(a,b)=1, c | a+b, A monic deg>=1; P := A a b d - E, f := A a c d - 1.
Checks (P/f)_k == eps_k^{(1+deg f)(1+deg Ad)-1} for every k | q-1 (Jacobi symbols via own factorisation),
and, for P irreducible and k odd, (f/P)_k == 1.  Also Lemma 1.1 on random lambda, g."""
import random, sys
from review_dr_ff import FF, jacobi

def rmonic(F, d): return F.norm([random.randrange(F.p) for _ in range(d)] + [1])

def run(p, trials, seed=1):
    random.seed(seed); F = FF(p); ks = [k for k in range(2, p) if (p - 1) % k == 0]
    bad = 0; tested = 0; irr_tested = 0; bad13 = 0
    # Lemma 1.1
    for _ in range(200):
        lam = random.randrange(1, p); g = rmonic(F, random.randint(1, 6))
        for k in ks:
            lhs = jacobi(F, (lam,), g, k)
            z = pow(lam, (p - 1) // k, p)
            rhs = (F.dlog(z, k) * (len(g) - 1)) % k
            assert lhs == rhs, ("Lemma 1.1", p, lam, g, k)
    for _ in range(trials):
        A = rmonic(F, random.randint(1, 2)); a = rmonic(F, random.randint(0, 2)); b = rmonic(F, random.randint(0, 2))
        if F.gcd(a, b) != (1,): continue
        s = F.add(a, b)
        if not s: continue
        # c: random monic divisor of a+b
        fac = list(F.factor(s).items()); c = (1,)
        for l, e in fac: c = F.mul(c, F.pw(l, random.randint(0, e)))
        E = F.divmod(s, c)[0]; d = rmonic(F, random.randint(0, 2))
        Aad = F.mul(A, F.mul(a, d))
        P = F.sub(F.mul(Aad, b), E); f = F.sub(F.mul(Aad, c), (1,))
        assert F.mul(E, f) == F.add(P, F.mul(Aad, a))   # E f = P + A a^2 d
        degf, degAd = len(f) - 1, len(F.mul(A, d)) - 1
        for k in ks:
            eps = -1 if ((p - 1) // k) % 2 else 1
            pred = 0 if eps == 1 or ((1 + degf) * (1 + degAd) - 1) % 2 == 0 else k // 2
            got = jacobi(F, P, f, k)
            tested += 1
            if got != pred: bad += 1
        if F.is_irred(P):
            for k in ks:
                if k % 2:
                    irr_tested += 1
                    if jacobi(F, f, P, k) != 0: bad13 += 1
    print(f"q={p}: Prop1.2 tests {tested}, mismatches {bad}; Thm1.3 (P irreducible, odd k) tests {irr_tested}, mismatches {bad13}")

if __name__ == "__main__":
    for p in map(int, sys.argv[1:]): run(p, 3000)
