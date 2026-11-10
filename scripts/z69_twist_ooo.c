// z69 TWIST (I5 follow-up): all-odd words. For n == 1 (mod 4): every word (x,y,z) with x,y,z odd has y == 3 (mod 4);
// A = {x == z == 1 (4)} (contains the trivial word (1,n+2,1)), B = {x == 3 or z == 3 (4)} = Type I solutions with a = 1.
// Prints, for primes p == 1 (4), p <= N: parity statistics of |A|, |B| and the lists of primes with B empty,
// and with B empty and no (★) word (4 | y).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); uint16_t *A=calloc(N+1,2),*B=calloc(N+1,2),*S=calloc(N+1,2); uint8_t *bad=calloc(N+1,1);
  for(long x=1;x<=N+2;x++) for(long y=1;;y++){
    long f=x*y-1; if(f<=0) continue; long zmax=(N+x)/f; if(zmax<1) break;
    long zmin=(x+1+f-1)/f; if(zmin<1) zmin=1;
    for(long z=zmin;z<=zmax;z++){ long n=f*z-x; if(n<1||n>N||(n&3)!=1) continue;
      if(y%4==0){ if(S[n]<65535) S[n]++; }
      if((x&1)&&(y&1)&&(z&1)){ if((y&3)!=3) bad[n]=1;
        if((x&3)==3||(z&3)==3){ if(B[n]<65535) B[n]++; } else { if(A[n]<65535) A[n]++; } }
    }
  }
  char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  long np=0,Aodd=0,Beven=0,B0=0,both0=0,nbad=0;
  printf("primes p==1(4) with B empty:");
  for(long n=5;n<=N;n+=4){ if(comp[n]) continue; np++; Aodd+=A[n]&1; Beven+=!(B[n]&1); nbad+=bad[n];
    if(B[n]==0){ B0++; printf(" %ld",n); } }
  printf("\nprimes p==1(4) with B empty and no (★) word:");
  for(long n=5;n<=N;n+=4){ if(comp[n]) continue; if(B[n]==0&&S[n]==0){ both0++; printf(" %ld",n);} }
  printf("\nN=%ld primes p==1(4): %ld ; |A| odd: %ld ; |B| even: %ld ; words with y != 3 (4): %ld ; B empty: %ld ; B and (★) empty: %ld\n",N,np,Aodd,Beven,nbad,B0,both0);
  long sq=0,sqB=0; for(long m=3;m*m<=N;m+=2){ sq++; if(B[m*m]) sqB++; }
  printf("odd squares m^2<=N: %ld, with B nonempty: %ld\n",sq,sqB);
  return 0;
}
