# z70 LOOSE item 2 (I5): candidate involutions on the full word set T_n = {(x,y,z) >= 1 : xyz - x - z = n}
# (list pre-registered in Z70_LOOSE.md §3). Stage 1: T_73, T_409 (+ controls T_9, T_105); stage 2 for survivors.
import sys
from math import gcd

def words(n):
    out = []
    for y in range(1, n + 3):
        # (xy - 1)(zy - 1) = n y + 1
        N = n * y + 1
        f = 1
        while f * f <= N:
            if N % f == 0:
                for (u, v) in ((f, N // f), (N // f, f)):
                    if (u + 1) % y == 0 and (v + 1) % y == 0:
                        x, z = (u + 1) // y, (v + 1) // y
                        if x >= 1 and z >= 1 and x * y * z - x - z == n: out.append((x, y, z))
            f += 1
    return sorted(set(out))

def cert(w):
    x, y, z = w
    return x % 4 == 0 or y % 4 == 0 or z % 4 == 0 or (x % 4 == 3 and y % 4 == 3) or (z % 4 == 3 and y % 4 == 3)

def gam(w, n):
    x, y, z = w; return (x * y - 1, n, y, z * y - 1)
def word_of(g, n):
    a, b, c, d = g
    if b != n or c < 1 or (a + 1) % c or (d + 1) % c: return None
    x, z = (a + 1) // c, (d + 1) // c
    if x < 1 or z < 1: return None
    return (x, c, z)
def mul(g, h):
    a, b, c, d = g; e, f, gg, hh = h
    return (a * e + b * gg, a * f + b * hh, c * e + d * gg, c * f + d * hh)
def Lk(k): return (1, 0, k, 1)

def orbit(w, n, act):
    g = gam(w, n); res = {0: w}
    for sgn in (1, -1):
        k = sgn; miss = 0
        while miss < 3 * n + 10:
            if act == 'L': h = mul(Lk(k), g)
            elif act == 'R': h = mul(g, Lk(k))
            else: h = mul(mul(Lk(k), g), Lk(-k))
            u = word_of(h, n)
            if u is not None: res[k] = u; miss = 0
            else: miss += 1
            # stop when entries go negative for good
            if min(h[0], h[3]) < -1 and abs(k) > 2: break
            k += sgn
    ks = sorted(res); return [res[k] for k in ks]

def rho(act, n):
    def f(w):
        o = orbit(w, n, act); i = o.index(w); return o[len(o) - 1 - i]
    return f
def swap(w): return (w[2], w[1], w[0])
def tau_xy(w, n):
    x, y, z = w
    if x * y >= 2 and (n + y) % (x * y - 1) == 0: return (y, x, (n + y) // (x * y - 1))
    return None
def tau_yz(w, n):
    t = tau_xy(swap(w), n); return swap(t) if t else None

def candidates(n):
    rC, rL, rR = rho('C', n), rho('L', n), rho('R', n)
    def s2a(w):
        t = tau_xy(w, n)
        if t: return t
        t = tau_yz(w, n)
        if t: return t
        return swap(w)
    def s2b(w):
        t = tau_xy(w, n); return t if t else swap(w)
    return {'rho_L': rL, 'rho_R': rR, 'rho_C': rC, 'sigma_C=s.rho_C': (lambda w: swap(rC(w))),
            'sigma_R=s.rho_R.s': (lambda w: swap(rR(swap(w)))), 'sigma2a': s2a, 'sigma2b': s2b}

def test(n, verbose=True):
    T = words(n); S = set(T); C = [w for w in T if cert(w)]
    out = {}
    if verbose: print(f"n={n}: |T|={len(T)} |C|={len(C)}  T={T if len(T) <= 40 else str(len(T)) + ' words'}")
    for name, f in candidates(n).items():
        img = {w: f(w) for w in T}
        ok_map = all(v in S for v in img.values())
        inv = ok_map and all(img[img[w]] == w for w in T)
        fix = [w for w in T if img[w] == w]
        fixc = [w for w in fix if cert(w)]
        moves_y = any(img[w][1] != w[1] for w in T)
        is_swap = all(img[w] == swap(w) for w in T)
        res = 'PASS' if inv and not is_swap and fix and len(fixc) == len(fix) else 'fail'
        out[name] = res
        if verbose:
            print(f"   {name:18s} maps-into-T={ok_map} involution={inv} =swap={is_swap} moves_y={moves_y} "
                  f"#fix={len(fix)} #fix-in-C={len(fixc)} noncert-fixed={[w for w in fix if not cert(w)][:4]} -> {res}")
    return out

if __name__ == '__main__':
    for n in (73, 409, 9, 105):
        test(n)
