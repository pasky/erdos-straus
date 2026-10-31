// Z1371: C_min(p) = least C such that 4Cp+1 has a divisor d ≡ -1 (mod 4C)  [(★) line], for primes p ≡ 1 (4) ≤ X.
// Tail histogram P(C_min > x) at x = 2^k; prints records. Cap at CMAX (reported as fail).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), CMAX=strtoull(argv[2],0,10), LO = argc>3? strtoull(argv[3],0,10):0;
  char*sv=calloc(X+1,1); for(u64 i=2;i*i<=X;i++) if(!sv[i]) for(u64 j=i*i;j<=X;j+=i) sv[j]=1;
  u64 hist[64]={0}, n=0, rec=0, fails=0;
  for(u64 p=5;p<=X;p+=4){ if(sv[p]||p<LO) continue; n++;
    u64 C; int found=0;
    for(C=1;C<=CMAX && !found;C++){
      u64 N=4*C*p+1, m=4*C;
      for(u64 d=m-1; d*d<=N; d+=m) if(N%d==0){found=1;break;}
      if(found) break;
    }
    if(!found){fails++; printf("FAIL p=%llu (C<=%llu)\n",p,CMAX); continue;}
    int k=0; while((1ULL<<k) < C) k++;   // C <= 2^k
    hist[k]++;
    if(C>rec){rec=C; printf("record p=%llu Cmin=%llu\n",p,C);}
  }
  printf("n=%llu fails=%llu\n",n,fails);
  u64 cum=n-fails; for(int k=0;k<40;k++){ if(!hist[k]&&k>20) break; cum-=hist[k]; printf("P(Cmin > 2^%d) = %.3e  (%llu)\n",k,(double)cum/n,cum);}
}
