// Shared exhaustive prime enumeration for Z1901 and Z2780; divisor method.
// g++ -O2 -std=c++17 this.cpp -o /tmp/zf0-enum
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <cassert>
using ll=long long; using I=__int128;
ll gcd(ll a,ll b){return std::gcd(a,b);}
int main(int argc,char**argv){
 int N=argc>1?atoi(argv[1]):100000;
 std::vector<int> spf(N+1); for(int i=2;i<=N;i++)if(!spf[i])for(int j=i;j<=N;j+=i)if(!spf[j])spf[j]=i;
 std::vector<std::vector<ll>> ds(3*N/4+1);
 for(int x=1;x<(int)ds.size();x++){auto &v=ds[x];v={1};int m=x;while(m>1){int q=spf[m],e=0;while(m%q==0){m/=q;e++;}int k=v.size();ll pw=1;for(int j=1;j<=2*e;j++){pw*=q;for(int h=0;h<k;h++)v.push_back(v[h]*pw);}}}
 puts("p,triples,unit_binary,distinct_anchors,minimal_anchors,anchor_certificates,typeI,typeII,path00,path01,path10,path11,cert00,cert01,cert10,cert11,only_z");
 for(int p=2;p<=N;p++)if(spf[p]==p){
 ll cnt=0,ub=0,ac=0,tI=0,tII=0,paths[4]={},certs[4]={},oz=0; std::set<ll> anchors;int mins=0;
 for(ll x=p/4+1;4*x<=3*p;x++){
  ll a=4*x-p,b=(ll)p*x,g=gcd(a,b);a/=g;b/=g; bool hit=false;
  // For odd primes x<p, gcd(a,b)=1; p=2 is handled by generic tiny divisors.
  std::vector<ll> tiny; if(p==2)for(ll d=1;d<=b;d++)if(b*b%d==0)tiny.push_back(d);
  auto accept=[&](ll d){if(d>b||(b+d)%a)return;ll y=(b+d)/a;if(y<x)return;I zz=((I)b*b/d+b)/a;assert(zz<=9223372036854775807LL);ll z=zz;
   assert((I)4*x*y*z==(I)p*(x*y+(I)x*z+(I)y*z));cnt++;hit=true;
   ll w[3]={x,y,z};int typ=(x%p==0)+(y%p==0)+(z%p==0);if(typ==1)tI++;if(typ==2)tII++;
   oz+=(x%p!=0&&y%p!=0&&z%p==0);
   bool binary=false;for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if((I)w[i]*w[j]%(w[i]+w[j])==0)binary=true;ub+=binary;
   for(int i=0;i<3;i++)if(i==0||w[i]!=w[i-1]){anchors.insert(w[i]);ac++;}
   bool seen[4]={}; do {
    // Reduced prefix (u+v)/(uv); determinants test genuine Farey edges.
    ll u=w[0],v=w[1],last=w[2];I prod=(I)u*v;ll h=gcd(u+v,(ll)(prod%(u+v)));
    bool middle=(I)u*u==h; // determinant u^2 / gcd(u+v,uv).
    bool final=(p==2)||(last%p==0&&(4*(last/p)-1)%p==0);int mask=2*middle+final;paths[mask]++;seen[mask]=true;
   }while(std::next_permutation(w,w+3));for(int i=0;i<4;i++)certs[i]+=seen[i];
  };
  if(p==2){for(ll d:tiny)accept(d);}else for(ll t:ds[x]){accept(t);if(t<=x)accept(p*t);}
  mins+=hit;
 }
 printf("%d,%lld,%lld,%zu,%d,%lld,%lld,%lld",p,cnt,ub,anchors.size(),mins,ac,tI,tII);for(auto a:paths)printf(",%lld",a);for(auto a:certs)printf(",%lld",a);printf(",%lld\n",oz);
 }
}
