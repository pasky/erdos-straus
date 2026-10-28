/* Exact AP census of two certificate lines. No factorisation assumptions.
   cc -O3 -Wall -Wextra -o /tmp/z48_ltastra_census ... -lm
   Usage: executable N output.csv [24|4]. Memory < 14*N+100 bytes, N <= 10000000.
   MBM_upper is an outward-rounded upper bound, using the product cutoff.
   R counts ordered (u,v,C), B counts (x,y,C) with
   p=4xyC-4x-y, y>=3 odd. Both are sufficient ES lines.
*/
#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>
#include <fenv.h>
static long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
int main(int argc,char **argv){
 if(argc!=3&&argc!=4){fprintf(stderr,"usage: %s N output.csv [24|4]\n",argv[0]);return 2;}
 int modulus=argc==4?atoi(argv[3]):24;
 if(modulus!=4&&modulus!=24)return 2;
 long N=strtol(argv[1],NULL,10);
 if(N<100||N>10000000){fprintf(stderr,"N outside [100,10000000]\n");return 2;}
 uint32_t *R=calloc(N+1,sizeof(*R)),*B=calloc(N+1,sizeof(*B));
 unsigned char *composite=calloc(N+1,1);
 long M=(N+1)/3;
 uint32_t *phi=malloc((M+1)*sizeof(*phi));
 unsigned char *omega=calloc(M+1,1);
 double *upper=calloc(M+1,sizeof(*upper));
 if(!R||!B||!composite||!phi||!omega||!upper){fprintf(stderr,"allocation failed\n");return 2;}
 assert(FLT_RADIX==2&&DBL_MANT_DIG==53&&FLT_EVAL_METHOD==0&&fegetround()==FE_TONEAREST);
 for(long i=1;i<=M;i++)phi[i]=i;
 for(long i=2;i<=M;i++)if(phi[i]==i)for(long j=i;j<=M;j+=i){phi[j]=phi[j]/i*(i-1);omega[j]++;}
 for(long m=1;m<=M;m++){
  upper[m]=upper[m-1];
  if(m%2==0){double w=nextafter((double)(1UL<<omega[m])/(4.0*phi[m]),INFINITY);upper[m]=nextafter(upper[m]+w,INFINITY);}
 }
 for(long i=2;i*i<=N;i++)if(!composite[i])for(long j=i*i;j<=N;j+=i)composite[j]=1;
 for(long u=1;4*u*(u+1)-2*u-1<=N;u++){
  long vmax=(N+u)/(4*u-1);
  for(long v=u+1;v<=vmax;v+=2){
   if(gcdl(u,v)!=1)continue;
   long q=4*u*v;
   for(long n=q-u-v;n<=N;n+=q){assert(R[n]<=UINT32_MAX-2);R[n]+=2;}
  }
 }
 for(long y=3;3*y-4<=N;y+=2){
  long xmax=(N+y)/(4*(y-1));
  for(long x=1;x<=xmax;x++){
   if(gcdl(x,y)!=1)continue;
   long q=4*x*y;
   for(long n=q-4*x-y;n<=N;n+=q){assert(B[n]<UINT32_MAX);B[n]++;}
  }
 }
 FILE *out=fopen(argv[2],"w");if(!out){perror(argv[2]);return 2;}
 fprintf(out,"p,R,B,T,near_square_gap,MBM_upper\n");
 long count=0,zr=0,zb=0,zt=0,squares=0;double min=1e100,minbm=1e100;long arg=0,argbm=0,fail16=0;
 for(long n=3;n<=N;n+=2){
  long root=(long)sqrt((double)n);while((root+1)*(root+1)<=n)root++;
  if(root*root==n){assert(R[n]==0&&B[n]==0);squares++;}
  if(n%modulus!=1||composite[n])continue;
  uint64_t t=(uint64_t)R[n]+B[n];
  double ub=2*upper[(n+1)/3];
  fprintf(out,"%ld,%u,%u,%llu,%ld,%.17g\n",n,R[n],B[n],(unsigned long long)t,n-root*root,ub);
  if(16.0*t<ub)fail16++;
  if(t/ub<minbm){minbm=t/ub;argbm=n;}
  count++;zr+=R[n]==0;zb+=B[n]==0;zt+=t==0;
  double ratio=t/pow(log((double)n),2);if(ratio<min){min=ratio;arg=n;}
 }
 if(fclose(out)!=0){perror("fclose");return 2;}
 fprintf(stderr,"primes=%ld Rzeros=%ld Bzeros=%ld unionzeros=%ld odd_squares=%ld minT/log^2=%.12g at %ld\n",count,zr,zb,zt,squares,min,arg);
 fprintf(stderr,"outward_upper: minT/MBM_upper=%.12g at %ld; failures of T>=MBM_upper/16: %ld\n",minbm,argbm,fail16);
 free(R);free(B);free(composite);free(phi);free(omega);free(upper);return fail16?1:0;
}
