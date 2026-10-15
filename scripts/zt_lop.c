/* zt_lop.c (O227): COMPLETE search for Case B tuples covering a polynomial slice point x_u (u(0) = 1),
   level by level, using the Liouville lemma (FF_THIRDS_CORNER Lemma 1.2) and the case split of §2.

   Tuple (FF_STERILE_PUSH (B)):  m' w1 C1 = T^{s-2} + v1,  w1 + C1 = T g' v1,  all of m', g', w1, C1 monic,
   T does not divide m' g' w1 C1 v1;  E = T g' m' w1 - 1,  E' = T g' m' C1 - 1.
   Covers x_u at level N = N(s) = ceil((s+k-2)/2) iff E == -u (mod T^{N+1}) (equivalently E' == -u^{-1}).
   Lemma 1.2: (if N+1 <= s-1) either w1 = -u C1 (exact; handled elsewhere) or
     orientation A: b >= N+2-h  (deg M <= s-N-3+h for M = m' w1, small side X1 = w1, big side X2 = C1, Ehat = E,
                                  target class tau = -u), or
     orientation B: a >= N+2    (deg M <= s-N-3   for M = m' C1, X1 = C1, X2 = w1, Ehat = E', tau = -u^{-1}).
   In either orientation Ehat = T M g' - 1, Ehat * X2 = g' T^{s-1} + X1, and the cylinder condition is
     g' == alpha * M^{-1} (mod T^N), alpha = (1 - tau... ) : alpha_A = (1-u)/T, alpha_B = (1-u^{-1})/T.
   Case 1 (y = deg g' <= N-1): g' = trunc_N(alpha M^{-1}) is forced by M; X1 = (-g' T^{s-1}) mod Ehat.
   Case 2 (y >= N): deg M + deg v1 <= s-3-N + max(0,2h-4); v1 == -T^{s-2} (mod M), X2 = (T^{s-2}+v1)/M,
           X1 | M with X1 == -X2 (mod T v1).
   Every candidate is verified from scratch (verify()); only verified tuples are reported.
   usage: zt_lop p k N1 N2 u0,u1,...,uh      (u0 must be 1)                                              */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MD 160
typedef struct { int d; int c[MD]; } poly;
static int P, K, H;
static int INV[64];
static poly U, ALPHA[2];
static long long cand1, cand2, hits, verfail, tup2;
static double exp1, exp2, TAUBAR[MD], exp1r, exp2r, NSTAR[MD];

static void norm(poly *a){ while(a->d>=0 && a->c[a->d]==0) a->d--; }
static void zero(poly *a){ a->d=-1; }
static void setmono(poly *a,int k){ a->d=k; memset(a->c,0,sizeof(int)*(k+1)); a->c[k]=1; }
static void add(poly *r,const poly *a,const poly *b){ poly t; int d=a->d>b->d?a->d:b->d; t.d=d;
  for(int i=0;i<=d;i++){ int x=(i<=a->d?a->c[i]:0)+(i<=b->d?b->c[i]:0); t.c[i]=x%P; } norm(&t); *r=t; }
static void sub(poly *r,const poly *a,const poly *b){ poly t; int d=a->d>b->d?a->d:b->d; t.d=d;
  for(int i=0;i<=d;i++){ int x=(i<=a->d?a->c[i]:0)-(i<=b->d?b->c[i]:0); x%=P; if(x<0)x+=P; t.c[i]=x; } norm(&t); *r=t; }
static void mul(poly *r,const poly *a,const poly *b){ poly t; if(a->d<0||b->d<0){ r->d=-1; return; }
  t.d=a->d+b->d; if(t.d>=MD){ fprintf(stderr,"overflow\n"); exit(2);} memset(t.c,0,sizeof(int)*(t.d+1));
  for(int i=0;i<=a->d;i++) if(a->c[i]) for(int j=0;j<=b->d;j++) t.c[i+j]+=a->c[i]*b->c[j];
  for(int i=0;i<=t.d;i++) t.c[i]%=P; norm(&t); *r=t; }
static void mulmodT(poly *r,const poly *a,const poly *b,int n){ /* a*b mod T^n */
  poly t; t.d=n-1; memset(t.c,0,sizeof(int)*n);
  for(int i=0;i<=a->d && i<n;i++) if(a->c[i]) for(int j=0;j<=b->d && i+j<n;j++) t.c[i+j]+=a->c[i]*b->c[j];
  for(int i=0;i<n;i++) t.c[i]%=P; norm(&t); *r=t; }
/* q = a div b, r = a mod b */
static void pdivmod(poly *q,poly *r,const poly *a,const poly *b){ poly rr=*a, qq; int il=INV[b->c[b->d]];
  qq.d = a->d-b->d; if(qq.d<0) qq.d=-1; else memset(qq.c,0,sizeof(int)*(qq.d+1));
  while(rr.d>=b->d){ int f=rr.c[rr.d]*il%P; int s=rr.d-b->d; qq.c[s]=f;
    for(int i=0;i<=b->d;i++){ rr.c[s+i]=(rr.c[s+i]-f*b->c[i])%P; if(rr.c[s+i]<0) rr.c[s+i]+=P; } norm(&rr); }
  norm(&qq); if(q)*q=qq; if(r)*r=rr; }
static void sinv(poly *r,const poly *a,int n){ /* power series inverse mod T^n */
  int a0i=INV[a->c[0]]; r->d=n-1;
  for(int i=0;i<n;i++){ int s=0; for(int j=1;j<=i && j<=a->d;j++) s+=a->c[j]*r->c[i-j]; s%=P;
    int v=((i==0?1:0)-s)%P; if(v<0)v+=P; r->c[i]=v*a0i%P; } norm(r); }
static int tval(const poly *a){ for(int i=0;i<=a->d;i++) if(a->c[i]) return i; return 1<<20; }
static int eq(const poly *a,const poly *b){ if(a->d!=b->d) return 0; for(int i=0;i<=a->d;i++) if(a->c[i]!=b->c[i]) return 0; return 1; }
static void pr(const poly *a){ printf("["); for(int i=0;i<=a->d;i++) printf("%d%s",a->c[i],i<a->d?",":""); printf("]"); }
static int Nof(int s){ return (s+K-2+1)/2; }

/* full verification of a tuple (s, m', g', w1, C1); returns 1 iff it is a genuine tuple covering x_u at level N(s) */
static int verify(int s,const poly *m,const poly *g,const poly *w1,const poly *C1,int report,const char *tag){
  const poly *L[4]={m,g,w1,C1};
  for(int i=0;i<4;i++){ if(L[i]->d<0 || L[i]->c[L[i]->d]!=1 || L[i]->c[0]==0) return 0; }
  poly sm,tg,v1,rem; add(&sm,w1,C1); /* v1 = (w1+C1)/(T g') */
  if(sm.d<0 || sm.c[0]!=0) return 0;
  poly sh; sh.d=sm.d-1; for(int i=0;i<=sh.d;i++) sh.c[i]=sm.c[i+1];
  pdivmod(&v1,&rem,&sh,g); if(rem.d>=0) return 0; (void)tg;
  if(v1.d<0 || v1.c[0]==0) return 0;
  poly lhs,t1,rhs; mul(&t1,m,w1); mul(&lhs,&t1,C1); setmono(&rhs,s-2); add(&rhs,&rhs,&v1);
  if(!eq(&lhs,&rhs)) return 0;
  int N=Nof(s); poly E,Tt; mul(&t1,g,m); mul(&E,&t1,w1); Tt.d=E.d+1; Tt.c[0]=0; for(int i=0;i<=E.d;i++) Tt.c[i+1]=E.c[i];
  poly one; one.d=0; one.c[0]=1; sub(&E,&Tt,&one);
  poly EU; add(&EU,&E,&U); int dep=tval(&EU);
  if(dep < N+1) return 0;
  if(report){ int a=w1->d+1,b=C1->d+1; printf("HIT %s s=%d N=%d a=%d b=%d z=%d y=%d t=%d dep=%d m'=",tag,s,N,a,b,m->d,g->d,v1.d+2,dep);
    pr(m); printf(" g'="); pr(g); printf(" w1="); pr(w1); printf(" C1="); pr(C1); printf(" v1="); pr(&v1); printf("\n"); fflush(stdout); }
  return 1;
}

/* iterate over monic polys of degree d with nonzero constant term: init/next */
static void first_monic(poly *a,int d){ a->d=d; memset(a->c,0,sizeof(int)*(d+1)); a->c[d]=1; if(d>0) a->c[0]=1; }
static int next_monic(poly *a){ int d=a->d; if(d==0) return 0;
  for(int i=0;i<d;i++){ if(i==0){ if(a->c[0]<P-1){ a->c[0]++; return 1;} a->c[0]=1; }
    else { if(a->c[i]<P-1){ a->c[i]++; return 1;} a->c[i]=0; } }
  return 0; }
/* iterate over all polys of degree <= d (including 0): odometer on d+1 digits */
static int next_any(int *dig,int n){ for(int i=0;i<n;i++){ if(dig[i]<P-1){ dig[i]++; return 1;} dig[i]=0; } return 0; }

static void case1(int s,int orient,int Dmax){
  int N=Nof(s);
  for(int dM=0; dM<=Dmax; dM++){
    poly M; first_monic(&M,dM);
    do {
      cand1++;
      poly Mi,g; sinv(&Mi,&M,N); mulmodT(&g,&ALPHA[orient],&Mi,N);
      if(g.d<0 || g.c[g.d]!=1) continue;
      poly t1,Eh,one; one.d=0; one.c[0]=1; mul(&t1,&M,&g);
      poly Tt; Tt.d=t1.d+1; Tt.c[0]=0; for(int i=0;i<=t1.d;i++) Tt.c[i+1]=t1.c[i]; sub(&Eh,&Tt,&one);
      /* X1 = (-g T^{s-1}) mod Eh */
      { double e=1.0; for(int i=0;i<Eh.d;i++) e/=P; exp1 += TAUBAR[dM]*e;
        /* refined model (FF_THIRDS_CORNER Cor 3.2 / §3): only divisors X1 of M of degree >= lo can occur */
        int N_=Nof(s), y=Eh.d-1-dM, t=s-dM-1-y, lo;
        if(orient==0) lo = (t>=N_+3-H) ? 0 : N_+1-dM; else lo = (t>=N_+3) ? 0 : N_+1-H-dM;
        if(lo<0) lo=0; double ad=0; for(int r=lo;r<=dM;r++) ad+=NSTAR[r]*NSTAR[dM-r]/NSTAR[dM]; exp1r += ad*e; }
      poly Ts,X1,r; setmono(&Ts,s-1); pdivmod(NULL,&r,&Ts,&Eh); mul(&t1,&r,&g); pdivmod(NULL,&X1,&t1,&Eh);
      poly zz; zero(&zz); sub(&X1,&zz,&X1);
      if(X1.d<0 || X1.c[X1.d]!=1 || X1.c[0]==0) continue;
      poly mq,rem; pdivmod(&mq,&rem,&M,&X1); if(rem.d>=0) continue;
      /* X2 = (g T^{s-1} + X1)/Eh */
      poly num,X2; setmono(&Ts,s-1); mul(&t1,&g,&Ts); add(&num,&t1,&X1); pdivmod(&X2,&rem,&num,&Eh);
      if(rem.d>=0){ verfail++; continue; }
      int ok = orient==0 ? verify(s,&mq,&g,&X1,&X2,1,"A1") : verify(s,&mq,&g,&X2,&X1,1,"B1");
      if(ok) hits++;
    } while(next_monic(&M));
  }
}

static void case2(int s,int orient,int D2){
  for(int dM=0; dM<=D2; dM++){
    poly M; first_monic(&M,dM);
    do {
      poly Ts,A,zz; zero(&zz); setmono(&Ts,s-2); pdivmod(NULL,&A,&Ts,&M); sub(&A,&zz,&A); /* A = -T^{s-2} mod M */
      int nb = D2 - 2*dM; /* deg B <= D2 - deg M - deg M */
      int dig[MD]; int nd = nb>=0 ? nb+1 : 0; memset(dig,0,sizeof(dig));
      do {
        poly B; B.d=nd-1; for(int i=0;i<nd;i++) B.c[i]=dig[i]; norm(&B);
        poly v1,t1; mul(&t1,&M,&B); add(&v1,&A,&t1);
        if(v1.d<0 || v1.c[0]==0 || v1.d > D2-dM) continue;
        cand2++;
        poly F,X2,rem; setmono(&F,s-2); add(&F,&F,&v1); pdivmod(&X2,&rem,&F,&M); if(rem.d>=0){ verfail++; continue; }
        /* X1 | M, monic, X1 == -X2 mod T v1 */
        poly Tv; Tv.d=v1.d+1; Tv.c[0]=0; for(int i=0;i<=v1.d;i++) Tv.c[i+1]=v1.c[i];
        poly r0; sub(&r0,&zz,&X2); pdivmod(NULL,&r0,&r0,&Tv); /* least residue of -X2 mod Tv */
        int kmax = dM - Tv.d; /* X1 = r0 + Tv*Kp, deg X1 <= dM */
        int dg[MD]; int nk = kmax>=0 ? kmax+1 : 0; memset(dg,0,sizeof(dg));
        do {
          poly Kp,X1; Kp.d=nk-1; for(int i=0;i<nk;i++) Kp.c[i]=dg[i]; norm(&Kp);
          mul(&t1,&Tv,&Kp); add(&X1,&r0,&t1);
          if(X1.d<0 || X1.c[X1.d]!=1 || X1.c[0]==0) continue;
          poly mq; pdivmod(&mq,&rem,&M,&X1); if(rem.d>=0) continue;
          poly sm,g; add(&sm,&X1,&X2); pdivmod(&g,&rem,&sm,&Tv); if(rem.d>=0) continue;
          if(g.d>=0 && g.c[g.d]==1){ tup2++; double e=0.5; for(int i=0;i<Nof(s)-1;i++) e/=P; exp2+=e;
            int N_=Nof(s), a_,b_,z_=mq.d,t_=v1.d+2; if(orient==0){ a_=X1.d+1; b_=X2.d+1; } else { a_=X2.d+1; b_=X1.d+1; }
            int c1 = (z_+2*a_-2>=N_+1) || (H+t_-2>=N_+1), c2 = (H+z_+2*b_-2>=N_+1) || (t_-2>=N_+1);
            if(c1&&c2) exp2r+=e; }
          int ok = orient==0 ? verify(s,&mq,&g,&X1,&X2,1,"A2") : verify(s,&mq,&g,&X2,&X1,1,"B2");
          if(ok) hits++;
        } while(nk>0 && next_any(dg,nk));
      } while(nd>0 && next_any(dig,nd));
    } while(next_monic(&M));
  }
}

int main(int argc,char**argv){
  if(argc<6){ fprintf(stderr,"usage: zt_lop p k N1 N2 u0,u1,...\n"); return 1; }
  P=atoi(argv[1]); K=atoi(argv[2]); int N1=atoi(argv[3]), N2=atoi(argv[4]);
  for(int i=1;i<P;i++) for(int j=1;j<P;j++) if(i*j%P==1) INV[i]=j;
  U.d=-1; { char *s=argv[5]; int i=0; char *tok=strtok(s,","); while(tok){ U.c[i++]=((atoi(tok)%P)+P)%P; tok=strtok(NULL,","); } U.d=i-1; norm(&U); }
  if(U.c[0]!=1 || U.d<1 || U.c[1]==0){ fprintf(stderr,"need u(0)=1, u'(0)!=0\n"); return 1; }
  H=U.d;
  { double Ns[MD]; Ns[0]=1; for(int d=1;d<MD;d++){ double x=1; for(int i=0;i<d;i++) x*=P; Ns[d]=x*(P-1)/P; }
    for(int d=0;d<MD/2;d++){ double t=0; for(int i=0;i<=d;i++) t+=Ns[i]*Ns[d-i]; TAUBAR[d]=t/Ns[d]; }
    for(int d=0;d<MD;d++) NSTAR[d]=Ns[d]; }
  printf("zt_lop p=%d k=%d u=",P,K); pr(&U); printf(" levels %d..%d\n",N1,N2);
  for(int N=N1; N<=N2; N++){
    if(N<3){ printf("N=%d skipped (Lemma 1.2 needs N+1<=s-1)\n",N); continue; }
    /* alpha_A = (1-u)/T mod T^N ; alpha_B = (1-u^{-1})/T mod T^N */
    poly one,t1; one.d=0; one.c[0]=1; sub(&t1,&one,&U); ALPHA[0].d=t1.d-1; for(int i=0;i<=ALPHA[0].d;i++) ALPHA[0].c[i]=t1.c[i+1]; norm(&ALPHA[0]);
    poly ui; sinv(&ui,&U,N+1); sub(&t1,&one,&ui); ALPHA[1].d=t1.d-1; for(int i=0;i<=ALPHA[1].d;i++) ALPHA[1].c[i]=t1.c[i+1]; norm(&ALPHA[1]);
    if(ALPHA[0].d>=N){ poly tmp=ALPHA[0]; tmp.d=N-1; norm(&tmp); ALPHA[0]=tmp; }
    long long h0=hits; double e10=exp1, e20=exp2, e1r0=exp1r, e2r0=exp2r; long long t20=tup2;
    for(int s=2*N-K+1; s<=2*N-K+2; s++){
      if(Nof(s)!=N || s<N+2) { fprintf(stderr,"bad s\n"); return 3; }
      int DA = s-N-3+H, DB = s-N-3, D2A = s-3-N+(2*H-4>0?2*H-4:0), D2B = s-3-N;
      case1(s,0,DA); case1(s,1,DB); if(D2A>=0) case2(s,0,D2A); if(D2B>=0) case2(s,1,D2B);
    }
    printf("N=%d done: hits this level %lld (cumulative cand1 %lld cand2 %lld, division failures %lld) model: case1 %.3e case2 %.3e (case-2 region tuples %lld) refined: case1 %.3e case2 %.3e\n",N,hits-h0,cand1,cand2,verfail,exp1-e10,exp2-e20,tup2-t20,exp1r-e1r0,exp2r-e2r0);
    fflush(stdout);
  }
  return 0;
}
