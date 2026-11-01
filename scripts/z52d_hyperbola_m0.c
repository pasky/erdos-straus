/* z52d_hyperbola_m0.c — exact class-blind prime local density of the balanced block (Z52D_HYPERBOLA.md §5):
   M0(U) = sum_{u,B in (U,2U], gcd(u,B)=1, u+B odd} 1/phi(4uB) = sum 1/(4 phi(u) phi(B)).
   usage: ./a.out U   (OpenMP) */
#include <stdio.h>
#include <stdlib.h>
static unsigned gcdu(unsigned a,unsigned b){ while(b){unsigned t=a%b;a=b;b=t;} return a; }
int main(int c,char**v){ long U=atol(v[1]); long N=2*U+1; long *ph=malloc(sizeof(long)*(N+1));
  for(long i=0;i<=N;i++) ph[i]=i; for(long i=2;i<=N;i++) if(ph[i]==i) for(long j=i;j<=N;j+=i) ph[j]-=ph[j]/i;
  double S=0;
  #pragma omp parallel for reduction(+:S) schedule(dynamic,64)
  for(long u=U+1;u<=2*U;u++){ double a=0; for(long B=U+1+((U+1+u)%2==0);B<=2*U;B+=2){ if(gcdu(u,B)==1) a+=1.0/(double)ph[B]; } S+=a/(4.0*ph[u]); }
  printf("%ld\t%.8f\n",U,S); return 0; }
