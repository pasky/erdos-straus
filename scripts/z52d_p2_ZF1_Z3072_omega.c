// z52d Pass-2 ZF1/S6, items Z3072 (P(certificate at C | Omega(4Cp+1)=k)) and Z2306 (parity test).
// For each prime p in a list, C = 1..CMAX: fully factor N_C = 4Cp+1 by a sieve over C (primes l <= sqrt(4*CMAX*pmax+1)),
// count r_C = #{d | N_C : d ≡ -1 (mod 4C)} (the (★) divisor-form count at level C, FRONTIER §2.1), and tabulate:
//   T1[k][b]  : number of (p,C) with Omega(N_C)=k, C-bucket b (b = floor(log10 C)), and how many have r_C>0, sum r_C
//   T2[o][t][b]: parity test: N = s*r, s = N^{1/3}-smooth part, r = rough part (Omega(r) in {0,1,2});
//               o = Omega(r), t = min(tau(s),63) bucketed, b = C-bucket; counts / successes.
// Usage: prog CMAX  < primes.txt   (one prime per line). Output: text tables to stdout.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;
#define MAXF 16
static int CMAX; static uint32_t *plist; static int np;
static u64 *rem; static uint32_t (*fp)[MAXF]; static uint8_t (*fe)[MAXF]; static uint8_t *nf;
static long long inv_mod(long long a, long long m){ long long g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; long long b=a1;
  // extended Euclid on (b, m)
  long long r0=m,r1=b,s0=0,s1=1; while(r1){ long long q=r0/r1,t=r0-q*r1; r0=r1;r1=t; t=s0-q*s1; s0=s1;s1=t;} (void)g;(void)x;(void)x1;
  if(s0<0)s0+=m; return s0; }
#define KMAX 24
#define NB 6
static double T1n[KMAX][NB], T1s[KMAX][NB], T1r[KMAX][NB];
static double T2n[3][8][NB], T2s[3][8][NB];
// divisor enumeration counting d ≡ -1 mod q
static int cnt_div_target(int nfac, const uint32_t *pr, const uint8_t *ex, u64 q, u64 target);
static int cnt_div(int nfac, const uint32_t *pr, const uint8_t *ex, u64 big, u64 q){
  // divisors as residues mod q; include 'big' prime (if >1) as an extra prime factor exponent 1
  static u64 res[1<<16]; int n=1; res[0]=1%q;
  for(int i=0;i<=nfac;i++){ u64 P; int e; if(i<nfac){P=pr[i];e=ex[i];} else { if(big<=1) break; P=big; e=1; }
    int n0=n; u64 pm=P%q, pw=1;
    for(int j=1;j<=e;j++){ pw=(u64)((u128)pw*pm%q); for(int t=0;t<n0;t++){ if(n>=(1<<16)){fprintf(stderr,"tau overflow\n");exit(1);} res[n++]=(u64)((u128)res[t]*pw%q);} }
  }
  int c=0; for(int t=0;t<n;t++) if(res[t]==q-1) c++; return c; }
int cnt_div_target(int nfac, const uint32_t *pr, const uint8_t *ex, u64 q, u64 target){
  static u64 res[1<<16]; int n=1; res[0]=1%q;
  for(int i=0;i<nfac;i++){ int n0=n; u64 pm=pr[i]%q,pw=1; for(int j=1;j<=ex[i];j++){ pw=(u64)((u128)pw*pm%q); for(int t=0;t<n0;t++) res[n++]=(u64)((u128)res[t]*pw%q);} }
  int c=0; for(int t=0;t<n;t++) if(res[t]==target) c++; return c; }
static double T3s[KMAX],T3v[KMAX];
int main(int argc,char**argv){
  CMAX=atoi(argv[1]); u64 ps[100000]; int nps=0; u64 x; u64 pmax=0;
  while(scanf("%llu",&x)==1){ ps[nps++]=x; if(x>pmax)pmax=x; }
  u64 L=(u64)sqrt((double)(4.0*CMAX*(double)pmax+1))+2;
  char *sv=calloc(L+1,1); plist=malloc(sizeof(uint32_t)*(L/2+10)); np=0;
  for(u64 i=2;i<=L;i++) if(!sv[i]){ plist[np++]=i; for(u64 j=i*i;j<=L;j+=i) sv[j]=1; }
  free(sv);
  rem=malloc(sizeof(u64)*(CMAX+1)); fp=malloc(sizeof(*fp)*(CMAX+1)); fe=malloc(sizeof(*fe)*(CMAX+1)); nf=malloc(CMAX+1);
  long long totalpairs=0, zero_p=0;
  for(int ip=0;ip<nps;ip++){ u64 p=ps[ip];
    for(int C=1;C<=CMAX;C++){ rem[C]=4ULL*C*p+1; nf[C]=0; }
    for(int i=1;i<np;i++){ u64 l=plist[i]; if(l==p) continue; // l=2 never divides N (odd)
      long long a=(long long)((4*(p%l))%l); long long C0=(l-inv_mod(a,l))%l; // 4pC ≡ -1
      if(C0==0) C0=l;
      for(long long C=C0;C<=CMAX;C+=l){ int e=0; while(rem[C]%l==0){rem[C]/=l;e++;}
        if(e){ if(nf[C]>=MAXF){fprintf(stderr,"MAXF\n");exit(1);} fp[C][nf[C]]=l; fe[C][nf[C]]=e; nf[C]++; } } }
    int anyp=0; long long succ_p=0, vis_p=0;
    for(int C=1;C<=CMAX;C++){ u64 N=4ULL*C*p+1; u64 big=rem[C]; // big is 1 or a prime > L
      int Om=(big>1); for(int j=0;j<nf[C];j++) Om+=fe[C][j];
      u64 q=4ULL*C; int r=cnt_div(nf[C],fp[C],fe[C],big,q);
      int b=0; for(int c=C;c>=10;c/=10) b++; if(b>=NB)b=NB-1; int k=Om<KMAX?Om:KMAX-1;
      T1n[k][b]++; if(r>0){T1s[k][b]++; anyp=1;} T1r[k][b]+=r;
      // parity split: rough part = prime factors > N^{1/3}
      double z=cbrt((double)N); int orough=0; double taus=1;
      for(int j=0;j<nf[C];j++){ if((double)fp[C][j]>z) orough+=fe[C][j]; else taus*=(fe[C][j]+1); }
      if(big>1) orough++;
      int t= taus<2?0: taus<3?1: taus<5?2: taus<9?3: taus<17?4: taus<33?5: taus<65?6:7;
      if(orough>2){fprintf(stderr,"orough>2?\n");exit(1);}
      T2n[orough][t][b]++; if(r>0) T2s[orough][t][b]++;
      // sieve-visible success: since N ≡ 1 (mod 4C), the rough part r ≡ s^{-1}; if Omega(r)<=1 every divisor is d or d*r with d|s,
      // so success is decided by s alone: exists d|s with d ≡ -1 or d ≡ -s (mod 4C).  vis := that test (any Omega(r)).
      { uint32_t sp[MAXF]; uint8_t se[MAXF]; int ns=0; u64 sv=1;
        for(int j=0;j<nf[C];j++) if((double)fp[C][j]<=z){ sp[ns]=fp[C][j]; se[ns]=fe[C][j]; ns++; for(int e=0;e<fe[C][j];e++) sv=(u64)((u128)sv*fp[C][j]%q); }
        int v1=cnt_div(ns,sp,se,1,q); int v2=cnt_div_target(ns,sp,se,q,(q-sv)%q);
        int vis=(v1+v2)>0; if(vis && r==0){fprintf(stderr,"vis without success?\n");exit(1);}
        if(orough<=1 && (r>0)!=vis){fprintf(stderr,"vis mismatch at Omega(r)<=1\n");exit(1);}
        if(r>0){ succ_p++; if(vis) vis_p++; T3s[k]++; if(vis) T3v[k]++; } }
      totalpairs++; }
    if(!anyp) zero_p++;
    printf("P %llu %lld %lld\n",p,succ_p,vis_p);
  }
  printf("# primes %d, CMAX %d, pairs %lld, primes with no C<=CMAX success %lld, sieve bound %llu\n",nps,CMAX,totalpairs,zero_p,L);
  printf("# T1: k Cbucket n succ P(succ) mean_r\n");
  for(int k=0;k<KMAX;k++) for(int b=0;b<NB;b++) if(T1n[k][b]>0) printf("T1 %d %d %.0f %.0f %.5f %.4f\n",k,b,T1n[k][b],T1s[k][b],T1s[k][b]/T1n[k][b],T1r[k][b]/T1n[k][b]);
  printf("# T2: Omega(rough) tau(s)bucket Cbucket n succ P\n");
  for(int o=0;o<3;o++) for(int t=0;t<8;t++) for(int b=0;b<NB;b++) if(T2n[o][t][b]>0) printf("T2 %d %d %d %.0f %.0f %.5f\n",o,t,b,T2n[o][t][b],T2s[o][t][b],T2s[o][t][b]/T2n[o][t][b]);
  printf("# T3: k succ vis_succ frac_visible\n");
  for(int k=0;k<KMAX;k++) if(T3s[k]>0) printf("T3 %d %.0f %.0f %.4f\n",k,T3s[k],T3v[k],T3v[k]/T3s[k]);
  return 0; }
