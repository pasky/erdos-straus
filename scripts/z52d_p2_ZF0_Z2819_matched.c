/* Leave-one-prime-out fixed-level success propensities, matched p mod840
   and p in (0,50000] or (50000,100000]. Input from Z1597_levels optional raw file. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define G 1024
static unsigned char hit[5000][G],adj[G][G];static int P[5000],sum[1680][G],cnt[1680],comp[G+1];
int inv(int a,int q){int t=0,nt=1,r=q,nr=a;while(nr){int v=r/nr,x=t-v*nt;t=nt;nt=x;x=r-v*nr;r=nr;nr=x;}return t<0?t+q:t;}
int main(int argc,char**argv){if(argc!=2)return 2;FILE*f=fopen(argv[1],"rb");int n=0;while(fread(P+n,4,1,f)){if(fread(hit[n],1,G,f)!=G)return 3;int group=P[n]%840+840*(P[n]>50000);cnt[group]++;for(int c=0;c<G;c++)sum[group][c]+=hit[n][c];n++;}fclose(f);for(int q=2;q<=G;q++)if(!comp[q])for(int j=2*q;j<=G;j+=q)comp[j]=1;double total=0;long HH=0;puts("p,observed_HH,level_matched_expected_HH,stratum_n");for(int i=0;i<n;i++){int p=P[i],group=p%840+840*(p>50000);if(cnt[group]<2){fprintf(stderr,"excluded singleton p=%d\n",p);continue;}double prob[G];for(int c=0;c<G;c++){prob[c]=(sum[group][c]-hit[i][c])/(double)(cnt[group]-1);for(int d=0;d<G;d++)adj[c][d]=0;}for(int q=3;q<=G;q++)if(!comp[q]&&q!=p){int r=q-inv((4LL*p)%q,q);for(int c=r;c<=G;c+=q)for(int d=c+q;d<=G;d+=q)adj[c-1][d-1]=1;}int obs=0;double ex=0;for(int c=0;c<G;c++)for(int d=c+1;d<G;d++)if(adj[c][d]){obs+=hit[i][c]*hit[i][d];ex+=prob[c]*prob[d];}HH+=obs;total+=ex;printf("%d,%d,%.9f,%d\n",p,obs,ex,cnt[group]);}fprintf(stderr,"n=%d HH=%ld expected=%.9f ratio=%.9f\n",n,HH,total,HH/total);}
