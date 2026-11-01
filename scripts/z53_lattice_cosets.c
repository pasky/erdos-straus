/* z53_lattice_cosets.c — brute force: largest coset t+H (H subgroup of (Z/q)^3) contained in
   V_n(Z/q) = { (u,B,C) : 4CuB - u - B - n == 0 mod q }, over all t in V_n and (optionally sampled) n mod q.
   Prints, per q, max |H| over n,t, and the implied minimal index D' = q^3/|H| (for exactness modulus D = q).
   Usage: z53_lattice_cosets q [nstep] [tstep]   (nstep/tstep >1 subsample n and t).  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int q, Q3;
static unsigned char *inS;   /* membership in S_t = {h : G(t+h)=0} */
static unsigned char *good;  /* <h> subset of S_t */
static int *goodlist, ngood;
static unsigned char *cur;   /* current subgroup bitmap */
static int best;
static long long gmod(long long x){ x%=q; if(x<0)x+=q; return x; }
static int idx(int a,int b,int c){ return (a*q+b)*q+c; }
static void dec(int i,int*a,int*b,int*c){ *c=i%q; i/=q; *b=i%q; *a=i/q; }
static int addi(int i,int j){ int a,b,c,d,e,f; dec(i,&a,&b,&c); dec(j,&d,&e,&f); return idx((a+d)%q,(b+e)%q,(c+f)%q); }
/* closure of subgroup (list) with new generator g; returns size or -1 if leaves good */
static int *buf, *buf2;
static int closure(int *Hl,int hn,int g,int *out){
  /* <H,g> = { h + k g : h in H, k in 0..ord-1 } */
  static unsigned char *mark=0; if(!mark) mark=calloc(Q3,1);
  int on=0; int kg=0; /* kg = k*g */
  for(int k=0;k<q;k++){
    for(int i=0;i<hn;i++){ int e=addi(Hl[i],kg); if(!mark[e]){ if(!good[e]){ for(int j=0;j<on;j++)mark[out[j]]=0; return -1;} mark[e]=1; out[on++]=e; } }
    kg=addi(kg,g);
  }
  for(int j=0;j<on;j++)mark[out[j]]=0;
  return on;
}
static void dfs(int *Hl,int hn,int start,int depth){
  if(hn>best) best=hn;
  if(depth==3) return;
  int *out=malloc(sizeof(int)*Q3);
  unsigned char *inH=calloc(Q3,1); for(int i=0;i<hn;i++) inH[Hl[i]]=1;
  for(int gi=start;gi<ngood;gi++){ int g=goodlist[gi]; if(inH[g]) continue;
    int sz=closure(Hl,hn,g,out); if(sz<0) continue; if(sz<=hn) continue;
    dfs(out,sz,gi+1,depth+1);
    /* prune: if already best equals q^2*... no prune */
  }
  free(out); free(inH);
}
int main(int argc,char**argv){
  q=atoi(argv[1]); int nstep=argc>2?atoi(argv[2]):1; int tstep=argc>3?atoi(argv[3]):1;
  Q3=q*q*q; inS=malloc(Q3); good=malloc(Q3); goodlist=malloc(sizeof(int)*Q3);
  int globalbest=0; long long ntested=0;
  int histo[64]; memset(histo,0,sizeof histo);
  for(int n=0;n<q;n+=nstep){
    if(q%2==0 && n%2==0) continue; /* n odd */
    int nbest=0;
    for(int ti=0;ti<Q3;ti+=tstep){ int tu,tB,tC; dec(ti,&tu,&tB,&tC);
      if(gmod(4LL*tC*tu*tB - tu - tB - n)!=0) continue;
      ntested++;
      for(int h=0;h<Q3;h++){ int a,b,c; dec(h,&a,&b,&c); long long u=tu+a,B=tB+b,C=tC+c; inS[h]=(gmod(4*C*u*B-u-B-n)==0); }
      ngood=0;
      for(int h=0;h<Q3;h++){ good[h]=0; if(!inS[h]) continue; int e=0,ok=1; for(int k=0;k<q;k++){ if(!inS[e]){ok=0;break;} e=addi(e,h);} if(ok){good[h]=1; if(h) goodlist[ngood++]=h;} }
      best=1; int zero=0; dfs(&zero,1,0,0);
      if(best>nbest)nbest=best;
      int lg=0; while((1<<lg)<best) lg++; /* not used */
    }
    if(nbest>globalbest) globalbest=nbest;
    printf("q=%d n=%d max|H|=%d\n",q,n,nbest); fflush(stdout);
  }
  printf("SUMMARY q=%d tested_t=%lld max|H|=%d  min index D'=q^3/|H|=%d\n",q,ntested,globalbest,Q3/globalbest);
  return 0;
}
