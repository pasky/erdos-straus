/* Z1338: basin-hopping on E(x,y,z) = |4/n - 1/x - 1/y - 1/z| over [1, n^2]^3 (integers), for primes n.
 * Local minimisation = exact block-coordinate descent (each coordinate set to its exact optimum given the other two:
 * floor/ceil of 1/r, r = 4/n - 1/x_j - 1/x_k, or n^2 if r <= 0), iterated to a fixed point ("local minimum").
 * Hop = replace one random coordinate by a log-uniform random value in [1, n^2]; Metropolis on log E (temperature TEMP);
 * E = 0 (ground state, an ES solution) ends the run.  For every accepted local minimum we test whether
 *   S = 1/x+1/y+1/z, or any two-term partial sum 1/x_i+1/x_j, or the single term 1/min(x)  is a convergent or
 *   semiconvergent (intermediate fraction) of 4/n.
 * usage: basin NMIN NMAX NPRIMES HOPS TEMP SEED   (distinct primes n == 1 mod 4, log-spaced sample)
 * output per prime: n hops_to_ground nloc_distinct  frac_S_cf frac_pair_cf frac_single_cf  ground(x,y,z) logE_trace(first 12)
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef __int128 i128; typedef long double ld;
static uint64_t rs = 88172645463325252ULL; static uint64_t xr(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static double ur(void){ return (xr() >> 11) * (1.0/9007199254740992.0); }
static long long N, LIM;
static i128 Dval(long long x,long long y,long long z){ return (i128)4*x*y*z - (i128)N*((i128)x*y+(i128)y*z+(i128)z*x); }
static ld logE(long long x,long long y,long long z){ i128 D = Dval(x,y,z); if (D==0) return -INFINITY; if (D<0) D=-D;
  return logl((ld)D) - logl((ld)N) - logl((ld)x) - logl((ld)y) - logl((ld)z); }
static long long best3(long long x,long long y,long long z0){ /* best z given x,y */
  i128 num = (i128)4*x*y - (i128)N*(x+y), den = (i128)N*x*y;
  if (num <= 0) return LIM;
  long long f = (long long)(den/num); long long c[3] = {f, f+1, z0}; long long bz = z0; ld be = logE(x,y,z0);
  for (int i=0;i<2;i++){ long long z=c[i]; if (z<1) z=1; if (z>LIM) z=LIM; ld e=logE(x,y,z); if (e<be){be=e;bz=z;} }
  return bz; }
static void descend(long long *v){ for (int it=0; it<200; it++){ int ch=0;
  for (int i=0;i<3;i++){ long long a=v[(i+1)%3], b=v[(i+2)%3]; long long nz=best3(a,b,v[i]); if (nz!=v[i]){ v[i]=nz; ch=1; } }
  if (!ch) break; } }
static i128 gcd128(i128 a,i128 b){ if(a<0)a=-a; if(b<0)b=-b; while(b){ i128 t=a%b; a=b; b=t; } return a; }
/* convergents + semiconvergents of 4/N */
static long long *cp, *cq; static long ncf;
static void cf_build(void){ free(cp); free(cq); cp = malloc(8*(N/2+200)); cq = malloc(8*(N/2+200)); ncf=0; long long a=4,b=N; long long p0=0,q0=1,p1=1,q1=0; /* h_{-2}=0,h_{-1}=1 */
  while (b){ long long t=a/b; long long r=a%b;
    for (long long k=1;k<=t;k++){ cp[ncf]=k*p1+p0; cq[ncf]=k*q1+q0; ncf++; } /* semiconvergents incl. convergent k=t */
    long long p2=t*p1+p0, q2=t*q1+q0; p0=p1;q0=q1;p1=p2;q1=q2; a=b; b=r; } }
static int is_cf(i128 num, i128 den){ i128 g=gcd128(num,den); num/=g; den/=g; if (den > N) return 0;
  for (long i=0;i<ncf;i++) if (cp[i]==(long long)num && cq[i]==(long long)den) return 1; return 0; }
static int isprime(long long n){ if(n<2)return 0; for(long long d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
int main(int argc,char**argv){
  long long NMIN=atoll(argv[1]), NMAX=atoll(argv[2]); int NP=atoi(argv[3]); long HOPS=atol(argv[4]); double TEMP=atof(argv[5]); rs^=atoll(argv[6])*0x9E3779B97F4A7C15ULL;
  long tot_loc=0, tot_S=0, tot_pair=0, tot_single=0, solved=0; double sumhops=0;
  long long lastn = 0;
  for (int k=0;k<NP;k++){
    long long n = (long long)(NMIN*pow((double)NMAX/NMIN,(double)k/(NP-1))); if (n <= lastn) n = lastn + 1; n |= 1; while(!(n%4==1 && isprime(n))) n++; lastn = n; /* distinct primes */
    N=n; LIM=n*n; cf_build();
    long long v[3]; for(int i=0;i<3;i++) v[i]=(long long)exp(ur()*log((double)LIM)); if(v[0]<1)v[0]=1;
    descend(v); ld e=logE(v[0],v[1],v[2]);
    long nloc=0, nS=0, npair=0, nsingle=0; long hop; ld trace[12]; int nt=0; long long prev[3]={-1,-1,-1};
    for (hop=0; hop<HOPS && e!=-INFINITY; hop++){
      long long w[3]={v[0],v[1],v[2]}; int i=xr()%3; w[i]=(long long)exp(ur()*log((double)LIM)); if(w[i]<1)w[i]=1;
      descend(w); ld ew=logE(w[0],w[1],w[2]);
      if (ew<=e || ur()<expl((e-ew)/TEMP)){
        v[0]=w[0];v[1]=w[1];v[2]=w[2]; e=ew;
        if (!(v[0]==prev[0]&&v[1]==prev[1]&&v[2]==prev[2])){ nloc++; prev[0]=v[0];prev[1]=v[1];prev[2]=v[2];
          if (nt<12) trace[nt++]=e;
          i128 x=v[0],y=v[1],z=v[2];
          if (is_cf(x*y+y*z+z*x, x*y*z)) nS++;
          int pc=0; if (is_cf(x+y,x*y)||is_cf(y+z,y*z)||is_cf(x+z,x*z)) pc=1; npair+=pc;
          long long mn=v[0]; if(v[1]<mn)mn=v[1]; if(v[2]<mn)mn=v[2]; if (is_cf(1,mn)) nsingle++; } } }
    int ok = (e==-INFINITY); solved+=ok; if(ok) sumhops+=hop;
    tot_loc+=nloc; tot_S+=nS; tot_pair+=npair; tot_single+=nsingle;
    printf("%lld %ld %d %ld %.4f %.4f %.4f %lld %lld %lld |", n, hop, ok, nloc, nloc?(double)nS/nloc:0, nloc?(double)npair/nloc:0, nloc?(double)nsingle/nloc:0, v[0],v[1],v[2]);
    for(int t=0;t<nt;t++) printf(" %.1Lf", trace[t]/logl(10)); printf("\n"); fflush(stdout);
  }
  fprintf(stderr,"primes=%d solved=%ld mean_hops_solved=%.1f local_minima=%ld S_is_cf=%ld pair_is_cf=%ld single_is_cf=%ld\n", NP, solved, solved?sumhops/solved:0, tot_loc, tot_S, tot_pair, tot_single);
}
