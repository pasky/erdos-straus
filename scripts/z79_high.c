/* Half-octave P grid for N in [2^(B-1),2^B], large B. Integer upper
   costs c*2^e, logs in sixteenths, Chebyshev gains via verified log16. */
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <gmp.h>
static int ls[]={2,3,4,5,6,8,12,16,24},lo[1024];static short caps[10000][9];
static int low[800],hi[800],wid[800],ne;static uint64_t hist[370][370];
static int mn(int a,int b){return a<b?a:b;}static int mx(int a,int b){return a>b?a:b;}
static int lgplus(int x,int y){int z=mx(x,y),d=abs(x-y);return z+(d>=80?1:d>=48?3:d>=32?6:d>=16?10:16);}
static int bestE,bestC;
static void opt(int c,int e){if(e-bestE>10)return;if(e+10<bestE||(e>=bestE?c<<(e-bestE)<bestC:c<bestC<<(bestE-e))){bestE=e;bestC=c;}}
static void cap(int v,int f,int w,int pp){opt(1,w+pp);if(w<=0||f<=0)return;
 for(int i=0;i<9;i++){int l=ls[i],h=mn(l-1,l*f/v),s=l*(l-1)/2, gain=16*(2*s-l+1)-(l*(lo[l]+!!(l&(l-1)))+1)/2;
 int a=f*h*l-v*h*(h+1)/2+gain;if(a<=0)continue;int k=(a-1)/(16*s);opt(l-1,pp+mx(0,w-k));}}
int main(int argc,char**argv){assert(argc==4);FILE*fp=fopen(argv[1],"r");assert(fp);for(int i=1;i<=512;i++)assert(fscanf(fp,"%d",lo+i)==1);fclose(fp);
 for(int B=atoi(argv[2]);B<=atoi(argv[3]);B++){assert(B>=80&&B<=320);memset(hist,0,sizeof hist);ne=1;low[0]=hi[0]=wid[0]=0;int jmin=B*3/8-4,jmax=B/2;
 for(int x=1;x<=B-jmin;x++){low[ne]=16*x;hi[ne]=16*x+10;wid[ne++]=x-1;low[ne]=16*x+9;hi[ne]=16*x+16;wid[ne++]=x-1;}
 for(int i=0;i<ne;i++){int a=low[i],A=hi[i];if(2*a+16>16*B)break;for(int h=0;h<ne;h++){int c=low[h],C=hi[h];if(a+c>16*(B-jmin))break;
 for(int t=0;t<ne;t++){int d=low[t],D=hi[t],s=a+c+d;if(s>16*(B-jmin)||2*a+d+16>16*B)break;
 int lb=s+(s>=48?31:25),ub=32+A+C+D;int v=mn(16*B+26,lgplus(16*B,32+2*A+D));int j=mn(B,(v-lb)/16);if(j<jmin)continue;
 int w[]={wid[h],wid[t],wid[i]},pp[]={wid[i]+wid[t],wid[i]+wid[h],wid[h]+wid[t]};int vs[]={v,lgplus(16*B+C,A),lgplus(32+2*C+D+16*B,0)};int ls0[]={16*(B-1),16*(B-1)+c,32+2*c+d+16*(B-1)};
 bestC=1;bestE=wid[i]+wid[h]+wid[t];for(int m=0;m<3;m++){if(pp[m]>bestE+5)continue;cap(vs[m],lb,w[m],pp[m]);int dif=vs[m]+16*w[m]-2*lb;
 // Strict width: w indices, diameter < w; reverse width <= ceil(V*w/f^2).
 int wr=mx(0,(dif+15)/16);if(m!=1)cap(vs[m],ls0[m]-ub,wr,pp[m]);else opt(1,pp[m]+wr);}
 assert(bestE<370);hist[j][bestE]+=2*bestC;
 }}}
 mpz_t z;mpz_init(z);for(int j=B;j>=jmin;j--){for(int e=0;e<=B;e++)hist[j][e]+=hist[j+1][e];if(j<=jmax){mpz_set_ui(z,0);for(int e=B;e>=0;e--){mpz_mul_2exp(z,z,1);mpz_add_ui(z,z,hist[j][e]);}printf("%d %d ",B,j);mpz_out_str(stdout,10,z);puts("");}}mpz_clear(z);fflush(stdout);}}
