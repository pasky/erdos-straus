/* O89 (POINTWISE_TYPEI4.md Prop 1.2): enumerate fibre certificates via (1.1):
     16 P X^2 - Q Y^2 = 1,  Y = 7^b,  v_7(Q) = a odd,  c' | P (7 not | c'),
     M := (P/c')(Q/7^a) = c_o delta^2 + 2^(L-4),  c_o = 7^a c',  delta odd > 0.
   For every solution prints: L c_o delta k_o(=X*7^b) a b c' P Q  F e  v2(F+9) v2(e+9)
   where F = A - 8 n delta, e = A + 8 n delta, A = 2 Q Y^2 + 1, n = c_o k_o.
   Complete for all solutions with P <= Pmax, X <= Xmax (X odd, 7 not | X).
   Usage: typei4_pqsearch Pmax Xmax */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned __int128 u128; typedef long long ll;
static void pr(u128 v){char b[60];int i=59;b[i]=0;if(!v){putchar('0');return;}while(v){b[--i]='0'+(int)(v%10);v/=10;}fputs(b+i,stdout);}
static u128 isq(u128 n){u128 x=(u128)sqrtl((long double)n);while(x*x>n)x--;while((x+1)*(x+1)<=n)x++;return x;}
static int v2(u128 x){int e=0;if(!x)return 99;while(!(x&1)){x>>=1;e++;}return e;}
int main(int argc,char**argv){
  ll Pmax=atoll(argv[1]),Xmax=atoll(argv[2]); long cnt=0;
  for(ll P=1;P<=Pmax;P++){ if(P%7==0||P%2==0)continue;
    for(ll X=1;X<=Xmax;X+=2){ if(X%7==0)continue;
      u128 T=(u128)16*P*X*X-1; int v=0; u128 Tq=T; while(Tq%7==0){Tq/=7;v++;}
      if(v%2==0)continue;               /* need a+2b = v with a odd */
      for(int b=0;2*b<v;b++){ int a=v-2*b; u128 Y2=1; for(int i=0;i<2*b;i++)Y2*=7;
        u128 Q=T/Y2; u128 p7a=1; for(int i=0;i<a;i++)p7a*=7; u128 Q1=Q/p7a;
        ll dv[4096];int nd=0; for(ll q=1;q*q<=P;q++) if(P%q==0){dv[nd++]=q; if(q*q!=P)dv[nd++]=P/q;}
        for(int di=0;di<nd;di++){ ll cp=dv[di];
          u128 co=(u128)cp*p7a; u128 M=(u128)(P/cp)*Q1;
          for(int j=1;j<126;j++){ u128 pj=(u128)1<<j; if(pj>=M)break;
            u128 r=M-pj; if(r%co)continue; u128 s=r/co; if(!(s&1))continue; u128 dl=isq(s); if(dl*dl!=s)continue;
            int L=j+4; u128 ko=(u128)X; for(int i=0;i<b;i++)ko*=7; u128 n=co*ko;
            u128 A=2*Q*Y2+1; u128 F=A-8*n*dl, e=A+8*n*dl;
            printf("%d ",L);pr(co);putchar(' ');pr(dl);putchar(' ');pr(ko);printf(" %d %d %lld %lld ",a,b,cp,P);pr(Q);putchar(' ');
            pr(F);putchar(' ');pr(e);printf(" %d %d\n",v2(F+9),v2(e+9)); cnt++;
          }}}}}
  fprintf(stderr,"solutions %ld\n",cnt); return 0;}
