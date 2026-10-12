/* O154 adversarial hard primes: EXACT Type II count f_II(p) at a single prime p (p < 2^62),
   same convention as scripts/bs_prob_fII.c (ordered weight: (a,b,c,d), a<=b, gcd(a,c)=1,
   weight 2 if a<b, 1 if a==b; equation 4abcd = a+b+pc, i.e. p+e = 4abd, a+b = ce).
   Split at slice parameter E:
     Part A (e <= E): N_e = (p+e)/4 runs over CONSECUTIVE integers; factor them with a segmented sieve,
       count pairs a<=b, ab | N, e | a+b, gcd(a,(a+b)/e)=1.
     Part B (e > E): then f = 4acd-1 = (p+4a^2 d)/e <= (2p+e)/e < 2p/E + 1 (uses 4a^2d <= 4abd = p+e);
       loop (a,d,c) with f <= F := 2p/E + 1, test f | p+4a^2 d, e > E, b = ce-a >= a.
   Output (one line): p fII partA partB X_e for e<=31 (e = 3,7,...,31 or 1,5,.. if p=3 mod 4)
                      emin (least e with X_e>0) Wmin (least f over all solutions) first solution (a,b,c,d,e)
   Metadata caveat: with option A (part B skipped), fII/emin/Wmin/X_e cover only the slices e <= E.
   Usage: bs_adv_count p [E [A]]  (default E ~ 2*sqrt(p); third arg A = slices e<=E only, skip part B)
   Build: gcc -O2 -o /tmp/bs_adv_count scripts/bs_adv_count.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef uint64_t u64; typedef __uint128_t u128;
static u64 gcdu(u64 x, u64 y){ while(y){ u64 t=x%y; x=y; y=t;} return x; }

/* sieve primes up to S */
static uint32_t *pr; static long npr;
static void sieve(u64 S){ char *c = calloc(S+1,1); pr = malloc(sizeof(uint32_t)*(S/2+100)); npr=0;
  for(u64 i=2;i<=S;i++){ if(!c[i]){ pr[npr++]=i; for(u64 j=i*i;j<=S;j+=i) c[j]=1; } } free(c); }

#define MAXF 20
static u64 p, E, F;
static u64 partA=0, partB=0, Wmin=0, emin=0; static u64 Xsmall[16];
static int have_sol=0; static u64 sol[5];

static void note(u64 a,u64 b,u64 c,u64 d,u64 e,u64 w){
  u64 f = 4*a*c*d-1; if(!Wmin || f<Wmin) Wmin=f;
  if(!have_sol){ have_sol=1; sol[0]=a;sol[1]=b;sol[2]=c;sol[3]=d;sol[4]=e; }
  (void)w;
}

/* count pairs for N with prime factorisation (q[i]^v[i]) */
static u64 divs[1<<17];
static u64 count_slice(u64 N, u64 e, u64 *q, int *v, int k){
  /* enumerate divisors */
  int nd=1; divs[0]=1;
  for(int i=0;i<k;i++){ int cur=nd; u64 m=1; for(int t=1;t<=v[i];t++){ m*=q[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*m; } }
  u64 tot=0;
  for(int i=0;i<nd;i++){ u64 a=divs[i]; if(a*a>N) continue; u64 M=N/a; u64 am=a%e;
    for(int j=0;j<nd;j++){ u64 b=divs[j]; if(b<a || M%b) continue;
      if((am + b%e)%e) continue; u64 c=(a+b)/e; if(gcdu(a,c)!=1) continue;
      u64 w=(b>a)?2:1; tot+=w; note(a,b,c,N/(a*b),e,w); } }
  return tot;
}

int main(int argc,char**argv){
  p = strtoull(argv[1],0,10);
  E = argc>2 ? strtoull(argv[2],0,10) : (u64)(2*sqrt((double)p));
  F = 2*p/E + 2;
  u64 Nmax = (p+E)/4+1; u64 S = (u64)sqrt((double)Nmax)+2; sieve(S);
  /* Part A: e = e0 + 4j, N = (p+e0)/4 + j */
  u64 e0 = (4 - p%4)%4; if(e0==0) e0=4; /* e = -p mod 4, e>=1 */
  if(p%4==1) e0=3; else if(p%4==3) e0=1;
  u64 N0 = (p+e0)/4; u64 J = (E>=e0)? (E-e0)/4+1 : 0;
  const u64 B = 1<<18; u64 *rem = malloc(B*8); u64 (*fq)[MAXF] = malloc(B*sizeof(*fq)); int (*fv)[MAXF]=malloc(B*sizeof(*fv)); int *fk=malloc(B*sizeof(int));
  for(u64 j0=0;j0<J;j0+=B){ u64 L = (J-j0<B)?J-j0:B;
    for(u64 i=0;i<L;i++){ rem[i]=N0+j0+i; fk[i]=0; }
    for(long t=0;t<npr;t++){ u64 q=pr[t]; u64 start=N0+j0; u64 off=(q - start%q)%q;
      for(u64 i=off;i<L;i+=q){ int vv=0; while(rem[i]%q==0){ rem[i]/=q; vv++; } fq[i][fk[i]]=q; fv[i][fk[i]]=vv; fk[i]++; } }
    for(u64 i=0;i<L;i++){ if(rem[i]>1){ fq[i][fk[i]]=rem[i]; fv[i][fk[i]]=1; fk[i]++; }
      u64 e=e0+4*(j0+i); if(e%p==0) continue;
      u64 x = count_slice(N0+j0+i, e, fq[i], fv[i], fk[i]);
      if(x){ partA+=x; if(!emin) emin=e; if(e<64) Xsmall[e/4]=x; } }
  }
  /* Part B */
  if(!(argc>3 && argv[3][0]=='A'))
  for(u64 a=1; 4*a-1<=F; a++) for(u64 d=1; 4*a*d-1<=F; d++){ u64 R = p + 4*a*a*d;
    for(u64 c=1; 4*a*c*d-1<=F; c++){ u64 f=4*a*c*d-1; if(R%f) continue; u64 e=R/f; if(e<=E) continue;
      if(c*e < 2*a) continue; if(gcdu(a,c)!=1) continue; u64 b=c*e-a; u64 w=(b>a)?2:1; partB+=w; note(a,b,c,d,e,w);
      /* O160 fix: part-B solutions must also feed the emin / Xsmall metadata. Before this fix, emin stayed 0
         when all slices e <= E were empty, and X_e for E < e <= 31 was reported as 0 when E < 31. Neither case
         occurs in the O154 logs (default E ~ 2 sqrt(p) >> 64 there; all 351 records have partA > 0). */
      if(!emin || e<emin) emin=e; if(e<64) Xsmall[e/4]+=w; } }
  printf("%llu %llu %llu %llu |", (unsigned long long)p,(unsigned long long)(partA+partB),(unsigned long long)partA,(unsigned long long)partB);
  for(int i=0;i<8;i++) printf(" %llu",(unsigned long long)Xsmall[i]);
  printf(" | emin %llu Wmin %llu sol %llu %llu %llu %llu %llu\n",(unsigned long long)emin,(unsigned long long)Wmin,
    (unsigned long long)sol[0],(unsigned long long)sol[1],(unsigned long long)sol[2],(unsigned long long)sol[3],(unsigned long long)sol[4]);
  return 0;
}
