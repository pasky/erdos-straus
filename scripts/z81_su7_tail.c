/* Stream the three-menu product at every f<=2B+1. No duplicate-large-q
   issues here: q>7 has at most one c in {1,3,5}. O(B) bits sieve. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <string.h>
static unsigned char *bad;static uint16_t *spf;
static int comp(uint32_t q){return bad[q>>4]&(1u<<((q>>1)&7));}
static void mark(uint32_t q){bad[q>>4]|=1u<<((q>>1)&7);}
static int tab[2048];
static int divisors(uint32_t x){int s=1;tab[0]=1;while(x>1){uint32_t l=spf[x];if(!l)l=x;int old=s;uint32_t a=1;
 do{a*=l;x/=l;for(int j=0;j<old;j++){assert(s<2048);tab[s++]=a*tab[j];}}while(x%l==0);}return s;}
int main(int argc,char**argv){assert(argc==2);int B=atoi(argv[1]);assert(B>=17 && B<=1000000000);uint32_t F=2u*B+1,N=(F+1)/8;
 bad=calloc(F/16+1,1);spf=calloc(N+1,sizeof(uint16_t));assert(spf&&bad);mark(1);
 for(uint32_t l=3;l<=F/l;l+=2)if(!comp(l))for(uint32_t n=l*l;n<=F;n+=2*l)mark(n);
 for(uint32_t l=2;l<=N/l;l++)if(l==2||(l%2&&!comp(l)))for(uint32_t n=l*l;n<=N;n+=l)if(!spf[n])spf[n]=l;
 // To avoid accumulating billions of O(epsilon) absolute summand errors,
 // store separate log products per class. Monotone blocks bound sum over p.
 long double lg[6][5]={{0}},Elo=0,Ehi=0,prev=1,P=1;int small7=0,small15=0;
 uint32_t counts=0,prevB=0,cur=1,f=7;
 for(;;){for(;f<=2*cur+1;f+=8){int c=0;if(!comp(f))c=1;else if(f%3==0&&!comp(f/3))c=3;else if(f%5==0&&!comp(f/5))c=5;
   if(!c)continue;if(f==7){small7=1;continue;}if(f==15){small15=1;continue;}uint32_t q=f/c;
   uint32_t i=(f+1)/8,pow2=8;while(i%2==0){i/=2;pow2*=2;}int s=divisors(i),hits[5]={0};
   for(int j=0;j<s;j++)for(uint32_t t=1;t<=pow2;t*=2){uint32_t r=tab[j]*t;if(r>=f)continue;hits[r%c]++;}
   // Store by r residue, condition p = -r mod c.
   for(int a=0;a<c;a++)if(c==1||a)lg[c][a]+=log1pl(-(long double)hits[a]/(q-1));
  }
  uint32_t cnt=0;for(uint32_t p=(prevB/8)*8+1;p<=cur;p+=8)if(p>prevB && !comp(p))++cnt;counts+=cnt;
  P=0;int na=0;for(int a=1;a<105;a++)if(a%3&&a%5&&a%7){na++;int r7=7-a%7,r15=15-a%15;if((small7&&8%r7==0)||(small15&&16%r15==0))continue;
   P+=expl(lg[1][0]+lg[3][3-a%3]+lg[5][5-a%5]);}P/=na;
  Elo+=cnt*P;Ehi+=cnt*prev;
  if(cur==B||cur==1000000)printf("B=%u primes=%u P3=%.13Lg E3_bounds=%.9Lf %.9Lf\n",cur,counts,P,Elo,Ehi);
  if(cur==B)break;prev=P;prevB=cur;cur+=1+cur/4;if(cur>(uint32_t)B)cur=B;
 }free(bad);free(spf);}
