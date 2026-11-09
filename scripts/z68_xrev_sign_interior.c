/* Independent corrected KT3 interior-no-outgoing-move census, p <= 200000.
   Compile with cc -O2; fixed allocations < 1 MB; no lane routines imported. */
#include <stdio.h>
#include <stdint.h>
static unsigned char composite[200001];
static int gcd(int a, int b) { while (b) { int c = a % b; a = b; b = c; } return a; }
static int movable(int b, int other) {
    int g = gcd(b, other);
    if (g == 1) return 0;
    for (int d = 2; d <= g / d; ++d)
        if (g % d == 0) return b / d >= 2;
    return b / g >= 2;
}
static int negative(int a, int p) {
    int e = (p - 1) / 2;
    int64_t x = a, y = 1;
    while (e) {
        if (e & 1) y = y * x % p;
        x = x * x % p;
        e >>= 1;
    }
    return y == p - 1;
}
int main(void) {
    for (int i = 2; i <= 200000 / i; ++i)
        if (!composite[i]) for (int j = i * i; j <= 200000; j += i) composite[j] = 1;
    puts("# p L3 neg3 L4 interior_noout neg_interior_noout");
    for (int p = 10001; p <= 200000; p += 8) {
        if (composite[p]) continue;
        int L3 = 0, neg3 = 0, L4 = 0, no = 0, negno = 0;
        for (int a = 1; a < p; ++a) {
            int n = p, d = a, w[5], r = 0;
            while (d && r < 5) {
                int b = (n + d - 1) / d, rem = b * d - n;
                w[r++] = b; n = d; d = rem;
            }
            if (d) continue;
            if (r == 3) { ++L3; neg3 += negative(a, p); }
            if (r == 4) {
                ++L4;
                /* At b the only direction needs k|b,d; at c it needs k|c,a. */
                if (!movable(w[1], w[3]) && !movable(w[2], w[0])) {
                    ++no; negno += negative(a, p);
                }
            }
        }
        printf("%d %d %d %d %d %d\n", p, L3, neg3, L4, no, negno);
    }
    return 0;
}
