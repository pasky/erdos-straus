/* review_r232_l1count.c -- R232 round 2 (hostile review of STERILE_LOWER §6), FROM SCRATCH.
   Exact level-1 counts for every prime r in [X0, X1), by parametrisations DIFFERENT from the author's joint sweep:
   P (all N-points of Sigma^II_r, a <= b):  loop (a, b), c | a+b (smallest-prime-factor table), e = (a+b)/c, then the
      arithmetic progression r = 4abd - e in d.  [author: loop (a, c, d) and r == -4a^2 d (mod 4acd - 1)]
   Q (all N-points of Sigma^I_r with a < A, a <= b, e = (a+b)/c integral):  for each a, the divisor pairs {g, m/g} of
      m = 4a^2 d + 1 are found WITHOUT factoring: for every g <= sqrt(m_max) with gcd(g, 2a) = 1, d runs over the progression
      d == -(4a^2)^{-1} (mod g) with g^2 <= m; both orientations (e, f) = (g, m/g), (m/g, g); then r = 4acd - f in c, b = ce - a.
      [author: segmented sieve / Pollard rho factoring of m]
   Bounds used: P: b(4ad - 2) <= N (e <= a + b <= 2b), so b <= X1/(4a - 2);  Q: f = (aF + c)/b <= F + 2, 4acd = F + f <= 2F + 2.
   Every datum is checked against its defining equation in 128-bit arithmetic (abort on failure).
   With R232_QA=1 also the Q-data with a >= A are counted exactly (sieve of 4d a^2 + 1 in a, see below): then Q = all data.
   Output: one line "r P Q Qy" per prime r in [X0, X1); Qy = #Q-data with ad <= Y (env R232_Y, default 0), included in Q.
   Usage: review_r232_l1count X0 X1 A > out */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;
static uint32_t *spf; static uint8_t *isp; static uint32_t *CP, *CQ, *CY; static ll Yc = 0;
static ll X0, X1;
static ll inv_mod(ll a, ll m){ ll t = 0, nt = 1, r = m, nr = a % m; if(nr < 0) nr += m;
  while(nr){ ll q = r / nr, tmp; tmp = t - q*nt; t = nt; nt = tmp; tmp = r - q*nr; r = nr; nr = tmp; }
  if(r != 1) return -1; if(t < 0) t += m; return t; }
static ll pw_mod(ll b, ll e, ll m){ ll r = 1; b %= m; while(e){ if(e & 1) r = (ll)((i128)r*b % m); b = (ll)((i128)b*b % m); e >>= 1; } return r; }
static ll sqrt_mod(ll t, ll p){ /* a root of x^2 == t (mod odd prime p), or -1 */
  t %= p; if(t == 0) return 0; if(pw_mod(t, (p - 1)/2, p) != 1) return -1;
  ll q = p - 1; int s = 0; while(!(q & 1)){ q >>= 1; s++; }
  ll z = 2; while(pw_mod(z, (p - 1)/2, p) != p - 1) z++;
  ll M_ = s, c = pw_mod(z, q, p), tt = pw_mod(t, q, p), R = pw_mod(t, (q + 1)/2, p);
  while(tt != 1){ ll i = 0, x = tt; while(x != 1){ x = (ll)((i128)x*x % p); i++; }
    ll bb = c; for(ll k = 0; k < M_ - i - 1; k++) bb = (ll)((i128)bb*bb % p);
    M_ = i; c = (ll)((i128)bb*bb % p); tt = (ll)((i128)tt*c % p); R = (ll)((i128)R*bb % p); }
  if((ll)((i128)R*R % p) != t) return -2; return R; }
static ll gcdll(ll a, ll b){ while(b){ ll t = a % b; a = b; b = t; } return a; }
int main(int argc, char **argv){
  if(argc < 4){ fprintf(stderr, "usage\n"); return 2; }
  X0 = atoll(argv[1]); X1 = atoll(argv[2]); ll A = atoll(argv[3]);
  ll M = X1 + 2;
  spf = calloc(M + 1, 4); isp = calloc(M + 1, 1); CP = calloc(X1 - X0 + 1, 4); CQ = calloc(X1 - X0 + 1, 4); CY = calloc(X1 - X0 + 1, 4); if(getenv("R232_Y")) Yc = atoll(getenv("R232_Y"));
  if(!spf || !isp || !CP || !CQ){ fprintf(stderr, "alloc\n"); return 3; }
  for(ll i = 2; i <= M; i++) if(!spf[i]){ isp[i] = 1; for(ll k = i; k <= M; k += i) if(!spf[k]) spf[k] = (uint32_t)i; }
  /* ---- P ---- */
  for(ll a = 1; 4*a - 2 <= X1; a++){
    ll bmax = X1 / (4*a - 2);
    for(ll b = a; b <= bmax; b++){
      ll s = a + b;               /* enumerate divisors c of s */
      ll pr[40]; int ex[40], np = 0; ll t = s;
      while(t > 1){ ll p = spf[t]; int k = 0; while(t % p == 0){ t /= p; k++; } pr[np] = p; ex[np] = k; np++; }
      ll divs[20000]; int nd = 1; divs[0] = 1;
      for(int i = 0; i < np; i++){ int cur = nd; ll pw = 1; for(int k = 1; k <= ex[i]; k++){ pw *= pr[i]; for(int u = 0; u < cur; u++) divs[nd++] = divs[u] * pw; } }
      ll q4 = 4*a*b;
      for(int u = 0; u < nd; u++){
        ll c = divs[u], e = s / c;
        ll d = (X0 + e + q4 - 1) / q4; if(d < 1) d = 1;
        for(; q4*d - e < X1; d++){
          ll N = q4*d - e; if(N < X0) continue;
          if(!isp[N]) continue;
          if((i128)4*a*b*c*d != (i128)a + b + (i128)N*c){ fprintf(stderr, "P check failed\n"); return 4; }
          if(++CP[N - X0] == 0){ fprintf(stderr, "overflow\n"); return 5; }
        }
      }
    }
  }
  /* ---- Q, a < A ---- */
  for(ll a = 1; a < A; a++){
    ll dmax = (2*X1 + 2) / (4*a); if(dmax < 1) break;
    ll a24 = 4*a*a;
    ll mmax = a24*dmax + 1;
    ll G = (ll)sqrtl((long double)mmax); while(G*G > mmax) G--; while((G+1)*(G+1) <= mmax) G++;
    for(ll g = 1; g <= G; g += 2){
      if(gcdll(g, a) != 1) continue;
      ll d0;
      if(g == 1) d0 = 1;
      else { ll iv = inv_mod(a24 % g, g); if(iv < 0) continue; d0 = (g - iv) % g; if(d0 == 0) d0 = g; }
      /* need g^2 <= 4a^2 d + 1  <=>  d >= (g^2 - 1)/(4a^2) */
      ll dlo = ((i128)g*g - 1 + a24 - 1) / a24; if(dlo < 1) dlo = 1;
      ll d = d0; if(d < dlo) d += ((dlo - d + g - 1) / g) * g;
      for(; d <= dmax; d += g){
        ll m = a24*d + 1; ll h = m / g;            /* m = g h */
        for(int o = 0; o < 2; o++){
          ll e = o ? h : g, f = o ? g : h;
          if(o && h == g) break;
          ll q = 4*a*d;
          ll c = (X0 + f + q - 1) / q; if(c < 1) c = 1;
          for(; q*c - f < X1; c++){
            ll F = q*c - f; if(F < X0) continue;
            ll b = c*e - a; if(b < a) continue;
            if(!isp[F]) continue;
            if((i128)4*a*b*c*d != (i128)F*(a + b) + c){ fprintf(stderr, "Q check failed\n"); return 4; }
            if(a*d <= Yc) CY[F - X0]++;
            if(++CQ[F - X0] == 0){ fprintf(stderr, "overflow\n"); return 5; }
          }
        }
      }
    }
  }
  /* ---- Q, a >= A: for each d <= (2X1+2)/(4A), factor m(a) = 4d a^2 + 1 for all a in [A, (2X1+2)/(4d)] by sieving the
     quadratic polynomial in a (roots of a^2 == -(4d)^{-1} mod p, Tonelli-Shanks), primes p <= sqrt(m_max); the leftover
     cofactor is 1 or prime.  [different from the author's sieve in d for fixed a] */
  if(getenv("R232_QA")) for(ll d = 1; 4*A*d <= 2*X1 + 2; d++){
    ll amax = (2*X1 + 2) / (4*d); if(amax < A) break;
    ll mmax = 4*d*amax*amax + 1;
    ll PM = (ll)sqrtl((long double)mmax) + 2; if(PM > M) { fprintf(stderr, "prime table too small\n"); return 6; }
    /* collect roots */
    ll np2 = 0; for(ll p = 3; p <= PM; p += 2) if(isp[p]) np2++;
    ll *RP = malloc(sizeof(ll) * 2 * (np2 + 1)), *RN = malloc(sizeof(ll) * 2 * (np2 + 1)); ll nr = 0;
    for(ll p = 3; p <= PM; p += 2){ if(!isp[p] || d % p == 0) continue;
      ll t = (p - inv_mod((4*d) % p, p)) % p;           /* t == -(4d)^{-1} */
      ll s = sqrt_mod(t, p); if(s < 0) continue;
      RP[nr] = p; RN[nr] = s; nr++; if(s != 0 && p - s != s){ RP[nr] = p; RN[nr] = p - s; nr++; } }
    const ll SEG = 1 << 15; static ull res[1 << 15]; static uint32_t fp[1 << 15][24]; static uint8_t nfp[1 << 15];
    for(ll lo = A; lo <= amax; lo += SEG){
      ll hi = lo + SEG; if(hi > amax + 1) hi = amax + 1;
      for(ll a = lo; a < hi; a++){ res[a - lo] = (ull)(4*d*a*a + 1); nfp[a - lo] = 0; }
      for(ll k = 0; k < nr; k++){ ll p = RP[k], s = RN[k];
        ll a = lo + ((s - lo % p) % p + p) % p;
        for(; a < hi; a += p){ ull *rr = &res[a - lo]; if(*rr % p) { fprintf(stderr, "sieve root error\n"); return 7; }
          while(*rr % p == 0) *rr /= p; if(nfp[a - lo] >= 24){ fprintf(stderr, "too many primes\n"); return 8; } fp[a - lo][nfp[a - lo]++] = (uint32_t)p; } }
      for(ll a = lo; a < hi; a++){
        ull m = (ull)(4*d*a*a + 1);
        ll pr[26]; int ex[26], npr = 0; ull t = m;
        for(int i = 0; i < nfp[a - lo]; i++){ ll p = fp[a - lo][i]; int k = 0; while(t % p == 0){ t /= p; k++; } pr[npr] = p; ex[npr++] = k; }
        if(t > 1){ if(t != res[a - lo]) { fprintf(stderr, "residual mismatch\n"); return 9; } pr[npr] = (ll)t; ex[npr++] = 1; }
        static ll dv[1 << 16]; int nd = 1; dv[0] = 1;
        for(int i = 0; i < npr; i++){ int cur = nd; ull pw = 1; for(int k = 1; k <= ex[i]; k++){ pw *= pr[i]; for(int u = 0; u < cur; u++){ if(nd >= (1 << 16)) { fprintf(stderr, "divbuf\n"); return 10; } dv[nd++] = dv[u] * (ll)pw; } } }
        ll q = 4*a*d;
        for(int u = 0; u < nd; u++){ ll f = dv[u]; if(f > X1 + 2) continue; ll e = (ll)(m / (ull)f);
          ll c = (X0 + f + q - 1) / q; if(c < 1) c = 1;
          for(; q*c - f < X1; c++){ ll F = q*c - f; if(F < X0) continue; ll b = c*e - a; if(b < a) continue; if(!isp[F]) continue;
            if((i128)4*a*b*c*d != (i128)F*(a + b) + c){ fprintf(stderr, "Q2 check failed\n"); return 4; }
            if(a*d <= Yc) CY[F - X0]++;
            if(++CQ[F - X0] == 0){ fprintf(stderr, "overflow\n"); return 5; } } }
      }
    }
    free(RP); free(RN);
  }
  for(ll r = X0; r < X1; r++) if(isp[r]) printf("%lld %u %u %u\n", r, CP[r - X0], CQ[r - X0], CY[r - X0]);
  return 0;
}
