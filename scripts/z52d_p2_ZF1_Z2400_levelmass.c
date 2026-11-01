/* Z2400: how much of the averaged (★) mass sum_p R(p) over primes p in [X,X+W) comes from witness moduli m=4uC-1 <= X^theta
   (the "level" an ET-type average argument must handle), and the same for odd n; plus how many primes have
   ALL their (★) solutions at level > theta (pointwise: level needed by a single p). Usage: levelmass X W */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
#define NB 20
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), W=strtoull(argv[2],0,10), N1=X+W; double L=log((double)X);
  unsigned short (*H)[NB]=calloc(W,sizeof(*H));  /* per n: hits by level bin, bin = floor(20*log m/log X) */
  for(u64 u=1; 4*u-1<=N1+u; u++) for(u64 C=1;;C++){ u64 m=4*u*C-1; if(m>N1+u) break;
      int b=(int)(NB*log((double)m)/L); if(b>=NB) b=NB-1;
      u64 r=(m-(u%m))%m; u64 lo=X; if(lo+u<m) lo=m-u; u64 n=lo+((r+m-lo%m)%m);
      for(;n<N1;n+=m) H[n-X][b]++; }
  char *comp=calloc(W,1); u64 s=(u64)sqrtl((long double)N1)+1;
  for(u64 i=2;i<=s;i++){ int ip=1; for(u64 j=2;j*j<=i;j++) if(i%j==0){ip=0;break;} if(!ip) continue;
     u64 st=(X+i-1)/i*i; if(st<i*i) st=i*i; for(u64 j=st;j<N1;j+=i) comp[j-X]=1; }
  double tot[2]={0},cum[2][NB]={{0}}; long np=0, minlev[NB+1]={0};
  for(u64 i=0;i<W;i++){ u64 n=X+i; if(!(n&1)) continue; int isp=(!comp[i] && (n&3)==1);
     for(int b=0;b<NB;b++){ cum[0][b]+=H[i][b]; if(isp) cum[1][b]+=H[i][b]; }
     if(isp){ np++; int f=NB; for(int b=0;b<NB;b++) if(H[i][b]){f=b;break;} minlev[f]++; } }
  for(int k=0;k<2;k++){ double t=0; for(int b=0;b<NB;b++) t+=cum[k][b]; tot[k]=t; }
  printf("X=%llu W=%llu primes(1 mod 4)=%ld\n theta  massfrac(odd n)  massfrac(primes)  theta^2  frac primes whose least witness level > theta\n",X,W,np);
  double c0=0,c1=0; long cm=0;
  for(int b=0;b<NB;b++){ c0+=cum[0][b]; c1+=cum[1][b]; cm+=minlev[b]; double th=(b+1.0)/NB;
     printf(" %.2f   %.4f           %.4f            %.4f   %.4f\n",th,c0/tot[0],c1/tot[1],th*th,1.0-(double)cm/np); }
  printf(" primes with no witness at all: %ld\n",minlev[NB]);
  return 0;}
