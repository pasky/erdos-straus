// z52d pass2 NC1 Z1363: f(n) = number of ES triples 4/n = 1/x+1/y+1/z with x ≤ y ≤ z (unordered, positive), n ≤ NMAX.
// For each x in (n/4, 3n/4]: a = 4x-n, b = n x; solutions (a y - b)(a z - b) = b^2 with d | b^2, d ≡ -b (mod a).
// Output: n f(n) per line. Divisors of b^2 from trial-division factorisation of b.
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
typedef long long ll;
static int fac(u64 b, u64*pr, int*ex){ int k=0; for(u64 q=2;q*q<=b;q++){ if(b%q==0){ int e=0; while(b%q==0){b/=q;e++;} pr[k]=q; ex[k]=e; k++; } } if(b>1){pr[k]=b; ex[k]=1; k++;} return k; }
int main(int argc,char**argv){
  int NMAX=atoi(argv[1]);
  static u64 divs[400000];
  for(int n=2;n<=NMAX;n++){
    ll cnt=0;
    // collect (y,z) pairs via x; use set-free counting with x ≤ y ≤ z: count triples where x is minimal.
    for(int x=(n+3)/4; 4*x<=3*n; x++){
      ll a=4LL*x-n; if(a<=0) continue;
      u64 b=(u64)n*x;
      u64 pr[32]; int ex[32]; int k=fac(b,pr,ex);
      int nd=1; divs[0]=1;
      for(int i=0;i<k;i++){ int cur=nd; u64 pw=1;
        for(int e=1;e<=2*ex[i];e++){ pw*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
      // also powers from exponent 0 handled; now divisors of b^2 = all products; we built all divisors of b^2 with exponents up to 2e
      for(int i=0;i<nd;i++){
        u64 d=divs[i]; if(((d+b)%a)!=0) continue;
        // dp = b^2/d ; need b^2 = d*dp: b^2 up to ~1e14 fits in u64
        u64 bb=b*b; u64 dp=bb/d; if(((dp+b)%a)!=0) continue;
        u64 y=(d+b)/a, z=(dp+b)/a;
        if(y>=1 && z>=1 && (ll)x<=(ll)y && y<=z) cnt++;
      }
    }
    printf("%d %lld\n",n,cnt);
  }
  return 0;
}
