/* Z1018 extension: bitset version of z52d_p2_ZF2_Z1018_conductor.c (no level data). Marks odd n <= N that are
   (*) words 4uBC-u-B (any u,B,C >= 1) and prints every odd non-square gap n in [LO, N].  Usage: ./a.out N LO */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static int is_sq(uint64_t n){uint64_t r=(uint64_t)sqrtl((long double)n);while(r*r>n)r--;while((r+1)*(r+1)<=n)r++;return r*r==n;}
int main(int argc,char**argv){
  uint64_t N=strtoull(argv[1],0,10), LO=strtoull(argv[2],0,10);
  uint64_t M=N/2+1; uint64_t *bits=calloc(M/64+1,8); if(!bits){perror("calloc");return 1;}
  for(uint64_t u=1;3*u-1<=N;u++) for(uint64_t B=1;4*u*B-u-B<=N;B++){
    uint64_t q=4*u*B, n=q-u-B; if(!(n&1)) continue; /* n parity fixed along the AP since q even */
    for(;n<=N;n+=q){uint64_t i=n>>1; bits[i>>6]|=1ULL<<(i&63);} }
  uint64_t g=0; for(uint64_t n=(LO|1);n<=N;n+=2){uint64_t i=n>>1; if(!(bits[i>>6]>>(i&63)&1) && !is_sq(n)){g++; printf("gap %llu\n",(unsigned long long)n);} }
  printf("# N=%llu LO=%llu nonsquare_gaps=%llu\n",(unsigned long long)N,(unsigned long long)LO,(unsigned long long)g);
  return 0; }
