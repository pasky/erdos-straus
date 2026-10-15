/* review_r248_caseB.c (R248, from scratch): enumerate ALL Case B tuples at q=3, k=2 with parameter s <= SMAX
   via the (w,C) parametrisation of FUNCTIONFIELD_ES3 Lemma 2.1 re-derived independently:
     L' = g'm' monic (T !| L'), w = T*w1, C = T*C1 monic, m'wC = T^s + v, w + C = g'v,
     deg v <= max(a,b) < a+b = deg(wC)  =>  m' = quotient(T^s, wC) is forced.
   Checks E*E' = 1 + T^s L' g' with E = L'w - 1, E' = L'C - 1 (both monic), and prints the ball of E:
     depth N+1 with N = ceil(s/2), digits of u = -E mod T^{N+1}.
   usage: review_r248_caseB SMAX > balls.txt   (lines: "s depth digits") */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MD 40
typedef struct { int d; int c[MD]; } P;   /* d = degree, -1 for zero */
static void norm(P *p){ while(p->d>=0 && p->c[p->d]==0) p->d--; }
static void mul(const P*a,const P*b,P*r){ P t; memset(&t,0,sizeof t); if(a->d<0||b->d<0){t.d=-1;*r=t;return;}
  t.d=a->d+b->d; for(int i=0;i<=a->d;i++) if(a->c[i]) for(int j=0;j<=b->d;j++) t.c[i+j]=(t.c[i+j]+a->c[i]*b->c[j])%3; norm(&t); *r=t; }
static void add(const P*a,const P*b,P*r){ P t; memset(&t,0,sizeof t); int d=a->d>b->d?a->d:b->d; t.d=d;
  for(int i=0;i<=d;i++){ int x=(i<=a->d?a->c[i]:0)+(i<=b->d?b->c[i]:0); t.c[i]=x%3;} norm(&t); *r=t; }
static void sub(const P*a,const P*b,P*r){ P nb=*b; for(int i=0;i<=nb.d;i++) nb.c[i]=(3-nb.c[i])%3; add(a,&nb,r); }
static int inv3(int x){ return x==1?1:2; }
static void divmod(const P*a,const P*b,P*q,P*r){ P R=*a, Q; memset(&Q,0,sizeof Q); Q.d=-1;
  if(R.d>=b->d){ Q.d=R.d-b->d; } int il=inv3(b->c[b->d]);
  while(R.d>=b->d){ int sh=R.d-b->d; int f=(R.c[R.d]*il)%3; Q.c[sh]=f;
    for(int i=0;i<=b->d;i++) R.c[i+sh]=(R.c[i+sh]+3*3-f*b->c[i])%3; norm(&R); }
  norm(&Q); *q=Q; *r=R; }
static void mono(int s,P*r){ memset(r,0,sizeof *r); r->d=s; r->c[s]=1; }
/* enumerate monic polys of degree d with nonzero constant term: index -> poly */
static int npoly(int d){ if(d==0) return 1; int n=2; for(int i=1;i<d;i++) n*=3; return n; }
static void mkpoly(int d,int idx,P*r){ memset(r,0,sizeof *r); r->d=d; r->c[d]=1; if(d==0) return;
  r->c[0]=1+(idx%2); idx/=2; for(int i=1;i<d;i++){ r->c[i]=idx%3; idx/=3; } }
int main(int argc,char**argv){ int SMAX=atoi(argv[1]); long ntup=0;
  for(int t=3;t<=SMAX;t++) for(int a=1;a<t;a++){ int b=t-a; if(b<1) continue;
    int nw=npoly(a-1), nc=npoly(b-1);
    for(int iw=0;iw<nw;iw++){ P w1; mkpoly(a-1,iw,&w1); P w; mono(1,&w); mul(&w,&w1,&w);
     for(int ic=0;ic<nc;ic++){ P C1; mkpoly(b-1,ic,&C1); P C; mono(1,&C); mul(&C,&C1,&C);
      P wC; mul(&w,&C,&wC); P wpc; add(&w,&C,&wpc);
      for(int s=t;s<=SMAX;s++){ P Ts,mq,rem,v; mono(s,&Ts); divmod(&Ts,&wC,&mq,&rem);
        if(mq.c[0]==0) continue;                      /* T | m' => T | L' */
        P prod; mul(&mq,&wC,&prod); sub(&prod,&Ts,&v); if(v.d<0) continue;
        if(v.d> (a>b?a:b)) continue;
        if(wpc.d<0) continue; P g,r2; divmod(&wpc,&v,&g,&r2); if(r2.d>=0) continue;
        if(g.d<0||g.c[g.d]!=1||g.c[0]==0) continue;    /* g' monic, T !| g' */
        P L; mul(&g,&mq,&L); P one; mono(0,&one);
        P E,Ep; mul(&L,&w,&E); sub(&E,&one,&E); mul(&L,&C,&Ep); sub(&Ep,&one,&Ep);
        /* sanity: E*E' == 1 + T^s L' g' */
        P EE,D,Lg; mul(&E,&Ep,&EE); mul(&L,&g,&Lg); mul(&Ts,&Lg,&D); add(&D,&one,&D); P df; sub(&EE,&D,&df);
        if(df.d>=0){ fprintf(stderr,"identity fail\n"); return 1; }
        if(E.c[E.d]!=1||Ep.c[Ep.d]!=1){ fprintf(stderr,"non-monic\n"); return 1; }
        int N=(s+1)/2, dep=N+1; printf("%d %d ",s,dep);
        for(int i=0;i<dep;i++){ int x=(i<=E.d?E.c[i]:0); printf("%d",(3-x)%3); } if(getenv("FULL")){ printf(" a=%d b=%d E=",a,b); for(int i=0;i<=E.d;i++) printf("%d",E.c[i]);
          printf(" w1="); for(int i=0;i<=w1.d;i++) printf("%d",w1.c[i]); printf(" C1="); for(int i=0;i<=C1.d;i++) printf("%d",C1.c[i]); }
        printf("\n"); ntup++;
      } } } }
  fprintf(stderr,"tuples %ld\n",ntup); return 0; }
