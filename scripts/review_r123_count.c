/* R123 from-scratch exact Type I counts f_I(p) (y<=z, primitive) for all primes p <= N,
   and a Type II existence check.  Independent of scripts/spec_typecount.c.

   Type I (ET Prop 2.2/2.3): p = 4acd - f, f | m := 4a^2 d + 1, b = (ap+c)/f >= a, gcd(a,b,c)=1, p∤c.
   a<=b  <=>  c*m >= 2af  (since af <= a(4acd-f)+c  <=>  2af <= c(4a^2 d+1)).
   Factorisation of m: regime 1 (a <= A0): m linear in d, sieve over d;
                       regime 2 (a >  A0): m = 4d a^2 + 1 quadratic in a, sieve over a with sqrt(-1/(4d)) mod q.
   Type II existence: (4acd-1) | (a + c p), b = (a+cp)/(4acd-1), p ∤ abd  (ET (2.15): 4abcd = a+b+cp).
   usage: review_r123_count N outprefix
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef uint64_t u64; typedef __uint128_t u128;

static long N; static uint8_t *comp; static uint32_t *cnt; static uint32_t *primes; static long np;
#define MAXF 16
typedef struct { u64 res; uint8_t k; uint32_t q[MAXF]; uint8_t e[MAXF]; } fac_t;

static u64 pw(u64 b, u64 e, u64 m){ u64 r=1; b%=m; while(e){ if(e&1) r=(u128)r*b%m; b=(u128)b*b%m; e>>=1;} return r; }
static u64 inv(u64 a, u64 m){ return pw(a, m-2, m); } /* m prime */
static u64 gcdu(u64 a, u64 b){ while(b){ u64 t=a%b; a=b; b=t;} return a; }
static long sqrtmod(u64 t, u64 q){ /* q odd prime, returns -1 if non-residue */
  t%=q; if(t==0) return 0;
  if(pw(t,(q-1)/2,q)!=1) return -1;
  if(q%4==3) return (long)pw(t,(q+1)/4,q);
  u64 s=q-1; int e=0; while(!(s&1)){s>>=1;e++;}
  u64 z=2; while(pw(z,(q-1)/2,q)!=q-1) z++;
  u64 x=pw(t,(s+1)/2,q), b=pw(t,s,q), g=pw(z,s,q); int r=e;
  while(b!=1){ int m=0; u64 bb=b; while(bb!=1){ bb=(u128)bb*bb%q; m++; }
    u64 gs=g; for(int i=0;i<r-m-1;i++) gs=(u128)gs*gs%q;
    x=(u128)x*gs%q; g=(u128)gs*gs%q; b=(u128)b*g%q; r=m; }
  return (long)x;
}
static inline void addf(fac_t *F, u64 q){ /* divide out q fully */
  int e=0; while(F->res%q==0){ F->res/=q; e++; }
  if(e){ if(F->k>=MAXF){fprintf(stderr,"MAXF\n"); exit(1);} F->q[F->k]=(uint32_t)q; F->e[F->k]=e; F->k++; }
}
/* process all divisors f of m (fully factored: F primes + residual prime R>1 or 1) */
static u64 A_, D_, M_;
static void use_f(u64 f){
  u64 a=A_, d=D_, m=M_;
  if(f > 2*(u64)N+2) return;
  u64 ad4=4*a*d;
  u64 clo = f/ad4 + 1;                       /* 4acd > f  */
  u64 c2 = (2*a*f + m - 1)/m; if(c2>clo) clo=c2;  /* a<=b */
  u64 chi = ((u64)N + f)/ad4;
  for(u64 c=clo;c<=chi;c++){
    u64 n = ad4*c - f;
    if(n<5 || n>(u64)N || comp[n]) continue;
    if(c%n==0) continue;
    u64 num = a*n + c; if(num%f){ fprintf(stderr,"BUG f|an+c a=%lu d=%lu f=%lu c=%lu\n",a,d,f,c); exit(1);} 
    u64 b = num/f; if(b<a) continue;
    if(gcdu(gcdu(a,b),c)!=1) continue;
    cnt[n]++;
  }
}
static void gen(fac_t *F, int i, u64 f, u64 R){
  if(f > 2*(u64)N+2) return;
  if(i==F->k){ use_f(f); if(R>1 && (u128)f*R <= 2*(u128)N+2) use_f(f*R); return; }
  u64 g=f; for(int e=0;e<=F->e[i];e++){ gen(F,i+1,g,R); if((u128)g*F->q[i] > 2*(u128)N+2) break; g*=F->q[i]; }
}

int main(int argc, char **argv){
  N = atol(argv[1]); const char *pre = argc>2?argv[2]:"/tmp/r123";
  long A0 = (long)sqrt((double)N);
  long QMAX = (long)(1.6*N)+10;              /* sqrt of max m in both regimes is < 1.6 N */
  comp = calloc(QMAX+1,1); comp[0]=comp[1]=1;
  for(long i=2;i*i<=QMAX;i++) if(!comp[i]) for(long j=i*i;j<=QMAX;j+=i) comp[j]=1;
  primes = malloc(sizeof(uint32_t)*(QMAX/5+1000)); np=0;
  for(long i=3;i<=QMAX;i++) if(!comp[i]) primes[np++]=i;
  cnt = calloc(N+1,sizeof(uint32_t));
  const long B = 1<<18; fac_t *Fa = malloc(sizeof(fac_t)*B);
  /* regime 1: a <= A0, d from 1 while 4ad <= (N + 2N+2)  (4acd = n+f <= 3N+2) */
  for(long a=1;a<=A0;a++){
    long Dm = (3*N+2)/(4*a);
    for(long d0=1; d0<=Dm; d0+=B){
      long len = (d0+B-1<=Dm)? B : Dm-d0+1;
      for(long j=0;j<len;j++){ Fa[j].res = 4*(u64)a*a*(d0+j)+1; Fa[j].k=0; }
      u64 mmax = 4*(u64)a*a*(d0+len-1)+1; u64 qlim = (u64)sqrtl((long double)mmax)+1;
      for(long t=0;t<np && primes[t]<=qlim;t++){
        u64 q=primes[t]; if(a%q==0) continue;
        u64 r = (q - inv(4*(u64)a*a%q, q))%q;       /* d = r mod q */
        long j = (long)((r + q - (u64)(d0%q))%q);
        for(;j<len;j+=q) addf(&Fa[j],q);
      }
      for(long j=0;j<len;j++){ A_=a; D_=d0+j; M_=4*(u64)a*a*D_+1; gen(&Fa[j],0,1,Fa[j].res); }
    }
  }
  fprintf(stderr,"regime 1 done\n");
  /* regime 2: a > A0, d with 4 a d <= 3N+2 */
  for(long d=1; 4*d*(A0+1) <= 3*N+2; d++){
    long Am = (3*N+2)/(4*d);
    for(long a0=A0+1; a0<=Am; a0+=B){
      long len = (a0+B-1<=Am)? B : Am-a0+1;
      for(long j=0;j<len;j++){ u64 a=a0+j; Fa[j].res = 4*(u64)d*a*a+1; Fa[j].k=0; }
      u64 amax=a0+len-1; u64 mmax=4*(u64)d*amax*amax+1; u64 qlim=(u64)sqrtl((long double)mmax)+1;
      for(long t=0;t<np && primes[t]<=qlim;t++){
        u64 q=primes[t]; if(d%q==0) continue;
        u64 tt = (q - inv(4*(u64)d%q, q))%q; long s = sqrtmod(tt,q); if(s<0) continue;
        u64 roots[2]={ (u64)s, (q-(u64)s)%q }; int nr = (roots[0]==roots[1])?1:2;
        for(int ri=0;ri<nr;ri++){
          long j = (long)((roots[ri] + q - (u64)(a0%q))%q);
          for(;j<len;j+=q) addf(&Fa[j],q);
        }
      }
      for(long j=0;j<len;j++){ A_=a0+j; D_=d; M_=4*(u64)d*A_*A_+1; gen(&Fa[j],0,1,Fa[j].res); }
    }
  }
  fprintf(stderr,"regime 2 done\n");
  /* Type II existence by marking residue classes for small (a,c,d), then per-prime fallback search */
  uint8_t *t2 = calloc(N+1,1);
  long QQ = 4000;
  for(long a=1;4*a-1<=QQ;a++) for(long c=1;4*a*c-1<=QQ;c++) for(long d=1;4*a*c*d-1<=QQ;d++){
    u64 q=4*a*c*d-1; /* p = -a c^{-1} mod q ; gcd(c,q)=1 */
    /* c^{-1} mod q via ext gcd */
    long long r0=q, r1=c%q, s0=0, s1=1; while(r1){ long long qq=r0/r1, tmp=r0-qq*r1; r0=r1; r1=tmp; tmp=s0-qq*s1; s0=s1; s1=tmp; }
    long long ci = ((s0% (long long)q)+q)%q;
    u64 p0 = (u64)(((u128)(q - a%q) * ci) % q);
    for(u64 p=p0; p<=(u64)N; p+=q){ if(p<5||comp[p]||t2[p]) continue;
      u64 b=(a+c*p)/q; if(b%p==0 || a%p==0 || d%p==0) continue; t2[p]=1; }
  }
  long miss2=0;
  for(long p=5;p<=N;p++) if(!comp[p] && !t2[p]){
    int ok=0; for(long a=1;a<=p && !ok;a++) for(long c=1;4*a*c<=8*p && !ok;c++) for(long d=1;4*a*c*d<=8*p && !ok;d++){
      u64 q=4*a*c*d-1; if((a+(u64)c*p)%q==0){ u64 b=(a+(u64)c*p)/q; if(b%p && a%p && d%p) ok=1; } }
    if(ok) t2[p]=1; else miss2++;
  }
  long miss1=0, nprime=0;
  for(long p=5;p<=N;p++) if(!comp[p]){ nprime++; if(cnt[p]==0) miss1++; }
  printf("N=%ld primes(>=5)=%ld  f_I=0: %ld   no TypeII found: %ld\n", N, nprime, miss1, miss2);
  char fn[512]; snprintf(fn,sizeof fn,"%s_fI.bin",pre); FILE *fo=fopen(fn,"wb"); fwrite(cnt,sizeof(uint32_t),N+1,fo); fclose(fo);
  return 0;
}
