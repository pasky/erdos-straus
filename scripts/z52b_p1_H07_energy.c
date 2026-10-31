// Z2461: energy E(N) = sum_{n<=N} R(n)^2, R(n) = #{(u,B,C)>=1 : 4uBC-u-B = n}
// also split over odd n / primes p≡1(4). Prints at N = 10^k checkpoints.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  uint16_t *R=calloc(N+1,2);
  for(long u=1;4*u-u-1<=N;u++) for(long B=1;4*u*B-u-B<=N;B++){
    long step=4*u*B; long n=step-u-B;
    for(;n<=N;n+=step) R[n]++;
  }
  char *comp=calloc(N+1,1);
  for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  double S1=0,S2=0,S3=0,P1=0,P2=0; long cnt=0,pc=0; long next=1000;
  int maxR=0;
  for(long n=1;n<=N;n++){
    double r=R[n]; S1+=r; S2+=r*r; S3+=r*r*r; cnt++;
    if(R[n]>maxR) maxR=R[n];
    if(n>2 && !comp[n] && n%4==1){P1+=r;P2+=r*r;pc++;}
    if(n==next){ double L=log(n);
      printf("N=%ld S1/N=%.4f S2/N=%.4f S3/N=%.3f  S1/(N L^2)=%.4f S2/(N L^4)=%.5f S3/(N L^6)=%.6f  primes1mod4: meanR/L^2=%.4f meanR^2/L^4=%.5f  ratio E[R^2]/E[R]^2 all=%.3f primes=%.3f maxR=%d\n",
        n,S1/cnt,S2/cnt,S3/cnt,S1/(cnt*L*L),S2/(cnt*L*L*L*L),S3/(cnt*pow(L,6)),P1/pc/(L*L),P2/pc/pow(L,4),(S2/cnt)/((S1/cnt)*(S1/cnt)),(P2/pc)/((P1/pc)*(P1/pc)),maxR);
      next*=10; fflush(stdout);}
  }
}
