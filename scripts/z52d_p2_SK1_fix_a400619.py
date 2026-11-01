# z52d pass2 SK1 fix (Z0941): reproduce OEIS A400619 (primes setting records of 4*x_min - p, x_min = least denominator
# over all solutions of 4/p) from our count.c data (col 8 = minx), primes <= 1e5.
rows=[l.split() for l in open('data/z52b/pass2/SK1/Z0707_count4_primes1e5.txt')]
best=-10**9; recs=[]
for r in rows:
    p=int(r[0]); minx=int(r[8])
    if minx==0: continue
    v=4*minx-p
    if v>best: best=v; recs.append((p,v))
A=[2,5,73,1129,1201,21169]
print("record primes (p, 4xmin-p):", recs)
print("match A400619 terms <= 1e5:", [p for p,_ in recs]==A)
