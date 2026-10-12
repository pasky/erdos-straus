// O152: enumerate all unordered positive solutions x<=y<=z of 4/n=1/x+1/y+1/z
// for ALL n in [lo,hi] with gcd(n,6)=1 and n%md==rs (optional args md rs; composites included).  Output "n x y z".
// Build: g++ -O2 -std=c++17 scripts/bs_invol_enum.cpp -o /tmp/bsinv/enum
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <cstdint>
typedef long long ll; typedef __int128 i128;
static void pr(i128 v){ char b[64]; int k=0; if(v==0){putchar('0');return;} while(v){b[k++]='0'+(int)(v%10); v/=10;} while(k)putchar(b[--k]); }
ll gcdl(ll a,ll b){ while(b){ll t=a%b;a=b;b=t;} return a; }
int main(int argc,char**argv){
  ll lo=atoll(argv[1]), hi=atoll(argv[2]); ll md=argc>3?atoll(argv[3]):1, rs=argc>4?atoll(argv[4]):0; ll N=hi+1;
  std::vector<int> spf(N+1,0);
  for(ll i=2;i<=N;i++) if(!spf[i]) for(ll j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i;
  for(ll n=lo;n<=hi;n++){
    if(n%2==0||n%3==0||n<5||n%md!=rs) continue;
    for(ll x=n/4+1; 4*x<=3*n; x++){
      ll r0=4*x-n; ll s0=n*x; ll g=gcdl(r0,s0); ll r=r0/g; ll s=s0/g;
      std::map<ll,int> f; ll m=n; while(m>1){int q=spf[m]; while(m%q==0){m/=q;f[q]++;}}
      m=x; while(m>1){int q=spf[m]; while(m%q==0){m/=q;f[q]++;}}
      std::vector<i128> divs{1}; ll ss=s;
      for(auto&pe:f){ int e=0; while(ss%pe.first==0){ss/=pe.first;e++;} if(!e) continue;
        size_t k=divs.size(); i128 pw=1; for(int j=1;j<=2*e;j++){ pw*=pe.first; for(size_t i=0;i<k;i++) divs.push_back(divs[i]*pw);} }
      i128 S=s, R=r, target=((-S)%R+R)%R;
      for(i128 D:divs){ if(D>S) continue; if(D%R!=target) continue;
        i128 y=(S+D)/R, z=(S+S*S/D)/R; if(y<x) continue;
        printf("%lld %lld ",n,x); pr(y); putchar(' '); pr(z); putchar('\n'); }
    }
  }
}
