#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
int main(){ char line[64]; double tot=0,tot2=0; int np=0;
  while(fgets(line,64,stdin)){ u64 p=strtoull(line,0,10); u64 U=(u64)floor(pow((double)p,0.25)); while((U+1)*(U+1)*(U+1)*(U+1)<=p) U++; while(U*U*U*U>p) U--;
    u64 k0=p/(4*U*U)>2?p/(4*U*U)-2:1, k1=p/(U*U)+2; long e1=0,e2=0;
    for(u64 k=k0;k<=k1;k++){ u64 s=(k-p%k)%k; if(s<=2*U||s>4*U) continue; e1++;
      u64 m=(p+s)/k; long long D=(long long)(s*s)-4*(long long)m; if(D<=0) continue; long long w=(long long)sqrtl((long double)D); while(w*w>D) w--; while((w+1)*(w+1)<=D) w++;
      if(w*w==D && (s-w)%2==0 && (s-w)/2>U && (s+w)/2<=2*U) e2++; }
    tot+=(double)e1/U; tot2+=e2; np++; if(getenv("PER")) printf("%llu %ld\n",p,e2); }
  printf("primes %d mean E1-levels/U %.4f mean 2-cycles %.4f\n",np,tot/np,tot2/np); }
