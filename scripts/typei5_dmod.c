/* O92 (POINTWISE_TYPEI5.md §3): d-graded fibre-certificate filter, valid for ALL b, no big integers.
   For level L, c_o = 7^a c' (a odd, c' odd, 7 !| c'), delta odd, c_o*delta <= CD:
     d = c_o (c_o delta^2 + 2^(L-4)).
   eps_f = fundamental norm-one unit of Z[sqrt d] from the continued fraction of sqrt d, computed modulo 2^64
   and modulo 7^22 (exact residues).  nu0 = eps_f^k, k = least of {1,2,4} with 4 | B (generator of
   G = {A + 4B' sqrt d}).  By TYPEI5 Lemma 1.1 / Cor 1.2 a fibre certificate with these (L,a,c',delta) is
   nu0 = A + B sqrt d with A = 2 Q 49^b + 1, B = 8 X 7^b (X odd, 7 !| X), hence necessarily
     A == -1 (mod 32),  B == 8 (mod 16),  v7(A-1) = a + 2 v7(B).
   Survivors are printed (L co delta k period vA vB) for exact verification (typei5_verify.py).
   Usage: typei5_dmod Lmin Lmax CD [selftest]  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef long long ll;
static const u64 M7 = 3909821048582988049ULL; /* 7^22 */
static u64 mm(u64 x,u64 y){return (u64)((u128)x*y%M7);}
static u64 am(u64 x,u64 y){u64 s=x+y; if(s>=M7||s<x) s-=M7; return s;}
typedef struct {u64 A2,B2,A7,B7;} U; /* residues mod 2^64 and mod 7^22 */
static u64 dmod7; static u64 d64;
static U mul(U x,U y){U r; r.A2=x.A2*y.A2+d64*x.B2*y.B2; r.B2=x.A2*y.B2+x.B2*y.A2;
  r.A7=am(mm(x.A7,y.A7),mm(dmod7,mm(x.B7,y.B7))); r.B7=am(mm(x.A7,y.B7),mm(x.B7,y.A7)); return r;}
static int v7(u64 x){ if(x==0) return 22; int e=0; while(x%7==0){x/=7;e++;} return e;}
static ll isqrtll(ll n){ ll r=(ll)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r;}
/* fundamental solution of x^2-dy^2=+-1: returns period, residues in *e */
static long fund(ll d, U*e){
  ll a0=isqrtll(d), m=0, q=1, a=a0; long per=0;
  u64 p0_2=1,p1_2=(u64)a0,q0_2=0,q1_2=1;  /* mod 2^64 */
  u64 p0_7=1,p1_7=(u64)a0%M7,q0_7=0,q1_7=1;
  for(;;){ m=q*a-m; q=(d-m*m)/q; a=(a0+m)/q; per++;
    if(q==1) break;
    u64 t; t=(u64)a*p1_2+p0_2; p0_2=p1_2; p1_2=t; t=(u64)a*q1_2+q0_2; q0_2=q1_2; q1_2=t;
    u64 a7=(u64)a%M7; t=am(mm(a7,p1_7),p0_7); p0_7=p1_7; p1_7=t; t=am(mm(a7,q1_7),q0_7); q0_7=q1_7; q1_7=t; }
  /* convergent index per-1 gives (p,q) with p^2-dq^2 = (-1)^per */
  e->A2=p1_2; e->B2=q1_2; e->A7=p1_7; e->B7=q1_7;
  if(per&1) *e=mul(*e,*e);
  return per;
}
int main(int argc,char**argv){
  int Lmin=atoi(argv[1]),Lmax=atoi(argv[2]); ll CD=atoll(argv[3]);
  if(argc>4){ /* selftest: print eps_f residues for d given as argv[3] */
    ll d=CD; d64=(u64)d; dmod7=(u64)d%M7; U e; long per=fund(d,&e);
    printf("%lld %ld %llu %llu %llu %llu\n",d,per,e.A2,e.B2,e.A7,e.B7); return 0; }
  long nd=0, nsurv=0; double steps=0;
  for(ll co=7; co<=CD; co+=2){ ll c=co; int a=0; while(c%7==0){c/=7;a++;} if(a%2==0) continue;
    for(ll dl=1; dl*co<=CD; dl+=2) for(int L=Lmin; L<=Lmax; L++){
      ll T=1LL<<(L-4); ll d=co*(co*dl*dl+T); d64=(u64)d; dmod7=(u64)d%M7; nd++;
      U e; long per=fund(d,&e); steps+=per;
      U nu=e; int k=1; if(nu.B2%4){ nu=mul(nu,nu); k=2; if(nu.B2%4){ nu=mul(nu,nu); k=4; if(nu.B2%4){fprintf(stderr,"k>4?! d=%lld\n",d);return 1;}}}
      if((nu.A2+1)%32) continue; if(nu.B2%16!=8) continue;
      int vB=v7(nu.B7), vA=v7((nu.A7+M7-1)%M7);
      if(a+2*vB<22 ? vA!=a+2*vB : vA<22) continue;
      /* Legendre-shape filter: (A-1)/(2*7^(a+2b)) = Q_1 must be a divisor of M (exact if 7^(22-a-2b) > M) */
      int sh=a+2*vB; int weak=0;
      if(sh<=18){ u64 md=1; for(int i=0;i<22-sh;i++) md*=7; u64 x=(nu.A7+M7-1)%M7; for(int i=0;i<sh;i++) x/=7;
        x%=md; x=(x%2==0)?x/2:(x+md)/2; /* x = Q_1 mod 7^(22-sh) */
        ll M=co*dl*dl+T; int ok=0;
        for(ll q1=1;q1*q1<=M;q1++) if(M%q1==0){ if((u64)q1%md==x||(u64)(M/q1)%md==x){ok=1;break;} }
        if(!ok) continue;
      } else weak=1;
      printf("%d %lld %lld %d %ld %d %d%s\n",L,co,dl,k,per,vA,vB,weak?" WEAK":""); nsurv++; }
  }
  fprintf(stderr,"L=%d..%d CD=%lld: %ld fields, %.3g CF steps, %ld survivors\n",Lmin,Lmax,CD,nd,steps,nsurv); return 0;}
