// Full unordered strict Type I and II counts, for primes 5 <= p <= 2e11, p=1 mod 4.
// See data/z75/esexact/README.md for the coverage argument and invocation.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
#include <gmpxx.h>
using U=unsigned long; using W=__uint128_t;
static_assert(sizeof(U)==8);
using namespace std;
U p,E,F; int typ; bool verbose;
set<tuple<U,W,U,U>> hits[3];
string dec(W n){if(n<10)return string(1,'0'+int(n));return dec(n/10)+char('0'+int(n%10));}
vector<U> primes;
U root(U n){U r=sqrt((long double)n);while((W)r*r>n)--r;while((W)(r+1)*(r+1)<=n)++r;return r;}
U modpow(U a,U b,U n){U t=1;while(b){if(b&1)t=W(t)*a%n;a=W(a)*a%n;b>>=1;}return t;}
// All GMP primality decisions above the library's 'definite' range are
// confirmed by the first 12 prime MR bases (Sorenson-Webster threshold
// 318665857834031151167461 > (2e11)^2+4*(3*2e11/4)^2).
bool prime(const mpz_class& n){int z=mpz_probab_prime_p(n.get_mpz_t(),8);if(z!=1)return z==2;
 mpz_class m=n-1;unsigned s=mpz_scan1(m.get_mpz_t(),0);m>>=s;
 for(U a:{2,3,5,7,11,13,17,19,23,29,31,37}){mpz_class v=a;mpz_powm(v.get_mpz_t(),v.get_mpz_t(),m.get_mpz_t(),n.get_mpz_t());if(v==1||v==n-1)continue;
 unsigned j=1;for(;j<s;++j){v=v*v%n;if(v==n-1)break;}if(j==s)return false;}return true;
}
mpz_class rho(const mpz_class& n){if(n%2==0)return 2;
 for(U k=1;;++k){mpz_class x=2,y=x,g=1,q=1;
 for(U r=1;g==1 && r<(1UL<<24);r*=2){x=y;for(U i=0;i<r;i++)y=(y*y+k)%n;
 for(U i=0;i<r && g==1;i+=64){q=1;for(U j=0;j<min(64UL,r-i);j++){y=(y*y+k)%n;q=q*(x-y)%n;}mpz_gcd(g.get_mpz_t(),q.get_mpz_t(),n.get_mpz_t());}}
 if(g!=1&&g!=n)return g;}}
using Pows=vector<pair<mpz_class,int>>;
void record(Pows& v,const mpz_class& q,int e){for(auto& t:v)if(t.first==q){t.second+=e;return;}v.emplace_back(q,e);}
void factor(mpz_class n,Pows& v){if(n==1)return;if(prime(n)){record(v,n,1);return;}auto h=rho(n);factor(h,v);factor(n/h,v);}
// Visit all divisors <= cap (every stored product fits unsigned long).
template<class G> void divs(const Pows& v,U cap,G g){auto rec=[&](auto&& self,size_t i,U n)->void{if(i==v.size()){g(n);return;}auto& [q,e]=v[i];for(int j=0;;++j){self(self,i+1,n);if(j==e||q>cap/n)break;n*=q.get_ui();}};rec(rec,0,1);}
void hit(U a,W b,U c,U d){if(b<a||gcd(gcd(a,U(b%a)),c)!=1)return;
 if(typ==1){if(a%p==0||b%p==0||c%p==0||d%p==0)return;assert(W(4)*a*b*c*d==W(p)*(a+b)+c);}else{if(a%p==0||b%p==0||d%p==0)return;assert(W(4)*a*b*c*d==W(p)*c+a+b);}
 hits[typ].emplace(a,b,c,d);}
// Short arithmetic progression, peel small primes by a progression sieve. Factor
// remaining cofactors exactly. Typical memory linear in sample length.
template<class G> void progression(U start,U step,U len,G g){if(!len)return;
 vector<U> rem(len);vector<Pows> facts(len);for(U i=0;i<len;++i)rem[i]=start+step*i;
 U top=root(rem.back());for(U q:primes){if(q>top)break;if(step%q==0){assert(start%q);continue;}
 U r=(q-start%q)*modpow(step%q,q-2,q)%q;for(;r<len;r+=q){int e=0;do{rem[r]/=q;++e;}while(rem[r]%q==0);facts[r].emplace_back(q,e);}}
 bool done=top<=primes.back();for(U i=0;i<len;++i){if(rem[i]>1){if(done)facts[i].emplace_back(rem[i],1);else factor(mpz_class(rem[i]),facts[i]);}g(i,facts[i]);}}
// Enumerate all labelled products a*b*d=N; cap a<=sqrt(N) since a<=b.
template<class G> void splits(const Pows& v,U N,G g){U qs[64];for(size_t i=0;i<v.size();++i)qs[i]=v[i].first.get_ui();auto rec=[&](auto&& self,size_t i,U a,U b)->void{if(i==v.size()){if(a<=b)g(a,b,N/(a*b));return;}int e=v[i].second;U q=qs[i],aa=a;for(int j=0;j<=e;++j){if(aa>N/aa)break;U bb=b;for(int k=0;k<=e-j;++k){self(self,i+1,aa,bb);if(k<e-j)bb*=q;}if(j<e)aa*=q;}};rec(rec,0,1,1);}
void eslices(U lim){if(lim<3)return;U len=(lim-3)/4+1,first=(typ==1?(3*p+1):(p+3))/4,step=typ==1?p:1;
 for(U off=0;off<len;off+=65536){progression(first+step*off,step,min(65536UL,len-off),[&](U i,const Pows& v){U e=3+4*(off+i),N=first+step*(off+i);splits(v,N,[&](U a,U b,U d){if((a+b)%e==0)hit(a,b,(a+b)/e,d);});});}}
// Here the labelled factor pair in splits is not (a,c): their order matters.
void acds(U y,const Pows& v,U f){splits(v,y,[&](U a,U c,U d){auto one=[&](U a,U c){W bf=typ==1?W(p)*a+c:W(p)*c+a;if(bf%f==0){W b=bf/f;hit(a,b,c,d);}};one(a,c);if(a!=c)one(c,a);});}
void smallf(){if(F<3)return;U len=(F-3)/4+1;for(U off=0;off<len;off+=65536)progression((p+3)/4+off,1,min(65536UL,len-off),[&](U i,const Pows& v){acds((p+3)/4+off+i,v,3+4*(off+i));});}
void typeII(){typ=2;U L=root(p);eslices(L);U K=p/(L+1);for(U off=0;off<K;off+=65536)progression(1+off,1,min(65536UL,K-off),[&](U i,const Pows& v){U k=1+off+i;acds(k,v,4*k-1);});}
// Type I residual, e>E, f>F, T=c*c*d; (ef-1)T=(p+f)^2/4.
// a<=d: b lies in a single class mod 4ac because bf=pa+c,
// f=-p mod 4ac.  d<a: f=-p mod 4cd and f | p^2+4T.
void residual(){U Y=3*p/4; W H=W(4)*Y*Y; // (p+f)^2/4 <= 4Y^2
 U Tmax=U(min<W>(Y*W(Y),H/(W(E+1)*(F+1)-1))); // parameters restricted in main
 U maxA=root(Y);vector<U> inv(maxA+1);for(U a=1;a<=maxA;++a){mpz_class v=p,m=4*a;int ok=mpz_invert(v.get_mpz_t(),v.get_mpz_t(),m.get_mpz_t());assert(ok);inv[a]=v.get_ui();}
 for(U c=1;c<=root(Tmax);++c){U maxsmall=root(Y/c);U minA=U((W(c)*((E+1)*W(F+1)-1)+4*Y-1)/(4*Y));
 for(U a=max(1UL,minA);a<=maxsmall;++a){if(gcd(a,c)!=1)continue;U m=4*a*c, neg=(a+c*inv[a])%m;U b=m-neg;W prod=W(p)*a+c;U hi=U(prod/(F+1));for(;b<=hi;b+=m){if(b<a||prod%b)continue;U f=U(prod/b);if((p+f)%m==0)hit(a,b,c,(p+f)/m);}}
 for(U d=1;d<=min(maxsmall,Tmax/(c*c));++d){U t=c*c*d,m=4*c*d;U hi=U(min<W>(4*Y-p,(H/t+1)/(E+1)));
 // Tighten the bound twice: use current f upper bound on the RHS.
 for(int j=0;j<2;j++)hi=U(min<W>(hi,((W(p+hi)*(p+hi)/(4*t))+1)/(E+1)));
 U a0=max(d+1,(p+F)/m+1),a1=(p+hi)/m;if(a1<a0)continue;
 auto test=[&](U a,U f){W bf=W(p)*a+c;if(bf%f==0){W b=bf/f;hit(a,b,c,d);}};
 if(a1-a0<12000){for(U a=a0;a<=a1;++a)test(a,m*a-p);}
 else {mpz_class n=mpz_class(p)*p+4*t;Pows v;for(U q:primes){if(q>1000)break;int e=0;while(mpz_divisible_ui_p(n.get_mpz_t(),q)){n/=q;++e;}if(e)v.emplace_back(q,e);}factor(n,v);
 divs(v,hi,[&](U f){if(f>F&&(p+f)%m==0){U a=(p+f)/m;if(a>d)test(a,f);}});}
 }} }
int main(int argc,char** argv){if(argc!=4 && argc!=5){cerr<<"usage: prime E F [emit]\n";return 1;}p=stoul(argv[1]);E=stoul(argv[2]);F=stoul(argv[3]);verbose=argc==5;
 if(p<5||p>200000000000UL||p%4!=1||E<1||F<1||E>20000000||F>200000000 || W(9)*p*p/(4*(W(E+1)*(F+1)-1))>1000000000000000UL)return 2;
 for(U q=2;q*q<=p;q++)if(p%q==0)return 2;
 vector<bool> composite(400001);for(U q=2;q<composite.size();q++)if(!composite[q]){primes.push_back(q);for(U j=q*q;j<composite.size();j+=q)composite[j]=true;}
 typeII();cerr<<"Type II complete: "<<hits[2].size()<<"\n";typ=1;eslices(E);cerr<<"Type I e done\n";smallf();cerr<<"Type I f done\n";residual();cout<<p<<" "<<E<<" "<<F<<" "<<hits[1].size()<<" "<<hits[2].size()<<"\n";
 if(verbose)for(int i:{1,2})for(auto [a,b,c,d]:hits[i])cout<<i<<" "<<a<<" "<<dec(b)<<" "<<c<<" "<<d<<"\n";
}
