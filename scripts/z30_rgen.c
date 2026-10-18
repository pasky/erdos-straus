/* z30_rgen.c (O260): for each n read from stdin, compute over all pairs (u,B) >= 1 with
   gcd(u,B)=1, u+B odd, q = 4uB <= n+u+B:
     R    = #{pairs : q | n+u+B}                       (the (*) count, c = 1 line)
     M0   = sum 1/phi(q)                               (uniform-unit model)
     M2   = sum s2(q)/phi(q) [n*a == 1 mod 2^min(v2(q),3)]   (2-adic conditioning only)
     Mg   = sum s(q)/phi(q)  [n*a is a square unit mod q]   (genus = quadratic-character part)
   where a = -(u+B) mod q, s(q) = size of (Z/q)^x mod squares.
   Exact identity (see SINGLE_P_COUNT.md Lemma 3.1): Mg is the contribution of all characters of
   order <= 2 to the character expansion of R.  Also outputs Mg restricted to pairs with
   uB <= n^theta for theta = 1/3 (small-pair share).
   Sanity: every hit must be genus-matched (checked; aborts otherwise).
   usage: echo "n1 n2 ..." | ./z30_rgen            (n odd, n >= 5)
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

static int *spf; static long NMAX;

static void sieve(long N){ spf = calloc(N+1, sizeof(int)); for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i; }

static int jacobi(int64_t a, int64_t m){ /* m odd > 0 */
  a %= m; if(a<0) a+=m; int t=1;
  while(a){ while(!(a&1)){ a>>=1; int64_t r=m&7; if(r==3||r==5) t=-t; }
    int64_t tmp=a; a=m; m=tmp; if((a&3)==3 && (m&3)==3) t=-t; a%=m; }
  return m==1 ? t : 0;
}

int main(int argc,char**argv){
  long Y = argc>1 ? atol(argv[1]) : 0; /* full local conditioning at primes <= Y (incl. 2-power), genus elsewhere */
  long ns[100000]; int k=0; long mx=0;
  while(k<100000 && scanf("%ld",&ns[k])==1){ if(ns[k]>mx) mx=ns[k]; k++; }
  NMAX = mx+2; sieve(NMAX);
  printf("# Y=%ld\n# n R M0 M2 Mg Mg_small(uB<=n^(1/3)) M0_small npairs Mloc Rsmooth(q Y-smooth)\n",Y);
  for(int i=0;i<k;i++){
    long n=ns[i]; long R=0, np=0; double M0=0,M2=0,Mg=0,Mgs=0,M0s=0,Ml=0; long Rsm=0; double small=cbrt((double)n);
    for(long u=1; 3*u-1 <= n; u++){
      long Bmax = (n+u)/(4*u-1);
      for(long B=1; B<=Bmax; B++){
        if(((u+B)&1)==0) continue;
        /* gcd */
        long x=u,y=B; while(y){ long t=x%y; x=y; y=t; } if(x!=1) continue;
        np++;
        int64_t q = 4*(int64_t)u*B;
        int64_t a = (-(int64_t)(u+B)) % q; if(a<0) a+=q;
        /* phi and genus over odd primes of u and B, 2-part */
        int v2=2; long uu=u, bb=B; while(!(uu&1)){uu>>=1; v2++;} while(!(bb&1)){bb>>=1; v2++;}
        double phi = (double)(1L<<(v2-1)); int s = (v2==2)?2:4; int gen=1;
        int64_t na = ((n % q) * (a % q)) % q; /* q <= ~4e9? keep q small: n<=1e9 => q<=n+u+B fine; product < 2^63 */
        int m2 = (v2==2)?4:8; int ok2 = ((na % m2)==1);
        long parts[2]={uu,bb};
        for(int w=0;w<2;w++){ long z=parts[w]; while(z>1){ long l=spf[z]; phi*= (double)(l-1); z/=l; while(z%l==0){ phi*=l; z/=l; } s*=2; if(gen){ if(jacobi(na % l, l)!=1) gen=0; } } }
        { /* Mloc */
          int64_t qs=1; double phip=1; int sp=1; int okp=1; long z;
          int64_t two=(int64_t)1<<v2;
          if(Y>=2){ qs=two; } else { phip=(double)(two/2); sp=(v2==2)?2:4; if(((na%m2)!=1)) okp=0; }
          for(int w=0;w<2;w++){ z=parts[w]; while(z>1){ long l=spf[z]; int64_t pe=1; while(z%l==0){ pe*=l; z/=l; }
              if(l<=Y) qs*=pe; else { phip*= (double)(pe/l*(l-1)); sp*=2; if(okp && jacobi(na % l, l)!=1) okp=0; } } }
          if(okp && (((int64_t)n - a) % qs == 0)) Ml += sp/phip;
          if(qs==q && ((int64_t)n+u+B)%q==0) Rsm++;
        }
        double w0 = 1.0/phi;
        M0 += w0; if(ok2) M2 += (v2==2?2.0:4.0)/phi;
        int match = gen && ok2;
        if(match) Mg += s/phi;
        if((double)u*B <= small){ M0s += w0; if(match) Mgs += s/phi; }
        if(((int64_t)n+u+B) % q == 0){ R++; if(!match){ fprintf(stderr,"UNMATCHED HIT n=%ld u=%ld B=%ld\n",n,u,B); return 1; } }
      }
    }
    printf("%ld %ld %.4f %.4f %.4f %.4f %.4f %ld %.4f %ld\n", n, R, M0, M2, Mg, Mgs, M0s, np, Ml, Rsm);
    fflush(stdout);
  }
  return 0;
}
