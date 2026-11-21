"""Opus cross-review of R17_WALK (NOT a certificate): ablation/sensitivity harness around z80_budget2.py.
Filters the certificate files at read time, then calls the unmodified budget2 analyze().
Usage from repo root:  python scripts/z80_xr_walk_ablate.py OPTS r ...
OPTS (comma list):
  nop11            drop data/z80/crush2/p11.txt
  p11x=K           multiply every P11 window total by K (sensitivity)
  p11w=I           keep only windows with index < I (then the cumulative seed is not formed -> drop)
  p11j30           use window 0 only, seeded as the cumulative count for e<2^30 (J=30)
  nos33 / nos35    drop shift33.txt / shift35.txt
  s=R              keep only shift33/35 rows of prime R
  nomid            replace the z80_mid band refinement by the z79 short() prefix
  noxr             drop reviewer xr_prefix_lo / xr_cf_lo rows (z80_xr_extend)
  sx=K             multiply every shift33/35 entry by K
  dropk=K          drop shift33/35 rows with that K
Prints r, global margin ppm (max of union/monotone), union margin ppm, monotone margin ppm, dominant.
"""
import sys, pathlib
opts=dict((o.split('=')+[''])[:2] for o in sys.argv[1].split(',') if o) if len(sys.argv)>1 else {}
rs=list(map(int,sys.argv[2:])) or [73,79,83]
sys.argv=sys.argv[:1]
_orig=pathlib.Path.read_text
def patched(self,*a,**k):
    t=_orig(self,*a,**k);n=str(self)
    if n.endswith('crush2/p11.txt'):
        rows=[list(map(int,l.split())) for l in t.splitlines()]
        if 'nop11' in opts:return ''
        if 'p11x' in opts:rows=[[r,j,o,s,c*int(opts['p11x'])] for r,j,o,s,c in rows]
        if 'p11j30' in opts:rows=[[r,30,o,s,c] for r,j,o,s,c in rows if o==0]
        return '\n'.join(' '.join(map(str,x)) for x in rows)+('\n' if rows else '')
    if n.endswith('crush2/shift33.txt') or n.endswith('crush2/shift35.txt'):
        if ('nos33' in opts and n.endswith('33.txt')) or ('nos35' in opts and n.endswith('35.txt')):return ''
        rows=[list(map(int,l.split())) for l in t.splitlines()]
        if 's' in opts:rows=[x for x in rows if x[0]==int(opts['s'])]
        if 'dropk' in opts:rows=[x for x in rows if x[1]!=int(opts['dropk'])]
        if 'sx' in opts:rows=[x[:2]+[c*int(opts['sx']) for c in x[2:]] for x in rows]
        return '\n'.join(' '.join(map(str,x)) for x in rows)+('\n' if rows else '')
    if 'noxr' in opts and n.endswith(('xr_prefix_lo.txt','xr_cf_lo.txt','crush2/prefix9.txt','crush2/cf9.txt')):return ''
    return t
pathlib.Path.read_text=patched
import z80_budget2 as B
if 'nomid' in opts:
    B.old.sh=B.prev
from z79_pbudget import ppm
for r in rs:
    x,total,big,who,m,P,Qs,pt,qt=B.analyze(r)
    a,p,t,q,h,u=B.row(r);mono=a-sum(p)-q-h-u
    print(r,(m*1000000).__floor__(),((x-total)*1000000).__floor__(),(mono*1000000).__floor__(),who,ppm(big),
          ' '.join(f'{n}:{ppm(z)}' for z,n in P[:6]),flush=True)
