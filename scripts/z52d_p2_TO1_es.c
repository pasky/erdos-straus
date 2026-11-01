// z52d pass2 TO1: enumeration of ES solutions 4/p = 1/x+1/y+1/z with x<=y<=z, p prime = 1 mod 4, p < N.
// All arithmetic that can exceed 64 bits (b = p*x/g ~ p^2/4, b^2, divisors of b^2, z) is done in __int128.
// Modes:
//   full (default): per prime: p, #solutions, E=min(4x-p) over solutions (x = min denominator),
//                   M=min max-denominator (z), #sols with all den = 0 mod 3, #sols all even with some den = 0 mod 8,
//                   2-adic pattern bitmask over sorted (v2 triple capped at 4) (code = 25a+5b+c; 125 bits in two u64),
//                   #sols with all den even.
//   E (argv[2]=="E"): stop at first x having a solution; print p, E(p) only.
// usage: z52d_p2_TO1_es N [E]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;
static int *spf; static int SPFN;
static ll gcdll(ll a, ll b){ while(b){ ll t=a%b; a=b; b=t;} return a; }
static int factor_small(ll n, int *ps, int *es){
  int k=0; while(n>1){ int q=spf[n]; int e=0; while(n%q==0){ n/=q; e++; } ps[k]=q; es[k]=e; k++; }
  return k;
}
int main(int argc, char **argv){
  int N = atoi(argv[1]); int modeE = (argc>2 && argv[2][0]=='E');
  SPFN = 2*N+10;
  spf = calloc(SPFN+1, sizeof(int));
  for(int i=2;i<=SPFN;i++) if(!spf[i]) for(int j=i;j<=SPFN;j+=i) if(!spf[j]) spf[j]=i;
  i128 *divs = malloc(sizeof(i128)*2000000);
  for(int p=5;p<N;p++){
    if(spf[p]!=p || p%4!=1) continue;
    ll cnt=0, E=-1; i128 M=-1; ll c3=0, c8=0, ce=0; unsigned __int128 pat=0;
    for(ll x=p/4+1; 4*x<=3LL*p; x++){
      if(4*x<=p) continue;
      ll a=4*x-p; ll bfull=(ll)p*x;   // b = p*x / g
      ll g=gcdll(a,bfull); a/=g;
      // exponents of b = p*x/g over primes
      int pp[64],pe[64],np=0;
      { int tp[32],te[32]; int k=factor_small(x,tp,te);
        for(int i=0;i<k;i++){ pp[np]=tp[i]; pe[np]=te[i]; np++; }
        int found=0; for(int i=0;i<np;i++) if(pp[i]==p){ pe[i]+=1; found=1; }
        if(!found){ pp[np]=p; pe[np]=1; np++; } }
      { int tp[32],te[32]; int k=factor_small(g,tp,te);
        for(int i=0;i<k;i++) for(int j=0;j<np;j++) if(pp[j]==tp[i]) pe[j]-=te[i]; }
      i128 bval=1; for(int j=0;j<np;j++) for(int e=0;e<pe[j];e++) bval*=pp[j];
      i128 B2exp_ndiv=1; for(int j=0;j<np;j++) B2exp_ndiv*=(2*pe[j]+1);
      if(B2exp_ndiv>2000000){ fprintf(stderr,"too many divisors p=%d x=%lld\n",p,x); exit(1); }
      ll ndiv=(ll)B2exp_ndiv; ll cur=1; divs[0]=1;
      for(int j=0;j<np;j++){ ll base=cur; i128 pw=1;
        for(int e=1;e<=2*pe[j];e++){ pw*=pp[j]; for(ll t=0;t<base;t++) divs[e*base+t]=divs[t]*pw; }
        cur=base*(2*pe[j]+1); }
      int any=0;
      for(ll i=0;i<ndiv;i++){
        i128 d=divs[i]; if(d>bval) continue;
        i128 zz=bval*bval/d;                  // b^2/d
        if( (d+bval)%a ) continue;
        if( (zz+bval)%a ) continue;
        i128 y=(d+bval)/a, z=(zz+bval)/a;
        if(y<(i128)x) continue;
        cnt++; any=1;
        if(E<0) E=4*x-p;
        if(M<0 || z<M) M=z;
        if(x%3==0 && y%3==0 && z%3==0) c3++;
        if(x%2==0 && y%2==0 && z%2==0 && (x%8==0 || y%8==0 || z%8==0)) c8++;
        if(x%2==0 && y%2==0 && z%2==0) ce++;
        int v[3]; i128 t[3]={x,y,z};
        for(int k=0;k<3;k++){ int c=0; i128 u=t[k]; while(u%2==0 && c<4){u/=2;c++;} v[k]=c; }
        for(int a1=0;a1<3;a1++) for(int b1=a1+1;b1<3;b1++) if(v[b1]<v[a1]){int tt=v[a1];v[a1]=v[b1];v[b1]=tt;}
        int code=v[0]*25+v[1]*5+v[2]; pat |= ((unsigned __int128)1)<<code;
        if(modeE) break;
      }
      if(modeE && any) break;
    }
    if(modeE){ printf("%d\t%lld\n", p, E); }
    else printf("%d\t%lld\t%lld\t%lld\t%lld\t%lld\t%llu\t%llu\t%lld\n", p, cnt, E, (ll)M, c3, c8, (ull)(pat>>64), (ull)pat, ce);
    fflush(stdout);
  }
  return 0;
}
