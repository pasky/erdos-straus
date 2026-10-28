/* Exact global genus minorant for the finite q|Q certificate menu.
   All cutoffs are inactive for p>Q. Restrict residues to p=1 mod 24.
   Output min/mean/max within each global quadratic-character fibre.
   Q is a multiple of 24, Q<=200000000; at most 10 odd prime factors >=5.
   Memory <= 8Q bytes. No Cartesian-product arrays.
*/
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
static long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
static int jac(long a,long n){int s=1;a%=n;while(a){while(!(a&1)){a/=2;if(n%8==3||n%8==5)s=-s;}long t=a;a=n;n=t;if(a%4==3&&n%4==3)s=-s;a%=n;}return n==1?s:0;}
int main(int argc,char **argv){
 if(argc!=2)return 2;
 long Q=strtol(argv[1],NULL,10);
 if(Q<24||Q%24||Q>200000000)return 2;
 long rem=Q, primes[10];int k=0;
 while(rem%2==0)rem/=2;
 while(rem%3==0)rem/=3;
 for(long l=5;l*l<=rem;l+=2)if(rem%l==0){if(k==10)return 2;primes[k++]=l;while(rem%l==0)rem/=l;}
 if(rem>1){if(k==10)return 2;primes[k++]=rem;}
 uint32_t *R=calloc(Q,sizeof(*R)),*B=calloc(Q,sizeof(*B));if(!R||!B)return 2;
 long divs[4096],nd=0;
 for(long d=1;d*d<=Q/4;d++)if((Q/4)%d==0){divs[nd++]=d;if(d*d!=Q/4)divs[nd++]=(Q/4)/d;}
 long starpairs=0,bpairs=0;
 for(long j=0;j<nd;j++){
  long m=divs[j],q=4*m;
  for(long u=1;u*u<m;u++)if(m%u==0){long v=m/u;
   if((u+v)%2&&gcdl(u,v)==1){long a=(q-u-v)%q;for(long r=a;r<Q;r+=q)R[r]+=2;starpairs+=2;}
  }
  for(long y=3;y<=m;y+=2)if(m%y==0&&y%4==3){long x=m/y;
   if(gcdl(x,y)==1){long a=(-(4*x+y))%q;if(a<0)a+=q;for(long r=a;r<Q;r+=q)B[r]++;bpairs++;}
  }
 }
 int cells=1<<k;uint64_t cnt[1024]={0},sr[1024]={0},sb[1024]={0};
 uint32_t minr[1024],mint[1024],maxt[1024]={0};long arg[1024]={0};
 for(int s=0;s<cells;s++){minr[s]=UINT_MAX;mint[s]=UINT_MAX;}
 for(long r=1;r<Q;r+=24){int s=0,unit=1;
  for(int j=0;j<k;j++){int z=jac(r,primes[j]);if(!z){unit=0;break;}if(z<0)s|=1<<j;}
  if(!unit)continue;
  uint32_t t=R[r]+B[r];cnt[s]++;sr[s]+=R[r];sb[s]+=B[r];
  if(R[r]<minr[s])minr[s]=R[r];
  if(t<mint[s]){mint[s]=t;arg[s]=r;}if(t>maxt[s])maxt[s]=t;
 }
 printf("# Q=%ld star_ordered_pairs=%ld B_pairs=%ld character_primes=",Q,starpairs,bpairs);
 for(int j=0;j<k;j++){printf("%s%ld",j?",":"",primes[j]);}
 puts("");
 puts("mask,units,minR,minT,meanR,meanB,maxT,argminT");
 for(int s=0;s<cells;s++){assert(cnt[s]);printf("%d,%llu,%u,%u,%.12g,%.12g,%u,%ld\n",s,(unsigned long long)cnt[s],minr[s],mint[s],(double)sr[s]/cnt[s],(double)sb[s]/cnt[s],maxt[s],arg[s]);}
 free(R);free(B);return 0;
}
