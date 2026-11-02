// z54 HCKILL: search for "quadratic confinement families" p = (y^2 + delta)/(4a), y in an AP, such that for every
// x in C ∩ [4, X] (C = {x : 4|x or x = 7 mod 8}) both window integers p + x and x p + 1 are, identically in y,
// (1/4a)·(norm form of discriminant D f^2) with D a negative fundamental discriminant, |D| | x  (so chi_D is an odd
// character mod x and all good prime factors of the window integer have chi_D = +1  =>  no divisor = -1 mod x).
//   4a(p+x)      = y^2 + (delta + 4 a x)                 -> need fd(-(delta+4ax)) in Allowed(x)
//   4a x (xp+1)  = (xy)^2 + x (x delta + 4a)             -> need fd(-x(x delta+4a)) in Allowed(x)
// Allowed(x) = {D < 0 fundamental : |D| divides x, and D = 1 mod 8 if x = 7 mod 8 (window integer even)}.
// Line 4 forces delta+16a = U^2, delta + a = W^2 (up to common square), i.e. (a,delta) ~ (U^2-W^2, 16W^2-U^2)/15.
// Usage: z54_hckill_qfam UMAX XMAX MINREPORT   -> prints (U,W,a,delta,Xreached,Ds) for families reaching >= MINREPORT
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long long ll; typedef __int128 i128;
static ll gcdl(ll a, ll b){ if(a<0)a=-a; if(b<0)b=-b; while(b){ll t=a%b;a=b;b=t;} return a; }
static int isqr(i128 n){ if(n<0) return 0; ll r=(ll)__builtin_sqrtl((long double)n); for(ll s=r-2;s<=r+2;s++) if(s>=0 && (i128)s*s==n) return 1; return 0; }
// squarefree part of n>0 (n up to ~1e24 ok if cofactor logic holds; we use trial division to cube root bound)
static i128 sqfree(i128 n){ i128 s=1; for(ll q=2; (i128)q*q*q<=n; q++){ int e=0; while(n%q==0){n/=q;e++;} if(e&1) s*=q; }
  // remaining n has all prime factors > cube root of original => n = 1, r, r^2, r*r'
  if(n>1 && !isqr(n)) s*=n; return s; }
static ll fdisc_neg(i128 n){ // fundamental discriminant of -n, n>0; returns as ll (could overflow if huge; we only compare)
  i128 s=sqfree(n); i128 d = -s; if(((d%4)+4)%4==1) return (ll)d; return (ll)(-4*s); }
static int allowed(ll D, ll x){ ll aD = -D; if(x % aD) return 0; if(x%8==7 && (((D%8)+8)%8)!=1) return 0; return 1; }
static int sqrt_mod_exists(ll t, ll m){ // is t a square mod m (brute force over residues; m small-ish)
  t%=m; if(t<0)t+=m; for(ll y=0;y<m;y++) if((y*y)%m==t) return 1; return 0; }
int main(int argc,char**argv){ ll UMAX=atoll(argv[1]); ll XMAX=atoll(argv[2]); int MINREP=atoi(argv[3]);
  ll Cx[512]; int nC=0; for(ll x=7;x<=XMAX;x++) if(x%4==0||x%8==7) Cx[nC++]=x;
  long hist[512]={0}; long tot=0;
  for(ll U=2;U<=UMAX;U++) for(ll W=U/4+1; W<U; W++){ if(gcdl(U,W)!=1) continue;
    ll A0=U*U-W*W, B0=16*W*W-U*U; if(A0<=0||B0<=0) continue;
    // (a,delta) = t^2 (A0,B0)/15, t minimal
    ll g=gcdl(A0,B0); ll t=1; if(g%3) t*=3; if(g%5) t*=5;
    i128 a=(i128)t*t*A0/15, de=(i128)t*t*B0/15;
    // remove common square factors
    for(ll s=2; (i128)s*s<=a; s++){ while(a%((i128)s*s)==0 && de%((i128)s*s)==0){ a/=(i128)s*s; de/=(i128)s*s; } }
    if(a > 2000000) continue; // keep the modular check cheap
    // Delta0 = -delta must be 0,1 mod 4 and -delta a square mod 4a
    ll dm4 = (ll)(((-de)%4+4)%4); if(dm4!=0 && dm4!=1) continue;
    if(!sqrt_mod_exists((ll)((-de)%(4*a)), (ll)(4*a))) continue;
    tot++;
    int k; ll Ds[1024]; int nd=0;
    for(k=0;k<nC;k++){ ll x=Cx[k]; i128 ne=de+4*a*x, nl=(i128)x*(x*de+4*a);
      ll De=fdisc_neg(ne), Dl=fdisc_neg(nl); if(!allowed(De,x)||!allowed(Dl,x)) break; Ds[nd++]=De; Ds[nd++]=Dl; }
    hist[k]++;
    if(k>=MINREP){ printf("U=%lld W=%lld a=%lld delta=%lld reached_lines=%d (X>=%lld) Ds:", U,W,(ll)a,(ll)de,k, k>0?Cx[k-1]:4);
      for(int i=0;i<nd;i++) printf(" %lld",Ds[i]); printf("\n"); fflush(stdout); }
  }
  fprintf(stderr,"total admissible (a,delta) families: %ld\n", tot);
  for(int k=0;k<=nC;k++) if(hist[k]) fprintf(stderr,"lines beyond 4 satisfied = %d (next x = %lld): %ld\n", k, k<nC?Cx[k]:-1, hist[k]);
  return 0; }
