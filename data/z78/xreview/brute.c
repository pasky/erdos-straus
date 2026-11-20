/* Independent brute enumerator (Opus cross-review of notes/z78/F3_CONJ.md).
   Plain int8 coefficient arrays; shares no code with scripts/z78_f3*.c.
   Enumerates (m', w1, C1) monic T-units with deg m'+deg w1+deg C1 = n, subject only to
   w1 + u C1 == 0 mod T^Kt (FF_THIRDS_CORNER Lemma 3.1), Kt = ceil((n+1)/2), u = 1+cT.
   The short side and m' are enumerated freely; the long side is fixed mod T^Kt and its
   higher digits are enumerated freely (no quotient/remainder shortcut).
   Outputs: (1) every genuine tuple (v1 != 0, T v1 | w1+C1, g' monic T-unit) with its depth;
            (2) per (N,s,c,orientation) the stage counts of z78_f3 (monicV, vbound, integralG)
                and z78_f3_hybrid (near), recomputed from scratch.
   usage: brute nlo nhi allpatterns(0/1)                                                     */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MD 128
typedef struct { int d; signed char c[MD]; } Poly;
static void norm(Poly *p){ while(p->d>=0 && p->c[p->d]==0) p->d--; }
static Poly zero(void){ Poly p; memset(&p,0,sizeof p); p.d=-1; return p; }
static Poly mul(const Poly *a,const Poly *b){ Poly r=zero(); if(a->d<0||b->d<0) return r;
  r.d=a->d+b->d; for(int i=0;i<=a->d;i++) if(a->c[i]) for(int j=0;j<=b->d;j++) r.c[i+j]=(r.c[i+j]+a->c[i]*b->c[j])%3; norm(&r); return r; }
static Poly addp(const Poly *a,const Poly *b,int sb){ Poly r=zero(); int D=a->d>b->d?a->d:b->d; r.d=D;
  for(int i=0;i<=D;i++){ int x=(i<=a->d?a->c[i]:0)+sb*(i<=b->d?b->c[i]:0); x%=3; if(x<0)x+=3; r.c[i]=x; } norm(&r); return r; }
static int inv3(int x){ return x==1?1:2; }
/* a = q*b + rem */
static Poly divmodp(Poly a,const Poly *b,Poly *q){ Poly Q=zero(); int il=inv3(b->c[b->d]);
  if(a.d>=b->d) Q.d=a.d-b->d;
  while(a.d>=b->d){ int s=a.d-b->d, f=(a.c[a.d]*il)%3; Q.c[s]=f;
    for(int i=0;i<=b->d;i++) a.c[i+s]=((a.c[i+s]-f*b->c[i])%3+3)%3; norm(&a); }
  norm(&Q); if(q) *q=Q; return a; }
static int valT(const Poly *p){ if(p->d<0) return 1000; int i=0; while(p->c[i]==0) i++; return i; }
static Poly Tpow(int n){ Poly p=zero(); p.d=n; p.c[n]=1; return p; }
static void pr(FILE *f,const Poly *p){ if(p->d<0){fputc('0',f);return;} for(int i=0;i<=p->d;i++) fputc('0'+p->c[i],f); }
/* iterate monic T-units of degree e: returns 0 when exhausted */
static void first_unit(Poly *p,int e){ *p=zero(); p->d=e; p->c[e]=1; if(e>0) p->c[0]=1; }
static int next_unit(Poly *p){ int e=p->d; if(e==0) return 0;
  for(int i=0;i<e;i++){ if(i==0){ if(p->c[0]==1){p->c[0]=2;return 1;} p->c[0]=1; }
    else { if(p->c[i]<2){p->c[i]++;return 1;} p->c[i]=0; } } return 0; }

typedef struct { long long monicV, vb[2], ig[2], near, hit, deepNonLop; } Row;
static FILE *tf;
int main(int argc,char**argv){
  int nlo=atoi(argv[1]), nhi=atoi(argv[2]), allp=atoi(argv[3]);
  tf=fopen(argc>4?argv[4]:"tuples.txt","w");
  for(int n=nlo;n<=nhi;n++) for(int c=1;c<=2;c++){
    int N=(n%2)?(n+3)/2:(n+2)/2, K=N+1, Kt=(n+2)/2;
    Poly u=zero(); u.d=1; u.c[0]=1; u.c[1]=c;
    Poly ui=zero(); ui.d=MD-1; { int pw=1; for(int i=0;i<MD;i++){ ui.c[i]=pw; pw=(pw*(3-c))%3; } } norm(&ui); /* 1/(1+cT)=sum (-c)^i T^i */
    Row R[2]; memset(R,0,sizeof R); long long cand=0, genuine=0;
    Poly Tn=Tpow(n);
    for(int z=0;z<=n;z++) for(int a1=0;a1+z<=n;a1++){ int b1=n-z-a1;
      int mx=a1>b1?a1:b1, mn=a1>b1?b1:a1, shortw = (a1<=b1);
      if(!allp && mx < Kt-1) continue;
      Poly m; first_unit(&m,z);
      do { Poly S; first_unit(&S,mn);
        do { Poly MS=mul(&m,&S);
          /* long side mod T^Kt */
          Poly base = shortw ? mul(&S,&ui) : mul(&S,&u); /* long == -base */
          Poly Lg=zero(); int ok=1;
          if(mx<Kt){ for(int i=0;i<Kt;i++){ int x=(i<=base.d)?(3-base.c[i])%3:0; if(i>mx && x){ok=0;break;} if(i<=mx) Lg.c[i]=x; }
            Lg.d=mx; if(ok && Lg.c[mx]!=1) ok=0; if(!ok) continue; }
          else { for(int i=0;i<Kt;i++) Lg.c[i]=(i<=base.d)?(3-base.c[i])%3:0; Lg.d=mx; Lg.c[mx]=1; }
          int nfree = mx>=Kt ? mx-Kt : 0;
          for(int i=Kt;i<mx;i++) Lg.c[i]=0;
          for(;;){
            cand++;
            /* early abort: coefficients of MS*Lg at degrees n-1..mx must vanish */
            int bad=0; for(int k=n-1;k>=mx && !bad;k--){ int s=0; for(int i=0;i<=MS.d;i++){ int j=k-i; if(j>=0&&j<=mx) s+=MS.c[i]*Lg.c[j]; } if(s%3) bad=1; }
            if(!bad){
              Poly w1 = shortw?S:Lg, C1 = shortw?Lg:S;
              Poly P=mul(&MS,&Lg), V=addp(&P,&Tn,-1);
              Poly sum=addp(&w1,&C1,1);
              Poly uC=mul(&u,&C1), cov=addp(&w1,&uC,1); int dep=valT(&cov);
              /* genuine tuple? */
              if(V.d>=0 && V.c[0]){ Poly TV=zero(); TV.d=V.d+1; for(int i=0;i<=V.d;i++) TV.c[i+1]=V.c[i];
                Poly g; Poly rem=divmodp(sum,&TV,&g);
                if(rem.d<0 && g.d>=0 && g.c[g.d]==1 && g.c[0]){ genuine++;
                  Poly mg=mul(&m,&g), mgw=mul(&mg,&w1); Poly E=zero(); E.d=mgw.d+1; for(int i=0;i<=mgw.d;i++) E.c[i+1]=mgw.c[i]; E.c[0]=2; norm(&E);
                  Poly Eu=addp(&E,&u,1); int depE=valT(&Eu);
                  fprintf(tf,"n=%d c=%d N=%d z=%d a1=%d b1=%d dep=%d depE=%d m=",n,c,N,z,a1,b1,dep,depE); pr(tf,&m); fprintf(tf," w=");pr(tf,&w1);fprintf(tf," C=");pr(tf,&C1);fprintf(tf," g=");pr(tf,&g);fprintf(tf," V=");pr(tf,&V);fputc('\n',tf);
                  if(depE>=K){ int o=(b1>=N)?0:((a1>=N+1)?1:-1); if(o>=0) R[o].hit++; else R[0].deepNonLop+=1000000; }
                }}
              if(dep>=K){
                int o=(b1>=N)?0:((a1>=N+1)?1:-1);
                if(o<0) R[0].deepNonLop++;
                else { Poly X=o?C1:w1, B=o?w1:C1; int P_=o, r=X.d, L=B.d, d=z+r;
                  int patf3 = ((z-n)%2==0) && (d+r+P_>=K) && (2*d+P_>=K);
                  int j=d+r+P_-K; int pathy = ((z-n)%2==0) && j>=0 && (N-d<=r+2*P_-1) && (2*d+P_>=K);
                  int v=V.d; int Vok = v>=0 && V.c[0] && V.c[v]==1 && v<L;
                  if(patf3 && Vok){ R[o].monicV++;
                    if(v<=n-N-1+P_ && (v-n)%2==0){ int c2=(L-1-v>=N); R[o].vb[c2]++;
                      Poly TV=zero(); TV.d=v+1; for(int i=0;i<=v;i++) TV.c[i+1]=V.c[i]; Poly XB=addp(&X,&B,1); Poly rm=divmodp(XB,&TV,NULL); if(rm.d<0) R[o].ig[c2]++; } }
                  if(pathy && Vok && v>=N-d && v<=r+2*P_-1 && (v-n)%2==0) R[o].near++;
                }
              }
            }
            /* next free digits */
            int i; for(i=Kt;i<Kt+nfree;i++){ if(Lg.c[i]<2){Lg.c[i]++;break;} Lg.c[i]=0; }
            if(i==Kt+nfree) break;
          }
        } while(next_unit(&S));
      } while(next_unit(&m));
    }
    for(int o=0;o<2;o++) printf("N=%d s=%d c=%d orient=%c monicV=%lld vb1=%lld vb2=%lld ig1=%lld ig2=%lld near=%lld hits=%lld deepNonLop=%lld cand=%lld genuine=%lld\n",N,n+2,c,'A'+o,R[o].monicV,R[o].vb[0],R[o].vb[1],R[o].ig[0],R[o].ig[1],R[o].near,R[o].hit,o?0:R[0].deepNonLop,cand,genuine);
    fflush(stdout);
  }
  fclose(tf); return 0; }
