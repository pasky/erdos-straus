/* Z2876: Riemenschneider dual shape of ES5 certificates.
   For prime p≡1 (4), B in [1,p-1]: test whether p/B = [[2^a,3,2^b,3,2^c]] or [[2^a,4,2^c]] (HJ, entries>=2),
   i.e. B = p - A with p/A = [[v,t,u]] (length-3 HJ).  Compare with the direct word count, record the quadratic
   class and the regular-CF digits of p/B (max digit) for the certificate B.  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int jac(long a,long n){int s=1;a%=n;if(a<0)a+=n;while(a){while(!(a&1)){a>>=1;long r=n&7;if(r==3||r==5)s=-s;}
 long t=a;a=n;n=t;if((a&3)==3&&(n&3)==3)s=-s;a%=n;}return n==1?s:0;}
/* returns 1 if HJ(p/B) has the dual shape; HJ: p/B = a1 - 1/(...): a1 = ceil(p/B) */
static int dualshape(long p,long B){long n=p,q=B;int n3=0,n4=0;
 while(q>0){long a=(n+q-1)/q; if(a>4)return 0; if(a==3)n3++; else if(a==4)n4++; if(n3+2*n4>2)return 0;
   long r=a*q-n; n=q;q=r;}
 return (n3==2&&n4==0)||(n4==1&&n3==0);}
static long maxdigit(long p,long B,int*len){long n=p,q=B,m=0;*len=0;while(q){long a=n/q;if(a>m)m=a;long r=n-a*q;n=q;q=r;(*len)++;}return m;}
int main(int c,char**v){long N=atol(v[1]);char*comp=calloc(N+1,1);
 for(long i=2;i*i<=N;i++)if(!comp[i])for(long j=i*i;j<=N;j+=i)comp[j]=1;
 long np=0,mism=0,mism2=0,totshape=0,totneg=0,zeros=0; double worst=1e9;long worstp=0; long minmaxdig_over_cbrt_p=0;
 for(long p=5;p<=N;p+=4){ if(comp[p])continue; np++;
   /* direct word count: ordered words (v,t,u), t,u,v>=2, tuv-u-v=p ; A=tu-1 */
   long W=0,Wneg=0; for(long t=2;2*t*2-4<=p+0;t++)for(long u=2;t*u*2-u-2<=p;u++){long den=t*u-1;if((p+u)%den==0){long vv=(p+u)/den;if(vv>=2){W++;if(jac(den,p)==-1)Wneg++;}}}
   long S=0,Sneg=0; long best=-1; /* min over certificate B of max regular digit */
   for(long B=1;B<p;B++) if(dualshape(p,B)){S++; if(jac(B,p)==-1){Sneg++; int L; long md=maxdigit(p,B,&L); if(best<0||md<best)best=md;}}
   if(S!=W)mism++; if(Sneg!=Wneg)mism2++; totshape+=S; totneg+=Sneg; if(Sneg==0)zeros++;
   if(best>0&&p>1000){double r=best/cbrt((double)p); if(r<worst){worst=r;worstp=p;}}
 }
 printf("primes p≡1(4), 5<=p<=%ld: %ld primes; shape-B count == word count mismatches: %ld; nonsquare mismatches: %ld\n",N,np,mism,mism2);
 printf("total shape-B %ld, nonsquare %ld (frac %.4f); primes with no nonsquare shape-B: %ld\n",totshape,totneg,(double)totneg/totshape,zeros);
 printf("min over p of [min over certificate B of max regular CF digit of p/B] / p^(1/3) (p>1000) = %.4f at p=%ld\n",worst,worstp);
 return 0;}
