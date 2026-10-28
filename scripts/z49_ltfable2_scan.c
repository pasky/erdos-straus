// z49 ltfable2: word census for primes p = 1 (mod 4) (or odd squares with -sq), coordinate-form certificate predicate.
// Words (t,u,v): tuv-u-v = n, t,u,v >= 1. Enumerated by the smaller endpoint u <= sqrt(n+1)+1 via divisors of n+u
// in the class -n (mod u) (smallest-prime-factor sieve), re-checked with uv | n+u+v.
// Coordinate classes: C_n = {x : x = 0 (mod 4) or x = -n (mod 8)}.
// Theorem 1 (coordinate form): (uv/n) = -1  <=>  some coordinate of (t,u,v) lies in C_n  (gcd(uv,n)=1).
// Per n we output: W (ordered words), Ncert_slot (five-slot predicate), Ncert_coord (Theorem 1 predicate),
//   Nt (t in C), Ne (u in C or v in C), Nte (both), Wfree, Ffree_cert, tC_min, uC_min (least coordinate in C over
//   level resp. endpoints), HC = min of the two, plus the I3 count.
// mode "cells": print the 160-cell vector (t,u,v mod 8, ordered words) per prime, for the rank computation.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint32_t *spf;
static long LIM;
static void sieve(long N){ spf=calloc(N+1,sizeof(uint32_t)); if(!spf){fprintf(stderr,"oom\n");exit(1);}
  for(long i=2;i<=N;i++) if(!spf[i]){ for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i; } LIM=N; }

static long divs[4096]; static int ndiv;
static void divisors(long m){ // m <= LIM
  long pr[32]; int ex[32]; int k=0;
  while(m>1){ long p=spf[m]; int e=0; while(m%p==0){m/=p;e++;} pr[k]=p; ex[k]=e; k++; }
  ndiv=1; divs[0]=1;
  for(int i=0;i<k;i++){ int cur=ndiv; long pe=1; for(int e=1;e<=ex[i];e++){ pe*=pr[i]; for(int j=0;j<cur;j++) divs[ndiv++]=divs[j]*pe; } }
}
static inline int inC(long x,long n){ return (x&3)==0 || ((x+n)&7)==0; }
static inline int slot(long t,long u,long v){ return (t&3)==0||(u&3)==0||(v&3)==0||((t*u-1)&3)==0||((t*v-1)&3)==0; }

int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: %s N mode[stats|cells|sq|list] [out]\n",argv[0]);return 1;}
  long N=atol(argv[1]); const char*mode=argv[2];
  FILE*out=argc>3?fopen(argv[3],"w"):stdout;
  // list mode: explicit n values on the command line after mode
  long listvals[64]; int nlist=0;
  if(!strcmp(mode,"list")){ for(int i=4;i<argc;i++){ listvals[nlist++]=atol(argv[i]); if(listvals[nlist-1]>N) N=listvals[nlist-1]; } }
  long S=(long)sqrt((double)N)+3; sieve(N+S+5);
  long viol=0, nprimes=0;
  // aggregates
  long cntHC[64]; memset(cntHC,0,sizeof cntHC); long histHC[130]; memset(histHC,0,sizeof histHC); long histuC[130]; memset(histuC,0,sizeof histuC); long histtC[130]; memset(histtC,0,sizeof histtC); double maxHC_L=0; long maxHC=0, maxHCp=0, maxuC=0,maxuCp=0,maxtC=0,maxtCp=0;
  long failsNt=0, failsNe=0, fails=0;
  long idx=0;
  for(long n=5; ; n+=4){
    if(!strcmp(mode,"list")){ if(idx>=nlist) break; n=listvals[idx++]; }
    else if(!strcmp(mode,"sq")){ long m=2*idx+3; idx++; n=m*m; if(n>N) break; }
    else { if(n>N) break; if(spf[n]!=(uint32_t)n) continue; }
    nprimes++;
    long W=0,Ns=0,Nc=0,Nt=0,Ne=0,Nte=0,Wf=0,Ff=0,I3=0; long tC=0,uC=0; int cells[512]; memset(cells,0,sizeof cells);
    long umax=(long)sqrt((double)(n+1))+2;
    for(long u=1;u<=umax;u++){
      long m=n+u; divisors(m);
      for(int i=0;i<ndiv;i++){ long v=divs[i]; if(v<u) continue; if((v+n)%u) continue;
        long s=n+u+v; if(s%(u*v)) continue; long t=s/(u*v);
        int mult=(v==u)?1:2;
        W+=mult; int sl=slot(t,u,v); int co=inC(t,n)||inC(u,n)||inC(v,n);
        if(sl!=co) viol++;
        Ns+=mult*sl; Nc+=mult*co;
        int it=inC(t,n), ie=inC(u,n)||inC(v,n);
        Nt+=mult*it; Ne+=mult*ie; Nte+=mult*(it&&ie);
        int fr=(t<=2||u<=2||v<=2); Wf+=mult*fr; Ff+=mult*(fr&&co); I3+=mult*(!fr);
        if(it && (tC==0||t<tC)) tC=t;
        if(inC(u,n) && (uC==0||u<uC)) uC=u;
        if(inC(v,n) && (uC==0||v<uC)) uC=v;
        if(!strcmp(mode,"cells")){ cells[((t&7)<<6)|((u&7)<<3)|(v&7)]+=1; if(v!=u) cells[((t&7)<<6)|((v&7)<<3)|(u&7)]+=1; }
      }
    }
    if(!strcmp(mode,"cells")){ fprintf(out,"%ld",n); for(int c=0;c<512;c++) if(cells[c]) fprintf(out," %d:%d",c,cells[c]); fprintf(out,"\n"); continue; }
    long HC = (tC&&uC)? (tC<uC?tC:uC) : (tC?tC:uC);
    double L=log((double)n);
    if(HC==0) fails++; if(Nt==0) failsNt++; if(Ne==0) failsNe++;
    if(HC>0){ histHC[HC<129?HC:129]++; histuC[uC<129?uC:129]++; histtC[tC<129?tC:129]++; int b=0; long h=HC; while(h>1){h>>=1;b++;} cntHC[b]++; if(HC/L>maxHC_L){maxHC_L=HC/L;maxHC=HC;maxHCp=n;} }
    if(uC>maxuC){maxuC=uC;maxuCp=n;} if(tC>maxtC){maxtC=tC;maxtCp=n;}
    if(!strcmp(mode,"list")||!strcmp(mode,"sq")||Nc==0||Nt==0||Ne==0||n<200||HC>=16)
      fprintf(out,"n=%ld W=%ld Nslot=%ld Ncoord=%ld Nt=%ld Ne=%ld Nte=%ld Wfree=%ld Ffree_cert=%ld I3=%ld tC=%ld uC=%ld HC=%ld\n",n,W,Ns,Nc,Nt,Ne,Nte,Wf,Ff,I3,tC,uC,HC);
  }
  if(strcmp(mode,"cells")){
    fprintf(out,"# count=%ld viol(slot!=coord)=%ld fails(HC=inf)=%ld fails(level line)=%ld fails(endpoint line)=%ld\n",nprimes,viol,fails,failsNt,failsNe);
    fprintf(out,"# max HC/log n = %.4f (HC=%ld at n=%ld); max uC=%ld at %ld; max tC=%ld at %ld\n",maxHC_L,maxHC,maxHCp,maxuC,maxuCp,maxtC,maxtCp);
    fprintf(out,"# exact histograms (value:count), 129 = >=129\n# HC:"); for(int i=0;i<130;i++) if(histHC[i]) fprintf(out," %d:%ld",i,histHC[i]);
    fprintf(out,"\n# uC:"); for(int i=0;i<130;i++) if(histuC[i]) fprintf(out," %d:%ld",i,histuC[i]);
    fprintf(out,"\n# tC:"); for(int i=0;i<130;i++) if(histtC[i]) fprintf(out," %d:%ld",i,histtC[i]);
    fprintf(out,"\n# HC distribution by floor(log2 HC):"); for(int b=0;b<40;b++) if(cntHC[b]) fprintf(out," [2^%d,2^%d):%ld",b,b+1,cntHC[b]); fprintf(out,"\n");
  }
  fclose(out); return 0;
}
