/* z52d_p2_TO5_pmb.c — R*(p), M0(p), M_BM(p) for primes read from stdin (one per line), same definitions as
   scripts/z38_mbm.c (pairs (u,B): gcd=1, u+B odd, 4uB-u-B<=p; R=#{4uB | p+u+B}; M0=sum_{gcd(p,4uB)=1} 1/phi(4uB);
   T=sum kron(-uB,p)/phi(4uB); M_BM=M0-T).  phi(4uB)=4phi(u)phi(B).  Uses Jacobi via Legendre-free algorithm.
   Output: p R M0 MBM.   usage: ./z52d_p2_TO5_pmb < primes.txt */
#include <stdio.h>
#include <stdlib.h>
static long gcdl(long a,long b){ while(b){ long t=a%b; a=b; b=t; } return a; }
static int jacobi(long a,long n){ /* n odd positive */
  a%=n; if(a<0) a+=n; int t=1;
  while(a){ while(!(a&1)){ a>>=1; long r=n&7; if(r==3||r==5) t=-t; }
    long x=a; a=n; n=x; if((a&3)==3&&(n&3)==3) t=-t; a%=n; }
  return n==1?t:0; }
int main(){
  long p;
  while(scanf("%ld",&p)==1){
    long R=0; double M0=0,T=0;
    /* phi table for u,B up to p (phi(u) via trial division is slow; use sieve up to p/3+2 once per call is costly: compute phi on the fly) */
    for(long u=1; 3*u-2<=p; u++){
      for(long B=1; B*(4*u-1)<=p+u; B++){
        if(((u+B)&1)==0) continue;
        if(gcdl(u,B)!=1) continue;
        long q=4*u*B;
        if((p+u+B)%q==0) R++;
        if(p%q==0) continue;
        /* phi(q)=4*phi(u)*phi(B) */
        long pu=u, pb=B; double fu=1, fb=1; long m;
        m=u; for(long d=2; d*d<=m; d++) if(m%d==0){ while(m%d==0) m/=d; fu*=(double)(d-1)/d; } if(m>1) fu*=(double)(m-1)/m;
        m=B; for(long d=2; d*d<=m; d++) if(m%d==0){ while(m%d==0) m/=d; fb*=(double)(d-1)/d; } if(m>1) fb*=(double)(m-1)/m;
        double phi=4.0*pu*fu*pb*fb;
        M0+=1.0/phi;
        int k=jacobi(-u*B, p); T+=k/phi;
      }
    }
    printf("%ld %ld %.6f %.6f\n",p,R,M0,M0-T);
  }
  return 0;
}
