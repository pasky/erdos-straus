/* review_zl_pern.c -- R231 round 2, FROM SCRATCH per-n level-1 counter (does NOT use Lemma 3.1 / divisor listing).
   For each n read from stdin (one per line) and parameters A, Y (argv):
     P(n) = #{(a,b,c,d,e) : 4abd = n+e, a+b = ce, a <= b}            loops over (a, b, d)
     Q(n) = #{(a,b,c,d)   : 4abcd = n(a+b)+c, c | a+b, a <= b}         loops over (c, d, f), f == -n (mod 4cd), 1 <= f <= n+2,
            a = (f+n)/(4cd), b = (an+c)/f   (own bounds: a<=b => f <= n + 2/e <= n+2 and 4acd = f+n => cd <= (n+1)/2)
   Q is split into  Qmain (a < A and ad > Y) | Qady (ad <= Y) | Qbig (a >= A and ad > Y); also the max number of Q-data sharing
   one pair (a, d) (the AD bound claims <= 2).
   Output: "n P Qmain Qady Qbig maxmult Qtotal". */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
static int cmp(const void *x, const void *y){ u64 a = *(const u64 *)x, b = *(const u64 *)y; return a < b ? -1 : a > b; }
int main(int argc, char **argv){
  if(argc < 3){ fprintf(stderr, "usage: review_zl_pern A Y < list_of_n\n"); return 2; }
  u64 A = strtoull(argv[1], 0, 10), Y = strtoull(argv[2], 0, 10);
  u64 n; size_t cap = 1 << 20; u64 *pairs = malloc(cap * sizeof(u64));
  while(scanf("%llu", (unsigned long long *)&n) == 1){
    u64 P = 0;
    for(u64 a = 1; 4 * a * a - 2 * a <= n; a++)
      for(u64 b = a; b * (4 * a - 2) <= n; b++){
        u64 m = 4 * a * b, d0 = (n + 1 + m - 1) / m, d1 = (n + a + b) / m;
        for(u64 d = d0; d <= d1; d++){ u64 e = m * d - n; if(e >= 1 && e <= a + b && (a + b) % e == 0) P++; }
      }
    u64 Qm = 0, Qa = 0, Qb = 0, np = 0;
    for(u64 c = 1; 2 * c <= n + 1; c++)
      for(u64 d = 1; 2 * c * d <= n + 1; d++){
        u64 s = 4 * c * d, f = (s - n % s) % s; if(f == 0) f = s;
        for(; f <= n + 2; f += s){
          u64 a = (f + n) / s;
          u128 num = (u128)a * n + c; if(num % f) continue;
          u64 b = (u64)(num / f); if(b < a || (a + b) % c) continue;
          if((u128)4 * a * b * c * d != (u128)n * (a + b) + c){ fprintf(stderr, "identity fail\n"); return 3; }
          if(a * d <= Y) Qa++; else if(a >= A) Qb++; else Qm++;
          if(np >= cap){ cap *= 2; pairs = realloc(pairs, cap * sizeof(u64)); }
          pairs[np++] = (a << 32) | d;
        }
      }
    qsort(pairs, np, sizeof(u64), cmp);
    u64 mm = 0, run = 0; for(u64 i = 0; i < np; i++){ run = (i && pairs[i] == pairs[i - 1]) ? run + 1 : 1; if(run > mm) mm = run; }
    printf("%llu %llu %llu %llu %llu %llu %llu\n", (unsigned long long)n, (unsigned long long)P, (unsigned long long)Qm,
           (unsigned long long)Qa, (unsigned long long)Qb, (unsigned long long)mm, (unsigned long long)np);
    fflush(stdout);
  }
  return 0;
}
