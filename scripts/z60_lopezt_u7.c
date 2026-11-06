// z60 LOPEZT: (U7) form. S(n) <=> exists a>=1: N_a has a divisor = -1 (mod M_a), where
//  a=0(4): N=n+a, M=a; a=1(4): N=(n+a)/2, M=4a; a=2(4): N=n+a, M=4a; a=3(4): N=(n+a)/4, M=a.
// prints n = 1 (mod 4) <= NMAX (onlyprime flag) with S false. Must agree with z60_lopezt_u5.c.
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; for(u64 d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
static int hasdiv(u64 N, u64 M){ for(u64 d=M-1; d<=N; d+=M) if(N%d==0) return 1; return 0; }
int main(int argc,char**argv){ u64 NMAX=atoll(argv[1]); int onlyprime=atoi(argv[2]);
  for(u64 n=5;n<=NMAX;n+=4){ if(onlyprime&&!isprime(n)) continue; int hit=0;
    for(u64 a=1;a<=n+1&&!hit;a++){ u64 N,M; switch(a%4){case 0:N=n+a;M=a;break;case 1:N=(n+a)/2;M=4*a;break;case 2:N=n+a;M=4*a;break;default:N=(n+a)/4;M=a;}
      if(M>1&&hasdiv(N,M)) hit=1; }
    if(!hit) printf("%llu %s\n",n,isprime(n)?"P":"C"); } }
