"""Rational areas and phase checks for all three CRT charts of the central triangle."""
from fractions import Fraction as F
from math import gcd,lcm
from itertools import combinations


def polygon_area(*edges):
    # Convex polygon cut by a*x+b*s<=c; CCW ordering without any floating point.
    from functools import cmp_to_key
    vs=set()
    for (a,b,c),(d,e,f) in combinations(edges,2):
        den=a*e-b*d
        if den:
            x=F(c*e-b*f,den);s=F(a*f-c*d,den)
            if all(u*x+v*s<=w for u,v,w in edges):vs.add((x,s))
    if len(vs)<3:return F(0)
    cx=sum(x for x,s in vs)/len(vs);cs=sum(s for x,s in vs)/len(vs)
    def cmp(p,q):
        x,s=p[0]-cx,p[1]-cs;y,r=q[0]-cx,q[1]-cs
        side=lambda u,v:v<0 or (v==0 and u<0)
        if side(x,s)!=side(y,r): return 1 if side(x,s) else -1
        z=x*r-s*y;return -1 if z>0 else int(z<0)
    pts=sorted(vs,key=cmp_to_key(cmp));return abs(sum(x*pts[(i+1)%len(pts)][1]-s*pts[(i+1)%len(pts)][0] for i,(x,s) in enumerate(pts)))/2


def areas():
    # s = 1/2 - b_exponent; x-s = 1/2 - d_exponent for outer-small tiles.
    edges=[(0,-1,0),(-1,1,0)]; simple=(34,66,1); pair=(156,-78,1)
    A=polygon_area(*edges,simple); B=polygon_area(*edges,pair); overlap=polygon_area(*edges,simple,pair)
    middle_half=polygon_area((0,-1,0),(-1,2,0),(78,66,1))
    c=F(3,4)+4*(A+B-overlap)+4*middle_half
    print('outer areas, intersection, middle half:',A,B,overlap,middle_half)
    print('coverage',c,'central increment',c-F(3,4),'previous',F(3,4)+F(1,2120))
    eq=(F(1,3),F(2,3),F(1,3)); x,y,h=eq
    grouped=(17*x/20+39*y/20-3*h/20,x+15*y/8);assert max(grouped)==F(19,12)
    assert c>F(3,4)+F(1,2120) and c<1
    assert (1+x+y)/2==x+y==1
    return c

def inv(m,n):return pow(m,-1,n)


def phases():
    seen=[0,0,0]
    for a in range(1,13):
      for ap in range(1,15):
       if a==ap:continue
       for b in range(1,14):
        for bp in range(1,11):
         for t in (1,2,3,6):
          for mode in (0,1,2):
           if mode==0: # small d=a; second free coordinate b
            v,w=4*a,4*ap; q,r=v*b-1,w*bp-1; R,S=-b,-bp
           else: # small outer a; parity d fixed
            if gcd(a,b)*gcd(ap,bp)>1 or (a+b)%2==0 or (ap+bp)%2==0:continue
            j=mode-1;v,w=8*a,8*ap;q,r=v*b,w*bp;R,S=-a-b+4*j*a*b,-ap-bp+4*j*ap*bp
           g=gcd(q,r);m=q//g;n=r//g; ell=g*m*n
           if gcd(t,ell)>1 or (S-R)%g:continue
           if not mode:
            h=gcd(v,w);V,W=v//h,w//h;H=h*t;H1=1;H2=H
            while (u:=gcd(H2,W))>1:H1*=u; H2//=u
            delta=(W-V)//g;z=inv(r,H2)
            ph=-F(1,v*t*ell)+F(delta*inv(H1*W*m,H2*V*n),H2*V*n)+F(z*inv(H1*W*m,H2),H2)+F(inv(q*H2*V*n,H1),H1)
           else:
            D=lcm(v,w);D1=1;D2=D
            while (u:=gcd(D2,t*m))>1:D1*=u;D2//=u
            c1=1-4*j*a;c2=1-4*j*ap;A1=c1*(D//v);A2=c2*(D//w);delta=D*(a-ap)//g
            I=inv(D1*t*m,D2*n)
            ph=F(R,t*ell)-F(R*inv(q*n,t),t)+F((delta+A1*m-A2*n)*I,D2*n)
           J=(ph%1)*ell;assert J.denominator==1 and (t*J-R)%q==0 and (t*J-S)%r==0
           seen[mode]+=1
    print('CRT tests small d, pair even, pair odd',*seen)

if __name__=='__main__':
    areas();phases()
