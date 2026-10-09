"""EVIDENCE for Prop 2.3 / Remark 2.4 (EXCEPTIONAL_MN3.md): the average of tau(k a b^2 + 1)
over a<=A, b<=B scales like phi(k)/k (coprimality gain), not like 1.
Prints S/(A B log(AB)) and its ratio to phi(k)/k for several k."""
import math, sys
from sympy import factorint, totient

def tau(n):
    r = 1
    for e in factorint(n).values():
        r *= e + 1
    return r

A = B = int(sys.argv[1]) if len(sys.argv) > 1 else 120
ks = [4, 4*3, 4*3*5, 4*3*5*7, 4*3*5*7*11, 4*3*5*7*11*13, 4*1009, 4*1009*1013]
print(f"A=B={A}")
print("k, S/(AB log(kAB^2)), phi(k)/k, ratio  [ratio should be ~constant if the phi(k)/k gain is real]")
for k in ks:
    S = sum(tau(k*a*b*b + 1) for a in range(1, A+1) for b in range(1, B+1))
    norm = S / (A*B*math.log(k*A*B*B))
    f = int(totient(k)) / k
    print(f"{k:>12d}  {norm:.4f}  {f:.4f}  {norm/f:.4f}")
