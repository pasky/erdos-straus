# full Lemma 3.1 mechanism over Z[w], w^2=w+1: e = 1/u+1/v integral, u,v totally positive; record class of e mod 4.
import math
s5=math.sqrt(5); w=(1+s5)/2; wc=(1-s5)/2
def mul(x,y):
    a,b=x; c,d=y   # (a+bw)(c+dw) = ac + (ad+bc)w + bd(w+1)
    return (a*c+b*d, a*d+b*c+b*d)
def conj(x): a,b=x; return (a+b, -b)   # w' = 1-w
def N(x): a,b=x; return a*a+a*b-b*b
def tp(x): a,b=x; return a+b*w>0 and a+b*wc>0
B=25
els=[(a,b) for a in range(-3*B,3*B) for b in range(-B,B) if tp((a,b))]
els=[x for x in els if abs(N(x))<=400]
print(len(els))
cls=set()
for u in els:
    for v in els:
        s=(u[0]+v[0],u[1]+v[1]); p=mul(u,v); n=N(p)
        # e = s/p = s*conj(p)/N(p)
        t=mul(s,conj(p))
        if t[0]%n or t[1]%n: continue
        e=(t[0]//n,t[1]//n)
        if N(e)%2: cls.add((e[0]%4,e[1]%4))
neg=sorted(((-a)%4,(-b)%4) for a,b in cls)
print('e classes',sorted(cls)); print('covered n classes (-e)',neg)
