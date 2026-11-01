/* Z1018: Frobenius/conductor test for the (*) word set S = {4uBC-u-B : u,B,C>=1}.
   For odd n <= N, minlev[n] = least C over all (u,B) with 4uBC-u-B = n (0 = no word).
   Reports the gap set (no word at any level), split square/non-square, n mod 4, prime/composite,
   and the level-restricted gap counts G_K = #{odd non-square n<=N : no word with C<=K}.
   Usage: ./a.out N */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static int is_sq(uint64_t n){uint64_t r=(uint64_t)sqrtl((long double)n);while(r*r>n)r--;while((r+1)*(r+1)<=n)r++;return r*r==n;}
static int is_prime(uint64_t n){if(n<2)return 0;for(uint64_t d=2;d*d<=n;d++)if(n%d==0)return 0;return 1;}
int main(int argc,char**argv){
  uint64_t N=strtoull(argv[1],0,10);
  uint64_t M=N/2+1; /* index n>>1 for odd n */
  uint16_t *lev=calloc(M,2); if(!lev){perror("calloc");return 1;}
  for(uint64_t u=1;4*u-u-1<=N;u++) for(uint64_t B=1;4*u*B-u-B<=N;B++){
    uint64_t q=4*u*B, n=q-u-B;
    for(uint64_t C=1;n<=N;C++,n+=q){ if(n&1){uint64_t i=n>>1; if(lev[i]==0||lev[i]>C) lev[i]=(C>65535?65535:C);} }
  }
  /* gap census */
  uint64_t gsq=0,gns=0,gns1=0,gns3=0,gnsp=0,last_ns=0; int printed=0;
  int Ks[]={1,2,4,8,16,32,64,128,256,1024,4096,65535}; int nK=12; uint64_t GK[12]={0};
  for(uint64_t n=3;n<=N;n+=2){ uint16_t L=lev[n>>1]; int sq=is_sq(n);
    if(!sq) for(int k=0;k<nK;k++) if(L==0||L>Ks[k]) GK[k]++;
    if(L) continue;
    if(sq){gsq++;continue;}
    gns++; last_ns=n; if(n%4==1)gns1++; else gns3++;
    int pr=(n<4000000000ULL)?is_prime(n):-1; if(pr==1)gnsp++;
    if(1){printf("gap %llu mod4=%llu prime=%d mod840=%llu\n",(unsigned long long)n,(unsigned long long)(n%4),pr,(unsigned long long)(n%840));printed++;}
  }
  printf("N=%llu odd-square gaps=%llu (all odd squares>1 expected: %llu)\n",(unsigned long long)N,(unsigned long long)gsq,(unsigned long long)(((uint64_t)sqrtl((long double)N)+1)/2-1));
  printf("non-square gaps=%llu (n=1 mod4: %llu, n=3 mod4: %llu, prime: %llu) largest non-square gap=%llu\n",(unsigned long long)gns,(unsigned long long)gns1,(unsigned long long)gns3,(unsigned long long)gnsp,(unsigned long long)last_ns);
  for(int k=0;k<nK;k++) printf("G_K K=%d nonsquare-odd-uncovered=%llu frac=%.6f\n",Ks[k],(unsigned long long)GK[k],(double)GK[k]/(N/2));
  return 0;
}
