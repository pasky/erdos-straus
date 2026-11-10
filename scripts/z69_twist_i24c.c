// z69 TWIST round 2, I24 exploratory follow-up (NOT pre-registered): lag profile of neighbouring fibres.
// (★) solutions (a <= b, d) of primes p == 1 (4), p <= N, in the regime 4d^2 >= p.  For lag k = -8..8, k != 0:
// is the fibre d+k non-empty (some t' with s' = 4(d+k)t' - p in [2, t'+1] and s'^2 - 4t' a square)?
// Prints the hit rate per lag (all fibres d+k also satisfy 4(d+k)^2 >= p/2 here, so at most 2 candidates t').
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int issq(long v){ if(v<0) return 0; long r=(long)sqrtl((long double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r*r==v; }
static int fibre(long p,long D){ if(D<1) return 0;
  for(long tp=(p+2+4*D-1)/(4*D); 4*D*tp-p<=tp+1; tp++){ long sp=4*D*tp-p; if(sp>=2&&issq(sp*sp-4*tp)) return 1; } return 0; }
int main(int argc,char**argv){
  long N=atol(argv[1]); char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  long n=0,hit[17]={0};
  for(long a=1;4*a*a-2*a<=N;a++) for(long b=a;4*a*b-a-b<=N;b++) for(long d=1;;d++){
    long p=4*a*b*d-a-b; if(p>N) break; if(p<5||comp[p]||(p&3)!=1||4*d*d<p||d<=8) continue;
    n++; for(int k=-8;k<=8;k++) if(k) hit[k+8]+=fibre(p,d+k);
  }
  printf("N=%ld: solutions with 4d^2 >= p: %ld\nlag: rate (hits)\n",N,n);
  for(int k=-8;k<=8;k++) if(k) printf("%+d: %.6f (%ld)\n",k,(double)hit[k+8]/n,hit[k+8]);
  return 0;
}
