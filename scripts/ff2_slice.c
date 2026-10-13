/* ff2_slice.c (O166) — slice test of the obstructed set O(q,A) (FUNCTIONFIELD_ES2.md §0.1):
 * for every unit u mod ell^e, the class x = u (mod ell^e), x = v (mod W'), is tested against all linear families
 * with W_F | ell^e W' (find_family of ff2_tree.c).  usage: ff2_slice q A ell e W'_factor_list v NTH
 * Output: one line per u: u FOUND/NONE (+family). */
#define main ffl_tree_main
#include "ff2_tree.c"
#undef main
int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage\n"); return 1; }
    field_init(atoi(argv[1])); parse(argv[2], &Apoly, 0); K = Apoly.d;
    poly ell; parse(argv[3], &ell, 0); int e = atoi(argv[4]); add_prime(&ell);
    poly roots[64]; int nr = parse(argv[5], roots, 1); poly W2; parse(argv[5], &W2, 0);
    for (int i = 0; i < nr; i++) add_prime(&roots[i]);
    poly Ap[64]; int na = parse(argv[2], Ap, 1); for (int i = 0; i < na; i++) add_prime(&Ap[i]);
    poly v; parse(argv[6], &v, 0); p_divmod(NULL, &v, &v, &W2); NTH = atoi(argv[7]); V = 0;
    poly Le = {.d = 0}; Le.c[0] = 1; for (int i = 0; i < e; i++) p_mul(&Le, &Le, &ell);
    poly W; p_mul(&W, &Le, &W2);
    int D = Le.d; static poly table[1 << 20]; static int have[1 << 20];
    /* map t -> (v + W2 t) mod Le, invert */
    for (uint64_t t = 0; t < qpow[D]; t++) { poly tt; tt.d = D - 1; for (int i = 0; i < D; i++) tt.c[i] = (t / qpow[i]) % Q; p_trim(&tt);
        poly r; p_mul(&r, &W2, &tt); p_add(&r, &r, &v); poly ru; p_divmod(NULL, &ru, &r, &Le);
        uint64_t key = 0; for (int i = D - 1; i >= 0; i--) key = key * Q + (i <= ru.d ? ru.c[i] : 0);
        table[key] = r; have[key] = 1; }
    long nnone = 0, ntot = 0;
    for (uint64_t key = 0; key < qpow[D]; key++) {
        poly u; u.d = D - 1; for (int i = 0; i < D; i++) u.c[i] = (key / qpow[i]) % Q; p_trim(&u);
        poly g; p_gcd(&g, &u, &ell); if (u.d < 0 || g.d != 0) continue;
        if (!have[key]) { fprintf(stderr, "CRT fail\n"); return 1; }
        poly r = table[key]; ntot++;
        poly Tm; int m = (W.d > NTH ? W.d : NTH) + 2; Tm.d = m; memset(Tm.c, 0, m + 1); Tm.c[m] = 1;
        poly P; p_mul(&P, &W, &Tm); p_add(&P, &P, &r);
        poly E, a0, b0; int ta, tb; p_print(stdout, &u);
        if (find_family(&P, &W, &E, &ta, &a0, &tb, &b0)) { printf(" FOUND E="); p_print(stdout, &E); printf(" a=(t%d,", ta); p_print(stdout, &a0); printf(") b=(t%d,", tb); p_print(stdout, &b0); printf(")\n"); }
        else { printf(" NONE\n"); nnone++; }
    }
    printf("# uncovered %ld / %ld\n", nnone, ntot);
    return 0;
}
