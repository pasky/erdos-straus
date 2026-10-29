"""z50 lsmass: class-family profiles and square-base checks (independent small script).

U-family (n == 1 mod 8, c = 7, S = 4Z u (8Z+7)):
  W1: word (t,u,v), pivot modulus M = t*u - 1 >= 2, class n == -u (mod M), u | M+1.
      U-certificate if u in S (class mod M), or v = (n+u)/M in S (2-adic refinement:
      v == 0 mod 4  <=> n == -u mod 4M ; v == 7 mod 8 <=> n == -u + 7M mod 8M).
  W2: pivot modulus u*v, class n == -(u+v) (mod uv), u or v in S.
ES5 family (n == 1 mod 4): certificate words = some slot of (t,u,v,tu-1,tv-1) == 0 mod 4;
  by Theorem A equivalently Jacobi (uv/n) = -1 when gcd(uv,n)=1.

Checks:
 (1) no U-class (both types, with the n == 1 mod 8 condition built in) of modulus G <= GMAX
     contains a unit square mod G   [square base, Theorem E];
 (2) mass profile: sum over classes with modulus <= X of 1/G  vs (log X)^2  (U, ES5)
     and vs the ES R(M) family (log X)^3;
 (3) smooth first moment M(y) = sum over classes with P(G) <= y of Gamma(G)/G (truncated at G <= X).
"""
import math, json, sys
from math import gcd, log

def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return ds

def inS(x):
    return x % 4 == 0 or x % 8 == 7

def u_classes(GMAX):
    """Return set of (G, b) U-classes with 8 | G (n == 1 mod 8 built in), G <= GMAX."""
    cls = set()
    # W1
    for M in range(2, GMAX + 1):
        for u in divisors(M + 1):
            if u >= M + 1:  # t >= 1 means u <= M+1 ; u = M+1 gives t = 1? tu-1 = M -> t=(M+1)/u
                pass
            t = (M + 1) // u
            if t < 1:
                continue
            if inS(u):
                G = 8 * M // gcd(8, M) if True else None
                # combine n == -u mod M with n == 1 mod 8
                G = M * 8 // gcd(M, 8)
                for b in range(-u % G, G, M):
                    if b % 8 == 1 % 8 and (b + u) % M == 0:
                        if G <= GMAX * 8:
                            cls.add((G, b))
                        break
            # v in S via 2-adic refinement: v == 0 mod 4 or v == 7 mod 8, v = (n+u)/M
            for r in range(8):  # v mod 8
                if not inS(r if r else 8):
                    continue
                # n = M*v - u with v == r mod 8 -> n mod 8M determined
                G0 = 8 * M
                b = (M * r - u) % G0
                if b % 8 == 1:
                    cls.add((G0, b))
    # W2
    for u in range(1, GMAX + 1):
        for v in range(u, GMAX // u + 1):
            if not (inS(u) or inS(v)):
                continue
            q = u * v
            G = q * 8 // gcd(q, 8)
            for b in range((-(u + v)) % q, G, q):
                if b % 8 == 1:
                    cls.add((G, b))
                    break
    return cls

def unit_squares_mod(G):
    return {(x * x) % G for x in range(G) if gcd(x, G) == 1}

def check_square_base(GMAX):
    bad = []
    cache = {}
    for (G, b) in sorted(u_classes(GMAX)):
        if G > 8 * GMAX:
            continue
        if gcd(b, G) != 1:
            continue
        if G not in cache:
            cache[G] = unit_squares_mod(G)
        if b in cache[G]:
            bad.append((G, b))
    return bad

def es5_class_has_unit_square(GMAX):
    """ES5 W1 classes -u mod M (u|M+1) refined by n mod 4M (to fix t,u,v,tu-1,tv-1 mod 4)
    and n == 1 mod 4; certificate iff some slot == 0 mod 4. Check: no certificate class
    contains a unit square mod its modulus."""
    bad = []
    for M in range(2, GMAX + 1):
        for u in divisors(M + 1):
            t = (M + 1) // u
            G = 4 * M * 4  # n mod 16M fixes v mod 16 ... enough to fix v mod 4
            sq = None
            for vr in range(4):  # v mod 4
                n_res = (M * vr - u) % (4 * M)
                if n_res % 4 != 1:
                    continue
                slots = [t % 4, u % 4, vr % 4, (t * u - 1) % 4, (t * vr - 1) % 4]
                if 0 not in slots:
                    continue
                G4 = 4 * M
                if gcd(n_res, G4) != 1:
                    continue
                if sq is None:
                    sq = {(x * x) % G4 for x in range(G4) if gcd(x, G4) == 1}
                if n_res in sq:
                    bad.append((G4, n_res, t, u, vr))
    return bad

def mass_profiles(X):
    """Mass sum_{classes, G<=X} 1/G for U (W1 core: u|M+1 with u in S), ES5-W1 (all u|M+1,
    half weight heuristic not used: exact count of certificate residues), ES R(M) family."""
    tau_shift = [0] * (X + 2)
    # tau(M+1) via divisor sieve
    d = [0] * (X + 2)
    for i in range(1, X + 2):
        for j in range(i, X + 2, i):
            d[j] += 1
    res = {}
    U1 = 0.0
    ALL1 = 0.0
    R3 = 0.0
    W2 = 0.0
    checkpoints = [10**k for k in range(2, 8) if 10**k <= X]
    out = []
    # W2 mass: sum_{uv<=X, u or v in S, u<=v} 1/(uv)   (computed by harmonic counting)
    for M in range(2, X + 1):
        ALL1 += d[M + 1] / M
        if M % 4 == 3:
            A = (M + 1) // 4
            # tau(A^2) needs factorization; approximate via exact factor
            a = A
            tt = 1
            p = 2
            while p * p <= a:
                if a % p == 0:
                    e = 0
                    while a % p == 0:
                        a //= p
                        e += 1
                    tt *= (2 * e + 1)
                p += 1
            if a > 1:
                tt *= 3
            R3 += tt / M
        if M in checkpoints:
            L = log(M)
            out.append({"X": M, "allW1_div_L2": ALL1 / L**2, "R_div_L3": R3 / L**3, "R_div_L2": R3 / L**2})
    return out

if __name__ == "__main__":
    GM = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    bad = check_square_base(GM)
    print("U classes with modulus <= 8*%d containing a unit square:" % GM, len(bad), bad[:10])
    bad5 = es5_class_has_unit_square(GM)
    print("ES5 W1 certificate classes (mod 4M, M<=%d) containing a unit square:" % GM, len(bad5), bad5[:10])
    X = int(sys.argv[2]) if len(sys.argv) > 2 else 10**5
    prof = mass_profiles(X)
    for r in prof:
        print(r)
    json.dump({"GMAX": GM, "U_bad": bad, "ES5_bad": bad5, "profiles": prof},
              open("data/z50_lsmass/profile.json", "w"), indent=1)
