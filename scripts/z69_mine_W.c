// z69 MINE: full U7 witness count W(n) for all odd n <= N, n = 1 mod 8.
// W(n) := #{ f = 7 mod 8, f <= 2n+1 : r := (-n mod f) in [1,f-1] divides f+1 }.
// Exhaustive: a witness f > 2n+1 is impossible (r = f - n | f+1 => r | n+1 => f <= 2n+1).
// Enumeration: for f = 7 mod 8, for each divisor r | f+1 with r < f, n = f*t - r, t >= 1,
//   n = 1 mod 8  <=>  t = -1 - r mod 8. Each (f, n) pair counted once since r = -n mod f is unique.
// Output: (a) "P p W fmin" for primes p = 1 mod 8 <= min(N, FULLMAX); (b) stats; (c) controls (odd squares, Z7).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 N = argc>1 ? strtoull(argv[1],0,10) : 10000000ULL;
  u64 FULLMAX = argc>2 ? strtoull(argv[2],0,10) : N;
  u64 M = 2*N+2;
  uint32_t *spf = calloc(M+1,sizeof(uint32_t));
  if(!spf){fprintf(stderr,"oom\n");return 1;}
  for(u64 i=2;i<=M;i++) if(!spf[i]){ for(u64 j=i;j<=M;j+=i) if(!spf[j]) spf[j]=(uint32_t)i; }
  u64 K = N/8+1;                     // index n>>3 for n = 1 mod 8
  uint16_t *W = calloc(K,sizeof(uint16_t));
  uint32_t *fmin = calloc(K,sizeof(uint32_t));
  u64 divs[4096];
  for(u64 f=7; f<=2*N+1; f+=8){
    // divisors of f+1
    u64 m=f+1; int nd=1; divs[0]=1;
    while(m>1){ u64 q=spf[m]; int e=0; while(m%q==0){m/=q;e++;}
      int cur=nd; u64 pw=1; for(int k=1;k<=e;k++){ pw*=q; for(int i=0;i<cur;i++) divs[nd++]=divs[i]*pw; } }
    for(int i=0;i<nd;i++){ u64 r=divs[i]; if(r>=f) continue;
      u64 t0 = (u64)((8 - ((1+r)%8))%8); if(t0==0) t0=8;   // t = -1-r mod 8, t>=1
      for(u64 t=t0; ; t+=8){ u64 n=f*t-r; if(n>N) break;
        u64 k=n>>3; if(W[k]<65535) W[k]++; if(fmin[k]==0) fmin[k]=(uint32_t)f; else if(f<fmin[k]) fmin[k]=(uint32_t)f; }
    }
  }
  // primes: spf[n]==n
  for(u64 n=9;n<=FULLMAX && n<=N;n+=8) if(spf[n]==n) printf("P %llu %u %u\n",n,W[n>>3],fmin[n>>3]);
  // controls
  int bad=0; for(u64 m=1; m*m<=N; m+=2){ u64 n=m*m; if(W[n>>3]!=0) {bad++; printf("SQBAD %llu %u\n",n,W[n>>3]);} }
  printf("CTRL odd squares <= N with W>0: %d\n",bad);
  u64 z7[8]={105,1465,3865,4545,10305,12145,39361,67425};
  for(int i=0;i<8;i++) if(z7[i]<=N && z7[i]%8==1) printf("CTRL Z7 %llu W=%u\n",z7[i],W[z7[i]>>3]);
  // composite non-square zeros n = 1 mod 8
  u64 cz=0; for(u64 n=9;n<=N;n+=8){ if(W[n>>3]==0 && spf[n]!=n){ u64 s=(u64)sqrtl((long double)n); while(s*s>n)s--; while((s+1)*(s+1)<=n)s++; if(s*s!=n){ cz++; if(cz<=50) printf("CZERO %llu\n",n);} } }
  printf("CTRL nonsquare composite zeros (n=1 mod 8): %llu\n",cz);
  u64 pz=0; for(u64 n=9;n<=N;n+=8) if(spf[n]==n && W[n>>3]==0){pz++; printf("PZERO %llu\n",n);} 
  printf("CTRL prime zeros: %llu\n",pz);
  return 0;
}
