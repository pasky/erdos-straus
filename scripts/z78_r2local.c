/* Per-N tight integer P layer. Bounds on log2*16 use 8-bit normalized
 mantissas; certificate lo[i]=floor(log2(i)*16) supplied by exact integer
 powers. N<=2^114; acd bounds tested in 128-bit via quotient. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;static int lo[513],capk[4800][4000][8];static int ls[]={2,3,4,5,6,8,12,16};
static int bits(Z x){U hi=x>>64,low=x;return hi?128-__builtin_clzll(hi):low?64-__builtin_clzll(low):0;}
static int lg(Z x,int up){int b=bits(x),s=b-9;if(s<=0)return lo[(int)x]+(up&&(x&(x-1))!=0);int a=x>>s;return 16*s+(up?lo[a+1]+1:lo[a]);}
static Z cap(int v,int f,Z w){if(w<2||f<=0)return w;assert(v<4800&&f<4000);Z best=w;for(int i=0;i<8;i++){int k=capk[v][f][i];if(k<0)continue;if(k>125)k=125;Z D=((Z)1<<k)+1;Z val=(ls[i]-1)*((w+D-1)/D);if(val<best)best=val;}return best;}
static Z mn(Z a,Z b){return a<b?a:b;}
static void pr(Z x){char s[64];int n=0;do{s[n++]=48+x%10;x/=10;}while(x);while(n)putchar(s[--n]);}
int main(int argc,char**argv){assert(argc>=5);FILE*fp=fopen(argv[1],"r");assert(fp);for(int i=1;i<=512;i++)assert(fscanf(fp,"%d",lo+i)==1);fclose(fp);int K=atoi(argv[2]),step=atoi(argv[3]);assert(K>=5&&K<=17&&step>=1&&step<=12);
 static Z es[4096],bu[200];static int le[4096],he[4096];
 for(int t=4;t<argc;t++){int r=atoi(argv[t]);Z n=1;for(int i=0;i<K;i++)n*=r;int b=bits(n),jmin=b*3/8-4,jmax=b/2+1;assert(b<=114&&r>=17&&r<1000);Z high=(n/((Z)1<<jmin)+1)/2;int ne=1;es[0]=1;while(es[ne-1]<=high){Z x=es[ne-1];es[ne++]=x+(x>=step?x/step:1);}for(int i=0;i<ne;i++){le[i]=lg(es[i],0);he[i]=lg(es[i],1);}int L=lg(n,1),LL=lg(n,0);for(int v=L-8;v<=16*(3*b-2*jmin+12);v++)for(int f=1;f<=16*(2*b-jmin+12);f++)for(int i=0;i<8;i++){int l=ls[i],m=f*l/v;if(m>=l)m=l-1;int a=f*m*l-v*(m*(m+1)/2);capk[v][f][i]=a>0?(a-1)/(16*(l*(l-1)/2)):-1;}
 for(int i=0;i<200;i++)bu[i]=0;
 for(int ia=0;ia+1<ne;ia++){Z A=es[ia],An=es[ia+1];if(2*A>n/A||A>high)break;for(int ic=0;ic+1<ne;ic++){Z C=es[ic],Cn=es[ic+1];if(C>high/A)break;Z top=high/(A*C);for(int id=0;es[id]<=top;id++){
 Z D=es[id],Dn=es[id+1],t=A*C*D;if(2*A*A>n/D)break;Dn=mn(Dn,n/(2*A*A)+1);Z wd=Dn-D,wc=Cn-C,wa=An-A;Z f=4*t-1,hi=n/(2*t-1);if(hi<((Z)1<<jmin))continue;
 Z v1=mn(3*n,n+4*(An-1)*(An-1)*(Dn-1));hi=mn(hi,v1/f);if(hi<((Z)1<<jmin))continue;int j=bits(hi)-1;int lb=lg(f,0),ub=32+he[ia+1]+he[ic+1]+he[id+1],v=lg(v1,1);Z z=cap(v,lb,wc)*wa*wd;
 // cofactor progression width via v*(w-1)/f^2, upper in bits;
 // denominator and numerator estimated by log bounds to avoid overflow.
 int vs[]={v,L+he[ic+1]+1,L+32+2*he[ic+1]+he[id+1]+1};int low[]={LL,LL+le[ic],LL+32+2*le[ic]+le[id]};Z ws[]={wc,wd,wa},ps[]={wa*wd,wa*wc,wc*wd};
 for(int m=0;m<3;m++){v=vs[m];Z p=ps[m],w=ws[m];if(p>=z)continue;z=mn(z,p*cap(v,lb,w));int h=v+lg(w,1)-2*lb;if(h>=16*116)continue;Z rev=h<0?1:((Z)1<<((h+15)/16))+1;int lf=low[m]-ub;Z back=m==1?rev:cap(v,lf,rev);if(back<=(z-1)/p)z=p*back;}
 bu[j]+=2*z;
 }}}
 for(int i=b;i>=jmin;i--)bu[i]+=bu[i+1];printf("%d %d %d",r,K,jmin);for(int j=jmin;j<=jmax;j++){putchar(' ');pr(bu[j]);}puts("");fflush(stdout);}}
