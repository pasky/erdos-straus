// Z2603: Liouville sign patterns on consecutive Type II slices N_e = (p+e)/4, e = 3,7,11,... (N_{e+4} = N_e + 1)
// vs ES hardness R(p) = #{(u,B,C): 4uBC - u - B = p} (FRONTIER §2.1, trial form).
// usage: z p0 p1  -> lines "p R pattern8" where bit i of pattern8 = [lambda(N_3 + i) = -1], i = 0..7
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
int main(int argc,char**argv){
  ll p0=atoll(argv[1]), p1=atoll(argv[2]);
  ll M=p1/4+16; signed char *lam=malloc(M+1); int *spf=calloc(M+1,sizeof(int));
  for(ll i=2;i<=M;i++) if(!spf[i]) for(ll j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i;
  lam[1]=1; for(ll i=2;i<=M;i++) lam[i]=-lam[i/spf[i]];
  // primality of p by sieve up to p1
  char *comp=calloc(p1+1,1); for(ll i=2;i*i<=p1;i++) if(!comp[i]) for(ll j=i*i;j<=p1;j+=i) comp[j]=1;
  for(ll p=p0;p<=p1;p++){
    if(p%4!=1||comp[p]||p<5) continue;
    ll R=0;
    for(ll u=1; 4*u-1<=p+u; u++) for(ll m=4*u-1; m<=p+u; m+=4*u) if((p+u)%m==0) R++;
    ll N=(p+3)/4; int pat=0; for(int i=0;i<8;i++) if(lam[N+i]<0) pat|=1<<i;
    printf("%lld %lld %d\n",p,R,pat);
  }
  return 0;
}
