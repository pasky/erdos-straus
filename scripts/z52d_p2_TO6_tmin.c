/* z52d pass2 TO6: minimal Type-I slice parameter t for prime p (Lemma 1.1, CONDITIONAL_ES.md §1):
 *   exists factorisation t p + 1 = m * m'' with m ≡ m'' ≡ -1 (mod t) and 4 | m.
 * Only t ≡ 3 (mod 4) can work for p ≡ 1 (mod 4) (since 4 | tp+1). We scan t in increasing order.
 * Output per prime p ≡ 1 mod 4 (p <= P): p, t_min (0 if none <= TMAX), sqrt(p), t_min/sqrt(p).
 * Lenstra's polynomial regime (Hales arXiv:2410.05030) needs S^3 > N with S = t, N = tp+1, i.e. t ≳ sqrt(p).
 * usage: tmin P TMAX
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
static int primes[100000]; static int np=0;
int main(int argc,char**argv){
  u64 P=atoll(argv[1]); u64 TMAX=atoll(argv[2]);
  int S=20000; char*isc=calloc(S+1,1);
  for(int i=2;i<=S;i++){ if(!isc[i]){ primes[np++]=i; for(long j=(long)i*i;j<=S;j+=i) isc[j]=1; } }
  char*comp=calloc(P+1,1);
  for(u64 p=2;p<=P;p++){
    if(comp[p]) continue; for(u64 j=p*p;j<=P;j+=p) comp[j]=1;
    if(p%4!=1) continue;
    u64 found=0;
    for(u64 t=3;t<=TMAX;t+=4){
      u64 N=t*p+1;
      /* factor N by trial division */
      u64 f[64]; int e[64]; int nf=0; u64 v=N;
      for(int i=0;i<np && (u64)primes[i]*primes[i]<=v;i++){ u64 q=primes[i]; if(v%q==0){int c=0; while(v%q==0){v/=q;c++;} f[nf]=q; e[nf]=c; nf++;}}
      if(v>1){ f[nf]=v; e[nf]=1; nf++; }
      /* enumerate divisors */
      u64 divs[4096]; int nd=1; divs[0]=1;
      for(int i=0;i<nf;i++){ int cur=nd; u64 pw=1; for(int k=1;k<=e[i];k++){ pw*=f[i]; for(int j=0;j<cur;j++){ divs[nd++]=divs[j]*pw; } } }
      int ok=0;
      for(int j=0;j<nd && !ok;j++){ u64 m=divs[j]; u64 m2=N/m;
        if(m%4==0 && m%t==t-1 && m2%t==t-1 && m2>=1) ok=1; }
      if(ok){ found=t; break; }
    }
    printf("%llu %llu %.3f %.5f\n",p,found,sqrt((double)p),found? found/sqrt((double)p):0.0);
  }
  return 0;
}
