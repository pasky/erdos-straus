// Exact P-box enumerator for K=5 by the complete Elsholtz--Tao four-regime cover.
// Usage: z78_exact_et r output.txt. GNU coreutils `factor` supplies exact factorizations.
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using u64 = uint64_t;
using u128 = __uint128_t;
struct Item { u64 value; u64 x, y; };
using Factors = std::vector<std::pair<u64,int>>;
static const std::string dir = "data/z78/exact/";

static std::vector<Factors> factor_batch(const std::vector<Item>& items, const std::string& tag) {
    const std::string in = dir + "factor_" + tag + ".in";
    const std::string out = dir + "factor_" + tag + ".out";
    { std::ofstream f(in); for (const auto& z : items) f << z.value << '\n'; }
    std::string cmd = "factor < " + in + " > " + out;
    if (std::system(cmd.c_str()) != 0) throw std::runtime_error("factor command failed");
    std::ifstream f(out);
    std::vector<Factors> ans; ans.reserve(items.size());
    std::string line;
    size_t row=0;
    while (std::getline(f,line)) {
        auto pos=line.find(':'); if(pos==std::string::npos || row>=items.size()) throw std::runtime_error("bad factor line");
        if(std::stoull(line.substr(0,pos))!=items[row].value) throw std::runtime_error("factor input/output mismatch");
        std::istringstream is(line.substr(pos+1)); u64 p; Factors fs; u128 product=1;
        while(is>>p) { product*=p; if(fs.empty() || fs.back().first!=p) fs.emplace_back(p,1); else fs.back().second++; }
        if(product!=items[row].value) throw std::runtime_error("factor product mismatch");
        ans.push_back(std::move(fs)); row++;
    }
    if(ans.size()!=items.size()) throw std::runtime_error("factor count mismatch");
    std::remove(in.c_str()); std::remove(out.c_str());
    return ans;
}
static void divisors_rec(const Factors& fs, size_t i, u64 cur, std::vector<u64>& ds) {
    if(i==fs.size()){ds.push_back(cur);return;}
    u64 p=fs[i].first, v=cur;
    for(int j=0;j<=fs[i].second;j++){divisors_rec(fs,i+1,v,ds); if(j<fs[i].second) v*=p;}
}
static std::vector<u64> divisors(const Factors& fs) {
    std::vector<u64> ds; divisors_rec(fs,0,1,ds); std::sort(ds.begin(),ds.end()); return ds;
}
static u64 ceil_pow(double x, double e) { u64 a=(u64)std::ceil(std::pow(x,e)); while(std::pow((long double)a,1.0L/e)<x) ++a; while(a>1 && std::pow((long double)(a-1),1.0L/e)>=x) --a; return a; }
int main(int argc,char**argv){
 try {
    if(argc!=3) throw std::runtime_error("usage: z78_exact_et r output.txt");
    const u64 r=std::stoull(argv[1]); const std::string output=argv[2];
    u64 nn=1; for(int i=0;i<5;i++){if(nn>std::numeric_limits<u64>::max()/r)throw std::runtime_error("r^5 overflow");nn*=r;}
    const u64 N=nn;
    const u64 Xcd=ceil_pow((double)N,0.3)+3; // conservative ceil((r^5)^0.3)
    u64 Xo=ceil_pow((double)N, 0.425)+3;
    while((u128)Xo*Xo*Xo*Xo*Xcd < (u128)N*N) ++Xo;
    if((u128)Xo*Xo*Xo*Xo*Xcd < (u128)N*N) throw std::runtime_error("ET cover threshold failed");
    std::set<std::array<u64,4>> sols;
    auto check=[&](u64 a,u64 b,u64 c,u64 d){
        if(!a||!b||!c||!d||a>b||c%r==0||d%r==0)return;
        if((u128)4*a*b*c*d != (u128)a+b+(u128)N*c)return;
        sols.insert({a,b,c,d});
    };
    // e regime: e <= Xo, 4abd=N+e, e | a+b.
    std::vector<Item> items;
    for(u64 e=1;e<=Xo;e++) if((N+e)%4==0) items.push_back({(N+e)/4,e,0});
    auto fs=factor_batch(items,"e");
    for(size_t i=0;i<items.size();i++){
        u64 e=items[i].x,M=items[i].value; auto ds=divisors(fs[i]);
        for(u64 a:ds){if((u128)a*a>M)break;u64 rem=M/a;
            for(u64 b:ds){if(b<a)continue;if(rem%b)continue;if((a+b)%e)continue;check(a,b,(a+b)/e,rem/b);}
        }
    }
    // ad regime.
    items.clear();
    for(u64 a=1;a<=Xo;a++) for(u64 d=1;d<=Xo/a;d++) if(d%r) items.push_back({(u64)((u128)N+4*(u128)a*a*d),a,d});
    fs=factor_batch(items,"ad");
    for(size_t i=0;i<items.size();i++){
        u64 a=items[i].x,d=items[i].y,L=4*a*d,M=items[i].value; auto ds=divisors(fs[i]);
        for(u64 f:ds) if((f+1)%L==0){u64 c=(f+1)/L,e=M/f;if((u128)c*e>=a)check(a,c*e-a,c,d);}
    }
    // ac regime.
    items.clear();
    for(u64 a=1;a<=Xo;a++) for(u64 c=1;c<=Xo/a;c++) if(c%r) items.push_back({(u64)((u128)N*c+a),a,c});
    fs=factor_batch(items,"ac");
    for(size_t i=0;i<items.size();i++){
        u64 a=items[i].x,c=items[i].y,L=4*a*c,M=items[i].value; auto ds=divisors(fs[i]);
        for(u64 f:ds) if((f+1)%L==0) check(a,M/f,c,(f+1)/L);
    }
    // cd regime.
    items.clear();
    for(u64 c=1;c<=Xcd;c++) for(u64 d=1;d<=Xcd/c;d++) if(c%r&&d%r){
        u128 v=(u128)4*c*c*d*N+1;if(v>std::numeric_limits<u64>::max())throw std::runtime_error("cd factor input exceeds uint64");
        items.push_back({(u64)v,c,d});
    }
    fs=factor_batch(items,"cd");
    for(size_t i=0;i<items.size();i++){
        u64 c=items[i].x,d=items[i].y,L=4*c*d,M=items[i].value; auto ds=divisors(fs[i]);
        for(u64 f:ds){if((f+1)%L)continue;u64 g=M/f;if((g+1)%L)continue;check((f+1)/L,(g+1)/L,c,d);}
    }
    u64 m=1;for(int i=0;i<3;i++)m*=r;
    std::set<u64> boxes;
    for(const auto&s:sols){u64 a=s[0],b=s[1],c=s[2],d=s[3];
        boxes.insert((u64)((m-((u128)4*a*c*d-1)%m)%m));
        boxes.insert((u64)((m-((u128)4*b*c*d-1)%m)%m));
    }
    std::ofstream out(output);for(u64 x:boxes)out<<x<<'\n';
    std::cerr<<"r="<<r<<" Xo="<<Xo<<" Xcd="<<Xcd<<" Pdata="<<sols.size()<<" boxes="<<boxes.size()<<"\n";
    return 0;
 } catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<"\n";return 2;}
}
