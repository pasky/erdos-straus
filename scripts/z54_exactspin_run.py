# z54 EXACTSPIN driver: runs scripts/z54_exactspin_engine.c (compiled to $ENG, default /tmp/z54es) on a list of n,
# standard GENUSX window U0=floor(n^(1/12)), U1=floor(n^(1/3)/2), Y=floor(n^(1/3)), X=floor(n^(2/3)/4) (8 U1 X <= n).
# Usage: python scripts/z54_exactspin_run.py OUT.tsv TAG n1 n2 ... | TAG @file
import sys, os, subprocess
ENG = os.environ.get('ENG', '/tmp/z54es')
def window(n):
    U0 = int(round(n ** (1 / 12) - 0.5)); U1 = int(n ** (1 / 3) / 2); Y = int(n ** (1 / 3)); X = int(n ** (2 / 3) / 4)
    while 8 * U1 * X > n: X -= 1
    return max(U0, 1), U1, Y, X
if __name__ == '__main__':
    outp, tag = sys.argv[1], sys.argv[2]
    ns = []
    for a in sys.argv[3:]:
        if a.startswith('@'): ns += [int(x) for x in open(a[1:]).read().split()]
        else: ns.append(int(a))
    new = not os.path.exists(outp)
    with open(outp, 'a') as fo:
        for n in ns:
            U0, U1, Y, X = window(n)
            out = subprocess.run([ENG, str(n), str(U0), str(U1), str(Y), str(X)], capture_output=True, text=True, timeout=1700)
            if out.returncode != 0: raise RuntimeError(out.stderr)
            kv = [t.split('=') for t in out.stdout.split()]
            if new: fo.write('tag\t' + '\t'.join(k for k, v in kv) + '\n'); new = False
            fo.write(tag + '\t' + '\t'.join(v for k, v in kv) + '\n'); fo.flush()
