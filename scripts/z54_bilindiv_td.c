/* z54_bilindiv_td.c — strip-form square detection sums (Z54_BILINDIV §3, hypothesis TD).
   For each odd n (stdin) and U = floor(n^{1/4}) (or argv[2] if > 0):
     E1 := { k : n+2U < k*m <= n+4U for an integer m with U^2 < m <= 4U^2 }  (s := k*m - n, m = (n+s)/k)
     D_k := s^2 - 4m ;  E1+ := { k in E1 : D_k >= 1 } ;  w_k := sqrt(D_k)
     T(h) := sum_{k in E1+} e(h w_k),  1 <= h <= H (argv[1])
   N2 := #{k in E1+ : D_k = w^2, (s +- w)/2 in (U,2U]}  (2-cycles; Lemma A of Z53_HYP2CYCLE), N4 := those with 4|k.
   Prints: n U |E1| |E1+| N2 N4 max_h|T|/sqrt|E1+| argmax rms_h|T|/sqrt|E1+| |T(1)|/sqrt
   Exact integer arithmetic for s, m, D; double only for sqrt(D) and the phases.  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef long long i64;
static u64 iroot4(u64 n){ u64 r=(u64)floor(pow((double)n,0.25)); while((u128)(r+1)*(r+1)*(r+1)*(r+1)<=n) r++; while((u128)r*r*r*r>n) r--; return r; }
static u64 isq(u64 x){ u64 r=(u64)sqrt((double)x); while(r*r>x) r--; while((r+1)*(r+1)<=x) r++; return r; }
int main(int argc,char**argv){ int H=atoi(argv[1]); long Ufix=argc>2?atol(argv[2]):0; char line[128];
  double complex *T=malloc(sizeof(double complex)*(H+1));
  while(fgets(line,sizeof line,stdin)){ u64 n=strtoull(line,0,10); if(n<5) continue; u64 U=Ufix>0?(u64)Ufix:iroot4(n);
    u64 U2=U*U; u64 klo=(n+2*U)/(4*U2); if(klo<1) klo=1; u64 khi=(n+4*U)/(U2)+1;
    for(int h=0;h<=H;h++) T[h]=0; long e1=0,e1p=0,N2=0,N4=0;
    for(u64 k=klo;k<=khi;k++){ u64 r=n%k; u64 s=(r==0)?0:k-r; /* s = (-n) mod k */
      if(!(s>2*U && s<=4*U)) continue; u64 m=(n+s)/k; if(!(m>U2 && m<=4*U2)) continue; e1++;
      i64 D=(i64)(s*s)-(i64)(4*m); if(D<1) continue; e1p++;
      u64 w=isq((u64)D); if(w*w==(u64)D){ u64 a=(s-w)/2,b=(s+w)/2; if(a>U&&a<=2*U&&b>U&&b<=2*U){N2++; if(k%4==0)N4++;} }
      double x=sqrt((double)D); double complex z=cexp(2*M_PI*I*fmod(x,1.0)), zz=z;
      for(int h=1;h<=H;h++){ T[h]+=zz; zz*=z; } }
    double best=0,ss=0; int bh=0; double sq=sqrt((double)(e1p>0?e1p:1));
    for(int h=1;h<=H;h++){ double v=cabs(T[h])/sq; ss+=v*v; if(v>best){best=v;bh=h;} }
    printf("%llu %llu %ld %ld %ld %ld %.3f %d %.3f %.3f\n",n,U,e1,e1p,N2,N4,best,bh,sqrt(ss/H),cabs(T[1])/sq); fflush(stdout); }
  return 0; }
