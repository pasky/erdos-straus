// Independent IDEAA audit: prime-by-prime direct congruences, not residue marking.
// g++ -O2 -std=c++17 scripts/z69_xrev_ideaa_census.cpp -o /tmp/xrev_IDEAA/census
// ulimit -v 6000000; timeout 1800 /tmp/xrev_IDEAA/census 100000000
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using U = uint64_t;
struct Candidate { U m,a,b,e; };
std::vector<Candidate> cs;
struct Hit { U m=0,a=0,b=0,e=0; };
void identity(U p, Hit h, bool typeI) {
    U a=h.a,b=h.b,e=h.e,c=(a+b)/e;
    U d=(typeI?p*e+1:p+e)/(4*a*b);
    assert(c && d && (a+b)%e==0);
    cpp_int x=cpp_int(typeI?p:1)*a*b*d;
    cpp_int y=cpp_int(typeI?1:p)*a*c*d, z=cpp_int(typeI?1:p)*b*c*d;
    assert(4*x*y*z==cpp_int(p)*(x*y+x*z+y*z));
}
std::pair<Hit,Hit> search(U p) {
    Hit i,ii;
    for (auto w:cs) {
        if (4*w.m>p) break;
        if (!i.m && (p*w.e+1)%(4*w.m)==0) i={w.m,w.a,w.b,w.e};
        if (!ii.m && (p+w.e)%(4*w.m)==0) ii={w.m,w.a,w.b,w.e};
        if (i.m && ii.m) break;
    }
    assert(i.m && ii.m);
    return {i,ii};
}
int main(int argc,char**argv) {
    U X=argc>1?std::strtoull(argv[1],nullptr,10):100000000;
    assert(X<=100000000); // Bound memory; extremes checked individually below.
    const U cap=40000;
    for(U a=1;a*a<=cap;++a) for(U b=a;a*b<=cap;++b) {
        U s=a+b;
        for(U e=1;e*e<=s;++e) if(s%e==0) {
            if(e%4==3) cs.push_back({a*b,a,b,e});
            if(s/e!=e && (s/e)%4==3) cs.push_back({a*b,a,b,s/e});
        }
    }
    std::sort(cs.begin(),cs.end(),[](auto a,auto b){return a.m<b.m;});
    std::vector<U> qs;
    for(U q=1;q<=cap;q=q<16?q+1:q*5/4+1) qs.push_back(q);
    std::vector<U> si(qs.size()),sii(qs.size()),sb(qs.size());
    std::vector<bool> composite(X+1);
    for(U q=2;q*q<=X;++q) if(!composite[q])
        for(U k=q*q;k<=X;k+=q) composite[k]=true;
    U count=0,maxK=0,maxP=0,maxI=0,maxII=0;
    for(U p=25;p<=X;p+=24) if(!composite[p]) {
        ++count;
        auto [i,ii]=search(p);
        U k=std::min(i.m,ii.m);
        if(k>maxK) {maxK=k;maxP=p;}
        maxI=std::max(maxI,i.m);maxII=std::max(maxII,ii.m);
        for(size_t j=0;j<qs.size();++j) {
            si[j]+=i.m>qs[j]; sii[j]+=ii.m>qs[j];sb[j]+=k>qs[j];
        }
    }
    std::cout<<"N "<<count<<" maxK "<<maxK<<" p "<<maxP<<" maxI "<<maxI<<" maxII "<<maxII<<"\n";
    for(size_t j=0;j<qs.size();++j)
        std::cout<<"S "<<qs[j]<<" "<<sb[j]<<" "<<si[j]<<" "<<sii[j]<<"\n";
    for(U p: {1775179561ULL,2431459801ULL,278893729ULL,7183201ULL,6106475761ULL,3280856329ULL}) {
        for(U d=2;d*d<=p;++d) assert(p%d!=0);
        auto [i,ii]=search(p);
        identity(p,i,true);identity(p,ii,false);
        std::cout<<"EXT "<<p<<" K "<<std::min(i.m,ii.m)<<" I "<<i.m<<" II "<<ii.m
                 <<" I(a,b,e) "<<i.a<<","<<i.b<<","<<i.e
                 <<" II(a,b,e) "<<ii.a<<","<<ii.b<<","<<ii.e<<"\n";
    }
}
