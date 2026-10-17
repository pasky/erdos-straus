import sys
sys.path.insert(0,'scripts')  # O257: single-prime non-residue points x_(l,r): x=1 in Z_2 and at all q != l, x=r at l
from z28_adelic_fast import run
from sympy import primerange, legendre_symbol
k=int(sys.argv[1]); B=int(sys.argv[2]); L0,L1=int(sys.argv[3]),int(sys.argv[4])
for l in primerange(L0,L1):
    un=[r for r in range(2,l) if legendre_symbol(r,l)==-1 and not run(k,{2:1,l:r},B)]
    print(f"k={k} l={l} B={B}: uncovered non-residues r (x=1 elsewhere) {un}",flush=True)
