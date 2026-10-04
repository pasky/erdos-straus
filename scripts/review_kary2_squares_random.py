import random, sys
sys.path.insert(0,'.')
from review_kary2_squares import is_sq, g_of, factor
from math import isqrt
random.seed(1); bad=0; n=0
for _ in range(20000):
    a=random.randint(1,10**6); D=random.randint(1,10**9)
    G=4*a*g_of(D); n+=1; bad+=is_sq(-(4*D+a),G)
for _ in range(5000):
    r=1
    while True:
        r=random.randint(1,10**5); f=factor(r)
        if all(e==1 for e in f.values()): break
    h=random.randint(1,10**4); N=4*r*h*h+1; G=4*r*h
    divs=[1]
    for p,e in factor(N).items(): divs=[x*p**k for x in divs for k in range(e+1)]
    for m in divs:
        n+=1; bad+=is_sq(-pow(m,-1,G),G)
print("random large classes",n,"squares",bad)
