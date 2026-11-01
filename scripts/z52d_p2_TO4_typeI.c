// z52d pass2 TO4: Type I with c=1 (CONDITIONAL_ES.md §1): f | p^2+4d and f ≡ -p (mod 4d), for 1<=d<=D.
// Output per prime p ≡ 1 (mod 4), p<=P:  "p k d1 d2 ..." listing d<=D admitting such f (k = count).
// Usage: ./typeI P D [PMIN] > out.txt
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int *smallp; static int nsp;
static int has_f(u64 N, u64 m, u64 r){ // exists divisor f of N with f ≡ r (mod m)?  (r in [0,m))
    u64 fac[64]; int ex[64]; int nf=0; u64 n=N;
    for(int i=0;i<nsp;i++){ u64 q=smallp[i]; if(q*q>n) break; if(n%q==0){ int e=0; while(n%q==0){n/=q;e++;} fac[nf]=q; ex[nf]=e; nf++; } }
    if(n>1){ fac[nf]=n; ex[nf]=1; nf++; }
    static u64 divs[1<<16]; int nd=1; divs[0]=1;
    for(int i=0;i<nf;i++){ int cur=nd; u64 pw=1; for(int e=1;e<=ex[i];e++){ pw*=fac[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
    for(int j=0;j<nd;j++) if(divs[j] % m == r) return 1;
    return 0;
}
int main(int argc,char**argv){
    u64 P=strtoull(argv[1],0,10); int D=atoi(argv[2]);
    u64 PMIN = argc>3? strtoull(argv[3],0,10):5;
    u64 maxN = P*P + 4ULL*D + 1; u64 lim=1; while(lim*lim<=maxN) lim++;
    char*sv=calloc(lim+1,1); smallp=malloc(sizeof(int)*(lim+1)); nsp=0;
    for(u64 i=2;i<=lim;i++){ if(!sv[i]){ smallp[nsp++]=(int)i; for(u64 j=i*i;j<=lim;j+=i) sv[j]=1; } }
    char*ps=calloc(P+1,1); for(u64 i=2;i<=P;i++) if(!ps[i]) for(u64 j=i*i;j<=P;j+=i) ps[j]=1;
    static int ds[100000];
    for(u64 p=PMIN;p<=P;p++){
        if(ps[p]||p%4!=1) continue;
        int k=0;
        for(int d=1; d<=D; d++){
            u64 m=4ULL*d; u64 r=(m - (p%m))%m; // -p mod m
            if(has_f(p*p+4ULL*d, m, r)) ds[k++]=d;
        }
        printf("%llu %d",(unsigned long long)p,k); for(int i=0;i<k;i++) printf(" %d",ds[i]); printf("\n");
    }
    return 0;
}
