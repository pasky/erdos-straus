// z68 U7F §9: census of the "borrowed-cofactor" witness families F_c = { f = c*q : q prime } for c in {1,3,5,7,9,25}.
// For every prime p = 1 (8) <= N records which families provide a witness (bitmask), and prints primes lacking
// F_1, F_1∪F_3, F_1∪F_3∪F_5, and the union of all six.  Same exhaustive (f, r, t) enumeration as z68_u7f_wit.c.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef uint32_t u32;
static inline int getbit(const uint8_t*b,u64 i){return (b[i>>3]>>(i&7))&1;}
static inline void setbit(uint8_t*b,u64 i){b[i>>3]|=1<<(i&7);}
int main(int argc,char**argv){
  u64 N=atoll(argv[1]); u64 F=2*N+1;
  uint8_t*comp=calloc(F/16+2,1);
  for(u64 i=3;i*i<=F;i+=2) if(!getbit(comp,i>>1)) for(u64 j=i*i;j<=F;j+=2*i) setbit(comp,j>>1);
  #define ISPRIME(n) ((n)==2 || ((n)>=3 && ((n)&1) && !getbit(comp,(n)>>1)))
  u64 M=(F+1)/8+1; u32*spf=calloc(M+1,4);
  for(u64 i=2;i<=M;i++) if(!spf[i]){ for(u64 j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i; }
  u64 P=N/8+2; uint8_t*fl=calloc(P,1);
  const u64 cs[6]={1,3,5,7,9,25};
  u64 divs[4096];
  for(u64 f=7;f<=F;f+=8){
    int mask=0;
    for(int i=0;i<6;i++) if(f%cs[i]==0 && ISPRIME(f/cs[i])) mask|=1<<i;
    if(!mask) continue;
    u64 m=(f+1)/8; u64 pr[32]; int ex[32]; int k=0; u64 mm=m;
    while(mm>1){ u64 q=spf[mm]; int e=0; while(mm%q==0){mm/=q;e++;} pr[k]=q;ex[k]=e;k++; }
    int has2=-1; for(int i=0;i<k;i++) if(pr[i]==2) has2=i;
    if(has2>=0) ex[has2]+=3; else {pr[k]=2;ex[k]=3;k++;}
    int nd=1; divs[0]=1;
    for(int i=0;i<k;i++){ int cur=nd; u64 pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
    for(int i=0;i<nd;i++){ u64 r=divs[i]; if(r>=f) continue;
      u64 t0=(8-((1+r)&7))&7; if(t0==0) t0=8;
      for(u64 t=t0; f*t<=N+r; t+=8){ u64 p=f*t-r; if(p>N) break; if(!ISPRIME(p)) continue; fl[(p-1)/8]|=mask; }
    }
  }
  u64 cnt=0,n1=0,n13=0,n135=0,nall=0; u64 hist[64]={0};
  for(u64 p=17;p<=N;p+=8){ if(!ISPRIME(p)) continue; cnt++; int m=fl[(p-1)/8]; hist[m]++;
    if(!(m&1)) n1++;
    if(!(m&3)) n13++;
    if(!(m&7)){ n135++; printf("NO135 %llu mask=%d\n",p,m); }
    if(!m){ nall++; printf("NONE %llu\n",p); }
  }
  printf("N=%llu primes=%llu noF1=%llu noF1F3=%llu noF1F3F5=%llu none_of_six=%llu\n",N,cnt,n1,n13,n135,nall);
  // marginal: primes lacking F3 alone, F5 alone
  u64 no3=0,no5=0; for(int m=0;m<64;m++){ if(!(m&2)) no3+=hist[m]; if(!(m&4)) no5+=hist[m]; }
  printf("noF3=%llu noF5=%llu\n",no3,no5);
  return 0;
}
