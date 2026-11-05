// z58 WITNESS: list ALL (★) solutions of 4uBC − u − B = n (n odd), unordered {u,B} with P = min < Q = max, and C.
// Loops (each unordered solution exactly once; FAMDESIGN z56_famdesign_scan.c scheme):
//   1a P < Q <= C : loop P, Q (4PQ^2 − P − Q <= n), test 4PQ | n + P + Q, C = (n+P+Q)/(4PQ) >= Q
//   1b P <= C < Q : loop P, C (C(4PC−1) < n + P), d = 4PC − 1 | n + P, Q = (n+P)/d > C
//   2  C < P < Q  : loop C, P (P(4PC−1) <= n + P), d | n + P, Q = (n+P)/d > P
// (P = Q is impossible for odd n: gcd(u,B) | n and u = B forces u = B = 1, n = 4C − 2.)  Cost ~ 3 n^{2/3}.
// Input: integers n from stdin.  Output: "n R/2 : P,Q,C P,Q,C ..." (R/2 = number of unordered solutions).
// Build: gcc -O2 -o /tmp/z58sols scripts/z58_witness_sols.c
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
int main(void) {
  ll n;
  while (scanf("%lld", &n) == 1) {
    static ll S[100000][3]; int k = 0;
    for (ll P = 1; 4 * P * (P + 1) * (P + 1) - P - (P + 1) <= n; P++)
      for (ll Q = P + 1; 4 * P * Q * Q - P - Q <= n; Q++) {
        ll s = n + P + Q; if (s % (4 * P * Q)) continue; ll C = s / (4 * P * Q); if (C >= Q && k < 100000) { S[k][0] = P; S[k][1] = Q; S[k][2] = C; k++; } }
    for (ll P = 1; 4 * P * P - 1 <= n + P; P++)
      for (ll C = P; C * (4 * P * C - 1) < n + P; C++) {
        ll d = 4 * P * C - 1; if ((n + P) % d) continue; ll Q = (n + P) / d; if (Q > C && Q > P && k < 100000) { S[k][0] = P; S[k][1] = Q; S[k][2] = C; k++; } }
    for (ll C = 1; ; C++) { ll P = C + 1; if (P * (4 * P * C - 1) > n + P) break;
      for (; P * (4 * P * C - 1) <= n + P; P++) {
        ll d = 4 * P * C - 1; if ((n + P) % d) continue; ll Q = (n + P) / d; if (Q > P && k < 100000) { S[k][0] = P; S[k][1] = Q; S[k][2] = C; k++; } } }
    printf("%lld %d :", n, k); for (int i = 0; i < k; i++) printf(" %lld,%lld,%lld", S[i][0], S[i][1], S[i][2]); printf("\n"); fflush(stdout);
  }
  return 0;
}
