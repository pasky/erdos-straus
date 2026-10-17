// R267 from-scratch check of NONCONG_LIFTS Thm 2.6.
// For k, odd prime l (any, also l | k reported separately), slices a<=b<=B, c | a+b, e=(a+b)/c:
// H = k*a*b; x = point "2 at l, 1 elsewhere" reduced mod H: x == 2 mod l^{v_l(H)}, x == 1 mod H/l^v.
// Type II hit: H | x+e ; Type I hit: H | x*e+1.  We test via the CRT components (no big x needed):
//   II: e == -1 mod H',  e == -2 mod l^v ;  I: e == -1 mod H', 2e == -1 mod l^v.
// Independent second test: build x by CRT explicitly with __int128 and test divisibility directly.
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
static ll egcd(ll a, ll b, ll *x, ll *y){ if(!b){*x=1;*y=0;return a;} ll x1,y1; ll g=egcd(b,a%b,&x1,&y1); *x=y1; *y=x1-(a/b)*y1; return g; }
static ll inv(ll a, ll m){ ll x,y; egcd(((a%m)+m)%m,m,&x,&y); x%=m; if(x<0)x+=m; return x; }
int main(int argc,char**argv){
  int B=atoi(argv[1]); int kmin=atoi(argv[2]), kmax=atoi(argv[3]); int lmax=atoi(argv[4]);
  int primes[64],np=0; for(int l=3;l<lmax;l+=2){int ok=1;for(int d=3;d*d<=l;d+=2)if(l%d==0)ok=0; if(ok)primes[np++]=l;}
  ll mism=0;
  for(int k=kmin;k<=kmax;k++) for(int pi=0;pi<np;pi++){ int l=primes[pi];
    long hits=0;
    for(ll a=1;a<=B;a++) for(ll b=a;b<=B;b++){
      ll H=(ll)k*a*b; ll Lv=1; ll Hp=H; while(Hp%l==0){Hp/=l;Lv*=l;}
      // explicit CRT x mod H
      ll x; if(Lv==1) x=1%H; else { // x = 1 + Hp*t, 1+Hp*t == 2 mod Lv -> t == inv(Hp) mod Lv
        ll t=inv(Hp%Lv,Lv); x=(ll)((1+(i128)Hp*t)%H); }
      ll s=a+b;
      for(ll c=1;c<=s;c++){ if(s%c) continue; ll e=s/c;
        int II = ((e+1)%Hp==0) && ((e+2)%Lv==0);
        int I  = ((e+1)%Hp==0) && ((2*e+1)%Lv==0);
        int II2 = ((x+e)%H==0); int I2 = (((i128)x*e+1)%H==0);
        if(II!=II2||I!=I2) mism++;
        if(II||I){ hits++; printf("HIT k=%d l=%d%s a=%lld b=%lld c=%lld e=%lld %s%s H=%lld\n",k,l,(k%l==0)?"(l|k)":"",a,b,c,e,II?"II":"",I?"I":"",H);} }
    }
  }
  printf("done B=%d k=%d..%d l<%d mismatches=%lld\n",B,kmin,kmax,lmax,mism);
}
