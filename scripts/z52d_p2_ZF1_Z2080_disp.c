// z52d Pass-2 ZF1/S6 item Z2080: second-moment (dispersion) of R(p) stratified by the level C.
// For primes p ≡ 1 (4) in [P0, P0+H]: R_b(p) = #{(u,B,C): 4uBC-u-B=p, C in bucket b} via the trial form
// (4uC-1) | p+u (FRONTIER §2.1). Buckets: C = 1..32 individually (b = C-1), then dyadic [2^j, 2^{j+1}) for j >= 5 (the first one is [33,64) since C=32 has its own bucket).
// Also, per (C-bucket), the BV-type discrepancy over the whole range p <= P1 is NOT computed here (see notes).
// Output: header + one line per prime: p and R_b for all buckets.  Usage: prog P0 H
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NBK 64
static int bucket(long long C){ if(C<=32) return (int)C-1; int j=0; while((1LL<<(j+1))<=C) j++; return 32+(j-5); }
int main(int argc,char**argv){
  long long P0=atoll(argv[1]),H=atoll(argv[2]),P1=P0+H;
  char *isp=malloc(H+1); memset(isp,1,H+1);
  for(long long q=2;q*q<=P1;q++){ int pr=1; for(long long r=2;r*r<=q;r++) if(q%r==0){pr=0;break;} if(!pr) continue;
    long long s=((P0+q-1)/q)*q; if(s<q*q) s=q*q; for(long long j=s;j<=P1;j+=q) isp[j-P0]=0; }
  int *R=calloc((H+1)*NBK,sizeof(int)); int maxb=0;
  for(long long u=1;3*u-1<=P1;u++) for(long long C=1;;C++){ long long m=4*u*C-1; if(m>P1+u) break;
    long long r=(-u)%m; if(r<0) r+=m; long long st=P0+(((r-P0)%m)+m)%m; int b=bucket(C); if(b>maxb) maxb=b;
    for(long long p=st;p<=P1;p+=m){ long long i=p-P0; if(isp[i]&&(p&3)==1) R[i*NBK+b]++; } }
  printf("# P0 %lld H %lld nbuckets %d (b<32: C=b+1; b>=32: C in [2^(b-27),2^(b-26)), except b=32: C in [33,64))\n",P0,H,maxb+1);
  for(long long i=0;i<=H;i++){ long long p=P0+i; if(!isp[i]||(p&3)!=1) continue; printf("%lld",p); for(int b=0;b<=maxb;b++) printf(" %d",R[i*NBK+b]); printf("\n"); }
  return 0; }
