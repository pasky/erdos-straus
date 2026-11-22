/* Search Conj C on one reduced progression. Ascending-congruence sieve, then
   complete exact word search on primality-tested survivors. Unsigned arithmetic
   restricted by the assertions; under these bounds all Miller-Rabin bases in
   z80_parity_prime.c suffice. */
#define main z80_unused_main
#include "z80_parity_prime.c"
#undef main
#include <assert.h>
#include <inttypes.h>
#define U PRIu64
static void safe_divs(u64 N,u64 L,u64 r,u64 max){
 factor(N); u64 count=1;for(int i=0;i<nf;i++)count*=fe[i]+1;
 assert(count<=sizeof(divs)/sizeof(*divs));gL=L;gR=r%L;gMax=max;nd=0;gen(0,1);
}
static int ct[] = {1,3,5};
static int ok(u64 f){if(f%8!=7)return 0;for(int j=0;j<3;j++)if(f%ct[j]==0 && isprime(f/ct[j]))return 1;return 0;}
static u64 word(u64 p,u64 x,u64 y,u64 z){
 assert((u128)x*y*z==p+x+z && x && y && z);
 u64 a=x*y-1,b=z*y-1;
 if(ok(a))return a;
 if(ok(b))return b;
 return 0;
}
static u64 check(u64 p){
 // k=1 also handles all boundary words, incl. middle 1; ignore zero factors.
 for(u64 k=1;k*k*k<=p+2*k;k++){
   assert((u128)k*p+1<((u128)1<<62));
   u64 N=p+k;safe_divs(N,k,k-1,N);
   for(int i=0;i<nd;i++){
     u64 d=divs[i],t=(d+1)/k,v=N/d;
     if(t>=k&&v>=k){u64 f=word(p,k,t,v);if(f)return f;}
   }
   N=k*p+1;safe_divs(N,k,k-1,N);
   for(int i=0;i<nd;i++){
     u64 d=divs[i],u=(d+1)/k,v=(N/d+1)/k;
     if(k<=u&&u<=v){u64 f=word(p,u,k,v);if(f)return f;}
   }
 }
 return 0;
}
static i64 inv(i64 a,i64 m){i64 x=1,y=0,b=m;while(b){i64 q=a/b,r=a%b;a=b;b=r;r=x-q*y;x=y;y=r;}assert(a==1);return (x%m+m)%m;}
int main(int argc,char**argv){
 assert(argc==6);u64 step=strtoull(argv[1],0,10),base=strtoull(argv[2],0,10),first=strtoull(argv[3],0,10),cnt=strtoull(argv[4],0,10),lim=strtoull(argv[5],0,10);
 assert((u128)step*(first+(u128)cnt)+base<100000000000000ULL && cnt<=500000000 && base%8==1 && step%8==0 && lim<=5000000);
 for(int i=2;i<1000;i++)if(isprime(i))sp[nsp++]=i;
 unsigned char* closed=calloc(cnt,1);assert(closed);
 for(u64 f=7;f<=lim;f+=8){if(!ok(f))continue;
   u64 g=gcdu(step,f),m=f/g,v=inv((step/g)%m,m);
   safe_divs(f+1,1,0,f-1);
   for(int j=0;j<nd;j++){
     u64 r=divs[j];if((base+r)%g)continue;
     u64 ix=(m-((base+r)/g)%m)*v%m;
     for(u64 i=(ix+m-first%m)%m;i<cnt;i+=m)closed[i]=1;
   }
 }
 u64 left=0,prime=0,none=0,last=0;
 for(u64 i=0;i<cnt;i++)if(!closed[i]){
   left++;u64 p=base+step*(first+i);if(!isprime(p))continue;prime++;u64 f=check(p);
   if(!f){printf("NO135 %" U "\n",p);fflush(stdout);none++;}else {u64 r=f-p%f;assert(r<f&&(f+1)%r==0);if(f>last)last=f;}
 }
 printf("step=%" U " base=%" U " first=%" U " count=%" U " sieveF=%" U " survivors=%" U " primeSurvivors=%" U " no135=%" U " maxReturnedF=%" U "\n",step,base,first,cnt,lim,left,prime,none,last);
 free(closed);return 0;
}
