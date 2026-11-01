/* z53_hyp2cycle_mix.c — second-order Weyl sums of the remainder map (hypothesis MIX, Z53_HYP2CYCLE §5):
     W(h1,h2) = sum_{u in D_f} e(h1*theta_u + h2*theta_{f(u)}),   theta_x = {-n/x} = ((-n) mod x)/x,
   D_f = {u in (U,2U] : f(u) defined}.  For each n (stdin) and U = floor(n^{1/4}) (or argv[2] if > 0), prints
     n U |D_f| max_{0<|h|<=H, h2!=0}|W|/sqrt|D_f|  argmax  max_{h2=0, 0<|h1|<=H}|W|/sqrt|D_f|  rms_{h2!=0}|W|/sqrt|D_f|  rms_{h1=0,h2!=0}|W|/sqrt|D_f|
   over the half-plane of frequencies (h1,h2) with |h1|,|h2| <= H (argv[1]).  Phases computed exactly in integer
   arithmetic (residues), then converted to double angles.  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 iroot4(u64 n){ u64 r=(u64)floor(pow((double)n,0.25)); while((u128)(r+1)*(r+1)*(r+1)*(r+1)<=n) r++; while((u128)r*r*r*r>n) r--; return r; }
int main(int argc,char**argv){ int H=atoi(argv[1]); long Ufix=argc>2?atol(argv[2]):0; char line[128];
  while(fgets(line,sizeof line,stdin)){ u64 n=strtoull(line,0,10); if(n<5) continue; u64 U=Ufix>0?(u64)Ufix:iroot4(n); if(2*U>=n) continue;
    long m=0; double *a1=malloc(sizeof(double)*(U+1)), *a2=malloc(sizeof(double)*(U+1));
    for(u64 u=U+1;u<=2*U;u++){ u64 r=(u-n%u)%u; u64 y=r; if(y<=U) y+=u*((U-y)/u+1); if(!(y>U&&y<=2*U)) continue;
      u64 r2=(y-n%y)%y; a1[m]=(double)r/(double)u; a2[m]=(double)r2/(double)y; m++; }
    double best=0,best0=0,ss=0,ssz=0; int bh1=0,bh2=0; long cnt=0,cntz=0;
    for(int h2=0;h2<=H;h2++) for(int h1=-H;h1<=H;h1++){ if(h2==0&&h1<=0) continue;
      double complex s=0; for(long i=0;i<m;i++) s+=cexp(2*M_PI*I*(h1*a1[i]+h2*a2[i]));
      double v=cabs(s)/sqrt((double)m);
      if(h2==0){ if(v>best0) best0=v; } else { ss+=v*v; cnt++; if(h1==0){ssz+=v*v;cntz++;} if(v>best){best=v;bh1=h1;bh2=h2;} } }
    printf("%llu %llu %ld %.3f (%d,%d) %.3f %.3f %.3f\n",n,U,m,best,bh1,bh2,best0,sqrt(ss/cnt),sqrt(ssz/cntz)); fflush(stdout); free(a1); free(a2); }
  return 0; }
