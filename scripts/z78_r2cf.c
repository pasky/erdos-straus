/* Exact large-shift P union scan. Sparse outputs at depth 4; no universe bitmap.
   Modes: scan r K floorE t0 t1 [digit-list-file]; only t in the record chunk.
   All f=4t-1 with t in [t0,t1] and t <= (floor(N/E)+1)/2, e>=E.
   Optional input contains L1 digit residues that are already covered.
   Caller canonical sort/dedupe and remove any already covered parents. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;static U R,mod;static Z N;static int digit[1100];
int main(int argc,char**argv){assert(argc==6||argc==7);R=atoll(argv[1]);int K=atoi(argv[2]);U E=strtoull(argv[3],0,10),L=atoll(argv[4]),H=strtoull(argv[5],0,10);assert(R<1100&&K>=3&&K<=21&&K%2&&L>=1&&L<=H&&E>0);N=1;mod=1;
 for(int i=0;i<K;i++){assert(N<((Z)1<<110)/R);N*=R;}for(int i=0;i<=K/2;i++){assert(mod<UINT64_MAX/R);mod*=R;}
 for(U x=0;x<R;x++)digit[x*x%R]=1;if(argc==7){FILE*fp=fopen(argv[6],"r");assert(fp);int x;while(fscanf(fp,"%d",&x)==1){assert(0<=x&&x<R);digit[x]=1;}fclose(fp);}
 Z ma=(N/E+1)/2;if(ma<H)H=(U)ma;assert(H<(UINT64_MAX/8));U trials=0,hits=0;
 for(U t=L;t<=H;t++){
  U f=4*t-1;if(digit[(R-f%R)%R])continue;trials++;
  U rem=(U)(N%f),last=f,C0=1,C1=0;int neg=1;
  // Evens are floor-side (negative error). Update convergent denominator
  // from the Euclidean step; |c*N-b*f| is the alternating remainder.
  while(rem){if(!neg){U a=rem,c=C0;assert((Z)a*c<=f);U ac=a*c;if(t%ac==0){U d=t/ac;Z b=(N*c+a)/f;assert(b*f==N*c+a&&b<=((Z)1<<120));if(b>=a&&(a+b)%c==0){Z e=(a+b)/c;if(e>=E&&a%R&&b%R&&c%R&&d%R){U x=(mod-f%mod)%mod;U y=(1+mod-((Z)4*(b%mod)%mod*(c%mod)%mod*(d%mod)%mod))%mod;printf("%lu %lu\n",x,y);hits++;break;}}}}
    U q=last/rem,z=last%rem,cn=q*C0+C1;last=rem;rem=z;C1=C0;C0=cn;neg^=1;
  }}fprintf(stderr,"r %lu K %d t %lu %lu nonsquare trials %lu hits %lu\n",R,K,L,H,trials,hits);}
