/* O89 (POINTWISE_TYPEI4.md Cor 1.4): complete enumeration of fibre certificates at fixed level L
   and fixed s = a+2b (a odd), via (1.2):
       c' g h - P1 = K = 2^(L-4) 7^s,  g = 4 P1 X - D, h = 4 P1 X + D, D = 7^(a+b) delta.
   Bounds: (4c'g-1) P1 < K, h (8c'g-1) <= 8K + g.  Prints every solution:
       L s a b c' P1 X delta g h
   Usage: typei4_level L s      (K must fit in 62 bits) */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
int main(int argc,char**argv){
  int L=atoi(argv[1]),s=atoi(argv[2]); ll K=1LL<<(L-4); for(int i=0;i<s;i++)K*=7;
  long cnt=0; ll p7[40]; p7[0]=1; for(int i=1;i<40;i++)p7[i]=p7[i-1]*7;
  for(ll cp=1;4*cp-1<K;cp+=2){ if(cp%7==0)continue;
    for(ll g=1;(4*cp*g-1)<K;g+=2){
      i128 cg=(i128)cp*g;
      ll hmin=(ll)(K/cg)+1; ll hmax=(ll)(((i128)8*K+g)/(8*cg-1));
      if(hmin%2==0)hmin++;
      for(ll h=hmin;h<=hmax;h+=2){
        i128 P1=cg*h-K; if(P1<=0)continue; if(P1%7==0)continue;
        i128 sum=(i128)g+h; if(sum%(8*P1))continue; ll X=(ll)(sum/(8*P1)); if(X%2==0||X%7==0)continue;
        if(h<=g)continue; ll D=(h-g)/2;
        for(int b=0;2*b<s;b++){int a=s-2*b; ll q=p7[a+b]; if(D%q)continue; ll dl=D/q; if(dl%2==0)continue;
          printf("%d %d %d %d %lld %lld %lld %lld %lld %lld\n",L,s,a,b,cp,(ll)P1,X,dl,g,h); cnt++; }
      }}}
  fprintf(stderr,"L=%d s=%d K=%lld solutions %ld\n",L,s,K,cnt); return 0;}
