# z56 CENTRAL: inputs "x y U tag" for z56_central_slices.c
# x = p + 2U, y = 2U, U = floor(p^(1/4)) (TDCAL Lemma S(a) convention) for primes/near-squares;
# odd squares: x = (2i+1)^2 itself with U = floor(x^(1/4)), y = 2U (control: x a square).
import sys
from sympy import nextprime, isprime, integer_nthroot
out=sys.argv[1]
spec={10:200,12:100,14:50,16:24}
def U4(n): return integer_nthroot(n,4)[0]
with open(out,'w') as f:
    for k,cnt in spec.items():
        base=10**k; gap=10**(k//2+1)  # windows far apart (gap >> y)
        # generic primes
        for i in range(cnt):
            p=nextprime(base+i*gap); U=U4(p); f.write(f"{p+2*U} {2*U} {U} gen{k}\n")
        # odd squares
        N0=integer_nthroot(base,2)[0]|1
        for i in range(cnt):
            N=N0+2*i*1001; x=N*N; U=U4(x); f.write(f"{x} {2*U} {U} sq{k}\n")
        # near squares below: p=N^2-c prime, c in (2U,4U]  -> (N,N) in E1
        N=N0+7; j=0
        while j<cnt:
            U=U4(N*N)
            for c in range(2*U+1,4*U+1):
                p=N*N-c
                if isprime(p):
                    U2=U4(p); f.write(f"{p+2*U2} {2*U2} {U2} nsq{k}\n"); j+=1; break
            N+=2002
    for p in [409,577,5569,9601,23929,83449,102001,329617,712321,8813281,193,2521,66529,3361,5101441]:
        U=U4(p); f.write(f"{p+2*U} {2*U} {U} test\n")
