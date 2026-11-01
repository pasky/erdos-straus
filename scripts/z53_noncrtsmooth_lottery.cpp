// z53 NONCRTSMOOTH: structured sub-lotteries of (*) 4uBC - u - B = n.
// For each odd n read from stdin, enumerate all ordered (*) triples via u and divisors x | n+u with x ≡ -1 (mod 4u)
// (x = 4Cu-1, B = (n+u)/x, y = 4CB-1, and y*u = n+B).  Report:
//   R          number of ordered triples
//   Rxp        triples with x prime;  Rp = triples with x or y prime;  Rbp = triples with x and y both prime
//   Re25,Re33  triples with x OR y n^theta-smooth (theta = 1/4, 1/3)
//   Rs25,Rs33,Rs50  triples with both x and y n^theta-smooth (theta = 1/4, 1/3, 1/2)
//   Cmin       least C over triples (= least M with P_M(n) nonempty, Lemma 2)
//   bestM, bestPM  the M maximising |P_M(n)| = #{triples: C | M | C*u}, and that count
//   PM1..       |P_M| for M = 1, 2, 6, 12, 60 (fixed small menus)
// Usage: ./a.out < list ; output CSV.  Memory O(n) (segment of length n/3+2).
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
typedef long long ll; typedef unsigned long long ull;

static vector<int> small_primes(int lim){ vector<char> s(lim+1,1); vector<int> P; for(int i=2;i<=lim;i++){ if(s[i]){P.push_back(i); for(ll j=(ll)i*i;j<=lim;j+=i) s[j]=0;} } return P; }

int main(){
  ll n;
  printf("n,R,Rxp,Rp,Rs25,Rs33,Rs50,Cmin,bestM,bestPM,PM1,PM2,PM6,PM12,PM60,Rbp,Re25,Re33\n");
  while(scanf("%lld",&n)==1){
    ll L = n/3 + 3; ll lo = n+1, hi = n+L;
    int lim = (int)sqrt((double)hi)+2; vector<int> P = small_primes(lim);
    // factor lists for each value n+u, u = 1..L  (index u)
    vector<ll> rem(L+1); for(ll u=1;u<=L;u++) rem[u]=n+u;
    vector<int> head(L+1,-1); vector<int> fp; vector<int> fe; vector<int> nxt; fp.reserve(4*L); fe.reserve(4*L); nxt.reserve(4*L);
    for(int q: P){ ll start = ((lo + q - 1)/q)*q; for(ll v=start; v<=hi; v+=q){ ll u=v-n; int e=0; while(rem[u]%q==0){rem[u]/=q;e++;} fp.push_back(q); fe.push_back(e); nxt.push_back(head[u]); head[u]=(int)fp.size()-1; } }
    auto factors=[&](ll u, vector<pair<ll,int>>& F){ F.clear(); for(int k=head[u];k!=-1;k=nxt[k]) F.push_back({fp[k],fe[k]}); if(rem[u]>1) F.push_back({rem[u],1}); };
    vector<int> spf(L+1,0); for(ll i=2;i<=L;i++) if(!spf[i]) for(ll j=i;j<=L;j+=i) if(!spf[j]) spf[j]=(int)i;
    auto ufac=[&](ll m, vector<pair<ll,int>>& F){ F.clear(); while(m>1){ ll q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} F.push_back({q,e}); } };
    double t25=pow((double)n,0.25), t33=pow((double)n,1.0/3), t50=sqrt((double)n);
    ll Rbp=0,Re25=0,Re33=0; ll R=0,Rxp=0,Rp=0,Rs25=0,Rs33=0,Rs50=0,Cmin=-1; unordered_map<ll,ll> PM; ll PMf[5]={0,0,0,0,0}; ll Mf[5]={1,2,6,12,60};
    vector<pair<ll,int>> F, G, H;
    for(ll u=1; u<=L; u++){
      ll N=n+u; ll mod=4*u; if(mod-1> N) break;
      factors(u,F);
      // enumerate divisors with their max prime and primality flag
      vector<ll> D={1}; vector<ll> Dmx={1}; vector<int> Dw={0};
      for(auto&f:F){ size_t s=D.size(); ll pw=1; for(int e=1;e<=f.second;e++){ pw*=f.first; for(size_t i=0;i<s;i++){ D.push_back(D[i]*pw); Dmx.push_back(max(Dmx[i],f.first)); Dw.push_back(Dw[i]+e);} } }
      for(size_t i=0;i<D.size();i++){ ll x=D[i]; if((x+1)%mod) continue; ll C=(x+1)/mod; ll B=N/x; ll y=4*C*B-1;
        R++; bool xp=(Dw[i]==1); if(xp) Rxp++;
        // y = (n+B)/u ; factor n+B, remove u
        if(B> L){ fprintf(stderr,"B out of range\n"); exit(1);} factors(B,G); ufac(u,H);
        ll ymx=1; int yw=0; for(auto&g:G){ int e=g.second; for(auto&h:H) if(h.first==g.first) e-=h.second; if(e>0){ ymx=max(ymx,g.first); yw+=e; } }
        bool yp=(yw==1); if(xp||yp) Rp++; if(xp&&yp) Rbp++;
        ll mx=max(Dmx[i],ymx); ll mn=min(Dmx[i],ymx); if(mn<=t25) Re25++; if(mn<=t33) Re33++; if(mx<=t25) Rs25++; if(mx<=t33) Rs33++; if(mx<=t50) Rs50++;
        if(Cmin<0||C<Cmin) Cmin=C;
        // M = C*t, t | u
        vector<ll> T={1}; for(auto&h:H){ size_t s=T.size(); ll pw=1; for(int e=1;e<=h.second;e++){ pw*=h.first; for(size_t k=0;k<s;k++) T.push_back(T[k]*pw);} }
        for(ll t:T) PM[C*t]++;
        for(int k=0;k<5;k++) if(Mf[k]%C==0 && (C*u)%Mf[k]==0) PMf[k]++;
      }
    }
    ll bM=0,bc=0; for(auto&kv:PM) if(kv.second>bc||(kv.second==bc&&kv.first<bM)){bc=kv.second;bM=kv.first;}
    printf("%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld\n",n,R,Rxp,Rp,Rs25,Rs33,Rs50,Cmin,bM,bc,PMf[0],PMf[1],PMf[2],PMf[3],PMf[4],Rbp,Re25,Re33);
    fflush(stdout);
  }
}
