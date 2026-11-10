// z69 TWIST triage, IDEAA #11 (e = p+2 Type I slice):
// for odd M <= N: coprime a,b with ab | M^2 and (2M+1) | a+b ?
// (no coprimality imposed beyond a,b supported on disjoint prime sets; Lemma V itself needs none)
// usage: slice11 N   -> prints every hit "M a b c tag" (tag P if 2M-1 is a prime == 1 mod 8)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef uint64_t u64;
static int *spf;
static int isprime(u64 n){ if(n<2) return 0; for(u64 q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
int main(int argc,char**argv){
  long N=atol(argv[1]); spf=calloc(N+1,sizeof(int));
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
  long hits=0,hitsP=0,nM=0,nP=0;
  for(long M=1;M<=N;M+=2){
    u64 e=2*M+1; int np=0; u64 pr[20]; int ex[20]; long m=M;
    while(m>1){ int q=spf[m],v=0; while(m%q==0){m/=q;v++;} pr[np]=q; ex[np]=2*v; np++; }
    int isP = ((2*M-1)%8==1) && isprime(2*M-1); nM++; nP+=isP;
    // enumerate (a mod e, b mod e) over choices; residues tracked exactly with u128 a,b (a,b <= M^2 < 2^64 for M<4e9)
    // DFS
    u64 sa[21], sb[21]; int idx[21], st[21]; // iterative: state per prime: choice k in [0, 2*ex] : k<=ex -> a gets q^k ; k>ex -> b gets q^(k-ex)
    sa[0]=1; sb[0]=1; int d=0; idx[0]=0;
    while(d>=0){
      if(d==np){ u64 a=sa[d], b=sb[d]; if(a<b && (a+b)%e==0){ hits++; hitsP+=isP; printf("%ld %llu %llu %llu %s\n",M,(unsigned long long)a,(unsigned long long)b,(unsigned long long)((a+b)/e),isP?"P":"-"); } d--; continue; }
      int k=idx[d]; if(k>2*ex[d]){ d--; continue; }
      idx[d]=k+1; u64 a=sa[d], b=sb[d];
      if(k<=ex[d]){ for(int t=0;t<k;t++) a*=pr[d]; } else { for(int t=0;t<k-ex[d];t++) b*=pr[d]; }
      sa[d+1]=a; sb[d+1]=b; idx[d+1]=0; d++;
    }
  }
  printf("# DONE N=%ld odd M tested=%ld (M=1..N) hits=%ld ; M with 2M-1 a prime == 1 mod 8: tested=%ld hits=%ld\n",N,nM,hits,nP,hitsP);
  return 0;
}
