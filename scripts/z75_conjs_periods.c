/* List fixed (A,u) or (u,v) good templates on s=start+360j, 0<=j<period<=K.
   B<=30000000 so (8B)^2 fits uint64_t. stdout: period j AorU M u. */
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <string.h>
typedef uint64_t U;
static U pw(U e,U m){U r=1%m,b=2%m;while(e){if(e&1)r=r*b%m;b=b*b%m;e/=2;}return r;}
int main(int argc,char**argv){assert(argc==4);int K=atoi(argv[1]), B=atoi(argv[2]), s0=atoi(argv[3]);assert(K>0&&K<=4000&&B>=3&&B<=30000000&&s0>=64);char*seen=calloc((K+1)*(K+1),1);assert(seen);
 for(U M=3;M<=(U)B;M++){U m=8*M,odd=M;while(!(odd%2))odd/=2;if(!(odd%3))odd/=3;if(!(odd%5))odd/=5;U b=pw(360,odd),w=b;int o=1;while(w!=1%odd && o<K){w=w*b%odd;o++;}if(w!=1%odd)continue;
  U a=(15*pw(s0,m))%m, b8=pw(360,m);for(int j=0;j<o;j++,a=a*b8%m){if(seen[o*(K+1)+j])continue;U n=a+1,r=(M-(n%M))%M;
   if(r>=2 && (M+1)%r==0){U t=(M+1)/r,v=(n+r)/M;if(t>=2&&((n+t)*t*r*v)%8==0){printf("%d %d A %lu %lu\n",o,j,M,r);seen[o*(K+1)+j]=1;continue;}}
   if(r*r<4*M)continue;
   U z=(U)sqrt((double)(r*r-4*M));
   if(z*z!=r*r-4*M||(r-z)%2)continue;
   U u=(r-z)/2;
   if(u>=2&&((n+(n+r)/M)*M)%8==0){printf("%d %d U %lu %lu\n",o,j,M,u);seen[o*(K+1)+j]=1;}
  }
 }
 free(seen);return 0;}
