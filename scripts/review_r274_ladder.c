/* R274 from-scratch Type II ladder count (independent of z32_ladder.c).
   f_m(p) = #{(a,b,c,d) >= 1 ordered in (a,b), gcd(a,c)=1 : m*a*b*c*d = a + b + c*p}.
   Enumeration: k := m*a*b*d - p >= 1 divides a+b (c = (a+b)/k), so p = m*a*b*d - k.
   Loop (a,b) ordered, k | a+b via spf factorisation, d >= 1.
   Usage: review_r274_ladder m X out.bin   (uint32 counts, index p)  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static long gcd(long x,long y){while(y){long t=x%y;x=y;y=t;}return x;}
int main(int argc,char**argv){
  long m=atol(argv[1]), X=atol(argv[2]);
  long S = X/ (m>1? (m-1):1) + 10;     /* bound for a+b: m*a*b - (a+b) <= X  => a+b <= X+1 roughly; use X+2 */
  S = X + 3;
  int *spf = calloc(S+1,sizeof(int));
  for(long i=2;i<=S;i++) if(!spf[i]) for(long j=i;j<=S;j+=i) if(!spf[j]) spf[j]=i;
  uint32_t *cnt = calloc(X+1,4);
  long divs[4096];
  for(long a=1; m*a - (a+1) <= X; a++){
    for(long b=1; m*a*b - (a+b) <= X; b++){
      long s=a+b, t=s; int nd=1; divs[0]=1;
      while(t>1){ long q=spf[t]; int e=0; while(t%q==0){t/=q;e++;}
        int cur=nd; long pw=1; for(int j=1;j<=e;j++){pw*=q; for(int i=0;i<cur;i++) divs[nd++]=divs[i]*pw;} }
      for(int i=0;i<nd;i++){ long k=divs[i], c=s/k; if(gcd(a,c)!=1) continue;
        for(long d=1;;d++){ long p=m*a*b*d-k; if(p>X) break; if(p>=2) cnt[p]++; } }
    }
  }
  FILE*o=fopen(argv[3],"wb"); fwrite(cnt,4,X+1,o); fclose(o); return 0;
}
