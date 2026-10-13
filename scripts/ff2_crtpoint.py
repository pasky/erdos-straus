"""ff2_crtpoint.py (O166): build r mod W = T^e * W' with r = u mod T^e and r = v mod W' (CRT, prime p),
and run /tmp/ff2_point on it.  usage: python ff2_crtpoint.py p A e "W'factors" NTH  (u enumerated, v=1)"""
import sys, subprocess, itertools
sys.path.insert(0, 'scripts')
from ff2_polyq import *
def egcd(a, b, p):
    # returns (g, s, t) with s a + t b = g
    r0, r1, s0, s1, t0, t1 = a, b, [1], [], [], [1]
    while r1:
        q, r = divmod_(r0, r1, p)
        r0, r1 = r1, r; s0, s1 = s1, sub(s0, mul(q, s1, p), p); t0, t1 = t1, sub(t0, mul(q, t1, p), p)
    inv = pow(r0[-1], p - 2, p)
    return [x * inv % p for x in r0], [x * inv % p for x in s0], [x * inv % p for x in t0]
def crt(u, m1, v, m2, p):
    g, s, t = egcd(m1, m2, p); assert g == [1]
    M = mul(m1, m2, p)
    return mod(add(mul(mul(u, t, p), m2, p), mul(mul(v, s, p), m1, p), p), M, p)
def tostr(a): return ''.join(str(c) for c in reversed(a)) if a else '0'
if __name__ == '__main__':
    p, A, e, Wf, NTH = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5]
    vstr = sys.argv[6] if len(sys.argv) > 6 else '1'
    W2 = [1]
    for f in Wf.split('*'): W2 = mul(W2, parse(f, p), p)
    Te = [0] * e + [1]
    for coeffs in itertools.product(range(p), repeat=e):
        u = trim(list(coeffs))
        if not u or u[0] == 0: continue
        r = crt(u, Te, parse(vstr, p), W2, p)
        out = subprocess.run(['/tmp/ff2_point', str(p), A, '*'.join(['10'] * e) + '*' + Wf, tostr(r), NTH], capture_output=True, text=True).stdout.strip()
        print(tostr(u), out, flush=True)
