# Pattern-level check of the §6 degree test: enumerate all integer degree patterns allowed by §§1-3
# (c=1, both orientations, both n) and record which survive deg(pMW) >= N (the only escape from (6.1)).
import sys
from collections import Counter
Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 120
surv = Counter(); bad = []; total = 0
for N in range(4, Nmax+1):
    K = N+1
    for n in (2*N-3, 2*N-2):
        b = n-K; dl = N-b
        for o, P, Q in (('A', 0, 1), ('B', 1, 0)):
            for d in range(0, n+1):
                L = n-d
                if (o == 'A' and L < N) or (o == 'B' and L < N+1): continue
                h = L+Q-K
                if h < 0: continue
                for r in range(0, d+1):
                    z = d-r
                    if (z-n) % 2: continue
                    if d+r+P < K: continue
                    if not (L > r+1): bad.append(('L<=r+1', N, n, o, d, r)); continue
                    for v in range(0, L):
                        y = L-1-v
                        if (v-n) % 2: continue
                        if o == 'A' and d+y < N: continue
                        if o == 'B' and d+y < N-1: continue
                        w = r-v+2*P-1
                        if w < 0 or w > 1+P: continue
                        if b+P-v < 0: continue     # deg S >= 0
                        total += 1
                        deg1 = P+d+w; deg2 = N+b+3*Q-d-r
                        assert deg2 == dl+Q+z+2*h
                        if deg2 >= N or deg2 < dl: bad.append(('deg2', N, n, o, d, r, v)); continue
                        if deg1 > N: bad.append(('deg1>N', N, n, o, d, r, v)); continue
                        if deg1 == N:
                            surv[(o, dl, d == b, w, h)] += 1
print('patterns allowed by §§1-3 (N=4..%d):' % Nmax, total)
print('survivors of degree test (orient, delta, d==b, w, h):', dict(surv))
print('anomalies:', bad[:10], len(bad))
