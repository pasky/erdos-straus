"""Verify literals in the full modulus, independent of factorisation and old-modulus logs."""
import json,math
from pathlib import Path

data=json.loads(Path('data/z78/proth/tower-6.json').read_text());j=data['j'];d=data['d'];assert j==6 and d==3**(j-1);h=3*d;H=2**h-1;k=2*H+1;m=(h+1)//2;assert data['m']==m
B=lambda a:1+pow(2,a,H)
def ratio(a,b):
    assert math.gcd(a,h)==math.gcd(b,h) in (1,3);return B(a)*pow(B(b),-1,H)%H
# Build (1,3) = B_3/(B_(1+d)B_(1+2d)), since B_3=3^2.
y=ratio(1,1+d)*ratio(1,1+2*d)%H
A=pow(y,6,H)
for a,e in data['powers'].items():
    a=int(a);assert 0<a<d and math.gcd(a,3)==1 and e>=0
    p=ratio(3,3*a)
    for r in range(3):p=p*ratio(a+r*d,1+r*d)%H
    A=A*pow(p,e,H)%H
assert A==3**6%H
# Half orbit has length b=d; telescope and substitute A.
b=d;P=1
for i in range(b):P=P*ratio(pow(2,i,h),1)%H
assert pow(2,b,h)==h-1 and 2*P*pow(3,b,H)%H==H-1
# -1/(c*9) represented by ratios 2 * P * A^((b-3)/6) * B_1/B_m
c=2**m+1;assert k%c==0 and c%16==1
rhs=ratio(1,h-1)*P*pow(A,(b-3)//6,H)*ratio(1,m)%H;assert rhs*9*c%H==H-1
print(f'h={h}, m={m}: 3^6 and -1/(9c) verified by full-modulus gcd-1/3 ratios')
