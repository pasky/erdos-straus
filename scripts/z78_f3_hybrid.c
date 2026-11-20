/* Additional exhaustive quotient-lift engine. See F3_CONJ sections 3 and 4.
   gcc -O3 -std=gnu11 scripts/z78_f3_hybrid.c -o data/z78/hyb && data/z78/hyb N0 N1 [c]
   counts in this log are not the same stages as z78_f3.c. */
#define WIDE
#define main f3_unused_main
#include "z78_f3.c"
#undef main
static inline int eq(P a,P b){return a.a==b.a && a.b==b.b;}
static inline P scale(P a,int c){return c==1?a:neg(a);}
typedef struct{int N,K,n,ori,c,d,r; P u,p,q,Tn;U total[2],pool,split,near,hit;int gd,rd;P gm,gx,gb,rm,rx,rb;} Ctx;
static void test(Ctx *t,P H,P M,P X){
 int r=t->r,z=t->d-r;P m,B,g;
 if(deg(X)!=r || cf(X,r)!=1 || !cf(X,0) || !cf(M,0))return;
 if(deg(divr(M,X,&m))>=0 || deg(m)!=z || cf(m,z)!=1)return;
 B=sub(sh(H,t->K),mul(t->p,X));if(!t->ori && deg(divr(B,t->q,&B))>=0)return;
 if(deg(B)!=t->n-t->d || cf(B,deg(B))!=1 || !cf(B,0))return;
 P V=sub(mul(M,B),t->Tn);int v=deg(V);t->split++;
 if(v<t->N-t->d || v>r+2*t->ori-1 || (v^t->n)&1 || cf(V,v)!=1 || !cf(V,0))return;
 P sum=add(X,B),Tv=sh(V,1),rem=divr(sum,Tv,&g);int gd=deg(gcdp(rem,Tv)),rd=deg(rem);
 if(gd>t->gd){t->gd=gd;t->gm=m;t->gx=X;t->gb=B;}if(rd<t->rd){t->rd=rd;t->rm=m;t->rx=X;t->rb=B;}t->near++;
 if(rd>=0 || !cf(g,0) || cf(g,deg(g))!=1)return;
 P w=t->ori?B:X, C=t->ori?X:B, E=sub(sh(mul(mul(m,g),w),1),one), check=add(E,t->u);
 if((check.a|check.b)&(((Bits)1<<t->K)-1))return;
 t->hit++;printf("HIT N=%d s=%d ori=%d c=%d m,g,w,C,V=",t->N,t->n+2,t->ori,t->c);pr(m);putchar('/');pr(g);putchar('/');pr(w);putchar('/');pr(C);putchar('/');pr(V);puts("");
}
static void loop(int N,int n,int ori,int c){int dp=ori,dq=1-ori,K=N+1,b=n-K;
 Ctx t={.N=N,.n=n,.K=K,.ori=ori,.c=c,.gd=-1,.rd=99};P u=add(one,sh(unit(c),1)),p=dp?u:one,q=dq?u:one,rhs=sh(q,n),Tbq=sh(q,b);t.p=p;t.q=q;t.u=u;t.Tn=sh(one,n);
 for(int d=0;d<=b+dq;d++){int h=b+dq-d;if(2*d+dp<K)continue;t.pool+=d?2*three[d-1]:1;t.d=d;
 for(int r=0;r<=d;r++){int z=d-r,j=d+r+dp-K;if(j<0 || ((z^n)&1) || N-d>r+2*dp-1)continue;t.r=r;
 int shorter=z<r?z:r,route=(j>h?j:h)<=h+shorter;
 P H=sh(unit(dq?c:1),h);for(U k=0;k<three[h];k++,H=inc(H,h)){
 if(route){/* qT^b+J=MH, lc J=lc p. Free part of J/H fills the high digits. */
 P M0,J0=neg(divr(Tbq,H,&M0));int e=j-h,jlc=dp?c:1;
 if(e<0 && (deg(J0)!=j || cf(J0,j)!=jlc))continue;
 P D=e<0?zero:sh(unit(jlc*(dq?c:1)%3),e);int countdeg=e<0?0:e;
 for(U i=0;i<three[countdeg];i++,D=inc(D,countdeg)){P M=add(M0,D),J=add(J0,mul(H,D));t.total[1]++;if(!cf(M,0))continue;
 P X=M;if(z){/* qV has degree < deg(pM) if z>0 by section 3. */ divr(sh(J,K),mul(p,M),&X);}
 test(&t,H,M,X);
 }}else{P A=sh(H,K),known=sh(one,shorter);for(U i=0;i<three[shorter];i++,known=inc(known,shorter)){if(!cf(known,0))continue;t.total[0]++;
 P X=known,M;if(z<r){P mp=mul(known,p),lin=neg(mul(known,A)),R=rhs;X=zero;
 for(int l=r;l>=0;l--){int v=cf(R,z+K+h+l);if(!v)continue;int e=v*(dq?c:1)%3;X=add(X,sh(unit(e),l));R=add(R,sh(scale(lin,e),l));R=add(R,sh(mp,2*l));lin=sub(lin,sh(scale(mp,e),l));}M=mul(known,X);
 }else{P B=sub(A,mul(p,X));if(dq && deg(divr(B,q,&B))>=0)continue;divr(t.Tn,B,&M);}test(&t,H,M,X);
 }} }} }
 printf("N=%d s=%d c=%d orient=%c Mpool=%"PRIu64" factorTrials=%"PRIu64" liftTrials=%"PRIu64" split=%"PRIu64" near=%"PRIu64" hits=%"PRIu64" maxGcd=%d minRem=%d gcdWitness=",N,n+2,c,'A'+ori,t.pool,t.total[0],t.total[1],t.split,t.near,t.hit,t.gd,t.rd);pr(t.gm);putchar('/');pr(t.gx);putchar('/');pr(t.gb);printf(" remWitness=");pr(t.rm);putchar('/');pr(t.rx);putchar('/');pr(t.rb);puts("");fflush(stdout);
}
int main(int argc,char**argv){if(argc<3)return 1;int lo=atoi(argv[1]),hi=atoi(argv[2]),c0=argc>3?atoi(argv[3]):0;if(lo<4||hi>40||lo>hi||c0<0||c0>2)return 2;three[0]=1;for(int j=1;j<=40;j++)three[j]=3*three[j-1];for(int N=lo;N<=hi;N++)for(int n=2*N-3;n<=2*N-2;n++)for(int o=0;o<2;o++)for(int c=1;c<=2;c++)if(!c0||c0==c)loop(N,n,o,c);return 0;}
