/* R176: check "a valid c exists iff 4h | gcd(h,G)^2" over ALL factor pairs f<=f' of 1+nh,
   1<=h<=n^2, odd n<=NMAX (no tuple input). Also reports the h=0 edge (f=f'=1). */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){int NMAX=atoi(argv[1]); long pairs=0,pos=0,bad=0,over=0;
 for(u64 n=3;n<=(u64)NMAX;n+=2) for(u64 h=1;h<=n*n;h++){u64 N=1+n*h;
  for(u64 f=1;f*f<=N;f++){ if(N%f) continue; u64 g2=N/f; u64 G=gcd(f+1,g2+1), g=gcd(h,G);
   int P=((g*g)%(4*h)==0); int E=0;
   for(u64 c=1;4*c*c<=h;c++) if(h%(4*c*c)==0 && (c*G)%h==0){E=1;break;}
   pairs++; pos+=P; if(P!=E){bad++; if(bad<10)printf("bad n=%llu h=%llu f=%llu\n",n,h,f);}
   if(P && 4*h>(n+5)*(n+5)) over++; }}
 printf("odd n<=%d, h<=n^2: %ld factor pairs, %ld with predicate, %ld disagreements, %ld beyond (n+5)^2/4\n",NMAX,pairs,pos,bad,over);
 return 0;}
