from sympy import divisors, isprime
def works(p,c):
    if (p+c)%4: return None
    A=(p+c)//4
    for a in divisors(A):
        for b in divisors(A//a):
            if (a+b)%c==0: return ("II",a,b)
    for a in divisors(A):
        for w in divisors(A//a):
            if (4*a*a*w+1)%c==0: return ("I",a,w)
    return None
cands = {
 "f":lambda Y,f,g,k:f, "g":lambda Y,f,g,k:g, "Y+g":lambda Y,f,g,k:Y+g, "Y+f":lambda Y,f,g,k:Y+f,
 "f+g":lambda Y,f,g,k:f+g, "fg":lambda Y,f,g,k:f*g, "Y/4":lambda Y,f,g,k:Y//4, "Y":lambda Y,f,g,k:Y,
 "g(Y+1)":lambda Y,f,g,k:g*(Y+1), "k":lambda Y,f,g,k:k, "kg":lambda Y,f,g,k:k*g, "4Y'g+?":lambda Y,f,g,k:Y*g-1,
 "Yg+g":lambda Y,f,g,k:Y*g+g, "Y+g+... (p+Y+g)/Y=kg":lambda Y,f,g,k:k*g,
 "(g+1)/4":lambda Y,f,g,k:(g+1)//4, "Yk-1=f":lambda Y,f,g,k:f, "Y'+g":lambda Y,f,g,k:Y//4+g,
 "Y'g":lambda Y,f,g,k:(Y//4)*g, "Y'f":lambda Y,f,g,k:(Y//4)*f, "Y'(g+1)-1":lambda Y,f,g,k:(Y//4)*(g+1)-1,
 "g+4":lambda Y,f,g,k:g+4,"f+4":lambda Y,f,g,k:f+4,"Y'+1":lambda Y,f,g,k:Y//4+1, "2Y'+g":lambda Y,f,g,k:Y//2+g,
 "3g+2Y":lambda Y,f,g,k:3*g+2*Y,
}
good={n:True for n in cands}
fails={n:0 for n in cands}
tot=0
for p in range(5,1500,4):
    if not isprime(p): continue
    for Y in range(4,p,4):
        n=p+Y
        for f in range(Y-1,n+1,Y):
            if n%f==0:
                g=n//f;k=(f+1)//Y; tot+=1
                for nm,F in cands.items():
                    c=F(Y,f,g,k)
                    if c<1 or not works(p,c):
                        fails[nm]+=1
print("hits",tot)
for nm in cands: print(nm, "fails", fails[nm])
