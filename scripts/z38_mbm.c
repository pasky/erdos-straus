/* z38_mbm.c (O268): R*, M0 and the BM-corrected main term M_BM for odd n in [lo, hi].
   Pairs (u,B): gcd(u,B)=1, u+B odd, 4uB-u-B <= n, q = 4uB, a = -(u+B).
     R*(n)   = #{pairs : q | n+u+B}
     M0(n)   = sum_{pairs, gcd(n,q)=1} 1/phi(q)
     T(n)    = sum_{pairs, gcd(n,q)=1} kron(-4uB, n)/phi(q)       (kron(-4uB,n) = Jacobi(-uB/n), a character mod n in uB)
     M_BM(n) = M0(n) - T(n)   (principal + Brauer character chi_{-4uB}; BM_CORRECTED_COUNT Thm 1.1)
     X_BM(n) = R*(n) - M_BM(n)
   phi(4uB) = 4 phi(u) phi(B) (exactly one of u,B even).  For m = uB <= n/4 every coprime ordered splitting of an even m
   is a pair, weight W(m) = 2^omega(m)/phi(4m); pairs with uB > n/4 (boundary) enumerated directly.
   usage: ./z38_mbm lo hi mode     mode 0 = primes only, 1 = all odd n (composites too)
   output: one line per n:  n isprime R M0 MBM MBM8   (MBM8: also conditioned on n mod 8, i.e. characters mod 8 added) ; plus summary to stderr.
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

static int *spf; static double *phi4w; /* W(m) for m even, 0 otherwise */
static int jac(long a, long m){ a%=m; if(a<0)a+=m; int t=1; while(a){ while(!(a&1)){a>>=1; long r=m&7; if(r==3||r==5)t=-t;} long x=a;a=m;m=x; if((a&3)==3&&(m&3)==3)t=-t; a%=m;} return m==1?t:0; }
static long gcdl(long a,long b){ while(b){long t=a%b;a=b;b=t;} return a; }

int main(int argc,char**argv){
  long lo=atol(argv[1]), hi=atol(argv[2]); int mode=atoi(argv[3]);
  long N=hi+2;
  spf=calloc(N+1,sizeof(int)); for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i;
  int *phi=malloc((N+1)*sizeof(int)); int *om=calloc(N+1,sizeof(int)); phi[1]=1;
  for(long i=2;i<=N;i++){ long l=spf[i], r=i/l; if(r%l==0){ phi[i]=phi[r]*l; om[i]=om[r]; } else { phi[i]=phi[r]*(l-1); om[i]=om[r]+1; } }
  /* W(m) for m <= N/4: m even: 2^omega(m)/phi(4m); phi(4m) = 4 phi(u)phi(B) = 4 phi(m) for coprime split -> W = 2^om/(4 phi(m)) */
  long Mmax=N/3+2; phi4w=calloc(Mmax+1,sizeof(double));
  for(long m=2;m<=Mmax;m+=2) phi4w[m]=(double)(1L<<om[m])/(4.0*phi[m]);
  /* W8[m*4+j]: weight of coprime ordered splittings m = uB with (u+B) mod 8 = 2j+1 (for M_BM8) */
  double *W8=calloc(4*(Mmax+1),sizeof(double));
  for(long u=1;u<=Mmax;u++) for(long B=1;u*B<=Mmax;B++){ if(((u+B)&1)==0||gcdl(u,B)!=1) continue; long m=u*B; W8[4*m+(((u+B)&7)>>1)]+=1.0/(4.0*phi[m]); }
  /* R* for all n <= hi via triples */
  unsigned short *R=calloc(N+1,sizeof(unsigned short));
  for(long u=1;3*u-1<=hi;u++) for(long B=1;4*u*B-u-B<=hi;B++){ if(((u+B)&1)==0||gcdl(u,B)!=1) continue; long q=4*u*B; for(long n=q-u-B;n<=hi;n+=q) if(n>=lo) R[n]++; }
  signed char *chi=malloc(Mmax+2); signed char *chi0=malloc(Mmax+2);
  double minratio=1e9; long argmin=0; long cnt=0, zeroR=0;
  for(long n=lo|1;n<=hi;n+=2){
    if(n<5) continue;
    int isp = (spf[n]==n);
    if(mode==0 && !isp) continue;
    long K=(n+1)/3+1; /* max uB */
    int cm1 = jac(-1,n); chi[1]=1; chi0[1]=1;
    for(long k=2;k<=K;k++){ long l=spf[k]; if(l==k){ int j=jac(k,n); chi[k]=(signed char)j; chi0[k]=(signed char)(j!=0); } else { chi[k]=chi[l]*chi[k/l]; chi0[k]=chi0[l]*chi0[k/l]; } }
    double M0=0,T=0,M8=0; long m4=n/4; int jr=(((-n)&7)>>1); /* need (u+B) == -n mod 8 */
    for(long m=2;m<=m4;m+=2){ if(chi0[m]){ M0+=phi4w[m]; T+=chi[m]*phi4w[m]; double w=W8[4*m+jr]; if(w>0){ long o=m; while(!(o&1)) o>>=1; M8 += 4.0*w*(o>1 ? (1.0-cm1*chi[m]) : 1.0); } } }
    /* boundary: pairs with uB > n/4, 4uB-u-B <= n */
    for(long u=1;;u++){ long Bl=n/(4*u)+1; long Bh=(n+u)/(4*u-1); if(u>1 && Bh<1) break; if(3*u-1>n) break;
      for(long B=Bl;B<=Bh;B++){ if(((u+B)&1)==0) continue; if(gcdl(u,B)!=1) continue; long m=u*B; if(m<=m4) continue; if(!chi0[m]) continue;
        double w=1.0/(4.0*phi[u]*(double)phi[B]); M0+=w; T+=chi[m]*w;
        if((((u+B)+n)&7)==0){ long o=m; while(!(o&1)) o>>=1; M8 += 4.0*w*(o>1 ? (1.0-cm1*chi[m]) : 1.0); } } }
    T*=cm1; double MBM=M0-T; double X=R[n]-MBM; cnt++; if(R[n]==0) zeroR++;
    long sq=(long)llround(sqrt((double)n)); int issq=(sq*sq==n);
    printf("%ld %d %d %.4f %.4f %.4f\n",n,isp,R[n],M0,MBM,M8);
    if(!issq && MBM>0){ double r=R[n]/MBM; if(r<minratio){minratio=r;argmin=n;} }
  }
  fprintf(stderr,"# n in [%ld,%ld] mode %d: %ld values, R*=0 at %ld; min R/M_BM over non-squares %.4f at n=%ld\n",lo,hi,mode,cnt,zeroR,minratio,argmin);
  return 0;
}
