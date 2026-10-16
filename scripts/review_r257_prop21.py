from fractions import Fraction as F
# Prop 2.1: n = 3Y^3+1, a=80, c=1, d=(21Y+64)/320, b=(Y^2-3Y+9)/7
ok=0
for s in range(36, 36*60, 36):
    Y=2**(s//3); n=3*2**s+1
    assert (21*Y+64)%320==0 and (Y*Y-3*Y+9)%7==0
    a,c,d,b=80,1,(21*Y+64)//320,(Y*Y-3*Y+9)//7
    x,y,z=a*b*d,a*c*d*n,b*c*d*n
    assert 4*x*y*z==n*(x*y+y*z+z*x) and min(x,y,z)>0; ok+=1
print('Prop 2.1 ok for',ok,'values')
# exact class where both integral: j=s/3 mod lcm
good=[j for j in range(6,6+24) if (21*2**j+64)%320==0 and (4**j-3*2**j+9)%7==0]
print('j in [6,30) integral:',good)
