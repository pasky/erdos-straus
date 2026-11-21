/* In the both-large Q region sieve the f interval itself, for each w=c²d.
   The quadratic inequality gives a tighter ceiling than (2F+2)^2:
   4w(ef-1)=(F+f)^2, f<=F+2. If f>=t then f<=(F+h)^2/(4wE)+1/E
   for any valid h. Iterate, always rounding outward. */
#include <assert.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
typedef uint64_t U; typedef __uint128_t Z;
static int ns[1000];
int main(int argc,char**argv){assert(argc==5);U r=atoi(argv[1]),k=atoi(argv[2]),E=atoll(argv[3]),T=atoll(argv[4]);U F=1;for(U i=0;i<k;i++){assert(F<((U)1<<46)/r);F*=r;}assert(r<1000&&E&&T&&(Z)E*T>1);
 for(U a=0;a<r;a++)ns[a]=1;for(U a=0;a<r;a++)ns[(r-a*a%r)%r]=0;
 U top=F+2;/* (F+h)^2/h decreases up to F; endpoint F+2 can be bigger than F but not T for T<=F/2. */
 assert(T<=F/2);Z v=(Z)(F+T)*(F+T);U wmax=v/(4*((Z)E*T-1));assert(wmax<1000000000);
 U total=0,scan=0,tested=0;
 for(U c=1;c*c<=wmax;c++)if(c%r)for(U d=1;d<=wmax/(c*c);d++)if(ns[d%r]){U w=c*c*d,u=4*c*d;Z V=(Z)F*F+4*w;U h=top;
 for(int i=0;i<5;i++){Z H=(Z)(F+h)*(F+h);Z cut=(H/(4*w)+1)/E;if(cut>=h)break;h=(U)cut;}
 U x=T+(u-(F+T)%u)%u;if(x>h)continue;U count=1+(h-x)/u;
 if(count<=256){scan+=count;for(U f=x;f<=h;f+=u)if(V%f==0){tested++;U a=(F+f)/u;Z M=(Z)4*a*a*d+1;if(M%f||M/f<E||(M/f)%r==0||(Z)c*(M/f)<2*a)continue;total+=2;}}
 else { /* Compare progression length to a divisor bound after extracting g<=u. */
 U cap=1,g=1;Z y=V;for(U p=2;p<=251;p+=(p==2?1:2)){if(y%p)continue;U j=1;do{if(g<=u/p)g*=p;else j++;y/=p;}while(y%p==0);cap*=j;}if(y<=u/g)y=1;while(y>=252){y/=252;cap*=2;}total+=2*(cap<count?cap:count);}
 }
 printf("%lu %lu %lu %lu %lu %lu %lu %lu\n",r,k,E,T,wmax,scan,tested,total);
}
