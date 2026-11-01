/* z53 HYPSUMPROD: numerical check of the square-sieve route for the near-cube count.
   For n, a C-range (W,2W] and an s-range (S1,S2]:
     A = {(C,k): C in (W,2W], s := 4Ck - n in (S1,S2]},  f(C,k) = s^2 - 4k.
   Checks: (i) #{(C,k) in A : f = square >= 0} == #{(u,B,C): 4uBC-u-B=n, C in (W,2W], u+B in (S1,S2]} (unordered {u,B}),
           by brute force over (u,B) when feasible;
   (ii) character sums S_Q = sum_{A} (f / q q') (Jacobi) for primes q != q' in a list, vs |A|/Q and |A|.
   Usage: sqsieve n W S1 S2 brute(0/1) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef __int128 i128;
static int jacobi(int64_t a, int64_t m){ /* m odd positive */
  a%=m; if(a<0)a+=m; int r=1;
  while(a){ while(!(a&1)){a>>=1; int64_t t=m&7; if(t==3||t==5) r=-r;}
    int64_t t=a;a=m;m=t; if((a&3)==3&&(m&3)==3) r=-r; a%=m;}
  return m==1?r:0;
}
static int issq(i128 x,int64_t*r){ if(x<0)return 0; int64_t s=(int64_t)sqrtl((long double)x); while((i128)s*s>x)s--; while((i128)(s+1)*(s+1)<=x)s++; *r=s; return (i128)s*s==x;}
int main(int argc,char**argv){
  int64_t n=atoll(argv[1]),W=atoll(argv[2]),S1=atoll(argv[3]),S2=atoll(argv[4]); int brute=atoi(argv[5]);
  int qs[]={101,103,107,109,113,211,223,227,229,401,409,419,1009,1013};
  int nq=sizeof(qs)/sizeof(int);
  static double S[20][20]; int64_t A=0,sq=0,sq0=0;
  for(int64_t C=W+1;C<=2*W;C++){
    int64_t klo=(n+S1)/(4*C)+1, khi=(n+S2)/(4*C); /* k in ((n+S1)/4C,(n+S2)/4C] */
    for(int64_t k=klo;k<=khi;k++){
      int64_t s=4*C*k-n; i128 f=(i128)s*s-4*(i128)k; A++;
      int64_t r; if(issq(f,&r)){ if(r==0)sq0++; else sq++; }
      for(int i=0;i<nq;i++)for(int j=i+1;j<nq;j++){
        int64_t Q=(int64_t)qs[i]*qs[j]; int64_t fm=(int64_t)(f%Q); S[i][j]+=jacobi(fm,Q);
      }
    }
  }
  printf("n=%ld W=%ld S=(%ld,%ld] |A|=%ld squares(f>0)=%ld f=0:%ld\n",n,W,S1,S2,A,sq,sq0);
  if(brute){ /* unordered {u,B}, u<B, plus u==B */
    int64_t cnt=0,cnt0=0;
    for(int64_t u=1;u<=S2;u++) for(int64_t B=u;B<=S2-u;B++){
      if(u+B<=S1)continue; int64_t m=n+u+B, q=4*u*B; if(m%q)continue; int64_t C=m/q; if(C<=W||C>2*W)continue;
      if(u==B)cnt0++; else cnt++; }
    printf("brute: unordered u<B: %ld, u==B: %ld  -> %s\n",cnt,cnt0,(cnt==sq&&cnt0==sq0)?"MATCH":"MISMATCH");
  }
  double mx=0,ms=0; int np=0;
  for(int i=0;i<nq;i++)for(int j=i+1;j<nq;j++){ double Q=(double)qs[i]*qs[j]; double v=fabs(S[i][j]); if(v>mx)mx=v; ms+=v*v; np++;
     if(np<=6) printf("  q=%d q'=%d S_Q=%.0f  |A|/Q=%.3f\n",qs[i],qs[j],S[i][j],A/Q); }
  printf("max|S_Q|=%.0f rms=%.1f  |A|=%ld  sqrt|A|=%.1f  ratio max|S|/|A|=%.4f\n",mx,sqrt(ms/np),A,sqrt((double)A),mx/A);
  return 0;
}
