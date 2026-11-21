/* Meet in the middle for EXACT length 5; no O(n) scan. Works to listed 1.6e12. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
#include <math.h>
typedef int64_t I;
static int jac(I a,I n){int s=1;a%=n;while(a){int k=__builtin_ctzll(a);a>>=k;if((k&1)&&(n%8==3||n%8==5))s=-s;if((a&n&3)==3)s=-s;I r=n%a;n=a;a=r;}return n==1?s:0;}
static I W[2][2][6],n;
static void word(I A,I a,I b,I t,I d,I e,I C){if(C<A || (C==A && (a>e || (a==e && b>d))))return;
 assert(A==a*b-1&&C==d*e-1&&A*(t*C-e)-a*C==n);int sg=jac(b*(t*C-e)-C,n);assert(sg);int cmp=a!=e?(a<e?-1:1):b!=d?(b<d?-1:1):0;
 for(int i=0;i<1+(cmp!=0);i++){I x=i?e:a;int r=i?-cmp:cmp;for(int o=0;o<2;o++){if(o&&r>0)continue;I *v=W[sg<0][o];v[0]++;v[1]+=jac(x,n);v[2]+=x%2?-1:1;v[3]+=t%2?(t%4==1?1:-1):0;v[4]+=r;v[5]+=jac(t,n);}}}
typedef struct {I rem,*div;int len;} ds;
static void extend(ds *x,I p){int e=0;while(x->rem%p==0)x->rem/=p,++e;int h=x->len;x->len*=e+1;x->div=realloc(x->div,sizeof(I)*x->len);assert(x->div);for(int i=h;i<x->len;i++)x->div[i]=x->div[i-h]*p;}
int main(){while(scanf("%ld",&n)==1){assert(n%2&&n>6&&n<=1600000000000L);I B=sqrtl(1.5L*n)+1,K=1+(I)sqrtl(n)/4,lim=1+(I)sqrtl(n+K);ds *s=calloc(K+1,sizeof(ds));
 for(I i=1;i<=K;i++){s[i].rem=n+i;s[i].len=1;s[i].div=malloc(sizeof(I));*s[i].div=1;}char *comp=calloc(lim+1,1);for(I p=2;p<=lim;p++)if(!comp[p]){for(I k=p*p;k<=lim;k+=p)comp[k]=1;I k=p-n%p;for(;k<=K;k+=p)extend(s+k,p);}free(comp);for(I i=1;i<=K;i++)if(s[i].rem>1)extend(s+i,s[i].rem);
 for(I a=2;a*2-1<=B;a++)for(I b=2,A=a*2-1;A<=B;b++,A+=a){for(I t=2,M=2*A-a;M<=K;t++,M+=A)for(int k=0;k<s[M].len;k++){I e=s[M].div[k];if(e<2)continue;I u=(n+M)/e+A;if(u%M==0&&u/M>=2)word(A,a,b,t,u/M,e,(u/M)*e-1);}
 I cap=3*n/(2*A);if(cap>2*n/K)cap=2*n/K;I start=A+((A-(n%A)*(b%A)%A)%A);for(I C=start;C<=cap;C+=A){I r=(n+a*C)/A,e=C-r%C;if(e<2 || (C+1)%e || (C+1)/e<2)continue;I t=(r+e)/C;if(t>=2&&t*A-a>K)word(A,a,b,t,(C+1)/e,e,C);}}
 printf("%ld",n);for(int sgn=0;sgn<2;sgn++)for(int o=0;o<2;o++)for(int j=0;j<6;j++)printf(",%ld",W[sgn][o][j]);puts("");fflush(stdout);for(I i=1;i<=K;i++)free(s[i].div);free(s);memset(W,0,sizeof W);}}
