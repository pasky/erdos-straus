/* Opus cross-review: independent re-implementation of the z80 large-shift P_K
   count (author used z78_r2cf.c), plus a brute-force mode for small cases.
   usage: z80_xr_cf r K E digitfile [brute]
   Counts t=acd in [1,floor((floor(N/E)+1)/2)] for which some unit tuple
   4abd=N+e, a+b=ce, a<=b, e>=E exists and the digit of 1-4t mod r is live
   (not a square, not 0, not in digitfile). Output: r count2 = 2*#t, plus
   diagnostics: #t with live digit, #t ignoring digit, mismatches between the
   digit status of the two orientations (inverse-stability check).
   CF mode: every convergent p/q of N/f (both parities) is tested with
   a := q*N - p*f taken with sign; no break, each t counted once.
   brute mode: for all a,c with ac<=T and d<=T/(ac): f=4acd-1, test f | cN+a. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
typedef uint64_t u64; typedef unsigned __int128 u128; typedef __int128 i128;
static u64 R; static u128 N; static u64 W; static u64 Ecut; static int dead[2000];
static u64 nmis, nboth;
/* given candidate (a,c,d) with f=4acd-1, b from b*f=c*N+a; return 1 if a genuine a<=b hit */
static int test(u64 a,u64 c,u64 d,u64 f,int *live){
  u128 num=(u128)c*N+a; if(num%f) return 0; u128 b=num/f; if(b<a) return 0;
  if((a+b)%c) return 0; u128 e=(a+b)/c; if(e<Ecut) return 0;
  if(a%R==0||b%R==0||c%R==0||d%R==0) return 0;
  assert((u128)4*a*b*d==N+e);
  u64 xa=(u64)((R*R*4-(u64)(((u128)4*a*c*d)%R))%R); xa=(xa+1)%R; /* 1-4acd mod r */
  u64 xb=(u64)((1+R-(u64)((((u128)4*(b%R))%R)*(c%R)%R*(d%R)%R))%R);
  if(dead[xa]!=dead[xb]) nmis++;
  { /* check inverse relation mod W */ u64 A=(u64)((1+W-(u64)(((u128)4*a*c*d)%W))%W), B=(u64)((1+W-(u64)((((u128)4*(b%W))%W)*(c%W)%W*(d%W)%W))%W); assert((u128)A*B%W==1%W); }
  *live=!dead[xa]; return 1; }
int main(int argc,char**argv){
  assert(argc==5||argc==6); R=strtoull(argv[1],0,10); int K=atoi(argv[2]); Ecut=strtoull(argv[3],0,10); int brute=argc==6; assert(R<2000);
  N=1; for(int i=0;i<K;i++) N*=R; W=1; for(int i=0;i<(K+1)/2;i++) W*=R;
  for(u64 x=0;x<R;x++) dead[x*x%R]=1;
  FILE*fp=fopen(argv[4],"r"); assert(fp); int x; while(fscanf(fp,"%d",&x)==1){assert(x>=0&&(u64)x<R);dead[x]=1;} fclose(fp);
  u64 T=(u64)(((N/Ecut)+1)/2);
  u64 tl=0, ta=0;
  if(!brute){
    for(u64 t=1;t<=T;t++){ u64 f=4*t-1; int hit=0, live=0;
      /* CF of N/f: x0=N, x1=f; convergents h_k/k_k; remainder q_k N - p_k f */
      u128 A=N, B=f; i128 p0=1,q0=0,p1=0,q1=1; /* p_{-1}=1,q_{-1}=0; p_{-2}=0,q_{-2}=1 */
      while(B){ u128 a=A/B, rr=A%B; i128 p2=(i128)a*p0+p1, q2=(i128)a*q0+q1; p1=p0;q1=q0;p0=p2;q0=q2; A=B;B=rr;
        /* convergent p0/q0 ~ N/f; candidate hit has b=p0, c=q0, a=b f - c N >0 */
        i128 av=(i128)p0*(i128)f-(i128)q0*(i128)N; if(av<=0) continue;
        u64 c=(u64)q0, aa=(u64)av; if((u128)aa*c>t) continue; if(t%((u128)aa*c)) continue; u64 d=t/(aa*c);
        int lv; if(test(aa,c,d,f,&lv)){ if(!hit){hit=1;live=lv;} } }
      if(hit){ ta++; if(live) tl++; } }
  } else {
    static char *seen; seen=calloc(T+1,1); static char *lv; lv=calloc(T+1,1);
    for(u64 a=1;a<=T;a++) for(u64 c=1;a*c<=T;c++) for(u64 d=1;a*c*d<=T;d++){ u64 t=a*c*d,f=4*t-1; int l; if(test(a,c,d,f,&l)){ seen[t]=1; if(l) lv[t]=1; } }
    for(u64 t=1;t<=T;t++){ if(seen[t]) ta++; if(lv[t]) tl++; }
  }
  printf("%lu %lu\n",R,2*tl);
  fprintf(stderr,"r=%lu K=%d E=%lu T=%lu live_t=%lu all_t=%lu orient_digit_mismatch=%lu mode=%s\n",R,K,Ecut,T,tl,ta,nmis,brute?"brute":"cf");
  (void)nboth; return 0; }
