/* fz1_caseA_enum.c (O220): exact upper count of k = 1 Case A data on the slices u0 not in F_3 (FF_STERILE_SMALL §7):
   per pattern (alpha; lam, be, ka): data (a1', b1, K), a1' monic deg lam, b1 monic deg be, K deg ka with lc(K) in {1, 2},
   all T-free, gcd(a1', b1) = 1, E = a1' b1 K - 1 with E | T^alpha a1' + b1, deg(T^alpha a1' + b1) - deg E = f = alpha - be - ka,
   and E(0) not in F_3. Route (ix): E | 1 + T^alpha a1'^2 K (b1 == -T^alpha a1' mod E and a1' b1 K == 1 mod E), E == -1 mod a1'K;
   so for each (a1', K) factor D = 1 + T^alpha a1'^2 K and run over its divisors of degree lam + be + ka (times lc(K)).
   usage: fz1_caseA_enum q AMAX [filter=1] [brute=0]   prints "A alpha lam be ka count" */
#define main fz1_enum_main
#include "fz1_enum.c"
#undef main
static int A_al, A_la, A_be, A_ka, AFILT = 1, ABRUTE = 0; static poly A_a1, A_K; static long A_cnt;
static void cbA(const poly *Em) {      /* Em: monic divisor; E = lc(K) * Em */
  poly E, one, Ep1, aK, b1, rr; pscal(&E, Em, A_K.c[A_K.d]);
  pmul(&aK, &A_a1, &A_K); one.d = 0; one.c[0] = 1; padd(&Ep1, &E, &one);
  pdivmod(&b1, &rr, &Ep1, &aK); if (rr.d >= 0) return;
  if (b1.d != A_be || b1.c[b1.d] != 1 || !b1.c[0]) return;
  poly g; pgcd(&g, &A_a1, &b1); if (g.d != 0) return;
  poly Ta, num, F; pshift(&Ta, &A_a1, A_al); padd(&num, &Ta, &b1); pdivmod(&F, &rr, &num, &E); if (rr.d >= 0) return;
  if (F.d != A_al - A_be - A_ka) return;
  int e0 = E.c[0]; if (AFILT && (e0 == 0 || e0 == 1 || e0 == ADD[1][1])) return;          /* slice filter */
  A_cnt++;
}
int main(int argc, char **argv) {
  int q = atoi(argv[1]), AMAX = atoi(argv[2]); field_init(q); if (argc > 3) AFILT = atoi(argv[3]); if (argc > 4) ABRUTE = atoi(argv[4]);
  for (int x = 0; x < q; x++) for (int y = 0; y < q; y++) { int p = 1; for (int k = 0; k < PCH; k++) p = MUL[p][y]; if (p == x) PROOT[x] = y; }
  for (int al = 1; al <= AMAX; al++) for (int be = 0; be <= al; be++) for (int ka = 0; be + ka <= al; ka++) {
    int f = al - be - ka; int zmax = f > be ? f : be;
    for (int la = 0; la <= zmax; la++) {
      A_al = al; A_la = la; A_be = be; A_ka = ka; A_cnt = 0;
      if (AFILT && la + be + ka == 0) { printf("A %d %d %d %d 0\n", al, la, be, ka); continue; }   /* E constant: E(0) in F_3 */
      poly a1; FOR_MONIC(a1, la) { for (int lk = 1; lk <= 2; lk++) { poly K; FOR_MONIC(K, ka) {
        poly Kl; pscal(&Kl, &K, lk == 1 ? 1 : ADD[1][1]); A_a1 = a1; A_K = Kl;
        poly D, aa, one; pmul(&aa, &a1, &a1); pmul(&aa, &aa, &Kl); pshift(&D, &aa, al); one.d = 0; one.c[0] = 1; padd(&D, &D, &one);
        if (!ABRUTE) { fact Fc; factor(&Fc, &D); divisors(&Fc, la + be + ka, cbA); }
        else { poly b1; FOR_MONIC(b1, be) {     /* validation: run over b1 directly, E = a1' b1 K - 1, pass E/lc(K) */
          poly E, one2, Em; pmul(&E, &a1, &b1); pmul(&E, &E, &Kl); one2.d = 0; one2.c[0] = 1; psub(&E, &E, &one2);
          if (E.d != la + be + ka) continue; pscal(&Em, &E, INV[Kl.c[Kl.d]]); cbA(&Em); } } } } }
      printf("A %d %d %d %d %ld\n", al, la, be, ka, A_cnt); fflush(stdout);
    }
  }
  return 0;
}
