/* exf_engine.c — O131: dump ALL Type I / Type II tuples (n,a,b,c,d), n<=N, a<=b, NO gcd filters.
 * Derived from spec_typecount.c (O123). Output records: struct {u32 n,a,c,d; u64 b;} to prefix.T1.bin / .T2.bin
 * argv[3] = -1: partner families T1-: 4abcd + c = n(a+b) (via f | c(4a^2 d - 1), b=(na-c)/f), T2-: n = 4abd + e, e|a+b.
 * Original header follows.
 * spec_typecount.c — O123 step (1): exact Type I / Type II solution counts for all n <= N.
 *
 * Type I  (ET Prop 2.2, coordinates (a,c,d,f)):  n = 4acd - f,  f | 4a^2 d + 1,
 *          b = (n a + c)/f,  normalised by  a <= b  (i.e. y <= z)  and  gcd(a,b,c) = 1.
 *          Each Type I solution (x,y,z) of 4/n with y <= z is counted exactly once.
 * Type II (ET Prop 2.6, coordinates (a,b,d,e)):  n = 4abd - e,  e | a + b,  c = (a+b)/e,
 *          a <= b, gcd(a,b,c) = 1, gcd(abd, n) = 1.
 *
 * Factorisation of m = 4a^2 d + 1 by sieving:
 *   (A) a <= A0: m linear in d, sieve primes q with d == -(4a^2)^{-1} (mod q);
 *   (B) a >  A0: d <= D0 small, m = 4d a^2 + 1 quadratic in a, roots a^2 == -(4d)^{-1} (mod q).
 * Output: binary arrays FI[n], FI1[n] (a = 1 part), FII[n] as uint32 to files.
 * usage: spec_typecount N outprefix
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef uint64_t u64; typedef __uint128_t u128; typedef int64_t i64;
static u64 N, FMAX;
static uint32_t *FI, *FI1, *FII;
static uint32_t *primes; static u64 nprimes;

static u64 gcd(u64 a, u64 b){ while(b){ u64 t=a%b; a=b; b=t;} return a; }
static u64 mulmod(u64 a, u64 b, u64 m){ return (u64)((u128)a*b % m); }
static u64 powmod(u64 a, u64 e, u64 m){ u64 r=1%m; a%=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static u64 invmod(u64 a, u64 m){ /* m prime, a != 0 mod m */ return powmod(a, m-2, m); }
static i64 sqrtmod(u64 n, u64 p){ /* Tonelli-Shanks, p odd prime; -1 if non-residue */
  n%=p; if(n==0) return 0;
  if(powmod(n,(p-1)/2,p)!=1) return -1;
  if(p%4==3) return (i64)powmod(n,(p+1)/4,p);
  u64 q=p-1, s=0; while(!(q&1)){q>>=1;s++;}
  u64 z=2; while(powmod(z,(p-1)/2,p)!=p-1) z++;
  u64 M=s, c=powmod(z,q,p), t=powmod(n,q,p), R=powmod(n,(q+1)/2,p);
  while(t!=1){ u64 i=0, tt=t; while(tt!=1){ tt=mulmod(tt,tt,p); i++; }
    u64 b=c; for(u64 j=0;j<M-i-1;j++) b=mulmod(b,b,p);
    M=i; c=mulmod(b,b,p); t=mulmod(t,c,p); R=mulmod(R,b,p); }
  return (i64)R;
}

#define MAXF 16
typedef struct { u64 rem; u64 pr[MAXF]; uint8_t ex[MAXF]; uint8_t nf; } Fac;

static u64 g_a, g_d; static i64 S=1; /* sign: +1 = ES Type I/II; -1 = signed partner families */
typedef struct __attribute__((packed)) { uint32_t n,a,c,d; u64 b; } Rec;
static FILE *O1,*O2;
static void count_I(u64 f){
  u64 a=g_a, d=g_d, q4=4*a*d;
  u64 clo=(f+1+q4-1)/q4, chi=(N+f)/q4;
  for(u64 c=clo;c<=chi;c++){
    u64 n=q4*c-f;               /* 1 <= n <= N */
    if(S<0 && (u128)c >= (u128)n*a) continue;
    u128 num = S>0 ? (u128)n*a+c : (u128)n*a-c;
    if((u128)a*f > num) continue;   /* b >= a */
    if(num % f){ fprintf(stderr,"BUG b non-integral a=%llu d=%llu f=%llu c=%llu\n",(unsigned long long)a,(unsigned long long)d,(unsigned long long)f,(unsigned long long)c); exit(1);}
    u64 b=(u64)(num/f);
    Rec r={(uint32_t)n,(uint32_t)a,(uint32_t)c,(uint32_t)d,b}; fwrite(&r,sizeof r,1,O1); FI[n]++;
  }
}
static void divrec(const Fac *F, int k, u64 cur){
  if(k==F->nf){ count_I(cur); return; }
  u64 v=cur;
  for(int e=0;e<=F->ex[k];e++){
    divrec(F,k+1,v);
    if(e<F->ex[k]){ if((u128)v*F->pr[k] > FMAX) break; v*=F->pr[k]; }
  }
}
static void addfac(Fac *F, u64 q){ /* divide out q fully, record */
  uint8_t e=0; while(F->rem%q==0){ F->rem/=q; e++; }
  if(e){ if(F->nf>=MAXF){fprintf(stderr,"MAXF\n");exit(1);} F->pr[F->nf]=q; F->ex[F->nf]=e; F->nf++; }
}
static void finish(Fac *F){ if(F->rem>1){ F->pr[F->nf]=F->rem; F->ex[F->nf]=1; F->nf++; F->rem=1; } }

#define BLK (1u<<18)
static Fac *buf;

int main(int argc, char **argv){
  if(argc<3){ fprintf(stderr,"usage\n"); return 1; }
  N=strtoull(argv[1],0,10); if(argc>3) S=atoi(argv[3]); FMAX=(5*N)/3+2;
  { char fn[512]; sprintf(fn,"%s.T1.bin",argv[2]); O1=fopen(fn,"wb"); sprintf(fn,"%s.T2.bin",argv[2]); O2=fopen(fn,"wb"); }
  FI=calloc(N+1,4); FI1=calloc(N+1,4); FII=calloc(N+1,4);
  buf=malloc(sizeof(Fac)*BLK);
  u64 PL=N+10; /* primes up to N suffice: sqrt(4 d A_d^2+1) <= N/sqrt(d)+1 */
  char *comp=calloc(PL+1,1); nprimes=0;
  for(u64 i=2;i<=PL;i++) if(!comp[i]){ nprimes++; if(i*i<=PL) for(u64 j=i*i;j<=PL;j+=i) comp[j]=1; }
  primes=malloc(4*nprimes); nprimes=0;
  for(u64 i=2;i<=PL;i++) if(!comp[i]) primes[nprimes++]=(uint32_t)i;
  free(comp);
  u64 A0=(u64)sqrt((double)N); if(A0<1) A0=1;
  u64 *start=malloc(8*nprimes), *r2=malloc(8*nprimes);
  /* (A) a <= A0, d in [1, Da] */
  for(u64 a=1;a<=A0;a++){
    u64 Da=(2*N+1)/(4*a); if(!Da) continue;
    u64 mmax=4*a*a*Da+1; u64 qmax=(u64)sqrt((double)mmax)+1;
    u64 np=0; while(np<nprimes && primes[np]<=qmax) np++;
    for(u64 i=1;i<np;i++){ u64 q=primes[i]; if(a%q==0){ start[i]=~0ULL; continue; }
      u64 t=(4*(a%q)%q)*(a%q)%q; start[i]= S>0 ? (q-invmod(t,q))%q : invmod(t,q); } /* d == -(4a^2)^{-1} mod q */
    for(u64 d0=1; d0<=Da; d0+=BLK){
      u64 d1=d0+BLK; if(d1>Da+1) d1=Da+1;
      for(u64 d=d0;d<d1;d++){ Fac *F=&buf[d-d0]; F->rem=4*a*a*d+S; F->nf=0; }
      for(u64 i=1;i<np;i++){ if(start[i]==~0ULL) continue; u64 q=primes[i];
        u64 r=start[i]; u64 d=d0+((r+q-(d0%q))%q);
        for(;d<d1;d+=q) addfac(&buf[d-d0],q); }
      for(u64 d=d0;d<d1;d++){ Fac *F=&buf[d-d0]; finish(F); g_a=a; g_d=d; divrec(F,0,1); }
    }
  }
  /* (B) a > A0: d <= D0 */
  u64 D0=(2*N+1)/(4*(A0+1));
  for(u64 d=1; d<=D0; d++){
    u64 Ad=(2*N+1)/(4*d); if(Ad<=A0) continue;
    u64 mmax=4*d*Ad*Ad+1; u64 qmax=(u64)sqrt((double)mmax)+1;
    u64 np=0; while(np<nprimes && primes[np]<=qmax) np++;
    if(qmax>PL){ fprintf(stderr,"prime table too short\n"); return 1; }
    for(u64 i=1;i<np;i++){ u64 q=primes[i]; if(d%q==0){ start[i]=~0ULL; continue; }
      u64 t= S>0 ? (q-invmod(4*(d%q)%q,q))%q : invmod(4*(d%q)%q,q); i64 s=sqrtmod(t,q);
      if(s<0){ start[i]=~0ULL; continue; } start[i]=(u64)s; r2[i]=(q-(u64)s)%q; }
    for(u64 a0=A0+1; a0<=Ad; a0+=BLK){
      u64 a1=a0+BLK; if(a1>Ad+1) a1=Ad+1;
      for(u64 a=a0;a<a1;a++){ Fac *F=&buf[a-a0]; F->rem=4*d*a*a+S; F->nf=0; }
      for(u64 i=1;i<np;i++){ if(start[i]==~0ULL) continue; u64 q=primes[i];
        for(int k=0;k<2;k++){ u64 r=k?r2[i]:start[i]; if(k && r==start[i]) break;
          u64 a=a0+((r+q-(a0%q))%q);
          for(;a<a1;a+=q) if(buf[a-a0].rem%q==0) addfac(&buf[a-a0],q); } }
      for(u64 a=a0;a<a1;a++){ Fac *F=&buf[a-a0]; finish(F); g_a=a; g_d=d; divrec(F,0,1); }
    }
  }
  fprintf(stderr,"Type I done\n");
  /* Type II: n = 4abd - e, e | a+b, a<=b. Need n>=1 and e<=a+b. smallest-prime-factor table up to 2*(N+1) */
  u64 SM=2*N+4; uint32_t *spf=calloc(SM+1,4);
  for(u64 i=2;i<=SM;i++) if(!spf[i]) for(u64 j=i;j<=SM;j+=i) if(!spf[j]) spf[j]=(uint32_t)i;
  for(u64 a=1; 4*a*a <= N+2*a; a++)
    for(u64 d=1; 4*a*a*d <= N+2*a; d++)
      for(u64 b=a; 4*a*b*d <= N+a+b; b++){
        u64 s=a+b, P=4*a*b*d;
        /* divisors e of s with 1 <= P - e <= N */
        u64 pr[20]; int ex[20]; int k=0; u64 t=s;
        while(t>1){ u64 q=spf[t]; int e=0; while(t%q==0){t/=q;e++;} pr[k]=q; ex[k]=e; k++; }
        u64 divs[4096]; int nd=1; divs[0]=1;
        for(int i=0;i<k;i++){ int cur=nd; u64 v=1; for(int e=1;e<=ex[i];e++){ v*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*v; } }
        for(int j=0;j<nd;j++){ u64 e=divs[j]; if(S>0 && e>=P) continue; u64 n= S>0 ? P-e : P+e; if(n>N) continue;
          u64 c=s/e; Rec r={(uint32_t)n,(uint32_t)a,(uint32_t)c,(uint32_t)d,b}; fwrite(&r,sizeof r,1,O2);
          FII[n]++; }
      }
  fclose(O1); fclose(O2);
  fprintf(stderr,"done\n");
  return 0;
}
