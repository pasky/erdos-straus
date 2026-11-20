"""Targeted fixed rows at larger moduli, testing exponent cosets not individual n. Runs on a partial certificate."""
from z78_proth_period import root,order,pa,ds
from math import gcd
import json,sys

def seek(m,H,cap):
    F=root/f'period-{m}-{H}.json';data=json.loads(F.read_text());k=4**m-1;left=set(data['left']);rows=data['rows']
    for q in range(3,cap+1):
        odd=q//(q&-q);w=odd//gcd(odd,k)
        if pow(2,H,w)!=1%w:continue
        for j in sorted(left):
            n=(k*pow(2,j+H,8*q)+1)%(8*q);u=(-n)%q;t,rem=divmod(q+1,u or 1);row=None
            if n%q==0:row=['D',q]
            elif min(u,t)>=2 and rem==0 and (1+t)*t*u*((n+u)//q)%8==0:row=['W',q,u]
            elif q%4==3:
                for a in ds((q+1)//4):
                    b=-(n%q)*a%q
                    if b and (q+1)%(4*a*b)==0:row=['II',q,b,a];break
            if row:
                P=order(w);rows.append([P,j%P,*row]);left={i for i in left if (i-j)%P};print(m,row,'remaining',len(left),flush=True);break
        if not left:break
    data['left']=sorted(left);F.write_text(json.dumps(data,separators=(',',':'))+'\n')
if __name__=='__main__':seek(*map(int,sys.argv[1:]))
