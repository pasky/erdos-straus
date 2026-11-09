// z68 U7F: for primes p = 1 (mod 8) up to N, least witness f = 7 (mod 8) with r = (-p mod f) | f+1.
// Prints histogram of least f and the hardest primes (largest least f) with (f, r, s=(f+1)/r, t=(p+r)/f).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 N=atoll(argv[1]); int K=argc>2?atoi(argv[2]):30; // print top K hardest
  char*sv=calloc(N+1,1); for(u64 i=2;i*i<=N;i++) if(!sv[i]) for(u64 j=i*i;j<=N;j+=i) sv[j]=1;
  // top-K by least f
  u64 *hp=calloc(K,8),*hf=calloc(K,8); int nh=0;
  u64 cnt=0; double sumlogf=0; u64 hist[64]={0};
  for(u64 p=17;p<=N;p+=8){ if(sv[p]) continue; cnt++;
    u64 f; int found=0;
    for(f=7;;f+=8){ u64 r=f-(p%f); if(r==f) continue; if((f+1)%r==0){found=1;break;} if(f>2*p+1) break; }
    if(!found){ printf("ZERO %llu\n",p); continue; }
    int b=0; while((1ULL<<b)<f) b++; hist[b]++;
    // insert into top-K
    if(nh<K || f>hf[nh-1]){ int i=nh<K?nh:K-1; if(nh<K) nh++; while(i>0 && hf[i-1]<f){hp[i]=hp[i-1];hf[i]=hf[i-1];i--;} hp[i]=p;hf[i]=f; }
  }
  printf("primes p=1(8) <= %llu: %llu\n",N,cnt);
  for(int b=0;b<64;b++) if(hist[b]) printf("f in [2^%d,2^%d): %llu\n",b-1,b,hist[b]);
  for(int i=0;i<nh;i++){ u64 p=hp[i],f=hf[i],r=f-(p%f); printf("HARD p=%llu minf=%llu r=%llu s=%llu t=%llu f mod 840=%llu p mod 840=%llu\n",p,f,r,(f+1)/r,(p+r)/f,f%840,p%840); }
}
