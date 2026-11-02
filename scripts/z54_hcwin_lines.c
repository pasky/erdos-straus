// z54 HCWIN: per-line anatomy / genus / class data for the HC lines, and window masses.
//
// For n = 1 (mod 8) and x in C = {x >= 4 : x = 0 (4) or x = 7 (8)}, lines iota = (x,E): N = n + x, (x,L): N = x n + 1.
// Per line:  tau(N);  genus count g = #{d | N : d in -G_x^2}  (G_x = (Z/x)^*);  class count c = #{d | N : d = -1 (mod x)};
//            mind = min over certificate divisors d of min(d, N/d)  (0 if c = 0);  o_T = #{d | N : min(d,N/d) <= T}.
// Window masses at X (lines with x <= X):  Lam = sum min(1, tau/phi(x)),  Gam = sum min(1, g/|G_x^2|),
//            Z = #successful lines, LamOut = sum min(1, o_X/phi(x)), Zout = #lines with mind <= X (outer certificate).
// Output per n (one line):  n HC  then for each X in {8,16,...,1024} (up to Xmax): Lam Gam Z LamOut Zout GE GL
//   (GE, GL = untruncated sums of m = g/|G_x^2| over E-lines, resp. L-lines, with x <= X)
// Output <out>.lines : per (type, dyadic j of x, bin of log2(m)) counts and successes, m = g/|G^2| (and m' = tau/phi).
//
// Modes:  stat <start> <count> <Xmax> <out>   primes p = 1 (8) from start
//         int  <start> <count> <Xmax> <out>   non-square n = 1 (8)
//         sq   <m_start> <count> <Xmax> <out> odd squares
//         near <k> <m_start> <count> <Xmax> <out>   primes m^2 + k = 1 (8)
//         list <Xmax> <out> n1 n2 ...
// Build: gcc -O2 -o /tmp/z54hcwin scripts/z54_hcwin_lines.c -lm
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
static int inC(u64 x){ return x>=4 && (x%4==0 || x%8==7); }

// ---- per-x data: phi, real-character basis ----
#define XM 4097
static int phi_[XM], rk[XM], nq[XM], qs[XM][8], two_e[XM];
static unsigned char *qr[XM]; // qr[q][a] = 1 if a is a nonzero square mod q (q odd prime)
static void init_x(int Xmax){
  for(int x=1;x<=Xmax;x++){ int n=x, ph=x; nq[x]=0; two_e[x]=0;
    while(n%2==0){n/=2;two_e[x]++;} if(two_e[x]) ph=ph/2;
    for(int q=3;q*q<=n;q+=2) if(n%q==0){ qs[x][nq[x]++]=q; ph=ph/q*(q-1); while(n%q==0)n/=q; }
    if(n>1){ qs[x][nq[x]++]=n; ph=ph/n*(n-1); }
    phi_[x]=ph; rk[x]=nq[x]+(two_e[x]==2?1:(two_e[x]>=3?2:0)); }
  for(int q=3;q<=Xmax;q+=2){ int pr=1; for(int d=3;d*d<=q;d+=2) if(q%d==0){pr=0;break;} if(!pr)continue;
    qr[q]=calloc(q,1); for(long a=1;a<q;a++) qr[q][a*a%q]=1; }
}
static unsigned vec(int x,u64 n){ // bit vector of real characters (value -1 -> bit 1); n coprime to x
  unsigned v=0; int b=0;
  for(int i=0;i<nq[x];i++){ int q=qs[x][i]; if(!qr[q][n%q]) v|=1u<<b; b++; }
  if(two_e[x]>=2){ if(n%4==3) v|=1u<<b; b++; }
  if(two_e[x]>=3){ int r=n%8; if(r==3||r==5) v|=1u<<b; b++; }
  return v;
}
// ---- divisor enumeration ----
static u64 divs[1<<20];
static int ndivs(u64*P,int*E,int k){ int n=1; divs[0]=1;
  for(int i=0;i<k;i++){ int n0=n; u64 pp=1; for(int e=1;e<=E[i];e++){ pp*=P[i]; for(int j=0;j<n0;j++){ if(n>=(1<<20)) return -1; divs[n++]=divs[j]*pp; } } }
  return n; }

#define NT 9
static const int TH[NT]={8,16,32,64,128,256,512,1024,2048};
static int XMAX, nth;
// per-line bins: type(2) x dyadic j (13) x mbin (61, log2 m in [-15,15] step .5) : count, succ ; same for tau/phi
#define NJ 13
#define NB 61
static long binC[2][NJ][NB], binS[2][NJ][NB], binC2[2][NJ][NB], binS2[2][NJ][NB];
static long confined[2][NJ], confsucc[2][NJ], linecount[2][NJ];
static int mbin(double m){ if(m<=0) return 0; double l=log2(m); int b=(int)floor(l*2)+31; if(b<1)b=1; if(b>=NB)b=NB-1; return b; }

typedef struct { double tau, g, gm, mo[NT]; long c; u64 mind; } LineRes;
static void doline(u64 N,int x,LineRes*R){
  // only divisors coprime to x matter (d = -1 mod x forces gcd(d,x)=1): strip primes of x (never needed at primes p > x)
  { u64 g; while((g=gcdu(N,(u64)x))>1) N/=g; }
  u64 P[MAXF]; int E[MAXF]; int k=factor(N,P,E);
  double tau=1; for(int i=0;i<k;i++) tau*=(E[i]+1);
  // genus DP
  int r=rk[x]; int S=1<<r; double cnt[1<<12], nw[1<<12]; for(int s=0;s<S;s++)cnt[s]=0; cnt[0]=1;
  for(int i=0;i<k;i++){ unsigned v=vec(x,P[i]); double ev=E[i]/2+1, od=(E[i]+1)/2;
    for(int s=0;s<S;s++) nw[s]=cnt[s]*ev+cnt[s^v]*od; for(int s=0;s<S;s++)cnt[s]=nw[s]; }
  double g=cnt[vec(x,(u64)x-1)];
  R->tau=tau; R->g=g; R->gm=g*(double)S/(double)phi_[x];
  // class count via divisors
  int nd=ndivs(P,E,k); long c=0; u64 mind=0; for(int t=0;t<nth;t++)R->mo[t]=0;
  if(nd<0){ fprintf(stderr,"too many divisors N=%llu\n",N); exit(2); }
  for(int j=0;j<nd;j++){ u64 d=divs[j], e=N/d, m=d<e?d:e;
    for(int t=0;t<nth;t++) if(m<=(u64)TH[t]) R->mo[t]+=1;
    if(d%x==(u64)x-1){ c++; if(mind==0||m<mind)mind=m; } }
  R->c=c; R->mind=mind;
}
static FILE *pout;
static long nn=0;
static void process(u64 n){
  double Lam[NT]={0},Gam[NT]={0},LO[NT]={0},GE[NT]={0},GL[NT]={0}; long Z[NT]={0},ZO[NT]={0}; u64 HC=0;
  for(int x=4;x<=XMAX;x++){ if(!inC(x)) continue; if((u64)x>=n) break;
    for(int ty=0;ty<2;ty++){ u64 N= ty==0 ? n+x : (u64)x*n+1; LineRes R; doline(N,x,&R);
      int succ = R.c>0; if(succ && (HC==0||(u64)x<HC)) HC=x;
      double ph=phi_[x]; double lam=R.tau/ph; if(lam>1)lam=1; double gam=R.gm; if(gam>1)gam=1;
      for(int t=0;t<nth;t++) if(x<=TH[t]){ Lam[t]+=lam; Gam[t]+=gam; Z[t]+=succ; if(ty==0) GE[t]+=R.gm; else GL[t]+=R.gm; double lo=R.mo[t]/ph; LO[t]+= lo>1?1:lo; if(succ && R.mind<=(u64)TH[t]) ZO[t]++; }
      int j=0; while((2<<j)<=x) j++; if(j>=NJ) j=NJ-1;
      int b=mbin(R.gm); binC[ty][j][b]++; binS[ty][j][b]+=succ;
      int b2=mbin(R.tau/ph); binC2[ty][j][b2]++; binS2[ty][j][b2]+=succ;
      linecount[ty][j]++; if(R.g==0){ confined[ty][j]++; confsucc[ty][j]+=succ; }
    }
  }
  fprintf(pout,"%llu %llu",n,HC);
  for(int t=0;t<nth;t++) fprintf(pout," %.2f %.2f %ld %.2f %ld %.3g %.3g",Lam[t],Gam[t],Z[t],LO[t],ZO[t],GE[t],GL[t]);
  fprintf(pout,"\n"); nn++;
}
static void report(const char*of,const char*tag){
  char fn[600]; snprintf(fn,sizeof fn,"%s.lines",of); FILE*f=fopen(fn,"w");
  fprintf(f,"# %s n=%ld Xmax=%d ; rows: kind type j bin lo2 count succ   (kind G: m=g/|G^2| ; kind T: m=tau/phi ; bin 0 = m=0)\n",tag,nn,XMAX);
  for(int ty=0;ty<2;ty++) for(int j=0;j<NJ;j++){
    for(int b=0;b<NB;b++) if(binC[ty][j][b]) fprintf(f,"G %c %d %d %.1f %ld %ld\n","EL"[ty],j,b,(b-31)/2.0,binC[ty][j][b],binS[ty][j][b]);
    for(int b=0;b<NB;b++) if(binC2[ty][j][b]) fprintf(f,"T %c %d %d %.1f %ld %ld\n","EL"[ty],j,b,(b-31)/2.0,binC2[ty][j][b],binS2[ty][j][b]);
    if(linecount[ty][j]) fprintf(f,"C %c %d lines %ld genus_confined %ld confined_succ %ld\n","EL"[ty],j,linecount[ty][j],confined[ty][j],confsucc[ty][j]);
  }
  fclose(f);
}
// scan mode: light per-prime record for joint-failure calibration at small windows.
// per prime: p HC then for X in SX: GE GL (untruncated genus sums over E resp. L lines with x <= X); lines up to 64.
static const int SX[]={8,12,16,20,24,28,32,40,48,64}; 
#define NSX 10
static void scan(u64 n){
  double GE[NSX]={0},GL[NSX]={0}; u64 HC=0;
  for(int x=4;x<=64;x++){ if(!inC(x)) continue;
    for(int ty=0;ty<2;ty++){ u64 N= ty==0 ? n+x : (u64)x*n+1; LineRes R; doline(N,x,&R);
      if(R.c>0 && (HC==0||(u64)x<HC)) HC=x;
      for(int t=0;t<NSX;t++) if(x<=SX[t]){ if(ty==0) GE[t]+=R.gm; else GL[t]+=R.gm; } } }
  fprintf(pout,"%llu %llu",n,HC); for(int t=0;t<NSX;t++) fprintf(pout," %.3g %.3g",GE[t],GL[t]); fprintf(pout,"\n");
}
int main(int argc,char**argv){
  init_small();
  if(argc<2){fprintf(stderr,"usage\n");return 1;}
  const char*mode=argv[1]; const char*of;
  if(!strcmp(mode,"scan")){ u64 p=strtoull(argv[2],0,10); long count=atol(argv[3]); of=argv[4]; XMAX=64; init_x(64); nth=1;
    pout=fopen(of,"w"); while(p%8!=1)p++; long got=0; for(;got<count;p+=8){ if(!isprime(p))continue; scan(p); got++; } fclose(pout); return 0; }
  if(!strcmp(mode,"list")){ XMAX=atoi(argv[2]); of=argv[3]; init_x(XMAX); nth=0; while(nth<NT&&TH[nth]<=XMAX)nth++;
    pout=fopen(of,"w"); for(int i=4;i<argc;i++){ u64 n=strtoull(argv[i],0,10); process(n);} fclose(pout); report(of,"list"); return 0; }
  int ai=2; long kshift=0; if(!strcmp(mode,"near")) kshift=atol(argv[ai++]);
  u64 start=strtoull(argv[ai++],0,10); long count=atol(argv[ai++]); XMAX=atoi(argv[ai++]); of=argv[ai++];
  if(XMAX>=XM){fprintf(stderr,"Xmax too big\n");return 1;}
  init_x(XMAX); nth=0; while(nth<NT&&TH[nth]<=XMAX)nth++;
  pout=fopen(of,"w");
  if(!strcmp(mode,"stat")){ u64 p=start; while(p%8!=1)p++; long got=0;
    for(;got<count;p+=8){ if(!isprime(p))continue; process(p); got++; } }
  else if(!strcmp(mode,"int")){ u64 p=start; while(p%8!=1)p++; long got=0;
    for(;got<count;p+=8){ u64 r=(u64)sqrtl((long double)p); while(r*r>p)r--; while((r+1)*(r+1)<=p)r++; if(r*r==p)continue; process(p); got++; } }
  else if(!strcmp(mode,"sq")){ u64 m=start|1; for(long i=0;i<count;i++,m+=2){ process(m*m);} }
  else if(!strcmp(mode,"near")){ u64 m=start; long got=0; for(;got<count;m++){ u64 p=m*m+kshift; if(p%8!=1||!isprime(p))continue; process(p); got++;} }
  fclose(pout); report(of,mode); return 0;
}
