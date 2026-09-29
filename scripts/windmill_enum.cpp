// Enumerate all unordered positive ES solutions x<=y<=z of 4/p=1/x+1/y+1/z
// for primes p = 1 mod 24 in [lo,hi].  Output: "P p" line, then "x y z" lines.
// Exact: for each x in (p/4, 3p/4], r/s = (4x-p)/(px) is already reduced,
// and y=(s+D)/r, z=(s+s^2/D)/r over divisors D<=s of s^2 with D=-s mod r.
// Build: g++ -O2 -std=c++17 scripts/windmill_enum.cpp -o /tmp/wm_enum
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstdint>
typedef unsigned long long u64;
typedef __int128 i128;
static void print128(i128 v){ char b[64]; int n=0; if(v==0){putchar('0');return;} bool neg=v<0; if(neg)v=-v; while(v){b[n++]='0'+(int)(v%10); v/=10;} if(neg)putchar('-'); while(n)putchar(b[--n]); }
int main(int argc,char**argv){
  long lo=atol(argv[1]), hi=atol(argv[2]);
  long N=hi+1;
  std::vector<int> spf(N+1,0);
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i;
  for(long p=lo;p<=hi;p++){
    if(p<25||p%24!=1||spf[p]!=p) continue;
    printf("P %ld\n",p);
    for(long x=p/4+1; 4*x<=3*p; x++){
      i128 r=4*x-p; i128 s=(i128)p*x;
      // factor s^2 = p^2 x^2
      std::vector<std::pair<i128,int>> f; f.push_back({p,2});
      long m=x; while(m>1){ long q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} f.push_back({q,2*e}); }
      std::vector<i128> divs{1};
      for(auto&pe:f){ size_t n=divs.size(); i128 pw=1; for(int e=1;e<=pe.second;e++){ pw*=pe.first; for(size_t i=0;i<n;i++) divs.push_back(divs[i]*pw);} }
      i128 target=((-s)%r+r)%r;
      for(i128 D:divs){ if(D>s) continue; if(D%r!=target) continue;
        i128 y=(s+D)/r, z=(s+s*s/D)/r; if(y<x) continue;
        printf("%ld ",x); print128(y); putchar(' '); print128(z); putchar('\n'); }
    }
  }
}
