/* z52d pass2 TO6 fix: witness bitmask for primes p≡1 mod 4, p<=P. Bit j set iff t=3+4j (j<64) has a Type-I
 * slice witness (CONDITIONAL_ES Lemma 1.1: tp+1=m*m'', m≡m''≡-1 mod t, 4|m). Output: p mask(hex).  usage: wit P */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
static int primes[30000]; static int np=0;
static int witness(u64 p,u64 t){
  u64 N=t*p+1; u64 f[64]; int e[64]; int nf=0; u64 v=N;
  for(int i=0;i<np && (u64)primes[i]*primes[i]<=v;i++){ u64 q=primes[i]; if(v%q==0){int c=0; while(v%q==0){v/=q;c++;} f[nf]=q; e[nf]=c; nf++;}}
  if(v>1){ f[nf]=v; e[nf]=1; nf++; }
  static u64 divs[1<<14]; int nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){ int cur=nd; u64 pw=1; for(int k=1;k<=e[i];k++){ pw*=f[i]; for(int j=0;j<cur;j++){ divs[nd++]=divs[j]*pw; } } }
  for(int j=0;j<nd;j++){ u64 m=divs[j]; u64 m2=N/m; if(m%4==0 && m%t==t-1 && m2%t==t-1) return 1; }
  return 0;
}
int main(int argc,char**argv){
  u64 P=atoll(argv[1]);
  int S=20000; char*isc=calloc(S+1,1);
  for(int i=2;i<=S;i++){ if(!isc[i]){ primes[np++]=i; for(long j=(long)i*i;j<=S;j+=i) isc[j]=1; } }
  char*comp=calloc(P+1,1);
  for(u64 p=2;p<=P;p++){
    if(comp[p]) continue; for(u64 j=p*p;j<=P;j+=p) comp[j]=1;
    if(p%4!=1) continue;
    u64 mask=0;
    for(int j=0;j<64;j++){ if(witness(p,3+4*j)) mask|=(1ULL<<j); }
    printf("%llu %llx\n",p,mask);
  }
  return 0;
}
