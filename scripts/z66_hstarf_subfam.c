// z66 HSTARF: for primes p=1(4) <= N, test sub-families of Type II (4a^2 d + p has a divisor = -1 mod 4ad):
//   D1: d=1 only (q | 4a^2+p, q = -1 mod 4a)      A1: a=1 only (q | p+4d, q = -1 mod 4d)
//   C1: star (q = 4ad-1 exactly)                   report primes failing each family, with min a (resp d) needed
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static char *sv; 
static long first_hit_fixed_d(u64 p,u64 d,u64 amax){ // smallest a with hit, 0 if none up to amax
  for(u64 a=1;a<=amax;a++){ u64 n=4*a*d,N=4*a*a*d+p; u64 s=(u64)sqrtl((long double)N); 
    for(u64 r=1;r<=s;r++) if(N%r==0){ if((r+1)%n==0) return a; if((N/r+1)%n==0) return a; } }
  return 0; }
static long first_hit_fixed_a(u64 p,u64 a,u64 dmax){
  for(u64 d=1;d<=dmax;d++){ u64 n=4*a*d,N=4*a*a*d+p; u64 s=(u64)sqrtl((long double)N);
    for(u64 r=1;r<=s;r++) if(N%r==0){ if((r+1)%n==0) return d; if((N/r+1)%n==0) return d; } }
  return 0; }
int main(int argc,char**argv){ u64 N=strtoull(argv[1],0,10); u64 LIM=argc>2?strtoull(argv[2],0,10):200;
  sv=calloc(N+1,1); for(u64 i=2;i<=N;i++) if(!sv[i]) for(u64 j=i*i;j<=N;j+=i) sv[j]=1;
  long np=0, fD1=0, fA1=0; u64 maxa=0,maxd=0; 
  for(u64 p=5;p<=N;p+=4){ if(sv[p]) continue; np++;
    long a=first_hit_fixed_d(p,1,LIM); long d=first_hit_fixed_a(p,1,LIM);
    if(!a){ fD1++; printf("D1_FAIL(a<=%llu) %llu\n",LIM,p);} else if((u64)a>maxa){maxa=a; printf("D1 new max a=%ld at p=%llu\n",a,p);}
    if(!d){ fA1++; printf("A1_FAIL(d<=%llu) %llu\n",LIM,p);} else if((u64)d>maxd){maxd=d; printf("A1 new max d=%ld at p=%llu\n",d,p);}
  }
  printf("done N=%llu primes=%ld D1_fail=%ld A1_fail=%ld maxa=%llu maxd=%llu\n",N,np,fD1,fA1,maxa,maxd); }
