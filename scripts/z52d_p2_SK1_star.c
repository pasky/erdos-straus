// z52d pass2 SK1 (item Z0849/Z0181-type): (star) word census for n <= N.
// Word (u,B,C) with 4uBC - u - B = n, C>=1, u>=1, B>=1 (B = v, t = 4C).  R(n) = #words.
// interior word: u>=2 and B>=2 ; boundary word: u=1 or B=1.
// Output: for primes n=1 mod 4 <= N: n R(n) Rint(n) Cmin(n) ; plus summary.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10);
  uint32_t *R=calloc(N+1,4),*RI=calloc(N+1,4),*CM=calloc(N+1,4);
  for(u64 C=1;4*C<=N+2+4*C;C++){ // t=4C
    u64 t=4*C;
    for(u64 u=1;;u++){
      if(t*u<2) continue;
      if(t*u-1>N+u) break;
      u64 vmax=(N+u)/(t*u-1); if(vmax<1) break;
      for(u64 v=1;v<=vmax;v++){
        long long nn=(long long)(t*u*v)-(long long)u-(long long)v; if(nn<1) continue; if((u64)nn>N) break;
        R[nn]++; if(u>=2&&v>=2) RI[nn]++;
        if(!CM[nn]||C<CM[nn]) CM[nn]=C;
      }
    }
    if(t>N+2) break;
  }
  // primes via sieve
  char *comp=calloc(N+1,1); comp[0]=comp[1]=1;
  for(u64 i=2;i*i<=N;i++) if(!comp[i]) for(u64 j=i*i;j<=N;j+=i) comp[j]=1;
  u64 np=0,nzero=0,nbonly=0,nint=0; FILE*f=fopen(argv[2],"w");
  for(u64 p=5;p<=N;p+=4){
    if(comp[p]) continue; np++;
    if(R[p]==0){ nzero++; fprintf(f,"R0 %llu\n",p); }
    else if(RI[p]==0){ nbonly++; fprintf(f,"BONLY %llu R=%u Cmin=%u\n",p,R[p],CM[p]); }
    else nint++;
  }
  printf("N=%llu primes1mod4=%llu R-zeros=%llu boundary-only(R>0,Rint=0)=%llu with-interior=%llu\n",N,np,nzero,nbonly,nint);
  fclose(f);
  return 0;
}
