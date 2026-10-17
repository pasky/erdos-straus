"""O258 item (vi): which T1-adjacent points x_{l,r} (x = r in Z_l, x = 1 in Z_q for all q != l) lie in an ET witness
class of numerator k?  (Generalises O257 NONCONG_LIFTS Thm 2.6, which is r = 2.)
Witness class (theta, a, b, c), e = (a+b)/c, H = k a b: II needs H | x + e, I needs H | x e + 1, for x = x_{l,r} mod H, i.e.
  II: e == -1 mod H', e == -r mod l^v;   I: e == -1 mod H', r e == -1 mod l^v   (H = H' l^v, l coprime to H').
Usage: PYTHONPATH=scripts uv run python scripts/s8_xlr_points.py B
"""
import sys

def isp(n): return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
def is_qr(r, l): return pow(r % l, (l - 1) // 2, l) == 1

def covered(k, l, r, B):
    hits = []
    for a in range(1, B + 1):
        for b in range(a, B + 1):
            H = k * a * b; v = 0; Hp = H
            while Hp % l == 0: Hp //= l; v += 1
            if v == 0: continue          # Case 0 impossible (e >= kab - 1 > a + b)
            L = l ** v; s = a + b
            for c in range(1, s + 1):
                if s % c: continue
                e = s // c
                if (e + 1) % Hp == 0:
                    if (e + r) % L == 0: hits.append(("II", a, b, c, e))
                    if (r * e + 1) % L == 0: hits.append(("I", a, b, c, e))
    return hits

if __name__ == "__main__":
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    for k in (4, 8, 12, 16, 20, 24):
        row = []
        for l in [q for q in range(3, 40) if isp(q) and k % q]:
            nonres = [r for r in range(2, l) if not is_qr(r, l)]
            cov = [r for r in nonres if covered(k, l, r, B)]
            unc = [r for r in nonres if r not in cov]
            row.append(f"l={l}: min uncovered-free r={min(cov) if cov else '-'} uncovered={unc}")
        print(f"k={k}:"); [print("   ", x) for x in row]
