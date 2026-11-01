/* Level factor sieve (all C<=4096, p=1 mod4<=100000) and exact shared-prime
   hypergraphs on C<=1024. No Cartesian-product arrays beyond 1024^2 bytes. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
#define X 4096
#define G 1024
static int ps[10000],np,comp[100001],parent[G+1];
static uint64_t rem[X+1];static unsigned char om[X+1],hit[X+1],adj[G+1][G+1];
int inv(int a,int q){int t=0,nt=1,r=q,nr=a;while(nr){int v=r/nr,x=t-v*nt;t=nt;nt=x;x=r-v*nr;r=nr;nr=x;}return t<0?t+q:t;}
int root(int a){while(parent[a]!=a){parent[a]=parent[parent[a]];a=parent[a];}return a;}
int main(int argc,char**argv){if(argc!=3&&argc!=4)return 2;FILE*raw=argc==4?fopen(argv[3],"wb"):NULL;FILE*f=fopen(argv[1],"w"),*g=fopen(argv[2],"w");fprintf(f,"p,total_hits,rich,rich_fail,maxomega,rich_fail_example_C\n");fprintf(g,"p,hits,edges,HH,HF,FF,expected_HH,components,giant,isolates\n");for(int i=2;i<=100000;i++)if(!comp[i]){if(i<=40500)ps[np++]=i;for(int j=2*i;j<=100000;j+=i)comp[j]=1;}
uint64_t hist[16][2]={0},band[4][16][2]={0},feasible[16][2]={0};for(int p=5;p<=100000;p+=4)if(!comp[p]){for(int c=1;c<=X;c++){rem[c]=4ULL*c*p+1;om[c]=hit[c]=0;for(uint64_t d=4*c-1;d*d<=rem[c];d+=4*c)if(rem[c]%d==0){hit[c]=1;break;}}
for(int i=1;i<np&&(uint64_t)ps[i]*ps[i]<=4ULL*X*p+1;i++){int q=ps[i];if(p==q)continue;int r=q-inv((4LL*p)%q,q);for(int c=r;c<=X;c+=q){if(!c)continue;if(rem[c]%q==0){om[c]++;do{rem[c]/=q;}while(rem[c]%q==0);}}}
int h=0,rich=0,rf=0,m=0,ex=0;for(int c=1;c<=X;c++){if(rem[c]>1)om[c]++;h+=hit[c];if(om[c]>m)m=om[c];if(om[c]>=6){rich++;if(!hit[c]){rf++;if(!ex)ex=c;}}hist[om[c]][hit[c]]++;if(8*c-3<=p)feasible[om[c]][hit[c]]++;int b=c<=64?0:c<=256?1:c<=1024?2:3;band[b][om[c]][hit[c]]++;}fprintf(f,"%d,%d,%d,%d,%d,%d\n",p,h,rich,rf,m,ex);
if(raw){fwrite(&p,4,1,raw);fwrite(hit+1,1,G,raw);}
/* Build every shared-prime hyperedge; primes >G cannot occur twice. */
for(int c=1;c<=G;c++){parent[c]=c;for(int d=1;d<=G;d++)adj[c][d]=0;}
for(int i=1;i<np&&ps[i]<=G;i++){int q=ps[i];if(p==q)continue;int r=q-inv((4LL*p)%q,q);for(int c=r;c<=G;c+=q)for(int d=c+q;d<=G;d+=q){adj[c][d]=1;parent[root(c)]=root(d);}}
int counts[G+1]={0},bh[G/16]={0},nh=0,edges=0,HH=0,HF=0,FF=0,iso=0,giant=0,ncomp=0;double expected=0;for(int c=1;c<=G;c++){counts[root(c)]++;bh[(c-1)/16]+=hit[c];nh+=hit[c];}for(int c=1;c<=G;c++){if(counts[c]){ncomp++;if(counts[c]>giant)giant=counts[c];if(counts[c]==1)iso++;}for(int d=c+1;d<=G;d++)if(adj[c][d]){edges++;if(hit[c]&&hit[d])HH++;else if(hit[c]||hit[d])HF++;else FF++;int a=(c-1)/16,b=(d-1)/16;expected+=a==b?bh[a]*(bh[a]-1)/240.:bh[a]*bh[b]/256.;}}
fprintf(g,"%d,%d,%d,%d,%d,%d,%.9f,%d,%d,%d\n",p,nh,edges,HH,HF,FF,expected,ncomp,giant,iso);
}fclose(f);fclose(g);if(raw)fclose(raw);puts("omega,fail,hit");for(int w=0;w<16;w++)if(hist[w][0]+hist[w][1])printf("%d,%llu,%llu\n",w,(unsigned long long)hist[w][0],(unsigned long long)hist[w][1]);puts("band,omega,fail,hit");for(int b=0;b<4;b++)for(int w=0;w<16;w++)if(band[b][w][0]+band[b][w][1])printf("%d,%d,%llu,%llu\n",b,w,(unsigned long long)band[b][w][0],(unsigned long long)band[b][w][1]);puts("feasible_omega,fail,hit");for(int w=0;w<16;w++)if(feasible[w][0]+feasible[w][1])printf("%d,%llu,%llu\n",w,(unsigned long long)feasible[w][0],(unsigned long long)feasible[w][1]);fprintf(stderr,"cpu=%.3f\n",(double)clock()/CLOCKS_PER_SEC);}
