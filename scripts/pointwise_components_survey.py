"""Component anatomy of the complete signed graph (p<=300000): seed size, sterile sizes.

PYTHONPATH=scripts uv run python scripts/pointwise_components_survey.py LO HI > out.jsonl
Finite evidence only."""
import sys, json
from multiprocessing import Pool
from sympy import primerange
from pointwise_incidence import incidence_solutions
from pointwise_refactor import components, seed
def job(p):
    V=incidence_solutions(p); s=seed(p)
    out={"p":p,"V":len(V),"sterile":[], "seedsize":None,"seedpos":None,"ncomp":0,"posfree":[]}
    for C in components(V):
        out["ncomp"]+=1
        pos=sum(v[0]>0 for v in C)
        if s in C: out["seedsize"]=len(C); out["seedpos"]=pos
        elif pos==0: out["sterile"].append(len(C))
        else: out["posfree"].append((len(C),pos))
    return out
lo,hi=int(sys.argv[1]),int(sys.argv[2])
ps=[p for p in primerange(lo,hi) if p%4==1]
with Pool(20) as pool:
    for r in pool.imap_unordered(job,ps,chunksize=8): print(json.dumps(r),flush=True)
