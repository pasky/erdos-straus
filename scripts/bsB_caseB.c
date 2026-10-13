/* bsB_caseB.c (O175, SIGNLAYER_DEEP Lemma 1.1): enumerate all Case B families on the slice x = 1 off T,
   q = 3, A = T^2, via (h1, h1', K):  h1+h1' = T g' r,  h1 h1' L'' = T^K + r,  L' = g' L''.
   For each solution print  K a b w  where w = h1*L' mod T^(K+1) (digits low->high); the family covers
   u = 1 + T v with v = -w (mod T^N) for any N in [max(2,ceil(K/2)+1), K+1].
   usage: bsB_caseB KMAX  (prints solutions, then a summary line "#K count")                          */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MX 80
typedef struct { int d; unsigned char c[MX]; } P;   /* coeffs mod 3, d = degree (-1 for zero) */
static void norm(P*a){ while(a->d>=0 && a->c[a->d]==0) a->d--; }
static void mul(const P*a,const P*b,P*r){ P t; memset(&t,0,sizeof t); if(a->d<0||b->d<0){t.d=-1;*r=t;return;}
  for(int i=0;i<=a->d;i++) if(a->c[i]) for(int j=0;j<=b->d;j++) t.c[i+j]=(t.c[i+j]+a->c[i]*b->c[j])%3;
  t.d=a->d+b->d; norm(&t); *r=t; }
/* divide a by monic b: q, rem */
static void divmonic(const P*a,const P*b,P*q,P*rm){ P r=*a, qq; memset(&qq,0,sizeof qq); qq.d=-1;
  if(r.d>=b->d){ qq.d=r.d-b->d; }
  for(int i=r.d;i>=b->d;i--){ int co=r.c[i]; if(!co) continue; qq.c[i-b->d]=co;
     for(int j=0;j<=b->d;j++) r.c[i-b->d+j]=(r.c[i-b->d+j]+3*3-co*b->c[j])%3; }
  norm(&r); norm(&qq); if(q)*q=qq; if(rm)*rm=r; }
static int KMAX; static long cnt[MX];
static P h1,h2;
static void test_pair(void){
  int a=h1.d,b=h2.d; P s; memset(&s,0,sizeof s); int ds=a>b?a:b;
  for(int i=0;i<=ds;i++) s.c[i]=(h1.c[i]+h2.c[i])%3; s.d=ds; norm(&s);
  if(s.d<1 || s.c[0]) return;                     /* T | s, s != 0 */
  P sT; memset(&sT,0,sizeof sT); sT.d=s.d-1; for(int i=0;i<=sT.d;i++) sT.c[i]=s.c[i+1];
  P Pp; mul(&h1,&h2,&Pp);
  /* rem = T^K mod Pp, start K=a+b */
  P rem; memset(&rem,0,sizeof rem); rem.d=-1;
  { P tk; memset(&tk,0,sizeof tk); tk.d=a+b; tk.c[a+b]=1; divmonic(&tk,&Pp,NULL,&rem); }
  for(int K=a+b; K<=KMAX; K++){
    if(K>a+b){ /* rem *= T mod Pp */ P t; memset(&t,0,sizeof t); if(rem.d>=0){ t.d=rem.d+1; for(int i=0;i<=rem.d;i++) t.c[i+1]=rem.c[i]; }
      else t.d=-1; divmonic(&t,&Pp,NULL,&rem); }
    if(rem.d<0) continue; if(rem.d>sT.d) continue;
    P r=rem; for(int i=0;i<=r.d;i++) r.c[i]=(3-r.c[i])%3;           /* r = -rem */
    if(r.c[r.d]!=sT.c[sT.d]) continue;                                /* g' monic */
    /* g' = sT / r exactly */
    int inv = r.c[r.d]==1?1:2; P rm=r; for(int i=0;i<=rm.d;i++) rm.c[i]=(rm.c[i]*inv)%3;  /* monic version */
    P g,re; divmonic(&sT,&rm,&g,&re); if(re.d>=0) continue;
    /* g' = g * inv  (sT = g*rm = g*inv*r) => g' = g*inv; must be monic */
    for(int i=0;i<=g.d;i++) g.c[i]=(g.c[i]*inv)%3; if(g.c[g.d]!=1 || g.c[0]==0) continue;
    P tk,L2; memset(&tk,0,sizeof tk); tk.d=K; tk.c[K]=1; divmonic(&tk,&Pp,&L2,NULL);
    if(L2.d<0 || L2.c[0]==0) continue;
    P L1,w; mul(&g,&L2,&L1); mul(&h1,&L1,&w);
    cnt[K]++;
    printf("%d %d %d ",K,a,b); for(int i=0;i<=K;i++) putchar('0'+(i<=w.d?w.c[i]:0)); putchar('\n');
  }
}
static void rec2(int i){ /* fill h2 coefficients 1..h2.d-1 */
  if(i>=h2.d){ test_pair(); return; } for(int x=0;x<3;x++){ h2.c[i]=x; rec2(i+1);} }
static void rec1(int i){
  if(i>=h1.d){ for(int b=0; h1.d+b<=KMAX; b++){ memset(&h2,0,sizeof h2); h2.d=b; h2.c[b]=1;
        h2.c[0]=(3-h1.c[0])%3; if(b==0 && h2.c[0]!=1) continue; if(b==0){ test_pair(); continue;} rec2(1);} return; }
  for(int x=0;x<3;x++){ h1.c[i]=x; rec1(i+1);} }
int main(int argc,char**argv){ KMAX=atoi(argv[1]);
  for(int a=0;a<=KMAX;a++) for(int c0=1;c0<=2;c0++){ memset(&h1,0,sizeof h1); h1.d=a; h1.c[a]=1; h1.c[0]=c0;
      if(a==0 && c0!=1) continue; if(a==0){ /* h1 = 1 */ for(int b=0;b<=KMAX;b++){ memset(&h2,0,sizeof h2); h2.d=b; h2.c[b]=1; h2.c[0]=2; if(b==0) continue; rec2(1);} continue; }
      rec1(1); }
  for(int K=0;K<=KMAX;K++) fprintf(stderr,"#K %d count %ld\n",K,cnt[K]);
  return 0; }
