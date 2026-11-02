# z54 EXACTSUM driver: conductor profile engine (scripts/z54_exactsum_cond.c) over a list of n.
# Usage: python scripts/z54_exactsum_run.py OUT.tsv TAG WINDOW n1 n2 ... | @file
#   WINDOW = std : U0=n^(1/12), U1=n^(1/3)/2, Y=n^(1/3), X=n^(2/3)/4           (Z53_GENUSX standard window)
#   WINDOW = dyad / dyad16 : the dyadic u-slice (U1/2, U1] of std with U1 = n^(1/3)/2 resp. n^(1/3)/32
#   WINDOW = thx : alpha1=19/120, alpha0=(1+alpha1)/16, beta=2alpha1+1/4, gamma: X = n^(1-alpha1)/8  (Thm X optimum, r->inf)
# Requires ENG (default /tmp/z54es) compiled from scripts/z54_exactsum_cond.c.
import sys, os, subprocess, math
ENG = os.environ.get('ENG', '/tmp/z54es')

def window(n, kind):
    if kind == 'std':
        U0 = int(round(n ** (1 / 12) - 0.5)); U1 = int(n ** (1 / 3) / 2); Y = int(n ** (1 / 3)); X = int(n ** (2 / 3) / 4)
    elif kind == 'thx':
        a1 = 19 / 120; a0 = (1 + a1) / 16; b = 2 * a1 + 0.25
        U0 = int(n ** a0); U1 = int(n ** a1); Y = int(n ** b); X = int(n ** (1 - a1) / 8)
    elif kind in ('dyad', 'dyad16'):   # one dyadic u-slice (U1/2, U1] of the standard window; dyad16: U1 = n^(1/3)/32
        U1 = int(n ** (1 / 3) / (2 if kind == 'dyad' else 32)); U0 = U1 // 2; Y = int(n ** (1 / 3)); X = int(n ** (2 / 3) / 4)
    else:
        raise ValueError(kind)
    while 8 * U1 * X > n: X -= 1
    return max(U0, 1), U1, Y, X

if __name__ == '__main__':
    outp, tag, kind = sys.argv[1], sys.argv[2], sys.argv[3]
    ns = []
    for a in sys.argv[4:]:
        if a.startswith('@'): ns += [int(x) for x in open(a[1:]).read().split()]
        else: ns.append(int(a))
    new = not os.path.exists(outp)
    with open(outp, 'a') as fo:
        for n in ns:
            U0, U1, Y, X = window(n, kind)
            out = subprocess.run([ENG, str(n), str(U0), str(U1), str(Y), str(X)], capture_output=True, text=True, timeout=1700)
            if out.returncode != 0: raise RuntimeError(out.stderr)
            kv = dict(t.split('=') for t in out.stdout.split())
            if new:
                fo.write('tag\twin\t' + '\t'.join(kv.keys()) + '\n'); new = False
            fo.write(tag + '\t' + kind + '\t' + '\t'.join(kv.values()) + '\n'); fo.flush()
