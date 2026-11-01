// z52d pass2 TO4: C-form winning sets. For prime p ≡ 1 (mod 4), p ≤ P, and C ≤ K:
// win(p,C) iff exists a | 4Cp+1 with a ≡ -1 (mod 4C)  (CForm n C a := a | 4Cn+1 ∧ 4C | a+1).
// VARIANT: all n ≡ 1 (mod 4) (not only primes). Output per n: "p k w1 w2 ..." where w_i are winning C (sorted), k = number of winning C ≤ K.
// Usage: ./cform P K [PMIN] > out.txt   (memory: O(sqrt(4KP)) primes; PMIN restricts to p>=PMIN)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
static int *smallp; static int nsp;
static int isprime_u(u64 n){ if(n<2) return 0; for(u64 d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
// returns 1 iff N has a divisor a with a ≡ -1 mod m (a>1), by full divisor enumeration via factorization
static int has_div_mod(u64 N, u64 m){
    // factor N
    u64 fac[64]; int ex[64]; int nf=0; u64 n=N;
    for(int i=0;i<nsp;i++){ u64 q=smallp[i]; if(q*q>n) break; if(n%q==0){ int e=0; while(n%q==0){n/=q;e++;} fac[nf]=q; ex[nf]=e; nf++; } }
    if(n>1){ fac[nf]=n; ex[nf]=1; nf++; }
    // enumerate divisors (iterative) and test a % m == m-1
    static u64 divs[1<<16]; int nd=1; divs[0]=1;
    for(int i=0;i<nf;i++){ int cur=nd; u64 pw=1; for(int e=1;e<=ex[i];e++){ pw*=fac[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
    for(int j=0;j<nd;j++){ u64 a=divs[j]; if(a>1 && a % m == m-1) return 1; }
    return 0;
}
int main(int argc, char**argv){
    u64 P=strtoull(argv[1],0,10); int K=atoi(argv[2]);
    u64 maxN = 4ULL*K*P+1; u64 lim=1; while(lim*lim<=maxN) lim++;
    char *sv=calloc(lim+1,1); smallp=malloc(sizeof(int)*(lim+1)); nsp=0;
    for(u64 i=2;i<=lim;i++){ if(!sv[i]){ smallp[nsp++]=(int)i; for(u64 j=i*i;j<=lim;j+=i) sv[j]=1; } }
    char *ps=calloc(P+1,1); for(u64 i=2;i<=P;i++) if(!ps[i]) for(u64 j=i*i;j<=P;j+=i) ps[j]=1;
    int wins[4096];
    u64 PMIN = argc>3 ? strtoull(argv[3],0,10) : 5;
    for(u64 p=PMIN;p<=P;p++){
        if(p%4!=1) continue; // ALL n ≡ 1 mod 4 (z52d Z1630 variant)
        int k=0;
        for(int C=1;C<=K;C++){
            if(has_div_mod(4ULL*C*p+1, 4ULL*C)) wins[k++]=C;
        }
        printf("%llu %d", (unsigned long long)p, k);
        for(int i=0;i<k;i++) printf(" %d", wins[i]);
        printf("\n");
    }
    return 0;
}
