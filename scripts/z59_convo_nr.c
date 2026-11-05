// For primes p = 1 mod 24 in [lo,hi]: least prime NR q of p; minimal ab (over solutions with q | ab) and
// minimal ab over all solutions. Solution: (a,b), rho = (-p mod 4ab) divides a+b.
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; for(u64 i=2;i*i<=n;i++) if(n%i==0) return 0; return 1;}
static int legendre(u64 a,u64 q){ u64 r=1,b=a%q,e=(q-1)/2; while(e){ if(e&1) r=r*b%q; b=b*b%q; e>>=1;} return r==1?1:-1;}
int main(int argc,char**argv){
  u64 lo=atoll(argv[1]),hi=atoll(argv[2]); u64 B=atoll(argv[3]);
  for(u64 p=lo;p<=hi;p++){ if(p%24!=1||!isprime(p)) continue;
    u64 q=5; while(!(isprime(q)&&legendre(p,q)==-1)) q++;
    u64 best=0,bestq=0,ba=0,bb=0,qa=0,qb=0;
    for(u64 n=1;n<=B;n++){ // n = ab
      for(u64 a=1;a*a<=n;a++){ if(n%a) continue; u64 b=n/a; u64 m=4*n; u64 rho=(m - p%m)%m; if(rho==0) continue;
        if((a+b)%rho==0){ if(!best){best=n;ba=a;bb=b;} if(!bestq && n%q==0){bestq=n;qa=a;qb=b;} }
      }
      if(best&&bestq) break;
    }
    printf("%llu q=%llu min_ab=%llu (%llu,%llu) min_ab_qdiv=%llu (%llu,%llu)\n",p,q,best,ba,bb,bestq,qa,qb);
  }
}
