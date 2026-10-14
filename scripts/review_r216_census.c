/* R216 from-scratch Type II census (independent of scripts/y3_census.c).
 * Type II certificate for n: (c,d,h), c,d>=1, h = 4cdj-1 (j>=1), h | n + 4c^2 d.
 * Bijection used: with t = (nj + c)/h (integer), n = 4cdt - (c+t)/j, j | c+t.
 * Proof: h | n+4c^2d <=> h | nj + c (multiply by j, 4cdj = h+1); then t h = nj + c
 * <=> c + t = j(4cdt - n). Conversely any c,d,t>=1, j | c+t gives n = 4cdt-(c+t)/j > 0
 * with h = 4cdj-1 | n + 4c^2 d.
 * Enumerate all (c,d,t,j) with n <= N; n >= 4cdt - c - t so t <= (N + c)/(4cd - 1).
 * Output: per-n counts N_II (all h) and N_II^pr (h prime) for primes; odd squares.
 * usage: review_r216_census N
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 u128;
typedef uint64_t u64;
static u64 mulmod(u64 a, u64 b, u64 m){ return (u64)((u128)a*b % m); }
static u64 powmod(u64 a, u64 e, u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static int isprime64(u64 n){
  if(n<2) return 0;
  static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){
    u64 x=powmod(sp[i],d,n); if(x==1||x==n-1) continue;
    int ok=0; for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} }
    if(!ok) return 0;
  }
  return 1;
}
int main(int argc,char**argv){
  long N = atol(argv[1]);
  uint32_t *spf = calloc(N+2, sizeof(uint32_t));
  for(long i=2;i<=N+1;i++) if(!spf[i]) for(long k=i;k<=N+1;k+=i) if(!spf[k]) spf[k]=i;
  uint32_t *nall = calloc(N+1,sizeof(uint32_t)), *npr = calloc(N+1,sizeof(uint32_t));
  long divs[4096];
  for(long d=1; 4*d-1-1 <= N; d++){
    for(long c=1; 4*c*d - c - 1 <= N; c++){
      long tmax = (N + c)/(4*c*d - 1);
      for(long t=1;t<=tmax;t++){
        long s = c+t;  /* enumerate divisors j of s */
        if(s > N+1){ fprintf(stderr,"s too big %ld\n",s); return 1; }
        int nd=1; divs[0]=1; long x=s;
        while(x>1){ long q=spf[x]; int e=0; while(x%q==0){x/=q;e++;}
          int cur=nd; long pw=1; for(int k=1;k<=e;k++){ pw*=q; for(int i=0;i<cur;i++) divs[nd++]=divs[i]*pw; } }
        for(int i=0;i<nd;i++){
          long j=divs[i]; long n = 4*c*d*t - s/j;
          if(n<1 || n>N) continue;
          nall[n]++;
          int nprime = (n>=2 && spf[n]==(uint32_t)n);
          long r = (long)floor(sqrt((double)n)); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++;
          if(nprime || (r*r==n && (n&1))){
            u64 h = (u64)4*c*d*j - 1;
            if(isprime64(h)) npr[n]++;
          }
        }
      }
    }
  }
  /* report */
  long sqcount=0, sqsol=0;
  for(long r=3;r*r<=N;r+=2){ sqcount++; if(nall[r*r]) sqsol++; }
  printf("odd squares 9..N: %ld, with any Type II cert: %ld\n", sqcount, sqsol);
  printf("primes p>=5 with N_II^pr<=1:\n");
  for(long n=5;n<=N;n++) if(spf[n]==(uint32_t)n && npr[n]<=1) printf("  p=%ld N_II=%u N_II^pr=%u\n",n,nall[n],npr[n]);
  /* blocks */
  long edges[64]; int ne=0; for(long a=1024;a<=N;a*=2) edges[ne++]=a;
  for(int b=0;b+1<ne;b++){
    long lo=edges[b], hi=edges[b+1]; double sa=0,sp=0,sl2=0,sl3=0; long np=0; uint32_t mn=1u<<30; long amn=0;
    for(long n=lo;n<hi;n++) if(spf[n]==(uint32_t)n){ np++; sa+=nall[n]; sp+=npr[n]; double L=log((double)n); sl2+=L*L; sl3+=L*L*L; if(npr[n]<mn){mn=npr[n];amn=n;} }
    printf("[%ld,%ld): primes %ld mean N_II %.1f mean N_pr %.2f  N_pr/log^2 %.3f N_II/log^3 %.3f min N_pr %u at %ld\n",
      lo,hi,np,sa/np,sp/np,sp/sl2,sa/sl3,mn,amn);
  }
  if(N>=1000000){ uint32_t mn=1u<<30; long amn=0; long np=0; double sp=0, sa=0;
    for(long n=100000;n<=1000000;n++) if(spf[n]==(uint32_t)n){ np++; sp+=npr[n]; sa+=nall[n]; if(npr[n]<mn){mn=npr[n];amn=n;} }
    printf("[1e5,1e6]: primes %ld mean N_II %.2f mean N_pr %.2f min N_pr %u at %ld\n",np,sa/np,sp/np,mn,amn); }
  if(getenv("WIN")){ long lo=atol(getenv("WIN")); long np=0; double sa=0,sp=0; uint32_t mn=1u<<30;
    for(long n=lo;n<=N;n++) if(spf[n]==(uint32_t)n){ np++; sa+=nall[n]; sp+=npr[n]; if(npr[n]<mn) mn=npr[n]; }
    printf("window [%ld,%ld]: primes %ld mean N_II %.2f mean N_pr %.2f min N_pr %u\n",lo,N,np,sa/np,sp/np,mn); }
  /* small sanity dump */
  long dl = getenv("DUMP")?atol(getenv("DUMP")):60;
  for(long n=5;n<=dl;n++) if(spf[n]==(uint32_t)n || (n&1 && (long)sqrt((double)n)*(long)sqrt((double)n)==n)) printf("p=%ld N_II=%u N_pr=%u\n",n,nall[n],npr[n]);
  return 0;
}
