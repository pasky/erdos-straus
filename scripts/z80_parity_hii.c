/* High prime Type II; full weighted counts on exactly two n-multiple denominators. */
#define main unused_hj5_main
#include "z80_parity_huge.c"
#undef main
#include "z80_parity_weights.h"
/* weights header's Jacobi uses 32-bit n. Implement 64-bit version for high rows. */
static I hi[2][5];
static I gcd_(I a,I b){while(b){I r=a%b;a=b;b=r;}return a;}
static void put(I a,I b,I c,I d,I e){if(b<a||gcd_(a,b)!=1)return;assert(4*a*b*d==n+e&&a+b==c*e);large x=(large)a*b*d, y=(large)n*a*c*d,z=(large)n*b*c*d;assert(x<y && y<z);I vals[3][5];large v[]={x,y,z};for(int i=0;i<3;i++){I q=v[i]%n;vals[i][0]=1;vals[i][1]=jac(q,n);vals[i][2]=v[i]%2?-1:1;vals[i][3]=v[i]%2?(v[i]%4==1?1:-1):0;vals[i][4]=i==0;for(int j=0;j<5;j++){if(i==0)hi[0][j]+=vals[i][j];hi[1][j]+=j==4?0:2*vals[i][j];}}}
int main(){while(scanf("%ld",&n)==1){assert(n%4==1&&n<=1600000000000L);I B=(I)sqrtl(n)+1,lo=n/4+1,up=(n+B)/4,K=up-lo+1,lim=(I)sqrtl(up)+1;ds *s=calloc(K,sizeof(ds));for(I i=0;i<K;i++){s[i].rem=lo+i;s[i].len=1;s[i].div=malloc(sizeof(I));*s[i].div=1;}char *co=calloc(lim+1,1);for(I p=2;p<=lim;p++)if(!co[p]){for(I k=p*p;k<=lim;k+=p)co[k]=1;for(I k=(p-lo%p)%p;k<K;k+=p)extend(s+k,p);}free(co);
 for(I i=0;i<K;i++){if(s[i].rem>1)extend(s+i,s[i].rem);I N=lo+i,e=4*N-n;for(int j=0;j<s[i].len;j++){I a=s[i].div[j];if(a>N/a)continue;I M=N/a;for(int k=0;k<s[i].len;k++){I b=s[i].div[k];if(b>=a&&(a+b)%e==0&&M%b==0)put(a,b,(a+b)/e,M/b,e);}}free(s[i].div);}free(s);
 I T=(2*n/B+2)/4;for(I a=1;a<=T;a++)for(I d=1;a*d<=T;d++)for(I c=1;c<=T/(a*d);c++){I f=4*a*d*c-1,num=n*c+a;if(num%f)continue;I b=num/f;if(b<a||(a+b)%c)continue;I e=(a+b)/c;if(e>B)put(a,b,c,d,e);}
 printf("%ld",n);for(int i=0;i<2;i++)for(int j=0;j<5;j++)printf(",%ld",hi[i][j]);puts("");fflush(stdout);memset(hi,0,sizeof hi);}}
