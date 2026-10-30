# sanity check of reformulations in batch 05 (items 'one-parameter' and 'divisor-shift')
def R_brute(p):
    c=0
    for u in range(1,p+1):
        for B in range(1,p+1):
            if 4*u*B-u-B>p: break
            if (p+u+B)%(4*u*B)==0: c+=1
    return c
def R_m(p):
    c=0
    for m in range(3,4*p+8,4):
        r=(-p)%m
        if r and ((m+1)//4)%r==0: c+=1
    return c
def R_shift(p):
    c=0
    for B in range(1,p+2):
        n=p+B
        c+=sum(1 for s in range(1,n+1) if n%s==0 and (s+1)%(4*B)==0)
    return c
for p in [5,13,17,29,37,41,53,409,1009]:
    print(p,R_brute(p),R_m(p),R_shift(p))
