// z53 HCHYP: per-line success statistics for the six-coordinate (HC) certificate lines.
//
// For p = 1 (mod 8) and x in C_p = {x >= 4 : x = 0 (mod 4) or x = 7 (mod 8)}:
//   endpoint line E_x(p): p + x  has a divisor A = -1 (mod x)   (word (t,x,v), A = tx - 1, v = (p+x)/A)
//   level    line L_x(p): xp + 1 has a divisor d = -1 (mod x)   (word (x,u,v), d = xu - 1)
// HC(p) = least x in C_p at which E_x or L_x succeeds (LOWERTAIL_ROUND2_FABLE Cor 1.1).
// T1 control: for n = m^2 (odd) every line fails (mode "sq").
//
// Modes:
//   stat  <p_start> <count> <Xmax> <outfile>   : first <count> primes p = 1 (8), p >= p_start
//   int   <n_start> <count> <Xmax> <outfile>   : all non-square n = 1 (8), n >= n_start (integer null model)
//   sq    <m_start> <count> <Xmax> <outfile>   : odd squares n = m^2, m >= m_start (T1 control, expects 0 successes)
//   near  <k> <m_start> <count> <Xmax> <out>   : primes p = m^2 + k (p = 1 (8)), m >= m_start
//   list  <Xmax> <outfile> p1 p2 ...           : given p (any n = 1 (8)), per-line success bits
// Per-n file <out>.hc: n HC Z(64) Z(256) Z(1024) Z(Xmax), Z = number of successful lines (E and L counted separately).
// Output (stat/sq/near): per x: #E successes, #L successes, #either; histogram of HC; joint-failure counts
//   F(X) = #{p : no line with x <= X succeeds} for every x in C;  plus per-p HC list (optional file .hc).
//
// Build: gcc -O2 -o /tmp/z53lines scripts/z53_hchyp_lines.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;

static u64 mulmod(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1%m;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){
  if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){if(n%sp[i]==0)return n==sp[i];}
  u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){u64 a=sp[i];u64 x=powmod(a,d,n);if(x==1||x==n-1)continue;int ok=0;
    for(int r=1;r<s;r++){x=mulmod(x,x,n);if(x==n-1){ok=1;break;}} if(!ok)return 0;}
  return 1;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){ // Brent
  if(n%2==0)return 2; static u64 seed=1;
  for(;;){ u64 c=(seed++)%(n-1)+1, y=(seed*7919)%n, m=128, g=1, r=1, q=1, x=0, ys=0;
    do{ x=y; for(u64 i=0;i<r;i++) y=(mulmod(y,y,n)+c)%n; u64 k=0;
      do{ ys=y; for(u64 i=0;i<m && i<r-k;i++){ y=(mulmod(y,y,n)+c)%n; q=mulmod(q, x>y?x-y:y-x, n);} g=gcdu(q,n); k+=m; }while(k<r && g==1);
      r<<=1; }while(g==1);
    if(g==n){ do{ ys=(mulmod(ys,ys,n)+c)%n; g=gcdu(x>ys?x-ys:ys-x,n);}while(g==1); }
    if(g!=n) return g; }
}
#define MAXF 64
static int nsp; static unsigned sp_small[2000];
static void init_small(void){ nsp=0; for(unsigned i=2;i<15000 && nsp<2000;i++){int ok=1;for(int j=0;j<nsp&&sp_small[j]*sp_small[j]<=i;j++)if(i%sp_small[j]==0){ok=0;break;} if(ok)sp_small[nsp++]=i;} }
static int fac_rec(u64 n,u64*P,int*E,int k){
  if(n==1)return k;
  if(isprime(n)){ for(int i=0;i<k;i++) if(P[i]==n){E[i]++;return k;} P[k]=n;E[k]=1;return k+1;}
  u64 d=rho(n); k=fac_rec(d,P,E,k); return fac_rec(n/d,P,E,k);
}
static int factor(u64 n,u64*P,int*E){ int k=0;
  for(int i=0;i<nsp;i++){u64 q=sp_small[i]; if(q*q>n)break; if(n%q==0){P[k]=q;E[k]=0;while(n%q==0){n/=q;E[k]++;}k++;}}
  if(n>1) k=fac_rec(n,P,E,k); return k;}
// does N (factored) have a divisor = target (mod x)?  enumerate residues of divisors mod x with a bitmap (x <= 65536)
static unsigned char seen[1<<17], seen2[1<<17]; static int list[1<<17];
static int has_div_class(u64*P,int*E,int k,u64 x,u64 target){
  // set of residues of divisors mod x, BFS over prime powers; residue-set size <= x
  int n=1; list[0]=1%x; memset(seen,0,x); seen[1%x]=1;
  if((1%x)==target) return 1;
  for(int i=0;i<k;i++){ u64 pr=P[i]%x; int n0=n;
    for(int j=0;j<n0;j++){ u64 r=list[j];
      for(int e=1;e<=E[i];e++){ r=(r*pr)%x; if(!seen[r]){ if(r==target) return 1; seen[r]=1; list[n++]=r; } } }
  }
  return 0;
}
static int inC(u64 x){ return x>=4 && (x%4==0 || x%8==7); }

static int XMAX;
static long *cE,*cL,*cB,*joint; static long hist[100000]; static long nn=0, nofail_all=0;
static FILE *hcout=NULL;
static void process(u64 n, int verbose, FILE*out){
  u64 P[MAXF]; int E[MAXF];
  long HC=0; int anyfirst=0;
  // joint: firstsucc = least x with success; joint[x] counts n with firstsucc > x
  u64 first=0; long Z64=0,Z256=0,Z1024=0,Zall=0;
  for(u64 x=4;x<=(u64)XMAX;x++){ if(!inC(x))continue;
    int k=factor(n+x,P,E); int e=has_div_class(P,E,k,x,x-1);
    k=factor(x*n+1,P,E); int l=has_div_class(P,E,k,x,x-1);
    if(e)cE[x]++; if(l)cL[x]++; if(e||l){cB[x]++; if(!first)first=x;}
    { int z=e+l; Zall+=z; if(x<=64)Z64+=z; if(x<=256)Z256+=z; if(x<=1024)Z1024+=z; }
    if(verbose) fprintf(out,"%llu x=%llu E=%d L=%d\n",n,x,e,l);
  }
  nn++;
  if(!first) nofail_all++;
  for(u64 x=4;x<=(u64)XMAX;x++) if(inC(x) && (first==0 || first>x)) joint[x]++;
  if(first) hist[first]++;
  if(hcout) fprintf(hcout,"%llu %llu %ld %ld %ld %ld\n",n,first,Z64,Z256,Z1024,Zall);
  (void)HC;(void)anyfirst;
}
static void report(FILE*out,const char*tag){
  fprintf(out,"# %s n_count=%ld Xmax=%d all_lines_fail=%ld\n",tag,nn,XMAX,nofail_all);
  fprintf(out,"# x  E_succ  L_succ  either  F(x)=#{no success at any line <= x}\n");
  for(int x=4;x<=XMAX;x++) if(inC(x)) fprintf(out,"%d %ld %ld %ld %ld\n",x,cE[x],cL[x],cB[x],joint[x]);
  fprintf(out,"# HC histogram (value:count):");
  for(int x=4;x<=XMAX;x++) if(hist[x]) fprintf(out," %d:%ld",x,hist[x]);
  fprintf(out,"\n");
}
int main(int argc,char**argv){
  init_small();
  if(argc<2){fprintf(stderr,"usage\n");return 1;}
  const char*mode=argv[1];
  if(!strcmp(mode,"list")){ XMAX=atoi(argv[2]); FILE*out=fopen(argv[3],"w");
    cE=calloc(XMAX+1,sizeof(long));cL=calloc(XMAX+1,sizeof(long));cB=calloc(XMAX+1,sizeof(long));joint=calloc(XMAX+1,sizeof(long));
    for(int i=4;i<argc;i++){ u64 n=strtoull(argv[i],0,10); process(n,1,out);} fclose(out); return 0; }
  int ai=2; long kshift=0; if(!strcmp(mode,"near")) kshift=atol(argv[ai++]);
  u64 start=strtoull(argv[ai++],0,10); long count=atol(argv[ai++]); XMAX=atoi(argv[ai++]); const char*of=argv[ai++];
  if(XMAX>=(1<<17)){fprintf(stderr,"Xmax too big\n");return 1;}
  cE=calloc(XMAX+1,sizeof(long));cL=calloc(XMAX+1,sizeof(long));cB=calloc(XMAX+1,sizeof(long));joint=calloc(XMAX+1,sizeof(long));
  char hcf[512]; snprintf(hcf,sizeof hcf,"%s.hc",of); hcout=fopen(hcf,"w");
  FILE*out=fopen(of,"w");
  if(!strcmp(mode,"stat")){ u64 p=start; while(p%8!=1)p++; long got=0;
    for(;got<count;p+=8){ if(!isprime(p))continue; process(p,0,out); got++; } report(out,"stat"); }
  else if(!strcmp(mode,"int")){ u64 p=start; while(p%8!=1)p++; long got=0;
    for(;got<count;p+=8){ u64 r=(u64)sqrtl((long double)p); while(r*r>p)r--; while((r+1)*(r+1)<=p)r++; if(r*r==p)continue; process(p,0,out); got++; } report(out,"int"); }
  else if(!strcmp(mode,"sq")){ u64 m=start|1; for(long i=0;i<count;i++,m+=2){ process(m*m,0,out);} report(out,"sq"); }
  else if(!strcmp(mode,"near")){ u64 m=start; long got=0; for(;got<count;m++){ u64 p=m*m+kshift; if(p%8!=1||!isprime(p))continue; process(p,0,out); got++;} report(out,"near"); }
  fclose(out); if(hcout)fclose(hcout); return 0;
}
