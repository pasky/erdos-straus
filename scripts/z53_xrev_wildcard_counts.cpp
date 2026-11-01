// Independent II-ii enumeration: factor p+4*a*a*C, rather than loop over (a,b,h).
// Usage: counts < counts_hard.out (five columns; asserts equality).
// Build/run under timeout and ulimit; memory O(max p), capped here at p <= 1000000.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>
using I = long long;
int main() {
    std::vector<std::array<I,5>> rows;
    std::array<I,5> row;
    I largest = 0;
    while (std::cin >> row[0] >> row[1] >> row[2] >> row[3] >> row[4]) {
        assert(row[0] >= 5 && row[0] <= 1000000);
        rows.push_back(row); largest = std::max(largest,row[0]);
    }
    assert(!rows.empty());
    int bound = 2*largest + 2*std::sqrt(largest) + 10;
    std::vector<int> spf(bound+1);
    for (int i=2;i<=bound;++i) if (!spf[i]) {
        spf[i]=i;
        if (I(i)*i<=bound) for (int j=i*i;j<=bound;j+=i) if (!spf[j]) spf[j]=i;
    }
    for (auto expected: rows) {
        I p=expected[0];
        std::array<I,5> got{p,0,0,0,0};
        // a <= b, h >= 1 imply p >= 4*a*b*C-a-b >= 4*a*a*C-2*a.
        for (I a=1;4*a*a-2*a<=p;++a) {
            for (I C=1;4*a*a*C-2*a<=p;++C) {
                int n=p+4*a*a*C;
                std::vector<I> divisors{1};
                while (n>1) {
                    int q=spf[n], exponent=0;
                    do { n/=q; ++exponent; } while (n%q==0);
                    size_t old=divisors.size(); I power=1;
                    for(int j=1;j<=exponent;++j) {
                        power*=q;
                        for(size_t k=0;k<old;++k) divisors.push_back(divisors[k]*power);
                    }
                }
                I modulus=4*a*C;
                for (I d: divisors) if ((d+1)%modulus==0) {
                    I h=(d+1)/modulus;
                    assert((h*p+a)%d==0);
                    I b=(h*p+a)/d;
                    if (b<a) continue;
                    assert(h*p==4*a*h*b*C-a-b);
                    ++got[2]; if(h==1) ++got[1]; if(a==1) ++got[3]; if(h==2) ++got[4];
                }
            }
        }
        for (I x:got) std::cout<<x<<' ';
        std::cout<<'\n';
        if(got!=expected) { std::cerr<<"MISMATCH p="<<p<<'\n'; return 1; }
    }
    std::cerr<<"Independent II-ii counts agree: "<<rows.size()<<" rows\n";
}
