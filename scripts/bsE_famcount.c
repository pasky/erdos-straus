/* bsE_famcount.c (O178): exhaustive enumeration of all Case B tuples (m', g', w, C) with parameter s
   (FUNCTIONFIELD_ES3 Lemma 2.1: m'wC = T^s + v, w + C = g'v, all monic, T || w, T || C, T ∤ m'g', v != 0),
   over F_p (p odd prime), by enumerating ordered (w, C) with deg w + deg C <= s and putting v = (-T^s) mod wC.
   For each tuple it checks the reconstruction identities of DEPTH_ASPECT Lemma 2.2:
     E := g'm'w - 1 divides g'T^s + w  and  T^s + m'w^2;   E' := g'm'C - 1 divides g'T^s + C, T^s + m'C^2;
     E*E' = 1 + T^s L' g'.
   Output per s: number of tuples, split by c = -L'(0) w1(0) (the T-digit of the slice point), the largest
   degree pattern, and the covered relative mass sum_tuples q^{1 - N(s)}, N(s) = ceil((s+k-2)/2) (Lemma 3.1:
   one maximal cylinder per tuple).
   usage: bsE_famcount p k SMAX [print]   */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MX 256
typedef struct { int d; int c[MX]; } poly; /* d = degree, -1 for zero */
static int P;
static int inv_tab[64];
static void norm(poly *a){ while(a->d>=0 && a->c[a->d]==0) a->d--; }
static void pmod_(poly *r, const poly *b){ /* r = r mod b */
  int il = inv_tab[b->c[b->d]];
  while(r->d >= b->d){ int f = r->c[r->d]*il % P; int s = r->d - b->d;
    for(int i=0;i<=b->d;i++){ r->c[s+i] = (r->c[s+i] - f*b->c[i]) % P; if(r->c[s+i]<0) r->c[s+i]+=P; }
    norm(r); }
}
static void pmul(poly *r, const poly *a, const poly *b){
  poly t; if(a->d<0||b->d<0){ r->d=-1; return; }
  t.d = a->d+b->d; memset(t.c,0,sizeof(int)*(t.d+1));
  for(int i=0;i<=a->d;i++) if(a->c[i]) for(int j=0;j<=b->d;j++) t.c[i+j]=(t.c[i+j]+a->c[i]*b->c[j])%P;
  norm(&t); *r = t;
}
static void psub(poly *r, const poly *a, const poly *b){
  poly t; int d = a->d > b->d ? a->d : b->d; t.d=d;
  for(int i=0;i<=d;i++){ int x = (i<=a->d?a->c[i]:0) - (i<=b->d?b->c[i]:0); x%=P; if(x<0)x+=P; t.c[i]=x; }
  norm(&t); *r=t;
}
/* inverse of a mod m (gcd must be 1); returns 0 if not invertible */
static int pinvmod(poly *res, const poly *a, const poly *m){
  poly r0=*m, r1=*a, s0, s1; s0.d=-1; s1.d=0; s1.c[0]=1; pmod_(&r1,m);
  while(r1.d>=0){
    /* q = r0 / r1 */
    poly q; q.d = r0.d - r1.d; if(q.d<0){ q.d=-1; }
    else { memset(q.c,0,sizeof(int)*(q.d+1)); poly rr=r0; int il=inv_tab[r1.c[r1.d]];
      while(rr.d>=r1.d){ int f=rr.c[rr.d]*il%P; int s=rr.d-r1.d; q.c[s]=f;
        for(int i=0;i<=r1.d;i++){ rr.c[s+i]=(rr.c[s+i]-f*r1.c[i])%P; if(rr.c[s+i]<0) rr.c[s+i]+=P; } norm(&rr); }
      norm(&q); }
    poly rem=r0; pmod_(&rem,&r1); poly tq; pmul(&tq,&q,&s1); poly ns; psub(&ns,&s0,&tq);
    r0=r1; r1=rem; s0=s1; s1=ns;
  }
  if(r0.d!=0) return 0;
  int il=inv_tab[r0.c[0]]; for(int i=0;i<=s0.d;i++) s0.c[i]=s0.c[i]*il%P; *res=s0; pmod_(res,m); return 1;
}
/* power series inverse of a (a(0)!=0) mod T^n */
static void sinv(poly *r, const poly *a, int n){
  int a0i = inv_tab[a->c[0]]; r->d = n-1;
  for(int i=0;i<n;i++){ int s=0; for(int j=1;j<=i && j<=a->d;j++) s += a->c[j]*r->c[i-j]; s%=P;
    int v = (i==0?1:0) - s; v%=P; if(v<0)v+=P; r->c[i]=v*a0i%P; }
  norm(r);
}
static void padd(poly *r, const poly *a, const poly *b){
  poly t; int d = a->d > b->d ? a->d : b->d; t.d=d;
  for(int i=0;i<=d;i++){ int x = (i<=a->d?a->c[i]:0) + (i<=b->d?b->c[i]:0); t.c[i]=x%P; }
  norm(&t); *r=t;
}
static void pdivq(poly *qq, const poly *a, const poly *b){ /* qq = a / b (exact or floor) */
  poly rr=*a; qq->d = a->d - b->d; if(qq->d<0){ qq->d=-1; return; }
  memset(qq->c,0,sizeof(int)*(qq->d+1)); int il=inv_tab[b->c[b->d]];
  while(rr.d>=b->d){ int f=rr.c[rr.d]*il%P; int s=rr.d-b->d; qq->c[s]=f;
    for(int i=0;i<=b->d;i++){ rr.c[s+i]=(rr.c[s+i]-f*b->c[i])%P; if(rr.c[s+i]<0) rr.c[s+i]+=P; } norm(&rr); }
  norm(qq);
}
static int divides(const poly *e, const poly *f){ poly r=*f; pmod_(&r,e); return r.d<0; }
static void mono(poly *a, int d){ a->d=d; memset(a->c,0,sizeof(int)*(d+1)); a->c[d]=1; }
static void pprint(const poly *a){ printf("["); for(int i=0;i<=a->d;i++) printf("%d%s",a->c[i],i<a->d?",":""); printf("]"); }
/* enumerate monic w = T*w1, deg w = a, w1(0) != 0 : index -> poly */
static long nW(int a){ if(a==1) return 1; long n=P-1; for(int i=0;i<a-2;i++) n*=P; return n; }
static void mkW(poly *w, int a, long idx){ w->d=a; memset(w->c,0,sizeof(int)*(a+1)); w->c[a]=1;
  if(a==1) return; w->c[1]=1+idx%(P-1); idx/=(P-1); for(int i=2;i<a;i++){ w->c[i]=idx%P; idx/=P; } }
int main(int argc,char**argv){
  P=atoi(argv[1]); int k=atoi(argv[2]), SMAX=atoi(argv[3]); int pr = argc>4;
  for(int i=1;i<P;i++) for(int j=1;j<P;j++) if(i*j%P==1) inv_tab[i]=j;
  double totmass=0;
  for(int s=2;s<=SMAX;s++){
    long cnt=0, cntc[64]={0}, bad=0, nonmonic_g=0; int best[6]={0}; double bestv=-1;
    poly Ts; mono(&Ts,s);
    for(int a=1;a<s;a++) for(int b=1;a+b<=s;b++){
      long na=nW(a), nb=nW(b);
      for(long ia=0;ia<na;ia++){ poly w; mkW(&w,a,ia);
        for(long ib=0;ib<nb;ib++){ poly C; mkW(&C,b,ib);
          poly wC; pmul(&wC,&w,&C);
          poly v=Ts; pmod_(&v,&wC); for(int i=0;i<=v.d;i++) v.c[i]=(P-v.c[i])%P; /* v = -T^s mod wC */
          if(v.d<0) continue;
          poly sum; padd(&sum,&w,&C); if(sum.d<0) continue;
          if(!divides(&v,&sum)) continue;
          poly g; pdivq(&g,&sum,&v);
          poly num; padd(&num,&Ts,&v); poly m; pdivq(&m,&num,&wC);
          if(m.c[0]==0 || g.c[0]==0) continue;            /* T ∤ L' */
          if(g.c[g.d]!=1){ nonmonic_g++; continue; }       /* g' monic */
          cnt++;
          poly L; pmul(&L,&g,&m); poly E; pmul(&E,&L,&w); E.c[0]=(E.c[0]+P-1)%P; norm(&E);
          poly Ep; pmul(&Ep,&L,&C); Ep.c[0]=(Ep.c[0]+P-1)%P; norm(&Ep);
          /* identities */
          poly x1; pmul(&x1,&g,&Ts); padd(&x1,&x1,&w); poly x2; pmul(&x2,&w,&w); pmul(&x2,&x2,&m); padd(&x2,&x2,&Ts);
          poly y1; pmul(&y1,&g,&Ts); padd(&y1,&y1,&C); poly y2; pmul(&y2,&C,&C); pmul(&y2,&y2,&m); padd(&y2,&y2,&Ts);
          poly D; pmul(&D,&Ts,&L); pmul(&D,&D,&g); D.c[0]=(D.c[0]+1)%P; if(D.d<0)D.d=0; norm(&D);
          poly EE; pmul(&EE,&E,&Ep); psub(&EE,&EE,&D);
          if(!divides(&E,&x1)||!divides(&E,&x2)||!divides(&Ep,&y1)||!divides(&Ep,&y2)||EE.d>=0||E.c[E.d]!=1) bad++;
          int c = (P - L.c[0]*w.c[1]%P)%P; cntc[c]++;
          int t=v.d;
          if(pr){ printf("s=%d a=%d b=%d mu=%d y=%d t=%d c=%d w=",s,a,b,m.d,g.d,t,c); pprint(&w); printf(" C="); pprint(&C);
                  printf(" m'="); pprint(&m); printf(" g'="); pprint(&g); printf(" E="); pprint(&E); printf("\n"); }
        } }
    }
    int N = (s+k-2+1)/2; double mass = cnt*pow(P,1-N)/(P-1); /* per c-slice, averaged over the P-1 values of c */
    totmass += mass;
    printf("s=%d tuples=%ld (bad identities %ld, nonmonic g' %ld) N(s)=%d  per-c:",s,cnt,bad,nonmonic_g,N);
    for(int c=1;c<P;c++) printf(" %ld",cntc[c]);
    printf("  mean rel. mass in a c-slice %.5f, cumulative %.5f\n",mass,totmass); fflush(stdout);
  }
  return 0;
}
