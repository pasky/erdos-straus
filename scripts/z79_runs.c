/* Aggregate entire runs along the largest fine-grid index. Reuse exact log
   and Chebyshev routines from the flat player. No fine-grid count is assumed. */
#define main flat_unused_main
#include "z79_cheb.c"
#undef main
static Z edges[512],dp[512],N;static int lN,uN;
static Z box(Z A,Z B,Z C,Z G,Z D,Z F,Z E){ // inclusive lower, exclusive upper
 Z t=A*C*D; if(2*A>N/D/A || t>(N/E+1)/2)return 0;
 F=mn(F,N/(2*A*A)+1);Z f=4*t-1;Z ad=4*(B-1)*(F-1);Z v1=(B-1)>2*N/ad?3*N:N+ad*(B-1);if(v1/f<E)return 0;
 Z hi=v1/f; if(4*A*A>(N+hi)/D)return 0;
 Z u=(N+hi)/(4*A*A)+1;F=mn(F,u); Z T=(v1/E+1)/4;if(t>T)return 0;
 F=mn(F,T/(A*C)+1);G=mn(G,T/(A*D)+1);B=mn(B,T/(C*D)+1);
 Z wa=B-A,wc=G-C,wd=F-D,nok=sf(D,wd);if(!nok)return 0;
 int la=lg(A,0),lc=lg(C,0),ld=lg(D,0),ha=lg(B-1,1),hc=lg(G-1,1),hd=lg(F-1,1);
 int lb=lg(f,0),ub=32+ha+hc+hd;
 int vs[]={lg(v1,1),uN+hc+1,uN+32+2*hc+hd+1};int lows[]={lN,lN+lc,lN+32+2*lc+ld};Z ws[]={wc,wd,wa},ps[]={wa*nok,wa*wc,wc*nok};
 Z best=wa*wc*wd; // coarse intervals have bounded ratios
 for(int m=0;m<3;m++){Z p=ps[m],w=ws[m];if(p>=best)continue;int v=vs[m];best=mn(best,p*cap(v,lb,w));if(w<2)continue;
 int h=v+lg(w-1,1)-2*lb;if(h>=16*116)continue;Z rev=h<0?1:((Z)(mant[h%16]+32)<<(h/16))/256+1;if(m==0)rev=mn(rev,(hi-E)/(4*A*D)+1);
 Z back=m==1?rev:cap(v,lows[m]-ub,rev);if(back<=(best-1)/p)best=p*back;}
 return best;
}
static Z runs(Z E,int ne){Z T=(N/E+1)/2,out=0;
 for(int m=0;m<3;m++){int n=(m+1)%3,o=(m+2)%3;
 for(int i=0;i<ne;i++){Z I=edges[i];if(I>T/I)break;for(int j=0;j<ne;j++){Z J=edges[j];int first=i+(n<m);if(j+(o<m)>first)first=j+(o<m);Z top=T/(I*J);if(edges[first]>top){if(J>=I)break;continue;}
 Z vals[3],end[3];vals[n]=I;end[n]=edges[i+1];vals[o]=J;end[o]=edges[j+1];dp[first]=0;int k;
 for(k=first;edges[k]<=top;k++){Z best=~(Z)0;end[m]=edges[k+1]; for(int d=1;d<=16&&k+1-d>=first;d*=2){int s=k+1-d;vals[m]=edges[s];Z v=box(vals[0],end[0],vals[1],end[1],vals[2],end[2],E);best=mn(best,dp[s]+v);}dp[k+1]=best;}
 out+=dp[k];}}}return 2*out;}
int main(int argc,char**argv){assert(argc==7);int r=atoi(argv[2]),K=atoi(argv[3]),step=atoi(argv[4]),j0=atoi(argv[5]),j1=atoi(argv[6]);assert(step>=2&&step<=12&&r<=283&&r>=17&&K<=17&&K>=7);
 N=1;for(int k=0;k<K;k++){assert(N<((Z)1<<121)/r);N*=r;}int b=bits(N);assert(j0>=b*3/8-4&&j1<=b/2+1&&j0<=j1);FILE *fp=fopen(argv[1],"r");assert(fp);for(int i=1;i<=512;i++)assert(fscanf(fp,"%d",lo+i)==1);fclose(fp);
 for(int i=0;i<PER;i++)pre[i+1]=pre[i]+(i%4&&i%9&&i%25&&i%49);for(int h=0;h<16;h++){int i=256;while(i<512&&lo[i]<128+h)i++;mant[h]=i==256?256:i-1;}
 memset(capk,-1,sizeof capk);lN=lg(N,0);uN=lg(N,1);
 for(int v=uN-8;v<=16*(3*b-2*j0+12);v++)for(int f=1;f<=16*(2*b-j0+12);f++)for(int i=0;i<8;i++){int l=ls[i],h=f*l/v;if(h>=l)h=l-1;int s=l*(l-1)/2,gain=16*(2*s-l+1)-((l*(lo[l]+!!(l&(l-1)))+1)/2),A=f*h*l-v*h*(h+1)/2+gain;capk[v][f][i]=A>0?(A-1)/s:-1;}
 int ne=0;edges[0]=1;Z top=(N/((Z)1<<j0)+1)/2;while(edges[ne]<=top){Z x=edges[ne];assert(ne<505);edges[++ne]=x+(x>=step?x/step:1);}edges[ne+1]=edges[ne]*2;printf("%d %d %d",r,K,j0);for(int j=j0;j<=j1;j++){putchar(' ');pr(runs((Z)1<<j,ne));}puts("");}
