/* ff2_point.c (O166) — test one residue class r mod W against all linear families (FUNCTIONFIELD_ES.md §6.2)
 * with A*E*lcm(a0,b0) | W (E | W/A up to units), deg a0+deg b0+k < NTH, deg E < NTH.  Reuses ffl_tree.c's
 * find_family.  usage: ff2_point q A W_factor_list r NTH   (r given like W, as high->low digits)
 * Prints the family found or NONE. */
#define main ffl_tree_main
#include "ff2_tree.c"
#undef main
int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage\n"); return 1; }
    field_init(atoi(argv[1])); parse(argv[2], &Apoly, 0); K = Apoly.d;
    poly roots[64]; int nr = parse(argv[3], roots, 1); poly W; parse(argv[3], &W, 0);
    for (int i = 0; i < nr; i++) add_prime(&roots[i]);
    poly Ap[64]; int na = parse(argv[2], Ap, 1); for (int i = 0; i < na; i++) add_prime(&Ap[i]);
    poly r; parse(argv[4], &r, 0); p_divmod(NULL, &r, &r, &W);
    NTH = atoi(argv[5]); V = 0;
    poly Tm; int m = (W.d > NTH ? W.d : NTH) + 2; Tm.d = m; memset(Tm.c, 0, m + 1); Tm.c[m] = 1;
    poly P; p_mul(&P, &W, &Tm); p_add(&P, &P, &r);
    poly E, a0, b0; int ta, tb;
    if (find_family(&P, &W, &E, &ta, &a0, &tb, &b0)) { printf("FOUND E="); p_print(stdout, &E); printf(" a=(t%d,", ta); p_print(stdout, &a0); printf(") b=(t%d,", tb); p_print(stdout, &b0); printf(")\n"); }
    else printf("NONE\n");
    return 0;
}
