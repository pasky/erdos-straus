"""R159 from-scratch check of POINTWISE_BINARYFORM Lemma 1.1 (square vanishing for N-points).
Enumerate N-points of ET Sigma^I_n, Sigma^II_n via (a,b,c,d) and verify the Jacobi-symbol claims,
WITHOUT any coprimality restriction. Also check the character facts used in the proof."""
from sympy import jacobi_symbol as J
from math import isqrt
B = 40
def issq(n): r = isqrt(n); return r*r == n
nI = nII = badI = badII = sqI = sqII = 0
for a in range(1, B):
  for b in range(1, B):
    for c in range(1, B):
      if (a+b) % c: continue
      e = (a+b)//c
      for d in range(1, B):
        # Type I: n = c(4abd-1)/(a+b)
        num = c*(4*a*b*d-1)
        if num % (a+b) == 0:
          n = num//(a+b); f = 4*a*c*d - n
          if n > 0 and f > 0:
            assert 4*a*b*d == n*e+1 and e*f == 4*a*a*d+1 and b*f == n*a+c and n*n+4*c*c*d == f*(4*b*c*d-n)
            nI += 1
            if n % 2:
              if J(-d % n if n>1 else 0, n) != -1 and n > 1: badI += 1
              if issq(n): sqI += 1
        # Type II: n = (4abcd - a - b)/c
        num = 4*a*b*c*d - a - b
        if num % c == 0:
          n = num//c; f = 4*a*c*d - 1
          if n > 0:
            assert 4*a*b*d == n+e and e*f == n+4*a*a*d and b*f == n*c+a and 4*c*c*d*n+1 == f*(4*b*c*d-1)
            nII += 1
            if J(n % f, f) != -1: badII += 1
            if issq(n): sqII += 1
print(f"TypeI N-points {nI}: Jacobi(-d/n)!=-1 (odd n>1): {badI}; odd squares: {sqI}")
print(f"TypeII N-points {nII}: (n/f)!=-1: {badII}; squares n (any parity): {sqII}")
# n=1 Type I: (-d/1)=1 would contradict; check no Type I point with n=1
# character facts: psi(k)=(-d/k) periodic mod 4d with psi(4d-1)... psi(-1)=-1
bad = 0
for d in range(1, 200):
  for k in range(1, 8*d, 2):
    if J((-d) % k if k > 1 else 0, k) != J((-d) % (k+4*d), k+4*d) and k > 1: bad += 1
    if k < 4*d and k > 1 and J((-d) % k, k) != -J((-d) % (4*d-k), 4*d-k) and 4*d-k > 1: bad += 1
print("character periodicity/oddness violations:", bad)
