// z68 U7F: U7 witnesses for primes p = 1 (mod 8), p <= N, enumerated from the witness side.
// A witness is f = 7 (mod 8), r | f+1, 1 <= r < f, with p = f t - r (t >= 1), i.e. r = (-p mod f) divides f+1.
// For every p = 1 (8) prime we record:  minf_all, minf_prime (f prime), minf_om2 (omega(f) <= 2),
// minf_sqfree2 ... and report primes with NO prime witness (f <= 2p+1 is exhaustive: f > p => r = f-p | f+1 => r | p+1
// => f <= 2p+1).  Also records min x = min r over witnesses (least shift) and min t.
// usage: wit N  [prints summary + lists]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64; typedef uint32_t u32;
static inline int getbit(const uint8_t*b,u64 i){return (b[i>>3]>>(i&7))&1;}
static inline void setbit(uint8_t*b,u64 i){b[i>>3]|=1<<(i&7);}
int main(int argc,char**argv){
  u64 N=atoll(argv[1]); u64 F=2*N+1;
  // prime sieve up to F (odd bitmap: index n>>1)
  uint8_t*comp=calloc(F/16+2,1); // bit set = composite (odd n)
  for(u64 i=3;i*i<=F;i+=2) if(!getbit(comp,i>>1)) for(u64 j=i*i;j<=F;j+=2*i) setbit(comp,j>>1);
  #define ISPRIME(n) ((n)==2 || (((n)&1) && !getbit(comp,(n)>>1)))
  // omega for odd n <= F: uint8 array indexed n>>1
  uint8_t*om=calloc(F/2+2,1);
  for(u64 q=3;q<=F;q+=2) if(!getbit(comp,q>>1)) for(u64 j=q;j<=F;j+=2*q) om[j>>1]++;
  // SPF for m <= (F+1)/8 (f+1 = 8m)
  u64 M=(F+1)/8+1; u32*spf=calloc(M+1,4);
  for(u64 i=2;i<=M;i++) if(!spf[i]){ for(u64 j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i; }
  // per-p arrays, index (p-1)/8
  u64 P=N/8+2; u32*mf=calloc(P,4),*mfp=calloc(P,4),*mf2=calloc(P,4),*mr=calloc(P,4);
  u64 divs[4096];
  for(u64 f=7;f<=F;f+=8){
    u64 m=(f+1)/8; // divisors of 8m
    // factor m
    u64 pr[32]; int ex[32]; int k=0; u64 mm=m;
    while(mm>1){ u64 q=spf[mm]; int e=0; while(mm%q==0){mm/=q;e++;} pr[k]=q;ex[k]=e;k++; }
    // add factor 2^3
    int has2=-1; for(int i=0;i<k;i++) if(pr[i]==2) has2=i;
    if(has2>=0) ex[has2]+=3; else {pr[k]=2;ex[k]=3;k++;}
    int nd=1; divs[0]=1;
    for(int i=0;i<k;i++){ int cur=nd; u64 pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
    int fprime=ISPRIME(f); int fom=om[f>>1];
    for(int i=0;i<nd;i++){ u64 r=divs[i]; if(r>=f) continue;
      // p = f t - r = 1 (mod 8): t = -1 - r (mod 8)
      u64 t0=(8-((1+r)&7))&7; if(t0==0) t0=8;
      for(u64 t=t0; f*t<=N+r; t+=8){ u64 p=f*t-r; if(p>N) break; if(!ISPRIME(p)) continue;
        u64 idx=(p-1)/8;
        if(!mf[idx]) { mf[idx]=f; mr[idx]=r; }
        if(fprime && !mfp[idx]) mfp[idx]=f;
        if(fom<=2 && !mf2[idx]) mf2[idx]=f;
      }
    }
  }
  u64 cnt=0,zero=0,noprime=0,noom2=0; u64 hist[40]={0},histp[40]={0};
  double maxratio=0; u64 maxp=0;
  for(u64 p=17;p<=N;p+=8){ if(!ISPRIME(p)) continue; cnt++; u64 idx=(p-1)/8;
    if(!mf[idx]){ zero++; printf("ZERO %llu\n",p); continue; }
    int b=0; while((1ULL<<b)<=mf[idx]) b++; hist[b]++;
    if(!mfp[idx]){ noprime++; printf("NOPRIME p=%llu minf=%u r=%u om(minf)=%d minf_om2=%u\n",p,mf[idx],mr[idx],om[mf[idx]>>1],mf2[idx]); }
    else { int c=0; while((1ULL<<c)<=mfp[idx]) c++; histp[c]++; }
    if(!mf2[idx]){ noom2++; printf("NOOM2 p=%llu minf=%u om=%d\n",p,mf[idx],om[mf[idx]>>1]); }
    double rt=(double)mf[idx]/p; if(rt>maxratio){maxratio=rt;maxp=p;}
  }
  printf("N=%llu primes p=1(8): %llu zeros %llu noprime %llu noom2 %llu maxratio minf/p=%.4f at p=%llu\n",N,cnt,zero,noprime,noom2,maxratio,maxp);
  for(int b=0;b<40;b++) if(hist[b]||histp[b]) printf("minf<2^%d: all %llu  prime-witness %llu\n",b,hist[b],histp[b]);
  return 0;
}
