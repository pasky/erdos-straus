"""R234: from-scratch even-Clifford construction of E(L) (unique index-2 overorder of C0(L)) and check of
  r_L(m) = #{x in E(L) : nrd x = m p}  for 1 <= m < p/4  (all x, not only trace zero),
and that every x in E(L) with p | nrd x, nrd x < p^2/4 has trace 0. Also the Heegner algebra of z9_heegner_layers (a)."""
import sys
from fractions import Fraction as Fr
from itertools import product
from review_r234_lib import *


def mono_mul(a, b, G):
    """product of monomials e_a * e_b (tuples of indices, a and b sorted strictly increasing) -> dict"""
    res = {}
    def reduce(word, coef):
        # bubble: find first adjacent pair out of order or equal
        for k in range(len(word) - 1):
            i, j = word[k], word[k + 1]
            if i == j:
                reduce(word[:k] + word[k + 2:], coef * G[i][i])
                return
            if i > j:
                # e_i e_j = -e_j e_i + 2 G_ij
                reduce(word[:k] + (j, i) + word[k + 2:], -coef)
                reduce(word[:k] + word[k + 2:], coef * 2 * G[i][j])
                return
        res[word] = res.get(word, 0) + coef
    reduce(tuple(a) + tuple(b), Fr(1))
    return res


def mul(x, y, G):
    out = {}
    for a, ca in x.items():
        for b, cb in y.items():
            for w, c in mono_mul(a, b, G).items():
                out[w] = out.get(w, 0) + ca * cb * c
    return {w: c for w, c in out.items() if c}


def rev(x):
    out = {}
    for w, c in x.items():
        k = len(w)
        # reversal of e_{i1}..e_{ik} = e_ik..e_i1 = (-1)^{k(k-1)/2} e_{i1}..e_{ik} for distinct anticommuting? no:
        # anticommutation only up to 2G_ij terms, so compute honestly
        out = add(out, scal(revword(w), c))
    return out


GLOBAL_G = None


def revword(w):
    r = {(): Fr(1)}
    for i in reversed(w):
        r = mul(r, {(i,): Fr(1)}, GLOBAL_G)
    return r


def add(x, y):
    out = dict(x)
    for w, c in y.items():
        out[w] = out.get(w, 0) + c
    return {w: c for w, c in out.items() if c}


def scal(x, c):
    return {w: v * c for w, v in x.items()}


BAS = [(), (0, 1), (1, 2), (0, 2)]


def to_vec(x):
    assert all(len(w) % 2 == 0 for w in x)
    return [x.get(w, Fr(0)) for w in BAS]


def from_vec(c):
    return {w: Fr(v) for w, v in zip(BAS, c) if v}


def nrd(x):
    s = mul(x, rev(x), GLOBAL_G)
    assert set(s) <= {()}, s
    return s.get((), Fr(0))


def trd(x):
    s = add(x, rev(x))
    assert set(s) <= {()}
    return s.get((), Fr(0))


def overorder(G):
    """unique index-2 overorder of C0 = Z<BAS>. Returns list of basis vectors (C0 coords)."""
    basis0 = [[Fr(int(i == j)) for j in range(4)] for i in range(4)]
    found = []
    for c in product((0, 1), repeat=4):
        if not any(c):
            continue
        y = [Fr(ci, 2) for ci in c]
        gens = basis0 + [y]
        def inN(z):
            for k in (0, 1):
                if all((zi - k * yi).denominator == 1 for zi, yi in zip(z, y)):
                    return True
            return False
        ok = True
        for a in gens:
            for b in gens:
                if not inN(to_vec(mul(from_vec(a), from_vec(b), G))):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            found.append(c)
    assert len(found) == 1, found
    c = found[0]
    # Z-basis of C0 + Z y/2: replace a basis vector with odd coefficient
    k = max(i for i in range(4) if c[i])
    B = [basis0[i] for i in range(4) if i != k] + [[Fr(ci, 2) for ci in c]]
    return B


SHARP = 0

def run(P, M):
    global GLOBAL_G
    bad = 0; checked = 0
    for p in primes_1mod4(5, P):
        cls = [k for k in classes_det_p(p) if aniso_at_p(key_to_gram(k), p)]
        for k in cls:
            G = key_to_gram(k)
            GLOBAL_G = G
            B = overorder(G)
            # nrd Gram on E basis
            els = [from_vec(b) for b in B]
            N = [[(nrd(add(els[i], els[j])) - nrd(els[i]) - nrd(els[j])) / 2 if i != j else nrd(els[i]) for j in range(4)] for i in range(4)]
            Mmax = min(M, (p * p) // (4 * p) + 5)
            sv = short_vectors(N, Mmax * p)
            trB = [trd(e_) for e_ in els]
            cnt = {}
            for q, x in sv:
                if q % p == 0:
                    m = int(q // p)
                    tr = sum(x[i] * trB[i] for i in range(4))
                    cnt.setdefault(m, [0, 0])
                    cnt[m][0] += 1
                    cnt[m][1] += (tr != 0)
            r = rep_counts(G, Mmax)
            for m in range(1, Mmax + 1):
                c_all, c_tr = cnt.get(m, [0, 0])
                checked += 1
                if 4 * m < p:
                    if c_all != r[m] or c_tr:
                        bad += 1; print('BAD', p, k, m, c_all, c_tr, r[m])
                elif c_tr:
                    global SHARP
                    SHARP += 1
    print('P', P, 'M', M, 'checks', checked, 'bad', bad, 'nonzero-trace elements seen at m>=p/4 (expected to exist):', SHARP)

if __name__ == '__main__':
    run(int(sys.argv[1]), int(sys.argv[2]))
