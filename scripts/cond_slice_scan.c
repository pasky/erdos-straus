/* O127b: S(p) = #{(c,f,g): cfg-c-f=p, fg=1 mod 4} for Mordell-hard primes p (p square mod 840)
   in [lo,hi], restricted to p = r (mod k) for job splitting. Dual form: S(p) = sum over m=0 mod 4,
   m <= 2p+2, gcd(m,p)=1 of [r_m | m+1] + [r_m == 1], r_m = least positive residue of -p^{-1} mod m.
   Output: p S(p) gmin   (gmin = least g with a solution).
   Build: gcc -O2 -o /tmp/cond_slice_scan scripts/cond_slice_scan.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int64_t inv(int64_t a, int64_t m){ int64_t g=m,x=0,x1=1,a1=a%m; int64_t b=a1;
  /* extended Euclid on (b,m) */ int64_t r0=m,r1=b,s0=0,s1=1; while(r1){int64_t q=r0/r1,t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;}
  (void)g;(void)x;(void)x1; if(r0!=1) return -1; s0%=m; if(s0<0) s0+=m; return s0; }
static int isprime(int64_t n){ if(n<2) return 0; for(int64_t d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
int main(int argc,char**argv){ int64_t lo=atoll(argv[1]),hi=atoll(argv[2]),k=atoll(argv[3]),r=atoll(argv[4]);
  char sq[840]={0}; for(int x=0;x<840;x++) sq[(x*x)%840]=1;
  for(int64_t p=lo;p<=hi;p++){ if(p%k!=r) continue; if(!sq[p%840]) continue; if(!isprime(p)) continue;
    long S=0; int64_t gmin=-1;
    for(int64_t m=4;m<=2*p+2;m+=4){ if(m%p==0) continue; int64_t iv=inv(p%m,m); if(iv<0) continue;
      int64_t rm=(m-iv)%m; if(rm==0) rm=m; 
      if((m+1)%rm==0){ S++; if(gmin<0||rm<gmin) gmin=rm; }
      if(rm==1){ S++; } }
    printf("%lld %ld %lld\n",(long long)p,S,(long long)gmin); fflush(stdout); }
  return 0; }
