/* Streaming bounded-endpoint census; uint128 prevents modular overflow. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <string.h>
typedef uint64_t U;
static U mul(U a,U b,U m){return (__uint128_t)a*b%m;}
static U power(U a,U b,U m){U r=1;for(;b;b>>=1,a=mul(a,a,m))if(b&1)r=mul(r,a,m);return r;}
static int prime(U n){
 U small[]={2,3,5,7,11,13,17,19,23,29,31,37};
 if(n<2)return 0;
 for(unsigned i=0;i<12;i++){if(n==small[i])return 1;if(n%small[i]==0)return 0;}
 U d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
 U bases[]={2,325,9375,28178,450775,9780504,1795265022};
 for(unsigned i=0;i<7;i++) {U a=bases[i]%n;if(!a)continue;U x=power(a,d,n);if(x==1||x==n-1)continue;int j;for(j=1;j<s;j++){x=mul(x,x,n);if(x==n-1)break;}if(j==s)return 0;}
 return 1;
}
static U nr(U p){for(U a=2;;a++)if(power(a,(p-1)/2,p)==p-1)return a;}
typedef enum { HIT, CENSORED } Status;
typedef struct { Status status; U h,u,t; } Result;
static U cap=1000000, evaluated=0, censored=0;
static Result h4(U p){
 evaluated++;
 for(U v=2;v<=cap && v<=p+2;v++){
  U r=(v-p%v)%v;if(!r)continue;U q=p/v+1;if((q+1)%r)continue;U z=(q+1)/r;
  if(!(z%4)||!(r%4)||!(v%4)||!((z*r-1)%4)||!((z*v-1)%4))return (Result){HIT,v,r,z};
 }
 censored++;
 return (Result){CENSORED,0,0,0};
}
static void row(const char*tag,U p,Result s){
 printf("%s,%"PRIu64",",tag,p);
 if(s.status==HIT)printf("%"PRIu64,s.h); /* Missing H is not a zero minimum. */
 printf(",%"PRIu64",%"PRIu64",%"PRIu64",%s,%"PRIu64"\n",s.u,s.t,nr(p),s.status==HIT?"HIT":"CENSORED",cap);
}
static void emit(const char*tag,U p){if(p%24==1&&prime(p))row(tag,p,h4(p));}
static U argument(const char*s){char*end;U n=strtoull(s,&end,10);if(!*s||*end||s[0]=='-'||n<1||n>1000000000){fprintf(stderr,"invalid positive argument: %s\n",s);exit(2);}return n;}
static U state=460419;
static U rng(void){state^=state<<13;state^=state>>7;state^=state<<17;return state;}
static U gcd(U a,U b){while(b){U r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){
 /* Original defaults and RNG stream are unchanged. Small caps/draw counts allow regression tests. */
 if(argc>2)cap=argument(argv[2]);
 puts("family,p,H,u,t,r,status,cap");
 if(argc>1&&!strcmp(argv[1],"input")){char tag[100];U p;while(scanf("%99s %"SCNu64,tag,&p)==2)emit(tag,p);fprintf(stderr,"input evaluated=%"PRIu64" censored=%"PRIu64" cap=%"PRIu64"\n",evaluated,censored,cap);return 0;}
 if(argc>1&&!strcmp(argv[1],"qnr")){
  U trials=argc>3?argument(argv[3]):2000000;
  U ls[]={5,7,11,13,17,19,23,29,31}, more[]={37,41,43,47,53,59,61,67,71,73,79,83,89,97};unsigned accepted=0;
  for(U trial=0;trial<trials;trial++){
   U a=1,m=24;for(unsigned i=0;i<9;i++){U l=ls[i],s=1+rng()%(l-1),b=s*s%l;U k=mul((b+l-a%l)%l,power(m%l,l-2,l),l);a+=m*k;m*=l;}
   U p=a+m*(1+rng()%1000);int ok=1;
   for(unsigned i=0;i<14;i++)if(power(p%more[i],(more[i]-1)/2,more[i])!=1){ok=0;break;}
   if(ok&&prime(p)){emit("qnr97",p);accepted++;}
  }
  fprintf(stderr,"qnr97 candidates=%"PRIu64" prime_hits=%u evaluated=%"PRIu64" censored=%"PRIu64" cap=%"PRIu64" seed=460419\n",trials,accepted,evaluated,censored,cap);return 0;
 }
 if(argc>1&&!strcmp(argv[1],"hunt")){
  U draws=argc>3?argument(argv[3]):2000000;
  for(int band=0;band<2;band++){
   U base=band?100000000000000ULL:1000000000000ULL; unsigned got=0,kept=0,cut=0; U maxh=0; unsigned tails[7]={0};
   while(got<draws){U p=base+rng()%base;p+=(25-p%24)%24;if(!prime(p))continue;got++;Result s=h4(p);if(s.h>maxh)maxh=s.h;
    cut+=s.status==CENSORED;
    /* Censored draws exceed every threshold at or below the searched cap.
       Above the cap these counts are LOWER BOUNDS, not exact tails. */
    for(int j=0;j<7;j++)tails[j]+=s.status==HIT?s.h>(16ULL<<j):cap>=(16ULL<<j);
    if(s.status==CENSORED||s.h>=256){char tag[80];snprintf(tag,sizeof tag,"hunt_%d",band);row(tag,p,s);kept++;}
   }
   fprintf(stderr,"band=%d primes=%u kept=%u censored=%u cap=%"PRIu64" maxH=%"PRIu64" maxH_complete=%d seed=460419 tails_exact_through=%"PRIu64" tails16,32,64,128,256,512,1024=",band,got,kept,cut,cap,maxh,cut==0,cut?cap:UINT64_MAX);
   for(int j=0;j<7;j++)fprintf(stderr,"%u%s",tails[j],j==6?"\n":",");
  }
  return 0;
 }
 U fixtures[]={193,409,577,2521,3361,5569,9601,23929,66529,83449,102001,329617,712321,8813281,5101441,59929,4962049,8803369,9257329};
 for(unsigned i=0;i<sizeof(fixtures)/sizeof(*fixtures);i++)emit("fixture",fixtures[i]);
 /* Consecutive prime samples, not independent random primes. */
 U starts[]={100000000ULL,10000000000ULL,1000000000000ULL,100000000000000ULL,999999900000000ULL};
 int count=argc>1?(int)argument(argv[1]):100000;
 for(unsigned j=0;j<5;j++){char tag[80];snprintf(tag,sizeof tag,"interval_%u",j);U p=starts[j]+(25-starts[j]%24)%24;int got=0;for(;got<count;p+=24)if(prime(p)){emit(tag,p);got++;}}
 int ks[]={-24,-8,-3,1,8,24};U ms[]={10000,100000,1000000,10000000,31610000};
 for(unsigned j=0;j<5;j++)for(U m=ms[j];m<ms[j]+12000;m++)for(unsigned k=0;k<6;k++){char tag[80];snprintf(tag,sizeof tag,"near_%u_%d",j,ks[k]);emit(tag,m*m+ks[k]);}
 /* Square-mimicking lcm progressions. */
 U M=24;for(U h=4;h<=32;h++){M=M/gcd(M,h)*h;if(h%4)continue;char tag[80];snprintf(tag,sizeof tag,"lcm_%"PRIu64,h);U a=1;int got=0;while(got<300&&a<1000000&&a*M<1100000000000000ULL){U p=1+a*M;if(prime(p)){emit(tag,p);got++;}a++;}}
 /* Random CRT square classes: p=1 mod24, p=s_l^2 mod each l<=y. */
 U ls[]={5,7,11,13,17,19,23,29,31,37,41};
 for(unsigned j=2;j<11;j++){char tag[80];snprintf(tag,sizeof tag,"qr_%"PRIu64,ls[j]);
  for(unsigned trial=0;trial<1500;trial++){U a=1,m=24;for(unsigned i=0;i<=j;i++){U l=ls[i],s=1+rng()%(l-1),b=s*s%l;U k=mul((b+l-a%l)%l,power(m%l,l-2,l),l);a+=m*k;m*=l;}
   U start=1000000000000ULL;U k=a>=start?0:(start-a+m-1)/m;
   for(unsigned step=0;step<200&&a+k*m<=1100000000000000ULL;step++,k++)if(prime(a+k*m)){emit(tag,a+k*m);break;}
  }
 }
 fprintf(stderr,"census evaluated=%"PRIu64" censored=%"PRIu64" cap=%"PRIu64" interval_count=%d seed=460419\n",evaluated,censored,cap,count);
 return 0;
}
