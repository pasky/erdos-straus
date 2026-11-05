// list all (a,b,c,d), a<=b, with 4abcd = a+b+nc: for each (a,d), b in [ceil((n+1)/4ad), floor((n+a)/(4ad-1))], need (4abd-n) | (a+b)
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ for(int i=1;i<argc;i++){ long n=atol(argv[i]); int cnt=0; printf("n=%ld:",n);
  for(long a=1;4*a*a<=n+2*a;a++) for(long d=1;4*a*a*d<=n+2*a;d++){ long lo=(n+1+4*a*d-1)/(4*a*d), hi=(n+a)/(4*a*d-1); if(lo<a)lo=a;
    for(long b=lo;b<=hi;b++){ long m=4*a*b*d-n; if(m>0 && (a+b)%m==0){ printf(" (%ld,%ld,%ld,%ld)",a,b,(a+b)/m,d); cnt++; } } }
  printf("  [%d]\n",cnt);} return 0;}
