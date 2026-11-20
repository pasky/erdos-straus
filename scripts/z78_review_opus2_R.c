// R(n) = #{(a,b,d)>=1 : 4abd - a - b = n} = #{(a,d): (4ad-1) | (n+a)}, all n <= X.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  long X=atol(argv[1]);
  unsigned short *R=calloc(X+1,sizeof(unsigned short));
  for(long a=1;3*a<=X+a;a++) for(long d=1;;d++){
    long m=4*a*d-1; if(m-a> X) break;      // b=1 gives n=m-a
    for(long b=1;;b++){ long n=b*m-a; if(n>X) break; if(n>=1) R[n]++; }
  }
  // brute check per-n formula on a few n
  long bad=0;
  for(long n=2;n<=3000 && n<=X;n++){ long c=0;
    for(long a=1;a<=n;a++) for(long d=1;4*a*d-1<=n+a;d++) if((n+a)%(4*a*d-1)==0) c++;
    if(c!=R[n]) bad++; }
  printf("brute-check mismatches n<=3000: %ld\n",bad);
  double e1=20.0/63, best=0; long bn=0, mx=0, mxn=0;
  for(long n=2;n<=X;n++){ if(R[n]>mx){mx=R[n];mxn=n;}
    double v=R[n]/pow(n,e1); if(n>1000 && v>best){best=v;bn=n;} }
  printf("X=%ld max R=%ld at n=%ld (n^(20/63)=%.1f, n^(1/4)=%.1f); max R/n^(20/63) (n>1000)=%.3f at %ld\n",
         X,mx,mxn,pow(mxn,e1),pow(mxn,0.25),best,bn);
  for(long k=3;k<=7;k++){ long lo=(long)pow(10,k-1), hi=(long)pow(10,k); if(hi>X) break; long m=0,mn=0;
    for(long n=lo;n<=hi;n++) if(R[n]>m){m=R[n];mn=n;}
    printf("decade [1e%ld,1e%ld]: max R=%ld at n=%ld  log(maxR)/log(n)=%.4f\n",k-1,k,m,mn,log(m)/log(mn)); }
  return 0;
}
