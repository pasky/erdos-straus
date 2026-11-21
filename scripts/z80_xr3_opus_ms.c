/* Opus R3 independent (MS+_105) replay on [LO,HI]  (hostile review of EXTREME.md §13).
   Claim tested: every nonsquare n = 1 mod 4, gcd(n,105)=1 in [LO,HI] has
   n = 4*c*u*b - u - b with c,u,b >= 1.  Equivalent: some d = 4cu-1 with n = -u mod d
   (then b=(n+u)/d >= 1).
   Design (independent of z75 engines): n = 5 mod 12 uses (c,u)=(1,1), d=3 (checked
   by explicit identity on every such n via the class bookkeeping below);
   n = 1 mod 12 is split into its 48 classes r mod 840 coprime to 105; in each class
   AP n=840 i + r we sieve, per (d,u) pair with d<=DS, via CRT offset (offset checked
   explicitly at first hit). Survivors: minimal-d search, witness verified in
   128-bit arithmetic.  Also: second-stage comparison data
   (survivors with minimal d > 80000 and no pair-family hit t<=20000).
   Usage: prog LO HI DS */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long I; typedef unsigned __int128 W;
static I g_(I a,I b){while(b){I t=a%b;a=b;b=t;}return a;}
static I inv(I a,I m){I t=m,x=1,y=0;a%=m;while(t){I q=a/t,r=a-q*t,z=x-q*y;a=t;t=r;x=y;y=z;}assert(a==1);return ((x%m)+m)%m;}
static int isM(I n){int r=n%840;return r==1||r==121||r==169||r==289||r==361||r==529;}
static int issq(I n){I s=(I)sqrtl((long double)n);while(s*s>n)s--;while((s+1)*(s+1)<=n)s++;return s*s==n;}
#define SEG (1<<20)
static unsigned char seg[SEG];
typedef struct{I d,u,step,next;int ok;}P;
int main(int argc,char**argv){assert(argc==4);I LO=atoll(argv[1]),HI=atoll(argv[2]),DS=atoll(argv[3]);
 assert(LO>1000&&HI>=LO&&DS>=3&&DS%4==3);
 int np=0;P*pr=malloc(sizeof(P)*4000000);
 for(I d=3;d<=DS;d+=4){I k=(d+1)/4;for(I u=1;u<=k;u++)if(k%u==0){pr[np].d=d;pr[np].u=u;np++;}}
 /* n = 5 mod 12 eligible counts (all trivially represented by d=3,u=1) */
 I cnt5[2]={0,0};
 I cntM=0,cntN=0,sqM=0,sqN=0,surv=0,survsq=0,maxd=0,argd=0,unk=0,late2[2]={0,0},maxlate2[2]={0,0},arglate2[2]={0,0};
 I survM=0;
 /* pair family (comp-engine style comparison only): t<=20000, u|t, n = -u-t/u mod 4t */
 int nq=0;I*qm=malloc(sizeof(I)*400000),*qr=malloc(sizeof(I)*400000);
 for(I t=1;t<=20000;t++)for(I u=1;u*u<=t;u++)if(t%u==0){qm[nq]=4*t;qr[nq]=((-(u+t/u))%(4*t)+4*t)%(4*t);nq++;}
 for(int r=1;r<840;r+=4){ if(g_(r,105)!=1)continue;
  I i0=(LO-r+839)/840; if(LO<=r)i0=0; I i1=(HI-r)/840; if(i1<i0)continue; I len=i1-i0+1;
  if(r%12==5){ for(I i=i0;i<=i1;i++){I n=840*i+r; assert((n+1)%3==0); W b=(n+1)/3; assert((I)(4*b-1-b)==n);}
     /* squares are never 5 mod 12? squares mod 4 are 0,1 and mod 3 are 0,1: n=2 mod3 nonsquare */
     cnt5[isM(r)]+=len; continue; }
  /* class r = 1 mod 12 */
  for(int k=0;k<np;k++){I d=pr[k].d,u=pr[k].u,g=g_(840,d);I target=((-u-r-840*i0)%d+d)%d; /* want 840*j = target mod d, j=i-i0 */
    if(target%g){pr[k].ok=0;continue;} I m=d/g; I j=((target/g)%m)*inv((840/g)%m==0?1:(840/g)%m,m)%m; if(m==1)j=0;
    pr[k].ok=1;pr[k].step=m;pr[k].next=j;
    if(j<len){I n=840*(i0+j)+r; assert((n+u)%d==0);} }
  for(I s=0;s<len;s+=SEG){I L=len-s<SEG?len-s:SEG;memset(seg,0,L);
   for(int k=0;k<np;k++){if(!pr[k].ok)continue;I h=pr[k].next-s;I st=pr[k].step;for(;h<L;h+=st)seg[h]=1;pr[k].next=h+s;}
   for(I j=0;j<L;j++){I n=840*(i0+s+j)+r;int M=isM(n);
     if(M)cntM++;else cntN++;
     if(seg[j])continue;
     if(issq(n)){survsq++; continue;}
     surv++; if(M)survM++;
     I d;for(d=DS+4;d<=2000000003LL;d+=4){I u=d-n%d;if(((d+1)/4)%u==0)break;}
     if(d>2000000003LL){unk++;printf("UNKNOWN %lld\n",n);continue;}
     {I u=d-n%d;W c=(d+1)/(4*u),b=((W)n+u)/d; assert(4*c*u*b-u-b==(W)n);}
     if(d>maxd){maxd=d;argd=n;}
     if(d>80000){int hit=0;for(int q=0;q<nq;q++)if(n%qm[q]==qr[q]){hit=1;break;}
       if(!hit){late2[M]++; if(d>maxlate2[M]){maxlate2[M]=d;arglate2[M]=n;}}}
   }}
 }
 for(I q=(I)sqrtl((long double)LO)-2;q*q<=HI;q++){if(q<1||q*q<LO)continue;I n=q*q;if(n%4==1&&g_(n,105)==1){assert(n%12==1);if(isM(n))sqM++;else sqN++;}}
 cntM-=sqM;cntN-=sqN;
 printf("LO %lld HI %lld DS %lld\n",LO,HI,DS);
 printf("eligible_nonsquare nonM %lld M %lld (5mod12 nonM %lld M %lld; 1mod12 nonM %lld M %lld)\n",cntN+cnt5[0],cntM+cnt5[1],cnt5[0],cnt5[1],cntN,cntM);
 printf("1mod12 survivors_of_d<=DS nonsquare %lld (M %lld) surviving_squares %lld; all eligible-class squares M %lld nonM %lld\n",surv,survM,survsq,sqM,sqN);
 printf("max minimal d among survivors %lld at n %lld; unknown %lld\n",maxd,argd,unk);
 printf("comp-style late (min d>80000, no pair t<=20000): nonM %lld maxd %lld n %lld | M %lld maxd %lld n %lld\n",late2[0],maxlate2[0],arglate2[0],late2[1],maxlate2[1],arglate2[1]);
 return unk!=0;}
