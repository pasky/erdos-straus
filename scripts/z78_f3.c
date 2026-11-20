/* z78 F3 quotient + short factor enumeration; see notes/z78/F3_CONJ.md.
   gcc -O3 -std=gnu11 scripts/z78_f3.c -o data/z78/f3; f3 Nlo Nhi [c].
   Unsigned bit planes for disjoint coefficients +1,-1. Terms used in divisions fit;
   only the low K coefficients of the final E are needed. WIDE uses 128-bit planes.
*/
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <inttypes.h>
#include <assert.h>
typedef uint64_t U;
#ifdef WIDE
typedef __uint128_t Bits;
static int topbit(Bits x){return x>>64 ? 127-__builtin_clzll(x>>64) : 63-__builtin_clzll((U)x);}
static int lowbit(Bits x){return (U)x?__builtin_ctzll((U)x):64+__builtin_ctzll(x>>64);}
#else
typedef U Bits;
static int topbit(Bits x){return 63-__builtin_clzll(x);}
static int lowbit(Bits x){return __builtin_ctzll(x);}
#endif
typedef struct {Bits a,b;} P;
static const P one={1,0},zero={0,0};
static P neg(P f){return (P){f.b,f.a};}
static P add(P f,P g){Bits x=~(f.a|f.b), y=~(g.a|g.b);return(P){(x&g.a)|(y&f.a)|(f.b&g.b),(x&g.b)|(y&f.b)|(f.a&g.a)};}
static P sub(P f,P g){return add(f,neg(g));}
static P sh(P f,int j){return(P){f.a<<j,f.b<<j};}
static int deg(P f){return f.a|f.b?topbit(f.a|f.b):-1;}
static int cf(P f,int j){return ((f.a>>j)&1)+2*((f.b>>j)&1);}
static P unit(int c){return c==1?one:neg(one);}
static P mul(P f,P g){P r=zero;while(g.a){r=add(r,sh(f,lowbit(g.a)));g.a&=g.a-1;}while(g.b){r=sub(r,sh(f,lowbit(g.b)));g.b&=g.b-1;}return r;}
static P divr(P f,P g,P *out){int k=deg(g),i;assert(k>=0);P Q=zero;int flip=cf(g,k)==2;if(flip)g=neg(g);while((i=deg(f)-k)>=0){P t=sh(g,i);if(cf(f,k+i)==1){Q.a|=(Bits)1<<i;f=sub(f,t);}else{Q.b|=(Bits)1<<i;f=add(f,t);}}if(out)*out=flip?neg(Q):Q;return f;}
static P gcdp(P a,P b){while(deg(b)>=0){P t=divr(a,b,NULL);a=b;b=t;}return a;}
static P inc(P f,int k){/* increment k low ternary digits */Bits mask=((Bits)1<<k)-1, t=~f.b & mask;if(!t){f.a&=~mask;f.b&=~mask;return f;}Bits bit=t&-t, carry=bit-1,was=f.a&bit;f.b=(f.b&~carry)|was;f.a^=bit;return f;}
static U three[41];
static void pr(P f){for(int j=0;j<=deg(f);j++)printf("%d",cf(f,j));}
typedef struct{U trial,unitX,intB,split,unitV,bound[2],rem[2],hit[2];int gd[2],rd[2];P wm[2],wx[2],wb[2],vm[2],vx[2],vb[2];} Stat;
static void run(int N,int n,int ori,int c){int K=N+1,dp=ori,dq=1-ori;P u=add(one,sh(unit(c),1)),p=dp?u:one,q=dq?u:one,Tn=sh(one,n),rhs=sh(q,n);Stat S={.rd={99,99},.gd={-1,-1}};U initial=0;
 for(int d=0;d<=n+dq-K;d++){int L=n-d,h=L+dq-K;if(2*d+dp<K)continue;initial+=d?2*three[d-1]:1;
 for(int r=0;r<=d;r++){int z=d-r;if(d+r+dp<K || ((z^n)&1))continue;
 P H=sh(unit(dq?c:1),h);for(U j=0;j<three[h];j++,H=inc(H,h)){P A=sh(H,K);int usem=z<r,b=usem?z:r;
 P known=sh(one,b);for(U i=0;i<three[b];i++,known=inc(known,b)){if(!cf(known,0))continue;S.trial++;P X=known,B,M,m=known;
 if(usem){/* residual rhs - m*X*(A-pX), linear coefficient -m*A+2mpX */
 P mp=mul(m,p),lin=neg(mul(m,A)),R=rhs;X=zero;
 for(int l=r;l>=0;l--){int at=z+K+h+l,v=cf(R,at);if(!v)continue;P e=unit(v*(dq?c:1)%3);X=add(X,sh(e,l));R=add(R,sh(e.a?lin:neg(lin),l));R=add(R,sh(mp,2*l));lin=sub(lin,sh(e.a?mp:neg(mp),l));}
 if(!cf(X,0))continue;
 }
 S.unitX++;B=sub(A,mul(p,X));if(dq && deg(divr(B,q,&B))>=0)continue;S.intB++;if(deg(B)!=L || !cf(B,0))continue;
 P V=neg(divr(Tn,B,&M));if(usem){P test=sub(M,mul(m,X));if(deg(test)>=0)continue;}else if(deg(divr(M,X,&m))>=0)continue;
 S.split++;int v=deg(V);if(v<0||!cf(V,0)||cf(V,v)!=1)continue;S.unitV++;int y=L-1-v,case2=y>=N;if(v>n-N-(ori?0:1)||((v^n)&1))continue;S.bound[case2]++;
 P g,Tv=sh(V,1),sum=add(X,B),rem=divr(sum,Tv,&g);int gd=deg(gcdp(rem,Tv)),rd=deg(rem);if(gd>S.gd[case2]){S.gd[case2]=gd;S.wm[case2]=m;S.wx[case2]=X;S.wb[case2]=B;}if(rd<S.rd[case2]){S.rd[case2]=rd;S.vm[case2]=m;S.vx[case2]=X;S.vb[case2]=B;}if(rd>=0)continue;S.rem[case2]++;
 if(!cf(g,0)||cf(g,deg(g))!=1)continue;
 P w=ori?B:X, C=ori?X:B,E= sub(sh(mul(mul(m,g),w),1),one);P chk=add(E,u);U mask=((U)1<<K)-1;if((chk.a|chk.b)&mask)continue;assert(deg(sub(mul(M,B),add(Tn,V)))<0 && deg(sub(sum,mul(Tv,g)))<0);printf("HIT m,g,w,C,V=");pr(m);putchar(',');pr(g);putchar(',');pr(w);putchar(',');pr(C);putchar(',');pr(V);puts("");S.hit[case2]++;
 }}}}
 printf("N=%d s=%d c=%d orient=%c Mpool=%"PRIu64" trials=%"PRIu64" unitX=%"PRIu64" intB=%"PRIu64" split=%"PRIu64" monicV=%"PRIu64,N,n+2,c,'A'+ori,initial,S.trial,S.unitX,S.intB,S.split,S.unitV);
 for(int k=0;k<2;k++){printf(" case%d[vbound=%"PRIu64" integralG=%"PRIu64" hits=%"PRIu64" maxGcd=%d minRem=%d gcdWitness=",k+1,S.bound[k],S.rem[k],S.hit[k],S.gd[k],S.rd[k]);pr(S.wm[k]);putchar('/');pr(S.wx[k]);putchar('/');pr(S.wb[k]);printf(" remWitness=");pr(S.vm[k]);putchar('/');pr(S.vx[k]);putchar('/');pr(S.vb[k]);putchar(']');}puts("");fflush(stdout);
}
int main(int argc,char**argv){if(argc<3)return 1;int lo=atoi(argv[1]),hi=atoi(argv[2]),fix=argc>3?atoi(argv[3]):0;if(lo<4||hi>31||lo>hi||fix<0||fix>2)return 2;three[0]=1;for(int j=1;j<34;j++)three[j]=three[j-1]*3;for(int N=lo;N<=hi;N++)for(int n=2*N-3;n<=2*N-2;n++)for(int o=0;o<2;o++)for(int c=1;c<=2;c++)if(!fix||fix==c)run(N,n,o,c);return 0;}
