/* O234 goal 4: PM-SQ_± (CAP_GROWING §3, Lemma 3.1) in C.  For n ≡ 1 (mod 8), n ≤ N: least |u| (u ≠ 0, −n) such that
   n + u has an odd prime factor l with |u| | l+1 or |u| | l−1, and Legendre (−u / l) = −1.  (Then a word with
   A = ±l and χ = −1 exists.)  Reports histogram of least |u|, max, exceptions (non-squares with none up to UMAX),
   and the odd-square control (squares must never fire, T1).  usage: z10_sqpm N UMAX */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int *spf;
static int legendre(ll a, ll p){ a%=p; if(a<0)a+=p; if(a==0)return 0; ll r=1,b=a,e=(p-1)/2;
  while(e){ if(e&1) r=(__int128)r*b%p; b=(__int128)b*b%p; e>>=1;} return r==1?1:-1; }
int fires(ll n, ll u){ ll m=n+u; if(m<=0) m=-m; if(m==0) return 0; ll au=u<0?-u:u;
  while(m>1){ ll l=spf[m]; while(m%l==0) m/=l; if(l==2) continue;
    if(((l+1)%au==0 || (l-1)%au==0) && legendre(-u,l)==-1) return 1; } return 0; }
int main(int argc,char**argv){ ll N=atoll(argv[1]); int UMAX=atoi(argv[2]); ll M=N+UMAX+2;
  spf=malloc(sizeof(int)*(M+1)); for(ll i=0;i<=M;i++) spf[i]=0;
  for(ll i=2;i<=M;i++) if(!spf[i]) for(ll j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i;
  ll hist[64]={0}; ll exc=0, sqfired=0, nsq=0, cnt=0; int maxu=0; ll argmax=0;
  for(ll n=9;n<=N;n+=8){ ll r=(ll)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++;
    int issq=(r*r==n); int best=0;
    for(int a=1;a<=UMAX && !best;a++){ if(fires(n,a)) best=a; else if(a!=n && fires(n,-a)) best=a; }
    if(issq){ nsq++; if(best) sqfired++; continue; }
    cnt++; if(!best){ exc++; if(exc<20) printf("EXCEPTION n=%lld\n",n); continue; }
    if(best<64) hist[best]++; if(best>maxu){maxu=best;argmax=n;} }
  printf("N=%lld UMAX=%d: %lld non-squares n≡1(8); exceptions %lld; max least|u| = %d (n=%lld)\n",N,UMAX,cnt,exc,maxu,argmax);
  printf("odd squares: %lld, fired (must be 0): %lld\nhist least|u|:",nsq,sqfired);
  for(int i=1;i<64;i++) if(hist[i]) printf(" %d:%lld",i,hist[i]); printf("\n"); return 0; }
