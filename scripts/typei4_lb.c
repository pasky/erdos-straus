#include <math.h>
/* O89 (POINTWISE_TYPEI4.md Cor 3.2): complete enumeration of fibre certificates with level L and
   v_7(k) = b (all a, all heights), via Lemma 3.1:
     y = c' g delta < T 7^b (y odd), z = T 7^b - y, a odd with 7^a < T/2 (2y>T7^b) or 7^a < T^2 7^b/4,
     P1 = c' g^2 + 7^(a+b) (2y - T 7^b) >= 1, P1 | z, 7 !| P1,
     X = (1 + 7^(a+b) z / P1) / (4 c' g) odd integer, 7 !| X, 7 !| c'.
   Prints: L b a c' g delta P1 X F e  (F = 8c'Xg-1, e = 8c'Xh-1, h = g + 2*7^(a+b)*delta), verifying
   F*e == 1 + 2^(L+2) c' 7^(a+2b) X^2 in 128-bit arithmetic.
   Usage: typei4_lb L b */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
static void pr(i128 v){char b[60];int i=59;b[i]=0;if(v==0){putchar('0');return;}while(v){b[--i]='0'+(int)(v%10);v/=10;}fputs(b+i,stdout);}
int main(int argc,char**argv){
  int L=atoi(argv[1]),b=atoi(argv[2]); ll T=1LL<<(L-4); ll p7b=1; for(int i=0;i<b;i++)p7b*=7;
  ll Y=T*p7b; long cnt=0;
  int *spf=calloc(Y+1,sizeof(int)); for(ll i=2;i<=Y;i++) if(!spf[i]) for(ll j=i;j<=Y;j+=i) if(!spf[j]) spf[j]=(int)i;
  static ll dv[1<<16];
  for(ll y=1;y<Y;y+=2){ ll z=Y-y; i128 twoy=(i128)2*y-Y;
    int nd=1; dv[0]=1; { ll m=y; while(m>1){ int q=spf[m],e=0; while(m%q==0){m/=q;e++;} int n0=nd; ll pw=1;
        for(int k=1;k<=e;k++){ pw*=q; for(int i=0;i<n0;i++) dv[nd++]=dv[i]*pw; } } }
    for(int ic=0;ic<nd;ic++){ ll cp=dv[ic]; if(cp%7==0)continue; ll r=y/cp;
      for(int ig=0;ig<nd;ig++){ ll g=dv[ig]; if(r%g)continue; ll dl=r/g;
        i128 cg2=(i128)cp*g*g;
        i128 p=7*p7b; /* 7^(a+b), a=1 */
        for(int a=1;a<60;a+=2,p*=49){
          /* bound (iv) */
          i128 p7a=p/p7b;
          if(twoy>0){ if(2*p7a>=T)break; } else { if(4*p7a>=(i128)T*T*p7b)break; }
          i128 P1=cg2+p*twoy; if(P1<1)continue; if(z%P1)continue; if(P1%7==0)continue;
          i128 num=1+p*(z/P1); if(num%(4*(i128)cp*g))continue; i128 X=num/(4*(i128)cp*g);
          if(X%2==0||X%7==0)continue;
          i128 h=g+2*p*dl;
          /* R89 repair D6 (applied by reviewer): refuse to compute e, N if they could exceed 2^126 */
          { long double lx=log2l((long double)X), le=log2l(8.0L*cp)+lx+log2l((long double)h),
              ln=(L+2)+log2l((long double)cp)+log2l((long double)(p7a*p7b*p7b))+2*lx;
            if(le>125||ln>125){fprintf(stderr,"OVERFLOW RISK L=%d b=%d a=%d: re-verify with big ints\n",L,b,a);return 3;} }
          i128 F=8*cp*X*g-1, e=8*cp*X*h-1;
          i128 N=1+((i128)1<<(L+2))*cp*(p7a*p7b*p7b)*X*X;
          if(F*e!=N){fprintf(stderr,"IDENTITY FAIL\n");return 1;}
          printf("%d %d %d %lld %lld %lld ",L,b,a,cp,g,dl);pr(P1);putchar(' ');pr(X);putchar(' ');pr(F);putchar(' ');pr(e);putchar('\n');cnt++;
        }}}}
  fprintf(stderr,"L=%d b=%d solutions %ld\n",L,b,cnt); return 0;}
