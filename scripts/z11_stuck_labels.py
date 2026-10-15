# z11_stuck_labels.py — label the stuck nodes printed by z11_tree.c (SHOWSTUCK=N) by integer square points.
# Usage: uv run python scripts/z11_stuck_labels.py stuck.txt 4,-2,2,3
import sys,collections
LAB=[int(x) for x in sys.argv[2].split(',')]
C=collections.Counter(); ex=[]
for line in open(sys.argv[1]):
    out=[]
    for tok in line.split()[1:]:
        pe,c=tok.split(':'); l,e=map(int,pe.split('^')); c=int(c); Q=l**e
        t=None
        for v in LAB:
            if (c-v)%Q==0: t=v;break
        out.append('%d:%s'%(l, '*' if t is None else t))
    gen=sum(1 for o in out if o.endswith('*'))
    C[gen]+=1
    if len(ex)<8: ex.append(' '.join(out))
print('stuck nodes by number of generic components:',sorted(C.items()))
print('\n'.join(ex))
