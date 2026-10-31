# Z1665: forms fixed by ES5/SL2 words gamma=[[a,p],[c,d]], c=4C, a=cu-1, d=cB-1.
# Fixed form Q = c x^2 + (d-a) xy - p y^2, disc (a+d)^2-4. Check: values c,-p adjacent (river edge),
# river period, and whether the form is the X-certificate ambiguous form of WINDMILL_REDUCTION §5.2/§8.
import math,sys
def isprime(n):
    return n>1 and all(n%q for q in range(2,int(n**.5)+1))
def river(f):
    a,b,c=f; D=b*b-4*a*c; seen=[]; cur=(a,b,c)
    while True:
        seen.append(cur); a,b,c=cur
        cur=(a+b+c,b+2*c,c) if a+b+c>0 else (a,b+2*a,a+b+c)
        if cur==f or len(seen)>10**5: break
    return seen
P=int(sys.argv[1]) if len(sys.argv)>1 else 500
for p in [q for q in range(5,P) if isprime(q) and q%4==1]:
    words=[]
    for C in range(1,p):
        c=4*C
        for u in range(1,p):
            if c*u-u-1>p: break
            # c u B - u - B = p  -> B = (p+u)/(c u -1)
            if (p+u)%(c*u-1)==0:
                B=(p+u)//(c*u-1); a,d=c*u-1,c*B-1
                assert a*d-p*c==1
                f=(c,d-a,-p); D=(a+d)**2-4
                assert f[1]**2-4*f[0]*f[2]==D
                r=river(f)
                words.append((C,u,B,D,len(r), min(abs(x[0]) for x in r)))
    if p in (409,) or p<120:
        print(p, len(words), words[:4])
