# z52d Pass 2 NC0, item Z0949 — smallest y/N and z/N among the capped solutions (shift <= 200) at N = 119945383009.
N=119945383009
ys=[];zs=[]
for l in open('data/z52b/pass2/NC0/capped_119945383009_s200.txt'):
    if l.startswith('shift'):
        t=l.split(); ys.append(int(t[5])); zs.append(int(t[7]))
print('solutions',len(ys),'min y/N = %.4g'%(min(ys)/N),'min z/N = %.4g'%(min(zs)/N))
