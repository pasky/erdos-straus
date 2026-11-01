// Z0556: T(n) = #{(t,u,v) in N^3: tuv - u - v = n}; also T4(n) = # with at least one coordinate in 4Z ∪ (8Z - n) (mod-8 test on n).
// Output "n T T4 Tall" for n ≤ N with T>0. Usage: z52d_p2_TO2_i3 N out
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv){
  long N = atol(argv[1]);
  long *T = calloc(N+1, sizeof(long)), *T4 = calloc(N+1, sizeof(long)), *TA = calloc(N+1, sizeof(long));
  for (long t=1; t<=N+2; t++){
    long umax = (t==1) ? N+2 : (N+1)/(t-1) + 2;
    for (long u=1; u<=umax; u++){
      long k = t*u - 1; if (k < 1) continue;
      for (long v=1; ; v++){
        long n = v*k - u; if (n > N) break; if (n < 1) continue;
        T[n]++;
        long r = (8 - (n % 8)) % 8;   // residue class -n mod 8
        int c4 = (t%4==0)||(u%4==0)||(v%4==0) || (t%8==r) || (u%8==r) || (v%8==r);
        if (c4) T4[n]++;
        if ((t%4==0)&&(u%4==0)&&(v%4==0)) TA[n]++;
      }
    }
  }
  FILE *f=fopen(argv[2],"w"); for(long n=1;n<=N;n++) if(T[n]) fprintf(f,"%ld %ld %ld %ld\n", n, T[n], T4[n], TA[n]); fclose(f); return 0; }
