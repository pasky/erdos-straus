import gzip,json,sys
sys.path.insert(0,__import__('os').path.dirname(__file__))
from sympy import primerange, divisors, isprime
c=json.load(gzip.open('data/formal_closure/certificate.json.gz'))
L={int(k) for k in c['q0_mod']}
print('primes<=17631 not in Lambda:', sum(1 for l in primerange(2,17632) if l not in L), ' <=7795:', sum(1 for l in primerange(2,7796) if l not in L))
def crit9(p):
    t=(p-1)//4
    for h in divisors(t*t):
        m=p*h-t; K=4*h-1
        for D in divisors(m*m):
            if (D+h)%K==0: return True
    return False
S=[]
for p in primerange(5,300000):
    if p%840 in (1,121,169,289,361,529) and not crit9(p): S.append(p)
print('fail (9) below 3e5:',S)
