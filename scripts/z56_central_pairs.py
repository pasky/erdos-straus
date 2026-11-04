# z56 CENTRAL: unconditional slice range theta(k,l) = (1-3k)/(4(l-k)) over exponent pairs obtained by
# A/B words (all words of length <= 9 are EVALUATED) from the seeds: (0,1); Bourgain (13/84,55/84) [arXiv 1408.5794 Thm 6];
# the four pairs of Trudgian-Yang arXiv 2306.05599 Lemma 1.1 (1.6). Epsilons dropped (all pairs are "+eps").
# Finite search only: no claim that the maximum is the best known exponent pair for this objective.
from fractions import Fraction as F
def A(p): k,l=p; return (k/(2*k+2),(k+l+1)/(2*k+2))
def B(p): k,l=p; return (l-F(1,2),k+F(1,2))
def theta(p):
    k,l=p
    return (1-3*k)/(4*(l-k)) if l>k else None
seeds=[((F(0),F(1)),"(0,1)"),((F(13,84),F(55,84)),"Bourgain"),
       ((F(4742,38463),F(35731,51284)),"TY1"),((F(18,199),F(593,796)),"TY2"),
       ((F(2779,38033),F(58699,76066)),"TY3"),((F(715,10238),F(7955,10238)),"TY4")]
best={}
frontier=seeds
for depth in range(10):            # depth d = words of length d; evaluates lengths 0..9
    new=[]
    for p,w in frontier:
        t=theta(p)
        if t is not None and (p not in best or len(best[p][1])>len(w)): best[p]=(t,w)
        if depth<9:
            new.append((A(p),"A"+w)); new.append((B(p),"B"+w))
    # dedupe frontier
    seen={}; 
    for p,w in new:
        if p not in seen: seen[p]=w
    frontier=list(seen.items())
L=sorted(((t,w,p) for p,(t,w) in best.items()),reverse=True)
for t,w,p in L[:10]: print(f"{float(t):.6f} = {t}   {w:22s} ({p[0]}, {p[1]})  -> delta > 1/2-theta = {F(1,2)-t} = {float(F(1,2)-t):.6f}")
print("EPC limit (0,1/2): theta = 1/2")
