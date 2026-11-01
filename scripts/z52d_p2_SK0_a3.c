/* Z0244/Z0245/Z0004 (pass 2, SK0): exact A_3(p) = #{m in [1,3p], gcd(m,p)=1 : m/p = 1/x+1/y+1/z, x,y,z>=1}
 * for all primes p <= PMAX. Method: m/p = 1/x + (mx-p)/(px); 2-term test for A/B via divisors u of B^2:
 * (Ay-B)(Az-B)=B^2 with u=Ay-B>0, u | B^2, u ≡ -B (mod A), B^2/u ≡ -B (mod A).
 * Output per prime: p, A3(p), #m≡0 mod 4, #m<=(log2 p)^3, #m<=sqrt(p), max m found.                  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
typedef __int128 i128;
static ll gcdll(ll a, ll b){ if(a<0)a=-a; if(b<0)b=-b; while(b){ll t=a%b;a=b;b=t;} return a; }
static int isprime_small(ll n){ if(n<2)return 0; for(ll d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }

#define MAXQ 64
/* factor B (given as product of known primes list with exponents) -> we factor by trial division over primes list */
static int primes_all[200000]; static int np=0;

static int factor_by(ll n, ll *pr, int *ex, int *k){ /* trial division with primes_all, n up to ~1e12 ok */
  *k=0;
  for(int i=0;i<np && (ll)primes_all[i]*primes_all[i] <= n; i++){
    ll q=primes_all[i]; if(n%q==0){ int e=0; while(n%q==0){n/=q;e++;} pr[*k]=q; ex[*k]=e; (*k)++; } }
  if(n>1){ pr[*k]=n; ex[*k]=1; (*k)++; }
  return *k;
}
/* two-term check for A/B (reduced, A>0, B>0): exists positive integers y,z with A/B=1/y+1/z ? */
static int two_term(ll A, ll B, ll *pr0, int *ex0, int k0){
  /* B's prime factorization is needed: B = product pr0^ex0 (given). Build divisors of B^2. */
  ll divs[1<<16]; int nd=1; divs[0]=1;
  for(int i=0;i<k0;i++){
    int e=2*ex0[i]; int cur=nd;
    ll pw=1;
    for(int j=1;j<=e;j++){ pw*=pr0[i];
      for(int t=0;t<cur;t++){ if(nd>=(1<<16)) { fprintf(stderr,"divcap\n"); exit(2);} divs[nd++]=divs[t]*pw; } }
  }
  ll Bm = B % A; ll negB = (A - Bm) % A; /* -B mod A */
  for(int i=0;i<nd;i++){
    ll u=divs[i];
    if(u % A != negB) continue;
    ll v = (ll)((i128)B*B / u);  /* v = B^2/u, fits: B<=3p^2 ~ 3e8 for p<=1e4 => B^2 ~ 1e17 */
    if(v % A == negB) return 1;
  }
  return 0;
}
int main(int argc, char**argv){
  ll PMAX = argc>1? atoll(argv[1]) : 3000;
  /* primes up to 3*PMAX for factor tables */
  char *sv = calloc(3*PMAX+100,1);
  for(ll i=2;i<=3*PMAX+50;i++){ if(!sv[i]){ if(i<=2*PMAX*3) primes_all[np++]=i; for(ll j=i*i;j<=3*PMAX+50;j+=i) sv[j]=1; } }
  for(ll p=2;p<=PMAX;p++){
    if(sv[p]) continue;  /* composite */
    ll A3=0, c4=0, cLog=0, cSqrt=0, maxm=0; ll hist[8]={0};
    ll lim_log = 0; { double l2=__builtin_log((double)p)/__builtin_log(2.0); double t=l2*l2*l2; lim_log=(ll)t; }
    ll lim_sq = 0; while((lim_sq+1)*(lim_sq+1) <= p) lim_sq++;
    for(ll m=1; m<=3*p; m++){
      if(m%p==0) continue;
      ll xlo = (p + m - 1)/m;      /* 1/x <= m/p  -> x >= p/m */
      ll xhi = (3*p)/m;             /* 1/x >= m/(3p) -> x <= 3p/m */
      if(xlo<1) xlo=1;
      int found=0;
      for(ll x=xlo; x<=xhi && !found; x++){
        ll A = m*x - p; if(A<=0) continue;
        ll B = p*x;
        ll g = gcdll(A,B); A/=g; B/=g;
        /* factor B using primes of p and x */
        ll pr[64]; int ex[64]; int k=0;
        ll tmp=p; ll pp[64]; int ee[64]; int kp=0;
        ll n1 = p; for(int i=0;i<np && (ll)primes_all[i]*primes_all[i]<=n1;i++){ ll q=primes_all[i]; if(n1%q==0){int e=0; while(n1%q==0){n1/=q;e++;} pp[kp]=q; ee[kp]=e; kp++;} } if(n1>1){pp[kp]=n1; ee[kp]=1; kp++;}
        (void)tmp;
        /* factor x */
        ll nx = x; ll qq[64]; int qe[64]; int kq=0;
        for(int i=0;i<np && (ll)primes_all[i]*primes_all[i]<=nx;i++){ ll q=primes_all[i]; if(nx%q==0){int e=0; while(nx%q==0){nx/=q;e++;} qq[kq]=q; qe[kq]=e; kq++;} } if(nx>1){qq[kq]=nx; qe[kq]=1; kq++;}
        /* merge primes of p and x; exponent of B = e_p + e_x ; then reduce by g (already applied to A,B values) */
        for(int i=0;i<kp;i++){ pr[k]=pp[i]; ex[k]=ee[i]; k++; }
        for(int j=0;j<kq;j++){ int dup=-1; for(int i=0;i<kp;i++) if(pp[i]==qq[j]) dup=i;
          if(dup>=0) ex[dup]+=qe[j]; else { pr[k]=qq[j]; ex[k]=qe[j]; k++; } }
        /* now exponents of p*x; divide out exponents of g (= gcd(A_orig,B_orig)) : recompute by dividing B by primes */
        /* B (reduced) = B_orig/g: remove exponents: for each prime in pr, while B % q ==0 and exponent budget left */
        ll Bred = B; /* reduce exponent vector to match Bred */
        for(int i=0;i<k;i++){ int e=0; ll t=Bred; while(t%pr[i]==0 && e<ex[i]){ t/=pr[i]; e++; } ex[i]=e; }
        /* verify product equals Bred */
        ll chk=1; for(int i=0;i<k;i++){ for(int j=0;j<ex[i];j++) chk*=pr[i]; }
        if(chk!=Bred){ fprintf(stderr,"factor mismatch p=%lld m=%lld x=%lld\n",p,m,x); exit(3);}  
        if(two_term(A,B,pr,ex,k)) found=1;
      }
      if(found){ A3++; hist[m%8]++; if(m%4==0) c4++; if(m<=lim_log) cLog++; if(m<=lim_sq) cSqrt++; if(m>maxm) maxm=m; }
    }
    printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", p, A3, c4, cLog, cSqrt, maxm, lim_log, hist[0],hist[1],hist[2],hist[3]);
    fprintf(stderr,"%lld %lld %lld %lld %lld %lld %lld %lld\n",p,hist[0],hist[1],hist[2],hist[3],hist[4],hist[5],hist[6]);
    fflush(stdout);
  }
  return 0;
}
