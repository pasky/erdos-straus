/* R131 from-scratch brute force: for n<=N print per-(n,family) solutions (n,a,b,c,d) directly from equations.
   fam 0: T1+  4abcd = n(a+b)+c ; fam 1: T1-  4abcd + c = n(a+b)
   fam 2: T2+  4abcd = a+b+nc   ; fam 3: T2-  4abcd + a + b = nc        (a<=b, all >=1) */
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
 for(long n=1;n<=N;n++){
  /* T1+: b(4acd-n) = na+c ; 4acd <= 2n+c, c <= n */
  for(long c=1;c<=n;c++) for(long a=1;4*a*c<=2*n+c;a++) for(long d=1;4*a*c*d<=2*n+c;d++){
    long f=4*a*c*d-n; if(f<=0) continue;
    if((n*a+c)%f==0){long b=(n*a+c)/f; if(b>=a) printf("0 %ld %ld %ld %ld %ld\n",n,a,b,c,d);}
    long g=n*a-c; if(g>0 && g%f==0){long b=g/f; if(b>=a) printf("1 %ld %ld %ld %ld %ld\n",n,a,b,c,d);} }
  /* T2+: c(4abd-n)=a+b ; b(4ad-1) <= n+a */
  for(long a=1;a*(4*a-1)<=n+a;a++) for(long d=1;a*(4*a*d-1)<=n+a;d++) for(long b=a;b*(4*a*d-1)<=n+a;b++){
    long e=4*a*b*d-n; if(e>0 && (a+b)%e==0) printf("2 %ld %ld %ld %ld %ld\n",n,a,b,(a+b)/e,d);}
  /* T2-: c(n-4abd)=a+b, 4abd<n */
  for(long a=1;4*a*a<n;a++) for(long d=1;4*a*a*d<n;d++) for(long b=a;4*a*b*d<n;b++){
    long e=n-4*a*b*d; if((a+b)%e==0) printf("3 %ld %ld %ld %ld %ld\n",n,a,b,(a+b)/e,d);}
 } return 0;}
