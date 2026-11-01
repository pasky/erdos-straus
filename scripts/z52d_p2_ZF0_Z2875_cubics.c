/* Independent coefficient-grid scan, exact discriminant and root tests. */
#include <stdio.h>
#include <math.h>
#include <assert.h>
typedef long long ll;
int main(void){
 puts("n,e1,e2,e3,discriminant,x,y,z");
 for(ll n=1;n<=100;n++)for(ll s=1;s<=200;s++)for(ll t=1;t<=10000;t++){
  if(n*t%4)continue;ll u=n*t/4;
  ll D=s*s*t*t-4*t*t*t-4*s*s*s*u-27*u*u+18*s*t*u;
  if(D<0)continue;ll q=(ll)sqrt((double)D);while(q*q<D)q++;if(q*q!=D)continue;
  ll x=0,y=0,z=0;
  for(ll r=1;3*r<=s;r++)if(r*r*r-s*r*r+t*r-u==0){
   ll sum=s-r,prod=u/r,disc=sum*sum-4*prod;
   if(disc<0)continue;ll h=(ll)sqrt((double)disc);if(h*h==disc&&(sum-h)%2==0){x=r;y=(sum-h)/2;z=(sum+h)/2;break;}
  }
  if(x)assert(x+y+z==s&&x*y+x*z+y*z==t&&x*y*z==u&&4*x*y*z==n*(x*y+x*z+y*z));
  printf("%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld\n",n,s,t,u,D,x,y,z);
 }
}
