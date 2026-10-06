/* O72 (POINTWISE_TYPEI3.md): dump near misses at the sign point (r; -1 at r; 1 elsewhere).
   Near miss = (c,k,F): v_r(c) odd, F | N=1+4ck^2, F = -1 mod (odd r-free part of ck), F = 1 mod r^v.
   Prints every near miss with t=v_2(4ck)>=4 and -F = 1 (mod 8):
   c k alpha gamma t F e d   where d = v_2(F + w) (capped at 64), w given on the command line.
   Usage: typei3_nmdump r w X */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll; typedef __int128 i128; typedef unsigned __int128 u128;
static ll inv(ll a, ll m){ll g=m,x=0,x1=1,b=((a%m)+m)%m;while(b){ll q=g/b,t=g-q*b;g=b;b=t;t=x-q*x1;x=x1;x1=t;}x%=m;if(x<0)x+=m;return x;}
static u128 isqrt128(u128 n){u128 x=(u128)sqrtl((long double)n);while(x*x>n)x--;while((x+1)*(x+1)<=n)x++;return x;}
static void pr(u128 v){char b[50];int i=49;b[i]=0;if(!v){putchar('0');return;}while(v){b[--i]='0'+(int)(v%10);v/=10;}fputs(b+i,stdout);}
int main(int argc,char**argv){
  ll r=atoll(argv[1]),w=atoll(argv[2]),X=atoll(argv[3]);
  for(ll c=r;c<=X;c+=r){
    ll cc=c;int a=0;while(cc%r==0){cc/=r;a++;} if(a%2==0)continue;
    int al=0; {ll q=c;while(q%2==0){q/=2;al++;}}
    for(ll k=1;k<=X/c;k++){
      ll P=c*k,h=4*P; ll o=h;int t=0;while(o%2==0){o/=2;t++;}
      int ga=t-2-al;
      ll rv=1,o2=o;while(o2%r==0){o2/=r;rv*=r;}
      ll xo; if(o2==1)xo=1%o; else{ll tt=(ll)(((i128)((o2-1-1%o2+o2)%o2))*inv(rv%o2,o2)%o2);xo=(ll)((1+(i128)rv*tt)%o);}
      u128 N=(u128)1+(u128)4*c*(u128)k*k; u128 s=isqrt128(N);
      for(u128 D=xo;D<=s;D+=o){ if(D==0)continue; if(N%D)continue;
        u128 Fs[2]={D,N/D};
        for(int i=0;i<(Fs[0]==Fs[1]?1:2);i++){u128 F=Fs[i];
          if(t<4)continue; if(((F+1)%8)!=0)continue; /* -F = 1 mod 8 */
          i128 z=(i128)F+(i128)w; int d=0; if(z==0)d=64; else {while(z%2==0&&d<64){z/=2;d++;}}
          printf("%lld %lld %d %d %d ",c,k,al,ga,t);pr(F);putchar(' ');pr(N/F);printf(" %d\n",d);
        }}
    }}
  return 0;}
