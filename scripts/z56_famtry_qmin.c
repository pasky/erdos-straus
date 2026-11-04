// q_min(n): least pair-form modulus 4uB over hits (u,B,C) of 4uBC-u-B=n (n lies in class -(u+B) mod 4uB).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int argc,char**argv){
  uint64_t X = argc>1?strtoull(argv[1],0,10):10000000ULL;
  uint8_t *comp=calloc(X+1,1); for(uint64_t i=2;i*i<=X;i++) if(!comp[i]) for(uint64_t j=i*i;j<=X;j+=i) comp[j]=1;
  uint64_t *qm=malloc((X+1)*8); for(uint64_t i=0;i<=X;i++) qm[i]=0;
  for(uint64_t u=1;3*u<=X+1;u++) for(uint64_t C=1;;C++){ uint64_t d=4*u*C-1; if(d>X+u) break;
    for(uint64_t n=d-u, B=1;n<=X;n+=d,B++){ uint64_t q=4*u*B; if(!qm[n]||q<qm[n]) qm[n]=q; } }
  printf("# decade  #p≡1(8)  #R=0  max q_min (over R>0)  argmax  mean log q_min/log log p   frac q_min<=1e3,1e4,1e5,1e6\n");
  for(uint64_t lo=1000;lo<X;lo*=10){ uint64_t hi=lo*10<X?lo*10:X; uint64_t mq=0,aq=0,c=0,z=0,f[4]={0}; double s=0;
    for(uint64_t p=lo+1;p<=hi;p++){ if(p%8!=1||comp[p]) continue; c++; if(!qm[p]){z++;continue;} if(qm[p]>mq){mq=qm[p];aq=p;}
      s+=log((double)qm[p])/log(log((double)p)); uint64_t T=1000; for(int i=0;i<4;i++,T*=10) if(qm[p]<=T) f[i]++; }
    printf("%llu-%llu %llu %llu %llu %llu %.3f  %.4f %.4f %.4f %.4f\n",(unsigned long long)lo,(unsigned long long)hi,(unsigned long long)c,(unsigned long long)z,(unsigned long long)mq,(unsigned long long)aq,s/(c-z),(double)f[0]/c,(double)f[1]/c,(double)f[2]/c,(double)f[3]/c); }
  return 0; }
