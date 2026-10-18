/* R279 from-scratch: for every prime 5 <= p <= N compute
 *   R(p)   = #{(u,B): gcd=1, u+B odd, 4uB | p+u+B}            (sieve over all odd n <= N; also prints odd squares)
 *   M0(p)  = sum_{P(p)} 1/phi(4uB),  MBM(p) = sum_{P(p)} (1 - (-uB/p))/phi(4uB)
 * P(p) = {gcd(u,B)=1, u+B odd, 4uB-u-B <= p}. Bulk uB <= p/4 via a table over m = uB of
 * sum_{coprime splittings, u+B odd} 1/phi(4uB) (built by explicit enumeration of (u,B)); boundary
 * uB > p/4 enumerated directly. Legendre symbols from a per-p table of squares.
 * Output: p R M0 MBM  (and "SQ n R" lines for odd squares).  Usage: review_r279_mbm N [pmin]
 */
#include <stdio.h>
#include <stdlib.h>
static long gcdl(long a, long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
int main(int argc, char **argv){
  long N = atol(argv[1]); long pmin = argc>2 ? atol(argv[2]) : 5;
  long M4 = N/4 + 2, PH = 4*(N/3+2) + 8;
  int *phi = malloc(sizeof(int)*PH);
  for(long i=0;i<PH;i++) phi[i]=i;
  for(long i=2;i<PH;i++) if(phi[i]==i) for(long j=i;j<PH;j+=i) phi[j]-=phi[j]/i;
  double *w = calloc(M4, sizeof(double));      /* w[m] = sum over pairs uB=m of 1/phi(4m) */
  for(long u=1; u<M4; u++) for(long B=1; u*B<M4; B++)
    if(((u+B)&1) && gcdl(u,B)==1) w[u*B] += 1.0/phi[4*u*B];
  int *R = calloc(N+1, sizeof(int));
  for(long u=1; 3*u-1<=N; u++) for(long B=1; 4*u*B-u-B<=N; B++){
    if(!((u+B)&1) || gcdl(u,B)!=1) continue;
    long q=4*u*B; for(long n=q-u-B; n<=N; n+=q) R[n]++;
  }
  for(long r=3; r*r<=N; r+=2) printf("SQ %ld %d\n", r*r, R[r*r]);
  char *isc = calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!isc[i]) for(long j=i*i;j<=N;j+=i) isc[j]=1;
  signed char *leg = malloc(N+1);
  for(long p=pmin; p<=N; p++){
    if(isc[p] || p<5) continue;
    for(long k=0;k<p;k++) leg[k]=-1; leg[0]=0;
    for(long k=1;k<=(p-1)/2;k++) leg[(k*k)%p]=1;
    double m0=0, t=0;
    long mb = p/4;                              /* 4m <= p  <=> m <= p/4 */
    for(long m=2;m<=mb;m+=2){ if(w[m]==0) continue; m0+=w[m]; t+=w[m]*leg[p-m]; }
    /* boundary: uB > p/4, 4uB-u-B <= p */
    for(long u=1; 3*u-1<=p; u++){
      long B0 = p/(4*u)+1; long B1 = (p+u)/(4*u-1);
      for(long B=B0; B<=B1; B++){
        if(4*u*B-u-B>p || u*B<=mb) continue;
        if(!((u+B)&1) || gcdl(u,B)!=1) continue;
        double x = 1.0/phi[4*u*B]; m0+=x; t+=x*leg[p-(u*B)%p];
      }
    }
    printf("%ld %d %.10f %.10f\n", p, R[p], m0, m0-t);
  }
  return 0;
}
