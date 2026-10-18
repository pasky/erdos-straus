from math import gcd
def anyword(n, step, mult):
    for t in range(step, n+3, step):
        if t % mult: continue
        for u in range(2, n+2):
            a=t*u-1
            if 2*a-u>n: break
            if (n+u)%a==0 and (n+u)//a>=2: return (t,u)
    return None
for D in (3,5,15,17):
    bad=[m for m in range(1,200,2) if gcd(m,D)==1 and anyword(D*m*m, 4, 4*D)]
    print(D, "n=D m^2, m<200 odd: words at levels 4D|t:", len(bad))
