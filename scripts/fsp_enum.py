"""fsp_enum.py (O179, FF_STERILE_PROOF.md): independent enumerator of all Case B solutions on the slice
x = 1 off T, q = 3, A = T^2 (SIGNLAYER_DEEP Lemma 1.1), for levels K <= KMAX, printing FULL tuples.
Solution = monic H, H' (H(0) = -H'(0) != 0), monic g', L'' with nonzero constant terms, r, such that
  (I) H + H' = T g' r,   (II) H H' L'' = T^K + r.
Independent of bsB_caseB.c: own polynomial arithmetic (ints base 3 as coefficient lists), and the test is done
by checking (I),(II) directly after computing L'' = quo(T^K, HH').
Output lines:  K a b H Hp gp Lpp r   (coefficient strings low->high; r written with digits 0..2)
usage: PYTHONPATH=scripts uv run python scripts/fsp_enum.py KMAX > out"""
import sys, itertools

def trim(p):
    while p and p[-1] == 0: p.pop()
    return p
def add(a, b):
    n = max(len(a), len(b)); return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % 3 for i in range(n)])
def neg(a): return [(-x) % 3 for x in a]
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % 3
    return trim(r)
def divmod_(a, b):
    a = a[:]; db = len(b) - 1; inv = 1 if b[-1] == 1 else 2
    q = [0] * max(0, len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] * inv % 3
        if c:
            q[i - db] = c
            for j, y in enumerate(b): a[i - db + j] = (a[i - db + j] - c * y) % 3
    return trim(q), trim(a)
def s(p): return ''.join(map(str, p)) if p else '0'

def monics(d, c0):
    """monic polys of degree d with constant term c0 (d >= 1) as lists"""
    for mid in itertools.product(range(3), repeat=max(0, d - 1)):
        yield [c0] + list(mid) + [1]

def main():
    KMAX = int(sys.argv[1])
    for a in range(0, KMAX + 1):
        for b in range(0, KMAX + 1 - a):
            for c0 in (1, 2):
                Hs = [[1]] if a == 0 else list(monics(a, c0))
                if a == 0 and c0 != 1: continue
                hc0 = Hs[0][0]
                Hps = [[1]] if b == 0 else list(monics(b, (-hc0) % 3))
                if b == 0 and (-hc0) % 3 != 1: continue
                for H in Hs:
                    for Hp in Hps:
                        S = add(H, Hp)
                        if not S or S[0] != 0: continue
                        ST = S[1:]                          # (H+H')/T = g' r
                        HH = mul(H, Hp)
                        for K in range(a + b, KMAX + 1):
                            TK = [0] * K + [1]
                            Lpp, rem = divmod_(TK, HH)
                            r = neg(rem)                    # T^K + r = L'' H H'
                            if not r or not Lpp or Lpp[0] == 0: continue
                            g, z = divmod_(ST, r)
                            if z or not g or g[-1] != 1 or g[0] == 0: continue
                            # verify (I),(II) explicitly
                            assert add(H, Hp) == mul([0, 1], mul(g, r))
                            assert mul(HH, Lpp) == add(TK, r)
                            print(K, a, b, s(H), s(Hp), s(g), s(Lpp), s(r))

if __name__ == '__main__':
    main()
