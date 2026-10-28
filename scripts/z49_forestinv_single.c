// z49 forestinv — decide U(n) (and U_cop(n)) for individual n ≡ 1 (mod 8) by enumerating words through the smaller
// endpoint u ≤ sqrt(n+1)+1: divisors A of n+u with A ≡ −1 (mod u), v = (n+u)/A.  Trial division by sieved primes.
// Usage: ./single n1 n2 ...            → one line per n: n  U  U_cop  least V-line (coprime)  least V-line (any)
//        ./single -scan N0 N1 M R      → scan n ≡ 1 (8) in [N0,N1] with M | n and least QNR r(n) ≥ R; print failures of U_cop/U
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull;
static int *primes, np;
static void sieve(int L){ char*c=calloc(L+1,1); primes=malloc(sizeof(int)*(L/2+10)); np=0; for(int i=2;i<=L;i++){ if(!c[i]){primes[np++]=i; for(ll j=(ll)i*i;j<=L;j+=i)c[j]=1;}} free(c); }
static ll gcdl(ll a,ll b){while(b){ll t=a%b;a=b;b=t;}return a;}
static int jac(ll a, ll m){ // Jacobi (a/m), m odd > 0
  a%=m; if(a<0)a+=m; int r=1; while(a){ while(!(a&1)){a>>=1; ll t=m&7; if(t==3||t==5) r=-r;} ll t=a;a=m;m=t; if((a&3)==3&&(m&3)==3) r=-r; a%=m;} return m==1?r:0; }
static int inV(ll x){ return (x&3)==0 || (x&7)==7; }
// factor m into prime powers; returns count, writes p[],e[]
static int factor(ll m, ll*p, int*e){ int k=0; for(int i=0;i<np;i++){ ll q=primes[i]; if(q*q>m) break; if(m%q==0){ int c=0; while(m%q==0){m/=q;c++;} p[k]=q;e[k]=c;k++; } } if(m>1){p[k]=m;e[k]=1;k++;} return k; }
// decide U for n; returns bits: 1 = coprime witness, 2 = non-coprime witness. vmin_c, vmin_a = least V-line.
static int decideU(ll n, ll*vmin_c, ll*vmin_a, int early){ int res=0; *vmin_c=*vmin_a=-1;
  ll umax=(ll)sqrtl((long double)(n+1))+2;
  ll p[64]; int e[64]; ll divs[1<<16];
  for(ll u=1;u<=umax;u++){ ll m=n+u; int k=factor(m,p,e);
    int nd=1; divs[0]=1; for(int i=0;i<k;i++){ int cur=nd; ll pw=1; for(int j=1;j<=e[i];j++){ pw*=p[i]; for(int s=0;s<cur;s++) divs[nd++]=divs[s]*pw; } }
    for(int s=0;s<nd;s++){ ll A=divs[s]; if((A+1)%u) continue; ll v=m/A; if(v<1) continue;
      // word (t,u,v) with t=(A+1)/u
      int uV=inV(u), vV=inV(v); if(!(uV||vV)) continue;
      ll g=gcdl(u,v); ll line = uV? u : v; if(uV&&vV&&v<u) line=v;
      if(g==1){ res|=1; if(*vmin_c<0||line<*vmin_c)*vmin_c=line; } else res|=2;
      if(*vmin_a<0||line<*vmin_a)*vmin_a=line; }
    if(early && (res&1)) return res;
  }
  return res; }
static int leastqnr(ll n){ if((n&7)==3||(n&7)==5) return 2; for(int i=1;i<np;i++){ ll q=primes[i]; if(n%q==0) continue; if(jac(n,q)==-1) return q; } return -1; }
int main(int argc,char**argv){ sieve(4000000);
  if(argc>1 && !strcmp(argv[1],"-scan")){ ll N0=atoll(argv[2]),N1=atoll(argv[3]),M=atoll(argv[4]); int R=atoi(argv[5]); long tested=0, fc=0, fa=0;
    ll start=N0 + ((1-N0%8)+8)%8; while(start%M) start+=8;
    for(ll n=start;n<=N1;n+=8*M/gcdl(8,M)){ ll s=(ll)sqrtl((long double)n); if(s*s==n||(s+1)*(s+1)==n) continue; if(leastqnr(n)<R) continue; tested++;
      ll vc,va; int r=decideU(n,&vc,&va,1); if(!(r&1)){ r=decideU(n,&vc,&va,0); fc++; if(!r) fa++; printf("%lld %s r=%d vmin_any=%lld\n", n, r?"U_cop-fail":"U-FAIL", leastqnr(n), va); fflush(stdout);} }
    fprintf(stderr,"tested %ld (M=%lld, r>=%d, [%lld,%lld]); U_cop failures %ld; U failures %ld\n",tested,M,R,N0,N1,fc,fa); return 0; }
  for(int i=1;i<argc;i++){ ll n=atoll(argv[i]); ll vc,va; int r=decideU(n,&vc,&va,0); printf("%lld U=%d U_cop=%d least_coprime_Vline=%lld least_Vline=%lld r=%d\n", n, r!=0, (r&1)!=0, vc, va, leastqnr(n)); }
  return 0; }
