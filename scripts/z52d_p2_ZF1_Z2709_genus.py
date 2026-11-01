"""Z2709: Type I at level d as an ideal-class statement in Z[w], w = sqrt(-d) (QUATERNION_ES Lemma 1.1).
A Type I solution (a,b,c,d,e): 4abd-1 = pe, a+b = ce.  Then alpha = 1+2aw lies in the ideal E = [e, k+w],
k = (2a)^{-1} mod e (k^2 ≡ -d mod e), of norm e; its form is (e, 2k, (k^2+d)/e), disc -4d.
We (1) check the forced genus: chi(E) = chi(-p) for every assigned character of disc -4d (PROVED below by
pe ≡ -1 mod 4d·(...)), (2) record the order of [E] in the form class group Cl(-4d) and compare with the
uniform-on-the-forced-genus model, (3) record whether [E] is the class of a norm-e ideal with e minimal etc.
Usage: python ... P DMAX"""
import sys, math, random
from collections import Counter, defaultdict
from sympy import isprime, divisors, jacobi_symbol
from sympy.ntheory import sqrt_mod

def reduce_form(f):
    a, b, c = f
    while True:
        if b > a or b <= -a:
            # normalise b into (-a, a]
            k = (a - b) // (2 * a)
            b, c = b + 2 * k * a, a * k * k + b * k + c
            continue
        if a > c:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        return (a, b, c)

def _egcd(x, y):
    """returns (g, u, v) with u*x + v*y = g >= 0"""
    if y == 0:
        return (abs(x), (1 if x >= 0 else -1), 0)
    g_, u, v = _egcd(y, x % y)
    return (g_, v, u - (x // y) * v)

def compose(f, g):
    """Gauss composition of primitive positive definite forms (Cohen, GTM 138, Algorithm 5.4.7)."""
    (a1, b1, c1), (a2, b2, c2) = f, g
    if a1 > a2:
        (a1, b1, c1), (a2, b2, c2) = (a2, b2, c2), (a1, b1, c1)
    s = (b1 + b2) // 2
    n = b2 - s
    if a2 % a1 == 0:
        y1, d = 0, a1
    else:
        d, u, v = _egcd(a2, a1)
        y1 = u
    if s % d == 0:
        y2, x2, d1 = -1, 0, d
    else:
        d1, x2, y2 = _egcd(s, d)
        y2 = -y2
    v1, v2 = a1 // d1, a2 // d1
    r = (y1 * y2 * n - x2 * c2) % v1
    b3 = b2 + 2 * v2 * r
    a3 = v1 * v2
    c3 = (c2 * d1 + r * (b2 + v2 * r)) // v1
    assert b3 * b3 - 4 * a3 * c3 == b1 * b1 - 4 * a1 * c1
    return reduce_form((a3, b3, c3))

def class_group(d):
    D = -4 * d
    forms = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                if c < a or (c == a and b < 0): continue
                if math.gcd(math.gcd(a, b), c) != 1: continue
                forms.append((a, b, c))
        a += 1
    return forms

def order(f, ident):
    g, k = f, 1
    while g != ident:
        g = compose(g, f); k += 1
        if k > 10000: raise RuntimeError("order")
    return k

def genus_chars(d):
    """assigned characters for D = -4d evaluated on odd n coprime to d: list of functions"""
    ells = [l for l in range(3, d + 1, 2) if d % l == 0 and isprime(l)]
    ch = [lambda n, l=l: jacobi_symbol(n % l, l) for l in ells]
    m = d % 8
    # Cox Thm 3.15 (D=-4n): n≡3 (4): none extra beyond odd primes... use full set (delta, epsilon) as in Cox
    if d % 4 == 1 or d % 4 == 2 or d % 4 == 3 or d % 4 == 0:
        pass
    if m in (1, 5):     # n ≡ 1 (4): delta
        ch.append(lambda n: (-1) ** ((n - 1) // 2))
    elif m in (2,):     # n ≡ 2 (8): delta*epsilon
        ch.append(lambda n: (-1) ** ((n - 1) // 2 + (n * n - 1) // 8))
    elif m in (6,):     # n ≡ 6 (8): epsilon
        ch.append(lambda n: (-1) ** ((n * n - 1) // 8))
    elif m in (4,):     # n ≡ 4 (8): delta
        ch.append(lambda n: (-1) ** ((n - 1) // 2))
    elif m == 0:        # n ≡ 0 (8): delta, epsilon
        ch.append(lambda n: (-1) ** ((n - 1) // 2)); ch.append(lambda n: (-1) ** ((n * n - 1) // 8))
    return ch

def main(P, DMAX):
    stats = defaultdict(Counter)
    genus_fail = 0; nsol = 0
    ord_hist = Counter(); model_hist = Counter()
    per_d = {}
    E1 = Counter()
    rng = random.Random(1)
    for d in range(1, DMAX + 1):
        forms = class_group(d)
        ident = reduce_form((1, 0, d))
        chars = genus_chars(d)
        ords = {f: order(f, ident) for f in forms}
        # genus of each form: chars on a represented odd value coprime to 2d
        def rep_value(f):
            a, b, c = f
            for x in range(0, 40):
                for y in range(0, 40):
                    v = a * x * x + b * x * y + c * y * y
                    if v > 0 and v % 2 == 1 and math.gcd(v, d) == 1 and math.gcd(x, y) == 1:
                        return v
            raise RuntimeError
        gen = {f: tuple(ch(rep_value(f)) for ch in chars) for f in forms}
        per_d[d] = (len(forms), Counter(gen.values()))
        a = 1
        while 4 * a * 1 * d - 1 <= P * 1 and a <= P:
            N0 = 4 * a * a * d + 1
            for e in divisors(N0):
                b = (-a) % e
                if b == 0: b = e
                any_ = False
                while True:
                    num = 4 * a * b * d - 1
                    if num > P * e: break
                    if num % e == 0:
                        p = num // e
                        if p >= 5 and isprime(p) and (a + b) % e == 0:
                            nsol += 1
                            k = pow(2 * a, -1, e) if e > 1 else 0
                            f = reduce_form((e, 2 * k, (k * k + d) // e)) if e > 1 else ident
                            # forced genus: chi(E) = chi(-p)  (characters evaluated on norm e vs on -p mod 4d)
                            gE = gen[f]
                            gp = tuple(ch((-p) % (8 * d) + 8 * d) for ch in chars)
                            if gE != gp: genus_fail += 1
                            o = ords[f]
                            ord_hist[o] += 1
                            # model: uniform class in the forced genus
                            cand = [g for g in forms if gen[g] == gp]
                            model_hist[ords[rng.choice(cand)]] += 1
                            stats[d]["sol"] += 1
                            stats[d]["principal" if f == ident else "nonprincipal"] += 1
                            stats[d]["model_principal_prob"] += 1.0 / len(cand) if ident in cand else 0
                            if e > 1:
                                # refined null model: uniform over the primitive ideals of norm e (all roots k of
                                # k^2 ≡ -d mod e), restricted to the forced genus
                                ks = sqrt_mod(-d % e, e, all_roots=True)
                                cl = [reduce_form((e, 2 * kk, (kk * kk + d) // e)) for kk in ks]
                                cl = [g for g in cl if gen[g] == gp]
                                E1["n"] += 1
                                E1["obs_principal"] += (f == ident)
                                E1["mod_principal"] += sum(g == ident for g in cl) / len(cl)
                                E1["obs_ord"] += o
                                E1["mod_ord"] += sum(ords[g] for g in cl) / len(cl)
                                E1["nchoices1"] += (len(set(cl)) == 1)
                    b += e
            a += 1
    print(f"Type I solutions (a,b,c,d,e) with p<= {P} prime, d<= {DMAX}: {nsol}")
    print(f"genus of [E] != forced genus chi(-p): {genus_fail} failures")
    print("order of [E] in Cl(-4d):   observed histogram vs uniform-in-forced-genus model")
    for o in sorted(set(ord_hist) | set(model_hist)):
        print(f"   ord {o:3d}: obs {ord_hist[o]:8d}   model {model_hist[o]:8d}")
    tot = sum(stats[d]["sol"] for d in stats); pr = sum(stats[d]["principal"] for d in stats)
    mp = sum(stats[d]["model_principal_prob"] for d in stats)
    print(f"[E] principal: observed {pr} ({pr/tot:.4f}), model expectation {mp:.1f} ({mp/tot:.4f})")
    print(f"e>1 solutions: {E1['n']}; [E] principal obs {E1['obs_principal']} vs refined model {E1['mod_principal']:.1f}; "
          f"mean order obs {E1['obs_ord']/E1['n']:.4f} vs model {E1['mod_ord']/E1['n']:.4f}; "
          f"solutions where the forced genus leaves a single norm-e class: {E1['nchoices1']}")
    # per-d summary for d with class number >= 4
    print("d  h(-4d)  #sol  principal_obs  principal_model")
    for d in sorted(stats):
        h = per_d[d][0]
        if h >= 4 and stats[d]["sol"] >= 200:
            print(f"{d:4d} {h:4d} {stats[d]['sol']:7d} {stats[d]['principal']:7d} {stats[d]['model_principal_prob']:9.1f}")

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
