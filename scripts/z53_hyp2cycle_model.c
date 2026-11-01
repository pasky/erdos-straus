/* z53_hyp2cycle_model.c — independent-CRT ("random prime") model for the remainder map f on (U,2U].
   For p uniform over units modulo a common multiple of all moduli:
     E N2   = sum_{U<u<B<=2U, gcd(u,B)=1} 1/phi(uB)
     E N4   = sum_{same, u+B odd} 1/phi(4uB)          (= (1/4) * odd-sum part)
     E Nodd = sum_{same, u+B odd} 1/phi(uB)
     E N3   = sum_{U<x<y<z<=2U pairwise coprime} 2/phi(xyz)   (directed 3-cycles; pairwise coprimality is forced at primes)
     E Ndef = sum_x #{y in (U,2U]: gcd(x,y)=1}/phi(x)
   usage: ./model U [do3]   */
#include <stdio.h>
#include <stdlib.h>
static long gcdl(long a,long b){ while(b){long t=a%b;a=b;b=t;} return a; }
int main(int argc,char**argv){ long U=atol(argv[1]); int do3=argc>2?atoi(argv[2]):1;
  long M=2*U+1; long *ph=malloc(sizeof(long)*(M+1)); for(long i=0;i<=M;i++) ph[i]=i;
  for(long i=2;i<=M;i++) if(ph[i]==i) for(long j=i;j<=M;j+=i) ph[j]-=ph[j]/i;
  double N2=0,N4=0,Nodd=0,N3=0,Nd=0;
  for(long u=U+1;u<=2*U;u++){ long c=0; for(long y=U+1;y<=2*U;y++) if(gcdl(u,y)==1) c++; Nd+=(double)c/ph[u]; }
  for(long u=U+1;u<=2*U;u++) for(long B=u+1;B<=2*U;B++){ if(gcdl(u,B)!=1) continue;
      double w=1.0/((double)ph[u]*ph[B]); N2+=w; if((u+B)&1){ Nodd+=w; N4+=w/4.0; } }
  if(do3){
    #pragma omp parallel for reduction(+:N3) schedule(dynamic)
    for(long x=U+1;x<=2*U;x++) for(long y=x+1;y<=2*U;y++){ if(gcdl(x,y)!=1) continue; double wxy=1.0/((double)ph[x]*ph[y]);
      for(long z=y+1;z<=2*U;z++){ if(gcdl(x,z)!=1||gcdl(y,z)!=1) continue; N3+=2.0*wxy/ph[z]; } }
  }
  printf("U=%ld EN2=%.5f EN4=%.5f ENodd=%.5f EN3=%.5f ENdef/U=%.5f\n",U,N2,N4,Nodd,do3?N3:-1.0,Nd/U); return 0; }
