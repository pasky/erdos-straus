// z69 TWIST: tail calibration for (W).  cnt[n] = number of certificate words of n (ordered; Remark C types (i)-(iii)),
// saturating at 255.  For non-square n == 1 (4), 5 <= n <= N prints, for k = 2, 4, 6, 8: how many n have cnt <= k and the
// largest such n (all / primes only), and the minimum of cnt over dyadic blocks.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); uint8_t *C=calloc(N+1,1);
  for(long x=1;x<=N+2;x++) for(long y=1;;y++){
    long f=x*y-1; if(f<=0) continue; long zmax=(N+x)/f; if(zmax<1) break;
    long zmin=(x+1+f-1)/f; if(zmin<1) zmin=1;
    for(long z=zmin;z<=zmax;z++){ long n=f*z-x; if(n<1||n>N||(n&3)!=1) continue;
      if((y&3)==0||(x&3)==0||(z&3)==0||((y&3)==3&&((x&3)==3||(z&3)==3))) if(C[n]<255) C[n]++; }
  }
  char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  for(int k=0;k<=8;k+=2){ long c=0,last=0,cp=0,lastp=0;
    for(long n=5;n<=N;n+=4){ long s=(long)(__builtin_sqrt((double)n)+0.5); if(s*s==n) continue;
      if(C[n]<=k){ c++; last=n; if(!comp[n]){ cp++; lastp=n; } } }
    printf("cnt <= %d: %ld non-squares (largest %ld); primes %ld (largest %ld)\n",k,c,last,cp,lastp); }
  for(long lo=1024;lo<N;lo*=4){ long hi=lo*4<N?lo*4:N; int mn=255,mnp=255; long am=0,amp=0;
    for(long n=lo+(5-lo%4+4)%4;n<=hi;n+=4){ if((n&3)!=1) continue; long s=(long)(__builtin_sqrt((double)n)+0.5); if(s*s==n) continue;
      if(C[n]<mn){ mn=C[n]; am=n; } if(!comp[n]&&C[n]<mnp){ mnp=C[n]; amp=n; } }
    printf("block (%ld, %ld]: min cnt %d at n=%ld ; over primes %d at p=%ld\n",lo,hi,mn,am,mnp,amp); }
  return 0;
}
