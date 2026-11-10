// z69 TWIST Remark C census: certificate words C_n = words (x,y,z), xyz - x - z = n, with
//   (i) 4|y, or (ii) 4|x or 4|z, or (iii) y == 3 (4) and (x == 3 (4) or z == 3 (4)).
// For n == 1 (mod 4), n <= N: lists n with C_n empty, tagged P (prime) / SQ (square) / C (other composite);
// also counts n with a U7 word (8 | xy or 8 | zy) for comparison.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); uint8_t *C=calloc(N+1,1),*U=calloc(N+1,1);
  for(long x=1;x<=N+2;x++) for(long y=1;;y++){
    long f=x*y-1; if(f<=0) continue; long zmax=(N+x)/f; if(zmax<1) break;
    long zmin=(x+1+f-1)/f; if(zmin<1) zmin=1;
    for(long z=zmin;z<=zmax;z++){ long n=f*z-x; if(n<1||n>N||(n&3)!=1) continue;
      if((y&3)==0||(x&3)==0||(z&3)==0||((y&3)==3&&((x&3)==3||(z&3)==3))) C[n]=1;
      if((x*y)%8==0||(z*y)%8==0) U[n]=1; }
  }
  char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  long zP=0,zS=0,zC=0,nS=0,uP=0,uC=0;
  printf("n == 1 (4), n <= %ld with C_n empty (non-squares listed):",N);
  for(long n=5;n<=N;n+=4){ long s=(long)(__builtin_sqrt((double)n)+0.5); int sq=(s*s==n);
    if(sq) nS++;
    if(!C[n]){ if(sq) zS++; else if(!comp[n]){ zP++; printf(" %ldP",n);} else { zC++; printf(" %ldC",n);} }
    if(!U[n]&&!sq&&(n&7)==1){ if(!comp[n]) uP++; else uC++; } }
  printf("\nC-empty: primes %ld, non-square composites %ld, squares %ld of %ld ; U7-empty among n == 1 (8) non-squares: primes %ld, composites %ld\n",zP,zC,zS,nS,uP,uC);
  return 0;
}
