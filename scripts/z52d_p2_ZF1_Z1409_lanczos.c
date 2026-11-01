/* Z1409: fast version of scripts/z52d_p2_ZF1_Z1409_qubo.py (same QUBO, same M rule, same normalisation).
 * (★) line at fixed C: 4C uB - u - B = p, u, B b-bit, Rosenberg ancillas w_ij = u_i B_j; nq = 2b + b^2.
 * H(s) = -(1-s) sum_q X_q + s H_P/scale.  Lowest two DISTINCT eigenvalues by plain Lanczos (no reorthogonalisation; ghost
 * copies are merged with a 1e-9 tolerance), m = 800 steps, deterministic start vector; E1 - E0 on an s-grid that is dense near 1.
 * The Krylov space is restricted to the S-symmetric sector (see lowest2), so the ground doublet {(u,B),(B,u)} does not
 * produce a spurious tunnel-splitting gap.
 * Also the classical data: E0, classical gap, ground degeneracy, solutions.  usage: lanczos b C p1,p2,... [end] [m]   ('end': s-grid 0.9..0.999 only)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int b, nq; static long D; static double *Hd;
static long swapS(long x) { long y = 0; for (int i = 0; i < b; i++) { y |= (x >> i & 1) << (b + i); y |= (x >> (b + i) & 1) << i;
    for (int j = 0; j < b; j++) y |= (x >> (2*b + b*i + j) & 1) << (2*b + b*j + i); } return y; }
static double *Vb; /* Krylov basis, m x D (full reorthogonalisation) */
static double lowest2(double s, double *v, double *w, double *vold, double *alpha, double *beta, int m, double *e1) {
    (void)vold;
    /* start vector symmetrised under the exact qubit symmetry S: u_i <-> B_i, w_ij <-> w_ji (H(s) commutes with S; the
       annealing state starts uniform, hence S-symmetric, and never leaves the symmetric sector) */
    for (long i = 0; i < D; i++) v[i] = 1.0 + 0.5 * (((i * 2654435761u) >> 7) % 1000) / 1000.0;
    for (long i = 0; i < D; i++) { long j = swapS(i); if (j > i) { double m2 = 0.5 * (v[i] + v[j]); v[i] = v[j] = m2; } }
    double nr = 0; for (long i = 0; i < D; i++) nr += v[i] * v[i]; nr = sqrt(nr); for (long i = 0; i < D; i++) v[i] /= nr;
    int k;
    for (k = 0; k < m; k++) {
        memcpy(Vb + (long)k * D, v, 8 * D);
        for (long i = 0; i < D; i++) { double acc = s * Hd[i] * v[i]; for (int q = 0; q < nq; q++) acc -= (1 - s) * v[i ^ (1L << q)]; w[i] = acc; }
        double a = 0; for (long i = 0; i < D; i++) a += w[i] * v[i]; alpha[k] = a;
        for (int pass = 0; pass < 2; pass++) for (int j = 0; j <= k; j++) { double *u = Vb + (long)j * D; double c = 0;
            for (long i = 0; i < D; i++) c += w[i] * u[i]; for (long i = 0; i < D; i++) w[i] -= c * u[i]; }
        double bb = 0; for (long i = 0; i < D; i++) bb += w[i] * w[i]; bb = sqrt(bb); beta[k] = bb;
        if (bb < 1e-10) { k++; break; }
        for (long i = 0; i < D; i++) v[i] = w[i] / bb;
    }
    /* eigenvalues of tridiagonal (k x k) by bisection: lowest values via Sturm count */
    int n = k; double lo = -1e9, hi = 1e9;
    for (int i = 0; i < n; i++) { double r = fabs(i ? beta[i-1] : 0) + fabs(i < n-1 ? beta[i] : 0); if (alpha[i]-r < lo || lo == -1e9) lo = alpha[i]-r; if (alpha[i]+r > hi || hi == 1e9) hi = alpha[i]+r; }
    #define STURM(x, cnt) { cnt = 0; double d = 1; for (int i = 0; i < n; i++) { d = alpha[i] - (x) - (i ? beta[i-1]*beta[i-1]/d : 0); if (d == 0) d = 1e-300; if (d < 0) cnt++; } }
    double ev[16]; for (int j = 0; j < 16 && j < n; j++) { double l = lo, h = hi; for (int it = 0; it < 200; it++) { double mid = 0.5*(l+h); int c; STURM(mid, c); if (c > j) h = mid; else l = mid; } ev[j] = 0.5*(l+h); }
    double E0 = ev[0], E1 = NAN; for (int j = 1; j < 16 && j < n; j++) if (ev[j] - E0 > 1e-8) { E1 = ev[j]; break; }  /* merge ghost copies */
    *e1 = E1; return E0;
}
int main(int argc, char **argv) {
    b = atoi(argv[1]); int C = atoi(argv[2]); nq = 2*b + b*b; D = 1L << nq;
    Hd = malloc(8*D); double *L2 = malloc(8*D); int *pen = malloc(4*D);
    double *v = malloc(8*D), *w = malloc(8*D), *vo = malloc(8*D); int m = argc > 5 ? atoi(argv[5]) : 240; Vb = malloc(8L * m * D); double alpha[1000], beta[1000];
    double a[64] = {0}; for (int i = 0; i < b; i++) { a[i] = -(1<<i); a[b+i] = -(1<<i); for (int j = 0; j < b; j++) a[2*b+b*i+j] = 4.0*C*(1<<(i+j)); }
    char *tok = strtok(argv[3], ",");
    double sg[64]; int ns = 0;
    if (argc > 4 && !strcmp(argv[4], "end")) { double fine[] = {0.9, 0.95, 0.97, 0.98, 0.99, 0.993, 0.995, 0.997, 0.998, 0.999}; for (int i = 0; i < 10; i++) sg[ns++] = fine[i]; }
    else { for (double s = 0.05; s < 0.951; s += 0.05) sg[ns++] = s;
      double fine[] = {0.96, 0.97, 0.98, 0.99, 0.995, 0.998, 0.999}; for (int i = 0; i < 7; i++) sg[ns++] = fine[i]; }
    while (tok) {
        int p = atoi(tok); tok = strtok(NULL, ",");
        double E1c = 1e300, E0c = 1e300;
        for (long x = 0; x < D; x++) { double L = -p; for (int q = 0; q < nq; q++) if (x >> q & 1) L += a[q]; L2[x] = L*L;
            int pe = 0; for (int i = 0; i < b; i++) for (int j = 0; j < b; j++) { int ui = x>>i&1, bj = x>>(b+j)&1, wij = x>>(2*b+b*i+j)&1;
                pe += ui*bj - 2*ui*wij - 2*bj*wij + 3*wij; } pen[x] = pe;
            if (!pe) { if (L*L < E0c) { E1c = E0c; E0c = L*L; } else if (L*L > E0c && L*L < E1c) E1c = L*L; } }
        long M = 1; for (;;) { double mn = 1e300; for (long x = 0; x < D; x++) if (pen[x] && L2[x] + M*pen[x] < mn) mn = L2[x] + M*pen[x]; if (mn >= E1c) break; M *= 2; }
        double E0 = 1e300, E1 = 1e300; long g = 0;
        for (long x = 0; x < D; x++) { Hd[x] = L2[x] + M*pen[x]; if (Hd[x] < E0) { E1 = E0; E0 = Hd[x]; g = 1; } else if (Hd[x] == E0) g++; else if (Hd[x] < E1) E1 = Hd[x]; }
        /* QUBO max |coeff| */
        double mx = 0; for (int q = 0; q < nq; q++) { double d = a[q]*a[q] - 2.0*p*a[q]; for (int i = 0; i < b; i++) for (int j = 0; j < b; j++) if (q == 2*b+b*i+j) d += 3*M; if (fabs(d) > mx) mx = fabs(d); }
        for (int q = 0; q < nq; q++) for (int r = q+1; r < nq; r++) { double c = 2*a[q]*a[r];
            for (int i = 0; i < b; i++) for (int j = 0; j < b; j++) { int x = i, y = b+j, ww = 2*b+b*i+j;
                if (q == x && r == y) c += M; if (q == x && r == ww) c -= 2*M; if (q == y && r == ww) c -= 2*M; }
            if (fabs(c) > mx) mx = fabs(c); }
        for (long x = 0; x < D; x++) Hd[x] /= mx;
        printf("{\"p\": %d, \"b\": %d, \"C\": %d, \"nq\": %d, \"M\": %ld, \"scale\": %.0f, \"E0\": %.0f, \"classical_gap\": %.0f, \"ground_deg\": %ld, \"sols\": [", p, b, C, nq, M, mx, E0, E1-E0, g);
        int first = 1; if (E0 == 0) for (long x = 0; x < D; x++) if (Hd[x] == 0) { int uu = 0, BB = 0; for (int i = 0; i < b; i++) { uu += (x>>i&1)<<i; BB += (x>>(b+i)&1)<<i; } printf("%s[%d,%d]", first ? "" : ",", uu, BB); first = 0; }
        printf("], \"gaps\": [");
        double gmin = 1e9, smin = 0;
        for (int i = 0; i < ns; i++) { double e1, e0 = lowest2(sg[i], v, w, vo, alpha, beta, m, &e1); double gp = e1 - e0; if (gp < gmin) { gmin = gp; smin = sg[i]; } printf("%s[%.4f,%.6g]", i ? "," : "", sg[i], gp); }
        double g1 = (E1 - E0) / mx; if (g1 < gmin) { gmin = g1; smin = 1.0; }
        printf("], \"gap_s1\": %.6g, \"min_gap\": %.6g, \"s_at_min\": %.4f}\n", g1, gmin, smin); fflush(stdout);
    }
    return 0;
}
