/* Exact early-exit divisor search. 128-bit B^2; divisors truncated at B.
   A bounded x search is NEVER called an exhaustive failure. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <omp.h>
typedef int64_t I; typedef __int128 J;
#define MAX 1000000
static int spf[MAX+1];
typedef struct{I A,B,lo;int q,r,np;I pf[32];int pe[32];} Ctx;
static void fac(Ctx*c,int v){while(v>1){int p=spf[v],e=0;while(v%p==0){v/=p;e+=2;}int j=0;while(j<c->np&&c->pf[j]!=p)j++;if(j==c->np){c->pf[j]=p;c->pe[j]=0;c->np++;}c->pe[j]+=e;}}
static int dfs(Ctx*c,int i,I d){if(i==c->np){if(d<c->lo||(d+c->B)%c->A)return 0;I y=(d+c->B)/c->A;if(y%c->q!=c->r)return 0;J z=(J)c->B*c->B/d+c->B;if(z%c->A)return 0;return (z/c->A)%c->q==c->r;}
for(int e=0;e<=c->pe[i];e++){if(dfs(c,i+1,d))return 1;if(d>c->B/c->pf[i])break;d*=c->pf[i];}return 0;}
static int search(int n,int q,int r,int steps){I x=n/4+1; x+=(r-x%q+q)%q;I hi=3LL*n/4;if(steps&&hi>x+(I)q*steps)hi=x+(I)q*steps;
for(;x<=hi;x+=q){Ctx c={.A=4*x-n,.B=n*x,.q=q,.r=r};c.lo=c.A*x-c.B;if(c.lo<1)c.lo=1;fac(&c,n);fac(&c,x);if(dfs(&c,0,1))return 1;}return 0;}
int main(int argc,char**argv){int N=argc>1?atoi(argv[1]):MAX,steps=argc>2?atoi(argv[2]):32;
for(int i=2;i<=MAX;i++)if(!spf[i])for(int j=i;j<=MAX;j+=i)if(!spf[j])spf[j]=i;
#pragma omp parallel for num_threads(4) schedule(dynamic)
for(int qi=0;qi<3;qi++){int qs[]={5,7,11},q=qs[qi];unsigned char *ok=calloc(N+1,1);I admiss[12]={0},yes[12]={0},inherited[12]={0},unresolved[12]={0};int first[12]={0},first6[12]={0};I admiss6[12]={0},yes6[12]={0};double st=omp_get_wtime();
char path[200];snprintf(path,sizeof(path),"data/z52b/pass2/ZF0/Z0524/failures_q%d_N%d_steps%d.csv",q,N,steps);FILE*fo=fopen(path,"w");if(!fo){perror(path);exit(2);}fprintf(fo,"n,r,coprime6\n");
for(int n=2;n<=N;n++){if(n%100000==0){
#pragma omp critical
{fprintf(stderr,"progress q=%d n=%d seconds=%.3f\n",q,n,omp_get_wtime()-st);fflush(stderr);}}
if(n%q==0)continue;
int r;
for(r=1;r<q;r++)if((4*r-3*n)%q==0)break;
admiss[r]++;int cop6=n%2&&n%3;if(cop6)admiss6[r]++;int m=n/spf[n];if(m>1&&ok[m]){ok[n]=1;inherited[r]++;}else ok[n]=search(n,q,r,steps);
if(ok[n]){yes[r]++;if(cop6)yes6[r]++;}else{unresolved[r]++;fprintf(fo,"%d,%d,%d\n",n,r,cop6);if(!first[r]&&n<=20000&&!search(n,q,r,0))first[r]=n;if(cop6&&!first6[r]&&n<=20000&&!search(n,q,r,0))first6[r]=n;}
}
fclose(fo);
#pragma omp critical
{printf("q=%d N=%d x_steps=%d seconds=%.3f\n",q,N,steps,omp_get_wtime()-st);for(int r=1;r<q;r++)printf("r=%d admissible=%lld certified=%lld inherited=%lld unresolved=%lld first_exact_failure=%d coprime6_admissible=%lld coprime6_certified=%lld coprime6_first_failure=%d\n",r,(long long)admiss[r],(long long)yes[r],(long long)inherited[r],(long long)unresolved[r],first[r],(long long)admiss6[r],(long long)yes6[r],first6[r]);fflush(stdout);}free(ok);}
}
