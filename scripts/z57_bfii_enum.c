// z57 BFII: exhaustive Type II counts for all n <= X.
// Type II N-points: (a,b,d,e) in N^4 with e | a+b and n = 4abd - e  (c = (a+b)/e).
// Equivalent to 4abcd = a + b + nc (Elsholtz-Tao (2.15)).
// Usage: z57_bfii_enum X out.bin
// Output (binary): int64 X, then five uint32 arrays, each indexed by n = 0..X (all n, even ones are simply 0):
//   tot[n]  = #(a,b,d,e) [ordered (a,b)]                       = N_II(n)
//   c1[n]   = # of those with c = 1                             = (★) count R(n)
//   prim[n] = # of those with gcd(a,b,c) = 1                    (= f_II(n) for prime n)
//   cmax[n] = largest c occurring (0 if none)
//   emin[n] = least e occurring (0xffffffff if none)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  long X=atol(argv[1]);
  const char*out=argv[2];
  uint32_t *tot=calloc(X+1,4),*c1=calloc(X+1,4),*prim=calloc(X+1,4),*cmax=calloc(X+1,4);
  uint32_t *emin=malloc((X+1)*4); for(long i=0;i<=X;i++) emin[i]=0xffffffffu;
  // divisor lists for m <= M: a+b <= ? with 4abd - (a+b) <= X and d>=1: a+b <= 4ab - X? bound a+b <= X (safe: 4ab-a-b >= a+b-? ) use M = X+2
  long M=X+2;
  uint32_t *cnt=calloc(M+2,4);
  for(long e=1;e<=M;e++) for(long m=e;m<=M;m+=e) cnt[m]++;
  uint64_t *start=malloc((M+2)*8); start[0]=0; for(long m=1;m<=M+1;m++) start[m]=start[m-1]+cnt[m-1];
  uint32_t *divs=malloc(start[M+1]*4); memset(cnt,0,(M+2)*4);
  for(long e=1;e<=M;e++) for(long m=e;m<=M;m+=e){divs[start[m]+cnt[m]]=e;cnt[m]++;}
  for(long a=1;;a++){
    if(3*a-1 > X) break; // with b=d=1: n >= 4a-(a+1) = 3a-1
    for(long b=1;;b++){
      long s=a+b; if(4*a*b - s > X) break;
      for(long d=1;;d++){
        long P=4*a*b*d; if(P - s > X) break;
        for(uint64_t k=start[s];k<start[s]+cnt[s];k++){
          long e=divs[k]; long n=P-e; if(n<1||n>X) continue;
          long c=s/e;
          tot[n]++; if(c==1) c1[n]++;
          if(gcdl(gcdl(a,b),c)==1) prim[n]++;
          if((uint32_t)c>cmax[n]) cmax[n]=c;
          if((uint32_t)e<emin[n]) emin[n]=e;
        }
      }
    }
  }
  FILE*f=fopen(out,"wb");
  fwrite(&X,8,1,f);
  fwrite(tot,4,X+1,f);fwrite(c1,4,X+1,f);fwrite(prim,4,X+1,f);fwrite(cmax,4,X+1,f);fwrite(emin,4,X+1,f);
  fclose(f);
  return 0;
}
