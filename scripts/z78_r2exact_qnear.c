/* Exact nearest-Q search for the 17-adic point 5, adapted from the
 * pointwise Q divisor reconstruction but with reduced congruence modulus U.
 * For Q level k, F=17^k remains the equation modulus while U=17^j controls
 * the point congruence. Every positive lift of a,d modulo U with
 * ad <= (F+1)/2 is visited. */
#include <assert.h>
#include <stdint.h>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
#include <stdio.h>
#include <stdlib.h>
typedef uint64_t u64; typedef __uint128_t u128; typedef __int128 i128;
static u64 F,U,WT; static int k,j,orient; static u64 npairs,nhits;
static u64 inv(u64 x,u64 m){i128 a=x%m,b=m,s=1,t=0;while(b){i128 q=a/b,r=a-q*b;a=b;b=r;r=s-q*t;s=t;t=r;}assert(a==1);s%=m;if(s<0)s+=m;return (u64)s;}
static u64 mmF(u64 x,u64 y){return (u64)((u128)x*y%F);}
static u64 mmU(u64 x,u64 y){return (u64)((u128)x*y%U);}
static u64 powU(u64 a,u64 e){u64 x=1;while(e){if(e&1)x=mmU(x,a);a=mmU(a,a);e>>=1;}return x;}
static u64 sqrtU(u64 y){u64 r=0;for(u64 x=1;x<17;x++)if(x*x%17==y%17){r=x;break;}if(!r)return 0;u64 inv2r=inv(2*r%U,U);for(int n=1;n<j;n++){u64 diff=(mmU(r,r)+U-y)%U;r=(r+U-mmU(diff,inv2r))%U;}if(mmU(r,r)!=y%U){fprintf(stderr,"sqrt check failed\n");exit(4);}return r;}
static cpp_int bigu(u128 x){cpp_int z=(u64)(x>>64);z<<=64;z+=(u64)x;return z;}
static u64 vp17(cpp_int x){u64 n=0;while(x%17==0){x/=17;n++;}return n;}
static void print128(u128 x){char b[64];int n=0;do{b[n++]='0'+x%10;x/=10;}while(x);while(n)putchar(b[--n]);}
static void pair(u64 a,u64 d){
 npairs++; if((u128)a*d>(F+1)/2)return;
 u128 t=(u128)4*a*a*d+1,s=(u128)4*a*d;
 u128 fs[2];int nf=0;u128 f0=s-(u128)F%s;fs[nf++]=f0;
 u64 s64=(u64)s,neg=(u64)(s-(u128)F%s);u64 ni=inv(neg,s64);
 u64 r2=(u64)((t%s)*ni%s);if(r2&&t%r2==0)fs[nf++]=t/r2;
 for(int h=0;h<nf;h++){
  if(h==1&&fs[0]==fs[1])continue;
  u128 f=fs[h];if(!f||t%f||(f+F)%s)continue;u128 c=(f+F)/s,num=(u128)F*a+c;if(num%f)continue;u128 b=num/f;
  if(b<a||(a+b)%c)continue;u128 e=(a+b)/c;
  if(e%17==0||4*(u128)a*b*c*d!=(u128)F*(a+b)+c)continue;
  if(((u128)4*a*a*d)%U!=WT)continue;
  /* The second oriented search uses 4a^2d == -1/5 mod U, which is
     equivalent by (4abd)^2 == 1 mod U to 4b^2d == -5 mod U. */
  u128 val=orient==0?(u128)4*a*a*d+5:(u128)4*b*b*d+5;
  if(val%U)continue;nhits++;
  printf("HIT k=%d j=%d orientation=%c a=",k,j,orient?'b':'a');print128(a);printf(" b=");print128(b);printf(" c=");print128(c);printf(" d=");print128(d);printf(" e=");print128(e);
  printf(" v17(4a^2d+5)=%llu v17(4b^2d+5)=%llu\n",(unsigned long long)vp17(bigu((u128)4*a*a*d+5)),(unsigned long long)vp17(4*bigu(b)*bigu(b)*d+5));
 }
}
static void search_one(u64 w){
 u64 lim=(F+1)/2,H=1;while((u128)(H+1)*(H+1)<=lim)H++;
 /* Complete small-a half: d=d0+nU, all positive lifts. */
 for(u64 a=1;a<=H;a++)if(a%17){u64 aa=mmU(a%U,a%U),d0=mmU(w,inv(mmU(4%U,aa),U));if(!d0)continue;
  for(u128 d=d0;d<=lim/a;d+=U)if((u64)d%17)pair(a,(u64)d);}
 /* Complement: d<=H and a is either Hensel root modulo U plus every lift. */
 for(u64 d=1;d<=H;d++)if(d%17){u64 y=mmU(w,inv(mmU(4%U,d%U),U)),r=sqrtU(y);if(!r)continue;u64 roots[2]={r,U-r};
  for(int z=0;z<2;z++){if(z&&roots[z]==roots[0])continue;u64 a0=roots[z];if(!a0)continue;
   u128 first=a0;if(first<=H)first+=(u128)(((H-first)/U)+1)*U;
   for(u128 a=first;a<=lim/d;a+=U)if((u64)a%17)pair((u64)a,d);
  }
 }
}
int main(int argc,char**argv){if(argc<2||argc>3)return 1;k=atoi(argv[1]);if(k<1||k>11||!(k&1))return 2;int jmin=argc==3?atoi(argv[2]):1;if(jmin<1||jmin>k)return 2;F=1;for(int i=0;i<k;i++)F*=17;
 for(orient=0;orient<2;orient++){
  u64 wk=orient?inv(F-5,F):F-5; /* w=-5 or -1/5 mod F */
  for(j=k;j>=jmin;j--){U=1;for(int i=0;i<j;i++)U*=17;npairs=nhits=0;
   /* Reduce the target from the full equation modulus. */
   WT=wk%U;search_one(WT);
   fprintf(stderr,"k=%d orientation=%c j=%d pairs=%llu hits=%llu\n",k,orient?'b':'a',j,(unsigned long long)npairs,(unsigned long long)nhits);
   if(nhits)break;
  }
  if(nhits)printf("MAX k=%d orientation=%c valuation=%d\n",k,orient?'b':'a',j);
  else if(jmin==1)printf("MAX k=%d orientation=%c valuation=0 (no Q datum even mod 17)\n",k,orient?'b':'a');
  else printf("NO_HIT k=%d orientation=%c j>=%d; maximum valuation <=%d\n",k,orient?'b':'a',jmin,jmin-1);
 }
 return 0;
}
