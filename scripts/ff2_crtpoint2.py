"""ff2_crtpoint2.py (O166): slice test.  x = u mod ell^e (u enumerated over units), x = v mod W' (v given).
usage: python ff2_crtpoint2.py p A ell e "W'factors" v NTH"""
import sys, subprocess, itertools
sys.path.insert(0, 'scripts')
from ff2_polyq import *
from ff2_crtpoint import crt, tostr
p, A, ell, e, Wf, vstr, NTH = int(sys.argv[1]), sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5], sys.argv[6], sys.argv[7]
L = parse(ell, p); Le = [1]
for _ in range(e): Le = mul(Le, L, p)
W2 = [1]
for f in Wf.split('*'): W2 = mul(W2, parse(f, p), p)
v = mod(parse(vstr, p), W2, p)
for coeffs in itertools.product(range(p), repeat=len(Le) - 1):
    u = trim(list(coeffs))
    if not mod(u, L, p): continue
    r = crt(u, Le, v, W2, p)
    out = subprocess.run(['/tmp/ff2_point', str(p), A, '*'.join([ell] * e) + '*' + Wf, tostr(r), NTH], capture_output=True, text=True).stdout.strip()
    print(tostr(u), out, flush=True)
