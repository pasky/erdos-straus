/* O127b §7: divisor-target covering test. For primes 5<=p<=X, count m in (0, 2p+2], m = a0 (mod q0),
   gcd(m,p)=1, with r_m | k*m+h, where r_m = least positive residue of -p^{-1} mod m (r_m in [1,m]).
   Prints the number of primes with no hit, the first 40 of them, and the minimum count among p > X/2.
   ES slice = (k,h,q0,a0) = (1,1,4,0).  Build: gcc -O2 -o /tmp/cond_divtarget scripts/cond_divtarget.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int64_t inv(int64_t a,int64_t m){int64_t r0=m,r1=a%m,s0=0,s1=1;while(r1){int64_t q=r0/r1,t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;}if(r0!=1)return -1;s0%=m;if(s0<0)s0+=m;return s0;}
static int isprime(int64_t n){if(n<2)return 0;for(int64_t d=2;d*d<=n;d++)if(n%d==0)return 0;return 1;}
int main(int c,char**v){int64_t X=atoll(v[1]),k=atoll(v[2]),h=atoll(v[3]),q0=atoll(v[4]),a0=atoll(v[5]);
 long nf=0,minc=1L<<40;int64_t minp=0;
 for(int64_t p=5;p<=X;p++){if(!isprime(p))continue;long cnt=0;
  for(int64_t m=(a0%q0==0?q0:a0%q0);m<=2*p+2;m+=q0){if(m<1||m%p==0)continue;int64_t iv=inv(p%m,m);if(iv<0)continue;
   int64_t r=(m-iv)%m;if(r==0)r=m;int64_t P=k*m+h;if(P<0)P=-P;if(P!=0&&P%r==0)cnt++;}
  if(cnt==0){nf++;if(nf<=40)printf("%lld ",(long long)p);}
  if(p>X/2&&cnt<minc){minc=cnt;minp=p;}}
 printf("\nk=%lld h=%lld q0=%lld a0=%lld: failures=%ld; min count on (X/2,X]=%ld at p=%lld\n",(long long)k,(long long)h,(long long)q0,(long long)a0,nf,minc,(long long)minp);return 0;}
