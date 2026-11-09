// z69 IDEAA test T2: "two-small" search cost K(p) of an ES solution.
// K(p) := min{ a*b : a<=b, exists e | a+b with  4ab | p+e (Type II)  or  4ab | p*e+1 (Type I) }.
// Every such (a,b,e) gives an ES decomposition of 4/p (ET parametrisation; see memo §3.2):
//   II: 4/p = 1/(abd) + 1/(p a c d) + 1/(p b c d),  4abd = p+e, a+b = e c
//   I : 4/p = 1/(p a b d) + 1/(a c d) + 1/(b c d),  4abd = p e+1, a+b = e c
// (no coprimality needed for the identity).  K(p) is the least class modulus/4 at which p is "caught".
// Usage: kcost X [res mod] [Qmax]   -- all primes p <= X with p == res (mod mod); default 1 mod 24.
// Output: survival table S(Q) = #{p : K(p) > Q} by decade of p; record setters; final unsolved.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
typedef uint64_t u64; typedef uint32_t u32;

static u64 mulmod(u64 a,u64 b,u64 m){return (unsigned __int128)a*b%m;}

int main(int argc,char**argv){
  u64 X = argc>1? strtoull(argv[1],0,10):100000000ULL;
  u32 res = argc>2? atoi(argv[2]):1, mod = argc>3? atoi(argv[3]):24;
  u32 Qmax = argc>4? atoi(argv[4]):2000000;
  int typeMask = argc>5? atoi(argv[5]):3; // 1 = Type II only, 2 = Type I only, 3 = both
  // sieve primes in class res mod mod up to X (segment over k: p = res + mod*k)
  u32 sq = (u32)sqrt((double)X)+2;
  char *small = calloc(sq+1,1); u32 *pr = malloc(sizeof(u32)*(sq/2+10)); u32 np=0;
  for(u32 i=2;i<=sq;i++){ if(!small[i]){pr[np++]=i; for(u64 j=(u64)i*i;j<=sq;j+=i) small[j]=1;} }
  u64 nk = (X-res)/mod+1; char *comp = calloc(nk,1);
  for(u32 i=0;i<np;i++){ u32 q=pr[i]; if(mod%q==0) continue;
    // solve res + mod*k == 0 mod q
    u64 inv=1; { // inverse of mod mod q
      long long a=mod%q,b=q,x0=1,x1=0; while(b){long long t=a/b; long long r=a-t*b; a=b;b=r; long long y=x0-t*x1; x0=x1;x1=y;} inv=((x0%(long long)q)+q)%q; }
    u64 k0 = mulmod((q - res%q)%q, inv, q);
    for(u64 k=k0;k<nk;k+=q){ u64 p=res+(u64)mod*k; if(p!=q) comp[k]=1; }
  }
  u64 cap=1<<20, n=0; u64 *P=malloc(cap*sizeof(u64));
  for(u64 k=0;k<nk;k++){ if(!comp[k]){ u64 p=res+(u64)mod*k; if(p<5) continue; if(n==cap){cap*=2;P=realloc(P,cap*sizeof(u64));} P[n++]=p; } }
  free(comp); free(small);
  fprintf(stderr,"primes: %llu\n",(unsigned long long)n);
  // decades
  int ND=0; u64 dlo[32]; { u64 t=1000; while(t<X){dlo[ND++]=t; t*=10;} dlo[ND]=X+1; }
  u64 N0=n; u64 *U=P; u64 nu=n; // unsolved list (in place compaction)
  char *good = malloc((size_t)4*Qmax+8);
  u64 rec=0; // record K so far among solved (the max is the last solved)
  // thresholds at which to print survival
  printf("# X=%llu class %u mod %u  primes=%llu typeMask=%d\n",(unsigned long long)X,res,mod,(unsigned long long)N0,typeMask);
  printf("# columns: Q  S(Q)=#{p: K(p)>Q}  then per decade [10^3..): counts\n");
  u32 nextprint=1;
  for(u32 m=1;m<=Qmax && nu>0;m++){
    u32 M=4*m; memset(good,0,M);
    int any=0;
    for(u32 a=1;(u64)a*a<=m;a++){ if(m%a) continue; u32 b=m/a; u32 s=a+b;
      for(u32 e=1;e<=s;e++){ if(s%e) continue; if((e&3)!=3) continue;
        // Type II: p == -e mod 4m
        if(typeMask&1){ u32 r=(M - e%M)%M; good[r]=1; any=1; }
        // Type I: p*e == -1 mod 4m  -> need gcd(e,4m)=1
        if(typeMask&2){ long long aa=e%M,bb=M,x0=1,x1=0; while(bb){long long t=aa/bb; long long r=aa-t*bb; aa=bb;bb=r; long long y=x0-t*x1; x0=x1;x1=y;}
          if(aa==1){ long long inv=((x0%(long long)M)+M)%M; u32 r=(u32)((M-inv)%M); good[r]=1; any=1; } }
      }
    }
    if(any){
      u64 w=0;
      for(u64 i=0;i<nu;i++){ u64 p=U[i];
        // positivity: Type II needs p+e >= 4ab d with d>=1: p+e>=4m, true if p >= 4m; if p<4m we simply skip (leave unsolved)
        if(p>=M && good[p%M]){ if(m>rec){rec=m; printf("REC K=%u p=%llu\n",m,(unsigned long long)p);} }
        else U[w++]=p; }
      nu=w;
    }
    if(m==nextprint){
      printf("S %u %llu",m,(unsigned long long)nu);
      // per-decade counts of unsolved
      u64 c[32]; memset(c,0,sizeof c);
      for(u64 i=0;i<nu;i++){ int d=0; while(d<ND-1 && U[i]>=dlo[d+1]) d++; c[d]++; }
      for(int d=0;d<ND;d++) printf(" %llu",(unsigned long long)c[d]);
      printf("\n"); fflush(stdout);
      nextprint = nextprint<16? nextprint+1 : (u32)(nextprint*1.25)+1;
    }
  }
  printf("# final unsolved (K > Qmax or p<4m): %llu\n",(unsigned long long)nu);
  for(u64 i=0;i<nu && i<200;i++) printf("UNS %llu\n",(unsigned long long)U[i]);
  return 0;
}
