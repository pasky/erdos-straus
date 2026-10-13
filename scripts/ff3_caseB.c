/* ff3_caseB.c (O173): fast exhaustive Case B search at slice points x == 1 off T, x == u mod T^inf.
   q = p prime (odd), A = T^k.  Case B (FUNCTIONFIELD_ES2 §0.2, FUNCTIONFIELD_ES3 §1): exists monic L' (T∤L'),
   j >= 0, 0 <= gam <= j, monic g' | L', and monic E | D := 1 + T^(N+1+gam) L' g' (N = k+j-1) with monic
   cofactor, E == -u (mod T^(N+1)), E == -1 (mod L').  Exactly one of E, E' := D/E has degree < N+1+deg L'
   (or both), and it equals the least CRT rep rho (resp. rho' for E' == -u^{-1}).  For each (L', j, branch)
   we compute v = -(T^(N+1) L')^{-1} mod rho and test t_gam = v T^{-gam} mod rho: need t monic, deg t <= deg L',
   t | L' (deg rho > deg L' is proved, so g' = t_gam exactly).
   usage: ff3_caseB p k LMIN LMAX JMAX u0 u1 u2 ...   (u digits low->high, at least 1)
   JMAX = -1: j <= 4 deg L' - k (the complete range at u = 1 + cT by FUNCTIONFIELD_ES3 Lemma 2.3)
   prints each hit: branch, L', j, gam, g', E (rho or rho').  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
static void trunc_(poly *a, int n){ if(a->d>=n){ a->d=n-1; norm(a);} }
static void pprint(const poly *a){ printf("["); for(int i=0;i<=a->d;i++) printf("%d%s",a->c[i],i<a->d?",":""); printf("]"); }
int main(int argc, char **argv){
  if(argc<7){ fprintf(stderr,"usage\n"); return 1; }
  P=atoi(argv[1]); int k=atoi(argv[2]), LMIN=atoi(argv[3]), LMAX=atoi(argv[4]), JMAX=atoi(argv[5]);
  for(int i=1;i<P;i++) for(int j=1;j<P;j++) if(i*j%P==1) inv_tab[i]=j;
  poly u; u.d=argc-7; for(int i=0;i<=u.d;i++) u.c[i]=((atoi(argv[6+i])%P)+P)%P; norm(&u);
  int NMAX = k+(JMAX>=0?JMAX:4*LMAX); if(NMAX+2>MX/2-LMAX){fprintf(stderr,"MX too small\n");return 1;} /* need u to precision T^(NMAX+1) */
  poly U; U.d = NMAX; for(int i=0;i<=NMAX;i++) U.c[i] = i<=u.d? u.c[i]:0; norm(&U);
  poly Ui; sinv(&Ui,&U,NMAX+1);
  long hits=0, tested=0;
  for(int l=LMIN;l<=LMAX;l++){
    long cnt=1; for(int i=0;i<l;i++) cnt*=P; long lh=0;
    for(long idx=0; idx<cnt; idx++){
      poly L; L.d=l; long x=idx; for(int i=0;i<l;i++){ L.c[i]=x%P; x/=P; } L.c[l]=1;
      if(L.c[0]==0) continue;
      int JM = JMAX>=0? JMAX : 4*l-k; /* JMAX<0: complete range j <= 4l-k (Lemma 2.3, x* only) */
      for(int j=0;j<=JM;j++){
        int N=k+j-1;
        poly Li; sinv(&Li,&L,N+1);
        for(int br=0;br<2;br++){
          /* target: E == -w mod T^(N+1), w = u (br 0) or u^{-1} (br 1); E = -1 + L h, h == (1-w)/L */
          poly w = br? Ui: U; trunc_(&w,N+1);
          poly one; one.d=0; one.c[0]=1; poly omw; psub(&omw,&one,&w);
          poly h; pmul(&h,&omw,&Li); trunc_(&h,N+1);
          if(h.d<0) continue;
          poly rho; pmul(&rho,&L,&h); rho.c[0]=(rho.c[0]+P-1)%P; if(rho.d<0){rho.d=0;} norm(&rho);
          if(rho.d<1 || rho.c[rho.d]!=1) continue; /* must be monic, nonconstant */
          if(rho.d<=l){ printf("WARN deg rho <= deg L' l=%d j=%d\n",l,j); continue; }
          tested++;
          /* v = -(T^(N+1) L)^{-1} mod rho */
          poly TN; TN.d=N+1; memset(TN.c,0,sizeof(int)*(N+2)); TN.c[N+1]=1;
          poly a; pmul(&a,&TN,&L); pmod_(&a,&rho);
          poly v; if(!pinvmod(&v,&a,&rho)) continue;
          for(int i=0;i<=v.d;i++) v.c[i]=(P-v.c[i])%P; norm(&v);
          int r0i = inv_tab[rho.c[0]];
          for(int gam=0; gam<=j; gam++){
            if(gam>0){ /* v = v * T^{-1} mod rho */
              if(v.d>=0 && v.c[0]){ int f=v.c[0]*r0i%P; for(int i=0;i<=rho.d;i++){ int y=(i<=v.d?v.c[i]:0)-f*rho.c[i]; y%=P; if(y<0)y+=P; v.c[i]=y; } v.d=rho.d; norm(&v); }
              if(v.d>=0){ for(int i=0;i<v.d;i++) v.c[i]=v.c[i+1]; v.d--; norm(&v);} }
            if(v.d<0 || v.d>l || v.c[v.d]!=1) continue;
            poly rem=L; pmod_(&rem,&v); if(rem.d>=0) continue;
            hits++; lh++;
            printf("HIT br=%d l=%d j=%d N=%d gam=%d L'=",br,l,j,N,gam); pprint(&L); printf(" g'="); pprint(&v);
            printf(" %s=", br?"E'":"E"); pprint(&rho); printf("\n"); fflush(stdout);
          }
        }
      }
    }
    printf("done l=%d hits_l=%ld total=%ld tested=%ld\n",l,lh,hits,tested); fflush(stdout);
  }
  return 0;
}
