# z53 HCHYP: analyse per-line success statistics from z53_hchyp_lines.c output.
# usage: python scripts/z53_hchyp_analyze.py data/z53/hchyp/stat_1e12_X2048.txt [...]
import sys, math
def load(fn):
    rows=[]; n=None; hist={}
    for line in open(fn):
        if line.startswith('# ') and 'n_count=' in line:
            n=int(line.split('n_count=')[1].split()[0])
        elif line.startswith('# HC histogram'):
            for tok in line.split('):',1)[1].split():
                a,b=tok.split(':'); hist[int(a)]=int(b)
        elif not line.startswith('#') and line.strip():
            x,e,l,b,f=map(int,line.split()); rows.append((x,e,l,b,f))
    return n,rows,hist
for fn in sys.argv[1:]:
    n,rows,hist=load(fn)
    # HC = 0 in the .hc file means 'no success for x <= Xmax' (censored); decode as Xmax+1
    hcs=[(int(l.split()[1]) or 10**9) for l in open(fn+'.hc')]
    ps=[int(l.split()[0]) for l in open(fn+'.hc')]
    L=math.log(sum(ps)/len(ps)); L2=math.log(L)
    print(f"== {fn}: n={n}  log p~{L:.2f}  (log p)^log2={L**math.log(2):.1f}  (log p)^(2log2)={L**(2*math.log(2)):.1f}")
    srt=sorted(hcs); q=lambda a: srt[min(len(srt)-1,int(a*len(srt)))]
    print(f"  HC (10**9 = censored, no success <= Xmax): max={srt[-1]} (at p={ps[hcs.index(srt[-1])]})  q99={q(.99)} q999={q(.999)}  P(HC>4)={sum(h>4 for h in hcs)/n:.4f} P(HC>8)={sum(h>8 for h in hcs)/n:.5f} P(HC>16)={sum(h>16 for h in hcs)/n:.5f} P(HC>32)={sum(h>32 for h in hcs)/n:.6f}")
    print("  bin [a,2a): meanP_E meanP_L  | x*P_E/logp  x*P_L/logp | #lines")
    a=4
    while a<=2048:
        sel=[r for r in rows if a<=r[0]<2*a]
        if sel:
            pe=sum(r[1] for r in sel)/len(sel)/n; pl=sum(r[2] for r in sel)/len(sel)/n
            xe=sum(r[0]*r[1]/n for r in sel)/len(sel)/L; xl=sum(r[0]*r[2]/n for r in sel)/len(sel)/L
            print(f"  [{a:5d},{2*a:5d}): {pe:.4f} {pl:.4f} | {xe:.3f} {xl:.3f} | {len(sel)}")
        a*=2
    # independence test: F(X)/n vs prod_{x<=X}(1-P_E)(1-P_L) and vs prod(1-P_either)
    print("  X   F(X)/n   prod(1-P_either)   ratio")
    prod=1.0
    for (x,e,l,b,f) in rows:
        prod*= (1-b/n)
        if x in (4,7,8,12,15,16,20,24,28,32,40,48,64):
            print(f"  {x:3d} {f/n:.6f} {prod:.6f} {(f/n)/prod if prod>0 else float('nan'):.3f}")

def xstar(fn, target_mult=1.0):
    """X* = least X with S(X) = sum_{x<=X} (P_E(x)+P_L(x)) >= target_mult * log p (Poisson max-HC scale)."""
    n,rows,hist=load(fn)
    ps=[int(l.split()[0]) for l in open(fn+'.hc')]
    L=math.log(sum(ps)/len(ps)); S=0.0
    for (x,e,l,b,f) in rows:
        S+=(e+l)/n
        if S>=target_mult*L: return L,x,S
    return L,None,S
if __name__=="__main__" and len(sys.argv)>1 and sys.argv[1]=="--xstar":
    pass
