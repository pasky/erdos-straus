# z51_ffield_c2check.py — numerical check of Lemma C2 (EXSET_FUNCTION_FIELD §3.8):
# pair sum  S2nc(q) = sum over unordered pairs of distinct small classes {u,v} != {u',v'} (deg u, deg v >= 1,
# deg u + deg v <= D) with gcd(uv, u'v') != 1 and compatible residues, of q^{-deg lcm(uv, u'v')}.
# Claim: S2nc(q) = O_D(1/q). (Admissibility parity is ignored: it only removes classes.)
import itertools, sys
def trim(a):
    while a and a[-1] == 0: a.pop()
    return a
def mul(a, b, p):
    r = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j] = (r[i+j] + x*y) % p
    return trim(r)
def sub(a, b, p):
    n = max(len(a), len(b)); r = [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)]
    return trim(r)
def divmod_(a, b, p):
    a = a[:]; inv = pow(b[-1], p-2, p); q = [0]*max(1, len(a)-len(b)+1)
    while len(a) >= len(b) and a:
        c = a[-1]*inv % p; d = len(a)-len(b); q[d] = c
        for i,y in enumerate(b): a[i+d] = (a[i+d] - c*y) % p
        trim(a)
    return trim(q), a
def gcd(a, b, p):
    while b:
        a, b = b, divmod_(a, b, p)[1]
    inv = pow(a[-1], p-2, p); return [x*inv % p for x in a]
def monics(d, p):
    for c in itertools.product(range(p), repeat=d): yield list(c) + [1]
def run(p, D):
    classes = {}
    for a in range(1, D):
        for b in range(1, D - a + 1):
            for u in monics(a, p):
                for v in monics(b, p):
                    M = mul(u, v, p); key = (tuple(M), tuple(sorted([tuple(u), tuple(v)])))
                    r = divmod_(sub([0], [ (x+y) % p for x,y in itertools.zip_longest(u, v, fillvalue=0)], p), M, p)[1]
                    classes[key] = (M, r)
    cl = list(classes.values()); tot = 0.0; npairs = 0
    for i in range(len(cl)):
        Mi, ri = cl[i]
        for j in range(i+1, len(cl)):
            Mj, rj = cl[j]
            g = gcd(Mi, Mj, p)
            if len(g) <= 1: continue
            if divmod_(sub(ri, rj, p), g, p)[1]: continue   # incompatible
            lcmdeg = len(Mi) + len(Mj) - 2 - (len(g) - 1)
            tot += p ** (-lcmdeg); npairs += 1
    return len(cl), npairs, tot
for p in map(int, sys.argv[2:]):
    D = int(sys.argv[1]); n, m, s = run(p, D)
    print(f"D={D} q={p}: classes={n} compatible non-coprime pairs={m} S2nc={s:.5f} q*S2nc={p*s:.4f}", flush=True)
