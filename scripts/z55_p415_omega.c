// z55 P415: for primes p <= X, p = 1 (mod 8): exact Omega_Q(p+4), Omega_Q(4p+1) (Q = primes = 3 mod 4, with
// multiplicity) and (for the x^delta tests only) a lower bound for the least Q-prime factor of 4p+1 (if no Q-prime
// <= sqrt(4X+1) divides it, the stored value is the cofactor, which exceeds every tested cutoff x^delta, delta <= 1/4).  Exact: all Q-primes l <= sqrt(4X+1) are divided out; the
// cofactor then holds at most one Q-prime (> sqrt N), present iff cofactor = 3 (mod 4).
// Mode "int": same statistics over ALL n = 1 (mod 8) (integer control) instead of primes.
// Mode "sq": control over odd squares n = m^2 (theory: Omega_Q(n+4) = Omega_Q(4n+1) = 0 always).
// Usage: z55_p415_omega X [prime|int|sq]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64;
static u64 inv_mod(u64 a, u64 m){ long long t=0,nt=1; long long r=m, nr=a%m; while(nr){ long long q=r/nr, tmp=t-q*nt; t=nt; nt=tmp; tmp=r-q*nr; r=nr; nr=tmp; } if(t<0) t+=m; return (u64)t; }
#define NDEL 7
static const double DELS[NDEL]={0.01,0.02,0.03,0.05,0.1,0.2,0.25};
static int omegaQ_direct(u64 n, u64 *minq){ int c=0; *minq=0; while(n%2==0) n/=2; for(u64 l=3;l*l<=n;l+=2){ while(n%l==0){ if(l%4==3){ c++; if(!*minq) *minq=l; } n/=l; } } if(n>1 && n%4==3){ c++; if(!*minq) *minq=n; } return c; }
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10); const char *mode = argc>2? argv[2] : "prime";
  if(!strcmp(mode,"sq")){ // control over odd squares
    u64 bad=0, tot=0; for(u64 m=1; m*m<=X; m+=2){ u64 n=m*m, q1,q2; int a=omegaQ_direct(n+4,&q1), b=omegaQ_direct(4*n+1,&q2); tot++; if(a||b) bad++; }
    printf("odd squares n<=%llu: %llu checked, %llu with Omega_Q(n+4)+Omega_Q(4n+1)>0\n", X, tot, bad); return 0; }
  int isprime_mode = !strcmp(mode,"prime");
  u64 L=(u64)sqrtl((long double)(4*X+1))+2;
  char *isc=calloc(L+1,1); u64 *pr=malloc(sizeof(u64)*(L/2+10)); int np=0;
  for(u64 i=2;i<=L;i++){ if(!isc[i]){ pr[np++]=i; for(u64 j=i*i;j<=L;j+=i) isc[j]=1; } }
  const u64 SEG=1<<22; // idx positions per segment; p = base + 8*idx
  u64 *c1=malloc(8*SEG), *c2=malloc(8*SEG), *mq2=malloc(8*SEG); unsigned char *o1=malloc(SEG), *o2=malloc(SEG), *comp=malloc(SEG);
  u64 tot=0, n1S=0, hist[12]={0}, histall[12]={0}, delcnt[NDEL]={0}, both=0;
  double lx=log((double)X);
  for(u64 base=1; base<=X; base+=8*SEG){
    u64 n = SEG; if(base+8*(n-1) > X) n = (X-base)/8+1;
    for(u64 i=0;i<n;i++){ u64 p=base+8*i; c1[i]=p+4; c2[i]=4*p+1; mq2[i]=0; o1[i]=o2[i]=0; comp[i]=0; }
    if(isprime_mode){
      if(base==1) comp[0]=1; // p=1
      for(int k=0;k<np;k++){ u64 l=pr[k]; if(l==2) continue; if(l*l > base+8*(n-1)) break;
        // p = 0 mod l, p = 1 mod 8: idx i with base+8i = 0 mod l
        u64 i0 = ((l - base%l)%l) * inv_mod(8%l,l) % l; u64 p0=base+8*i0;
        for(u64 i=i0;i<n;i+=l){ u64 p=base+8*i; if(p!=l) comp[i]=1; } (void)p0; }
    }
    for(int k=0;k<np;k++){ u64 l=pr[k]; if(l%4!=3) continue;
      u64 inv8=inv_mod(8%l,l);
      for(int w=0;w<2;w++){
        u64 r = w==0 ? (l-4%l)%l : (l-inv_mod(4%l,l))%l;   // root of p+4 resp. 4p+1 mod l
        if(w==1 && l==3) { /* roots coincide mod 3: both handled since r computed separately */ }
        u64 i0 = ((r + l - base%l)%l) * inv8 % l;
        for(u64 i=i0;i<n;i+=l){
          if(w==0){ while(c1[i]%l==0){ c1[i]/=l; o1[i]++; } }
          else { if(!mq2[i]) mq2[i]=l; while(c2[i]%l==0){ c2[i]/=l; o2[i]++; } }
        }
      }
    }
    for(u64 i=0;i<n;i++){ if(comp[i]) continue; u64 p=base+8*i; if(isprime_mode && p<2) continue;
      if(c1[i]>1 && c1[i]%4==3) o1[i]++;
      if(c2[i]>1 && c2[i]%4==3){ o2[i]++; if(!mq2[i]) mq2[i]=c2[i]; }
      tot++;
      int h2 = o2[i]>10?11:o2[i]; histall[h2]++;
      if(o1[i]==0){ n1S++; hist[h2]++; if(o2[i]==0) both++;
        for(int d=0;d<NDEL;d++){ double z=exp(DELS[d]*lx); if(mq2[i]==0 || (double)mq2[i] >= z) delcnt[d]++; } }
    }
  }
  printf("mode=%s X=%llu  #n=1(8)=%llu  #(N1 in S)=%llu  #(both in S)=%llu\n", mode, X, tot, n1S, both);
  printf("Omega_Q(4n+1) histogram among N1 in S (0..10, >10):"); for(int k=0;k<12;k++) printf(" %llu", hist[k]); printf("\n");
  printf("Omega_Q(4n+1) histogram over all:"); for(int k=0;k<12;k++) printf(" %llu", histall[k]); printf("\n");
  printf("among N1 in S, #(4n+1 free of Q-primes < X^delta):"); for(int d=0;d<NDEL;d++) printf(" d=%.2f:%llu", DELS[d], delcnt[d]); printf("\n");
  return 0; }
