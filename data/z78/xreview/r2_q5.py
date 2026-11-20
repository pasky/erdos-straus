# Sanity probe "does the §6 skeleton prove too much?": Case B tuples (k=2) over F_p, p=5 (or 7),
# depth at slice points u=1+cT. If coverings exist for N>=4 the char-3-specific steps are load-bearing.
import sys, itertools
PR = int(sys.argv[1]) if len(sys.argv) > 1 else 5
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 7
def nrm(a):
    a = [x % PR for x in a]
    while a and a[-1] == 0: a.pop()
    return a
def add(a, b, s=1):
    n = max(len(a), len(b)); return nrm([(a[i] if i < len(a) else 0)+s*(b[i] if i < len(b) else 0) for i in range(n)])
def mul(a, b):
    if not a or not b: return []
    o = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): o[i+j] += x*y
    return nrm(o)
def dvm(a, b):
    a = a[:]; q = [0]*max(0, len(a)-len(b)+1); il = pow(b[-1], PR-2, PR)
    while a and len(a) >= len(b):
        s = len(a)-len(b); f = (a[-1]*il) % PR; q[s] = f
        for i, y in enumerate(b): a[i+s] = (a[i+s]-f*y) % PR
        a = nrm(a)
    return nrm(q), a
def val(a):
    i = 0
    while a[i] == 0: i += 1
    return i
def mt(d):
    if d == 0: yield [1]; return
    for low in itertools.product(range(PR), repeat=d):
        if low[0]: yield list(low)+[1]
for n in range(2, NMAX+1):
    s = n+2; Nmin = -(-s//2); need = Nmin+1
    best = {c: (0, None) for c in range(1, PR)}; cnt = 0
    Tn = [0]*n+[1]
    for z in range(n+1):
        for a1 in range(n-z+1):
            b1 = n-z-a1
            Cs = list(mt(b1))
            for m in mt(z):
                for w in mt(a1):
                    mw = mul(m, w)
                    for C in Cs:
                        if (w[0]+C[0]) % PR: continue
                        V = add(mul(mw, C), Tn, -1)
                        if not V or V[0] == 0: continue
                        g, r = dvm(add(w, C), [0]+V)
                        if r or not g or g[-1] != 1 or g[0] == 0: continue
                        cnt += 1
                        for c in range(1, PR):
                            dep = val(add(w, mul([1, c], C)))
                            if dep > best[c][0]: best[c] = (dep, (m, w, C, g, V))
    print('p=%d n=%d s=%d N(s)=%d need dep>=%d tuples=%d' % (PR, n, s, Nmin, need, cnt),
          {c: best[c][0] for c in best}, 'COVER' if any(best[c][0] >= need for c in best) else '', flush=True)
    for c in best:
        if best[c][0] >= need: print('   c=%d witness m,w1,C1,g,V =' % c, best[c][1])
