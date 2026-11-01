/* Z0653 (pass 2, SK0): representation counts r(n) = #{ (p,{a<=b<=c}) : p prime, a,b,c>=0, p+2^a+2^b+2^c = n }
 * for odd n <= NMAX.  Output: per dyadic block [2^k,2^{k+1}): mean r over odd n, fraction r=0, and the
 * list of odd n <= NMAX with r(n)=0 (the 'Sun exceptions' candidates).  Memory: arrays of size NMAX (uint16/uint32). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int main(int argc, char **argv){
  long NMAX = argc>1? atol(argv[1]) : 10000000L;
  char *comp = calloc(NMAX+1,1);
  comp[0]=comp[1]=1;
  for(long i=2;(i*i)<=NMAX;i++) if(!comp[i]) for(long j=i*i;j<=NMAX;j+=i) comp[j]=1;
  unsigned int *r = calloc(NMAX+1,sizeof(unsigned int));
  int K=0; while((1L<<K) <= NMAX) K++;     /* powers 2^0..2^{K-1} */
  long ntrip=0;
  for(int a=0;a<K;a++) for(int b=a;b<K;b++) for(int c=b;c<K;c++){
    long S = (1L<<a)+(1L<<b)+(1L<<c);
    if(S > NMAX-2) continue;
    ntrip++;
    for(long p=2; p<=NMAX-S; p++) if(!comp[p]) r[p+S]++;
  }
  /* blocks */
  for(int k=1;k<K;k++){
    long lo=1L<<k, hi=(1L<<(k+1))-1; if(lo>NMAX) break; if(hi>NMAX) hi=NMAX;
    double sum=0; long cnt=0, zero=0; double sumlog2=0;
    for(long n=lo+1;n<=hi;n+=2){ sum+=r[n]; cnt++; if(r[n]==0) zero++; }
    double ln = log((double)lo);
    printf("block k=%d odd n in [%ld,%ld]: count=%ld mean_r=%.4f mean_r/(ln n)^2=%.4f frac_r0=%.6f\n", k, lo, hi, cnt, sum/cnt, sum/cnt/(ln*ln), (double)zero/cnt);
  }
  printf("triples used: %ld\n", ntrip);
  printf("odd n<=NMAX with r(n)=0 (first 200):");
  int shown=0; long totzero=0;
  for(long n=3;n<=NMAX;n+=2){ if(r[n]==0){ totzero++; if(shown<200){ printf(" %ld",n); shown++; } } }
  printf("\ntotal odd n with r=0: %ld\n", totzero);
  return 0;
}
