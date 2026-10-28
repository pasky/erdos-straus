/* Full pair/genus diagnostics, and bounded-modulus positive character kernels.
   stdin: n=1 mod4, 5<=n<=10000000. No primality assumption in computation.
   M_k^Q projects onto characters chi^k=1 for q<=65536 (k=2,6,12,60).
   Memory < 10*(max(n)/3+4) bytes. Every hit is checked against BM/genus.
*/
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
static int *spf,*phi;static signed char *chi;
static long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
static int jac(long a,long n){int s=1;a%=n;if(a<0)a+=n;while(a){while(!(a&1)){a/=2;if(n%8==3||n%8==5)s=-s;}long t=a;a=n;n=t;if(a%4==3&&n%4==3)s=-s;a%=n;}return n==1?s:0;}
static long power(long a,long e,long q){long r=1;while(e){if(e&1)r=r*a%q;a=a*a%q;e/=2;}return r;}
static double kernel(long n,long u,long v,long ph,int k){
 long parts[2]={u,v};int e2=2;long idx=1;
 for(int j=0;j<2;j++)while(parts[j]%2==0){parts[j]/=2;e2++;}
 int vk=0;for(int t=k;t%2==0;t/=2)vk++;
 int e=e2<vk+2?e2:vk+2;long two=1L<<e;
 if((n+u+v)%two)return 0;
 idx=1L<<(e-1);
 for(int j=0;j<2;j++)while(parts[j]>1){long l=spf[parts[j]],pe=1;
  while(parts[j]%l==0){parts[j]/=l;pe*=l;}
  long phl=pe/l*(l-1),d=gcdl(k,phl),a=(pe-(u+v)%pe)%pe;
  if(power(n%pe,phl/d,pe)!=power(a,phl/d,pe))return 0;
  idx*=d;
 }
 return (double)idx/ph;
}
int main(void){
 long ns[4096],nmax=0;int nn=0;
 while(nn<4096&&scanf("%ld",&ns[nn])==1){if(ns[nn]<5||ns[nn]>10000000||ns[nn]%4!=1)return 2;if(ns[nn]>nmax)nmax=ns[nn];nn++;}
 if(nn==4096){long extra;if(scanf("%ld",&extra)==1){fprintf(stderr,"too many inputs\n");return 2;}}
 if(!nn)return 2;
 long N=(nmax+1)/3+2;
 spf=calloc(N+1,sizeof(*spf));phi=calloc(N+1,sizeof(*phi));chi=calloc(N+1,sizeof(*chi));if(!spf||!phi||!chi)return 2;
 phi[1]=1;
 for(long i=2;i<=N;i++)if(!spf[i])for(long j=i;j<=N;j+=i)if(!spf[j])spf[j]=i;
 for(long i=2;i<=N;i++){long l=spf[i],r=i/l;phi[i]=phi[r]*(r%l?l-1:l);}
 puts("n,R,npairs,M0,MBM,Mgen,Rsmall,M2small,M6small,M12small,M60small,cs_pair_bound");
 const int ks[4]={2,6,12,60};
 for(int z=0;z<nn;z++){
  long n=ns[z],max=(n+1)/3;chi[1]=1;
  for(long i=2;i<=max;i++){long l=spf[i];chi[i]=i==l?jac(i,n):chi[l]*chi[i/l];}
  double M0=0,MBM=0,Mg=0,mk[4]={0},cs=0;long R=0,np=0,Rs=0;
  for(long u=1;4*u*(u+1)-2*u-1<=n;u++){
   long vmax=(n+u)/(4*u-1);
   for(long v=u+1;v<=vmax;v+=2){
    if(gcdl(u,v)!=1||!chi[u]||!chi[v])continue;
    long q=4*u*v,ph=4L*phi[u]*phi[v],s=4;int match=(n+u+v)%8==0;
    long parts[2]={u,v};
    for(int j=0;j<2;j++){
     long a=parts[j],other=parts[1-j];while(a%2==0)a/=2;
     while(a>1){long l=spf[a];s*=2;if(match&&chi[l]*jac(-other,l)!=1)match=0;while(a%l==0)a/=l;}
    }
    int hit=(n+u+v)%q==0;np+=2;R+=2*hit;
    M0+=2.0/ph;MBM+=2.0*(1-chi[u]*chi[v])/ph;if(match)Mg+=2.0*s/ph;
    cs+=2.0*(ph-s)/ph;
    if(hit)assert(match&&chi[u]*chi[v]==-1);
    if(q<=65536){Rs+=2*hit;for(int j=0;j<4;j++)mk[j]+=2*kernel(n,u,v,ph,ks[j]);}
   }
  }
  printf("%ld,%ld,%ld,%.12g,%.12g,%.12g,%ld,%.12g,%.12g,%.12g,%.12g,%.12g\n",n,R,np,M0,MBM,Mg,Rs,mk[0],mk[1],mk[2],mk[3],cs);
  fflush(stdout);
 }
 free(spf);free(phi);free(chi);return 0;
}
