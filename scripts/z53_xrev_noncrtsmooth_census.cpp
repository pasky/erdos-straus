// Independent hostile-review census: enumerate u <= B and C directly,
// never factor p+u or 4Cp+1. Usage: PROGRAM < prime_list > census.csv.
// Compile with g++ -O2 -std=c++17; bound memory/time in the invoking shell.
#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <vector>
using I = long long;
int main() {
    std::vector<I> ns;
    I n;
    while (std::cin >> n) ns.push_back(n);
    if (ns.empty()) return 0;
    const I top = (4 * *std::max_element(ns.begin(), ns.end()) + 1) / 3;
    if (top > 20000000 || *std::min_element(ns.begin(), ns.end()) < 5) return 2;
    std::vector<int> spf(top + 1);
    for (I a = 2; a <= top; ++a) if (!spf[a]) {
        spf[a] = a;
        if (a * a <= top) for (I b = a * a; b <= top; b += a)
            if (!spf[b]) spf[b] = a;
    }
    auto largest = [&](I a) {
        I m = 1;
        while (a > 1) { m = std::max<I>(m, spf[a]); a /= spf[a]; }
        return m;
    };
    std::cout << "n,R,Rxp,Rp,Rs25,Rs33,Rs50,Cmin,bestM,bestPM,PM1,PM2,PM6,PM12,PM60,Rbp,Re25,Re33\n";
    for (I p : ns) {
        I R=0,Rxp=0,Rp=0,Rbp=0,Rs25=0,Rs33=0,Rs50=0,Re25=0,Re33=0,Cmin=-1;
        std::map<I,I> pm;
        auto closure = [&](I u,I C) {
            for (I d=1; d*d<=u; ++d) if (u%d==0) {
                ++pm[C*d];
                if (d*d!=u) ++pm[C*(u/d)];
            }
        };
        for (I u=1; 4*u*u-2*u<=p; ++u) {
            // B >= u implies C <= (p+2u)/(4u^2).
            for (I C=1; C<=(p+2*u)/(4*u*u); ++C) {
                const I d=4*u*C-1;
                if ((p+u)%d) continue;
                const I B=(p+u)/d;
                if (B<u) return 3;
                const I x=d,y=4*C*B-1,mult=(u==B?1:2);
                const bool xp=(spf[x]==x),yp=(spf[y]==y);
                const I hi=std::max(largest(x),largest(y)),lo=std::min(largest(x),largest(y));
                R+=mult; Rxp+=xp+(u==B?0:yp);
                Rp+=mult*(xp||yp); Rbp+=mult*(xp&&yp);
                // Largest factors may be large: divide rather than raise to fourth powers.
                auto smooth=[&](I a,int power) {
                    I rem=p;
                    for(int j=0;j<power;++j) rem/=a;
                    return rem>=1;
                };
                Rs25+=mult*smooth(hi,4); Rs33+=mult*smooth(hi,3); Rs50+=mult*smooth(hi,2);
                Re25+=mult*smooth(lo,4); Re33+=mult*smooth(lo,3);
                if(Cmin<0||C<Cmin) Cmin=C;
                closure(u,C); if(u!=B) closure(B,C);
            }
        }
        I bestM=0,bestPM=0;
        for(auto [M,count]:pm) if(count>bestPM) {bestM=M;bestPM=count;}
        std::cout<<p<<','<<R<<','<<Rxp<<','<<Rp<<','<<Rs25<<','<<Rs33<<','<<Rs50<<','<<Cmin<<','<<bestM<<','<<bestPM;
        for(I M:{1,2,6,12,60}) std::cout<<','<<pm[M];
        std::cout<<','<<Rbp<<','<<Re25<<','<<Re33<<'\n';
    }
}
