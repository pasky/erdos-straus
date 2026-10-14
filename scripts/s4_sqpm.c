/* s4_sqpm: for odd n in [3,N], is there a SIGNED word (t,u,v nonzero, tuv-u-v=n) with chi=(-A/n)=-1, A=tu-1?
   (the n-adic signed relaxation R_n).  Search t by increasing |t| (t = 1,-1,2,-2,...), early exit.
   Reports non-square failures and the record of the least |t| needed.  usage: s4_sqpm N [POS]   (POS=1: positive words only, i.e. ES-five) */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int jacobi(ll a, ll n){ a%=n; if(a<0)a+=n; int r=1; while(a){ while(!(a&1)){a>>=1; if((n&7)==3||(n&7)==5) r=-r;} ll t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) r=-r; a%=n;} return n==1?r:0; }
static int ndiv; static ll divs[20000];
static void divisors(ll m){ ll p[64]; int e[64], k=0; for(ll q=2;q*q<=m;q++) if(m%q==0){p[k]=q;e[k]=0;while(m%q==0){m/=q;e[k]++;}k++;} if(m>1){p[k]=m;e[k]=1;k++;}
  ndiv=1; divs[0]=1; for(int i=0;i<k;i++){ int c=ndiv; ll pw=1; for(int j=1;j<=e[i];j++){ pw*=p[i]; for(int s=0;s<c;s++) divs[ndiv++]=divs[s]*pw; } } }
int main(int argc,char**argv){ ll N=atoll(argv[1]); int POS=argc>2?atoi(argv[2]):0; ll rec=0, recn=0; long fails=0;
  for(ll n=3;n<=N;n+=2){ ll r=(ll)__builtin_sqrtl((long double)n); while(r*r>n)r--; while((r+1)*(r+1)<=n)r++; int sq=(r*r==n);
    int found=0; ll tf=0; if(sq) continue; /* chi=+1 identically at odd squares (Jacobi), PROVED */
    for(ll k=1;k<=2*(n+3)&&!found;k++){ ll t=POS?k:((k&1)?(k+1)/2:-(k/2)); if(POS&&t>n+3)break; ll M=t*n+1; if(M==0)continue; ll aM=M<0?-M:M; divisors(aM);
      for(int i=0;i<ndiv&&!found;i++) for(int sg=-1;sg<=1;sg+=2){ if(POS&&sg<0)continue; ll A=sg*divs[i]; ll B=M/A; if(A==-1||B==-1)continue;
        ll tt=t<0?-t:t; if(((A+1)%tt)!=0||((B+1)%tt)!=0)continue; ll u=(A+1)/t,v=(B+1)/t; if(!u||!v)continue; if(POS&&(u<0||v<0))continue;
        if(jacobi(-A,n)==-1){found=1;tf=t;break;} } }
    if(!found && !sq){ fails++; if(fails<=30) printf("FAIL n=%lld\n",n); }
    if(found){ ll at=tf<0?-tf:tf; if(at>rec){rec=at;recn=n;} } }
  printf("N=%lld non-square failures %ld; record least |t| = %lld at n=%lld\n",N,fails,rec,recn); return 0; }
