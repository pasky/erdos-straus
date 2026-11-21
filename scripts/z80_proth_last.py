"""Target hard residues with a sieve of eligible (possibly large composite) word/gap moduli."""
from z80_proth_cover import root,pa,gcd,lcm,ds,order
import json,sys
from bisect import bisect_left

def run(m,B,extra):
    fpath=root/f'cover-{m}.json';c=json.loads(fpath.read_text());k=4**m-1;H0=c['period'];H=lcm(H0,extra);left={j for a in c['left'] for j in range(a,H,H0)}
    if not left:return
    # f, prime by prime, subject to f | k*(2^H-1). Also keep only actually
    # eligible q-adic digits for K0, including nonunits of k.
    powers=[];fs=[1]
    for q in map(int,pa.primes(3,B)):
        z=q;g=gcd(k,z)
        if pow(2,H,z//g)!=1%(z//g):continue
        while z*q<=B*B and pow(2,H,z*q//gcd(k,z*q))==1%(z*q//gcd(k,z*q)):z*=q
        powers.append((q,z));L=len(fs);t=q
        while t<=min(z,B):
            fs.extend(y*t for y in fs[:L] if y<=B//t);t*=q
    fs=sorted(f for f in fs if f%4==3);print(m,H,'gaps, moduli, primes',len(left),len(fs),len(powers),flush=True)
    for j in sorted(left):
        if j not in left:continue
        def put(o,R,*Z):
            o//=o&-o;P=order(o//gcd(o,k));assert H%P==0;c['rows'].append([P,j%P,R,*Z]);left.difference_update(x for x in list(left) if (j-x)%P==0)
        K0={f:gcd((f+1)//4,2**40) for f in fs};done=False
        for q,z in powers:
            n=(1+k*pow(2,j,z))%z
            if n%q==0:put(q,'D',q);done=True;break
            # sieve f == -n mod q, f == 3 mod 4
            t=(-n)%q;t+=q*((3-t)*pow(q,-1,4)%4)
            for f in range(t,B+1,4*q):
                if f in K0:K0[f]*=gcd(n+f,z)
        if done:continue
        for f in fs:
            K=K0[f];M=4*K*f;o=M//(M&-M);comp=pow(2,H,o//gcd(k,o))==1%(o//gcd(k,o));n=(k*pow(2,j+H,M)+1)%M
            assert ((n+f)//4)%K==0
            u=(-n)%f
            if u>=2 and (f+1)%u==0 and (f+1)//u>=2:
                v8=((k*pow(2,j+H,8*f)+1+u)%(8*f))//f;t=(f+1)//u
                if (1+t)*t*u*v8%8==0 and any(v%4==0 for v in (u,t,v8,f,t*v8-1)):put(8*f,'W',f,u);break
            C={d*n**i*((n+f)//(4*K))**a%f:(d,i,a) for a in range(1+comp) for i in (0,1) for d in ds(K)}
            v=next((v for v in C if -v%f in C),None)
            if v is not None:
                A,E=C[v],C[-v%f];put(M if A[2] or E[2] else 4*lcm(f,K),'K',f,K,A,E);break
    c.update(period=H,left=sorted(left));print(m,'left',len(left),flush=True);fpath.write_text(json.dumps(c,separators=(',',':'))+'\n')
if __name__=='__main__':run(*map(int,sys.argv[1:]))
