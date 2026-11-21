"""Independent (Opus R2 reviewer) checks of notes/z80/PROTH_CORE.md Theorem 9 (§6).
No repository script imported.  PARI only for znorder/kronecker/isprime.
 (1) coverage of r2/cover-11.json by a CRT-fibre sieve (different algorithm from the repo's
     recursive prime partition): L = 3825360*130169; bytearray sieve mod 3825360 with rows P|3825360,
     then a full Z/130169 sieve on every surviving fibre; lists every uncovered residue mod L;
 (2) per-row transfer at m = 11 + T' (T' = transfer.json T, 587 digits): compute n mod the row's
     own test modulus and check the rule from first principles (Mordell classes listed by hand,
     direct divisor triples, II / K triple formulas reduced mod Q, word with the ACTUAL Jacobi
     symbol (tu-1 / n) = -1 rather than the 8|(n+t)tuv criterion);
 (3) per-row actual-integer transfer at the smallest m_R = 11 + ord_{Q_odd}(4) when that order
     is <= ORDMAX: real triples / real Jacobi symbols for several s >= 64 in the row's class;
 (4) the gcd rule gcd(2m+1, s-1) > 1 with real triples on 1<=m<=150, 1<=s<=1500 and the
     arithmetic side conditions of the epsilon construction (36|T', 23|T', 23|L, gcd tests).
Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project --with cypari2 python -B opus_r2_cover.py
"""
import json, sys
from math import gcd, lcm
from pathlib import Path
from cypari2 import Pari
pari = Pari()
R = Path(__file__).resolve().parents[1] / 'proth'
ORDMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
MORDELL_BAD = {1, 121, 169, 289, 361, 529}          # Mordell: ES unless n in these classes mod 840

def tri_ok(n, x, y, z):
    return min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + z * x)

def direct(q):
    """Smallest-x search for 4/q = 1/x + 1/y + 1/z (q small)."""
    for x in range(q // 4 + 1, 4 * q):
        num, den = 4 * x - q, q * x           # remaining num/den = 1/y + 1/z
        g = gcd(num, den); num //= g; den //= g
        for y in range(den // num + 1, 2 * den // num + 1):
            r = num * y - den
            if r > 0 and (den * y) % r == 0:
                return x, y, den * y // r
    raise ValueError(q)

def modulus(row):
    P, j, t, *a = row
    if t == 'M': return 840
    if t == 'W': return 8 * a[0]
    if t == 'K':
        f, K, A, B = a
        return 4 * f * K if A[2] or B[2] else 4 * lcm(f, K)
    return a[0]

def check_mod(row, nr, Q):
    """Rule check knowing only nr = n mod Q (plus n huge, n = 1 mod 2^8)."""
    P, j, t, *a = row
    if t == 'M':
        return nr % 840 not in MORDELL_BAD
    if t == 'D':
        return nr % a[0] == 0
    if t == 'II':
        f, x, y = a                             # need (f+1) = 4xyd and f | y n + x
        return (f + 1) % (4 * x * y) == 0 and (y * nr + x) % f == 0
    if t == 'W':
        A, u = a; tt, r = divmod(A + 1, u)
        if r or tt < 2 or u < 2 or (nr + u) % A: return False
        rep = nr if nr % 2 else nr + Q          # positive odd representative, same class mod 8A
        return int(pari.kronecker(A, rep)) == -1 and rep % 4 == 1
    if t == 'K':
        f, K, Dd, Ee = a
        if f % 4 != 3 or (nr + f) % (4 * K): return False
        Kp = ((nr + f) // (4 * K))               # valid mod f only when Q = 4fK (b=1 terms)
        def val(V):
            d, i, b = V
            assert K % d == 0
            return d * nr ** i * Kp ** b
        return (val(Dd) + val(Ee)) % f == 0
    raise ValueError(t)

def check_actual(row, n):
    P, j, t, *a = row
    if t == 'M': return n % 840 not in MORDELL_BAD
    if t == 'D':
        q = a[0]
        if n % q: return False
        x, y, z = direct(q); c = n // q
        return tri_ok(n, c * x, c * y, c * z)
    if t == 'II':
        f, x, y = a
        d = (f + 1) // (4 * x * y); e, r = divmod(n + 4 * x * x * d, f)
        if r: return False
        bp, r2 = divmod(n + e, 4 * x * d)
        return r2 == 0 and tri_ok(n, x * bp * d, x * y * d * n, bp * y * d * n)
    if t == 'W':
        A, u = a; tt = (A + 1) // u
        if (n + u) % A: return False
        v = (n + u) // A
        return n == tt * u * v - u - v and v >= 2 and int(pari.kronecker(A, n)) == -1 and n % 4 == 1
    if t == 'K':
        f, K, Dd, Ee = a
        if (n + f) % (4 * K): return False
        Kp = (n + f) // (4 * K); y = (n + f) // 4
        def val(V):
            d, i, b = V; return d * n ** i * Kp ** b
        A, B = val(Dd), val(Ee)
        if (A + B) % f: return False
        w = (A + B) // f
        return (n * y) % A == 0 and (n * y) % B == 0 and tri_ok(n, y, n * y // A * w, n * y // B * w)
    raise ValueError(t)

def fibre_cover(rows, L, A):
    """L = A*B, gcd(A,B)=1.  Sieve mod A with the rows P|A; on each surviving fibre r mod A
    sieve Z/B with the compatible rows (class j mod gcd(P,B)).  Returns uncovered residues mod L."""
    B = L // A; assert gcd(A, B) == 1
    top = bytearray(b'\1') * A; other = []
    for P, j, *_ in rows:
        if A % P == 0: top[j::P] = bytes(len(range(j, A, P)))
        else: other.append((P, j))
    fibres = [r for r in range(A) if top[r]]
    print('    fibres mod', A, 'surviving the P|A rows:', len(fibres))
    left = []
    for r in fibres:
        arr = bytearray(b'\1') * B
        for P, j in other:
            pa = gcd(P, A)
            if (j - r) % pa: continue
            pb = P // pa; assert B % pb == 0
            jb = j % pb
            arr[jb::pb] = bytes(len(range(jb, B, pb)))
        for y in range(B):
            if arr[y]:
                left.append(int(pari.chinese(pari.Mod(r, A), pari.Mod(y, B)).lift()))
    return sorted(left)

def main():
    c = json.loads((R / 'r2/cover-11.json').read_text())
    tr = json.loads((R / 'r2/transfer.json').read_text())
    L = c['period']; Tp = int(tr['T']); T79 = int(json.loads((R.parents[1] / 'z79/proth/intersection.json').read_text())['T'])
    assert L == 497943285840 == 130169 * 3825360 and Tp == 3 * T79
    rows = c['rows']
    assert all(L % r[0] == 0 and 0 <= r[1] < r[0] for r in rows)
    assert all(r[1] % r[0] != 0 for r in rows), 'some row contains 0 mod L'
    left = fibre_cover(rows, L, 3825360)
    print('(1) CRT-fibre cover (A=3825360, B=130169): uncovered residues mod L =', left)
    assert left == [0]
    # (2) modular transfer at m = 11 + T' and m = 11 + 2T'
    for mm in (11, 11 + Tp, 11 + 2 * Tp):
        bad = 0
        for row in rows:
            P, j = row[0], row[1]; Q = modulus(row)
            dy = Q & -Q; assert dy <= 2 ** 64
            kq = (pow(4, mm, Q) - 1) % Q
            for i in range(3):
                s = j + P * ((64 + P - 1) // P + i)
                nr = (kq * pow(2, s, Q) + 1) % Q
                if not check_mod(row, nr, Q): bad += 1; print('FAIL mod', mm == 11, row[:3], s)
        print('(2) modular rule check at m =', 'm11' if mm == 11 else '11+%dT\'' % ((mm - 11) // Tp), 'failures', bad)
        assert bad == 0
    # (3) actual integers at small m_R = 11 + ord_{Q_odd}(4)
    tested = 0; skipped = 0
    for row in rows:
        P, j = row[0], row[1]; Q = modulus(row); o = Q // (Q & -Q)
        ordr = 1 if o == 1 else int(pari.znorder(pari.Mod(4, o)))
        assert Tp % ordr == 0
        for mm in ([11] + ([11 + ordr, 11 + 2 * ordr] if ordr <= ORDMAX else [])):
            k = 4 ** mm - 1
            for i in range(4):
                s = j + P * ((64 + P - 1) // P + i)
                if s > 6000: break
                n = k * 2 ** s + 1
                assert check_actual(row, n), (row[:3], mm, s)
                tested += 1
        if ordr > ORDMAX: skipped += 1
    print('(3) actual-integer rule checks:', tested, 'instances; rows with ord>ORDMAX tested only at m=11:', skipped)
    # (4) gcd rule and epsilon side conditions
    cnt = 0
    for m in range(1, 151):
        k = 4 ** m - 1
        for s in range(1, 1501):
            g = gcd(2 * m + 1, s - 1)
            if g > 1:
                q = 2 ** g - 1; n = k * 2 ** s + 1
                assert n % q == 0 and q % 4 == 3
                a = (q + 1) // 4; cc = n // q
                assert tri_ok(n, a * cc, 2 * a * q * cc, 2 * a * q * cc); cnt += 1
    O = int(tr['O']); M = Tp // (Tp & -Tp); z = 21 - 2 ** 14
    assert Tp % 36 == 0 and Tp % 23 == 0 and L % 23 == 0 and O % 4 == 0 and pow(2, O, M) == 1
    assert gcd(z, M) == 1 and gcd(z - 1, gcd(M, O)) == 1 and tr['b'] == 14
    assert (2 * 11 + 1) % 23 == 0 and (Tp & -Tp) >= 4
    print('(4) gcd-rule triples:', cnt, '; epsilon side conditions OK; v2(T\') =', (Tp & -Tp).bit_length() - 1,
          '; odd primes of gcd(M,z-1):', [int(p) for p in pari.factor(gcd(M, z - 1))[0]] if gcd(M, z - 1) > 1 else [])

if __name__ == '__main__':
    main()
