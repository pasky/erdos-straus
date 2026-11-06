// z60 LOPEZT: least witness modulus g*(p) for primes p = 1 (mod 24), p <= N, in the (U5) form:
//  g*(p) = min { g = 3 (mod 4) : (-p mod g) | (g+1)/4  or  (-p * 4^{-1} mod g) | (g+1)/4 }.
// Prints record-breakers "p g* branch" and a histogram summary.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef long long ll;
static ll inv(ll a, ll m){ ll r0=m, r1=a%m, s0=0, s1=1; while(r1){ ll q=r0/r1, t=r0-q*r1; r0=r1; r1=t; t=s0-q*s1; s0=s1; s1=t; } if(r0!=1) return -1; return ((s0%m)+m)%m; }
int main(int argc,char**argv){
  u64 N=atoll(argv[1]);
  unsigned char*comp=calloc(N+1,1);
  for(u64 i=2;i*i<=N;i++) if(!comp[i]) for(u64 j=i*i;j<=N;j+=i) comp[j]=1;
  u64 rec=0; static u64 hist[1<<16]; u64 cnt=0;
  for(u64 p=25;p<=N;p+=24){ if(comp[p]) continue; cnt++;
    u64 g; int br=0;
    for(g=3;;g+=4){ if(p%g==0) continue; u64 q=(g+1)/4; u64 r=g-p%g; if(q%r==0){br=1;break;}
      ll i4=inv(4,g); u64 r2=(u64)(( (unsigned __int128)(p%g)*(u64)i4)%g); r2=g-r2; if(r2<g && q%r2==0){br=2;break;} }
    if(g<(1<<16)) hist[g]++;
    if(g>rec){rec=g; printf("record p=%llu g*=%llu branch=%s\n",p,g,br==1?"BN(p)":"B4(p^-1)"); fflush(stdout);}
  }
  printf("primes=1(24) up to %llu: %llu\n",N,cnt);
  u64 acc=0; for(int g=3;g<(1<<16);g+=4){ if(hist[g]){acc+=hist[g]; printf("g*=%d: %llu (cum %.6f)\n",g,hist[g],(double)acc/cnt);} if(acc==cnt) break; }
}
