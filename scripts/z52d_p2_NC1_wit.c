// z52d pass2 NC1 fix: dump all C-form witnesses (C, d) with C ≤ CMAX for primes p ≡ 1 (mod 4), p ≤ X.
// d | 4Cp+1, d ≡ -1 (mod 4C), d ≤ sqrt(N). Complement e = N/d is also a witness (≡ -1 mod 4C).
// usage: z52d_p2_NC1_wit X CMAX > out ; line: "p C d"
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), CMAX=strtoull(argv[2],0,10);
  char*sv=calloc(X+1,1); sv[0]=sv[1]=1;
  for(u64 i=2;i*i<=X;i++) if(!sv[i]) for(u64 j=i*i;j<=X;j+=i) sv[j]=1;
  for(u64 p=5;p<=X;p+=4){ if(sv[p]) continue;
    for(u64 C=1;C<=CMAX;C++){ u64 N=4*C*p+1, m=4*C;
      for(u64 d=m-1; d*d<=N; d+=m) if(N%d==0) printf("%llu %llu %llu\n",p,C,d);
    }
  }
  return 0;
}
