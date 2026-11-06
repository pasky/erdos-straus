// z60 LOPEZT: (U5)-form test. For numerator N in {4,8}:
//   S_N(n) <=> exists g = -1 (mod N), g>=N-1, gcd(g,n)=1, such that r=(-n mod g) or r'=(-n*N^{-1} mod g)
//              divides (g+1)/N  (residues in [1,g-1]).
// Prints n (n = 1 mod 4, prime or all) with S_N(n) false.  usage: u5 NMAX N onlyprime
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; for(u64 d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
static ll inv(ll a, ll m){ ll g=m, x=0, x1=1, a1=a%m; if(a1<0)a1+=m; ll b=a1; // ext gcd of b mod m
  ll r0=m, r1=b, s0=0, s1=1; while(r1){ ll q=r0/r1; ll t=r0-q*r1; r0=r1; r1=t; t=s0-q*s1; s0=s1; s1=t; }
  if(r0!=1) return -1; return ((s0%m)+m)%m; }
int main(int argc,char**argv){
  u64 NMAX=atoll(argv[1]); int N=atoi(argv[2]); int onlyprime=atoi(argv[3]);
  for(u64 n=5; n<=NMAX; n+=4){
    if(onlyprime && !isprime(n)) continue;
    int hit=0; u64 gbound = 2*n+2; // witnesses g | n+a (g<=4n/3) or g | n+4a with g=-1 mod 4a: g <= ... safe bound 2n+2 (see memo)
    for(u64 g=N-1; g<=gbound && !hit; g+=N){
      if(n%g==0) continue;
      u64 q=(g+1)/N; ll r = (ll)(g - n%g); // -n mod g in [1,g-1]
      if(q % (u64)r == 0) { hit=1; break; }
      ll Ni = inv(N, g); if(Ni<0) continue;
      ll r2 = (ll)((( (__int128)(n%g) * Ni ) % g)); r2 = g - r2; if(r2==(ll)g) r2=0;
      if(r2>0 && q % (u64)r2 == 0) { hit=1; break; }
    }
    if(!hit) printf("%llu %s\n", n, isprime(n)?"P":"C");
  }
}
