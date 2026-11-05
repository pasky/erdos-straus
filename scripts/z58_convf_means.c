// z58 CONVF: mean counts of a=1 line (#(c,d): 4cd-1 | cp+1) and c=1 line (#(a,d): 4ad-1 | p+a) over primes p = 1 (24) in dyadic ranges
// sieve: a=1: n = B(4cd-1) - 4d ; c=1: n = B(4ad-1) - a   (all B>=1, n<=N)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
 unsigned short *A=calloc(N+1,2), *Cc=calloc(N+1,2);
 for(long c=1;4*c-1-4<=N;c++) for(long d=1;d<=N/4+1;d++){ long f=4*c*d-1; if(f-4*d>N) break; for(long B=1;;B++){ long n=B*f-4*d; if(n>N)break; if(n>0) A[n]++; } }
 for(long a=1;4*a-1-a<=N;a++) for(long d=1;;d++){ long f=4*a*d-1; if(f-a>N) break; for(long B=1;;B++){ long n=B*f-a; if(n>N)break; if(n>0) Cc[n]++; } }
 char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
 printf("range  #p  meanA  meanC  meanA/log2p  meanC/log2p  zerosA zerosC  minA minC\n");
 for(long lo=1000;lo<N;lo*=4){ long hi=lo*4; if(hi>N)hi=N; long np=0,sa=0,sc=0,za=0,zc=0,mA=1<<30,mC=1<<30; double L=0;
   for(long n=lo+((1-lo%24)+24)%24; n<=hi; n+=24){ /* n = 1 mod 24 */ if(comp[n]) continue; np++; sa+=A[n]; sc+=Cc[n]; if(!A[n])za++; if(!Cc[n])zc++; if(A[n]<mA)mA=A[n]; if(Cc[n]<mC)mC=Cc[n]; L+=log(n)*log(n);}
   if(np) printf("[%ld,%ld] %ld %.2f %.2f %.4f %.4f %ld %ld %ld %ld\n",lo,hi,np,(double)sa/np,(double)sc/np,sa/L,sc/L,za,zc,mA,mC); }
 return 0;}
