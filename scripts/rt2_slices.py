"""O132 §2: the slice table (Lemma 2.1 of reviews/redteam-automorphic-2.md).

Type I:  4abd = p e + 1, a + b = c e      Type II: 4abd = p + e, a + b = c e     (a,b,c,d,e >= 1)

For every pair theta of coordinates ({a,c},{a,d},{a,e},{c,d},{d,e}; {a,b},{c,e} and Type I {a,d} are
congruence-type), Lemma 2.1 asserts a bijection between the fibre of V(p) over theta and
{f >= 1 : f | N_theta(p), f in a residue class mod q_theta}. Here we check, for each prime p < P:
  (1) brute force V(p) from the defining equations (no divisor tricks);
  (2) forward: every element maps to a divisor f of N_theta(p) in the stated class;
  (3) converse: for every theta in a box containing all theta occurring, every divisor in the class
      reconstructs a valid element (and it lies in V(p)); box = occurring thetas U [1,39]^2.
Prints counts; any failure raises AssertionError.
"""
import sys
from math import isqrt
from sympy import primerange, divisors


def brute(p, typ):
    """All (a,b,c,d,e) with a,b ordered (both orders kept)."""
    out = set()
    # bounds: Type I: f=4acd-p>=1, f'=4bcd-p>=1, ff' = p^2+4c^2 d  => (4cd-p)^2 <= p^2+4c^2 d
    # Type II: f=4acd-1, ff' = 4c^2 d p + 1 => (4cd-1)^2 <= 4c^2 d p + 1
    c = 1
    while True:
        found_c = False
        d = 1
        while True:
            if typ == 1:
                lo = 4*c*d - p
                ok = lo < 1 or lo*lo <= p*p + 4*c*c*d
                N = p*p + 4*c*c*d
            else:
                lo = 4*c*d - 1
                ok = lo*lo <= 4*c*c*d*p + 1
                N = 4*c*c*d*p + 1
            if not ok:
                break
            found_c = True
            # f = 4acd - shift ranges over f >= 1, f <= N
            shift = p if typ == 1 else 1
            a = 1
            while 4*a*c*d - shift <= N:
                f = 4*a*c*d - shift
                if f >= 1:
                    # solve for b from ff' = N
                    if N % f == 0:
                        fp = N // f
                        if (fp + shift) % (4*c*d) == 0:
                            b = (fp + shift) // (4*c*d)
                            if (a + b) % c == 0:
                                e = (a + b) // c
                                lhs = 4*a*b*d
                                rhs = p*e + 1 if typ == 1 else p + e
                                if lhs == rhs and b >= 1:
                                    out.add((a, b, c, d, e))
                a += 1
            d += 1
        if not found_c or (typ == 2 and c > 2*p + 2):
            break   # Type II: a,b <= p (b(4ad-1) <= p+a), so c <= a+b <= 2p
        c += 1
    return out


def check_brute_independent(p, typ, V):
    """Second, cruder enumeration over (a,b,d) directly from 4abd = pe+1 (resp. p+e) for small p."""
    W = set()
    # Type I: 4abd <= p(a+b)+1 <= 2pb+1 (a<=b) => ad <= p/2+1; f' = 4bcd-p <= p^2+4c^2 d => b <= p^2+4p.
    # Type II: 4abd = p+e <= p+2b => ad <= p (b>=1); b <= p^2+4p is generous.
    for a in range(1, p + 2):
        for d in range(1, (p + 1)//a + 1):
            for b in range(a, p*p + 4*p + 1):
                m = 4*a*b*d
                if typ == 1:
                    if (m - 1) % p:
                        continue
                    e = (m - 1) // p
                else:
                    e = m - p
                if e < 1 or (a + b) % e:
                    continue
                c = (a + b)//e
                W.add((a, b, c, d, e)); W.add((b, a, c, d, e))
    return W


# slice definitions: (name, theta-extractor, N(p,theta) or None, residue test, reconstruct)
def slices(typ):
    S = []
    if typ == 1:
        # (c,d): f = 4acd - p | p^2 + 4c^2 d, f = -p mod 4cd
        S.append(("cd", lambda t: (t[2], t[3]),
                  lambda p, th: p*p + 4*th[0]**2*th[1],
                  lambda p, th: (4*th[0]*th[1], (-p) % (4*th[0]*th[1])),
                  lambda t, p: 4*t[0]*t[2]*t[3] - p))
        # (a,c): f = 4acd - p | ap + c, f = -p mod 4ac
        S.append(("ac", lambda t: (t[0], t[2]),
                  lambda p, th: th[0]*p + th[1],
                  lambda p, th: (4*th[0]*th[1], (-p) % (4*th[0]*th[1])),
                  lambda t, p: 4*t[0]*t[2]*t[3] - p))
        # (a,e): b | (pe+1)/(4a), b = -a mod e
        S.append(("ae", lambda t: (t[0], t[4]),
                  lambda p, th: (p*th[1] + 1)//(4*th[0]) if (p*th[1] + 1) % (4*th[0]) == 0 else None,
                  lambda p, th: (th[1], (-th[0]) % th[1]),
                  lambda t, p: t[1]))
        # (d,e): a | m = (pe+1)/(4d), a^2 = -m mod e
        S.append(("de", lambda t: (t[3], t[4]),
                  lambda p, th: (p*th[1] + 1)//(4*th[0]) if (p*th[1] + 1) % (4*th[0]) == 0 else None,
                  None,  # quadratic class: a^2 = -m mod e
                  lambda t, p: t[0]))
    else:
        S.append(("cd", lambda t: (t[2], t[3]),
                  lambda p, th: 4*th[0]**2*th[1]*p + 1,
                  lambda p, th: (4*th[0]*th[1], (-1) % (4*th[0]*th[1])),
                  lambda t, p: 4*t[0]*t[2]*t[3] - 1))
        S.append(("ac", lambda t: (t[0], t[2]),
                  lambda p, th: th[1]*p + th[0],
                  lambda p, th: (4*th[0]*th[1], (-1) % (4*th[0]*th[1])),
                  lambda t, p: 4*t[0]*t[2]*t[3] - 1))
        S.append(("ad", lambda t: (t[0], t[3]),
                  lambda p, th: p + 4*th[0]**2*th[1],
                  lambda p, th: (4*th[0]*th[1], (-1) % (4*th[0]*th[1])),
                  lambda t, p: 4*t[0]*t[2]*t[3] - 1))
        S.append(("ae", lambda t: (t[0], t[4]),
                  lambda p, th: (p + th[1])//(4*th[0]) if (p + th[1]) % (4*th[0]) == 0 else None,
                  lambda p, th: (th[1], (-th[0]) % th[1]),
                  lambda t, p: t[1]))
        S.append(("de", lambda t: (t[3], t[4]),
                  lambda p, th: (p + th[1])//(4*th[0]) if (p + th[1]) % (4*th[0]) == 0 else None,
                  None,
                  lambda t, p: t[0]))
    return S


def reconstruct(typ, name, p, th, f):
    """Given theta and the divisor f, rebuild (a,b,c,d,e) or None."""
    if name == "cd":
        c, d = th
        shift = p if typ == 1 else 1
        N = p*p + 4*c*c*d if typ == 1 else 4*c*c*d*p + 1
        fp = N // f
        if (f + shift) % (4*c*d) or (fp + shift) % (4*c*d):
            return None
        a, b = (f + shift)//(4*c*d), (fp + shift)//(4*c*d)
        if (a + b) % c:
            return None
        e = (a + b)//c
    elif name == "ac":
        a, c = th
        shift = p if typ == 1 else 1
        if (f + shift) % (4*a*c):
            return None
        d = (f + shift)//(4*a*c)
        num = 4*a*a*d + (1 if typ == 1 else p)
        if num % f:
            return None
        e = num // f
        b = c*e - a
    elif name == "ad":
        a, d = th
        if (f + 1) % (4*a*d):
            return None
        c = (f + 1)//(4*a*d)
        e = (p + 4*a*a*d)//f
        b = c*e - a
    elif name == "ae":
        a, e = th
        b = f
        m = (p*e + 1)//(4*a) if typ == 1 else (p + e)//(4*a)
        d = m // b
        if (a + b) % e:
            return None
        c = (a + b)//e
    elif name == "de":
        d, e = th
        a = f
        m = (p*e + 1)//(4*d) if typ == 1 else (p + e)//(4*d)
        b = m // a
        if (a + b) % e:
            return None
        c = (a + b)//e
    t = (a, b, c, d, e)
    if min(t) < 1:
        return None
    ok = (4*a*b*d == (p*e + 1 if typ == 1 else p + e)) and a + b == c*e
    return t if ok else None


def main():
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    Pind = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    tot = {1: 0, 2: 0}
    for p in primerange(5, P):
        print("p", p, flush=True) if p % 50 < 2 else None
        for typ in (1, 2):
            V = brute(p, typ)
            if p < Pind:
                W = check_brute_independent(p, typ, V)
                assert V == W, (p, typ, len(V), len(W))
            tot[typ] += len(V)
            for (name, th_of, Nf, cls, f_of) in slices(typ):
                # forward
                thetas = set()
                for t in V:
                    th = th_of(t)
                    thetas.add(th)
                    N = Nf(p, th)
                    f = f_of(t, p)
                    assert N is not None and f >= 1 and N % f == 0, (p, typ, name, t)
                    if cls is not None:
                        q, r = cls(p, th)
                        assert f % q == r, (p, typ, name, t)
                    else:
                        m, e = N, th[1]
                        assert (f*f + m) % e == 0, (p, typ, name, t)
                # converse over a box
                if not thetas:
                    continue
                m0 = max(x for x, _ in thetas) + 3
                m1 = max(y for _, y in thetas) + 3
                box = set(thetas) | {(x, y) for x in range(1, min(m0, 40)) for y in range(1, min(m1, 40))}
                for th in sorted(box):
                    if True:
                        N = Nf(p, th)
                        if N is None or N < 1:
                            continue
                        for f in divisors(N):
                            if cls is not None:
                                q, r = cls(p, th)
                                if f % q != r:
                                    continue
                            else:
                                if (f*f + N) % th[1]:
                                    continue
                            t = reconstruct(typ, name, p, th, f)
                            assert t is not None and t in V, (p, typ, name, th, f, t)
    print(f"primes 5<=p<{P}: Type I tuples {tot[1]}, Type II tuples {tot[2]}; "
          f"independent brute force agreed for p<{Pind}; all slice bijections verified")


if __name__ == "__main__":
    main()
