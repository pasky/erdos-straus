/* z54_bilindiv_geom.c — geometry of the strip set E1 and one-sided anatomy filters (Z54_BILINDIV §4.3, §4.5).
   For each n (stdin), U = floor(n^{1/4}) (or argv[1] if > 0):
     E1 points (k,m): n+2U < k*m <= n+4U, U^2 < m <= 4U^2  (all, including D < 0)
     L3 = #lines (in the (k,m)-plane) containing >= 3 points of E1; Lmax = max #points of E1 on one line;
     W  = max #points of E1 with k in a window of length floor(U^{2/3}) (Pick: such points are collinear, §4.5)
     P1 = #{(u,B) in (U,2U]^2 : B | n+u};  A1 = #{u : n+u has a divisor in (U,2U]};  A2 = |dom f| = #{u : some B in (U,2U] has u | n+B}
   Prints: n U |E1| L3 Lmax W P1 A1 A2 (P1, A1, A2 also divided by U), cov3 = #E1 points on some line with >= 3 points, dir = direction of a longest line  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef long long i64;
static u64 iroot4(u64 n){ u64 r=(u64)floor(pow((double)n,0.25)); while((u128)(r+1)*(r+1)*(r+1)*(r+1)<=n) r++; while((u128)r*r*r*r>n) r--; return r; }
static i64 gcdl(i64 a,i64 b){ if(a<0)a=-a; if(b<0)b=-b; while(b){i64 t=a%b;a=b;b=t;} return a; }
typedef struct { i64 a,b; } dir;
static int cmpd(const void*x,const void*y){ const dir*p=x,*q=y; if(p->a!=q->a) return p->a<q->a?-1:1; if(p->b!=q->b) return p->b<q->b?-1:1; return 0; }
int main(int argc,char**argv){ long Ufix=argc>1?atol(argv[1]):0; char line[128];
  while(fgets(line,sizeof line,stdin)){ u64 n=strtoull(line,0,10); u64 U=Ufix>0?(u64)Ufix:iroot4(n); u64 U2=U*U;
    u64 klo=(n+2*U)/(4*U2); if(klo<1) klo=1; u64 khi=(n+4*U)/U2+1;
    long cap=16*U+100, E=0; i64 *K=malloc(sizeof(i64)*cap), *M=malloc(sizeof(i64)*cap);
    for(u64 k=klo;k<=khi;k++){ u64 r=n%k; u64 s=r?k-r:0; if(!(s>2*U&&s<=4*U)) continue; u64 m=(n+s)/k; if(!(m>U2&&m<=4*U2)) continue;
      if(E<cap){K[E]=(i64)k;M[E]=(i64)m;E++;} }
    /* lines: for each i, directions to j>i, normalised; a line with t points is seen from its first point with t-1 equal directions */
    dir *D=malloc(sizeof(dir)*E); long L3=0; long Lmax=(E>=2)?2:E; char *cov=calloc(E+1,1); i64 ba=0,bb=0;
    for(long i=0;i<E;i++){ long c=0; for(long j=i+1;j<E;j++){ i64 a=K[j]-K[i], b=M[j]-M[i]; i64 g=gcdl(a,b); a/=g; b/=g; if(a<0||(a==0&&b<0)){a=-a;b=-b;} D[c].a=a; D[c].b=b; c++; }
      qsort(D,c,sizeof(dir),cmpd);
      for(long j=0;j<c;){ long t=j; while(t<c&&D[t].a==D[j].a&&D[t].b==D[j].b) t++; long cnt=t-j+1; if(cnt>=3){ /* count line once: only if i is its first point: check no earlier point on it */
            int first=1; for(long q=0;q<i;q++){ i64 a=K[i]-K[q], b=M[i]-M[q]; if(a*D[j].b==b*D[j].a){first=0;break;} } if(first){L3++; if(cnt>Lmax){Lmax=cnt;ba=D[j].a;bb=D[j].b;} cov[i]=1; for(long q=i+1;q<E;q++){ i64 a=K[q]-K[i], b=M[q]-M[i]; if(a*D[j].b==b*D[j].a) cov[q]=1; } } }
        j=t; } }
    long Wl=(long)floor(pow((double)U,2.0/3.0)), W=0; for(long i=0,j=0;i<E;i++){ while(K[i]-K[j]>=Wl) j++; if(i-j+1>W) W=i-j+1; }
    /* anatomy filters */
    long P1=0,A1=0,A2=0; char *has=calloc(2*U+2,1);
    for(u64 B=U+1;B<=2*U;B++){ u64 r=n%B; u64 u=r?B-r:0; while(u<=U) u+=B; if(u<=2*U){P1++; has[u]=1;} }
    for(u64 u=U+1;u<=2*U;u++){ A1+=has[u]; u64 r=n%u; u64 B=r?u-r:0; while(B<=U) B+=u; if(B<=2*U) A2++; }
    long C3=0; for(long i=0;i<E;i++) C3+=cov[i]; printf("%llu %llu %ld %ld %ld %ld %ld %ld %ld  %.3f %.3f %.3f  cov3=%ld dir=(%lld,%lld)\n",n,U,E,L3,Lmax,W,P1,A1,A2,(double)P1/U,(double)A1/U,(double)A2/U,C3,(long long)ba,(long long)bb); free(cov); fflush(stdout);
    free(K);free(M);free(D);free(has); }
  return 0; }
