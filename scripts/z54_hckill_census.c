// z54 HCKILL: exact count of primes p <= X, p = 1 (mod 8), with HC(p) > 4, i.e. p+4 and 4p+1 both in S
// (all prime factors = 1 mod 4).  Exact by sieving with primes l = 3 (mod 4), l <= sqrt(4X+1): after that, a window
// integer N = 1 (mod 4) free of small l = 3 (4) is (product of small primes = 1 mod 4) x (1 or one prime > sqrt N),
// and that prime is then = 1 (mod 4) by N = 1 (mod 4).  Primality of p by a segmented Eratosthenes sieve.
// Usage: z54_hckill_census X  -> prints cumulative counts at 10^k and at X; also counts p = 1 (8) primes.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64;
static u64 inv_mod(u64 a, u64 m){ long long t=0,nt=1; long long r=m, nr=a%m; while(nr){ long long q=r/nr, tmp=t-q*nt; t=nt; nt=tmp; tmp=r-q*nr; r=nr; nr=tmp; } if(t<0) t+=m; return (u64)t; }
int main(int argc,char**argv){ u64 X=strtoull(argv[1],0,10); u64 L=(u64)sqrtl((long double)(4*X+1))+2;
  char *isc=calloc(L+1,1); u64 *pr=malloc(sizeof(u64)*(L/2+10)); int np=0;
  for(u64 i=2;i<=L;i++){ if(!isc[i]){ pr[np++]=i; for(u64 j=i*i;j<=L;j+=i) isc[j]=1; } }
  // for each prime: next multiple offsets handled per segment
  const u64 SEG=1<<24; unsigned char *comp=malloc(SEG), *bad=malloc(SEG);
  u64 cnt=0, cnt8=0, nextdec=100000; 
  for(u64 lo=0; lo<=X; lo+=SEG){ u64 hi=lo+SEG; if(hi>X+1) hi=X+1; u64 n=hi-lo;
    memset(comp,0,n); memset(bad,0,n);
    for(int k=0;k<np;k++){ u64 q=pr[k]; if(q*q>=hi) break; u64 s=((lo+q-1)/q)*q; if(s<q*q) s=q*q; for(u64 j=s;j<hi;j+=q) comp[j-lo]=1; }
    for(int k=1;k<np;k++){ u64 l=pr[k]; if(l%4!=3) continue;
      u64 r1=(l-4%l)%l;                        // p = -4 mod l
      u64 r2=(l-inv_mod(4%l,l))%l;              // p = -1/4 mod l
      u64 s=lo+((r1+l-lo%l)%l); for(u64 j=s;j<hi;j+=l) bad[j-lo]=1;
      if(r2!=r1){ s=lo+((r2+l-lo%l)%l); for(u64 j=s;j<hi;j+=l) bad[j-lo]=1; } }
    u64 st=lo + ((1+8-lo%8)%8);
    for(u64 p=st;p<hi;p+=8){ if(p<2) continue; if(comp[p-lo]) continue;
      while(p>nextdec){ printf("x=%llu  #p=1(8)=%llu  #HC>4=%llu\n", nextdec, cnt8, cnt); nextdec*=10; }
      cnt8++; if(p<=L && 0){} 
      // small p: the sieve may mark p+4 = l itself etc.; correct by direct check for p < L
      int b=bad[p-lo];
      if(p< L){ // direct
        u64 a=p+4, c=4*p+1; b=0; for(int k=1;k<np && pr[k]<=c;k++){ u64 l=pr[k]; if(l%4==3 && (a%l==0 || c%l==0)) {b=1;break;} } }
      if(!b) cnt++; }
  }
  printf("x=%llu  #p=1(8)=%llu  #HC>4=%llu\n", X, cnt8, cnt); return 0; }
