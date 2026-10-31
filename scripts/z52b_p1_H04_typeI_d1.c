/* Z1482: primes p≡1 (4) <= P with no Type I d=1 certificate f | p^2+4c^2, f ≡ -p (mod 4c), c <= CMAX.
   Prints failures and histogram of first successful c. */
#include <stdio.h>
#include "z52b_p1_H04_fac.h"
int main(int argc,char**argv){u64 P=atoll(argv[1]);u64 CMAX=atoll(argv[2]);
 char*sv=calloc(P+1,1);for(u64 i=2;i*i<=P;i++)if(!sv[i])for(u64 j=i*i;j<=P;j+=i)sv[j]=1;
 long hist[64]={0};long nprimes=0,nfail=0;u64 pr[64];int ex[64];
 for(u64 p=5;p<=P;p+=4){if(sv[p])continue;nprimes++;u64 c;int found=0;
  for(c=1;c<=CMAX;c++){u64 N=p*p+4*c*c;int k=factor(N,pr,ex);u64 m=4*c;int r=has_div_class(pr,ex,k,m,(m-p%m)%m);if(r){found=1;break;}}
  if(found){int b=0;while((1ULL<<b)<c)b++;hist[b]++;}else{nfail++;printf("FAIL %llu\n",(unsigned long long)p);}}
 printf("primes %ld fails %ld\n",nprimes,nfail);for(int b=0;b<40;b++)if(hist[b])printf("first c in (2^%d,2^%d]: %ld\n",b-1,b,hist[b]);}
