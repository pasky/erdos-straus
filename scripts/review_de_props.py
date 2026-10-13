"""R168 from-scratch checks of DETERMINISTIC_EXISTENCE Props 3.2, 3.3, 3.4, 5.1, 6.2, 6.3, 8.1 (small cases)."""
from math import gcd
from sympy import primerange, isprime, factorint, jacobi_symbol, n_order, divisors
from fractions import Fraction


def kron(D, n):  # Kronecker symbol (D/n), n>0
    from sympy.ntheory import residue_ntheory as rn
    from sympy import jacobi_symbol
    r = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0:
            return 0
        r *= 1 if D % 8 in (1, 7) else -1
    return r * (jacobi_symbol(D % n, n) if n > 1 else 1)


def subgroup(gens, e):
    H = {1 % e}
    frontier = [1 % e]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = x * g % e
            if y not in H:
                H.add(y); frontier.append(y)
    return H


def sigma(N, e):
    return {a * pow(N // a // b * 0 + b, -1, e) % e for a in divisors(N) for b in divisors(N // a)}


# --- Type II / Type I slice identities (exact rational check)
bad = 0
for p in primerange(5, 400):
    for e in range(1, 60):
        for typ in ("II", "I"):
            num = p + e if typ == "II" else p * e + 1
            if num % 4: continue
            N = num // 4
            for a in divisors(N):
                for b in divisors(N // a):
                    if (a + b) % e: continue
                    k = N // (a * b); m = (a + b) // e
                    x = N if typ == "II" else p * N
                    y, z = (m * p * k * a, m * p * k * b) if typ == "II" else (m * k * a, m * k * b)
                    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p): bad += 1
print("slice identities violations:", bad)

# --- Prop 3.2: f | p^2+4c^2 d, f ≡ -p (4cd), f>0, p∤2cd  =>  kron(-4d,p) = -1
viol = cnt = 0; negf = 0
for p in primerange(3, 300):
    for c in range(1, 8):
        for d in range(1, 12):
            if (2 * c * d) % p == 0: continue
            M = p * p + 4 * c * c * d
            for f in divisors(M):
                for s in (1, -1):
                    if (s * f + p) % (4 * c * d) == 0:
                        if s == 1:
                            cnt += 1
                            if kron(-4 * d, p) != -1: viol += 1
                        else:
                            negf += (kron(-4 * d, p) == 1)
print(f"Prop3.2: {cnt} positive (c,d,f) tested, violations {viol}; negative-f integral points with chi(p)=+1: {negf}")

# --- Prop 5.1 / Cor 5.2 scope: integral points of C_{c,d,p}: 4cd*e*a - 4d a^2 - p e = 1 (any sign)
ex = []
for p in primerange(5, 120):
    for c in range(1, 4):
        for d in range(1, 6):
            if kron(-4 * d, p) != 1 or (2*c*d) % p == 0: continue
            for a in range(-300, 301):
                den = 4 * c * d * a - p
                if den != 0 and (1 + 4 * d * a * a) % den == 0:
                    e_ = (1 + 4 * d * a * a) // den
                    assert 4*c*d*e_*a - 4*d*a*a - p*e_ == 1
                    ex.append((p, c, d, a, e_))
print("integral points on C_{c,d,p} with chi_{-4d}(p)=+1 (should be non-positive):", len(ex), ex[:6],
      "any positive:", any(a > 0 and e_ > 0 for (_, _, _, a, e_) in ex))

# --- Prop 6.2: -1 in <r> mod odd e  <=>  v2(ord_{q^a} r) equal and >=1 over all q^a || e
def v2(n):
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k
bad = 0
for e in range(3, 400, 2):
    fe = factorint(e)
    for r in range(1, e):
        if gcd(r, e) != 1: continue
        lhs = (e - 1) in subgroup([r], e)
        vs = {v2(n_order(r % q**a, q**a)) if q**a > 2 else 0 for q, a in fe.items()}
        rhs = len(vs) == 1 and min(vs) >= 1
        bad += lhs != rhs
print("Prop6.2 2-adic criterion mismatches (odd e<400):", bad)

# --- Prop 6.3: Sigma(l) = {1,l,l^-1} vs <l>: does order-3 l give Sigma = H?  exponent<=2 <=> e|24
o3 = [(e, l) for e in range(3, 60) for l in range(2, e) if gcd(l, e) == 1 and n_order(l, e) == 3]
print("order-3 elements (Sigma=H for N=prime l in that class):", o3[:4])
print("exponent<=2 moduli <=200:", [e for e in range(1, 201) if all(pow(x, 2, e) == 1 % e for x in range(1, e) if gcd(x, e) == 1)])

# --- Prop 3.4: forced by Jacobi, and Prop 8.1(ii) never group-forced
bad = 0; fired = 0
for p in primerange(5, 20000):
    if p % 4 != 1: continue
    for e in primerange(3, 80):
        if e % 4 != 3 or e >= p: continue
        N = (p + e) // 4
        H = subgroup(list(factorint(N)), e)
        if jacobi_symbol(p, e) == -1:
            fired += 1; bad += (e - 1) not in H
        N1 = (p * e + 1) // 4
        assert (e - 1) not in subgroup([N1 % e], e)
print("Prop3.4: fired", fired, "violations", bad)
