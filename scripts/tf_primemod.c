/* O207: which primes p <= P have NO Type II certificate with a PRIME modulus h (h = 4cdj-1, h | p + 4c^2 d)?
   Stage 1 (marking): for every prime h = 3 mod 4, h <= H0, mark p = -c/j (mod h) for all cj | (h+1)/4.
   Stage 2 (exhaustive, for unmarked p): all Type II solutions via x in ((p+1)/4, p/2], e = 4x-p,
   delta | x^2 with delta = -x (mod e), y' = (x+delta)/e, h = 4y'-1; report whether some h is prime.
   Also odd squares: stage 2 must find no solution at all (T1).
   Usage: tf_primemod P H0 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef __int128 i128;
static int *spf; static long SL;
static int isprime64(u64 n){ if(n<2) return 0; if(n<(u64)SL) return spf[n]==(long)n;
  for(u64 q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
static long inv(long a,long m){ long t=0,nt=1,r=m,nr=a%m; if(nr<0) nr+=m; while(nr){ long q=r/nr,tmp; tmp=t-q*nt;t=nt;nt=tmp; tmp=r-q*nr;r=nr;nr=tmp;} if(t<0)t+=m; return t; }
static int divs(long n,long*dv){ int c=1; dv[0]=1; long m=n; while(m>1){ long q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} int c0=c; long pw=1; for(int i=1;i<=e;i++){pw*=q; for(int j=0;j<c0;j++) dv[c++]=dv[j]*pw;} } return c; }
/* stage 2: returns 0 none, 1 only composite moduli, 2 some prime modulus */
static int stage2(long p, long *nsol){
  int best=0; *nsol=0; static long dv[200000];
  for(long x=p/4+1; 2*x<=p; x++){ long e=4*x-p; if(e<=0) continue; { long a=x,b=p; while(b){ long t=a%b; a=b; b=t; } if(a!=1) continue; }
    /* divisors of x^2 from factorisation of x */
    long pr[20]; int ex[20],k=0; long m=x; while(m>1){ long q=spf[m]; int t=0; while(m%q==0){m/=q;t++;} pr[k]=q; ex[k]=2*t; k++; }
    int c=1; dv[0]=1; for(int i=0;i<k;i++){ int c0=c; long pw=1; for(int t=1;t<=ex[i];t++){ pw*=pr[i]; for(int j=0;j<c0;j++) dv[c++]=dv[j]*pw; } }
    for(int i=0;i<c;i++){ long d=dv[i]; if((x+d)%e) continue; long yp=(x+d)/e; long zp_num=x*(x+ (i128)0) ; (void)zp_num;
      /* z' = (x + x^2/d)/e must be integer too */
      i128 x2d=(i128)x*x/d; if(((i128)x+x2d)%e) continue;
      (*nsol)++; u64 h=4*(u64)yp-1; int pr_=isprime64(h); if(pr_) best=2; else if(best<1) best=1; }
  }
  return best;
}
int main(int argc,char**argv){
  long P=atol(argv[1]), H0=atol(argv[2]); SL=(H0>P?H0:P)+2;
  spf=calloc(SL,sizeof(int)); for(long i=2;i<SL;i++) if(!spf[i]) for(long j=i;j<SL;j+=i) if(!spf[j]) spf[j]=i;
  char *mark=calloc(P+1,1); static long dv[100000];
  for(long h=7; h<=H0; h+=4){ if(spf[h]!=h) continue; long k=(h+1)/4; int nd=divs(k,dv);
    for(int a=0;a<nd;a++){ long c=dv[a]; long kc=k/c; for(int b=0;b<nd;b++){ long j=dv[b]; if(kc%j) continue;
      long r=(h - (c%h)*inv(j%h,h)%h)%h; /* p = -c/j mod h */
      for(long p=r; p<=P; p+=h) mark[p]=1; } } }
  long np=0, unm=0, noprime=0, nsq=0, sqsol=0;
  for(long n=5;n<=P;n+=2){ int isp=(spf[n]==n); long r=0; while((r+1)*(r+1)<=n) r++; int issq=(r*r==n);
    if(isp){ np++; if(mark[n]) continue; unm++; long ns; int b=stage2(n,&ns);
      if(b<2){ noprime++; printf("no prime modulus: p=%ld (Type II solutions %ld, status %d)\n",n,ns,b); } }
    else if(issq){ nsq++; long ns; stage2(n,&ns); if(ns) sqsol++; } }
  printf("P=%ld H0=%ld primes=%ld unmarked_after_stage1=%ld no_prime_modulus=%ld ; odd squares=%ld with Type II solutions=%ld\n",P,H0,np,unm,noprime,nsq,sqsol);
  return 0; }
