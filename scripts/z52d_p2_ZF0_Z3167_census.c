/* Exact certificate census. gcc -O2 ... -lm; args N Ccap outdir.
   Level sieve marks p=4Cab-a-b, a<=b, p=1 mod4; uncovered primes
   are completed by factoring p+a for every 4a*a-2a<=p. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
static int primes[100000],np;
static uint64_t divs[20000];
static int divisors(uint64_t n){int nd=1;divs[0]=1;for(int i=0;i<np&&(uint64_t)primes[i]*primes[i]<=n;i++){int q=primes[i];if(n%q)continue;int base=nd;uint64_t pw=1;while(n%q==0){n/=q;pw*=q;for(int j=0;j<base;j++)divs[nd++]=divs[j]*pw;}}if(n>1){int base=nd;for(int j=0;j<base;j++)divs[nd++]=divs[j]*n;}return nd;}
int main(int argc,char**argv){if(argc!=4)return 2;int N=atoi(argv[1]),cap=atoi(argv[2]);char path[512];unsigned char*comp=calloc(N+1,1);uint32_t*K=calloc(N/4+1,4);for(int i=2;i<=N;i++)if(!comp[i]){if(i<=100000)primes[np++]=i;if((int64_t)i*i<=N)for(int j=i*i;j<=N;j+=i)comp[j]=1;}
for(int c=1;c<=cap;c++){for(int64_t a=1;4LL*c*a*a-2*a<=N;a++){int64_t d=4LL*c*a-1,b=a;while((a+b)%4!=3)b++;for(int64_t p=d*b-a;p<=N;p+=4*d)if(!K[p/4])K[p/4]=c;}if(c%512==0)fprintf(stderr,"C=%d cpu=%.1f\n",c,(double)clock()/CLOCKS_PER_SEC);}
snprintf(path,sizeof(path),"%s/tail.csv",argv[3]);FILE*t=fopen(path,"w");fprintf(t,"p,minC\n");int tail=0;for(int p=5;p<=N;p+=4)if(!comp[p]&&!K[p/4]){uint32_t best=UINT32_MAX;for(int a=1;4LL*a*a-2*a<=p;a++){int nd=divisors(p+a);for(int j=0;j<nd;j++){uint64_t d=divs[j];if((d+1)%(4*a)==0&&(p+a)/d>=(uint64_t)a){uint64_t c=(d+1)/(4*a);if(c<best)best=c;}}}K[p/4]=best;fprintf(t,"%d,%u\n",p,best==UINT32_MAX?0:best);tail++;}fclose(t);
snprintf(path,sizeof(path),"%s/decades.csv",argv[3]);FILE*f=fopen(path,"w");fprintf(f,"bound,count,zeros,maxC,argmax,maxC_hard,argmax_hard\n");for(int64_t B=10;B<=N;B*=10){int count=0,z=0,m=0,arg=0,mh=0,ah=0;for(int p=5;p<=B;p+=4)if(!comp[p]){count++;uint32_t k=K[p/4];if(k==UINT32_MAX){z++;continue;}if((int)k>m){m=(int)k;arg=p;}int r=p%840;if((r==1||r==121||r==169||r==289||r==361||r==529)&&(int)k>mh){mh=(int)k;ah=p;}}fprintf(f,"%lld,%d,%d,%d,%d,%d,%d\n",(long long)B,count,z,m,arg,mh,ah);}fclose(f);
snprintf(path,sizeof(path),"%s/records.csv",argv[3]);f=fopen(path,"w");fprintf(f,"p,minC\n");uint32_t rec=0;for(int p=5;p<=N;p+=4)if(!comp[p]&&K[p/4]!=UINT32_MAX&&K[p/4]>rec){rec=K[p/4];fprintf(f,"%d,%u\n",p,rec);}fclose(f);
printf("N=%d cap=%d completed_tail=%d cpu=%.3f\n",N,cap,tail,(double)clock()/CLOCKS_PER_SEC);free(K);free(comp);}
