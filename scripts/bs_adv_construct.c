/* O154: construct adversarial primes p in [X, 2X):
     p = r + k*M  (M, r given; e.g. 24 * primorial -> p == 1 mod M: square-mimicking AND p-1 highly divisible),
     p prime, N_e = (p+e)/4 prime for every e in list S2 (Type II shifts),
     (p*e+1)/4 prime for every e in list S1 (Type I shifts; needs p*e < 2^64*... we use u128 MR).
   Usage: bs_adv_construct X M r K seed "S2 list comma" "S1 list comma"   (prints up to K primes)
   Build: gcc -O2 -o /tmp/bs_adv_construct scripts/bs_adv_construct.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64; typedef __uint128_t u128;
static u128 mulm(u128 a,u128 b,u128 m){ /* m < 2^64 assumed for speed path */
  if(m < ((u128)1<<64)) return (u128)((u64)a%(u64)m) * (u128)((u64)b%(u64)m) % m;
  /* slow path: double-and-add */
  u128 r=0; a%=m; b%=m; while(b){ if(b&1){ r+=a; if(r>=m) r-=m; } a<<=1; if(a>=m) a-=m; b>>=1; } return r; }
static u128 powm(u128 a,u128 e,u128 m){ u128 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static int isprime(u128 n){ if(n<2) return 0; static const int sp[]={2,3,5,7,11,13,17,19,23,29,31,37,41};
  for(int i=0;i<13;i++){ if(n==(u128)sp[i]) return 1; if(n%sp[i]==0) return 0; }
  u128 d=n-1; int s=0; while(!(d&1)){ d>>=1; s++; }
  for(int i=0;i<13;i++){ u128 x=powm(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
static int parse(const char*s, u64*out){ int n=0; if(!s||!*s) return 0; char*b=strdup(s),*t=strtok(b,","); while(t){ out[n++]=strtoull(t,0,10); t=strtok(0,","); } free(b); return n; }
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), M=strtoull(argv[2],0,10), r=strtoull(argv[3],0,10); int K=atoi(argv[4]); u64 seed=strtoull(argv[5],0,10);
  u64 S2[64],S1[64]; int n2=parse(argc>6?argv[6]:"",S2), n1=parse(argc>7?argv[7]:"",S1);
  u64 kmin=(X-1)/M+1, kmax=(2*X-1)/M; if(kmax<kmin){ fprintf(stderr,"M too big\n"); return 1; }
  u64 span=kmax-kmin+1; u64 start = kmin + (seed*0x9E3779B97F4A7C15ULL)%span; int found=0;
  for(u64 t=0;t<span && found<K;t++){ u64 k = kmin + (start-kmin+t)%span; u64 p=r+k*M; if(p<X) continue;
    int ok=1;
    for(int i=0;i<n2&&ok;i++){ if((p+S2[i])%4){ok=0;break;} if(!isprime((p+S2[i])/4)) ok=0; }
    for(int i=0;i<n1&&ok;i++){ u128 v=(u128)p*S1[i]+1; if(v%4){ok=0;break;} if(!isprime(v/4)) ok=0; }
    if(ok && isprime(p)){ printf("%llu\n",(unsigned long long)p); found++; fflush(stdout);} }
  return 0; }
