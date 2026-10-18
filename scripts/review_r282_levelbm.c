/* R282 from-scratch check of SPARKS9 Prop 2.2 (witness) + share of witness levels carrying a (*) word.
   For every odd n <= NMAX: is n a square? if not: l = least odd prime with Legendre/Jacobi (n/l) = -1,
   t = least positive multiple of 4 with t*n+1 = 0 mod l; check l | tn+1, (-t/l) = -1 (Euler), t <= 4l.
   Then R_t>0 iff exists d | tn+1, d = -1 mod t (scan d = t-1, 2t-1, ... <= sqrt(N)). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef __int128 i128;
static u64 pw(u64 b,u64 e,u64 m){u64 r=1;b%=m;while(e){if(e&1)r=(i128)r*b%m;b=(i128)b*b%m;e>>=1;}return r;}
static int isprime(u64 x){if(x<2)return 0;for(u64 q=2;q*q<=x;q++)if(x%q==0)return 0;return 1;}
static int legendre(long long a,u64 p){long long r=a%(long long)p; if(r<0)r+=p; if(r==0)return 0; u64 e=pw(r,(p-1)/2,p); return e==1?1:-1;}
int main(int argc,char**argv){ u64 NMAX=atoll(argv[1]); u64 cnt=0,fail=0,maxl=0,maxratio_n=0,hit=0,sq=0; double maxr=0;
 for(u64 n=1;n<=NMAX;n+=2){ u64 r=(u64)sqrtl((long double)n); while(r*r>n)r--; while((r+1)*(r+1)<=n)r++;
  if(r*r==n){sq++;continue;} cnt++;
  u64 l=0; for(u64 q=3;;q+=2){ if(!isprime(q))continue; if(legendre((long long)(n%q),q)==-1){l=q;break;} if(q>100000){break;} }
  if(!l){fail++;printf("no l for n=%llu\n",n);continue;}
  if(l>maxl)maxl=l;
  u64 t=0; for(u64 s=4;s<=4*l;s+=4) if(((i128)s*n+1)%l==0){t=s;break;}
  if(!t||t>4*l||((i128)t*n+1)%l!=0||legendre(-(long long)t,l)!=-1){fail++;printf("fail n=%llu l=%llu t=%llu\n",n,l,t);continue;}
  u64 N=t*n+1; int ok=0; for(u64 d=t-1; d*d<=N; d+=t) if(N%d==0){ok=1;break;}
  hit+=ok; }
 printf("NMAX=%llu odd nonsquares=%llu odd squares=%llu failures=%llu max_l=%llu witness level carries (*) word: %llu (%.2f%%)\n",NMAX,cnt,sq,fail,maxl,hit,100.0*hit/cnt);
}
