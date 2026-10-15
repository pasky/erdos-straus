// R227 from-scratch census (independent of scripts/s5_*.c).
// Enumeration: for each u >= 1, divisors A of n+u with A = -1 (mod u), A >= 1; t = (A+1)/u, v = (n+u)/A.
// Keep v >= u (ordered words counted with multiplicity 2 when u != v).  Word check: t*u*v - u - v == n asserted.
// psi(r) = Jacobi (r/n).  chi(w) = Jacobi(A/n) (n = 1 mod 4).
// Side cleanliness via factorisations: N_t = A*B, N_u = A*v, N_v = B*u; clean(x) = no prime r | x with psi(r) = -1.
// Output per n: n N Nminus U Nt_clean Nany_clean violations isprime N1 Nm1
// (N1/Nm1: unforced words with some square-defect side = every psi-odd prime to an even power, >= 1 such prime)
// usage: review_r227_census LO HI mode   (mode 0: primes = 1 mod 4 only; 1: all odd n = 1 mod 4 (non-square and square))
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int *spf;
static int jac(ll a, ll n) { // Jacobi (a/n), n odd positive
    a %= n; if (a < 0) a += n; int s = 1;
    while (a) { while (!(a & 1)) { a >>= 1; ll r = n & 7; if (r == 3 || r == 5) s = -s; }
        ll t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) s = -s; a %= n; }
    return n == 1 ? s : 0; }
// collect psi-odd primes of x with exponents into (pr,ex,*k)
static void odd(ll x, ll n, ll *pr, int *ex, int *k) { while (x > 1) { ll r = spf[x]; int e = 0; while (x % r == 0) { x /= r; e++; }
    if (jac(r, n) == -1) { int j; for (j = 0; j < *k; j++) if (pr[j] == r) { ex[j] += e; break; } if (j == *k) { pr[*k] = r; ex[*k] = e; (*k)++; } } } }
static int sqdef(ll x, ll y, ll n) { ll pr[64]; int ex[64], k = 0; odd(x, n, pr, ex, &k); odd(y, n, pr, ex, &k);
    if (!k) return 0; for (int j = 0; j < k; j++) if (ex[j] & 1) return 0; return 1; }
static int cl(ll x, ll n) { while (x > 1) { ll r = spf[x]; if (jac(r, n) == -1) return 0; while (x % r == 0) x /= r; } return 1; }
int main(int argc, char **argv) {
    ll LO = atoll(argv[1]), HI = atoll(argv[2]); int mode = atoi(argv[3]);
    ll M = 2 * HI + 10;
    spf = calloc(M + 1, sizeof(int));
    for (ll i = 2; i <= M; i++) if (!spf[i]) for (ll j = i; j <= M; j += i) if (!spf[j]) spf[j] = (int)i;
    static ll divs[1 << 16];
    for (ll n = LO; n < HI; n++) {
        if (n % 4 != 1 || n < 5) continue;
        int isp = (spf[n] == n);
        if (mode == 0 && !isp) continue;
        ll N = 0, Nm = 0, U = 0, Ntc = 0, Na = 0, viol = 0, N1 = 0, Nm1 = 0;
        for (ll u = 1; u * u <= n + 2 * u + 2; u++) {
            ll x = n + u; int nd = 1; divs[0] = 1;
            while (x > 1) { ll r = spf[x]; int e = 0; while (x % r == 0) { x /= r; e++; }
                int c = nd; ll pk = 1; for (int k = 0; k < e; k++) { pk *= r; for (int i = 0; i < c; i++) divs[nd++] = divs[i] * pk; } }
            for (int i = 0; i < nd; i++) {
                ll A = divs[i]; if ((A + 1) % u) continue; ll t = (A + 1) / u; ll v = (n + u) / A;
                if (v < u) continue;
                ll B = t * v - 1;
                if (B <= 0 || (__int128)t * u * v - u - v != n) { fprintf(stderr, "BAD n=%lld %lld %lld %lld\n", n, t, u, v); exit(1); }
                int mult = (u == v) ? 1 : 2;
                int chi = jac(A, n);
                if (jac(B, n) != chi) { fprintf(stderr, "psiA!=psiB n=%lld\n", n); }
                int cA = cl(A, n), cB = cl(B, n), cu = cl(u, n), cv = cl(v, n);
                int ct = cA && cB, cuu = cA && cv, cvv = cB && cu;
                N += mult; if (chi == -1) Nm += mult;
                if (ct) Ntc += mult;
                if (ct || cuu || cvv) { Na += mult; if (chi == -1) viol += mult; } else { U += mult; if (sqdef(A, B, n) || sqdef(A, v, n) || sqdef(B, u, n)) { N1 += mult; if (chi == -1) Nm1 += mult; } }
            }
        }
        printf("%lld %lld %lld %lld %lld %lld %lld %d %lld %lld\n", n, N, Nm, U, Ntc, Na, viol, isp, N1, Nm1);
    }
    return 0; }
