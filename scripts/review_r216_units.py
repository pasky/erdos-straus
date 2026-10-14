"""R216 from-scratch check of BRIDGE_WORLDS Prop 6.2 (E+ unit twist over Q(sqrt 2)).
Variant as read by the reviewer: for a prime h ≡ 7 (mod 8), s = sqrt(2) mod h, U_h = <3 + 2s> ⊂ F_h^* (independent
of the root since (3+2s)(3-2s) = 1).  Fire+(n, h) :<=> exists (c, d), cd even (so 8 | 4cd), 4cd | h + 1, with
-n / (4 c^2 d) in U_h  (mod h).
Checks: index distribution of 1+s; least firing h < 2000 for primes 5 <= p < 1e5; (p/h) = -1 necessity;
T1 for odd squares; h = 103, p = 5; genuine Type II at the least firing h.
"""
import sys
from sympy import primerange, divisors, sqrt_mod, n_order, legendre_symbol, isprime

def unit_data(h):
    s = sqrt_mod(2, h)
    e0 = (1 + s) % h
    o = n_order(e0, h)
    u = (3 + 2 * s) % h
    U = set()
    x = 1
    while True:
        U.add(x)
        x = x * u % h
        if x == 1:
            break
    return (h - 1) // o, U

def slices(h, even_only=True):
    k = h + 1
    out = []
    for m4 in divisors(k):
        if m4 % 4: continue
        cd = m4 // 4
        if even_only and cd % 2: continue
        for c in divisors(cd):
            out.append((c, cd // c))
    return out

def fires_plus(n, h, U, sl):
    return [(c, d) for (c, d) in sl if (-n * pow(4 * c * c * d, -1, h)) % h in U]

def typeII(n, h):
    return [(c, d) for (c, d) in slices(h, even_only=False) if (n + 4 * c * c * d) % h == 0]

def main():
    H = [h for h in primerange(7, 100000) if h % 8 == 7]
    idx = {}
    for h in H:
        s = sqrt_mod(2, h); o = n_order((1 + s) % h, h); i = (h - 1) // o
        idx[i] = idx.get(i, 0) + 1
    print("h ≡ 7 mod 8 below 1e5:", len(H), "index distribution (top):", sorted(idx.items())[:6],
          "good (index<=2):", idx.get(1, 0) + idx.get(2, 0))
    Hs = [h for h in H if h < 2000]
    UD = {h: unit_data(h) for h in Hs}
    SL = {h: slices(h) for h in Hs}
    least = {}; viol = 0; good_nonfire = 0; tII = 0; nofire = []
    P = list(primerange(5, 100000))
    for p in P:
        first = None
        for h in Hs:
            if h == p: continue
            ind, U = UD[h]
            f = fires_plus(p, h, U, SL[h])
            if f and legendre_symbol(p % h, h) != -1: viol += 1
            if ind <= 2 and legendre_symbol(p % h, h) == -1 and not f: good_nonfire += 1
            if f and first is None:
                first = h
        if first is None:
            nofire.append(p)
        else:
            least[first] = least.get(first, 0) + 1
            if typeII(p, first): tII += 1
    print("primes:", len(P), "no firing h<2000:", nofire[:10], len(nofire))
    print("least firing h distribution:", sorted(least.items())[:6])
    print("violations of (p/h)=-1 necessity:", viol, " good h with (p/h)=-1 but no fire:", good_nonfire)
    print("genuine Type II at least firing h:", tII)
    sq = 0
    for r in range(3, 317, 2):
        n = r * r
        for h in Hs:
            if fires_plus(n, h, UD[h][1], SL[h]): sq += 1
    print("odd squares r<317: firing (n,h) pairs h<2000:", sq)
    ind, U = unit_data(103)
    print("h=103: index of 1+s:", ind, "|U| =", len(U), "slices", slices(103), "fires p=5:", fires_plus(5, 103, U, slices(103)),
          "(5/103) =", legendre_symbol(5, 103))

if __name__ == "__main__":
    main()
