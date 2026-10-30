// z51 dbreak round 4 (R4 repair): Monte Carlo law of the residual R in the independent model, same band and same
// histogram binning as z51_dbreak_resid.c (hlo = -10, hw = 0.02, bin b = [hlo + b*hw, hlo + (b+1)*hw)).
// Per draw and prime: hit with prob w/l (R += 1-2c), non-residue without hit with prob (l-1)/(2l) - w/l (R -= 2c).
// Usage: resid_modelmc N beta draws seed
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static uint64_t s[2]; static inline uint64_t nx(void){ uint64_t a=s[0], b=s[1]; s[0]=b; a^=a<<23; s[1]=a^b^(a>>17)^(b>>26); return s[1]+b; }
static int tau(long long x){ int d=1; for(long long p=2;p*p<=x;p++){ int e=0; while(x%p==0){x/=p;e++;} d*=e+1; } if(x>1) d*=2; return d; }
int main(int argc,char**argv){
  long long N=atoll(argv[1]); double beta=atof(argv[2]); long long D=atoll(argv[3]);
  s[0]=0x9E3779B97F4A7C15ULL^(uint64_t)atoll(argv[4]); s[1]=0xD1B54A32D192ED03ULL; for(int i=0;i<20;i++) nx();
  double z=exp(pow(log((double)N),beta)), y=sqrt(z); long long Z=(long long)z, Y=(long long)y;
  char *cp=calloc(Z+2,1); for(long long i=2;i*i<=Z;i++) if(!cp[i]) for(long long j=i*i;j<=Z;j+=i) cp[j]=1;
  long long np=0; for(long long l=3;l<=Z;l+=4) if(l>Y && !cp[l]) np++;
  uint64_t *th=malloc(8*np), *tn=malloc(8*np); double *vh=malloc(8*np), *vn=malloc(8*np); np=0; double mu=0;
  for(long long l=3;l<=Z;l+=4) if(l>Y && !cp[l]){ int w=tau((l+1)/4); double c=(double)w/(l-1); mu+=c;
    double ph=(double)w/l, pn=(double)(l-1)/(2.0*l);
    th[np]=(uint64_t)(ph*18446744073709551615.0); tn[np]=(uint64_t)(pn*18446744073709551615.0); vh[np]=1-2*c; vn[np]=-2*c; np++; }
  static long long hist[2001]; double hlo=-10, hw=0.02;
  for(long long d=0;d<D;d++){ double R=0; for(long long i=0;i<np;i++){ uint64_t u=nx(); if(u<th[i]) R+=vh[i]; else if(u<tn[i]) R+=vn[i]; }
    long long b=(long long)floor((R-hlo)/hw); if(b<0) b=0; if(b>2000) b=2000; hist[b]++; }
  printf("# model MC N=%lld beta=%.3f primes=%lld mu=%.6f draws=%lld\n", N, beta, np, mu, D);
  for(int b=0;b<=2000;b++) if(hist[b]) printf("HIST %.3f %lld\n", hlo+b*hw, hist[b]);
  return 0; }
