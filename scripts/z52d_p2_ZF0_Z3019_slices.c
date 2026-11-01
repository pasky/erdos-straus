/* Exact Type-II e-slice ratio test, e=3,7,...,255; p=1 mod4<=N.
   Enumerates coprime ratios via prime exponent differences [-v,v].
   Bit j of the output is the certificate at e=4j+3 (64 bits). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
static int *spf,fac[16],expn[16],nf,ee;static int powlist[16][64],plen[16];
static int inverse(int a,int q){int t=0,nt=1,r=q,nr=a;while(nr){int v=r/nr,x=t-v*nt;t=nt;nt=x;x=r-v*nr;r=nr;nr=x;}return t<0?t+q:t;}
static int search(int j,int r){if(j==nf)return r==ee-1;for(int k=0;k<plen[j];k++)if(search(j+1,r*powlist[j][k]%ee))return 1;return 0;}
static int ratio(int n,int e){nf=0;ee=e;while(n>1){int q=spf[n],k=0;while(n%q==0){n/=q;k++;}fac[nf]=q;expn[nf]=k;powlist[nf][0]=1;int a=q%e,b=inverse(a,e),pa=1,pb=1;plen[nf]=1;for(int j=1;j<=k;j++){pa=pa*a%e;pb=pb*b%e;powlist[nf][plen[nf]++]=pa;powlist[nf][plen[nf]++]=pb;}nf++;}return search(0,1);}
int main(int argc,char**argv){if(argc!=3)return 2;int N=atoi(argv[1]),M=(N+255)/4;spf=calloc(N+256,4);for(int i=2;i<=N+255;i++)if(!spf[i])for(int j=i;j<=N+255;j+=i)if(!spf[j])spf[j]=i;unsigned char*star=calloc(M+1,1);for(int64_t a=1;4*a*a-2*a<=M;a++)for(int64_t b=a;4*a*b-a-b<=M;b++)for(int64_t n=4*a*b-a-b;n<=M;n+=4*a*b)star[n]=1;
/* same-N collisions store first hit/fail prime/e; memory O(N). */
uint32_t *seenh=calloc(M+1,4),*seenf=calloc(M+1,4);FILE*f=fopen(argv[2],"w");uint64_t ct[6][2]={0},exists[6]={0},total=0,none=0,hits=0;int maxe=0,maxp=0,coll=0;puts("p,hitmask");for(int p=5;p<=N;p+=4)if(spf[p]==p){uint64_t mask=0;int seen[6]={0},first=0;total++;for(int e=3;e<=255&&e<3*p;e+=4){if(e%p==0)continue;int n=(p+e)/4,h=ratio(n,e),sq=(int)sqrt(n);int props[6]={1,spf[n]==n,spf[n]!=n,sq*sq==n,star[n],nf>=3};for(int j=0;j<6;j++)if(props[j]){ct[j][h]++;if(h)seen[j]=1;}if(h){mask|=1ULL<<((e-3)/4);hits++;if(!first)first=e;if(!seenh[n])seenh[n]=p;}else if(!seenf[n])seenf[n]=p;if(seenh[n]&&seenf[n]&&coll<20){fprintf(f,"collision N=%d hit_p=%u hit_e=%d fail_p=%u fail_e=%d starN=%d\n",n,seenh[n],4*n-seenh[n],seenf[n],4*n-seenf[n],star[n]);coll++;seenh[n]=seenf[n]=0;}}
for(int j=0;j<6;j++){exists[j]+=seen[j];}if(!first)none++;if(first>maxe){maxe=first;maxp=p;}printf("%d,%016llx\n",p,(unsigned long long)mask);}
fprintf(f,"total=%llu hits=%llu no_hit=%llu max_first_e=%d argmax=%d\n",(unsigned long long)total,(unsigned long long)hits,(unsigned long long)none,maxe,maxp);for(int j=0;j<6;j++)fprintf(f,"property=%d fail=%llu hit=%llu primes_with_hit_property=%llu\n",j,(unsigned long long)ct[j][0],(unsigned long long)ct[j][1],(unsigned long long)exists[j]);fprintf(f,"cpu=%.3f\n",(double)clock()/CLOCKS_PER_SEC);fclose(f);free(spf);free(star);free(seenh);free(seenf);}
