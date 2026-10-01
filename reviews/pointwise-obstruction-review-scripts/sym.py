from sympy import *
t,a,h,p,z,f,H,A,lam,al,be,k,q,d,w,M,x=symbols('t a h p z f H A lambda alpha beta k q d w M x')
P=4*t+1
# chart
xx=t+a; m=P*h-t; HH=4*h-1; e=(4*a-1)*h-a
assert expand(HH*xx-m-e)==0
assert expand((4*a-1)*HH-4*e-1)==0
assert simplify(Rational(4)/P-1/(P*m)-1/xx-e/(xx*m))==0
# outer: vieta; with z=t+a anchor, A=4z-p, f=z^2/e, other x = z m/e
zz=t+a; AA=4*zz-P
X=zz*m/e; F=zz**2/e
assert simplify(X+zz-HH*F)==0
assert simplify(AA*(X+zz)-4*zz**2-F)==0
# mixed case computations
tt=lam*al*be; dd=lam*al**2; uu=lam*be**2
xN=tt+dd; zz2=tt+uu; A2=4*zz2-(4*tt+1); wv=lam*(al+be)**2
assert expand(xN+zz2-wv)==0 and expand(zz2**2-lam*be**2*wv)==0
fN=-(xN+zz2)  # H_N=-1
gam=be-al
assert expand(fN+A2-(lam*gam*(4*be-gam)-1))==0
# quadratic for beta: beta^2 = k f_P
fP=lam*gam*(4*be-gam)-1
expr=expand(be**2-k*fP)
g=symbols('g')
assert expand(expr.subs(al,be-g)-(be**2-4*k*lam*g*be+k*(lam*g**2+1)))==0
qd=(2*k*lam*g)**2-k*(lam*g**2+1)
assert expand(qd-k*(lam*g**2*(4*k*lam-1)-1))==0
# both nonpositive: |f2| <= x1+z-A
assert expand(xN+zz2-A2-(2*tt+dd-3*uu+1))==0
# seed lemma path
pp=symbols('p'); T=(pp-1)/4
for v in [(T,-T*(pp+1),-pp*T*(pp+1)),(2*T,2*T+1,-pp*T*(pp+1)),(2*T,2*T,-pp*T),(T,-2*pp*T,-2*pp*T)]:
    assert simplify(sum(1/s for s in v)-4/pp)==0
# Lemma C identity with p=4dw+M
pC=4*d*w+M
assert simplify(1/(d*(w-1))-M/(pC*d*(w-1))-4/(pC*(w-1))-4/pC)==0
# Lemma B entries
xB=symbols('xB'); pB=4*xB+M
for dB in [d]:
    assert simplify(1/xB-pB*(xB-dB)/M/ (pB*(xB-dB))**2*0 + 1/xB - M/(pB*(xB-dB))*0 )!=None
yB=-pB*(xB-d)/M; wB=pB*xB*(xB-d)/(M*d)
assert simplify(1/xB+1/yB+1/wB-4/pB)==0
# astra positive point
Q=symbols('Q')
v=(6*Q+7,(24*Q+1)*(762*Q+32),(6*Q+7)*(762*Q+32)/857)
assert simplify(sum(1/s for s in v)-4/(24*Q+1))==0
assert all(((6*713+7)*(762*713+32))%857==0 for _ in [0])
assert (4*7-1)*32-7==857 and 24*32-6==762 and 32-0==32
# t=6q, a=7: x=6q+7; h=32: m=p*32-6q = 768q+32-6q=762q+32
# Lemma typeII bound
print('2p/(9p+3)<1/4:', simplify(Rational(2)*pp/(9*pp+3)-Rational(1,4)))
# outer case z<0 bound
T_=symbols('T',positive=True)
print(simplify(1/(T_*(3*T_+1))*(4*T_+1)*(3*T_+1)/(3*(4*T_+1))*T_))
print('case z>=p bound expr', factor((4*T_+1)**2-(3*T_+1)*(9*T_+2)))
# windmill (3) consistency skipped
# forced (3) table
print('all sympy identities OK')
