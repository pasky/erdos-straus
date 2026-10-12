/* bs_ident_mn.c — O145 (c): m/n = 1/x+1/y+1/z (positive integers, x<=y<=z).
 * Usage: bs_ident_mn MODE m N
 *   MODE 0: print every n<=N with NO representation (m-exceptional n), then count.
 *   MODE 1: for every prime n=p<=N, p∤m: print p, total count f, Type I count, Type II count
 *           (Type I: p divides exactly one denominator; Type II: exactly two).
 *   MODE 2: for odd s<=N with gcd(s,m)=1, n=s^2: print s, f, #Type I, #Type II where Type I (II) means
 *           n divides exactly one (two) denominators and is coprime to the others (ET's convention).
 */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef unsigned long long u64;
static ll gcdl(ll a,ll b){while(b){ll t=a%b;a=b;b=t;}return a;}
static int np; static ll P[64]; static int E[64];
static void addfac(ll n){for(ll q=2;q*q<=n;q++){if(n%q==0){int e=0;while(n%q==0){n/=q;e++;}int i;for(i=0;i<np;i++)if(P[i]==q)break;if(i==np){P[np]=q;E[np]=0;np++;}E[i]+=e;}}
  if(n>1){int i;for(i=0;i<np;i++)if(P[i]==n)break;if(i==np){P[np]=n;E[np]=0;np++;}E[i]+=1;}}
static ll D[200000]; static int nd;
static void divsq(void){ /* divisors of B^2 from P,E (E = exponent in B) */
  nd=1;D[0]=1;for(int i=0;i<np;i++){int c=nd;ll m=1;for(int k=1;k<=2*E[i];k++){m*=P[i];for(int j=0;j<c;j++)D[nd++]=D[j]*m;}}}
/* enumerate solutions; callback counts */
static ll cnt,cI,cII; static ll curn; static int mode2;
static void rec(ll x,ll y,ll z){cnt++; ll n=curn; int k=(x%n==0)+(y%n==0)+(z%n==0);
  if(mode2){ int cop=1; if(x%n&&gcdl(x,n)!=1)cop=0; if(y%n&&gcdl(y,n)!=1)cop=0; if(z%n&&gcdl(z,n)!=1)cop=0; if(!cop)return; }
  if(k==1)cI++; else if(k==2)cII++; }
static void solve(ll m,ll n,int stopfirst){
  cnt=cI=cII=0; curn=n;
  for(ll x=n/m+1;x<=3*n/m;x++){
    ll A=m*x-n,B=n*x,g=gcdl(A,B);A/=g;B/=g;
    /* need 1/y+1/z=A/B, y>=x, y<=z : (Ay-B)(Az-B)=B^2, delta=Ay-B <= B */
    np=0; addfac(n); addfac(x); /* B | n*x : get factorization of B by removing g */
    {ll gg=g; for(int i=0;i<np;i++) while(gg%P[i]==0){gg/=P[i];E[i]--;}}
    divsq();
    for(int j=0;j<nd;j++){ll d=D[j]; if(d>B)continue; if((B+d)%A)continue; ll y=(B+d)/A; if(y<x)continue;
      ll z=(B+B*(B/d))/A; /* B^2/d = B*(B/d) only if d|B; do it safely: */
      { __int128 B2=(__int128)B*B; if(B2%d)continue; __int128 zz=((__int128)B+B2/d); if(zz%A)continue; z=(ll)(zz/A);} 
      rec(x,y,z); if(stopfirst)return; }
  }
}
static int isprime(ll n){if(n<2)return 0;for(ll q=2;q*q<=n;q++)if(n%q==0)return 0;return 1;}
int main(int argc,char**argv){int mode=atoi(argv[1]);ll m=atoll(argv[2]),N=atoll(argv[3]);
  if(mode==0){ll ex=0;for(ll n=1;n<=N;n++){solve(m,n,1);if(!cnt){printf("%lld ",n);ex++;}}printf("\n# m=%lld N=%lld exceptions=%lld\n",m,N,ex);}
  if(mode==1){for(ll p=2;p<=N;p++){if(!isprime(p)||m%p==0)continue;solve(m,p,0);printf("%lld\t%lld\t%lld\t%lld\n",p,cnt,cI,cII);}}
  if(mode==2){mode2=1;for(ll s=3;s<=N;s+=2){if(gcdl(s,m)!=1)continue;solve(m,s*s,0);printf("%lld\t%lld\t%lld\t%lld\n",s,cnt,cI,cII);}}
  return 0;}
