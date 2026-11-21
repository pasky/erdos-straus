/* Canonical HJ words of lengths 3 and 5, all by-excess quotients >=2.
   Input n<=2^31-1 (incl. composite controls). Sum columns are full integer counts. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
static int jac(unsigned a,unsigned n){int s=1;while(a){int v=__builtin_ctz(a);a>>=v;if((v&1)&&((n&7)==3||(n&7)==5))s=-s;if((a&n&3)==3)s=-s;unsigned t=n%a;n=a;a=t;}return n==1?s:0;}
static int cmprev(unsigned *w,int j){for(int k=0;k<j/2;k++)if(w[k]!=w[j-1-k])return w[k]<w[j-1-k]?-1:1;return 0;}
int main(){unsigned n;while(scanf("%u",&n)==1){assert(n%2 && n<2147483647);long long col[2][2][2][6]={0};
for(unsigned A=2;A<n;A++){
 unsigned a=n,b=A,w[5];for(int i=0;i<5;i++){unsigned q=(a-1)/b+1,r=q*b-a;w[i]=q;if(r==0){if((i==2||i==4)&&b==1){int k=i/2-1,j=jac(A,n)<0,cmp=cmprev(w,i+1);unsigned x=w[0],m=w[i/2];for(int o=0;o<2;o++){if(o&&cmp>0)continue;long long *v=col[k][j][o];v[0]++;v[1]+=jac(x%n,n);v[2]+=(x&1)?-1:1;v[3]+=(m&1)?(m%4==1?1:-1):0;v[4]+=cmp;v[5]+=jac(m%n,n);}}break;}a=b;b=r;}}
printf("%u",n);for(int k=0;k<2;k++)for(int j=0;j<2;j++)for(int o=0;o<2;o++)for(int s=0;s<6;s++)printf(",%lld",col[k][j][o][s]);puts("");fflush(stdout);}return 0;}
