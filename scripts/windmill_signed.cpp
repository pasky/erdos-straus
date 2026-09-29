// Complete enumeration of signed ES vertices (unordered triples of nonzero
// integers, 4/p = 1/x+1/y+1/z) for primes p = 1 mod 24 in [lo,hi], using the
// exact incidence model of SIGNED_REFACTOR.md section 3: every vertex has a
// positive p-free denominator x <= 2t, and then f = +-p^j d, d | x^2, j in {0,1},
// m = (x+f)/(4x-p) nonzero integer, p !| m, vertex (x, p m, p x m / f).
// Output: "P p" then sorted triples, one per line (deduplicated).
// Build: g++ -O2 -std=c++17 scripts/windmill_signed.cpp -o /tmp/wm_signed
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <array>
typedef __int128 i128;
static void print128(i128 v){ char b[64]; int n=0; if(v==0){putchar('0');return;} bool neg=v<0; if(neg)v=-v; while(v){b[n++]='0'+(int)(v%10); v/=10;} if(neg)putchar('-'); while(n)putchar(b[--n]); }
int main(int argc,char**argv){
  long lo=atol(argv[1]), hi=atol(argv[2]); int mod24 = argc>3? atoi(argv[3]) : 24;
  long N=hi+1; std::vector<int> spf(N+1,0);
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i;
  for(long p=lo;p<=hi;p++){
    if(p<5||p%mod24!=1||spf[p]!=p) continue;
    long t=(p-1)/4;
    std::vector<std::array<i128,3>> V;
    for(long x=1;x<=2*t;x++){
      i128 q=4*x-p;
      std::vector<i128> divs{1}; long mm=x;
      while(mm>1){ long r=spf[mm]; int e=0; while(mm%r==0){mm/=r;e++;} size_t n=divs.size(); i128 pw=1; for(int k=1;k<=2*e;k++){pw*=r; for(size_t i=0;i<n;i++) divs.push_back(divs[i]*pw);} }
      for(i128 d:divs) for(int j=0;j<2;j++) for(int sg=-1;sg<=1;sg+=2){
        i128 f=sg*d*(j?p:1);
        i128 num=x+f; if(num%q) continue; i128 m=num/q; if(m==0||m%p==0) continue;
        i128 P=(i128)p*x*m; if(P%f) continue; i128 z=P/f; if(z==0) continue;
        std::array<i128,3> v={ (i128)x, (i128)p*m, z}; std::sort(v.begin(),v.end()); V.push_back(v);
      }
    }
    std::sort(V.begin(),V.end()); V.erase(std::unique(V.begin(),V.end()),V.end());
    printf("P %ld\n",p);
    for(auto&v:V){ print128(v[0]); putchar(' '); print128(v[1]); putchar(' '); print128(v[2]); putchar('\n'); }
  }
}
