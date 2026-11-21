/* Shares only sieve/divisor primitives with the independent prefix solver. */
#define main unused_hj5_main
#include "z80_parity_huge.c"
#undef main
static I bins[6][2][6];
static void add(int k,int o,I n,I u,I t,I v){I *r=bins[k][o];r[0]++;r[1]+=jac(u,n);r[2]+=u%2?-1:1;r[3]+=t%2?(t%4==1?1:-1):0;r[4]+=(u>v)-(u<v);r[5]+=jac(t,n);}
int main(){while(scanf("%ld",&n)==1){assert(n>1&&n%2&&n<=1600000000000L);I K=(I)sqrtl(n+1)+2,lim=(I)sqrtl(n+K)+1;ds *s=calloc(K+1,sizeof(ds));for(I i=1;i<=K;i++){s[i].rem=n+i;s[i].len=1;s[i].div=malloc(sizeof(I));*s[i].div=1;}char *comp=calloc(lim+1,1);for(I p=2;p<=lim;p++)if(!comp[p]){for(I k=p*p;k<=lim;k+=p)comp[k]=1;for(I k=p-n%p;k<=K;k+=p)extend(s+k,p);}free(comp);
 for(I u=1;u<=K;u++){if(s[u].rem>1)extend(s+u,s[u].rem);for(int i=0;i<s[u].len;i++){I v=s[u].div[i];if(v<u||(n+u+v)%(u*v))continue;I t=(n+u+v)/(u*v);int yes[6]={t%4==0,t%8==4,t%8==0,(t*u)%8==0||(t*v)%8==0,0,0};if(u>=2&&t>=2){int sg=jac(t*u-1,n);assert(sg!=0);yes[4+(sg<0)]=1;}for(int k=0;k<6;k++)if(yes[k]){add(k,1,n,u,t,v);if(k!=3||(t*u)%8==0)add(k,0,n,u,t,v);if(u!=v&&(k!=3||(t*v)%8==0))add(k,0,n,v,t,u);}}free(s[u].div);}free(s);
 printf("%ld",n);for(int k=0;k<6;k++)for(int o=0;o<2;o++)for(int j=0;j<6;j++)printf(",%ld",bins[k][o][j]);puts("");fflush(stdout);memset(bins,0,sizeof bins);}}
