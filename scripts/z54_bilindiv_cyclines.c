/* z54_bilindiv_cyclines.c — do 2-cycles sit on the major arcs of the strip? (Z54_BILINDIV §6.5, EVIDENCE)
   For each n (stdin), U = floor(n^{1/4}): build E1 (as in z54_bilindiv_td.c); for every 2-cycle level k (D_k = w^2,
   (s+-w)/2 in (U,2U]) compute r(k) := max #points of E1 on a line through (k, m_k) (r >= 2 if |E1| >= 2), and for a
   uniformly chosen control point of E1 (deterministic: index (n mod |E1|)) the same quantity.
   Prints per n with N2 > 0:  n U |E1| N2  then for each cycle "r"  and "ctrl r".  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef long long i64;
static u64 iroot4(u64 n){ u64 r=(u64)floor(pow((double)n,0.25)); while((u128)(r+1)*(r+1)*(r+1)*(r+1)<=n) r++; while((u128)r*r*r*r>n) r--; return r; }
static u64 isq(u64 x){ u64 r=(u64)sqrt((double)x); while(r*r>x) r--; while((r+1)*(r+1)<=x) r++; return r; }
static i64 gcdl(i64 a,i64 b){ if(a<0)a=-a; if(b<0)b=-b; while(b){i64 t=a%b;a=b;b=t;} return a; }
typedef struct { i64 a,b; } dir;
static int cmpd(const void*x,const void*y){ const dir*p=x,*q=y; if(p->a!=q->a) return p->a<q->a?-1:1; if(p->b!=q->b) return p->b<q->b?-1:1; return 0; }
static long richness(long i,long E,i64*K,i64*M,dir*D){ long c=0; for(long j=0;j<E;j++){ if(j==i) continue; i64 a=K[j]-K[i], b=M[j]-M[i]; i64 g=gcdl(a,b); a/=g; b/=g; if(a<0||(a==0&&b<0)){a=-a;b=-b;} D[c].a=a; D[c].b=b; c++; }
  qsort(D,c,sizeof(dir),cmpd); long best=1; for(long j=0;j<c;){ long t=j; while(t<c&&D[t].a==D[j].a&&D[t].b==D[j].b) t++; if(t-j+1>best) best=t-j+1; j=t; } return best; }
int main(void){ char line[128];
  while(fgets(line,sizeof line,stdin)){ u64 n=strtoull(line,0,10); u64 U=iroot4(n); u64 U2=U*U; if(16*U*U*U>n) continue;
    u64 klo=(n+2*U)/(4*U2); if(klo<1) klo=1; u64 khi=(n+4*U)/U2+1; long cap=16*U+100,E=0; i64 *K=malloc(sizeof(i64)*cap),*M=malloc(sizeof(i64)*cap); long cyc[64]; int nc=0;
    for(u64 k=klo;k<=khi;k++){ u64 r=n%k; u64 s=r?k-r:0; if(!(s>2*U&&s<=4*U)) continue; u64 m=(n+s)/k; if(!(m>U2&&m<=4*U2)) continue;
      i64 D=(i64)(s*s)-(i64)(4*m); if(D>=1){ u64 w=isq((u64)D); if(w*w==(u64)D){ u64 a=(s-w)/2,b=(s+w)/2; if(a>U&&a<=2*U&&b>U&&b<=2*U&&nc<64) cyc[nc++]=E; } }
      K[E]=(i64)k; M[E]=(i64)m; E++; }
    if(nc>0){ dir*D=malloc(sizeof(dir)*E); printf("%llu %llu %ld %d",n,U,E,nc); for(int c=0;c<nc;c++) printf(" r=%ld",richness(cyc[c],E,K,M,D)); printf(" ctrl=%ld\n",richness((long)(n%E),E,K,M,D)); free(D); }
    free(K); free(M); }
  return 0; }
