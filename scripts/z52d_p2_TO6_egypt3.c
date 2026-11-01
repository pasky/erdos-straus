/* z52d pass2 TO6: exact 3-term Egyptian fractions k/n = 1/x+1/y+1/z (x<=y<=z), n given as range or primes.
 * Method: for x in [n/k, 3n/k], a = k x - n > 0, b = n x; then 1/y+1/z = a/b  <=>  (a y - b)(a z - b) = b^2.
 * Divisors d of b^2 with d = a y - b, e = b^2/d = a z - b.  Requires d ≡ -b (mod a), e ≡ -b (mod a).
 * Usage: egypt3 k N mode   mode=fail : print every n in [2,N] with no representation (ordering not needed)
 *                          mode=count: for primes n in [2,N] print n and #{x<=y<=z}
 * Memory: O(N) sieve only; 64-bit arithmetic (b^2 < 2^63 for N <= 3e4 and k>=2).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;
static int *spf;
static int N, K;
/* enumerate divisors of b^2 given factorization of b (primes ps[], exps[] of b) */
static int nf;
static u64 pr[32]; static int ex[32];
static int factor_into(u64 v){ /* v <= N*N */
  nf=0;
  while(v>1){ u64 p=spf[v]; int e=0; while(v%p==0){v/=p;e++;}
    /* merge */
    int f=0; for(int i=0;i<nf;i++) if(pr[i]==p){ex[i]+=2*e; f=1;}
    if(!f){pr[nf]=p; ex[nf]=2*e; nf++;}
  }
  return nf;
}
/* returns count of solutions with x fixed; if stop_first, returns 1 on first */
static long long cnt_for_x(u64 n, u64 x, int stop_first, u64 *dummy){
  u64 a = (u64)K*x - n; u64 b = n*x;
  if (a==0) return 0;
  /* factor b^2 : we factor n and x separately, merging */
  static u64 P[64]; static int E[64]; int m=0;
  /* factor n */
  u64 t=n; for(u64 q=2;q*q<=t;q++){ } /* placeholder (unused) */
  (void)t;
  /* use spf on n and x */
  u64 vals[2]={n,x}; int mult[2]={1,1};
  for(int w=0;w<2;w++){ u64 v=vals[w]; while(v>1){ u64 p=spf[v]; int e=0; while(v%p==0){v/=p;e++;}
      int f=0; for(int i=0;i<m;i++) if(P[i]==p){E[i]+=2*e*mult[w]; f=1;} if(!f){P[m]=p;E[m]=2*e*mult[w];m++;} } }
  /* enumerate divisors d of b^2 (128-bit: b^2 can exceed 2^64 for N >~ 7.5e4) */
  static u128 divs[1<<16]; int nd=1; divs[0]=1;
  for(int i=0;i<m;i++){
    int cur=nd; u128 pw=1;
    for(int e=1;e<=E[i];e++){ pw*=P[i];
      for(int j=0;j<cur;j++){ if(nd>=(1<<16)){fprintf(stderr,"too many divisors\n");exit(2);} divs[nd++]=divs[j]*pw; } }
  }
  long long c=0;
  u128 bb = b;
  u128 B2 = bb*bb;
  for(int j=0;j<nd;j++){
    u128 d=divs[j]; u128 e=B2/d;
    if (d>bb) continue; /* y<=z  <=>  d<=b */
    if ( (d+bb)%a==0 && (e+bb)%a==0 ){
      u128 y=(d+bb)/a, z=(e+bb)/a;
      if (y>=x && z>=y) { c++; if(stop_first) return 1; }
    }
  }
  return c;
}
int main(int argc,char**argv){
  K=atoi(argv[1]); N=atoi(argv[2]); const char*mode=argv[3];
  spf=malloc(sizeof(int)*(N+2)); for(int i=0;i<=N+1;i++) spf[i]=0;
  for(int i=2;i<=N+1;i++) if(!spf[i]) for(int j=i;j<=N+1;j+=i) if(!spf[j]) spf[j]=i;
  int stop = strcmp(mode,"fail")==0;
  for(u64 n=2;n<=(u64)N;n++){
    if(!stop){ int isp=(spf[n]==(int)n); if(!isp) continue; }
    long long total=0; int found=0;
    u64 xlo = (n + K - 1)/K; if (xlo*K==n) xlo=n/K+1; /* need K/n > 1/x  => x > n/K */
    u64 xhi = 3*n/K + 1;
    for(u64 x=xlo; x<=xhi; x++){
      if ((u64)K*x <= n) continue;
      long long c = cnt_for_x(n,x,stop,0);
      if (stop){ if(c){found=1;break;} } else total+=c;
    }
    if (stop){ if(!found) printf("%llu\n",n); }
    else printf("%llu %lld\n",n,total);
  }
  return 0;
}
