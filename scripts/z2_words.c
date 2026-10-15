// z2_words.c (O225): enumerate all five-slice words (t,u,v), u<=v, tuv-u-v=n, for odd n in [lo,hi].
// chi(w) = Jacobi (A/n), A = tu-1 (for prime n this is the Legendre symbol); cross-checked against DK Thm 4.5
// (chi=-1 iff 4 | t,u,v,A or A*) for n = 1 mod 4.
// mode 1: test Prop 1.2 (u-side T1): if n+u (resp. n+v) is a sum of two coprime squares, every word with that
//         u (resp. v) has chi=+1, and for even u there are no words at all.
// usage: z2_words MODE LO HI [squares]   (squares: n runs over odd squares in [LO,HI] instead of primes 1 mod 4)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static int *spf; static ll SMAX;
static void sieve(ll N){ spf=calloc(N+1,sizeof(int)); for(ll i=2;i<=N;i++) if(!spf[i]) for(ll j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i; }
static int jacobi(ll a, ll n){ int s=1; a%=n; if(a<0)a+=n; while(a){ while(!(a&1)){ a>>=1; ll r=n&7; if(r==3||r==5) s=-s; } ll t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) s=-s; a%=n; } return n==1?s:0; }
static int sos_coprime(ll N){ // N>1 sum of two coprime squares <=> 4 !| N and no prime = 3 mod 4
  if(N%4==0) return 0; while(N%2==0) N/=2; while(N>1){ int r=spf[N]; if(r%4==3) return 0; while(N%r==0) N/=r; } return 1; }
static int isprime(ll n){ return n>1 && spf[n]==n; }
static ll divs[20000]; static int nd;
static void divisors(ll N){ int pr[40],ex[40],k=0; while(N>1){ int r=spf[N],e=0; while(N%r==0){N/=r;e++;} pr[k]=r;ex[k]=e;k++; }
  nd=1; divs[0]=1; for(int i=0;i<k;i++){ int cur=nd; ll pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } } }
int main(int argc,char**argv){
  int mode=atoi(argv[1]); ll lo=atoll(argv[2]), hi=atoll(argv[3]); int sq=argc>4;
  SMAX=2*hi+4*(ll)__builtin_sqrt((double)hi)+100; sieve(SMAX);
  ll nprim=0,nw=0,bad45=0,flagged=0,flagneg=0,evenflag=0;
  for(ll n=lo;n<=hi;n++){
    if(sq){ ll r=(ll)__builtin_sqrt((double)n); while(r*r<n)r++; while(r*r>n)r--; if(r*r!=n||!(n&1)) continue; }
    else if(!(n%4==1 && isprime(n))) continue;
    nprim++;
    for(ll u=1;(u-2)*u<=n;u++){
      ll N=n+u; divisors(N);
      int fu=sos_coprime(N);
      for(int i=0;i<nd;i++){ ll v=divs[i]; if(v<u) continue; if((N+v)%(u*v)) continue;
        ll t=(N+v)/(u*v), A=t*u-1, As=t*v-1; nw++;
        int ch=jacobi(A,n);
        int dk = (t%4==0||u%4==0||v%4==0||A%4==0||As%4==0) ? -1 : 1;
        if(ch!=0 && ch!=dk) bad45++;
        int fv=sos_coprime(n+v);
        if(fu||fv){ flagged++; if(ch==-1) flagneg++; if((fu&&u%2==0)||(fv&&v%2==0)) evenflag++; }
      }
    }
  }
  printf("n-count %lld words %lld DKmismatch %lld | u-side-T1 flagged words %lld, chi=-1 among them %lld, flagged with even u/v %lld\n",
         nprim,nw,bad45,flagged,flagneg,evenflag);
  return 0;
}
