"""Cross-review: print z78_layer buckets and z78_pack.packed at n=2^b for comparison
with exact counts from z78_xr_layercheck.c (bound must be >= exact)."""
import sys
from z78_layer import layer
from z78_pack import packed
b=int(sys.argv[1]);n=1<<b
cut,bk=layer(n,2)
for j in range(cut,b//2+1):print('j',j,'layer_large',bk[j],'packed_small',packed(n,j))
for j in range(1,cut):print('j',j,'packed_small',packed(n,j))
