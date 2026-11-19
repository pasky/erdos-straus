// Exact sieve for Type II e-slices with coprime ratio A/B and omega(AB)<=2.
// c | A+B, c=3 mod 4, n=4ABD-c (D>=1). For primes n=1 mod 4,
// c<n and K=(n+c)/4, so all the factors are prime to n.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
int main(int argc, char** argv) {
    if (argc!=2) return 2;
    long long lim=std::atoll(argv[1]);
    if(lim<5 || lim>500000000) return 2;
    const int N=lim, K=(N+1)/3;
    std::vector<int> spf(K+2);
    for(int j=2;j<=K+1;j++) if(!spf[j]) {
        spf[j]=j;
        for(int64_t i=1LL*j*j; i<=K+1;i+=j) if(!spf[i]) spf[i]=j;
    }
    std::vector<bool> ok(N/4+1,false), prime(N+1,true);
    for(int j=2;1LL*j*j<=N;j++) if(prime[j])
        for(int i=j*j;i<=N;i+=j) prime[i]=false;
    std::vector<int> divs;
    auto mark=[&](int k,int t) {
        divs.clear(); divs.push_back(1);
        while(t>1) {
            int q=spf[t], count=divs.size(), h=1;
            do { t/=q; h*=q;
                for(int j=0;j<count;j++) divs.push_back(divs[j]*h);
            } while(t%q==0);
        }
        for(int c:divs) if(c%4==3)
            for(int64_t n=4LL*k-c;n<=N;n+=4LL*k) ok[n/4]=true;
    };
    // k=1 has A+B=2, so c=3 mod 4 is impossible.
    for(int k=2;k<=K;k++) {
        int b=k,q=spf[k]; do b/=q; while(b%q==0);
        if (b>1) {
            int r=spf[b],h=b; do h/=r; while(h%r==0);
            if(h>1) continue;
            mark(k,b+k/b); // the two prime powers on opposite sides
        }
        mark(k,k+1); // all prime powers on the same side
    }
    int misses=0,tested=0;
    for(int n=5;n<=N;n+=4) if(prime[n]) {
        ++tested;
        if(!ok[n/4]) { if(misses<20) std::cout<<n<<' '; ++misses; }
    }
    std::cout<<"\nmisses "<<misses<<" / "<<tested<<", N="<<N<<'\n';
}
