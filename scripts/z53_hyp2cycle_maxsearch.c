/* z53_hyp2cycle_maxsearch.c — exhaustive scan of ALL primes p in [A,B) (segmented sieve, OpenMP):
   balanced-block 2-cycle counts with U = floor(p^{1/4}) (or fixed U if argv[3] > 0).
   N2 = # unordered 2-cycles {u<B} of f (uB | p+u+B), N4 = # with 4 | k.
   Prints histograms of N2 and N4 and every prime with N2 >= T2 or N4 >= T4 (argv[4], argv[5]).
   usage: ./maxsearch A B Ufix T2 T4 [mode]   mode 0 = primes (default), 1 = all odd n, 2 = odd composites
   (OMP_NUM_THREADS controls threads) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <omp.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 iroot4(u64 n){ u64 r=(u64)floor(pow((double)n,0.25)); while((u128)(r+1)*(r+1)*(r+1)*(r+1)<=n) r++; while((u128)r*r*r*r>n) r--; return r; }
#define SEG (1<<20)
int main(int argc,char**argv){
  u64 A=strtoull(argv[1],0,10), Bx=strtoull(argv[2],0,10); long Ufix=atol(argv[3]); int T2=atoi(argv[4]), T4=atoi(argv[5]); int mode=argc>6?atoi(argv[6]):0;
  u64 sq=(u64)sqrt((double)Bx)+2; char *isc=calloc(sq+1,1); int np=0; unsigned *pr=malloc(sizeof(unsigned)*(sq/2+10));
  for(u64 i=2;i<=sq;i++){ if(!isc[i]){ pr[np++]=(unsigned)i; for(u64 j=i*i;j<=sq;j+=i) isc[j]=1; } }
  long H2[64]={0},H4[64]={0}; long nprimes=0;
  u64 nseg=(Bx-A+SEG-1)/SEG;
  #pragma omp parallel
  { long h2[64]={0},h4[64]={0}; long cnt=0; char *seg=malloc(SEG); long *fx=malloc(sizeof(long)*(2*70000));
    #pragma omp for schedule(dynamic,1)
    for(u64 s=0;s<nseg;s++){
      u64 lo=A+s*SEG, hi=lo+SEG; if(hi>Bx) hi=Bx; memset(seg,1,hi-lo);
      for(int i=0;i<np;i++){ u64 q=pr[i]; if(q*q>=hi) break; u64 st=((lo+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<hi;j+=q) seg[j-lo]=0; }
      for(u64 p=lo;p<hi;p++){ if(p<5) continue; if(mode==0 && !seg[p-lo]) continue; if(mode==2 && seg[p-lo]) continue; if(p<lo||p%2==0) continue;
        u64 U = Ufix>0?(u64)Ufix:iroot4(p); if(2*U>=p) continue;
        for(u64 x=U+1;x<=2*U;x++){ u64 r=(x-p%x)%x; u64 y=r; if(y<=U) y+=x*((U-y)/x+1); fx[x-U]=(y<=2*U&&y>U)?(long)y:0; }
        int n2=0,n4=0;
        for(u64 u=U+1;u<=2*U;u++){ long Bv=fx[u-U]; if(!Bv||(u64)Bv<=u) continue; if(fx[Bv-U]!=(long)u) continue;
          u64 num=p+u+(u64)Bv, q=u*(u64)Bv; if(num%q) continue; n2++; if((num/q)%4==0) n4++; }
        h2[n2<63?n2:63]++; h4[n4<63?n4:63]++; cnt++;
        if(n2>=T2||n4>=T4){
          #pragma omp critical
          { printf("HIT %llu U=%llu N2=%d N4=%d\n",p,U,n2,n4); fflush(stdout); }
        }
      }
    }
    #pragma omp critical
    { for(int i=0;i<64;i++){H2[i]+=h2[i];H4[i]+=h4[i];} nprimes+=cnt; }
  }
  printf("RANGE %llu %llu mode %d count %ld\nH2",A,Bx,mode,nprimes); for(int i=0;i<64;i++) if(H2[i]) printf(" %d:%ld",i,H2[i]);
  printf("\nH4"); for(int i=0;i<64;i++) if(H4[i]) printf(" %d:%ld",i,H4[i]); printf("\n"); return 0; }
