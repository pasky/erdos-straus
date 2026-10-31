// z52b pass1 U09 (Z2047): representability of primes p<=X by four sign patterns
//   p = t*u*v + s1*u + s2*v,  t,u,v >= 1, with constraint 4 | t   (s1,s2 in {+1,-1})
// Output: per pattern: number of primes p≡1 (mod 4) (and all primes) with NO representation, first few failures.
// Build: gcc -O2 -o z52b_p1_U09_cont scripts/z52b_p1_U09_cont.c ; ./z52b_p1_U09_cont 200000
#include <stdio.h>
#include <stdlib.h>
static int is_rep(long p, int s1, int s2){
  // p = t*u*v + s1*u + s2*v with t>=4, 4|t, u,v>=1.  Solve for v: v*(t*u + s2) = p - s1*u.
  for(long u=1; u<=p; u++){
    long rhs = p - s1*u;                  // must be >= 1
    if(rhs < 1) { if(s1>0) break; else continue; }
    for(long t=4; ; t+=4){
      long den = t*u + s2;                // > 0 required
      if(den < 1) continue;
      if(den > rhs) break;                // v >= 1 needs den <= rhs
      if(rhs % den == 0) return 1;
    }
  }
  return 0;
}
int main(int argc, char**argv){
  long X = argc>1? atol(argv[1]) : 200000;
  char *comp = calloc(X+1,1);
  for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
  int pats[4][2]={{-1,-1},{-1,1},{1,-1},{1,1}};
  for(int k=0;k<4;k++){
    long fail14=0, fail_all=0, tot14=0, tot_all=0; long first[8]; int nf=0;
    for(long p=2;p<=X;p++){
      if(comp[p]) continue;
      if(p==2) continue;
      int r = is_rep(p, pats[k][0], pats[k][1]);
      tot_all++; if(!r){ fail_all++; if(nf<8) first[nf++]=p; }
      if(p%4==1){ tot14++; if(!r){ fail14++; if(fail14<=12) printf("%ld ",p);} }
    }
    printf("pattern t*u*v %+d*u %+d*v (4|t): primes p≡1(4): fail %ld / %ld; all odd primes: fail %ld / %ld; first failures:",
           pats[k][0], pats[k][1], fail14, tot14, fail_all, tot_all);
    for(int i=0;i<nf;i++) printf(" %ld", first[i]);
    printf("\n");
    fflush(stdout);
  }
  return 0;
}
