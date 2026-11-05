// z58 DISPROOF §3: least odd quadratic non-residue sd(p) over primes p = 1 (4) <= 9e6: max, share > 23 (all, Mordell). gcc -O2
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll pw(ll b, ll e, ll m){ll r=1;b%=m;while(e){if(e&1)r=r*b%m;b=b*b%m;e>>=1;}return r;}
int main(){ ll N=9000000; char*c=calloc(N+1,1); for(ll i=2;i*i<=N;i++) if(!c[i]) for(ll j=i*i;j<=N;j+=i)c[j]=1;
 int ps[200],np=0; for(int q=3;np<200;q+=2){int pr=1;for(int t=3;t*t<=q;t+=2)if(q%t==0)pr=0;if(pr)ps[np++]=q;}
 int mx=0; ll arg=0; long cnt23=0,tot=0, cntM23=0, totM=0;
 for(ll p=5;p<=N;p+=4){ if(c[p])continue; int s=0; for(int k=0;k<np;k++){int l=ps[k]; if(p%l && pw(p%l,(l-1)/2,l)==l-1){s=l;break;}} tot++; if(s>23)cnt23++; if(s>mx){mx=s;arg=p;}
   int m=p%840; if(m==1||m==121||m==169||m==289||m==361||m==529){totM++; if(s>23)cntM23++;} }
 printf("max sd %d at %lld; share sd>23: %ld/%ld; in M: %ld/%ld\n",mx,arg,cnt23,tot,cntM23,totM); }
