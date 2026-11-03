// z55 CROSSF: exhaustive scan of hits(p) = R_F(p)/2 on the Thm U family (standard window) for ALL primes
// p = 1 (mod 4) in [A, B].  hits(p) = #{(u,w): u sqfree, u = 1 (4), U0 < u <= U1; w odd sqfree, gcd(w,up)=1,
// Y < w <= X, w | p+u, (p+u)/(2w) = -1 (mod 4u)}; window U0=floor(p^(1/12)), U1=floor(p^(1/3)/2), Y=floor(p^(1/3)),
// X=floor(p^(2/3)/4) (decreased until 8*U1*X <= p), exactly as scripts/z53_genusx_run.py / z55_crossf_count.py.
// Output: one line per prime "p hits"; final summary line "# N zeros hist..." to stderr.
// Build: gcc -O2 -o /tmp/z55scan scripts/z55_crossf_scan.c -lm ;  Run: /tmp/z55scan A B > out.txt
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull;

static int *primes, nprimes;
static void sieve(int lim) {
  char *c = calloc(lim + 1, 1); primes = malloc(sizeof(int) * (lim / 2 + 10)); nprimes = 0;
  for (int i = 2; i <= lim; i++) { if (!c[i]) { primes[nprimes++] = i; for (ll j = (ll)i * i; j <= lim; j += i) c[j] = 1; } }
  free(c);
}
static int isprime(ll n) { if (n < 2) return 0; for (int i = 0; i < nprimes; i++) { ll q = primes[i]; if (q * q > n) break; if (n % q == 0) return 0; } return 1; }
static int sqfree(ll n) { for (int i = 0; i < nprimes; i++) { ll q = primes[i]; if (q * q > n) break; if (n % q == 0) { n /= q; if (n % q == 0) return 0; } } return 1; }
static ll gcdl(ll a, ll b) { while (b) { ll c = a % b; a = b; b = c; } return a; }

// factor n (odd), enumerate divisors w in (Y,X], odd squarefree, gcd(w,u)=1, with (n/w + 1) = 0 mod 4u
static ll pf[64]; static int pe[64], npf;
static void factor(ll n) { npf = 0; for (int i = 0; i < nprimes; i++) { ll q = primes[i]; if (q * q > n) break; if (n % q == 0) { int e = 0; while (n % q == 0) { n /= q; e++; } pf[npf] = q; pe[npf] = e; npf++; } } if (n > 1) { pf[npf] = n; pe[npf] = 1; npf++; } }
static int count_u(ll n, ll u, ll Y, ll X) { // n = (p+u)/2
  factor(n);
  // enumerate squarefree divisors w (each prime to power 0 or 1), require gcd(w,u)=1 and squarefree => also need prime^1 ok
  int cnt = 0; int k = npf; ll w;
  for (unsigned mask = 0; mask < (1u << k); mask++) {
    w = 1; int ok = 1;
    for (int i = 0; i < k; i++) if (mask >> i & 1) { w *= pf[i]; if (w > X) { ok = 0; break; } }
    if (!ok || w <= Y) continue;
    if (w % 2 == 0) continue;
    if (gcdl(w, u) != 1) continue;
    ll d = n / w; // cofactor w''
    if ((d + 1) % (4 * u) == 0) cnt++;
  }
  return cnt;
}

int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: A B\n"); return 1; }
  ll A = atoll(argv[1]), B = atoll(argv[2]);
  sieve((int)sqrt((double)B + 1e6) + 100);
  long N = 0, zeros = 0; long hist[64] = {0};
  for (ll p = A | 1; p <= B; p += 2) {
    if (p % 4 != 1 || !isprime(p)) continue;
    ll U0; { double t = pow((double)p, 1.0 / 12) - 0.5; U0 = (ll)floor(t + 0.5); } // = python round(p^(1/12) - 0.5)
    ll U1 = (ll)(pow((double)p, 1.0 / 3) / 2), Y = (ll)pow((double)p, 1.0 / 3), X = (ll)(pow((double)p, 2.0 / 3) / 4);
    while (8 * U1 * X > p) X--;
    if (U0 < 1) U0 = 1;
    int h = 0;
    for (ll u = U0 + 1; u <= U1; u++) {
      if (u % 4 != 1 || !sqfree(u) || p % u == 0) continue;
      h += count_u((p + u) / 2, u, Y, X);
    }
    printf("%lld %d\n", p, h); N++; if (h == 0) zeros++; if (h < 64) hist[h]++;
  }
  fprintf(stderr, "# N=%ld zeros=%ld", N, zeros);
  for (int i = 0; i < 20; i++) fprintf(stderr, " h%d=%ld", i, hist[i]);
  fprintf(stderr, "\n");
  return 0;
}
