/* Z1533: per-level (*) failure P(no d | N, d ≡ -1 mod 4C), N = 4Cn+1, for
   (E) primes n ≡ 1 (4) in [X, X+W];  (A) all n ≡ 1 (4) in the window (integer model);
   (B) same factorisation shapes as (E) but each prime factor gets an i.i.d. uniform class in (Z/4C)^*  (PD+uniform-class model);
   (B') as (B) but last class conditioned so that the product of classes ≡ 1 = N mod 4C. */
#include <stdio.h>
#include "z52b_p1_H04_fac.h"
static u64 rs=88172645463325252ULL;static u64 rnd(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static u64 gcd2(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){u64 X=atoll(argv[1]),W=atoll(argv[2]);int CM=atoi(argv[3]);
 for(int C=1;C<=CM;C++){u64 m=4*C;u64 units[512];int nu=0;for(u64 a=1;a<m;a++)if(gcd2(a,m)==1)units[nu++]=a;
  long tE=0,fE=0,tA=0,fA=0,fB=0,fB2=0;u64 pr[64],cl[64];int ex[64];
  for(u64 n=X|1;n<X+W;n+=2){if(n%4!=1)continue;u64 N=4*C*n+1;int k=factor(N,pr,ex);int r=has_div_class(pr,ex,k,m,m-1);
   tA++;if(!r)fA++; if(!isprime(n))continue; tE++;if(!r)fE++;
   /* model B / B' */
   for(int i=0;i<k;i++)cl[i]=units[rnd()%nu];
   int rb=has_div_class(cl,ex,k,m,m-1);if(!rb)fB++;
   /* B': fix last class so prod ≡ 1 */
   u64 prod=1;for(int i=0;i<k-1;i++)prod=mulm(prod,powm(cl[i],ex[i],m),m);
   /* find class c with c^{ex} * prod ≡ 1 ; pick uniformly among solutions */
   u64 sol[512];int ns=0;for(int j=0;j<nu;j++)if(mulm(prod,powm(units[j],ex[k-1],m),m)==1)sol[ns++]=units[j];
   if(ns){cl[k-1]=sol[rnd()%ns];int rb2=has_div_class(cl,ex,k,m,m-1);if(!rb2)fB2++;}else fB2++;
  }
  printf("C=%2d phi=%3d  primes: P(fail)=%.4f (n=%ld)  integers: %.4f  modelB(iid classes): %.4f  modelB'(prod≡1): %.4f\n",C,nu,(double)fE/tE,tE,(double)fA/tA,(double)fB/tE,(double)fB2/tE);
  fflush(stdout);}
}
