// z52d Pass 2 TO7 common engine: e-slice a=1 tests for ES at primes p ≡ 1 (mod 4).
// Type I  (k ≡ 3 mod 4, M = (k p + 1)/4):  exists divisor b of M with b ≡ -1 (mod k)   [CONDITIONAL_ES.md Lemma 1.2, a=1]
// Type II (k ≡ 3 mod 4, M = (p + k)/4):    exists divisor b of M with b ≡ -1 (mod k)
// Output per prime: p, p mod 840, hard flag, minI, minII (smallest successful k, 0 if none <= T),
//                   nI, nII (number of successful k <= T), ndivI(k=3) etc.
// usage: z52d_p2_TO7_slices X T > out.tsv     (p ≤ X, k ≤ T)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static uint32_t *spf;
static long LIM;
static void sieve(long n){
  spf = calloc(n+1, sizeof(uint32_t)); LIM=n;
  for (long i=2;i<=n;i++) if(!spf[i]){ for(long j=i;j<=n;j+=i) if(!spf[j]) spf[j]=i; }
}
// enumerate divisors of M, test b % k == k-1
static int has_div_cong(long M, long k){
  if (M<=0) return 0;
  long pr[64]; int ex[64]; int np=0; long m=M;
  while(m>1){ long q=spf[m]; if(q==0) q=m; int e=0; while(m%q==0){m/=q;e++;} pr[np]=q; ex[np]=e; np++; }
  // iterative divisor generation
  static long divs[1<<16]; int nd=1; divs[0]=1;
  for(int i=0;i<np;i++){
    int cur=nd;
    long pw=1;
    for(int e=1;e<=ex[i];e++){
      pw*=pr[i];
      for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw;
    }
  }
  for(int j=0;j<nd;j++) if(divs[j]%k==k-1) return 1;
  return 0;
}
static int isprime(long n){ if(n<2) return 0; for(long d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
int main(int argc, char**argv){
  long X = atol(argv[1]); int T = atoi(argv[2]);
  sieve((long)X*T/4 + X + 16);
  static const int hardset[]={1,121,169,289,361,529};
  printf("p\tp840\thard\tminI\tminII\tnI\tnII\n");
  for (long p=5;p<=X;p+=4){
    if(!spf[p]==0 && spf[p]!=p) continue; // not prime
    if(spf[p]!=(uint32_t)p) continue;
    int hard=0; int r=p%840; for(int i=0;i<6;i++) if(r==hardset[i]) hard=1;
    long minI=0,minII=0; int nI=0,nII=0;
    for(long k=3;k<=T;k+=4){
      long MI=(k*p+1)/4, MII=(p+k)/4;
      if(has_div_cong(MI,k)){ nI++; if(!minI) minI=k; }
      if(has_div_cong(MII,k)){ nII++; if(!minII) minII=k; }
    }
    printf("%ld\t%d\t%d\t%ld\t%ld\t%d\t%d\n",p,r,hard,minI,minII,nI,nII);
  }
  return 0;
}
