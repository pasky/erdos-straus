import sys; sys.path.insert(0,'scripts')
from review_r208_polygon import words, quid
import math
for r in (3,4):
    fails=[]
    for N in range(3,5001,2):
        if not any(any(x%4==0 for x in quid(b)[3]) for b in words(r,N)): fails.append(N)
    sq=[N for N in fails if math.isqrt(N)**2==N]
    print(r, len(fails), "squares", len(sq), "nonsq", [N for N in fails if N not in sq])
