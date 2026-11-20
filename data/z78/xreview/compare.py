import re,sys,glob
def parse(fn):
    out={}
    for line in open(fn):
        if not line.startswith('N='): continue
        kv=dict(re.findall(r'(\w+)=([^ \]]*)',line))
        key=(int(kv['N']),int(kv['s']),int(kv['c']),kv['orient'])
        out[key]=line
    return out
def ints(line,keys):
    return [int(re.search(r'\b'+k+r'=(-?\d+)',line).group(1)) for k in keys]
br={}
for f in sorted(sys.argv[1:]): br.update(parse(f))
f3={}
for f in ['../f3_1.txt','../f3_2.txt','../f3_high_1.txt','../f3_high_2.txt']: f3.update(parse(f))
hy={}
for f in ['../hybrid_1.txt','../hybrid_2.txt']: hy.update(parse(f))
mis=0;n=0
for key,line in sorted(br.items()):
    if key[0]<4: continue
    b=ints(line,['monicV','vb1','vb2','ig1','ig2','near','hits'])
    if key in f3:
        l=f3[key]
        mv=ints(l,['monicV'])[0]
        seg1=l.split('case1[')[1]; seg2=l.split('case2[')[1]
        v1,i1,h1=ints(seg1,['vbound','integralG','hits']); v2,i2,h2=ints(seg2,['vbound','integralG','hits'])
        F=[mv,v1,v2,i1,i2,h1+h2]
        B=[b[0],b[1],b[2],b[3],b[4],b[6]]
        n+=1
        if F!=B: mis+=1; print('F3 MISMATCH',key,F,B)
    if key in hy:
        hn,hh=ints(hy[key],['near','hits'])
        if [hn,hh]!=[b[5],b[6]]: mis+=1; print('HYB MISMATCH',key,[hn,hh],[b[5],b[6]])
print('rows compared',n,'mismatches',mis, 'Nmax', max(k[0] for k in br))
