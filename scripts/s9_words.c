// s9_words.c (O271): per-prime word census for W(p) = {(t,u,v) >= 1 : t u v - u - v = p}.
// For each prime p in [lo,hi] (optionally only p == 1 mod 4) outputs
//   p  Wtot  A=#{4|t}  B=#{4|u or 4|v}  U=#{some coord == 0 mod 4}  A1=#{4|t, u=1}  Wm=#{sigma(w) = -1}
// Enumeration: u <= v (mirror counted), u <= sqrt(p)+2, divisors e = t u - 1 of p + u with e == -1 (mod u), v = (p+u)/e >= u.
// A counts ordered (★)-words = R(p) of SINGLE_P_COUNT (pairs (u,B) ordered).  usage: s9_words lo hi mode [K=4]   mode 0 all primes, 1 primes == 1 (4), 2 odd squares
// K = numerator k: "coordinate == 0 (mod K)" (the k/p two-line union: c = 1 line k abd = p + a + b, b = 1 line).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int *spf; static ll LIM;
static int fac(ll n, ll *pr, int *ex){ int k=0; ll t=n; while(t>1){ ll q=spf[t]; pr[k]=q; ex[k]=0; while(t%q==0){t/=q;ex[k]++;} k++; } return k; }
static int gendiv(ll *pr,int *ex,int k, ll *dv){ int nd=1; dv[0]=1; for(int i=0;i<k;i++){ int cur=nd; ll pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) dv[nd++]=dv[j]*pp; } } return nd; }
static int jac(ll a, ll m){ a%=m; if(a<0)a+=m; int t=1; while(a){ while(!(a&1)){a>>=1; ll r=m&7; if(r==3||r==5)t=-t;} ll x=a;a=m;m=x; if((a&3)==3&&(m&3)==3)t=-t; a%=m;} return m==1?t:0; }
static ll pr[64]; static int ex[64]; static ll dv[100000];
int main(int argc,char**argv){
  ll lo=atoll(argv[1]), hi=atoll(argv[2]); int m4=atoi(argv[3]); ll K = argc>4 ? atoll(argv[4]) : 4;
  ll L=hi+(ll)sqrt((double)hi)+10; LIM=L; spf=calloc(L+1,sizeof(int));
  for(ll i=2;i<=L;i++) if(!spf[i]) for(ll j=i;j<=L;j+=i) if(!spf[j]) spf[j]=(int)i;
  for(ll p=(lo<5?5:lo);p<=hi;p++){
    if(m4==2){ ll r=(ll)sqrtl((long double)p); while(r*r>p) r--; while((r+1)*(r+1)<=p) r++; if(r*r!=p || !(p&1)) continue; }   // mode 2: odd squares (T1 control)
    else { if(spf[p]!=p) continue; if(m4 && (p&3)!=1) continue; }
    ll W=0,A=0,B=0,U=0,A1=0,Wm=0;
    for(ll u=1; u*u <= p+2*u+1; u++){
      int k=fac(p+u,pr,ex); int nd=gendiv(pr,ex,k,dv);
      for(int i=0;i<nd;i++){ ll e=dv[i]; if((e+1)%u) continue; ll t=(e+1)/u; if(t<1) continue; ll v=(p+u)/e; if(v<u) continue;
        int mult = (v==u)?1:2;            // (t,u,v) and (t,v,u)
        W+=mult; if(jac(e,p)==-1) Wm+=mult;   // sigma(w) = ((tu-1)/n), the DEDEKIND Thm 4.5 sign
        int a=(t%K==0), b=(u%K==0||v%K==0);
        if(a) A+=mult; if(b) B+=mult; if(a||b) U+=mult; if(a && u==1) A1+=mult; }
    }
    printf("%lld %lld %lld %lld %lld %lld %lld\n",p,W,A,B,U,A1,Wm);
  }
  return 0;
}
