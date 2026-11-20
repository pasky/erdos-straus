// Independent of f-scan: factor every n+u in increasing blocks. k is 4 or 8.
// Exact decision via u<=B and B(kuC-1)=n+u. Stops at first positive.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdint>
#include <vector>
using I=int64_t;
using Factors=std::vector<std::pair<I,int>>;
static I root(I n){I r=sqrtl(n);while(r+1<=n/(r+1))r++;while(r>n/r)r--;return r;}
static I search(const Factors& a,unsigned j,I f,I n,I k,I u){if(f>(n+u)/u)return 0;
 if(j==a.size())return (f+1)%(k*u)==0?f:0;
 auto [p,e]=a[j];for(int t=0;;t++){I h=search(a,j+1,f,n,k,u);if(h)return h;if(t==e)break;f*=p;}return 0;}
static I solve(I n,I k,const std::vector<int>& primes){
 // k*u*u-2*u<=n => u<=floor(sqrt(n/k))+2.
 I lim=root(n/k)+2,chunk=4096;
 for(I lo=1;lo<=lim;){I hi=std::min(lim,lo+chunk-1);
 std::vector<I> rem(hi-lo+1);std::vector<Factors> a(hi-lo+1);
 for(I u=lo;u<=hi;u++)rem[u-lo]=n+u;
 for(I p:primes){if(p*p>n+hi)break;for(I j=(p-(n+lo)%p)%p;j<=hi-lo;j+=p){int e=0;do{rem[j]/=p;++e;}while(rem[j]%p==0);a[j].emplace_back(p,e);}}
 for(I u=lo;u<=hi;u++){unsigned j=u-lo;if(rem[j]>1)a[j].emplace_back(rem[j],1);
 I f=search(a[j],0,1,n,k,u);if(f){I B=(n+u)/f,C=(f+1)/(k*u);assert(u<=B&&C>0&&(__int128)k*u*B*C-u-B==n);
 printf("%ld %ld %ld %ld %ld\n",k,n,u,B,C);return 1;}}
 lo=hi+1;chunk=std::min<I>(16*chunk,1000000);
 }printf("UNRESOLVED_REQUIRES_SECOND_EXACT %ld %ld\n",k,n);return 0;}
int main(){std::vector<std::pair<I,I>> jobs;I n,k,bound=0;while(scanf("%ld %ld",&k,&n)==2){assert((k==4||k==8)&&n>1&&n<=10000000000200000LL);jobs.emplace_back(n,k);bound=std::max(bound,root(n+root(n)+2));}
 std::vector<bool> composite(bound+1);std::vector<int> primes;
 for(I p=2;p<=bound;p++)if(!composite[p]){primes.push_back(p);for(I t=p*p;t<=bound;t+=p)composite[t]=true;}
 for(auto [value,coeff]:jobs)solve(value,coeff,primes);}
