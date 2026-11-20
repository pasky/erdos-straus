/* Independent exact check via round-1 short-interval factoring, no AP filters.
   Every possible smaller u is tested (8u²-2u<=n); emit all sorted u,B. */
#define main unused_round1_ap
#include "z75_obstruct.c"
#undef main
int main(int ac,char **av){for(int i=1;i<ac;i++){
 I n=atoll(av[i]);assert(n>0&&n<100000000000000LL);
 /* Keep the inherited fixed prime table within capacity. */
 int h=sqrtl(n+sqrtl(n)+10)+2;assert(h<=2700000);unsigned char *a=calloc(h+1,1);assert(a);np=0;
 for(int j=2;j<=h;j++)if(!a[j]){assert(np<200000);primes[np++]=j;for(I v=(I)j*j;v<=h;v+=j)a[v]=1;}
 free(a);int num=exact_rows(n);printf("%lld unordered R8 %d\n",n,num);
 }return 0;}
