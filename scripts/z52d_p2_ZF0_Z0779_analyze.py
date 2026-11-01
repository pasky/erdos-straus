"""Z0779: summarize segmented word-sieve histograms (primes p = 1 mod 4): per dyadic X=2^j, min / q01 / median of I3, R, Uv,
over [0,5e9) (complete) and the window [1e10, 1.05e10). Writes data/z52b/pass2/ZF0/Z0779/summary.json"""
import re, glob, json, collections
D='data/z52b/pass2/ZF0/Z0779/'
def load(files):
    H=collections.defaultdict(lambda: [collections.Counter() for _ in range(3)]); C=collections.Counter(); zeros=[]
    for f in files:
        for l in open(f):
            if l.startswith('ZERO'): zeros.append(l.split()[1]); continue
            m=re.match(r'W?X=2\^(\d+) cnt=(\d+)(.*)',l)
            if not m: continue
            j=int(m[1]); C[j]+=int(m[2]); parts=m[3].split(' | ')[1:]
            for k,p in enumerate(parts):
                for a,b in re.findall(r' (\d+):(\d+)',p): H[j][k][int(a)]+=int(b)
    return H,C,zeros
def q(c,f):
    n=sum(c.values()); t=0
    for v in sorted(c):
        t+=c[v]
        if t>=f*n: return v
out={}
for name,files in [('0_5e9',glob.glob(D+'seg_0_1e9_K*.txt')+glob.glob(D+'seg_1e9_5e9_K*.txt')),('1e10_window',glob.glob(D+'seg_1e10w_K*.txt'))]:
    H,C,zeros=load(files); rows={}
    for j in sorted(C):
        rows[j]=dict(cnt=C[j],**{nm:dict(min=min(H[j][k]),q01=q(H[j][k],.01),med=q(H[j][k],.5)) for k,nm in enumerate(['I3','R','Uv'])})
    out[name]=dict(per_dyadic=rows,zero_primes=sorted(set(zeros),key=int))
json.dump(out,open(D+'summary.json','w'),indent=1)
for name in out:
    print(name,'zeros:',out[name]['zero_primes'])
    for j,r in out[name]['per_dyadic'].items():
        if j>=20: print(' 2^%d n=%d'%(j,r['cnt']),' '.join('%s min=%d q01=%d med=%d'%(k,r[k]['min'],r[k]['q01'],r[k]['med']) for k in ['I3','R','Uv']))
