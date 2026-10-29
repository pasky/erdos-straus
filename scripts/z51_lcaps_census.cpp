// Exact prime census; O(N) memory, O(q^2) streamed residue DP, no product arrays.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using U = uint64_t;
static const int INF=1000000;
vector<uint32_t> spf;
vector<pair<int,int>> factor(int n) {
    vector<pair<int,int>> f;
    while(n>1) { int s=spf[n], b=0; do {n/=s; ++b;} while(n%s==0); f.push_back({s,b}); }
    return f;
}
int power(U a, int b, int m) {
    U z=1; for(;b;b>>=1,a=a*a%m) if(b&1) z=z*a%m; return z;
}
// Returns minimal Type-II/full fixed-x cap for the given budget.
pair<int,int> caps(int p,int m,int budget,bool full) {
    int K=(p+m)/4;
    assert(gcd(K,m)==1);
    vector<int> dp(m,INF); dp[1%m]=0;
    for(auto [s,b]:factor(K)) {
        vector<int> local(m,INF),next(m,INF);
        U a=1;
        for(int c=0;c<=2*b+2*(s==2?0:budget);++c,a=a*s%m) {
            if(c<=2*b || c%2==0) local[a]=min(local[a],max(0,(c-2*b)/2));
        }
        vector<pair<int,int>> opts;
        for(int v=0;v<m;++v) if(local[v]<INF) opts.push_back({v,local[v]});
        for(int u=0;u<m;++u) if(dp[u]<INF)
            for(auto [v,e]:opts) next[U(u)*v%m]=min(next[U(u)*v%m],max(dp[u],e));
        dp.swap(next);
    }
    int target=(m-K%m)%m, c=dp[target], f=c;
    if(full) {
        f=min(f,dp[U(target)*(p%m)%m]);
        f=min(f,dp[U(target)*power(p%m,m-2,m)%m]);
    }
    return {c,f};
}
int explicit_cap(int p,int q) {
    int best=INF;
    for(auto [s,b]:factor((p+q)/4)) if(s!=2 && b%2 && power(s,(q-1)/2,q)==q-1) {
        int o=q-1;
        for(auto [t,a]:factor(q-1)) while(o%t==0 && power(s,o/t,q)==1) o/=t;
        assert(o%2==0 && (o/2)%2==1);
        best=min(best,max(0,(o/2-b)/2));
    }
    assert(best<INF && 4*best<=q-3);
    return best;
}
void hist(const string& key,const vector<U>& h,bool comma=true) {
    cout<<"\""<<key<<"\":{"; bool first=true;
    for(size_t i=0;i<h.size();++i) if(h[i]) {if(!first)cout<<",";first=false;cout<<"\""<<i<<"\":"<<h[i];}
    cout<<"}"<<(comma?",\n":"\n");
}
int main(int argc,char**argv) {
    int N=argc>1?stoi(argv[1]):100000000, window=255;
    string csv=argc>2?argv[2]:"/tmp/z51_lcaps_sample.csv";
    assert(N>=10000 && N<=100000000);
    vector<uint8_t> prime(N+1,1); prime[0]=prime[1]=0;
    for(int p=2;U(p)*p<=U(N);++p) if(prime[p]) for(int j=p*p;j<=N;j+=p) prime[j]=0;
    int Kmax=max(10001,(N+10000)/4+1); spf.resize(Kmax+1);
    for(int p=2;p<=Kmax;++p) if(!spf[p]) {
        spf[p]=p;
        if(U(p)*p<=U(Kmax)) for(int j=p*p;j<=Kmax;j+=p) if(!spf[j]) spf[j]=p;
    }
    vector<int> qs; vector<vector<uint8_t>> qr;
    for(int q=3;q<=10000;q+=4) if(prime[q]) {
        qs.push_back(q); qr.emplace_back(q,0);
        for(int a=1;a<q;++a) qr.back()[U(a)*a%q]=1;
    }
    set<int> controls={193,409,577,2521,3361,5569,9601,66529,8813281,
        23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561};
    ofstream out(csv); assert(out);
    out<<"p,q3,typeii_cap,full_cap,oneprime_cap,least_typeii_window\n";
    vector<U> hq(10001),hc(2501),hf(2501),he(2501),hw(257);
    U all=0,p14=0,count=0,censored=0; int rq=0,rc=-1,rf=-1,re=-1,rw=0;
    for(int p=2;p<=N;++p) if(prime[p]) {
        ++all; if(p%4==1)++p14; if(p%8!=1) continue; ++count;
        int q=0;
        for(size_t i=0;i<qs.size();++i) if(!qr[i][p%qs[i]]) {q=qs[i];break;}
        assert(q && p%q && (q%4==3));
        int ec=explicit_cap(p,q); auto [c,f]=caps(p,q,ec,true);
        assert(f<=c && c<=ec && 4*ec<=q-3);
        int win=0;
        for(int m=3;m<=window;m+=4) if(gcd(p,m)==1 && caps(p,m,0,false).first==0) {win=m;break;}
        if(!win)++censored;
        ++hq[q];++hc[c];++hf[f];++he[ec];++hw[win?win:256];
        bool record=q>rq || c>rc || f>rf || ec>re || win>rw;
        if(p<=20000 || controls.count(p) || record || !win)
            out<<p<<","<<q<<","<<c<<","<<f<<","<<ec<<","<<win<<"\n";
        rq=max(rq,q);rc=max(rc,c);rf=max(rf,f);re=max(re,ec);rw=max(rw,win);
    }
    cout<<"{\n\"N\":"<<N<<",\"all_primes\":"<<all<<",\"primes_1mod4\":"<<p14
        <<",\"primes_1mod8\":"<<count<<",\"window_limit\":"<<window
        <<",\"window_censored\":"<<censored<<",\n";
    hist("q3",hq);hist("typeii_cap",hc);hist("full_cap",hf);hist("oneprime_cap",he);hist("least_typeii_window",hw,false);
    cout<<"}\n";
}
