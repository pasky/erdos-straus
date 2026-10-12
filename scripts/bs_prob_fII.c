/* O142 brainstorm: Type II counts f_II(p) for primes 5<=p<=X, dumped as (uint32 p, uint32 f).
   Enumeration identical in logic to scripts/review_r128b_count.c (R128b, from-scratch counter):
   f_II(p) = #{(a,b,c,d): 4abcd = a+b+pc, gcd(a,c)=1} ordered, via p = e*f - 4a^2 d, f = 4acd-1,
   b = ce - a >= a (weight 2 if b>a, 1 if b==a).
   Also dumps g(p) = number of distinct (a,d) pairs (cluster key: N = p+4a^2 d) carrying >=1 solution.
   Records per prime: p, f_II, g, f_II restricted to e<=16, to e<=256.
   Usage: bs_prob_fII X out.bin     Build: gcc -O2 -o /tmp/bs_prob_fII scripts/bs_prob_fII.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static long g(long x, long y){ while(y){ long t=x%y; x=y; y=t;} return x; }
int main(int argc, char **argv){
  long X = atol(argv[1]);
  uint32_t *cnt = calloc(X+1, 4); uint32_t *blk = calloc(X+1, 4); uint32_t *stamp = calloc(X+1, 4); uint32_t id=0; uint32_t *s16=calloc(X+1,4), *s256=calloc(X+1,4);
  unsigned char *comp = calloc(X+1, 1);
  if(!cnt||!blk||!stamp||!comp){ fprintf(stderr,"oom\n"); return 1; }
  for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
  for(long a=1; 4*a*a <= X+2*a; a++)
    for(long d=1; 4*a*a*d <= X + 2*a; d++){ id++;
      for(long c=1; ; c++){
        long f = 4*a*c*d - 1;
        long e0 = (2*a + c - 1)/c;
        long p0 = e0*f - 4*a*a*d;
        if(p0 > X) { if(e0==1) break; else continue; }
        if(g(a,c)!=1) continue;
        for(long e=e0, p=p0; p<=X; e++, p+=f){
          long b = c*e - a;
          cnt[p] += (b==a)?1:2; if(e<=16) s16[p]+=(b==a)?1:2; if(e<=256) s256[p]+=(b==a)?1:2;
          if(stamp[p]!=id){ stamp[p]=id; blk[p]++; }
        }
      }}
  FILE *o = fopen(argv[2], "wb");
  for(long p=5;p<=X;p++) if(!comp[p]){ uint32_t r[5]={ (uint32_t)p, cnt[p], blk[p], s16[p], s256[p] }; fwrite(r,4,5,o);}
  fclose(o); return 0;
}
