# z53 GENUSX driver: exact family sums (C engine) + genus main term M_hat via class numbers.
# Usage: uv run --with cypari2 python scripts/z53_genusx_run.py OUT.tsv TAG n1 n2 ...   (or TAG @file with one n per line)
# Window (standard family): U0 = floor(n^(1/12)), U1 = floor(n^(1/3)/2), Y = floor(n^(1/3)), X = floor(n^(2/3)/4).
# M_hat = sum_{u in U} H_u(1) L(1, chi_{-4un}) log(X/Y) / phi(u)  (Thm U window closed form; eta != 1 windows -> 0),
# H_u(1) = (6/pi^2) prod_{l | 2un} l/(l+1).  For non-prime n (controls) M_hat is not computed (NaN).
# With env DIRECT=1 also runs engine mode D (exact M and Mcls by direct summation; small n only).
import sys, os, subprocess, math
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
ENG = os.environ.get('ENG', '/tmp/z53gx')

def window(n):
    U0 = int(round(n ** (1 / 12) - 0.5)); U1 = int(n ** (1 / 3) / 2); Y = int(n ** (1 / 3)); X = int(n ** (2 / 3) / 4)
    while 8 * U1 * X > n: X -= 1
    return max(U0, 1), U1, Y, X

def mhat(n, U0, U1, Y, X):
    s = 0.0; lg = math.log(X / Y)
    for u in range(U0 + 1, U1 + 1):
        if u % 4 != 1: continue
        f = pari.factor(u); ps = [int(q) for q in f[0]]; es = [int(e) for e in f[1]]
        if any(e > 1 for e in es) or n % u == 0 and u > 1: continue
        if any(n % q == 0 for q in ps): continue
        D = -4 * u * n
        h = int(pari.quadclassunit(D)[0])
        L = math.pi * h / math.sqrt(-D)
        H = (6 / math.pi ** 2) * (2 / 3) * (n / (n + 1))
        phi = 1
        for q in ps: H *= q / (q + 1); phi *= (q - 1)
        s += H * L * lg / phi
    return s

def run(n, tag, direct):
    U0, U1, Y, X = window(n)
    mode = 'D' if direct else 'E'
    out = subprocess.run([ENG, mode, str(n), str(U0), str(U1), str(Y), str(X)], capture_output=True, text=True, timeout=1700)
    if out.returncode != 0: raise RuntimeError(out.stderr)
    kv = dict(t.split('=') for t in out.stdout.split())
    isp = bool(pari.isprime(n))
    M = mhat(n, U0, U1, Y, X) if isp else float('nan')
    cols = [tag, str(n), '%.4f' % math.log(n), kv['R'], kv['G'], kv['E1'], kv['C4'], kv['CU0'], kv['CBM'], kv['REST'], '%.6f' % M,
            kv.get('M', 'nan'), kv.get('Mcls', 'nan'), kv['shell'], kv['hits'], kv['lemma2_bad'], kv['fullbad'], kv['G4'], kv['G6'], kv['G12'], kv['G120'], str(U0), str(U1), str(Y), str(X)]
    return '\t'.join(cols)

if __name__ == '__main__':
    outp, tag = sys.argv[1], sys.argv[2]
    ns = []
    for a in sys.argv[3:]:
        if a.startswith('@'): ns += [int(x) for x in open(a[1:]).read().split()]
        else: ns.append(int(a))
    direct = os.environ.get('DIRECT') == '1'
    new = not os.path.exists(outp)
    with open(outp, 'a') as fo:
        if new: fo.write('tag\tn\tlogn\tR\tG\tE1\tC4\tCU0\tCBM\tREST\tMhat\tMdirect\tMcls\tshell\thits\tl2bad\tfullbad\tG4\tG6\tG12\tG120\tU0\tU1\tY\tX\n')
        for n in ns:
            fo.write(run(n, tag, direct) + '\n'); fo.flush()
