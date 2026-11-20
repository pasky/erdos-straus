/* Count the high-(c^2 d) large-shift Q cube rows exactly. Complement per dyadic
 rectangle capped by z78_qcap.py without enumerating its divisors. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;
int main(int argc,char**argv){assert(argc==3);int lo=atoi(argv[1]),hi=atoi(argv[2]);assert(lo>=17&&hi<=2400);
 for(U r=lo;r<=hi;r++){int ok=1;for(U p=2;p*p<=r;p++)if(r%p==0)ok=0;if(!ok)continue;
 U F=r*r*r,E=r*r,T=E,max=F+2;U lim=((Z)(F+max)*(F+max))/(4*(E*T-1)); // here E*T fits uint64
 U ct=0;for(U C=1;C*C<=lim;C*=2)for(U D=1;C*C*D<=lim;D*=2){
 Z init=(Z)(F+max)*(F+max)/(4*(Z)C*C*D);U hiF=(init+1)/E;if(hiF>max)hiF=max;
 if(hiF<T||1+(hiF-T)/(4*C*D)>128)continue;
 for(U c=C;c<2*C&&c*c*D<=lim;c++)if(c%r)for(U d=D;d<2*D&&c*c*d<=lim;d++)if(d%r){
 U u=4*c*d;Z V=(Z)F*F+u*c;
 for(U f=T+(u-(F+T)%u)%u;f<=hiF;f+=u){if(V%f)continue;U a=(F+f)/u;
 Z num=(Z)4*a*a*d+1;if(num%f||num/f<E)continue;Z e=num/f; if(e%r==0||c*e<2*a)continue;ct+=2;}
 }}printf("%lu %lu\n",r,ct);fflush(stdout);}}
