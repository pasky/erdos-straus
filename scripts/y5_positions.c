/* y5_positions: for primes p = 1 (mod 8) <= X, enumerate ALL certificate words (c,m,s) at N = p (formal, letters >= 1;
 * and interior, letters >= 2) and classify by the position of the opposite vertex o (mirror classes):
 *   H = {Ph, Ph'} (o = h or h'),  C = {Pc, Ps} (o = c or s),  M = {Pm} (o = m).
 * Reports how many primes have NO certificate in each position class (and in each pair of classes).
 * Enumeration: words with c <= s (mirror covers the rest); c <= sqrt(p)+2; h | p + c, h = -1 (mod c), s = (p+c)/h >= c.
 * usage: y5_positions X [A]   (A: all non-square N = 1 (mod 4) <= X; certificate = 8 | ee') */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int *spf;
static int divs(ll n, ll *D) { ll P[40]; int E[40], k = 0; while (n > 1) { ll q = spf[n]; int e = 0; while (n % q == 0) { n /= q; e++; } P[k] = q; E[k++] = e; }
  int nd = 1; D[0] = 1; for (int i = 0; i < k; i++) { int cur = nd; ll pw = 1; for (int e = 1; e <= E[i]; e++) { pw *= P[i]; for (int j = 0; j < cur; j++) D[nd++] = D[j] * pw; } } return nd; }
int main(int argc, char **argv) {
  ll X = atoll(argv[1]); ll L = X + 2 * 40000; spf = calloc(L + 1, sizeof(int));
  for (ll i = 2; i <= L; i++) if (!spf[i]) for (ll j = i; j <= L; j += i) if (!spf[j]) spf[j] = i;
  static ll D[100000]; ll cnt = 0; ll z4m = 0, sHx = 0, ex4m_p[10]; int ex4m = 0; ll cnt840 = 0, tH = 0, tC = 0, tM = 0, zH = 0, zC = 0, zM = 0; ll sH = 0, sC = 0, sM = 0, minH = 1LL << 60, minp[12]; int nmin = 0; ll noneF[8] = {0}, noneI[8] = {0}; ll example[8] = {0};
  int allN = argc > 2; /* mode A: all non-square N = 1 (mod 4) instead of primes = 1 (8) */
  for (ll p = allN ? 5 : 17; p <= X; p += allN ? 4 : 8) { if (allN) { ll r = 1; while ((r + 1) * (r + 1) <= p) r++; if (r * r == p) continue; } else if (spf[p] != p) continue; cnt++;
    int maskF = 0, maskI = 0; ll cH = 0, cC = 0, cM = 0, c4m = 0, cHx = 0;
    for (ll c = 1; c * c <= p + 2 * c + 4; c++) { ll n = p + c; int nd = divs(n, D);
      for (int i = 0; i < nd; i++) { ll h = D[i]; if ((h + 1) % c) continue; ll m = (h + 1) / c, s = n / h; if (m < 1 || s < c) continue;
        ll hp = m * s - 1; ll q[5] = {hp, c, m, s, h}; int ev[2], ne = 0; for (int j = 0; j < 5; j++) if (q[j] % 2 == 0 && ne < 2) ev[ne++] = j;
        int e0 = ((ev[1] - ev[0]) % 5 == 1) ? ev[0] : ev[1]; if ((q[e0] * q[(e0 + 1) % 5]) % 8) continue; /* not a certificate: N = 1 (4) needs 8 | ee' (FRIEZE Cor 1.3) */
        int pos = (e0 + 3) % 5; /* index of o: 0=h',1=c,2=m,3=s,4=h */
        int cls = (pos == 0 || pos == 4) ? 1 : ((pos == 1 || pos == 3) ? 2 : 4);
        if (m % 4 == 0) c4m++; if (cls == 1 && m % 4) cHx++;
        if (cls == 1) cH++; else if (cls == 2) cC++; else cM++;
        maskF |= cls; if (c >= 2 && m >= 2 && s >= 2) maskI |= cls; } }
    z4m += !c4m; if (!c4m && ex4m < 10) ex4m_p[ex4m++] = p; sHx += cHx; sH += cH; sC += cC; sM += cM; if (p % 840 == 1) { cnt840++; tH += cH; tC += cC; tM += cM; zH += !cH; zC += !cC; zM += !cM; } if (cH < minH) { minH = cH; nmin = 0; } if (cH == minH && nmin < 12) minp[nmin++] = p;
    for (int S = 1; S < 8; S++) { if (!(maskF & S)) { noneF[S]++; if (!example[S]) example[S] = p; if (allN && S == 1) printf("  no H-certificate (formal) at N = %lld\n", p); } if (!(maskI & S)) noneI[S]++; } }
  printf("%s <= %lld: %lld\n", allN ? "non-square N=1(4)" : "primes p=1(8)", X, cnt);
  printf("mean #certificate words (formal, c<=s half) per prime: H %.2f C %.2f M %.2f; min H count %lld at:", (double)sH / cnt, (double)sC / cnt, (double)sM / cnt, minH);
  for (int i = 0; i < nmin; i++) printf(" %lld", minp[i]); printf("\n");
  printf("p = 1 (mod 840): %lld primes; mean H %.2f C %.2f M %.2f; #zero (formal): H %lld C %lld M %lld\n", cnt840, (double)tH / cnt840, (double)tC / cnt840, (double)tM / cnt840, zH, zC, zM);
  printf("slice 4|m alone (classical p = 4kcs-c-s): primes with none %lld; first:", z4m); for (int i = 0; i < ex4m; i++) printf(" %lld", ex4m_p[i]);
  printf("\nmean # H-words with m = 2 (mod 4): %.2f\n", (double)sHx / cnt);
  const char *nm[8] = {"", "H", "C", "H+C", "M", "H+M", "C+M", "all"};
  for (int S = 1; S < 8; S++) printf("no certificate in positions %-4s: formal %lld (first %lld)  interior %lld\n", nm[S], noneF[S], example[S], noneI[S]);
  return 0; }
