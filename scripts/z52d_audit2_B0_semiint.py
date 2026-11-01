# Z2112: strict semi-integral (Darmon weight 2 on D_1={w=x=0}) points on the ES pair (X_n, D_w),
# X_n: 4xyz = n w (xy+yz+zx) in P^3, boundary w=0 = triangle of lines x=0,y=0,z=0 (same combinatorics as Markoff).
# A primitive point (w:x:y:z) with w=q^2 is a solution of 4/(n q^2) = 1/x+1/y+1/z with gcd(q, yz)=1
# (then v_q(x)=2 automatically for q coprime to 2n).  Search: smallest odd q>1 coprime to n admitting one, positive x<=y<=z
# up to any permutation (we require q-part concentrated in exactly one coordinate).
import sys, math
def sols(N):
    # all positive solutions of 4/N = 1/x+1/y+1/z, x<=y<=z
    out=[]
    for x in range(N//4+1, 3*N//4+1):
        num=4*x-N; den=N*x  # 1/y+1/z = num/den
        if num<=0: continue
        g=math.gcd(num,den); num//=g; den//=g
        ylo=den//num+1; yhi=2*den//num
        for y in range(max(x,ylo), yhi+1):
            n2=num*y-den; 
            if n2<=0: continue
            d2=den*y
            if d2%n2==0:
                z=d2//n2
                if z>=y: out.append((x,y,z))
    return out
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
n_list=[int(a) for a in sys.argv[1:]]
for n in n_list:
    base=sols(n)
    res=[]
    for q in range(3,40,2):
        if math.gcd(q,n)!=1: continue
        N=n*q*q
        good=[s for s in sols(N) if sum(1 for c in s if c%q==0)==1 and math.gcd(q, math.prod(c for c in s if c%q)) ==1]
        prim=[s for s in good if math.gcd(math.gcd(s[0],s[1]),s[2])%q!=0]
        res.append((q,len(good)))
        if len(res)>=4: break
    print(n, 'ES sols', len(base), 'strict Darmon(2) counts by q:', res, flush=True)
# n=1 check: Campana (w powerful) vs Darmon (w square): strict points of the n=1 pair = solutions of 4/w with w-part only in x
def strict1(w):
    return [s for s in sols(w) if any(c%w==0 and all(math.gcd(w,d)==1 for d in s if d is not c) for c in s)]
if not n_list:
    for w in [9,25,49,81,225,27,125,243,8*0+343,3**5,72*0+675,1125]:
        print('n=1 w=',w,'square' if int(w**.5)**2==w else 'non-square powerful', len(strict1(w)), strict1(w)[:3], flush=True)
