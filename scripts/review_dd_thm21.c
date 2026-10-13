/* R176 from-scratch check of DIFF_DEEP Thm 2.1 (Type II <-> (f,f',c)).
   Tuple side (ET Type II, naive): a<=b, d>=1, e=4abd-n>0, e | a+b, c=(a+b)/e.
   Triple side: c,d>=1, h=4c^2 d <= H, M=4cd, N=1+n h, f|N, f<=f'=N/f, f==f'==-1 mod M
   (equivalent to n|ff'-1, 4c^2|h, h|cG since h=cM, d=h/4c^2).
   Compares the sets {(f,f',c)} exactly, for all odd n in [3,NMAX].  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
typedef struct { u64 f, g, c; } T;
static int cmp(const void*x,const void*y){const T*a=x,*b=y;
 if(a->f!=b->f)return a->f<b->f?-1:1; if(a->g!=b->g)return a->g<b->g?-1:1;
 if(a->c!=b->c)return a->c<b->c?-1:1; return 0;}
static T A[2000000], B[2000000];
int main(int argc,char**argv){
 int NMAX=atoi(argv[1]); long tot=0, mism=0; int sq=0, sqsol=0; u64 maxh_ratio_num=0;
 for(u64 n=3;n<=(u64)NMAX;n+=2){
  long na=0, nb=0; u64 maxh=0;
  for(u64 a=1;;a++){ if(4*a*a*1-1 > n+a && 4*a*a > n+2*a) break;
   for(u64 d=1;;d++){ u64 den=4*a*d-1; if(den*a > n+a) break; /* b>=a needs a(4ad-1)<=n+a */
    for(u64 b=a; b*den<=n+a; b++){ u64 P=4*a*b*d; if(P<=n) continue; u64 e=P-n;
      if((a+b)%e) continue; u64 c=(a+b)/e;
      A[na].f=4*a*c*d-1; A[na].g=4*b*c*d-1; A[na].c=c; na++;
      u64 h=4*c*c*d; if(h>maxh) maxh=h; }}}
  u64 H=(n+5)*(n+5); /* 4x the analytic bound (n+5)^2/4 */
  for(u64 c=1;4*c*c<=H;c++) for(u64 d=1;4*c*c*d<=H;d++){
    u64 h=4*c*c*d, M=4*c*d, N=1+n*h;
    for(u64 f=M-1; f*f<=N; f+=M){ if(N%f) continue; u64 g=N/f; if((g+1)%M) continue;
      B[nb].f=f;B[nb].g=g;B[nb].c=c;nb++; }}
  qsort(A,na,sizeof(T),cmp); qsort(B,nb,sizeof(T),cmp);
  int bad = (na!=nb);
  for(long i=0;!bad && i<na;i++) if(cmp(&A[i],&B[i])) bad=1;
  for(long i=1;i<na;i++) if(!cmp(&A[i],&A[i-1])) bad=2;
  u64 r=1; while((r+1)*(r+1)<=n) r++; int issq=(r*r==n);
  if(issq){sq++; if(na) sqsol++;}
  if(bad){mism++; printf("MISMATCH n=%llu tuples=%ld triples=%ld code=%d\n",n,na,nb,bad);}
  if(maxh*4 > (n+5)*(n+5)) printf("bound exceeded n=%llu maxh=%llu\n",n,maxh);
  tot+=na;
 }
 printf("n<=%d odd: total tuples %ld, mismatching n: %ld, odd squares %d (with solutions: %d)\n",NMAX,tot,mism,sq,sqsol);
 return 0;}
