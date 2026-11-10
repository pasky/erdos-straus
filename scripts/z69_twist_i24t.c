// z69 TWIST round 2, I24 exploratory (NOT pre-registered): lag profile in the t-coordinate.
// (★) <=> exists even t and a | t with a + t/a = s(t) := 4t - (p mod 4t)   [K1 t-form; each t has one candidate s(t)].
// For every solution (a <= b, d) of a prime p == 1 (4), p <= N, with t = ab >= TMIN: is E_{t+2k} true,
// E_T := [ s(T)^2 - 4T is a perfect square ],  for near lags k = +-1..+-8 and far lags k = +-20..+-27 ?
// Local-class null: the same near-lag tests with p replaced by p' = the next prime == p (mod 6720) above p
// (6720 = 64*3*5*7 is a multiple of gcd(4t, 4(t+2k)) for all |k| <= 8), which carries the same small-modulus conditions.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int issq(long v){ if(v<0) return 0; long r=(long)sqrtl((long double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r*r==v; }
static int E(long p,long T){ if(T<2) return 0; long s=4*T-(p%(4*T)); return issq(s*s-4*T); }
static long dnat(long p,long T){ long s=4*T-(p%(4*T)); return (p+s)/(4*T); }   // the unique fibre d that t = T can serve
int main(int argc,char**argv){
  long N=atol(argv[1]), TMIN=atol(argv[2]); long NN=N+2000000; char *comp=calloc(NN+1,1); for(long i=2;i*i<=NN;i++) if(!comp[i]) for(long j=i*i;j<=NN;j+=i) comp[j]=1;
  long n=0,near[17]={0},farp[8]={0},farm[8]={0},nul[17]={0},nulself=0,nnul=0,nearx=0,nulx=0;
  for(long a=1;4*a*a-2*a<=N;a++) for(long b=a;4*a*b-a-b<=N;b++){ long t=a*b; if(t<TMIN) continue;
    for(long d=1;;d++){ long p=4*t*d-a-b; if(p>N) break; if(p<5||comp[p]||(p&3)!=1) continue;
      n++; for(int k=-8;k<=8;k++) if(k){ int h=E(p,t+2*k); near[k+8]+=h; if(h&&dnat(p,t+2*k)!=d) nearx++; }
      long q=p+6720; while(q<=NN&&comp[q]) q+=6720;
      if(q<=NN){ nnul++; nulself+=E(q,t); for(int k=-8;k<=8;k++) if(k){ int h=E(q,t+2*k); nul[k+8]+=h; if(h&&dnat(q,t+2*k)!=dnat(q,t)) nulx++; } }
      for(int k=20;k<28;k++){ farp[k-20]+=E(p,t+2*k); farm[k-20]+=E(p,t-2*k); } } }
  printf("N=%ld TMIN=%ld: solution instances (a<=b, counted with multiplicity over a): %ld\n",N,TMIN,n);
  long nn=0,ff=0; printf("near lags k (t' = t+2k): ");
  for(int k=-8;k<=8;k++) if(k){ printf("%+d:%ld ",k,near[k+8]); nn+=near[k+8]; }
  printf("\nfar lags +-20..27: "); for(int k=0;k<8;k++){ printf("%ld/%ld ",farm[k],farp[k]); ff+=farm[k]+farp[k]; }
  double rn=(double)nn/(16.0*n), rf=(double)ff/(16.0*n);
  printf("\nmean rate near %.6f (hits %ld), far %.6f (hits %ld); ratio %.3f; Poisson z of the difference = %+.2f\n",rn,nn,rf,ff,rf>0?rn/rf:0.0,(nn-ff)/sqrt((double)(nn+ff)));
  long tn=0; printf("local-class null (p -> next prime == p mod 6720; %ld instances; E_t itself true at p' in %ld): ",nnul,nulself);
  for(int k=-8;k<=8;k++) if(k){ printf("%+d:%ld ",k,nul[k+8]); tn+=nul[k+8]; }
  printf("\nnear-lag hits: observed %ld, local-class null %ld; ratio %.4f; Poisson z = %+.2f\n",nn,tn,tn?(double)nn/tn:0.0,(nn-tn)/sqrt((double)(nn+tn)));
  printf("cross-fibre only (hits at t+2k whose fibre d' differs from the fibre of t): observed %ld, local-class null %ld; ratio %.4f; Poisson z = %+.2f\n",nearx,nulx,nulx?(double)nearx/nulx:0.0,(nearx-nulx)/sqrt((double)(nearx+nulx)));
  return 0;
}
