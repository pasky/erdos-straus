/* Native moduli: mark r first digits; later append ONLY actual centres and sort.
   Exact P_3 with split e<=E (shift factorizations) vs acd<=T (joint triples).
   For large r this is much cheaper than lifting any box to common depth. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;
#define R 7220
#define Y 350000
#define W 8192
static int pr[Y+1],np,co[Y+1],allow[R];
static U r,n,w,dat,l1,raw,ng,alloc,*gens,re[W],fac[W][12];static unsigned char nf[W],expn[W][12];
static void add(U x){if(allow[x%r]!=1)return;if(w==r){allow[x%r]=2;l1++;return;}if(ng==alloc){alloc=2*alloc+1024;gens=realloc(gens,alloc*sizeof(U));assert(gens);}gens[ng++]=x;}
static void hit(U a,U b,U c,U d){if(c%r==0||d%r==0||a%r==0||b%r==0)return;dat++;add((1+w-(4*a%w*c%w*d%w))%w);add((1+w-(4*b%w*c%w*d%w))%w);}
static void triples(int i,int k,U a,U b,U e,U M){if(a>M/a)return;
 if(k==nf[i]){if(a<=b&&(a+b)%e==0)hit(a,b,(a+b)/e,M/(a*b));return;}
 U p=fac[i][k];int z=expn[i][k];for(int u=0;u<=z;u++){U bb=b;for(int v=0;v<=z-u;v++){triples(i,k+1,a,bb,e,M);if(v<z-u)bb*=p;}if(u<z)a*=p;}}
static void fs(int i,U p,int e){assert(nf[i]<12);expn[i][nf[i]]=e;fac[i][nf[i]++]=p;}
static void shifts(U E){U lo=n/4+1,end=(n+E)/4+1;
 for(U j=lo;j<end;j+=W){int len=end-j<W?end-j:W;for(int i=0;i<len;i++){re[i]=j+i;nf[i]=0;}
 for(int t=0;t<np;t++){U p=pr[t];if(p*p>end)break;for(int i=(p-j%p)%p;i<len;i+=p){int h=0;do{re[i]/=p;h++;}while(re[i]%p==0);fs(i,p,h);}}
 for(int i=0;i<len;i++){U M=j+i,e=4*M-n;if(e%r==0)continue;if(re[i]>1)fs(i,re[i],1);triples(i,0,1,1,e,M);}}}
static void large(U E){U T=(n/(E+1)+1)/2;for(U a=1;a<=T&&2*a*a<=n;a++)for(U d=1;a*d<=T&&2*a*a*d<=n;d++){
 U u=4*a*d,V=n+a*u;for(U c=1;c<=T/(a*d);c++){U f=u*c-1;if(V%f)continue;U e=V/f;if(e<=E||c*e<2*a)continue;hit(a,c*e-a,c,d);}}}
static void qfirst(){U T=(r+1)/2;for(U a=1;a<=T;a++)for(U d=1;a*d<=T;d++){U u=4*a*d,V=a*u+1;for(U c=r/u+1;c<=T/(a*d);c++){U f=u*c-r;if(V%f)continue;U e=V/f;if(c*e<2*a||e%r==0||c%r==0)continue;U b=c*e-a;add((r-4*a%r*a%r*d%r)%r);add((r-4*b%r*b%r*d%r)%r);}}}
static int cmp(const void*aa,const void*bb){U x=*(U*)aa,y=*(U*)bb;return(x>y)-(x<y);}
int main(int argc,char**argv){assert(argc==3);int L=atoi(argv[1]),H=atoi(argv[2]);assert(L>=17&&H<R&&L<=H);
 for(int p=2;p<=Y;p++)if(!co[p]){pr[np++]=p;if(p<=Y/p)for(int t=p*p;t<=Y;t+=p)co[t]=1;}
 for(r=L;r<=H;r++)if(!co[r]){for(int i=0;i<r;i++)allow[i]=1;for(int i=0;i<r;i++)allow[i*i%r]=0;dat=ng=l1=0;n=w=r;large(0);qfirst();
 n=r*r*r;w=r*r;U E=1;while(E*E<n)E++;dat=0;shifts(E);large(E);qsort(gens,ng,sizeof(U),cmp);U ct=0;for(U i=0;i<ng;i++)if(!i||gens[i]!=gens[i-1])ct++;
 printf("%lu %lu %lu %lu %lu\n",r,l1,dat,ng,ct);fflush(stdout);}}
