"""Local determinant + short-shift P refinements. r, K, optional grid steps; one row per query."""
from z78_layer import layer
from z78_pack import packed
import sys
if __name__=='__main__':
    k,step,*rs=map(int,sys.argv[1:]);
    for r in rs:
        n=r**k;cut,counts=layer(n,step);print(r,k,cut,*(f'{packed(n,j)}:{counts[j]}' for j in range(cut,n.bit_length()//2+1)),flush=True)
