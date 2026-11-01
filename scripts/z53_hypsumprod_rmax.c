/* z53 HYPSUMPROD: R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n} for ALL n <= X,
   plus Q(n) = #{solutions with 64*min(u,B,C)^3 >= n}  (near-cube region, min >= n^{1/3}/4),
   and Qh(n) = #{solutions with 4096*min^4 >= n^... } replaced by min(u,B,C) >= n^{1/4}: 256*min^4 >= n.
   Output: record-breaking values of R, Q, Qh over (a) all n, (b) odd n, (c) primes n == 1 mod 4;
   and the max of R, Q over n in dyadic ranges. Usage: rmax X */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
int main(int argc,char**argv){
  uint64_t X=strtoull(argv[1],0,10);
  uint16_t *R=calloc(X+1,2),*Q=calloc(X+1,2),*Qh=calloc(X+1,2);
  uint8_t *comp=calloc(X+1,1);
  if(!R||!Q||!Qh||!comp){fprintf(stderr,"oom\n");return 1;}
  for(uint64_t i=2;i*i<=X;i++) if(!comp[i]) for(uint64_t j=i*i;j<=X;j+=i) comp[j]=1;
  for(uint64_t u=1;4*u-u-1<=X;u++)
    for(uint64_t B=1;4*u*B-u-B<=X;B++){
      uint64_t q=4*u*B;
      for(uint64_t C=1;;C++){
        uint64_t n=q*C-u-B; if(n>X)break;
        if(R[n]<65535)R[n]++;
        uint64_t m=u<B?u:B; if(C<m)m=C;
        if(64*m*m*m>=n) Q[n]++;
        if(256*m*m*m*m>=n) Qh[n]++;
      }
    }
  /* records */
  const char*nm[3]={"all","odd","prime1mod4"};
  for(int cls=0;cls<3;cls++){
    unsigned rR=0,rQ=0,rQh=0;
    for(uint64_t n=3;n<=X;n++){
      if(cls==1 && !(n&1))continue;
      if(cls==2 && (comp[n]||(n&3)!=1))continue;
      if(R[n]>rR){rR=R[n];printf("REC %s R n=%lu R=%u Q=%u Qh=%u\n",nm[cls],n,R[n],Q[n],Qh[n]);}
      if(Q[n]>rQ){rQ=Q[n];printf("REC %s Q n=%lu R=%u Q=%u Qh=%u\n",nm[cls],n,R[n],Q[n],Qh[n]);}
      if(Qh[n]>rQh){rQh=Qh[n];printf("REC %s Qh n=%lu R=%u Q=%u Qh=%u\n",nm[cls],n,R[n],Q[n],Qh[n]);}
    }
  }
  /* dyadic maxima */
  for(uint64_t lo=1024;lo<=X;lo*=2){
    uint64_t hi=2*lo-1; if(hi>X)hi=X;
    unsigned mR[3]={0},mQ[3]={0}; uint64_t aR[3]={0},aQ[3]={0};
    double sR[3]={0}; uint64_t cnt[3]={0};
    for(uint64_t n=lo;n<=hi;n++){
      for(int cls=0;cls<3;cls++){
        if(cls==1 && !(n&1))continue;
        if(cls==2 && (comp[n]||(n&3)!=1))continue;
        if(R[n]>mR[cls]){mR[cls]=R[n];aR[cls]=n;}
        if(Q[n]>mQ[cls]){mQ[cls]=Q[n];aQ[cls]=n;}
        sR[cls]+=R[n];cnt[cls]++;
      }
    }
    for(int cls=0;cls<3;cls++) printf("DY %s lo=%lu maxR=%u at %lu maxQ=%u at %lu meanR=%.3f\n",nm[cls],lo,mR[cls],aR[cls],mQ[cls],aQ[cls],sR[cls]/(cnt[cls]?cnt[cls]:1));
  }
  return 0;
}
