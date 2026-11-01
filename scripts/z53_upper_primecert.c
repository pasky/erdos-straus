// z53 UPPER: prime-level certificates (Lemma 2.3 / Theorem 4.3 of Z53_UPPER.md).
// For prime p = 1 (mod 8), p <= X:
//   Q4(p)  = least prime q such that e := (-p mod q) satisfies e | q+1 and 4 | e   (or e=1 with 4 | q+1, i.e. e -> q+1)
//            -> word ((q+1)/e, e, (p+e)/q) with coordinate e in 4N, so HC(p) <= e <= q+1.
//   QC(p)  = least prime q such that e | q+1 and (e in C_p or (q+1)/e in C_p) (either small coordinate certifies).
// Prints records and a coarse histogram of Q4, QC.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
static int inC(u64 x,u64 p){ return (x&3)==0 || ((x+p)&7)==0; }
int main(int argc,char**argv){
  u64 X=atoll(argv[1]); u64 QM=atoll(argv[2]);
  char*sv=calloc(X+1,1); for(u64 i=2;i*i<=X;i++) if(!sv[i]) for(u64 j=i*i;j<=X;j+=i) sv[j]=1;
  // primes up to QM
  char*s2=calloc(QM+1,1); for(u64 i=2;i*i<=QM;i++) if(!s2[i]) for(u64 j=i*i;j<=QM;j+=i) s2[j]=1;
  u64*pr=malloc(sizeof(u64)*(QM/2+10)); long npr=0; for(u64 i=3;i<=QM;i++) if(!s2[i]) pr[npr++]=i;
  long n=0, fail4=0, failC=0; u64 rec4=0,rec4p=0,recC=0,recCp=0; long h4[64]={0},hC[64]={0};
  double maxr4=0, maxrC=0; u64 maxr4p=0,maxrCp=0;
  for(u64 p=17;p<=X;p+=8){ if(sv[p]) continue; n++;
    u64 q4=0,qC=0;
    for(long i=0;i<npr && (!q4||!qC);i++){ u64 q=pr[i]; if(q>=p) break; u64 r=(q-p%q)%q; if(r==0) continue;
      u64 es[2]; int ne=0; if(r==1){ es[ne++]=1; es[ne++]=q+1; } else if((q+1)%r==0) es[ne++]=r;
      for(int j=0;j<ne;j++){ u64 e=es[j], f=(q+1)/e;
        if(!q4 && (e%4==0)) q4=q;
        if(!qC && (inC(e,p)||inC(f,p))) qC=q; } }
    if(!q4) fail4++; else { int b=0; while((1ULL<<(b+1))<=q4) b++; h4[b]++; if(q4>rec4){rec4=q4;rec4p=p;}
      double lp=log((double)p), rr=log((double)q4)/log(lp); if(rr>maxr4){maxr4=rr;maxr4p=p;} }
    if(!qC){ failC++; fprintf(stderr,"no prime-level C-certificate with q<p: p=%llu\n",p); } else { int b=0; while((1ULL<<(b+1))<=qC) b++; hC[b]++; if(qC>recC){recC=qC;recCp=p;}
      double lp=log((double)p), rr=log((double)qC)/log(lp); if(rr>maxrC){maxrC=rr;maxrCp=p;} }
  }
  printf("X=%llu QM=%llu primes p=1(8): %ld; no prime q<p: Q4 %ld, QC %ld\n",X,QM,n,fail4,failC);
  printf("max Q4=%llu at p=%llu; max log Q4/loglog p = %.3f at p=%llu\n",rec4,rec4p,maxr4,maxr4p);
  printf("max QC=%llu at p=%llu; max log QC/loglog p = %.3f at p=%llu\n",recC,recCp,maxrC,maxrCp);
  printf("Q4 dyadic hist (b: 2^b<=Q4<2^(b+1)):"); for(int b=0;b<64;b++) if(h4[b]) printf(" %d:%ld",b,h4[b]); printf("\n");
  printf("QC dyadic hist:"); for(int b=0;b<64;b++) if(hC[b]) printf(" %d:%ld",b,hC[b]); printf("\n");
  return 0; }
