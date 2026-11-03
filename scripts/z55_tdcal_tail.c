/* z55 TDCAL: tail distribution of |T(h)|^2/|E1+| over all (n,h), 1<=h<=H, n from stdin, U=floor(n^{1/4}).
   Same strip/phase conventions as scripts/z54_bilindiv_td.c. Prints, for t in {0.5,1,...,4}, the empirical
   P(|T|/sqrt|E1+| > t) next to the complex-Gaussian (Rayleigh) value exp(-t^2), plus mean |T|^2/|E1+|. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef long long i64;
static u64 iroot4(u64 n){ u64 r=(u64)floor(pow((double)n,0.25)); while((u128)(r+1)*(r+1)*(r+1)*(r+1)<=n) r++; while((u128)r*r*r*r>n) r--; return r; }
int main(int argc,char**argv){ int H=atoi(argv[1]); char line[128]; double complex *T=malloc(sizeof(double complex)*(H+1));
  double th[9]={0.5,1,1.5,2,2.5,3,3.5,4,4.5}; long cnt[9]={0}; long tot=0; double m2=0;
  while(fgets(line,sizeof line,stdin)){ u64 n=strtoull(line,0,10); if(n<5) continue; u64 U=iroot4(n), U2=U*U;
    u64 klo=(n+2*U)/(4*U2); if(klo<1) klo=1; u64 khi=(n+4*U)/U2+1; long e1p=0; for(int h=0;h<=H;h++) T[h]=0;
    for(u64 k=klo;k<=khi;k++){ u64 r=n%k; u64 s=(r==0)?0:k-r; if(!(s>2*U&&s<=4*U)) continue; u64 m=(n+s)/k;
      if(!(m>U2&&m<=4*U2)) continue; i64 D=(i64)(s*s)-(i64)(4*m); if(D<1) continue; e1p++;
      double x=sqrt((double)D); double complex z=cexp(2*M_PI*I*fmod(x,1.0)), zz=z; for(int h=1;h<=H;h++){T[h]+=zz; zz*=z;} }
    for(int h=1;h<=H;h++){ double v=cabs(T[h])/sqrt((double)e1p); m2+=v*v; tot++; for(int j=0;j<9;j++) if(v>th[j]) cnt[j]++; } }
  printf("samples=%ld mean|T|^2/|E1+|=%.4f\n",tot,m2/tot);
  for(int j=0;j<9;j++) printf("t=%.1f emp=%.3e rayleigh=%.3e\n",th[j],(double)cnt[j]/tot,exp(-th[j]*th[j]));
  return 0; }
