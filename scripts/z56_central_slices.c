/* z56 CENTRAL: decomposition of the short-interval divisor sum D(x,y) into m-slices (Z56_CENTRAL.md Thm L).
   Input lines: "x y U [tag]"; central band (U^2,4U^2].
   Output per input: tag x y U Derr Ec | for delta in {0.05,0.10,0.15,0.20}: Eband Eband_h FLc resid resid_h | ... || E_M ...
   Derr   = D(x,y) - [(x+y)log(x+y) - x log x + (2g-1)y]   (D exact via the hyperbola identity)
   Ec     = #{(k,m): x<km<=x+y, U^2<m<=4U^2} - y*sum_{U^2<m<=4U^2} 1/m
   FLc    = sum_{m<=L} (floor((x+y)/m)-floor(x/m)) - y*H(L) = -F_L,  F_L = sum_{m<=L}[psi((x+y)/m)-psi(x/m)],
            L = x^{1/2-delta}, H(L) = sum_{m<=L} 1/m
   Eband  = #{(k,m): x<km<=x+y, L<m<=L'} - 2 delta y log x   (Thm L's E_band; L' = x^{1/2+delta})
   Eband_h= same count - y*sum_{L<m<=L'} 1/m                 (harmonic-centred variant)
   resid  = Derr - (Eband + 2 FLc)   = Thm L(i) residual (O(1));  resid_h = Derr - (Eband_h + 2 FLc)
   Without Z56_DIRECT the band count is not computed (loop only to max(sqrt(x+y),4U^2)); then the program prints
   the proxy Derr - 2 FLc (= E_band + O(1) by Thm L(i)) in both Eband columns and nan residuals.
   E_M = sum_{M<m<=2M} count - y*sum 1/m, M = y*2^j, j = 0.. while M <= sqrt(x).
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef unsigned long long u64;
static u64 isqrtll(u64 n){ u64 r=(u64)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r; }
int main(void){
  const long double g=0.57721566490153286060651209L;
  u64 x,y,U; char line[512]; char tag[64];
  const double dl[4]={0.05,0.10,0.15,0.20};
  while(fgets(line,sizeof line,stdin)){
    tag[0]=0; if(sscanf(line,"%llu %llu %llu %63s",&x,&y,&U,tag)<3) continue;
    u64 X1=x+y; u64 s0=isqrtll(x), s1=isqrtll(X1);
    u64 A=U*U, B4=4*U*U;
    u64 mmax = s1; if(B4>mmax) mmax=B4;
    u64 L[4],Lp[4]; long double lx=logl((long double)x);
    for(int i=0;i<4;i++){ L[i]=(u64)floorl(expl((0.5L-dl[i])*lx)); Lp[i]=(u64)floorl(expl((0.5L+dl[i])*lx)); }
    int direct = (getenv("Z56_DIRECT")!=NULL);
    if(direct) for(int i=0;i<4;i++) if(Lp[i]>mmax) mmax=Lp[i];
    /* accumulators */
    long double T0=0,T1=0; /* sum floor(x/m), floor(X1/m) up to s0,s1 */
    long long cntL[4]={0}, cntB[4]={0}; long double hL[4]={0}, hB[4]={0};
    long long cc=0; long double hc=0;
    int nb=0; long long cM[64]={0}; long double hM[64]={0}; u64 Mlo[64];
    { u64 M=y; while(M<=s0 && nb<60){ Mlo[nb++]=M; M*=2; } }
    for(u64 m=1;m<=mmax;m++){
      u64 q0=x/m, q1=X1/m; long long c=(long long)(q1-q0); long double inv=1.0L/(long double)m;
      if(m<=s0) T0+=q0; if(m<=s1) T1+=q1;
      for(int i=0;i<4;i++){ if(m<=L[i]){cntL[i]+=c; hL[i]+=inv;} else if(m<=Lp[i]){cntB[i]+=c; hB[i]+=inv;} }
      if(m>A && m<=B4){ cc+=c; hc+=inv; }
      for(int j=0;j<nb;j++) if(m>Mlo[j] && m<=2*Mlo[j]){ cM[j]+=c; hM[j]+=inv; }
    }
    long double D = (2*T1-(long double)s1*s1) - (2*T0-(long double)s0*s0);
    long double main_ = (long double)y*lx + (long double)X1*log1pl((long double)y/(long double)x) + (2*g-1)*(long double)y;
    long double Derr = D-main_;
    long double Ec = cc - (long double)y*hc;
    printf("%s %llu %llu %llu %.4Lf %.4Lf", tag[0]?tag:"-", x,y,U,Derr,Ec);
    for(int i=0;i<4;i++){
      long double FLc = cntL[i] - (long double)y*hL[i];
      long double Eband, Eband_h, resid, resid_h;
      if(direct){ Eband = cntB[i] - (long double)y*((0.5L+dl[i])*lx - (0.5L-dl[i])*lx);
                  Eband_h = cntB[i] - (long double)y*hB[i]; resid = Derr - (Eband + 2*FLc); resid_h = Derr - (Eband_h + 2*FLc); }
      else { Eband_h = Derr - 2*FLc; Eband = Eband_h; resid = NAN; resid_h = NAN; } /* proxy, = E_band + O(1) */
      printf(" | %.4Lf %.4Lf %.4Lf %.4Lf %.4Lf", Eband, Eband_h, FLc, resid, resid_h);
    }
    printf(" ||");
    for(int j=0;j<nb;j++) printf(" %.3Lf", cM[j]-(long double)y*hM[j]);
    printf("\n"); fflush(stdout);
  }
  return 0;
}
