/* exf_hurwitz.c — O131: 12*H(D) for all 0 <= D <= M (Hurwitz class numbers, H(0) = -1/12), via reduced forms.
 * Reduced: |b| <= a <= c, b >= 0 if |b| == a or a == c. Weight 1/2 for a==c,b==0; 1/3 for a==b==c. Output int32 file. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){ long M=atol(argv[1]); int32_t *H=calloc(M+1,4); H[0]=-1;
  for(long a=1; 3*a*a<=M; a++) for(long b=-a; b<=a; b++){
    for(long c=a; 4*a*c-b*b<=M; c++){ if(b<0 && (-b==a || a==c)) continue;
      long D=4*a*c-b*b; int w=12; if(a==c && b==0) w=6; if(a==b && b==c) w=4; H[D]+=w; } }
  FILE*o=fopen(argv[2],"wb"); fwrite(H,4,M+1,o); fclose(o); return 0; }
