/* O211 (c): census of Type II certificates (c,d,h): 4cd | h+1, h | p + 4c^2 d, per prime p,
   split by whether h is prime.  Enumeration: t = (p+4c^2 d)/h, j = (h+1)/(4cd):
   (4cdt - p) j = c + t, so for each (c,d): t in (p/(4cd), (p+c)/(4cd-1)].
   Output per dyadic-ish block: #primes, mean N_all, mean N_prime, min N_prime (argmin), and the
   list of p with N_prime <= LOW.  Odd squares n in range: must have N_all = 0 (T1 control).
   Usage: y3_census Pmin Pmax LOW */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; if(n%2==0) return n==2; if(n%3==0) return n==3;
  for(u64 q=5;q*q<=n;q+=6) if(n%q==0||n%(q+2)==0) return 0; return 1; }
static void count(ll p, ll *na, ll *np){
  *na=0; *np=0;
  for(ll c=1; 3*c<=p+1; c++) for(ll d=1; ; d++){ ll m=4*c*d; if(m-1>p+c) break;
      ll t0=p/m+1; for(ll t=t0; t*(m-1)<=p+c; t++){ ll den=m*t-p; if(den<=0) continue;
        if((c+t)%den) continue; ll j=(c+t)/den; u64 h=(u64)m*j-1; (*na)++; if(isprime(h)) (*np)++; } }
}
int main(int argc,char**argv){
  ll P0=atoll(argv[1]), P1=atoll(argv[2]), LOW=atoll(argv[3]);
  ll cnt=0, sa=0, sp=0, mn=1LL<<60, arg=0;
  for(ll n=P0|1; n<=P1; n+=2){ ll r=0; while((r+1)*(r+1)<=n) r++;
    if(r*r==n){ ll a,b; count(n,&a,&b); if(a) printf("T1 FAIL square n=%lld N_all=%lld\n",n,a); continue; }
    if(!isprime(n)||n<5) continue; ll a,b; count(n,&a,&b); cnt++; sa+=a; sp+=b;
    if(b<mn){mn=b;arg=n;} if(b<=LOW) printf("low p=%lld N_all=%lld N_prime=%lld\n",n,a,b); }
  printf("range [%lld,%lld] primes=%lld meanN_all=%.2f meanN_prime=%.2f minN_prime=%lld at p=%lld\n",
    P0,P1,cnt,(double)sa/cnt,(double)sp/cnt,mn,arg);
  return 0; }
