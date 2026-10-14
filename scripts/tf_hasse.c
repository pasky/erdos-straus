/* TORSION_FIRING §4: Type II certificates inside the Hasse interval (O207).
   For odd n (primes <= NMAX, and odd squares as T1 control):
   A(n): exists c,d>=1, 4c^2 d - 1 <= 2 sqrt(n), and a divisor h of n + 4c^2 d with h = -1 mod 4cd
         (= an F_n-curve of trace a = 1 - 4c^2 d has a subgroup of order = -1 mod 4cd).
   B(n): exists c>=1, c - 1 <= 2 sqrt(n), divisor h of n + c with h = -1 mod 4c   (trace a = 1 - c).
   S(n): (supersingular trace 0) n + 1 has a divisor h = 3 mod 4.
   Usage: tf_hasse NMAX */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int *spf;
static int ndiv(long N, long *dv){ /* all divisors */
  long pr[32]; int ex[32], k=0; long m=N;
  while(m>1){ long q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} pr[k]=q; ex[k]=e; k++; }
  int c=1; dv[0]=1;
  for(int i=0;i<k;i++){ int c0=c; long pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<c0;j++) dv[c++]=dv[j]*pw; } }
  return c;
}
static int hasdiv(long N, long M){ static long dv[20000]; int c=ndiv(N,dv); for(int i=0;i<c;i++) if((dv[i]+1)%M==0) return 1; return 0; }
int main(int argc,char**argv){
  long NMAX=atol(argv[1]); long L=NMAX+3*(long)sqrt((double)NMAX)+10;
  spf=calloc(L+1,sizeof(int));
  for(long i=2;i<=L;i++) if(!spf[i]) for(long j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i;
  long np=0,nA=0,nB=0,nAB=0,nS=0,nsq=0,sqA=0,sqB=0,sqS=0, noneAB=0; long firstnone[20]; int nf=0;
  for(long n=5;n<=NMAX;n+=2){
    int isp = (spf[n]==n); long r=(long)llround(sqrt((double)n)); int issq = (r*r==n);
    if(!isp && !issq) continue;
    double w=2*sqrt((double)n);
    int A=0,B=0,S=0;
    for(long c=1; 4*c*c-1<=w && !A; c++) for(long d=1; 4*c*c*d-1<=w && !A; d++) if(hasdiv(n+4*c*c*d,4*c*d)) A=1;
    for(long c=1; c-1<=w && !B; c++) if(hasdiv(n+c,4*c)) B=1;
    S=hasdiv(n+1,4);
    if(isp && (!A || !B) && n<2000000) printf("miss n=%ld A=%d B=%d\n",n,A,B);
    if(isp){ np++; nA+=A; nB+=B; nAB+=(A||B); nS+=S; if(!A&&!B){ noneAB++; if(nf<20) firstnone[nf++]=n; } }
    else { nsq++; sqA+=A; sqB+=B; sqS+=S; }
  }
  printf("NMAX=%ld primes=%ld  A(trace 1-4c^2d)=%ld  B(trace 1-c)=%ld  A|B=%ld  none=%ld  S(supersingular p+1)=%ld\n",NMAX,np,nA,nB,nAB,noneAB,nS);
  printf("first primes with neither:"); for(int i=0;i<nf;i++) printf(" %ld",firstnone[i]); printf("\n");
  printf("odd squares=%ld  A=%ld B=%ld S=%ld (T1: all must be 0)\n",nsq,sqA,sqB,sqS);
  return 0;
}
