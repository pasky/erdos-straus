// z53_pz_exactV_typeII.c — exact BV-model variance of the truncated FULL Type II family (ET Prop 2.6, eqs. (2.13)-(2.22), at prime p):
//   P = (a,c,d), gcd(a,c)=1, m = 4acd-1 <= Q, event m | c p + a  (p ≡ -a c^{-1} mod m), weight 1/m (c_P = phi(m)/m).
//   Each firing P gives the Type II solution (abd, acdp, bcdp), b = (cp+a)/m, injectively (gcd(a,b) | c and gcd(a,c)=1).
//   Prints M = sum 1/m, V = E N^2 - M^2 with E N^2 = sum_{P,P'} phi(g) 1[res == res' mod g]/(m m'), V/M^2, V/log^5 Q.
// usage: exactV_typeII Q
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll; typedef unsigned long long u64;
static ll gcdl(ll a,ll b){while(b){ll t=a%b;a=b;b=t;}return a<0?-a:a;}
static ll inv(ll a,ll m){ ll g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; ll b=a1; ll q,t; ll r0=m,r1=b,s0=0,s1=1; while(r1){q=r0/r1;t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;} (void)g;(void)x;(void)x1; s0%=m; if(s0<0)s0+=m; return s0; }
int main(int argc,char**argv){ ll Q=atoll(argv[1]);
  ll *ph=malloc((Q+2)*8); for(ll i=0;i<=Q+1;i++) ph[i]=i; for(ll i=2;i<=Q+1;i++) if(ph[i]==i) for(ll j=i;j<=Q+1;j+=i) ph[j]-=ph[j]/i;
  ll n=0,cap=1<<20; ll *m=malloc(cap*8),*res=malloc(cap*8); double *w=malloc(cap*8);
  for(ll a=1;4*a-1<=Q;a++) for(ll c=1;4*a*c-1<=Q;c++){ if(gcdl(a,c)!=1) continue; for(ll d=1;4*a*c*d-1<=Q;d++){
      if(n==cap){cap*=2;m=realloc(m,cap*8);res=realloc(res,cap*8);w=realloc(w,cap*8);}
      ll mm=4*a*c*d-1; m[n]=mm; ll r=(mm - (a%mm)*inv(c,mm)%mm)%mm; res[n]=r; w[n]=1.0/mm; n++; } }
  double M=0; for(ll i=0;i<n;i++) M+=w[i];
  double E2=0; for(ll i=0;i<n;i++){ double acc=0; for(ll j=0;j<n;j++){ ll g=gcdl(m[i],m[j]);
      if(g==1) acc+=w[j]; else if(res[i]%g==res[j]%g) acc+=w[j]*(double)ph[g]; } E2+=w[i]*acc; }
  double L=log((double)Q);
  printf("Q=%lld logQ=%.4f P=%lld M=%.6f M/logQ^3=%.5f V=%.6f V/M^2=%.6f V/logQ^5=%.6f V/logQ^4=%.6f\n",Q,L,n,M,M/(L*L*L),E2-M*M,(E2-M*M)/(M*M),(E2-M*M)/pow(L,5),(E2-M*M)/pow(L,4));
  return 0; }
