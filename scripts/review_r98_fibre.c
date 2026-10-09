/* R98 from-scratch complete fibre-certificate engine (r=7, sign fibre w≡9 mod 16).
   Derivation (re-done by R98): with T=2^{L-4}, u=7^b, y=c'gδ, z=Tu-y, every fibre
   certificate of level L, v_7(k)=b (oriented δ>0) satisfies
     P_1 = c'g^2 + 7^{a+b}(2y-Tu) >= 1,  P_1 | z,  X=(1+7^{a+b} z/P_1)/(4c'g) odd integer, 7∤X,
     and 7^a < T/2 (2y>Tu) or 7^a < T^2 u/4 (2y<Tu).
   Every hit is verified DIRECTLY from the definition (F|1+4ck^2 with c=2^L*7^a c' (alpha=L,gamma=0
   split, the congruences don't depend on split except t), F≡-1 mod c'X, F≡1 mod 7^{a+b}, F≡7 mod 16).
   Output: per hit L b a c' g delta P1 X F e v2(F+9) v2(e+9).
   usage: review_r98_fibre L b */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
typedef __int128 i128;
static uint32_t *spf;
static int v2(u128 x){int k=0; while(x && !(x&1)){x>>=1;k++;} return k;}
static void pr(u128 x){char b[50];int i=49;b[i]=0;if(!x){printf("0");return;}while(x){b[--i]='0'+(int)(x%10);x/=10;}printf("%s",b+i);}
int main(int argc,char**argv){
  int L=atoi(argv[1]), b=atoi(argv[2]);
  uint64_t T=1ULL<<(L-4), u=1; for(int i=0;i<b;i++) u*=7;
  uint64_t Y=T*u; /* y < Y */
  spf=calloc(Y+1,sizeof(uint32_t));
  for(uint64_t i=2;i<=Y;i++) if(!spf[i]) for(uint64_t j=i;j<=Y;j+=i) if(!spf[j]) spf[j]=(uint32_t)i;
  /* max a */
  long double capA=(long double)T/2, capB=(long double)T*T*u/4;
  long hits=0;
  uint64_t divs[4096]; 
  for(uint64_t y=1;y<Y;y+=2){
    /* divisors of y */
    int nd=1; divs[0]=1; uint64_t m=y;
    while(m>1){uint32_t p=spf[m]; int e=0; while(m%p==0){m/=p;e++;}
      int cur=nd; uint64_t pk=1; for(int k=1;k<=e;k++){pk*=p; for(int i=0;i<cur;i++) divs[nd++]=divs[i]*pk;}}
    int caseA = (2*y>Y);
    long double cap = caseA?capA:capB;
    for(int i=0;i<nd;i++){ uint64_t cp=divs[i]; if(cp%7==0) continue;
      uint64_t rest=y/cp;
      for(int j=0;j<nd;j++){ uint64_t g=divs[j]; if(rest%g) continue; uint64_t delta=rest/g;
        u128 p7a=7; int a=1;
        for(;(long double)p7a<cap; a+=2, p7a*=49){
          u128 p7ab=p7a; for(int i2=0;i2<b;i2++) p7ab*=7;
          i128 P1=(i128)cp*g*g + (i128)p7ab*((i128)2*y-(i128)Y);
          if(P1<1) continue;
          uint64_t z=Y-y;
          if((i128)z % P1) continue;
          if(P1%7==0) continue;
          u128 num=1+p7ab*(u128)(z/(uint64_t)P1);
          u128 den=(u128)4*cp*g;
          if(num%den) continue;
          u128 X=num/den; if(!(X&1) || X%7==0) continue;
          /* build certificate and verify from definition */
          u128 D=p7ab*delta, h=g+2*D;
          u128 F=8*(u128)cp*X*g-1, e=8*(u128)cp*X*h-1;
          u128 N=1; { u128 t=(u128)1<<(L+2); t*=cp; t*=p7ab; for(int i2=0;i2<b;i2++) t*=7; t*=X*X; N+=t; }
          int ok = (F*e==N) && (F%(cp*X)==cp*X-1 || cp*X==1) && (F%p7ab==1) && (F%16==7) && (e%16==7);
          hits++;
          printf("%d %d %d %llu %llu %llu ",L,b,a,(unsigned long long)cp,(unsigned long long)g,(unsigned long long)delta);
          pr((u128)P1);printf(" ");pr(X);printf(" ");pr(F);printf(" ");pr(e);
          printf(" %d %d %s\n",v2(F+9),v2(e+9),ok?"OK":"FAIL");
        }
      }
    }
  }
  fprintf(stderr,"L=%d b=%d hits=%ld\n",L,b,hits);
  return 0;
}
