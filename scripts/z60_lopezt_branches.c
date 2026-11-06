// z60 LOPEZT: zero sets of the two branches.
// B4 (4|y, modulus y): exists y=0 mod 4, f | p+y, f = -1 mod y.
// BN (4∤y, modulus 4y): exists y !=0 mod 4, f | p+y, f = -1 mod 4y.
// For each n=1 mod 4 (prime or not) up to N report which branches hit.
// Exhaustive: witness f = -1 (mod L_y) divides n+y with f >= L_y - 1 >= y - 1, so y <= n+1; y = n+1 forces f | 2n+1 with
// f = -1 mod 4(n+1) > 2n+1 (4 does not divide n+1 since n = 1 mod 4), impossible. Hence y <= n suffices. No cutoff.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; for(u64 d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
// check: does m have a divisor f = -1 mod L ?  enumerate f = L-1, 2L-1, ... up to m
static int hasdiv(u64 m, u64 L){ for(u64 f=L-1; f<=m; f+=L) if(f>1 && m%f==0) return 1; return 0; }
int main(int argc,char**argv){
  u64 N=atoll(argv[1]); int onlyprime = argc>2 ? atoi(argv[2]) : 1;
  for(u64 n=5; n<=N; n+=4){
    if(onlyprime && !isprime(n)) continue;
    int b4=0,bn=0; u64 y4=0,yn=0;
    for(u64 y=1; y<=n && !(b4&&bn); y++){
      if(y%4==0){ if(!b4 && hasdiv(n+y,y)){b4=1;y4=y;} }
      else { if(!bn && hasdiv(n+y,4*y)){bn=1;yn=y;} }
    }
    if(!b4||!bn) printf("%llu %s B4=%d(y=%llu) BN=%d(y=%llu)\n", n, isprime(n)?"P":"C", b4,y4,bn,yn);
  }
}
