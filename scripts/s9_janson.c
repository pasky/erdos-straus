// s9_janson.c (O271): empirical Janson dependency term for the (★) words at one prime.
// (★)-words: (t,u,v), 4 | t, t u v - u - v = p.  Each word uses three integers: t p + 1 (level), p + u, p + v (shifts).
// Two distinct words are "dependent" if they share one of these integers (same level, or a common shift value).
// Output per prime p == 1 (mod 4):  p  R  D  NL   (NL = number of distinct hit levels t) with D = #ordered pairs of distinct dependent words (incl. mirrors (t,v,u)).
// usage: s9_janson lo hi
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int *spf;
static int fac(ll n, ll *pr, int *ex){ int k=0; ll t=n; while(t>1){ ll q=spf[t]; pr[k]=q; ex[k]=0; while(t%q==0){t/=q;ex[k]++;} k++; } return k; }
static int gendiv(ll *pr,int *ex,int k, ll *dv){ int nd=1; dv[0]=1; for(int i=0;i<k;i++){ int cur=nd; ll pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) dv[nd++]=dv[j]*pp; } } return nd; }
static ll pr[64]; static int ex[64]; static ll dv[100000];
static ll WT[20000], WU[20000], WV[20000];
int main(int argc,char**argv){
  ll lo=atoll(argv[1]), hi=atoll(argv[2]);
  ll L=hi+(ll)sqrt((double)hi)+10; spf=calloc(L+1,sizeof(int));
  for(ll i=2;i<=L;i++) if(!spf[i]) for(ll j=i;j<=L;j+=i) if(!spf[j]) spf[j]=(int)i;
  for(ll p=(lo<5?5:lo);p<=hi;p++){
    if(spf[p]!=p || (p&3)!=1) continue;
    int R=0;
    for(ll u=1; u*u <= p+2*u+1; u++){
      int k=fac(p+u,pr,ex); int nd=gendiv(pr,ex,k,dv);
      for(int i=0;i<nd;i++){ ll e=dv[i]; if((e+1)%u) continue; ll t=(e+1)/u; if(t%4) continue; ll v=(p+u)/e; if(v<u) continue;
        WT[R]=t; WU[R]=u; WV[R]=v; R++; if(v!=u){ WT[R]=t; WU[R]=v; WV[R]=u; R++; } }
    }
    ll D=0;
    for(int i=0;i<R;i++) for(int j=0;j<R;j++){ if(i==j) continue;
      int dep = (WT[i]==WT[j]) || WU[i]==WU[j] || WU[i]==WV[j] || WV[i]==WU[j] || WV[i]==WV[j];
      if(dep) D++; }
    int NL=0; for(int i=0;i<R;i++){ int seen=0; for(int j=0;j<i;j++) if(WT[j]==WT[i]){seen=1;break;} if(!seen) NL++; }
    printf("%lld %d %lld %d\n",p,R,D,NL);
  }
  return 0;
}
