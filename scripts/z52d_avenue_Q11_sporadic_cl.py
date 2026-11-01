"""z52d avenue Q11 (Z2655): are the U(n) sporadics idoneal (Cl(−4n) of exponent ≤ 2)? h(−4n) by reduced forms, |Cl[2]| by
ambiguous reduced forms (b = 0, a = b or a = c). Run: timeout 60 python3 scripts/z52d_avenue_Q11_sporadic_cl.py"""
# class group of discriminant D<0 via reduced forms; compute h and exponent (by composing? use counting of ambiguous forms for 2-rank)
import math
def reduced_forms(D):
    fs=[]; a=1
    while 3*a*a<=-D:
        for b in range(-a+1,a+1):
            if (b*b-D)%(4*a)==0:
                c=(b*b-D)//(4*a)
                if c>=a and math.gcd(math.gcd(a,abs(b)),c)==1:
                    if b<0 and (a==c): continue
                    fs.append((a,b,c))
        a+=1
    return fs
for n in [105,2961,3985,25305,111969,978145]:
    for D in (-4*n,):
        f=reduced_forms(D); h=len(f)
        amb=sum(1 for (a,b,c) in f if b==0 or a==b or a==c)
        print(n,D,'h=',h,'#ambiguous (=2-torsion size)=',amb,'exponent<=2:',h==amb)
