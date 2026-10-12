"""O163 Lemma 8.2 sanity check (formal power series at the origin).

Genuinely two-variable polynomial families with k >= 1 are not known (Sec. 6), so Lemma 8.2 is
checked on formal power-series solutions of 4/Q = 1/x + 1/y + 1/z around (0,0), built from random
data, and on composed one-variable families (k = 0).  Truncation degree T.

Type I:  pick h, y (ord y = k); x~ = (Qh+1)/4, z = (Qh+1) y / (4yh - Qh - 1)  (power series).
         Check: identity yz(4x~-1) = Q x~ (y+z) mod deg > T, x~(0) = 1/4, ord z = k, z_k = -y_k.
Type II: pick h (h(0) != 0), y~ with y~(0) = 0; z~ = (Qh + y~)/(4y~ - 1), x = y~ z~ / h.
         Check: identity x(4y~z~ - y~ - z~) = Q y~ z~, x(0) = 0 and z~(0) = 0.
         Also the converse direction of the lemma on random data with y~(0) != 0: x(0) != 0.
"""
import random
import sympy as sp

u, v, t = sp.symbols('u v t')
T = 7


def trunc(e, d=T):
    p = sp.Poly(sp.expand(e), u, v)
    return sp.Add(*[c * u**i * v**j for (i, j), c in p.terms() if i + j <= d])


def inv_series(g, d=T):
    """1/g as truncated power series (g(0) != 0)."""
    g0 = g.subs({u: 0, v: 0})
    r = sp.expand(1 - g / g0)  # g = g0 (1 - r), ord r >= 1
    s, p = sp.Integer(1), sp.Integer(1)
    for _ in range(d):
        p = trunc(p * r, d)
        s += p
    return trunc(s / g0, d)


def homog(e, j):
    p = sp.Poly(sp.expand(e), u, v)
    return sp.Add(*[c * u**a * v**b for (a, b), c in p.terms() if a + b == j])


def order(e):
    p = sp.Poly(sp.expand(e), u, v)
    return min(a + b for (a, b), c in p.terms() if c != 0)


def rnd_poly(deg, lo, k0=0):
    return sum(random.randint(-3, 3) * u**i * v**j for i in range(deg + 1) for j in range(deg + 1 - i)
               if i + j >= k0 and i + j <= deg) + (random.randint(1, 3) if k0 == 0 else 0)


def main():
    random.seed(163)
    bad = 0
    for Q in (u**2 + v**2, u**2 + u*v + v**2, u**2 + 5*v**2):
        for trial in range(6):
            k = trial % 3  # 0,1,2
            h = rnd_poly(2, -3)
            y = rnd_poly(3, -3, k0=max(k, 1)) if k else rnd_poly(3, -3)
            if order(y) != k:
                y = y + (u if k == 1 else (u*v if k == 2 else 1))
            xt = (Q * h + 1) / 4
            den = sp.expand(4 * y * h - Q * h - 1)
            z = trunc((Q * h + 1) * y * inv_series(den), T)
            ident = trunc(y * z * (4 * xt - 1) - Q * xt * (y + z), T - 1)
            ok = (sp.expand(ident) == 0 and xt.subs({u: 0, v: 0}) == sp.Rational(1, 4)
                  and order(z) == order(y) and (k == 0 or sp.expand(homog(z, k) + homog(y, k)) == 0))
            bad += not ok
            print(f"TypeI Q={Q} k={k}: ok={ok}")
        for trial in range(4):
            h = rnd_poly(2, -3)
            if h.subs({u: 0, v: 0}) == 0:
                h += 1
            yt = rnd_poly(3, -3, k0=1) if trial % 2 == 0 else rnd_poly(3, -3) + 2
            zt = trunc((Q * h + yt) * inv_series(sp.expand(4 * yt - 1)), T)
            x = trunc(yt * zt * inv_series(h), T)
            ident = trunc(x * (4 * yt * zt - yt - zt) - Q * yt * zt, T - 1)
            x0, y0, z0 = (e.subs({u: 0, v: 0}) for e in (x, yt, zt))
            ok = sp.expand(ident) == 0 and ((x0 == 0) == (y0 == 0 and z0 == 0)) \
                and sp.expand((4*y0 - 1) * (4*z0 - 1) - 1) == 0
            bad += not ok
            print(f"TypeII Q={Q} y~(0)={y0}: x(0)={x0} z~(0)={z0} ok={ok}")
    # composed one-variable families (n -> Q): ET-type Type I family f=5, a=d=1 and a Type II one
    n = sp.Symbol('n')
    fams = {'I': (n * (n + 1) / 4, (n + 5) / 4, (n + 1) * (n + 5) / 16),
            'II': ((n + 1) / 4, n * (n + 1) / 2, n * (n + 1) / 2)}
    for name, (X, Y, Z) in fams.items():
        assert sp.simplify(1 / X + 1 / Y + 1 / Z - 4 / n) == 0
        if name == 'I':
            print("composed Type I: x~(0) =", sp.cancel(X / n).subs(n, 0), " y(0) =", Y.subs(n, 0))
        else:
            yt0 = sp.cancel(Y / n).subs(n, 0)
            print("composed Type II: x(0) =", X.subs(n, 0), " (4y~0-1)^2 =", (4 * yt0 - 1)**2)
    print("BAD", bad)


if __name__ == "__main__":
    main()
