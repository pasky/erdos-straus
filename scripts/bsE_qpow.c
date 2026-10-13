/* bsE_qpow.c (O178): ET Type I / Type II slices restricted to prime-power moduli.
   For n in a candidate set (primes 5..NMAX, or odd squares <= NMAX as the T1 control) and a fixed odd prime q:
     F_I(n)  = #{(s,a,b): t = q^s <= n+2, 4 | tn+1, ab | (tn+1)/4, t | a+b}      (ET Type I with t = q^s)
     F_II(n) = #{(s,a,b): e = q^s,        4 | n+e,  ab | (n+e)/4,  e | a+b}      (ET Type II with e = q^s)
   (ET Prop 2.3/2.7 as in CONDITIONAL_ES Lemma 1.2; each triple is one ES solution.)
   Also records, per n, the least s that works for each type.
   usage: bsE_qpow q NMAX mode   (mode 0 = primes, 1 = odd squares)   prints a summary.
   Factorisation: per s, sieve the linear form (t n + 1)/4 over n <= NMAX by primes <= sqrt(max), cofactor > 1 prime. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
#define MAXF 24
static int NMAX; static u64 *rem; static uint32_t *fp; static uint8_t *fe, *nf; static char *cand;
static int *primes; static int np;
static u64 cnt_t; /* modulus for counting */
static u64 pairs_count(u64 *pr, int *ex, int k, int i, u64 am, u64 bm){
  if(i==k) return ((am+bm)%cnt_t)==0;
  u64 c=0, pa=1;
  for(int x=0;x<=ex[i];x++){ u64 pb=1;
    for(int y=0;x+y<=ex[i];y++){ c+=pairs_count(pr,ex,k,i+1,(u64)((u128)am*pa%cnt_t),(u64)((u128)bm*pb%cnt_t)); pb=pb*pr[i]; }
    pa=pa*pr[i]; }
  return c;
}
static u64 count_M(u64 M, u64 t, u64 *pr0, int *ex0, int k0){ /* given factorisation */
  cnt_t=t; return pairs_count(pr0,ex0,k0,0,1%t,1%t);
}
static void addf(int n, u64 l){ /* divide rem[n] by l fully, record */
  int e=0; while(rem[n]%l==0){ rem[n]/=l; e++; }
  if(e){ int j=nf[n]; if(j<MAXF){ fp[(size_t)n*MAXF+j]=(uint32_t)l; fe[(size_t)n*MAXF+j]=e; nf[n]++; } else { fprintf(stderr,"MAXF\n"); exit(1);} }
}
static u64 powmod(u64 b,u64 e,u64 m){ u64 r=1%m; b%=m; while(e){ if(e&1) r=(u128)r*b%m; b=(u128)b*b%m; e>>=1;} return r; }
int main(int argc,char**argv){
  if(argc<4){ fprintf(stderr,"usage\n"); return 1; }
  int q=atoi(argv[1]); NMAX=atoi(argv[2]); int mode=atoi(argv[3]);
  int SL = (int)sqrt((double)NMAX*(NMAX+2)/4.0)+10; if(SL<NMAX+10) SL=NMAX+10;
  char *comp=calloc(SL+1,1); primes=malloc(sizeof(int)*(SL/2+100)); np=0;
  for(int i=2;i<=SL;i++){ if(!comp[i]){ primes[np++]=i; for(long j=(long)i*i;j<=SL;j+=i) comp[j]=1; } }
  cand=calloc(NMAX+1,1);
  if(mode==0){ for(int n=5;n<=NMAX;n++) if(!comp[n]) cand[n]=1; }
  else { for(long m=3;m*m<=NMAX;m+=2) cand[m*m]=1; }
  rem=malloc(sizeof(u64)*(NMAX+1)); fp=malloc((size_t)(NMAX+1)*MAXF*4); fe=malloc((size_t)(NMAX+1)*MAXF); nf=malloc(NMAX+1);
  double persI[64]={0},persII[64]={0}; u64 *FI=calloc(NMAX+1,8), *FII=calloc(NMAX+1,8); int *sI=malloc(4*(NMAX+1)), *sII=malloc(4*(NMAX+1));
  for(int n=0;n<=NMAX;n++){ sI[n]=-1; sII[n]=-1; }
  for(int type=1;type<=2;type++){
    u64 t=1; for(int s=0; ; s++, t*=q){
      if(type==1 && t > (u64)NMAX+2) break;
      if(type==2 && t > (u64)NMAX) break;
      int any=0;
      for(int n=0;n<=NMAX;n++){ nf[n]=0; rem[n]=0;
        if(!cand[n]) continue;
        if(type==1){ if(t>(u64)n+2) continue; u64 N=t*(u64)n+1; if(N%4) continue; rem[n]=N/4; }
        else { u64 N=(u64)n+t; if(N%4) continue; rem[n]=N/4; }
        any=1; }
      if(!any) continue;
      for(int i=0;i<np;i++){ u64 l=primes[i];
        if(type==1){ if(l*l > (t*(u64)NMAX+1)/4+1) break; }
        else { if(l*l > ((u64)NMAX+t)/4+1) break; }
        /* n with l | M:  type1: 4M = t n + 1 == 0 mod l  (l odd, l != q): n == -t^{-1};  l = 2: check all.
                          type2: n + t == 0 mod l (l odd): n == -t; l=2: all */
        if(l==2){ for(int n=0;n<=NMAX;n++) if(rem[n]) addf(n,2); continue; }
        if((u64)q==l && type==1) continue;
        u64 r = (type==1) ? (l - powmod(t%l, l-2, l)) % l : (l - t%l) % l;
        for(u64 n=r; n<=(u64)NMAX; n+=l) if(rem[n]) addf((int)n,l);
      }
      for(int n=0;n<=NMAX;n++){ if(!rem[n]) continue;
        u64 pr[MAXF+1]; int ex[MAXF+1]; int k=nf[n];
        for(int j=0;j<k;j++){ pr[j]=fp[(size_t)n*MAXF+j]; ex[j]=fe[(size_t)n*MAXF+j]; }
        if(rem[n]>1){ pr[k]=rem[n]; ex[k]=1; k++; }
        u64 c=count_M(0,t,pr,ex,k);
        if(type==1) persI[s]+=c; else persII[s]+=c;
        if(c){ if(type==1){ FI[n]+=c; if(sI[n]<0) sI[n]=s; } else { FII[n]+=c; if(sII[n]<0) sII[n]=s; } }
      }
    }
  }
  long tot=0,zI=0,zII=0,zB=0; double minr=1e99; int argmin=0; int maxsI=0,maxsII=0,maxsB=0,amI=0,amII=0,amB=0;
  int printed=0;
  for(int n=0;n<=NMAX;n++){ if(!cand[n]) continue; tot++;
    if(!FI[n]) zI++; if(!FII[n]) zII++;
    if(!FI[n]&&!FII[n]){ zB++; if(printed<20){ printf("both-empty n=%d (n mod 24 = %d)\n",n,n%24); printed++; } }
    double L=log((double)n); double r=(FI[n]+FII[n])/(L*L); if(r<minr){ minr=r; argmin=n; }
    if(sI[n]>maxsI){maxsI=sI[n];amI=n;} if(sII[n]>maxsII){maxsII=sII[n];amII=n;}
    int sb = (sI[n]<0)?sII[n]:((sII[n]<0)?sI[n]:(sI[n]<sII[n]?sI[n]:sII[n]));
    if(sb>maxsB){maxsB=sb;amB=n;}
  }
  printf("q=%d NMAX=%d mode=%s: candidates %ld; F_I=0: %ld; F_II=0: %ld; both=0: %ld\n",q,NMAX,mode?"oddsquares":"primes",tot,zI,zII,zB);
  printf("min (F_I+F_II)/log^2 n = %.4f at n=%d (F_I=%llu F_II=%llu)\n",minr,argmin,(unsigned long long)FI[argmin],(unsigned long long)FII[argmin]);
  printf("max least-s: TypeI %d (n=%d), TypeII %d (n=%d), either %d (n=%d)\n",maxsI,amI,maxsII,amII,maxsB,amB);
  printf("mean count per s (over candidates): s: TypeI TypeII\n"); for(int s=0;s<40;s++) if(persI[s]||persII[s]) printf("  s=%d %.4f %.4f\n",s,persI[s]/tot,persII[s]/tot);
  return 0;
}
