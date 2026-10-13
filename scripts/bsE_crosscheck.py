"""bsE_crosscheck.py (O178): cross-check bsE_famcount (enumeration via (w, C)) against O173's ff3_caseB
(enumeration via (L', j, gamma) and least CRT residues) at random points of the c-slice, q = 3, k = 2.
For random u (u0 = 1), every ff3_caseB hit with s = N+1+gamma <= SMAX must be a famcount tuple, and every famcount
tuple whose maximal cylinder (N(s) = ceil(s/2)) contains u and has deg L' <= LMAX, j <= JMAX must appear among the hits.
usage: uv run python scripts/bsE_crosscheck.py tuples.txt ff3_binary NPOINTS SEED"""
import sys, random, subprocess, re
P = 3

def norm(a):
    a = [x % P for x in a]
    while a and a[-1] == 0: a.pop()
    return a
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return norm(r)
def add(a, b):
    n = max(len(a), len(b)); return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])
def divmod_(a, b):
    a = norm(a); b = norm(b); q = [0] * max(0, len(a) - len(b) + 1); inv = pow(b[-1], P - 2, P)
    while len(a) >= len(b):
        f = a[-1] * inv % P; s = len(a) - len(b); q[s] = f
        a = norm([a[i] - (f * b[i - s] if 0 <= i - s < len(b) else 0) for i in range(len(a))])
    return norm(q), a
def T(n): return [0] * n + [1]
def plist(s): return norm([int(x) for x in s.strip('[]').split(',')]) if s.strip('[]') else []

def load(fn):
    tup = set(); rows = []
    for line in open(fn):
        d = dict(re.findall(r"(\S+?)=(\S+)", line))
        s = int(d['s']); w = plist(d['w']); C = plist(d['C']); m = plist(d["m'"]); g = plist(d["g'"])
        tup.add((s, tuple(w), tuple(C), tuple(m), tuple(g))); rows.append((s, w, C, m, g))
    return tup, rows

if __name__ == "__main__":
    fn, ff3, npts, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    SMAX, LMAX, JMAX = 12, 4, 5
    tup, rows = load(fn); rng = random.Random(seed); bad = 0; nh = 0; nt = 0
    for _ in range(npts):
        u = [1, rng.randrange(1, P)] + [rng.randrange(P) for _ in range(16)]
        out = subprocess.run([ff3, str(P), "2", "0", str(LMAX), str(JMAX)] + [str(x) for x in u],
                             capture_output=True, text=True, check=True).stdout
        hits = set()
        for line in out.splitlines():
            if not line.startswith("HIT"): continue
            d = dict(re.findall(r"(\S+?)=(\S+)", line))
            j, gam = int(d['j']), int(d['gam']); s = 2 + j + gam
            L = plist(d["L'"]); g = plist(d["g'"]); D = add(mul(mul(T(s), L), g), [1])
            if d['br'] == '0': E = plist(d['E']); Ep, r = divmod_(D, E)
            else: Ep = plist(d["E'"]); E, r = divmod_(D, Ep)
            assert not r
            w, r1 = divmod_(add(E, [1]), L); C, r2 = divmod_(add(Ep, [1]), L); m, r3 = divmod_(L, g)
            assert not r1 and not r2 and not r3
            key = (s, tuple(w), tuple(C), tuple(m), tuple(g)); hits.add(key)
            if s <= SMAX:
                nh += 1
                if key not in tup: bad += 1; print("ff3 hit not in famcount:", key)
        for (s, w, C, m, g) in rows:
            N = (s + 1) // 2; j = N - 1; gam = s - N - 1
            L = mul(g, m)
            if len(L) - 1 > LMAX or j > JMAX: continue
            E = add(mul(L, w), [P - 1])
            if all(((E[i] if i < len(E) else 0) + (u[i] if i < len(u) else 0)) % P == 0 for i in range(N + 1)):
                nt += 1
                if (s, tuple(w), tuple(C), tuple(m), tuple(g)) not in hits: bad += 1; print("famcount tuple missed by ff3:", s, w, C, m, g)
    r_ = 0
    print("points %d, ff3 hits (s<=%d) %d, famcount tuples covering %d, mismatches %d" % (npts, SMAX, nh, nt, bad))
    sys.exit(1 if bad else 0)
