/* Exact local coefficients at growing primorial; floating-point sums only.
   Count ordered normalized (a,c,d), gcd(a,c)=1, m=4acd-1<=10^6. */
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#define T 1000000
static int phi[T+1], sp[T+1], g[T+1];
static int gcd(int a,int b){while(b){int r=a%b;a=b;b=r;}return a;}
int main(void){
 int bs[]={1,7,43,313,1259};
 for(int i=1;i<=T;i++)phi[i]=i;
 for(int q=2;q<=T;q++)if(!sp[q]) for(int i=q;i<=T;i+=q){sp[i]=q;phi[i]-=phi[i]/q;}
 puts("B Tmax family base surviving_base conditioned nonrough_conditioned");
 for(size_t s=0;s<sizeof(bs)/sizeof(*bs);s++){
 int B=bs[s];g[1]=1;
 for(int i=2;i<=T;i++){int q=sp[i];g[i]=g[i/q]*((i/q)%q && q<=B?q:1);}
 double sums[3][2][4]={0};
 for(int a=1;a<=(T+1)/4;a++)for(int c=1;c<=(T+1)/(4*a);c++){
 if(gcd(a,c)>1)continue;
 for(int m=4*a*c-1;m<=T;m+=4*a*c){
 int ok=((a+c)%g[m]==0), z=(m>1000)+(m>50000);
 double u=1.0/phi[m],v=ok?phi[g[m]]*u:0;
 for(int j=0;j<=!!(c==1);j++){
 sums[z][j][0]+=u;sums[z][j][1]+=ok*u;sums[z][j][2]+=v;
 if(g[m]!=1)sums[z][j][3]+=v;
 }
 }}
 for(int z=0;z<3;z++)for(int j=0;j<=1;j++){
 printf("%d %d %s",B,(int[]){1000,50000,T}[z],j?"star":"II2");
 for(int k=0;k<4;k++){if(z)sums[z][j][k]+=sums[z-1][j][k];printf(" %.9f",sums[z][j][k]);}
 puts("");
 }}
 return 0;
}
