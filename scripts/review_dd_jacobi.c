/* R176 from scratch: least Jacobi index F*(p) = min over Type II pairs of min(f,f') for primes p = 1 (24) < PMAX.
   By Thm 2.1 (re-derived): F*(p) = min{ f : exists c,d with 4cd | f+1 and f | 1+4c^2 d p }. Prints records. */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(int argc,char**argv){ u64 PMAX=atoll(argv[1]); char*s=calloc(PMAX+1,1); u64 rec=0;
 for(u64 i=2;i<=PMAX;i++) if(!s[i]) for(u64 j=i*i;j<=PMAX;j+=i) s[j]=1;
 for(u64 p=5;p<PMAX;p++){ if(s[p]||p%24!=1) continue;
  for(u64 f=3;;f+=4){ u64 K=(f+1)/4; int ok=0;
    for(u64 c=1;c<=K && !ok;c++) if(K%c==0){ u64 R=K/c; for(u64 d=1;d<=R;d++) if(R%d==0){
        if((1+(4*c*c*d%f)*(p%f))%f==0){ok=1;break;} } }
    if(ok){ if(f>rec){rec=f; printf("(%llu, %llu) ",p,f);} break; } } }
 printf("\n"); return 0; }
