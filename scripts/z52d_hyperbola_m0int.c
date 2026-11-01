/* z52d_hyperbola_m0int.c — class-blind prime local density of the interior region (Z52D_HYPERBOLA.md §5):
   M0_int(p,T0) = sum_{u,B >= T0, gcd(u,B)=1, u+B odd, 4uB*T0 <= p+u+B} 1/phi(4uB)   [= sum 1/(4 phi(u) phi(B))].
   usage: ./a.out p T0   (OpenMP) */
#include <stdio.h>
#include <stdlib.h>
static unsigned long gcdu(unsigned long a,unsigned long b){ while(b){unsigned long t=a%b;a=b;b=t;} return a; }
int main(int c,char**v){ unsigned long p=strtoul(v[1],0,10); long T0=atol(v[2]);
  long N=(long)((p+2.0)/(4.0*T0*T0))+4; long *ph=malloc(sizeof(long)*(N+1));
  for(long i=0;i<=N;i++) ph[i]=i; for(long i=2;i<=N;i++) if(ph[i]==i) for(long j=i;j<=N;j+=i) ph[j]-=ph[j]/i;
  double S=0;
  #pragma omp parallel for reduction(+:S) schedule(dynamic,16)
  for(long u=T0;u<=N;u++){ double a=0;
    for(long B=T0;B<=N;B++){ if((__int128)4*u*B*T0 > (__int128)(p+u+B)) break; if(((u+B)&1)==0) continue; if(gcdu(u,B)==1) a+=1.0/(double)ph[B]; }
    S+=a/(4.0*ph[u]); }
  printf("%lu\t%ld\t%.8f\n",p,T0,S); return 0; }
