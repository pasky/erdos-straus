/* bsG_count: R(n) = #{(x,y,z) in Z_{>=2}^3 : xyz - x - z = n} for individual n (up to ~1e14).
   Method: x <= z wlog; z(xy-1) = n+x, so enumerate divisors d = xy-1 of n+x with d = -1 (mod x),
   d >= 2x-1, z = (n+x)/d >= x. n+x factored by a segmented sieve over x in [2, X], X ~ sqrt(n/2)+3.
   Usage: bsG_count n1 n2 ...   (prints n, R(n), and up to 8 solutions (x,y,z) with x<=z)
   gcc -O2 -o /tmp/bsG_count scripts/bsG_count.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
#define B 65536
static u64 *pr; static long npr;
static u64 fp[B][16]; static int fe[B][16], fn[B]; static u64 rem_[B];
static u64 n, xcur; static long R; static int shown;
static void rec(int i, int k, u64 d){
  if(k==fn[i]){ u64 x=xcur, N=n+x; if(d%x==x-1 && d>=2*x-1){ u64 z=N/d; if(z>=x){ R+= (z==x)?1:2;
        if(shown<8){ printf("   (x,y,z)=(%llu,%llu,%llu)\n",x,(d+1)/x,z); shown++; } } } return; }
  u64 p=fp[i][k]; for(int e=0;e<=fe[i][k];e++){ rec(i,k+1,d); d*=p; } }
int main(int argc,char**argv){
  for(int a=1;a<argc;a++){ n=strtoull(argv[a],0,10); R=0; shown=0;
    u64 X=(u64)sqrtl((long double)n/2)+3; u64 P=(u64)sqrtl((long double)(n+X))+2;
    pr=malloc(sizeof(u64)*(P/2+10)); npr=0; char*s=calloc(P+1,1);
    for(u64 i=2;i<=P;i++) if(!s[i]){ pr[npr++]=i; for(u64 j=i*i;j<=P;j+=i) s[j]=1; } free(s);
    printf("n=%llu\n",n);
    for(u64 x0=2;x0<=X;x0+=B){ u64 cnt = (X-x0+1<B)?X-x0+1:B;
      for(u64 i=0;i<cnt;i++){ rem_[i]=n+x0+i; fn[i]=0; }
      for(long j=0;j<npr;j++){ u64 p=pr[j]; u64 st=(p - (n+x0)%p)%p;
        for(u64 i=st;i<cnt;i+=p){ int e=0; while(rem_[i]%p==0){ rem_[i]/=p; e++; } fp[i][fn[i]]=p; fe[i][fn[i]]=e; fn[i]++; } }
      for(u64 i=0;i<cnt;i++){ if(rem_[i]>1){ fp[i][fn[i]]=rem_[i]; fe[i][fn[i]]=1; fn[i]++; }
        xcur=x0+i; rec(i,0,1); } }
    printf("R(%llu) = %ld\n",n,R); fflush(stdout); free(pr); }
  return 0; }
