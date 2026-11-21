/* Opus cross-review of R17_WALK (NOT the author's code): independent P endpoint searches for the
   J and Hd domains of the z79 four-index cover, written from the identities only.
   usage: z80_xr_ep r L p MODE CUT [SIGMA]
     r prime >=17, U=r^L, B=U/r, N=U*B, (p,q)=(1,5)|(5,1), e0=466*ceil(sqrt U) (z78 (2.3)).
     MODE J : all hits with J=(4pa^2d+qe)/U <= CUT, enumerated by (H,M): M=4ad multiple of 4 with
              qB+1 <= M*H <= qB+CUT, then e == -N (mod M), 1<=e<=e0.
     MODE Hd: all hits with v=H*d <= CUT. Split at SIGMA (default 12, author uses 12):
              part A (H*v^2 <= pB/SIGMA): exact mpz root windows of 4ad(V-pa)=q(N+e), V=UH;
              part B (H > pB/(SIGMA v^2)): for each v, the short a-window
                 a0=qB/(4v) < a <= floor(a0)+3+floor(36pB/(16 r hmin v^2)),  hmin=1+floor(pB/(SIGMA v^2)),
              then d in [(UJ-q e0)/(4pa^2),(UJ-q)/(4pa^2)], d|v, H=v/d>=hmin.
   Every candidate is verified with mpz arithmetic only (units, ordering, 4abd=N+e, e|a+b, U|pa+qb, e<=e0).
   Output: "xr r L p MODE CUT SIGMA cand hits" and one "HIT a b d e H J Hd" line per distinct hit.
*/
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gmp.h>
#include <math.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
static u64 r,p,q,C6=6; static int L; static mpz_t U,B,N,E0,t1,t2,t3;
#ifdef GEN
#define GENOK 1
#else
#define GENOK 0
#endif
static u64 cand,nh; static char seen[1<<14][160]; static int nseen;
static void zs(mpz_t z,u128 v){mpz_import(z,1,-1,sizeof v,0,0,&v);}
static int unit(const mpz_t z){return mpz_divisible_ui_p(z,r)==0;}
/* verify (a,b,d) as a P hit; all mpz */
static void verify(const mpz_t a,const mpz_t b,const mpz_t d){
  cand++;
  mpz_t e,c,s,H,J,v;mpz_inits(e,c,s,H,J,v,NULL);
  if(mpz_sgn(a)<=0||mpz_sgn(d)<=0||mpz_cmp(a,b)>0)goto out;
  mpz_mul(e,a,b);mpz_mul(e,e,d);mpz_mul_ui(e,e,4);mpz_sub(e,e,N);          /* e=4abd-N */
  if(mpz_sgn(e)<=0||mpz_cmp(e,E0)>0)goto out;
  mpz_add(s,a,b);if(!mpz_divisible_p(s,e))goto out;mpz_divexact(c,s,e);
  if(!unit(a)||!unit(b)||!unit(d)||!unit(e)||!unit(c))goto out;
  mpz_mul_ui(s,a,p);mpz_addmul_ui(s,b,q);if(!mpz_divisible_p(s,U))goto out;mpz_divexact(H,s,U);
  mpz_mul(J,a,a);mpz_mul(J,J,d);mpz_mul_ui(J,J,4*p);mpz_addmul_ui(J,e,q);assert(mpz_divisible_p(J,U));mpz_divexact(J,J,U);
  mpz_mul(v,H,d);
  {char buf[64*8];gmp_snprintf(buf,sizeof buf,"HIT %Zd %Zd %Zd %Zd %Zd %Zd %Zd",a,b,d,e,H,J,v);
   for(int i=0;i<nseen;i++)if(!strcmp(seen[i],buf))goto out;
   if(nseen<(1<<14)){assert(strlen(buf)<160);strcpy(seen[nseen],buf);nseen++;}
   puts(buf);nh++;}
out:mpz_clears(e,c,s,H,J,v,NULL);}
static u128 g(const mpz_t z){u128 v=0;size_t n;assert(mpz_sizeinbase(z,2)<=127);mpz_export(&v,&n,-1,sizeof v,0,0,z);return v;}
static u64 isqrt128(u128 x){u64 s=0;for(int b=63;b>=0;b--){u64 t=s|((u64)1<<b);if((u128)t*t<=x)s=t;}return s;}

static void modeJ(u64 J0){
  u128 Uu=g(U),Bu=g(B),Nu=g(N),e0=g(E0);
  /* J>=1 and J*U=4pa^2d+qe <= p M^2/4 + q e0 with M*H<=qB+J0  =>  H^2 (U-q e0) <= p (qB+J0)^2/4 */
  mpz_t K;mpz_init(K);zs(t1,q*Bu+J0);mpz_mul(K,t1,t1);mpz_mul_ui(K,K,p);mpz_fdiv_q_ui(K,K,4);  /* floor(p(qB+J0)^2/4) */
  u64 Hmax;
  if(Uu>q*e0){zs(t2,Uu-q*e0);mpz_fdiv_q(t3,K,t2);mpz_sqrt(t3,t3);Hmax=(u64)g(t3);}
  else{assert(GENOK);Hmax=(u64)((q*Bu+J0)/4);}   /* GEN only: M>=4 */
  mpz_t a,b,d;mpz_inits(a,b,d,NULL);
  for(u64 H=1;H<=Hmax;H++){
    u128 lo=(q*Bu+1+H-1)/H, hi=(q*Bu+J0)/H;           /* M*H in [qB+1,qB+J0] */
    /* also J*U <= p M^2/4 + q e0 must allow J>=1: p*M^2/4 >= U - q e0 (weak, skip) */
    u128 M=(lo+3)/4*4; if(M==0)M=4;
    for(;M<=hi;M+=4){
      u128 J=M*H-q*Bu; assert(J>=1&&J<=J0);
      u128 e=(M-Nu%M)%M; if(e==0)e=M;
      for(;e<=e0;e+=M){
        /* necessary: U*J-q*e = p*M*a with a | M/4 */
        u128 x=Uu*J; if(x<=q*e)continue; x-=q*e; if(x%(p*M))continue; u128 A=x/(p*M);
        if(A==0||(M/4)%A)continue;
        zs(a,A);zs(d,(M/4)/A);zs(b,(Nu+e)/M);if((Nu+e)%M)continue;verify(a,b,d);}
    }}
  mpz_clears(a,b,d,K,NULL);
}
static int doA=1,doB=1; static u64 vlo=1,vhi=0;
static void modeHd(u64 Y,u64 SIG){
  u128 Uu=g(U),Bu=g(B),e0=g(E0),Nu=g(N);
  mpz_t V,disc,lo,hi,a,b,d,tmp,num;mpz_inits(V,disc,lo,hi,a,b,d,tmp,num,NULL);
  /* part A: H*v^2 <= pB/SIG, v=H*d<=Y.  Only the SMALL root of p a^2 - V a + q(N+e)/(4d) = 0 can give a<=b
     (the large root has b=(V-pa)/q < V/(p+q) since V^2 >= (r/pq) * pq(N+e)/d * (1-o(1)) ... checked: b small root
     would need H*v <= 6p/(4r) < 1).  a_-(X) = X/(2p(V+sqrt(V^2-X))), X=pq(N+e)/d increasing in e.
     long double window, padded by 4 + a*2^-50 (>= 2^14 ulps), then exact integer verification. */
  u128 PB=(u128)p*Bu; long double Nl=(long double)g(N), e0l=(long double)e0;
  u64 pairs=0;
  for(u64 H=1;doA;H++){ if((u128)H*H*H>PB/SIG)break;
    u64 vmax=isqrt128(PB/SIG/H); if(vmax>Y)vmax=Y;
    u128 Vu=Uu*H; long double Vl=(long double)Vu;
    for(u64 dd=1;dd<=vmax/H;dd++){ pairs++;
      long double X1=(long double)(p*q)*(Nl+1.0L)/(long double)dd, X2=(long double)(p*q)*(Nl+e0l)/(long double)dd;
      long double D1=Vl*Vl-X1, D2=Vl*Vl-X2; if(D1<0)continue; if(D2<0)D2=0;
      long double a1=X1/(2.0L*p*(Vl+sqrtl(D1))), a2=X2/(2.0L*p*(Vl+sqrtl(D2)));
      long double pad=4.0L+a2*0x1p-50L;
#ifdef GEN
      /* GEN: also the large root a_+ = V/p - a_- (both endpoints), small L only */
      { long double b1=(long double)Vu/p-a2-pad, b2=(long double)Vu/p-a1+pad; if(b1<1)b1=1;
        for(u128 A=(u128)b1;A<=(u128)b2;A++){ if(Vu<=(u128)p*A)break; u128 nb=Vu-p*A; if(nb%q)continue; u128 Bb=nb/q; if(Bb<A)continue;
          u128 lim=(Nu+e0)/4/dd; if(A>lim/Bb)continue; zs(a,A);zs(b,Bb);zs(d,dd);verify(a,b,d);} }
#endif
      long double lo=a1-pad, hi=a2+pad; if(lo<1)lo=1;
      u128 A0=(u128)lo, A1=(u128)hi;
      for(u128 A=A0;A<=A1;A++){
        if(Vu<=(u128)p*A)break; u128 nb=Vu-p*A; if(nb%q)continue; u128 Bb=nb/q; if(Bb<A)continue;
        /* 4*A*Bb*dd in (N, N+e0] ?  compare via division to avoid overflow */
        u128 lim=(Nu+e0)/4/dd; if(A>lim/Bb)continue;
        zs(a,A);zs(b,Bb);zs(d,dd);verify(a,b,d);}
    }}
  fprintf(stderr,"partA pairs %lu\n",pairs);
  /* part B */
  if(!vhi||vhi>Y)vhi=Y;
  for(u64 v=vlo;doB&&v<=vhi;v++){
    u128 hmin=1+PB/((u128)SIG*v*v); if(hmin>v)continue;
    u128 a0f=q*Bu/(4*v); u128 ahi=a0f+3+(36*PB)/((u128)16*r*hmin*v*v);
#ifdef GEN
    { u128 NN=Nu; ahi=a0f+2+(q*e0)/(4*Uu*v)+ (u128)(((long double)(C6*C6)*PB*((long double)(NN+e0)/NN)*((long double)(NN+e0)/NN))/((long double)16*r*hmin*v*v))+2; }
#endif
    for(u128 A=a0f+1;A<=ahi;A++){
      u128 J=4*v*A-q*Bu; /* >0 since A>a0 */ if(4*v*A<=q*Bu)continue;
      u128 UJ=Uu*J; u128 den=4*(u128)p*A*A; if(!GENOK)assert(UJ>q*e0);
      if(UJ<=q)continue;
      u128 dlo=UJ>q*e0?(UJ-q*e0+den-1)/den:1, dhi=(UJ-q)/den; if(dlo<1)dlo=1; if(dhi>v/hmin)dhi=v/hmin;
      for(u128 dd=dlo;dd<=dhi;dd++){if(v%dd)continue;u128 H=v/dd;
        u128 V=Uu*H; if(V<=(u128)p*A||(V-p*A)%q)continue;
        zs(a,A);zs(b,(V-p*A)/q);zs(d,dd);verify(a,b,d);}}
  }
  mpz_clears(V,disc,lo,hi,a,b,d,tmp,num,NULL);
}
int main(int argc,char**argv){
  assert(argc>=6);r=atoll(argv[1]);L=atoi(argv[2]);p=atoll(argv[3]);q=6-p;
#ifdef GEN
  assert(argc>=12); q=atoll(argv[10]); C6=p+q;
#else
  assert(p==1||p==5);
#endif
  u64 CUT=strtoull(argv[5],0,10),SIG=argc>6?atoll(argv[6]):12;
  if(argc>7){doA=strchr(argv[7],'A')!=0;doB=strchr(argv[7],'B')!=0;} if(argc>8)vlo=strtoull(argv[8],0,10); if(argc>9)vhi=strtoull(argv[9],0,10);
  mpz_inits(U,B,N,E0,t1,t2,t3,NULL);mpz_ui_pow_ui(U,r,L);mpz_divexact_ui(B,U,r);mpz_mul(N,U,B);
  mpz_sqrt(E0,U);mpz_mul(t1,E0,E0);if(mpz_cmp(t1,U)<0)mpz_add_ui(E0,E0,1);mpz_mul_ui(E0,E0,466);
#ifdef GEN
  mpz_set_str(E0,argv[11],10);
#else
  mpz_mul_ui(t1,E0,5);assert(mpz_cmp(t1,U)<0);           /* 5 e0 < U, used for J>0 */
#endif
  assert(mpz_sizeinbase(N,2)<=127);
  if(!strcmp(argv[4],"J"))modeJ(CUT);else{assert(!strcmp(argv[4],"Hd"));modeHd(CUT,SIG);}
  printf("xr %lu %d %lu %s %lu %lu %s %lu %lu %lu %lu\n",r,L,p,argv[4],CUT,SIG,argc>7?argv[7]:"AB",vlo,vhi,cand,nh);return 0;}
