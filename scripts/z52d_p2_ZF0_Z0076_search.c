#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef long long I;
int main(int argc,char**argv){int B=argc>1?atoi(argv[1]):10000; int a[30000],b[30000],K=0;
for(int x=1;x*x<=B;x++)for(int y=-x;y<=x;y++)if(5*y*y<=x*x&&x*x+5*y*y<=B){a[K]=x;b[K++]=y;}
printf("{\"norm_bound\":%d,\"elements\":%d,\"rows\":[",B,K);int comma=0;
for(int p=3;p<=1000;p+=2){int prime=1;for(int j=2;j*j<=p;j++)if(p%j==0)prime=0;if(!prime||!(p%20==1||p%20==9||p%20==3||p%20==7))continue;
I cnt=0,irr=0;int ex[6]={0};
if(9LL*p*p<=32LL*B)for(int i=0;i<K;i++)for(int j=i;j<K;j++){
I u=(I)a[i]*a[j]-5LL*b[i]*b[j],v=(I)a[i]*b[j]+(I)b[i]*a[j];
I e=4*u-p*(a[i]+a[j]),f=4*v-p*(b[i]+b[j]),N=e*e+5*f*f;if(!N)continue;
I za=p*(u*e+5*v*f),zb=p*(v*e-u*f);if(za%N||zb%N)continue;I x=za/N,y=zb/N;
if(x<a[j]||(x==a[j]&&y<b[j])||x<=0||x*x+5*y*y>B||5*y*y>x*x)continue;
cnt++;if(b[i]||b[j]||y){irr++;if(irr==1){ex[0]=a[i];ex[1]=b[i];ex[2]=a[j];ex[3]=b[j];ex[4]=x;ex[5]=y;}}
}
printf("%s{\"p\":%d,\"principal\":%s,\"count\":%lld,\"nonrational\":%lld,\"example\":[%d,%d,%d,%d,%d,%d]}",comma++?",":"",p,(p%20==1||p%20==9)?"true":"false",cnt,irr,ex[0],ex[1],ex[2],ex[3],ex[4],ex[5]);
}puts("]}");}
