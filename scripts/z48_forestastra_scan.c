/* z48 forestastra: full edge census + first split-fibre / pruning audit.
 * O(N + selected edges) storage; hard N <= 10^7, allocation ceiling 2 GB.
 * Independent AP construction, SPF factor enumeration, Jacobi and Euler signs.
 */
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct { int u,v,next; } Edge;
static Edge *edges; static size_t ne,cap;
static int *head;
static void add(int p,int u,int v) {
 if(ne==cap){cap=cap?2*cap:65536;assert(cap*sizeof(Edge)<2000000000ULL);
  edges=realloc(edges,cap*sizeof(Edge));assert(edges);}
 edges[ne]=(Edge){u,v,head[p]};head[p]=(int)ne++;
}
static int jac(int a,int n) {
 int s=1;a%=n;while(a){while(!(a&1)){a/=2;if(n%8==3||n%8==5)s=-s;}
  int z=a;a=n;n=z;if(a%4==3&&n%4==3)s=-s;a%=n;}return n==1?s:0;
}
static int euler(int a,int p){int64_t x=a%p,y=1;for(int k=(p-1)/2;k;k>>=1,x=x*x%p)if(k&1)y=y*x%p;return y==1?1:y==p-1?-1:0;}
static int slots(int t,int u,int v,int k){return t%k==0||u%k==0||v%k==0||((int64_t)t*u-1)%k==0||((int64_t)t*v-1)%k==0;}
static int qrformula(int t,int u,int v) {
 if(u%2 && v%2)return u%4==1&&v%4==1?1:-1;
 int even=u%2?v:u;
 if(even%4==0)return -1;
 return t%4==1||t%4==2?1:-1;
}
static int divisors(int n,const int *spf,int *ds) {
 int k=1;ds[0]=1;while(n>1){int q=spf[n],old=k,power=1;
  while(n%q==0){n/=q;power*=q;for(int j=0;j<old;j++){assert(k<4096);ds[k++]=ds[j]*power;}}}return k;
}
static int root(int x,const int *parent){while(parent[x])x=parent[x];return x;}
int main(int argc,char **argv) {
 int N=argc>1?atoi(argv[1]):1000000;assert(N>=1000&&N<=10000000);
 int audit=argc>2; /* Optional complete independent divisor reconstruction. */
 int S=N+(int)sqrt(N)+10;
 int *spf=calloc(S+1,sizeof(int));head=malloc((N+1)*sizeof(int));
 int *parent=calloc(N+3,sizeof(int)),*seen=calloc(N+3,sizeof(int)),*verts=malloc((N+3)*sizeof(int));
 assert(spf&&head&&parent&&seen&&verts);
 for(int i=0;i<=N;i++)head[i]=-1;
 for(int i=2;i<=S;i++)if(!spf[i])for(int j=i;j<=S;j+=i)if(!spf[j])spf[j]=i;
 /* All p=1 mod24 to N; other p=1 mod4 through min(N,10^6). */
 unsigned char *sel=calloc(N+1,1);assert(sel);
 for(int p=5;p<=N;p+=4)if(spf[p]==p&&(p%24==1||p<=1000000))sel[p]=1;
 for(int u=1;(int64_t)(u-1)*(u-1)<=N+1;u++){
  int vmax=u==1?N+1:(N+u)/(u-1);
  for(int v=u+1;v<=vmax;v++){
   int64_t step=(int64_t)u*v;
   for(int64_t n=(u==1?2:1)*step-u-v;n<=N;n+=step)if(n>=5&&sel[n])add((int)n,u,v);
  }
 }
 long np=0,n24=0,total=0,good=0,splitfail=0,parentfail=0,root1fail=0;
 long hist[128]={0},failhist[128]={0},khist[128]={0};int maxH=0,atH=0,maxB=0,atB=0,maxgap=0,atgap=0,maxK=0,atK=0;
 puts("p,r,H,u,t,B,first_split_hit,min_good_smaller,min_mixed_root,edges,good_edges,root1_mixed,split_fibres_to_hit");
 for(int p=5;p<=N;p+=4)if(sel[p]){
  int nv=0,ec=0,gc=0,H=p+3,hu=0,ht=0,minu=p+3,minroot=p+3,rootmixed=0;
  for(int e=head[p];e>=0;e=edges[e].next){int u=edges[e].u,v=edges[e].v;
   assert(!parent[v]);parent[v]=u;
   if(seen[u]!=p){seen[u]=p;verts[nv++]=u;}if(seen[v]!=p){seen[v]=p;verts[nv++]=v;}
   int t=(int)((p+(int64_t)u+v)/((int64_t)u*v));
   int s=jac(u,p)*jac(v,p);
   assert(u==(v-p%v)%v);assert(qrformula(t,u,v)==s);assert(slots(t,u,v,4)==(s==-1));
   assert(euler(u,p)*euler(v,p)==s);assert(jac(t*u-1,p)==s);
   if(s==-1){gc++;if(v<H){H=v;hu=u;ht=t;}if(u<minu)minu=u;}
   ec++;
  }
  int nc=0;for(int j=0;j<nv;j++){int v=verts[j],rt=root(v,parent);nc+=parent[v]==0;
   if(jac(v,p)!=jac(rt,p)){if(rt<minroot)minroot=rt;if(rt==1)rootmixed=1;}
   if(parent[v]&&parent[parent[v]])assert((v-parent[parent[v]])%parent[v]==0);
  }
  assert(ec==nv-nc);assert((gc>0)==(minroot<p+3));
  if(audit){
   int found=0,ds[4096];
   for(int u=1;(int64_t)(u-1)*(u-1)<=p+1;u++){
    int nd=divisors(p+u,spf,ds);
    for(int j=0;j<nd;j++){int v=ds[j];
     if(v>u&&(p+(int64_t)u+v)%((int64_t)u*v)==0){assert(parent[v]==u);found++;}
    }
   }
   assert(found==ec);
  }
  /* Independent minimum scan: raw parent, no five-slot test. */
  int independent=0;for(int v=2;v<=H&&v<p;v++){int u=(v-p%v)%v;
   if(u&&(p+(int64_t)u+v)%((int64_t)u*v)==0&&euler(u,p)*euler(v,p)==-1){independent=v;break;}}
  assert(independent==H);assert(parent[p]==0&&parent[p+1]==1&&parent[p+2]==2);
  int r=2;while(jac(r,p)!=-1)r++;assert(r<=H);
  int B=0,bhit=0;int ds[4096];
  for(int b=1;b<r;b++){
   int nd=divisors(p+b,spf,ds),has=0;
   for(int j=0;j<nd;j++)if(jac(ds[j],p)==-1){has=1;assert(ds[j]>b&&ds[j]<p);
    if((p+ds[j])%b==0)bhit=1;}
   if(has){B=b;break;}
  }
  assert(B>0&&B<r);assert(B<=minu);assert((B==minu)==bhit);
  assert(B>=4||bhit); /* theorem for first split roots 1,2,3 */
  if(B==4)assert(bhit); /* direct reciprocity at p+4 */
  assert(B<128);hist[B]++;if(!bhit){splitfail++;failhist[B]++;}
  parentfail+=parent[r]==0;root1fail+=!rootmixed;
  if(H>maxH){maxH=H;atH=p;}if(B>maxB){maxB=B;atB=p;}
  if(minu-B>maxgap){maxgap=minu-B;atgap=p;}
  /* Count roots with an opposite-coloured child in the full remainder tree,
     through the first root with an actual opposite-coloured larger neighbour.
     After B, a root need not itself be a residue. */
  int K=0;
  for(int b=1;b<=minu;b++){
   int nd=divisors(p+b,spf,ds),has=0;
   for(int j=0;j<nd;j++)if(ds[j]>b&&ds[j]<p&&jac(ds[j],p)!=jac(b,p))has=1;
   K+=has;
  }
  assert(K>0&&K<128);khist[K]++;if(K>maxK){maxK=K;atK=p;}
  printf("%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n",p,r,H,hu,ht,B,bhit,minu,minroot,ec,gc,rootmixed,K);
  np++;n24+=p%24==1;total+=ec;good+=gc;
  for(int j=0;j<nv;j++)parent[verts[j]]=0;
 }
 fprintf(stderr,"N=%d primes=%ld p1mod24=%ld edges=%ld good=%ld first_split_fail=%ld least_QNR_parent_fail=%ld root1_fail=%ld complete_divisor_audit=%d\n",N,np,n24,total,good,splitfail,parentfail,root1fail,audit);
 fprintf(stderr,"maxH=%d at=%d maxB=%d at=%d max_min_good_smaller_minus_B=%d at=%d stored=%zu capacity_bytes=%zu\n",maxH,atH,maxB,atB,maxgap,atgap,ne,cap*sizeof(Edge));
 for(int b=1;b<128;b++)if(hist[b])fprintf(stderr,"B=%d primes=%ld first_split_fail=%ld\n",b,hist[b],failhist[b]);
 fprintf(stderr,"max_split_fibres_to_hit=%d at=%d\n",maxK,atK);
 for(int k=1;k<128;k++)if(khist[k])fprintf(stderr,"K=%d primes=%ld\n",k,khist[k]);
 free(edges);free(spf);free(head);free(parent);free(seen);free(verts);free(sel);return 0;
}
