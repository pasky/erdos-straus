// z70 CLASS item 2c: (*) solutions p = 4uBC - u - B with small modulus d = 4uC - 1 <= DMAX (exhaustive in that range).
// Input: first number of each stdin line = p.  Output: "S p count" then lines "u B C d".
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(int argc, char **argv){
  u64 DMAX = argc > 1 ? strtoull(argv[1], 0, 10) : 100000ULL; u64 p;
  static u64 buf[4000000][3];
  while (scanf("%llu%*[^\n]", &p) == 1) {
    int n = 0;
    for (u64 u = 1; 4*u - 1 <= DMAX; u++)
      for (u64 C = 1; 4*u*C - 1 <= DMAX; C++) {
        u64 d = 4*u*C - 1;
        if ((p + u) % d == 0) { if (n >= 4000000) { fprintf(stderr, "buffer\n"); return 3; }
          buf[n][0] = u; buf[n][1] = (p + u) / d; buf[n][2] = C; n++; }
      }
    printf("S %llu %d\n", p, n);
    for (int i = 0; i < n; i++) printf("%llu %llu %llu %llu\n", buf[i][0], buf[i][1], buf[i][2], 4*buf[i][0]*buf[i][2] - 1);
  }
  return 0;
}
