# R31 from-scratch check of Lemma 1.1: M_{c,k}(p) via divisors of N vs dual j-count
from sympy import divisors, primerange
bad=0; tot=0
for p in primerange(3, 400):
    for c in range(1, 25):
        for k in range(1, 12):
            if (c*k) % p == 0: continue
            h=4*c*k; N=p*p+4*c*k*k
            M1=sum(1 for D in divisors(N) if (D+p) % h == 0)
            # dual: j>=1, hj>p, (hj-p) | 4cj^2+1 ; j bounded since hj-p<=N
            M2=0; j=1
            while h*j-p <= N:
                if h*j>p and (4*c*j*j+1) % (h*j-p) == 0: M2+=1
                j+=1
            # also verify no solutions beyond bound for a further stretch
            for jj in range(j, j+200):
                if (4*c*jj*jj+1) % (h*jj-p) == 0: bad+=1; print("BEYOND",p,c,k,jj)
            tot+=1
            if M1!=M2: bad+=1; print("MISMATCH",p,c,k,M1,M2)
print("checked",tot,"mismatches",bad)
