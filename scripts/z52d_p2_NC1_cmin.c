// z52d pass2 NC1: C-form witness scan for primes p ≡ 1 (mod M0) up to X.
// witness(p,C): some divisor d of N=4Cp+1 with d ≡ -1 (mod 4C). WLOG d ≤ sqrt(N) (complementary divisor is also ≡ -1).
// Outputs: per-prime C_min (≤ CMAX, 0 = none) to stdout as "p Cmin" lines when OUT flag set; runs & tail stats.
// usage: z52d_p2_NC1_cmin X CMAX M0 MODE   (MODE: 'runs' = longest run of consecutive primes ≡ M0 mod 24 with no witness ≤ C0 ; 'list' = print p Cmin)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
static int witness(u64 p, u64 C){
  u64 N=4*C*p+1, m=4*C;
  for(u64 d=m-1; d*d<=N; d+=m) if(N%d==0) return 1;
  return 0;
}
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), CMAX=strtoull(argv[2],0,10), M0=strtoull(argv[3],0,10);
  const char*mode=argv[4];
  char*sv=calloc(X+1,1); sv[0]=sv[1]=1;
  for(u64 i=2;i*i<=X;i++) if(!sv[i]) for(u64 j=i*i;j<=X;j+=i) sv[j]=1;
  if(!strcmp(mode,"list")){
    for(u64 p=5;p<=X;p++){ if(sv[p]||p%M0!=1%M0) continue;
      u64 C=1; for(;C<=CMAX;C++) if(witness(p,C)) break;
      printf("%llu %llu\n",p, C<=CMAX? C:0ULL);
    }
    return 0;
  }
  if(!strcmp(mode,"runs")){
    // consecutive primes ≡ 1 mod 24 (in order); longest run with no witness for C ≤ c0 (c0 = CMAX), and with C ≤ 2,5,10 variants
    u64 cs[3]={2,5,10}; u64 best[3]={0}, bestend[3]={0}, cur[3]={0}, cnt=0, lastbad[3]={0};
    u64 bestp[3]={0}, bestlo[3]={0}, nbad[3]={0}; u64 runhist[3][64]; memset(runhist,0,sizeof runhist);
    u64 lo[3]={0};
    for(u64 p=25;p<=X;p++){ if(sv[p]||p%24!=1) continue; cnt++;
      for(int k=0;k<3;k++){
        int w=0; for(u64 C=1;C<=cs[k];C++) if(witness(p,C)){w=1;break;}
        if(w){ if(cur[k]<64) runhist[k][cur[k]]++; cur[k]=0; lo[k]=p; }
        else { nbad[k]++; cur[k]++; if(cur[k]>best[k]){best[k]=cur[k]; bestend[k]=p; bestlo[k]=lo[k]; if(k==0&&cur[k]>=3) printf("  C<=2 run length %llu first reached at p=%llu\n",cur[k],p);} }
      }
    }
    printf("primes≡1 mod 24 in (25,%llu]: %llu\n",X,cnt); for(int k=0;k<3;k++) printf("C<=%llu: fraction with no witness = %.5f ; maximal-run histogram(len:count) ",cs[k],(double)nbad[k]/cnt); for(int k=0;k<1;k++){ for(int l=1;l<12;l++) printf("%d:%llu ",l,runhist[k][l]); printf("\n"); }
    for(int k=0;k<3;k++) printf("C<=%llu: longest run with no witness = %llu primes (ending at p=%llu, starting after p=%llu)\n",cs[k],best[k],bestend[k],bestlo[k]);
    return 0;
  }
  return 1;
}
