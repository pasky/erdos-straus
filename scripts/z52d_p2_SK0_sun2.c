/* Z0653 comparison axis (pass 2, SK0): r2(n) = #{(p,{a<=b}) : p prime, p+2^a+2^b = n}, odd n<=NMAX.
 * Crocker-type control: the count of odd n with r2(n)=0, and mean r2 vs ln n per dyadic block. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  long NMAX = argc>1? atol(argv[1]) : 10000000L;
  char*comp=calloc(NMAX+1,1); comp[0]=comp[1]=1;
  for(long i=2;i*i<=NMAX;i++) if(!comp[i]) for(long j=i*i;j<=NMAX;j+=i) comp[j]=1;
  unsigned int*r=calloc(NMAX+1,sizeof(unsigned int));
  int K=0; while((1L<<K)<=NMAX) K++;
  for(int a=0;a<K;a++) for(int b=a;b<K;b++){ long S=(1L<<a)+(1L<<b); if(S>NMAX-2) continue;
    for(long p=2;p<=NMAX-S;p++) if(!comp[p]) r[p+S]++; }
  for(int k=2;k<=30;k++){ long lo=(1L<<k)+1, hi=(1L<<(k+1))-1; if(lo>NMAX) break; if(hi>NMAX) hi=NMAX;
    double s=0; long cnt=0, z=0; for(long n=lo;n<=hi;n+=2){ s+=r[n]; cnt++; if(!r[n]) z++; }
    printf("block k=%d count=%ld mean_r2=%.3f mean/ln n=%.3f zeros=%ld\n",k,cnt,s/cnt,s/cnt/log((double)lo),z); }
  long tz=0; printf("odd n<=%ld with r2=0 (first 40):",NMAX);
  int shown=0; for(long n=3;n<=NMAX;n+=2) if(!r[n]){ tz++; if(shown<40){ printf(" %ld",n); shown++; } }
  printf("\ntotal %ld\n",tz); return 0; }
