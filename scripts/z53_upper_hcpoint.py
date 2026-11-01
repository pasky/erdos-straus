# HC(p) for given p (Lemma 1.1 lines), with the witnessing word; used for spot checks in Z53_UPPER.md
import sys
from sympy import divisors
def inC(x,p): return x%4==0 or (x+p)%8==0
def hc(p):
    c=3
    while True:
        if inC(c,p):
            for d in divisors(p+c):
                if d%c==c-1: t=(d+1)//c; v=(p+c)//d; assert t*c*v-c-v==p; return c,('u-line',(t,c,v))
            for d in divisors(c*p+1):
                if d%c==c-1:
                    u=(d+1)//c; v=((c*p+1)//d+1)//c; assert c*u*v-u-v==p; return c,('t-line',(c,u,v))
        c+=1
for a in sys.argv[1:]:
    p=int(a); print(p, *hc(p))
