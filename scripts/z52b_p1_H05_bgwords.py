# Z1700: image mod q of length-3 ES words gamma = T^u [[-1,0],[c,-1]] T^B = [[cu-1,(cu-1)B-u],[c,cB-1]]
# (c ≡ 0 mod 4 imposed when 4|q) inside SL2(Z/q); fraction covered, and which b-entries (p mod q) occur.
import sys, math
def sl2size(q):
    s=q**3
    for l in range(2,q+1):
        if q%l==0 and all(l%k for k in range(2,l)): s=s*(1-1/l**2)
    return round(s)
for q in list(range(2,41))+[48,60,64,97,120]:
    S=set()
    for c in range(q):
        if q%4==0 and c%4: continue
        for u in range(q):
            a=(c*u-1)%q
            for B in range(q):
                S.add((a,(a*B-u)%q,c,(c*B-1)%q))
    bs={m[1] for m in S}
    units_b=[b for b in range(q) if math.gcd(b,q)==1]
    print(q, len(S), sl2size(q), round(len(S)/sl2size(q),3), "all unit b hit:", all(b in bs for b in units_b))
