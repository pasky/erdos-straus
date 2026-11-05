// z58 TRYF2: full R(p) for a list of p (one per line, '#' comments) via the symmetric region u <= B
// (4u^2 C <= p + 2u); R = 2 * #{(u,C) in region : (4uC-1) | p+u} (u = B is impossible for odd p).
#include <stdio.h>
#include <stdlib.h>
int main(){ char line[256]; while(fgets(line,sizeof line,stdin)){ if(line[0]=='#') continue; long p=atol(line); if(p<=0) continue;
  long cnt=0; for(long u=1; 4*u*u<=p+2*u; u++){ long Cmax=(p+2*u)/(4*u*u); long m=p+u; for(long C=1;C<=Cmax;C++){ if(m%(4*u*C-1)==0) cnt++; } }
  printf("%ld R=%ld\n",p,2*cnt); fflush(stdout);} return 0;}
