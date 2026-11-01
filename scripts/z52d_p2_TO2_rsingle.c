// R(n) for a single n: #{(u,B,C) >= 1 : 4uBC - u - B = n}. Usage: z52d_p2_TO2_rsingle n
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
    long long n = atoll(argv[1]), cnt = 0;
    for (long long u = 1; 3*u - 1 <= n; u++)
        for (long long B = 1; 4*u*B - u - B <= n; B++) {
            long long t = n + u + B, m4 = 4*u*B;
            if (t % m4 == 0) cnt++;
        }
    printf("%lld %lld\n", n, cnt);
    return 0;
}
