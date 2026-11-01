/* U(n) = #{x<=y<=z : 4/n = 1/x+1/y+1/z}  (A192787), via divisors of b^2 for 1/y+1/z = a/b.
   usage: ucount n1 n2 ...   (n <= 2e6) */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int fac(u64 n,u64*p,int*e){int k=0;for(u64 d=2;d*d<=n;d+=(d==2?1:2)){if(n%d==0){p[k]=d;e[k]=0;while(n%d==0){n/=d;e[k]++;}k++;}}if(n>1){p[k]=n;e[k]=1;k++;}return k;}
static u64 divs[2000000];
u64 U(u64 n){
  u64 pn[64],px[64],pp[128];int en[64],ex[64],ep[128];int kn=fac(n,pn,en);u64 cnt=0;
  for(u64 x=n/4+1;x<=3*n/4;x++){
    u64 a=4*x-n,b=n*x,g=gcd(a,b);a/=g;b/=g;
    int kx=fac(x,px,ex),k=0;
    for(int i=0;i<kn;i++)pp[k++]=pn[i];
    for(int i=0;i<kx;i++){int dup=0;for(int j=0;j<kn;j++)if(pn[j]==px[i])dup=1;if(!dup)pp[k++]=px[i];}
    int m=0;u64 bb=b;
    for(int i=0;i<k;i++){int e=0;while(bb%pp[i]==0){bb/=pp[i];e++;}if(e){pp[m]=pp[i];ep[m]=2*e;m++;}}
    long nd=1;divs[0]=1;
    for(int i=0;i<m;i++){long cur=nd;u64 pw=1;for(int t=1;t<=ep[i];t++){pw*=pp[i];for(long j=0;j<cur;j++){u128 v=(u128)divs[j]*pw;if(v<=b)divs[nd++]=(u64)v;}}}
    for(long j=0;j<nd;j++){u64 d=divs[j];if((d+b)%a==0&&(d+b)/a>=x)cnt++;}
  }
  return cnt;
}
int main(int c,char**v){for(int i=1;i<c;i++){u64 n=strtoull(v[i],0,10);printf("%llu %llu\n",n,U(n));fflush(stdout);}return 0;}
