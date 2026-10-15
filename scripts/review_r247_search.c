/* R247 from-scratch searcher for Case B tuples covering a polynomial slice point x_u (q = 3).
 * Independent of scripts/zt_lop.c: enumerates the SMALL SIDE as a pair (m', X1) directly (no case split on
 * deg g'), determines v1 by CRT from two necessary congruences
 *    v1 ≡ -T^{s-2}            (mod m'X1)            [m'w1C1 = T^{s-2} + v1]
 *    v1 ≡ -m'w1^2/u  (A)  or  v1 ≡ -u m'C1^2 (B)    (mod T^{n0}),  n0 = min(N+1, s-2)
 * (both are elementary consequences of (B) + covering, re-derived in the review), enumerates ALL v1 in that class
 * with deg v1 <= max(a,b) - 2, reconstructs the other side, g', and verifies (B) + E ≡ -u (mod T^{N+1}) directly.
 * Modes:  full : orientation A only, deg(m'w1) <= s-2  (covers EVERY tuple of parameter s; no Liouville input)
 *         lop  : orientation A with deg(m'w1) <= s-N-3+h  and orientation B with deg(m'C1) <= s-N-3
 *                (relies on Lemma 1.2 only; exact tuples w1 = -uC1 may be missed in lop mode)
 * usage: review_r247_search k u0,u1,..,uh Nmin Nmax full|lop
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MX 96
typedef struct { int d; signed char c[MX]; } P;   /* d = degree, -1 for zero */

static int md(int x){ x%=3; return x<0?x+3:x; }
static void norm(P*a){ while(a->d>=0 && a->c[a->d]==0) a->d--; }
static void zero(P*a){ memset(a,0,sizeof *a); a->d=-1; }
static void mul(P*r,const P*a,const P*b){ int t[2*MX]; P o; zero(&o);
  if(a->d<0||b->d<0){*r=o;return;}
  memset(t,0,sizeof t); for(int i=0;i<=a->d;i++) if(a->c[i]) for(int j=0;j<=b->d;j++) t[i+j]+=a->c[i]*b->c[j];
  o.d=a->d+b->d; if(o.d>=MX){fprintf(stderr,"overflow\n");exit(1);} for(int i=0;i<=o.d;i++) o.c[i]=md(t[i]); norm(&o); *r=o; }
static void mullow(P*r,const P*a,const P*b,int n){ int t[MX]; P o; zero(&o); memset(t,0,sizeof t);
  for(int i=0;i<=a->d&&i<n;i++) if(a->c[i]) for(int j=0;j<=b->d&&i+j<n;j++) t[i+j]+=a->c[i]*b->c[j];
  for(int i=0;i<n;i++) o.c[i]=md(t[i]); o.d=n-1; norm(&o); *r=o; }
static void add(P*r,const P*a,const P*b,int sg){ P o; zero(&o); int D=a->d>b->d?a->d:b->d;
  for(int i=0;i<=D;i++){ int x=(i<=a->d?a->c[i]:0)+sg*(i<=b->d?b->c[i]:0); o.c[i]=md(x);} o.d=D; norm(&o); *r=o; }
static void scal(P*r,const P*a,int k){ P o=*a; for(int i=0;i<=o.d;i++) o.c[i]=md(o.c[i]*k); norm(&o); *r=o; }
static int inv3(int x){ return x==1?1:2; }
/* q,r with a = q*b + r; b nonzero */
static void divmod(P*q,P*r,const P*a,const P*b){ P R=*a,Q; zero(&Q); int il=inv3(b->c[b->d]);
  while(R.d>=b->d){ int sh=R.d-b->d, f=md(R.c[R.d]*il); if(sh+1>Q.d) Q.d=sh; Q.c[sh]=f;
    for(int i=0;i<=b->d;i++) R.c[i+sh]=md(R.c[i+sh]-f*b->c[i]); norm(&R);} norm(&Q); if(q)*q=Q; if(r)*r=R; }
/* power-series inverse mod T^n, a(0) != 0 */
static void psinv(P*r,const P*a,int n){ P o; zero(&o); int i0=inv3(a->c[0]);
  for(int i=0;i<n;i++){ int s=(i==0)?1:0; for(int j=1;j<=i&&j<=a->d;j++) s-=a->c[j]*o.c[i-j]; o.c[i]=md(s*i0);} o.d=n-1; norm(&o); *r=o; }
static void trunc_(P*r,const P*a,int n){ P o=*a; for(int i=n;i<=o.d;i++) o.c[i]=0; if(o.d>=n) o.d=n-1; norm(&o); *r=o; }
static void Tpow(P*r,int e){ zero(r); r->d=e; r->c[e]=1; }
static int eq(const P*a,const P*b){ if(a->d!=b->d) return 0; for(int i=0;i<=a->d;i++) if(a->c[i]!=b->c[i]) return 0; return 1; }
static void prn(char*buf,const P*a){ char*p=buf; if(a->d<0){strcpy(buf,"0");return;} for(int i=0;i<=a->d;i++) p+=sprintf(p,"%d",a->c[i]); }
/* monic, T-free polys of degree z: iterate idx over 2*3^(z-1) (z>=1) or 1 (z=0) */
static long cnt(int z){ if(z==0) return 1; long n=2; for(int i=1;i<z;i++) n*=3; return n; }
static void mk(P*r,int z,long idx){ zero(r); r->d=z; r->c[z]=1; if(z==0) return; r->c[0]=1+(idx%2); idx/=2; for(int i=1;i<z;i++){ r->c[i]=idx%3; idx/=3; } }

static P U; static int K,H;
static char found[4096][256]; static int nfound;
static long ncand;

static void report(int N,int s,const P*m,const P*g,const P*w1,const P*C1,const P*v1,const char*ori){
  char b1[100],b2[100],b3[100],b4[100],b5[100],key[256];
  prn(b1,m);prn(b2,g);prn(b3,w1);prn(b4,C1);prn(b5,v1);
  sprintf(key,"N=%d s=%d m'=%s g'=%s w1=%s C1=%s v1=%s",N,s,b1,b2,b3,b4,b5);
  for(int i=0;i<nfound;i++) if(!strcmp(found[i],key)) return;
  strcpy(found[nfound++],key);
  /* exact? w1 == -u C1 */
  P t; mul(&t,&U,C1); add(&t,&t,w1,1); int ex = (t.d<0);
  printf("HIT %s ori=%s a=%d b=%d z=%d y=%d t=%d%s\n",key,ori,w1->d+1,C1->d+1,m->d,g->d,v1->d+2,ex?" EXACT":"");
}

/* given orientation, small side (m, X1), parameter s, level N: enumerate v1 and verify */
static void trypair(int N,int s,const P*m,const P*X1,int ori,const P*uinv){
  P M,Bc,A,t,Mi,v0,mod,Ts2;
  int d,a1,b1,a,b,n0=(N+1<s-2)?N+1:s-2;
  mul(&M,m,X1); d=M.d;
  /* degrees: ori A: X1=w1 (a-1), other side C1 deg s-2-d ; ori B: X1=C1 */
  int x1=X1->d, x2=s-2-d; if(x2<0) return;
  if(ori==0){a1=x1;b1=x2;} else {a1=x2;b1=x1;}
  a=a1+1;b=b1+1; int vmax=(a>b?a:b)-2; if(vmax<0) return;
  Tpow(&Ts2,s-2);
  divmod(NULL,&Bc,&Ts2,&M); scal(&Bc,&Bc,2); /* -T^{s-2} mod M */
  if(ori==0){ mullow(&A,m,X1,n0); mullow(&A,&A,X1,n0); mullow(&A,&A,uinv,n0); }
  else      { mullow(&A,m,X1,n0); mullow(&A,&A,X1,n0); mullow(&A,&A,&U,n0); }
  scal(&A,&A,2);
  /* CRT: v0 = Bc + M*((A-Bc)*M^{-1} mod T^n0) */
  psinv(&Mi,&M,n0); add(&t,&A,&Bc,-1); mullow(&t,&t,&Mi,n0); mul(&t,&t,&M); add(&v0,&Bc,&t,1);
  int mdeg=n0+d; /* modulus T^n0 * M */
  P TM; Tpow(&TM,n0); mul(&mod,&TM,&M);
  /* all v1 = v0 + K*mod, deg <= vmax */
  if(v0.d>vmax) return;
  int kmax=vmax-mdeg; long nk=1; for(int i=0;i<=kmax;i++) nk*=3; if(kmax<0) nk=1;
  for(long ki=0;ki<nk;ki++){
    P Kp,v1; zero(&Kp); long z=ki; for(int i=0;i<=kmax;i++){ Kp.c[i]=z%3; z/=3; } Kp.d=kmax; norm(&Kp);
    mul(&t,&Kp,&mod); add(&v1,&v0,&t,1); if(v1.d<0) continue; ncand++;
    P X2,r,S,g,Tv,w1,C1,E,chk;
    add(&t,&Ts2,&v1,1); divmod(&X2,&r,&t,&M); if(r.d>=0) continue;
    if(X2.d<0||X2.c[X2.d]!=1||X2.c[0]==0) continue;
    if(ori==0){w1=*X1;C1=X2;} else {w1=X2;C1=*X1;}
    add(&S,&w1,&C1,1); Tpow(&t,1); mul(&Tv,&t,&v1);
    divmod(&g,&r,&S,&Tv); if(r.d>=0) continue;
    if(g.d<0||g.c[g.d]!=1||g.c[0]==0) continue;
    /* full (B) verification */
    mul(&chk,m,&w1); mul(&chk,&chk,&C1); add(&chk,&chk,&Ts2,-1); if(!eq(&chk,&v1)){fprintf(stderr,"BUG1\n");exit(1);}
    if(v1.d>=s-2) continue;
    /* E = T g' m' w1 - 1 */
    mul(&E,&g,m); mul(&E,&E,&w1); Tpow(&t,1); mul(&E,&E,&t); P one; zero(&one); one.d=0; one.c[0]=1; add(&E,&E,&one,-1);
    add(&t,&E,&U,1); trunc_(&t,&t,N+1); if(t.d>=0) continue;
    report(N,s,m,&g,&w1,&C1,&v1,ori?"B":"A");
  }
}

int main(int argc,char**argv){
  if(argc<6){fprintf(stderr,"usage\n");return 1;}
  K=atoi(argv[1]); zero(&U); { char*p=argv[2]; int i=0; while(*p){ U.c[i++]=md(atoi(p)); while(*p&&*p!=',')p++; if(*p)p++; } U.d=i-1; norm(&U); }
  H=U.d; int Nmin=atoi(argv[3]),Nmax=atoi(argv[4]); int full=!strcmp(argv[5],"full");
  if(U.c[0]!=1){fprintf(stderr,"u(0) must be 1\n");return 1;}
  for(int N=Nmin;N<=Nmax;N++){
    int before=nfound; ncand=0;
    for(int s=2*N-K+1;s<=2*N-K+2;s++){
      if(s<4) continue;
      int n0=(N+1<s-2)?N+1:s-2; P uinv; psinv(&uinv,&U,n0);
      int DA= full? s-2 : s-N-3+H; if(DA>s-2) DA=s-2;
      for(int d=0;d<=DA;d++) for(int z=0;z<=d;z++){ long nm=cnt(z),nw=cnt(d-z);
        for(long i=0;i<nm;i++){ P m; mk(&m,z,i); for(long j=0;j<nw;j++){ P w; mk(&w,d-z,j); trypair(N,s,&m,&w,0,&uinv);} } }
      if(!full){ int DB=s-N-3; for(int d=0;d<=DB;d++) for(int z=0;z<=d;z++){ long nm=cnt(z),nw=cnt(d-z);
        for(long i=0;i<nm;i++){ P m; mk(&m,z,i); for(long j=0;j<nw;j++){ P w; mk(&w,d-z,j); trypair(N,s,&m,&w,1,&uinv);} } } }
    }
    printf("LEVEL N=%d hits=%d cand=%ld\n",N,nfound-before,ncand); fflush(stdout);
  }
  return 0;
}
