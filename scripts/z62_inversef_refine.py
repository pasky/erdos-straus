# Refine: for base modulus M0 and target classes T (non-square uncovered mod M0), compute uncovered sub-classes mod M0*k.
import sys
from z62_inversef_cover import classes, uncovered, is_square_class
M0=int(sys.argv[1]); k=int(sys.argv[2]); T=[int(x) for x in sys.argv[3].split(',')]
M=M0*k
un=uncovered(M)
for a in T:
    sub=[b for b in un if b%M0==a]
    print(f"class {a} mod {M0}: {len(sub)} of {k if k%2 else k//2} sub-classes mod {M} uncovered; non-square among them: {sum(1 for b in sub if not is_square_class(b,M))}")
