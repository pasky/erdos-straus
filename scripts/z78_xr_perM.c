/* z78 cross-review (Opus): per-shift test of the compression-bound LOGIC used by
   z78_p5.c, z78_p5fine.c, z78_q3.c and z78_p7.c against the EXACT number of
   divisors h | M^2 in the relevant unit class.  The author formulas are
   re-transcribed here from the C sources (they are the objects under test);
   factorisation is my own (trial division + Pollard-Brent + MR).
   Usage: z78_xr_perM mode r emin emax
     mode p5  : N=r^5, M=(N+e)/4, class -M mod e, engines p5.c & p5fine.c
     mode q3e : F=r^3, M=(eF+1)/4, class -M mod e,  engine q3.c (mode 0)
     mode q3f : F=r^3, M=(F+f)/4,  class -1/4 mod f, engine q3.c (mode 1)
     mode p7  : N=r^7 (needs N/4 < 2^64), class -M mod e, engine p7.c
   Only shifts with gcd(M,e)=1 and r!|e are tested (the only ones the lemma covers). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
typedef uint64_t U; typedef __uint128_t Z; typedef int64_t I;
#include "z78_xr_fac.h"
static U dv[1<<20];
static U cnt_class(U M,U e,U cls){ /* exact, via residues mod e and recursion over exponents */
 /* enumerate divisors as residues mod e */
 static U res[1<<20];int nd=1;res[0]=1%e;for(int i=0;i<nfp;i++){int cur=nd;U pw=1;for(int k=0;k<2*fe[i];k++){pw=(Z)pw*(fp[i]%e)%e;for(int j=0;j<cur;j++){assert(nd<(1<<20));res[nd++]=(Z)res[j]*pw%e;}}}
 U c=0;for(int j=0;j<nd;j++)if(res[j]==cls%e)c++;return c;}
static int cmpu(const void*a,const void*b){U x=*(U*)a,y=*(U*)b;return (x>y)-(x<y);}
static U sp[64];static int se[64],ns;
static void sorted(void){ns=nfp;for(int i=0;i<ns;i++){sp[i]=fp[i];se[i]=fe[i];}
 for(int i=0;i<ns;i++)for(int j=i+1;j<ns;j++)if(sp[j]<sp[i]){U t=sp[i];sp[i]=sp[j];sp[j]=t;int s=se[i];se[i]=se[j];se[j]=s;}}
/* z78_p5.c / z78_q3.c per-M cost (primes <=4096 sieved, greedy g<=e, residual 3^floor(log_4097)) */
static U cost_p5(U M,U e){U G=1,c=1,x=1;for(int i=0;i<ns;i++){U p=sp[i];if(p>4096){for(int k=0;k<se[i];k++)x*=p;continue;}int h=0;for(int k=0;k<se[i];k++){if(G*p<=e)G*=p;else h++;}c*=2*h+1;}
 U h=x;if(h<=e/G){G*=h;h=1;}U m=1;for(U u=h;u>1;u/=4097){if(u<4097)break;m*=3;}return c*m*(G<=e/G?1:2);}
static U q3cost(U M,U e){U G=1,c=1,x=1;for(int i=0;i<ns;i++){U p=sp[i];if(p>4096){for(int k=0;k<se[i];k++)x*=p;continue;}int h=0;for(int k=0;k<se[i];k++){if(G*p<=e)G*=p;else h++;}c*=2*h+1;}
 U h=x,GG=G;if(h<=e/GG){GG*=h;h=1;}for(;h>=4097;h/=4097)c*=3;return c*(GG<=e/GG?1:2);}
/* z78_p5fine.c test/run */
static U test(U g,U y,U e,U M){ if(e==1)return y==1?1:3; U G=g*g;if(y==1){U t=e-g; return t<=g&&G%t==0?2:0;}
 U t=e-M%e;U left=t<=g&&G%t==0; U a=(G<=e ? (t<=G&&G%t==0) : left+1); U mid=e-g;return 2*a+2*(mid<=g&&G%mid==0);}
static U run(U e,U M,int rev){U g=1,c=1;for(int z=0;z<ns;z++){int i=rev?ns-z-1:z;U q=sp[i];int h=se[i];for(;h&&q<=e/g;h--)g*=q;c*=2*h+1;}
 if(c<=3)return test(g,M/g,e,M); return c*(g<=e/g?1:2);}
/* z78_p7.c per-M */
static U r4;
static U cost_p7(U M,U e){U g=1,g2=1,cost=1;for(int i=0;i<ns;i++){U p=sp[i];if(p>4096)continue;for(int k=0;k<se[i];k++){if(g<=e/p)g*=p;else if(cost<r4)cost*=3;if(g2<=((U)1<<63)/p)g2*=p;}}
 U G=g,c=cost;U X=M/g2;if(X<=e/G){G=e;X=1;}int f=0;Z t=4097;while(t<=X){f++;t*=4097;}for(int v=0;v<f&&c<r4;v++)c*=3;c*=G<=e/G?1:2;return c;}
int main(int argc,char**argv){assert(argc==5);char*mode=argv[1];U r=atoll(argv[2]),e0=atoll(argv[3]),e1=atoll(argv[4]);r4=r*r*r*r;
 U F=r*r*r;Z N5=(Z)F*r*r,N7=N5*r*r;U tested=0,v1=0,v2=0,v3=0,sx=0,s1=0,s2=0,worst=0;
 for(U e=e0;e<e1;e++){U M,cls;
  if(!strcmp(mode,"p5")){if((N5+e)%4)continue;M=(U)((N5+e)/4);}
  else if(!strcmp(mode,"p7")){if((N7+e)%4)continue;assert((N7+e)/4<((Z)1<<64));M=(U)((N7+e)/4);}
  else if(!strcmp(mode,"q3e")){if(((Z)e*F+1)%4)continue;M=(U)(((Z)e*F+1)/4);}
  else {if((F+e)%4)continue;M=(F+e)/4;}
  if(e%r==0||gcdu(M,e)!=1)continue;
  if(!strcmp(mode,"q3f")){ /* class -1/4 mod f */ U inv4=1;while((4*inv4)%e!=1%e)inv4++; cls=(e-inv4%e)%e; if(e==1)cls=0;}
  else cls=(e-M%e)%e;
  factor(M);sorted();U ex=cnt_class(M,e,cls);tested++;sx+=ex;
  U b1,b2=0;
  if(!strcmp(mode,"p5")){b1=cost_p5(M,e);U x=run(e,M,0),y=run(e,M,1);b2=x<y?x:y;if(b2<ex){v2++;if(v2<10)printf("VIOL p5fine e=%lu M=%lu exact=%lu bound=%lu\n",e,M,ex,b2);}}
  else if(!strcmp(mode,"p7"))b1=cost_p7(M,e);
  else b1=q3cost(M,e);
  if(b1<ex){v1++;if(v1<10)printf("VIOL %s e=%lu M=%lu exact=%lu bound=%lu\n",mode,e,M,ex,b1);}
  s1+=b1;s2+=b2;if(ex>worst)worst=ex;}
 printf("%s r=%lu e in [%lu,%lu): tested %lu  sum_exact %lu  sum_bound %lu violations %lu",mode,r,e0,e1,tested,sx,s1,v1);
 if(!strcmp(mode,"p5"))printf("  p5fine_sum %lu p5fine_violations %lu",s2,v2);printf("  max_exact %lu\n",worst);return 0;}
