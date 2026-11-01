/* Z2411: variance-to-mean of R(n) = #{(u,B,C): 4uBC-u-B=n} over a window [X, X+W),
   for (a) odd n, (b) primes p = 1 mod 4; raw and after removing class means mod Q (Q=840, 9240).
   R(n) via trial form: R(n) = sum_{u,C>=1} 1[(4uC-1) | n+u, n+u >= 4uC-1].
   Usage: z2411 X W */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), W=strtoull(argv[2],0,10), N1=X+W;
  unsigned short *R=calloc(W,2);
  for(u64 u=1; 4*u-1<=N1+u; u++){
    for(u64 C=1;;C++){ u64 m=4*u*C-1; if(m>N1+u) break;
      /* n = -u mod m, n in [X,N1), n+u>=m */
      u64 r=(m - (u%m))%m; /* n ≡ r mod m */
      u64 lo = X; if(lo+u<m) lo=m-u; 
      u64 n = lo + ((r + m - lo%m)%m);
      for(; n<N1; n+=m) R[n-X]++;
    }
  }
  /* prime sieve on window */
  char *comp=calloc(W,1); u64 s=(u64)sqrtl((long double)N1)+1;
  char *sp=calloc(s+1,1);
  for(u64 i=2;i<=s;i++) if(!sp[i]){ for(u64 j=i*i;j<=s;j+=i) sp[j]=1;
     u64 st = (X+i-1)/i*i; if(st<i*i) st=i*i; for(u64 j=st;j<N1;j+=i) comp[j-X]=1; }
  int Qs[3]={1,840,9240};
  for(int set=0;set<3;set++){ /* 0: odd n, 1: odd nonsquare n, 2: primes 1 mod 4 */
    for(int qi=0;qi<3;qi++){ int Q=Qs[qi];
      double *S=calloc(Q,8),*S2=calloc(Q,8); long *K=calloc(Q,sizeof(long));
      for(u64 i=0;i<W;i++){ u64 n=X+i; if(!(n&1)) continue;
        if(set==1){ u64 r=(u64)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; if(r*r==n) continue; }
        if(set==2){ if(comp[i]||(n&3)!=1) continue; }
        int c=n%Q; S[c]+=R[i]; S2[c]+=(double)R[i]*R[i]; K[c]++; }
      double tot=0,tot2=0,within=0; long kk=0;
      for(int c=0;c<Q;c++){ if(!K[c]) continue; tot+=S[c]; tot2+=S2[c]; kk+=K[c]; within += S2[c]-S[c]*S[c]/K[c]; }
      double mean=tot/kk, var=tot2/kk-mean*mean, wv=within/kk; double L=log((double)X);
      printf("X=%llu W=%llu set=%d Q=%d count=%ld mean=%.3f mean/L2=%.4f var=%.2f var/mean=%.3f resid_var(after class means)=%.2f ratio=%.3f\n",
        X,W,set,Q,kk,mean,mean/(L*L),var,var/mean,wv,wv/mean);
      free(S);free(S2);free(K);}
  }
  return 0;}
