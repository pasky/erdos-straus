/* Designed witnesses beyond exhaustive count ranges. No zero output: 0 = UNKNOWN.
   Five labelled panels. MR uses first 12 prime bases, deterministic on uint64_t.
   A witness field is f; all the coordinates are recovered from n,f (see note). */
#include <stdint.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <limits.h>
typedef uint64_t U;
typedef __uint128_t W;
static const unsigned q[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
static U state=975031;
static U rand64(void){state^=state<<13;state^=state>>7;return state^=state<<17;}
static U powm(U a,U e,U m){U r=1;while(e){if(e&1)r=(W)a*r%m;a=(W)a*a%m;e>>=1;}return r;}
static int prime(U n){if(n<2)return 0;for(int i=0;i<12;i++)if(n%q[i]==0)return n==q[i];
 U d=n-1;int s=0;while(!(d&1)){d/=2;s++;}for(int i=0;i<12;i++){
 U x=powm(q[i],d,n);if(x==1||x==n-1)continue;int j=1;for(;j<s;j++){x=(W)x*x%n;if(x==n-1)break;}if(j==s)return 0;}return 1;}
static U gcd(U a,U b){while(b){U t=a%b;a=b;b=t;}return a;}
static int sqto31(U n){for(int i=1;q[i]<=31;i++)if(powm(n%q[i],q[i]/2,q[i])!=1)return 0;return 1;}
static void witness(char label,U n,U m,U s){assert(n>=100000000000000000ULL&&n<8000000000000000000ULL);
 unsigned R=0,A=0,Z=0,T=0,E=0;
 for(unsigned f=3;f<=5000003;f++){unsigned r=f-n%f;if((f+1)%r)continue;
 if((f&3)==3){if(!R&&((f+1)/4)%r==0)R=f;if(!A&&(r==1||r%4==0))A=f;
 if((f&7)==7){if(!Z)Z=f;if(!E&&((f+1)/8)%r==0)E=f;}}
 if(!T&&r>=2){U t=(f+1)/r,b=(n+r)/f;if(t>=2&&b>=2&&(((n+t)%8)*(t%8)*(r%8)*(b%8))%8==0)T=f;}
 if(R&&A&&Z&&T&&E)break;}
 printf("%c %"PRIu64" %"PRIu64" %"PRIu64" %u %u %u %u %u\n",label,n,m,s,R,A,Z,T,E);}
int main(void){const U M=120120,lo=100000000000000000ULL,hi=8000000000000000000ULL;
 puts("# panel n param1 param2 f_R f_A f_U7 f_S f_R8 (0=UNK)");
 for(int l=0;l<5;l++){int made=0;while(made<(l==1?120:1000)){U n,m,s;
 if(l==0){/* p-1 is 97-smooth; square shadows at all odd primes through 31 */
 m=M;s=0;while(m<lo){U t=q[rand64()%25];if((W)m*t>=hi){m=0;break;}m*=t;}if(!m)continue;n=m+1;
 if(!sqto31(n)||!prime(n))continue;}
 else if(l==1){/* n=m^2+t^2-1 kills u=1. Cofactor (4n+1)/5 prime also kills C=1. */
 m=M*(2633+rand64()%12000)+1;U t=M*(1+rand64()%8000)+1;s=t*t-1;n=m*m+s;
 if(n<lo||n>UINT64_MAX/4||gcd(m,t)!=1||!sqto31(n)||!prime(n)||!prime((4*n+1)/5)||!prime((n+3)/4))continue;}
 else if(l==4){/* new zero-prime kernels, all in M, force gcd(n,105)=1 */
 static const U z[]={25606400401ULL,25277866681ULL,37165786681ULL,179530327201ULL,452438542081ULL};
 s=z[rand64()%5];m=11*(2*(rand64()%6000)+1);W v=(W)m*m*s;
 if(v<lo||v>=hi||gcd(m,105)!=1)continue;n=(U)v;}
 else {static const U kern[]={105,4545,505,29210401,8813281,17401609,752257,1969,577,23881};
 s=kern[rand64()%10];m=(l==2?15015:1001)*(2*(rand64()%150000)+1);W v=(W)m*m*s;if(v<lo||v>=hi)continue;n=(U)v;}
 witness("HNDCK"[l],n,m,s);made++;}}
}
