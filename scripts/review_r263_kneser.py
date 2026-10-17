"""R263 from-scratch checks for JOINT_BUDGET §3: window equivalence, Lemma 3.1, Prop 3.2 (Kneser threshold)."""
import random
from math import gcd
from fractions import Fraction

random.seed(2631)


def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]


def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f


def divisors(n):
    ds = [1]
    for q, e in factor(n).items():
        ds = [x * q**k for x in ds for k in range(e + 1)]
    return ds


def sigma_set(fac, m):
    S = {1 % m}
    for s, b in fac.items():
        inv = pow(s, -1, m)
        new = set()
        for x in S:
            for k in range(-b, b + 1):
                new.add(x * pow(s if k >= 0 else inv, abs(k), m) % m)
        S = new
    return S


def gen_subgroup(gens, m):
    H = {1 % m}; frontier = [1 % m]
    while frontier:
        x = frontier.pop(); 
        for g in gens:
            y = x * g % m
            if y not in H: H.add(y); frontier.append(y)
    return H


# ---- 1. window equivalence: Type II at window m  <=>  -1 in Sigma_m(K), and ES identity
PR = primes_upto(3000)
nchk = mism = 0
for p in [q for q in PR if q % 4 == 1 and q < 1200]:
    for m in range(3, 2 * p, 4):
        if gcd(m, p) != 1: continue
        K = (p + m) // 4
        # direct: any a,b>=1 (not nec. coprime) with ab | K and m | a+b
        direct = False
        for a in divisors(K):
            for b in divisors(K // a):
                if (a + b) % m == 0:
                    direct = True
                    c = (a + b) // m; d = K // (a * b)
                    assert Fraction(4, p) == Fraction(1, a*b*d) + Fraction(1, a*c*d*p) + Fraction(1, b*c*d*p)
                    break
            if direct: break
        sig = (m - 1) in sigma_set(factor(K), m) if K > 1 else (m == 2)
        nchk += 1
        if direct != sig: mism += 1; print('MISMATCH', p, m, direct, sig)
print('window equivalence: windows checked', nchk, 'mismatches', mism)

# ---- 2. example p=809, m=31
K = (809 + 31) // 4
print('p=809 m=31 K', K, 'Sigma==(Z/31)^x', len(sigma_set(factor(K), 31)) == 30, '10*21==K', 10*21 == K, '31|31')

# ---- 3. Prop 3.2 brute force
def check_31(fac, m, H0):
    n0 = len(H0)
    # cyclic group: subgroups of H0 <-> divisors t of |H0|; H_t = {x in H0: x^t = 1}
    for t in range(1, n0):
        if n0 % t: continue
        H = {x for x in H0 if pow(x, t, m) == 1}
        lhs = sum(2 * b for s, b in fac.items() if s % m not in H)
        if lhs < n0 // t - 1: return False
    return True

tested = held = bad = forced_held = 0
small = [q for q in PR if q < 400]
for trial in range(40000):
    m = random.choice([q for q in PR if 5 <= q < 110])
    pool = [q for q in small if q != m]
    if random.random() < 0.5:  # bias towards primes of small order mod m
        pool = sorted(pool, key=lambda q: (pow(q, 2, m) == 1) + (pow(q, 3, m) == 1) + (pow(q, 4, m) == 1) + (pow(q, 6, m) == 1), reverse=True)[:12]
    k = random.randint(1, 6)
    fac = {}
    for _ in range(k):
        s = random.choice(pool); fac[s] = fac.get(s, 0) + random.randint(1, 8)
    H0 = gen_subgroup([s % m for s in fac], m)
    tested += 1
    if check_31(fac, m, H0):
        held += 1
        Sg = sigma_set(fac, m)
        if Sg != H0: bad += 1; print('KNESER COUNTEREXAMPLE', m, fac)
        if (m - 1) in H0 and m % 4 == 3: forced_held += 1
print('Prop 3.2: tested', tested, '(3.1) held', held, 'Sigma!=H0 among them', bad, '; with -1 in H0, m=3(4):', forced_held)

# ---- 4. sharpness probe: cases where (3.1) fails by 1 at exactly one H and Sigma != H0 (shows criterion is tight-ish)
