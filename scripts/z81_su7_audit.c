/* Independent single-input audit: trial division only, no word enumeration. */
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <assert.h>
typedef uint64_t U;
static unsigned factor(U a,int print){unsigned w=0;
 for(U l=2;l<=a/l;l+=1+(l!=2))if(a%l==0){unsigned e=0;do{a/=l;++e;}while(a%l==0);++w;if(print)printf(" %" PRIu64 "^%u",l,e);}
 if(a>1){++w;if(print)printf(" %" PRIu64 "^1",a);}return w;}
static int prime(U a){if(a<2)return 0;for(U j=2;j<=a/j;j+=1+(j!=2))if(a%j==0)return 0;return 1;}
int main(int argc,char**argv){assert(argc>=2);
 for(int i=1;i<argc;i++){
 U p=strtoull(argv[i],0,10);assert(p<=UINT64_MAX/3);printf("n=%" PRIu64 " prime=%d\n",p,prime(p));int hits=0,b=0,c135=0,c6=0,cl[]={1,3,5,7,9,25};
 for(U f=7;f<=2*p+1;f+=8){U r=f-p%f;if(r==f || (f+1)%r)continue;
 ++hits;printf(" f=%" PRIu64 " r=%" PRIu64 " fac:",f,r);b+=(factor(f,1)<=2);int m=0;
 for(int j=0;j<6;j++)if(f%cl[j]==0 && prime(f/cl[j]))m|=1<<j;
 printf(" mask=%d\n",m);c135+=!!(m&7);c6+=!!m;
 }printf("hits=%d B=%d C135=%d C6=%d\n",hits,b,c135,c6);
 }return 0;}
