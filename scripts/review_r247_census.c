/* R247 brute-force census of ALL Case B tuples of parameter s (q = 3), by direct enumeration of (m', w1, C1):
 * m' w1 C1 = T^{s-2} + v1 (deg v1 < s-2, v1 != 0), Tv1 | w1 + C1 with quotient g' monic, T-free.
 * All of m', w1, C1 monic, T-free. No Liouville / CRT input at all.  usage: review_r247_census smin smax
 * output: s m' g' w1 C1 v1   (coefficients low degree first, digits) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MX 40
static int c3(int x){x%=3;return x<0?x+3:x;}
static long cnt(int z){ if(z==0) return 1; long n=2; for(int i=1;i<z;i++) n*=3; return n; }
static void mk(int*r,int z,long idx){ memset(r,0,sizeof(int)*MX); r[z]=1; if(!z) return; r[0]=1+idx%2; idx/=2; for(int i=1;i<z;i++){r[i]=idx%3; idx/=3;} }
static void pr(const int*a,int d){ for(int i=0;i<=d;i++) putchar('0'+a[i]); }
int main(int argc,char**argv){
  int smin=atoi(argv[1]),smax=atoi(argv[2]);
  int m[MX],w[MX],C[MX],mw[MX],p[MX],v[MX],S[MX],g[MX];
  for(int s=smin;s<=smax;s++) for(int z=0;z<=s-2;z++) for(int a1=0;a1+z<=s-2;a1++){ int b1=s-2-z-a1;
    for(long i=0;i<cnt(z);i++){ mk(m,z,i);
     for(long j=0;j<cnt(a1);j++){ mk(w,a1,j);
      memset(mw,0,sizeof mw); for(int x=0;x<=z;x++) if(m[x]) for(int y=0;y<=a1;y++) mw[x+y]+=m[x]*w[y];
      for(int x=0;x<=z+a1;x++) mw[x]=c3(mw[x]);
      for(long l=0;l<cnt(b1);l++){ mk(C,b1,l);
        memset(p,0,sizeof p); for(int x=0;x<=z+a1;x++) if(mw[x]) for(int y=0;y<=b1;y++) p[x+y]+=mw[x]*C[y];
        for(int x=0;x<=s-2;x++) p[x]=c3(p[x]);
        /* v1 = p - T^{s-2} */
        memcpy(v,p,sizeof v); v[s-2]=0; int dv=s-3; while(dv>=0&&!v[dv]) dv--; if(dv<0) continue;
        /* S = w1 + C1 */
        memset(S,0,sizeof S); for(int x=0;x<=a1;x++) S[x]+=w[x]; for(int x=0;x<=b1;x++) S[x]=c3(S[x]+C[x]);
        int dS=(a1>b1?a1:b1); while(dS>=0&&!S[dS]) dS--;
        /* divide S by T*v1: need S[0]==0, then S/T divided by v1 exactly */
        if(dS<0||S[0]) continue; int Q[MX]; memset(Q,0,sizeof Q); int R[MX]; memcpy(R,S+1,sizeof(int)*(MX-1)); R[MX-1]=0; int dR=dS-1;
        if(dR<dv) continue; int il=(v[dv]==1)?1:2; int ok=1;
        for(int e=dR;e>=dv;e--){ int f=c3(R[e]*il); Q[e-dv]=f; for(int x=0;x<=dv;x++) R[e-dv+x]=c3(R[e-dv+x]-f*v[x]); }
        for(int x=0;x<dv;x++) if(R[x]) ok=0; if(!ok) continue;
        int dg=dR-dv; if(Q[dg]!=1||Q[0]==0) continue;
        memcpy(g,Q,sizeof g);
        printf("%d ",s); pr(m,z); putchar(' '); pr(g,dg); putchar(' '); pr(w,a1); putchar(' '); pr(C,b1); putchar(' '); pr(v,dv); putchar('\n');
      }}}}
  return 0;
}
