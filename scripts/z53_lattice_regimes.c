/* z53_lattice_regimes.c — enumerate all (*) solutions (u,B,C) of 4uBC - u - B = n (ordered triples),
   and split them by the Lenstra / Coppersmith-Howgrave-Graham-Nagaraj (CHN) regimes of the three
   one-coordinate slices:
     C-slice : divisors of N_C = 4Cn+1 that are = -1 mod s=4C   (Lenstra: s^3 > N_C ; CHN: s^4 > N_C)
     u-slice : divisors of n+u that are = -1 mod s=4u          (B = (n+u)/(4uC-1))  same thresholds with N = n+u
   Also prints, for n = a^2+b^2 (a>b>0 when n prime = 1 mod 4), the Thue-lattice angle ratio b/a and the
   near-square defect n - floor(sqrt n)^2.
   Usage: z53_lattice_regimes n1 n2 ...      (reads n from argv; or "-f file")
   Output per n: n R  cL cC  uL uC  anyC  b/a  defect      (cL = #solutions in C-Lenstra regime, etc.)  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef __int128 i128;
static int nd; static u64 divs[100000];
static void divisors(u64 m){ /* trial division */
  u64 pr[64]; int ex[64], k=0; u64 x=m;
  for(u64 d=2; d*d<=x; d+= (d==2?1:2)){ if(x%d==0){ pr[k]=d; ex[k]=0; while(x%d==0){x/=d; ex[k]++;} k++; } }
  if(x>1){ pr[k]=x; ex[k]=1; k++; }
  nd=1; divs[0]=1;
  for(int i=0;i<k;i++){ int cur=nd; u64 pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pp; } }
}
static int big(i128 s, int e, i128 N){ i128 v=1; for(int i=0;i<e;i++) v*=s; return v>N; }
static void doit(u64 n){
  long R=0, cL=0, cC=0, uL=0, uC=0, anyC=0, anyL=0;
  for(u64 u=1; 4*u*u <= n+2*u; u++){
    divisors(n+u);
    for(int i=0;i<nd;i++){ u64 B=divs[i]; if(B<u) continue;
      i128 num=(i128)n+u+B, den=(i128)4*u*B; if(num%den) continue;
      u64 C=(u64)(num/den);
      /* ordered: (u,B,C) and (B,u,C) if u!=B */
      int mult = (u==B)?1:2; R+=mult;
      i128 NC=(i128)4*C*n+1, s=4*(i128)C;
      int inCL=big(s,3,NC), inCC=big(s,4,NC);
      /* u-slice for (u,B,C): N=n+u, s=4u ; for (B,u,C): N=n+B, s=4B */
      int a1L=big(4*(i128)u,3,(i128)n+u), a1C=big(4*(i128)u,4,(i128)n+u);
      int a2L=big(4*(i128)B,3,(i128)n+B), a2C=big(4*(i128)B,4,(i128)n+B);
      cL+=mult*inCL; cC+=mult*inCC;
      uL+= a1L + (u!=B)*a2L; uC+= a1C + (u!=B)*a2C;   /* triple counted in its own u-slice */
      /* visible in some slice (C, u or B): */
      int vC = inCC || a1C || a2C, vL = inCL || a1L || a2L;
      anyC+=mult*vC; anyL+=mult*vL;
    }
  }
  /* Thue: n = a^2+b^2 */
  double ratio=-1; u64 r=(u64)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++;
  for(u64 a=r; a>0 && 2*a*a>=n; a--){ u64 b2=n-a*a; u64 b=(u64)sqrtl((long double)b2); while(b*b>b2)b--; while((b+1)*(b+1)<=b2)b++; if(b*b==b2){ ratio=(double)b/a; break; } }
  printf("%llu %ld %ld %ld %ld %ld %ld %ld %.6f %llu\n", n, R, cL, cC, uL, uC, anyL, anyC, ratio, n-r*r);
}
int main(int argc,char**argv){
  if(argc>2 && argv[1][0]=='-' && argv[1][1]=='f'){ FILE*f=fopen(argv[2],"r"); u64 n; while(fscanf(f,"%llu",&n)==1) doit(n); return 0; }
  for(int i=1;i<argc;i++) doit(strtoull(argv[i],0,10));
  return 0;
}
