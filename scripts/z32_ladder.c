/* O262 calibration ladder: Type II counts for the numerator-m model, for all primes p <= X.
   Type II (p | y, p | z, p ∤ x):  m/p = 1/(abd) + 1/(acdp) + 1/(bcdp)  <=>  m*abcd = a + b + c*p.
   Parametrisation (as scripts/bs_prob_fII.c with 4 -> m): f = m*a*c*d - 1, p = e*f - m*a^2*d, b = c*e - a >= a,
   gcd(a,c) = 1; weight 2 if b > a, 1 if b == a (ordered (y,z)).  For m = 4 this is exactly f_II of bs_prob_fII.
   Output: uint32 array cnt[0..X] (only prime entries meaningful) written to argv[3].
   Usage: z32_ladder m X out.bin      Build: gcc -O2 -o /tmp/z32/z32_ladder scripts/z32_ladder.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static long g(long x, long y){ while(y){ long t=x%y; x=y; y=t;} return x; }
int main(int argc, char **argv){
  if(argc<4){ fprintf(stderr,"usage: z32_ladder m X out.bin\n"); return 1; }
  long m = atol(argv[1]), X = atol(argv[2]);
  uint32_t *cnt = calloc(X+1, 4); if(!cnt){ fprintf(stderr,"oom\n"); return 1; }
  for(long a=1; m*a*a <= X + 2*a*m; a++)
    for(long d=1; m*a*a*d <= X + 2*a*m*a; d++){
      int any=0;
      for(long c=1; ; c++){
        long f = m*a*c*d - 1;
        long e0 = (2*a + c - 1)/c;          /* b = c e - a >= a */
        long p0 = e0*f - m*a*a*d;
        if(p0 > X){ if(e0==1) break; else continue; }
        any=1;
        if(g(a,c)!=1) continue;
        for(long e=e0, p=p0; p<=X; e++, p+=f){
          if(p < 2) continue;
          long b = c*e - a; cnt[p] += (b==a)?1:2;
        }
      }
      if(!any && d>1) break;
    }
  FILE *o = fopen(argv[3],"wb"); fwrite(cnt,4,X+1,o); fclose(o);
  return 0;
}
