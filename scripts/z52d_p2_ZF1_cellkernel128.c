// z52d Pass-2 ZF1 (Z2552 CPU proxy): fixed-cell adversarial ES search kernel at heights 1e18..1e36 (u128).
// Cell: n ≡ r (mod G), G = 840·11·13·17·19, r = a surviving Mordell-hard class of the static b=1 filter (see
// scripts/z52d_p2_ZF1_verifykernel.c); we take the survivor class with the FEWEST small b=1 pairs hitting it nearby
// (option) or the first survivor.  For each n = X0 + k·G in the cell: scan b=1 pairs (s,t), 4 | st, st <= K
// (st | n+s+t ⇔ a b=1 Type II solution of 4/n, B1_LINE.md Lemma 1.1), first hit = certified.  Since n mod st is
// periodic in k, we precompute per pair X0+s+t and G mod st and test (a + (k mod m)·g) mod m = 0 (u64 arithmetic
// in the loop: no u128 division per test).  Misses are counted (would need an exact fallback).
// Usage: cellkernel128 X0_decimal NCAND [K]   Build: gcc -O3 -march=native -o cellkernel128 z52d_p2_ZF1_cellkernel128.c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
typedef uint64_t u64; typedef __uint128_t u128;
static double now(){ struct timespec t; clock_gettime(CLOCK_MONOTONIC,&t); return t.tv_sec+1e-9*t.tv_nsec; }
static u128 parse(const char*s){ u128 x=0; for(;*s;s++) if(*s>='0'&&*s<='9') x=x*10+(*s-'0'); return x; }
static void pr128(u128 x){ char b[64]; int i=63; b[i]=0; do{ b[--i]='0'+(int)(x%10); x/=10; }while(x); printf("%s",b+i); }
int main(int argc,char**argv){
  u128 X=parse(argv[1]); u64 NC=strtoull(argv[2],0,10); u64 K=argc>3?strtoull(argv[3],0,10):200000;
  const u64 G=840ULL*11*13*17*19;
  u64 np=0, cap=1<<22; uint32_t *ps=malloc(4*cap), *pt=malloc(4*cap); u64 *pm=malloc(8*cap);
  for(u64 m=4;m<=K;m+=4) for(u64 s=1;s*s<=m;s++) if(m%s==0){ u64 t=m/s; if(np==cap){cap*=2; ps=realloc(ps,4*cap); pt=realloc(pt,4*cap); pm=realloc(pm,8*cap);} ps[np]=s; pt[np]=t; pm[np]=m; np++; }
  unsigned char *cov=calloc(G,1);
  for(u64 i=0;i<np;i++){ u64 m=pm[i]; if(G%m) continue; u64 r=(2*m - (ps[i]+pt[i])%m)%m; for(u64 x=r;x<G;x+=m) cov[x]=1; }
  static const int hard[6]={1,121,169,289,361,529}; u64 r0=0;
  for(u64 r=0;r<G;r++){ int h=0; for(int j=0;j<6;j++) if(r%840==(u64)hard[j]) h=1; if(h && !cov[r]){ r0=r; break; } }
  // first n >= X in the cell
  u128 X0 = X - (X % G) + r0; if(X0 < X) X0 += G;
  // per pair: a = (X0 + s + t) mod m, g = G mod m; n_k ≡ a + k·g (mod m)
  u64 *a=malloc(8*np), *gm=malloc(8*np);
  for(u64 i=0;i<np;i++){ u64 m=pm[i]; a[i]=(u64)((X0 + ps[i] + pt[i]) % m); gm[i]=G % m; }
  double t0=now(); u64 nmiss=0, tries=0;
  for(u64 k=0;k<NC;k++){ u64 i;
    for(i=0;i<np;i++){ u64 m=pm[i]; if((a[i] + (k%m)*gm[i]) % m == 0) break; }
    tries+=(i<np?i+1:np); if(i==np) nmiss++; }
  double dt=now()-t0;
  printf("X0="); pr128(X0); printf(" cell r=%llu mod G=%llu K=%llu pairs=%llu cand=%llu misses=%llu mean_tries=%.1f time=%.2fs cand_per_s=%.3e\n",
    (unsigned long long)r0,(unsigned long long)G,(unsigned long long)K,(unsigned long long)np,(unsigned long long)NC,(unsigned long long)nmiss,(double)tries/NC,dt,NC/dt);
  return 0; }
