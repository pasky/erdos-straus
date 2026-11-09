// Lemma N check: primes p = 1 (8) <= N such that (p+1)/2 and p+4 have only prime factors = 1 (4)
// and p+2 only prime factors = 1,3 (8)  (the forced "norm chain" of a U7 counterexample); print count + first few
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); long M=N+9; unsigned *spf=calloc(M+1,sizeof(unsigned));
  for(long i=2;i<=M;i++) if(!spf[i]) for(long j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i;
  long c=0,c8=0,tot=0;
  for(long p=9;p<=N;p+=8){ if(spf[p]!=p) continue; tot++;
    int ok=1; long m=(p+1)/2; while(m>1&&ok){long l=spf[m]; if(l%4!=1) ok=0; m/=l;}
    m=p+4; while(m>1&&ok){long l=spf[m]; if(l%4!=1) ok=0; m/=l;}
    m=p+2; while(m>1&&ok){long l=spf[m]; if(l%8!=1&&l%8!=3) ok=0; m/=l;}
    if(!ok) continue; c++;
    // p+8: subgroup {1,3} or {1,5}
    int h3=0,h5=0,h7=0; m=p+8; while(m>1){long l=spf[m]; int t=l%8; if(t==3)h3=1; if(t==5)h5=1; if(t==7)h7=1; m/=l;}
    if(!h7 && !(h3&&h5)) { c8++; if(c8<=10) printf("chain(1,2,4,8) p=%ld\n",p); }
  }
  printf("N=%ld primes=1(8): %ld  chain(1,2,4): %ld  chain(1,2,4,8): %ld\n",N,tot,c,c8);
}
