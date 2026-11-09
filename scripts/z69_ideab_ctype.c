// z69 IDEAB sanity check for ideas I1/I2/I20.
// For every n == 1 (mod 4), 5 <= n <= N, decide EXHAUSTIVELY whether n has an identity-type solution:
//   Type II:  exists a,b,c,d>=1 with n*c = 4abcd - a - b   <=> exists x in (n/4,(n+1)/3], e=4x-n, ab | x, e | a+b
//   Type I (class K3): exists a,d,f with f | 4a^2 d + 1 and n == -f (mod 4ad)
//             <=> exists f==-n (4), 1<=f<2n, x'=(n+f)/4 = a*c*d, f | 4a^2 d + 1   (c free; b=(an+c)/f)
// Output: lines "n flagII flagI" for n with flagII==0 or flagI==0 (so zeros of either type are visible).
// usage: ctype N [skipsq]   (skipsq=1: skip perfect squares, which are zeros of both types by reciprocity R5)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static int *dstart, *dlist;
int main(int argc, char **argv) {
    long N = atol(argv[1]); int skipsq = argc > 2 ? atoi(argv[2]) : 0;
    long M = (3 * N) / 4 + 2;            // max x' = (n+f)/4 < 3n/4
    int *cnt = calloc(M + 2, sizeof(int));
    for (long d = 1; d <= M; d++) for (long m = d; m <= M; m += d) cnt[m]++;
    dstart = malloc((M + 2) * sizeof(int));
    long tot = 0; for (long m = 1; m <= M; m++) { dstart[m] = tot; tot += cnt[m]; } dstart[M + 1] = tot;
    dlist = malloc(tot * sizeof(int));
    int *fill = calloc(M + 2, sizeof(int));
    for (long d = 1; d <= M; d++) for (long m = d; m <= M; m += d) dlist[dstart[m] + fill[m]++] = d;
    for (long n = 5; n <= N; n += 4) {
        int f2 = 0, f1 = 0;
        if (skipsq) { long r = (long)floor(sqrt((double)n) + 0.5); if (r * r == n) continue; }
        long xhi = (n + 1) / 3;
        for (long x = n / 4 + 1; x <= xhi && !f2; x++) {
            long e = 4 * x - n;
            for (int i = dstart[x]; i < dstart[x + 1] && !f2; i++) {
                long a = dlist[i], y = x / a;
                for (int j = dstart[y]; j < dstart[y + 1]; j++) {
                    long b = dlist[j];
                    if (b < a) continue;
                    if ((a + b) % e == 0) { f2 = 1; break; }
                }
            }
        }
        for (long f = 4 - (n % 4); f < 2 * n && !f1; f += 4) {   // f == -n mod 4, i.e. f==3 mod 4 for n==1
            long x = (n + f) / 4;
            for (int i = dstart[x]; i < dstart[x + 1] && !f1; i++) {
                long a = dlist[i], y = x / a;
                long a2 = (4 * (a % f) % f) * (a % f) % f;
                for (int j = dstart[y]; j < dstart[y + 1]; j++) {
                    long d = dlist[j];
                    if ((a2 * (d % f) + 1) % f == 0) { f1 = 1; break; }
                }
            }
        }
        if (!f2 || !f1) printf("%ld %d %d\n", n, f2, f1);
    }
    return 0;
}
