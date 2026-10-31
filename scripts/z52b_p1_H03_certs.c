// Enumerate (★) certificates (u,B,C) with 4uBC - u - B = p  (B >= 1, u >= 1, C >= 1).
// usage: ./certs p [Cmax]   -> prints "u B C" lines;  Cmax default: all
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){
  unsigned long long p=strtoull(argv[1],0,10);
  unsigned long long Cmax = argc>2? strtoull(argv[2],0,10) : (p+2)/4+1;
  for(unsigned long long C=1;C<=Cmax;C++){
    // m=4uC-1 must divide p+u, m <= p+u  => u(4C-1) <= p+1
    for(unsigned long long u=1; u*(4*C-1)<=p+1; u++){
      unsigned long long m=4*u*C-1;
      if((p+u)%m==0){ unsigned long long B=(p+u)/m; printf("%llu %llu %llu\n",u,B,C);}
    }
  }
  return 0;
}
