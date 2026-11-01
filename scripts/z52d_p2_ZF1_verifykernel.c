// z52d Pass-2 ZF1 (Z1789/Z1615/Z2552): a Salez/Mihnea–Dumitru-style ES verification kernel, to measure throughput
// at large heights on this CPU.  No primality testing: like Salez (arXiv:1406.6307) and Mihnea–Dumitru (arXiv:2509.00128)
// we check EVERY integer n in the residue classes that no identity covers (a composite n inherits ES from a factor,
// so this is a superset of the needed work).
//  1. Mordell: only n ≡ 1, 121, 169, 289, 361, 529 (mod 840) need work (all n ≡ 1 mod 8).
//  2. Static filter mod G = 840·11·13·17·19 (= 38 798 760): drop a class r if some b=1 pair (s,t) with st | G, 4 | st,
//     covers it: st | r + s + t  (B1_LINE.md Lemma 1.1: for n ≡ 1 (4), st | n+s+t with 4 | st ⇔ a b = 1 Type II
//     solution of 4/n).
//  3. Dynamic filter: for each surviving n, scan b=1 pairs (s,t), s<=t, 4|st, st <= K in increasing st; first hit = done.
//  4. Misses (no pair with st <= K) are counted and printed (they would go to an exact fallback; none expected often).
// Usage: verifykernel X W [K]   checks n in [X, X+W).   Output: counts, timing, candidates/s, misses.
// Build: gcc -O3 -march=native -o verifykernel z52d_p2_ZF1_verifykernel.c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <math.h>
typedef uint64_t u64; typedef __uint128_t u128;
static inline u64 mulm(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 B[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%B[i]==0) return n==B[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(B[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; } return 1; }
static int issq(u64 n){ u64 r=(u64)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r*r==n; }

static double now(){ struct timespec t; clock_gettime(CLOCK_MONOTONIC,&t); return t.tv_sec+1e-9*t.tv_nsec; }
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), W=strtoull(argv[2],0,10); u64 K=argc>3?strtoull(argv[3],0,10):200000;
  const u64 G=840ULL*11*13*17*19;
  // pairs (s,t), s<=t, 4 | st, st <= K, sorted by st
  u64 np=0, cap=1<<22; uint32_t *ps=malloc(4*cap), *pt=malloc(4*cap); u64 *pm=malloc(8*cap);
  for(u64 m=4;m<=K;m+=4) for(u64 s=1;s*s<=m;s++) if(m%s==0){ u64 t=m/s; if(np==cap){cap*=2; ps=realloc(ps,4*cap); pt=realloc(pt,4*cap); pm=realloc(pm,8*cap);} ps[np]=s; pt[np]=t; pm[np]=m; np++; }
  // static filter: survivors mod G among Mordell classes
  unsigned char *cov=calloc(G,1);
  u64 nst=0;
  for(u64 i=0;i<np;i++){ u64 m=pm[i]; if(G%m) continue; nst++; u64 r=(2*m - (ps[i]+pt[i])%m)%m; for(u64 x=r;x<G;x+=m) cov[x]=1; }
  static const int hard[6]={1,121,169,289,361,529};
  u64 nsurv=0; u64 *surv=malloc(8*(G/840*6+10));
  for(u64 r=0;r<G;r++){ int h=0; for(int j=0;j<6;j++) if(r%840==(u64)hard[j]) h=1; if(h && !cov[r]) surv[nsurv++]=r; }
  fprintf(stderr,"pairs=%llu static_pairs=%llu survivors mod G=%llu of %llu (density %.3e)\n",(unsigned long long)np,(unsigned long long)nst,(unsigned long long)nsurv,(unsigned long long)G,(double)nsurv/G);
  double t0=now(); u64 ncand=0, nmiss=0, tries=0; u64 maxm=0, nsq=0, nmissprime=0;
  u64 k0=X/G, k1=(X+W+G-1)/G;
  for(u64 k=k0;k<k1;k++){ u64 base=k*G;
    for(u64 j=0;j<nsurv;j++){ u64 n=base+surv[j]; if(n<X||n>=X+W) continue; ncand++;
      if(issq(n)){ nsq++; continue; }
      u64 i; for(i=0;i<np;i++){ if((n+ps[i]+pt[i])%pm[i]==0) break; }
      tries+=i+1; if(i==np){ nmiss++; if(isprime(n)){ nmissprime++; printf("PRIME MISS %llu\n",(unsigned long long)n);} } else if(pm[i]>maxm) maxm=pm[i]; } }
  double dt=now()-t0;
  printf("X=%llu W=%llu K=%llu candidates=%llu squares_skipped=%llu prime_misses=%llu misses=%llu mean_tries=%.1f max_hit_st=%llu time=%.2fs cand_per_s=%.3e ns_per_integer=%.4f\n",
    (unsigned long long)X,(unsigned long long)W,(unsigned long long)K,(unsigned long long)ncand,(unsigned long long)nsq,(unsigned long long)nmissprime,(unsigned long long)nmiss,(double)tries/(ncand?ncand:1),(unsigned long long)maxm,dt,ncand/dt,1e9*dt/W);
  return 0; }
