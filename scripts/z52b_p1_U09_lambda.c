// z52b pass1 U09 (Z2061): lambda(p) = min over non-residues A mod p of HJ(p/A), HJ = 1 + sum_{i odd} a_i,
// a_i the regular continued-fraction partial quotients of p/A = [a_0; a_1, a_2, ...] (repo convention, BRAINSTORM/z31_zaremba_thin_orbits.md).
// Output: p lambda(p)  for primes p ≤ X.  Build: gcc -O2 -o z52b_p1_U09_lambda scripts/z52b_p1_U09_lambda.c
#include <stdio.h>
#include <stdlib.h>
static int legendre(long a, long p){ // Euler criterion via modpow
  long e=(p-1)/2, r=1, b=a%p; if(b<0) b+=p;
  while(e){ if(e&1) r=(r*b)%p; b=(b*b)%p; e>>=1; }
  return r==1 ? 1 : (r==p-1 ? -1 : 0);
}
static long hj_len(long num, long den, long cutoff){ // returns 1 + sum odd-index quotients, early exit above cutoff
  long i=0, sum=0;
  while(den){
    long q=num/den, r=num%den;
    if(i%2==1){ sum+=q; if(1+sum>cutoff) return 1+sum; }
    num=den; den=r; i++;
  }
  return 1+sum;
}
int main(int argc,char**argv){
  long X = argc>1? atol(argv[1]) : 20000;
  char *comp=calloc(X+1,1);
  for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
  for(long p=3;p<=X;p++){
    if(comp[p]) continue;
    long best=1000000;
    for(long A=1;A<p;A++){
      if(legendre(A,p)!=-1) continue;
      long h=hj_len(p,A,best);
      if(h<best){ best=h; if(best<=1) break; }
    }
    printf("%ld %ld\n",p,best);
  }
  return 0;
}
