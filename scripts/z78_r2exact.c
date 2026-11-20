/* z78 cross-review (Opus), independent of the author engines.
   EXACT nonsquare union through depth 3 on the r-generic line for one prime r:
   L1 = P1 u Q1 (mod r), P3 (K=3, mod r^2), Q3 (k=3, mod r^3), P5 (K=5, mod r^3).
   Own splits (different from the author's): P3 e<4*ceil(sqrt N); P5 e<16 r^2;
   Q3 e<2r^2 / f<2r^2 / both large.  Factorisation by trial division + Pollard-
   Brent + deterministic Miller-Rabin (no sieve shared with author code).
   Also prints cumulative counts of DISTINCT oriented P5 centres (all digits) and
   of distinct ALIVE-digit P5 centres from shifts e < r^2 2^j, j=0..4, and the
   per-shift sum of distinct centres, for comparison with p5/p5fine columns.
   Usage: z78_xr_exact r      (r prime, 17<=r<=1600). Memory ~ r^3/4 bytes. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
typedef uint64_t U; typedef __uint128_t Z; typedef int64_t I;
static U mulm(U a,U b,U m){return (Z)a*b%m;}
static U powm(U a,U e,U m){U t=1;a%=m;while(e){if(e&1)t=mulm(t,a,m);a=mulm(a,a,m);e>>=1;}return t;}
static int mr(U n){if(n<2)return 0;static const U B[]={2,3,5,7,11,13,17,19,23,29,31,37};
 for(int i=0;i<12;i++){if(n%B[i]==0)return n==B[i];}
 U d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
 for(int i=0;i<12;i++){U x=powm(B[i],d,n);if(x==1||x==n-1)continue;int ok=0;for(int k=1;k<s;k++){x=mulm(x,x,n);if(x==n-1){ok=1;break;}}if(!ok)return 0;}
 return 1;}
static U gcdu(U a,U b){while(b){U t=a%b;a=b;b=t;}return a;}
static U rho(U n){if(n%2==0)return 2;for(U c=1;;c++){U y=2,x,g=1,q=1,ys=0;U m=128,rr=1;
 do{x=y;for(U i=0;i<rr;i++)y=(mulm(y,y,n)+c)%n;U k=0;
  do{ys=y;for(U i=0;i<m&&i<rr-k;i++){y=(mulm(y,y,n)+c)%n;q=mulm(q,x>y?x-y:y-x,n);}g=gcdu(q,n);k+=m;}while(k<rr&&g==1);rr*=2;}while(g==1);
 if(g==n){do{ys=(mulm(ys,ys,n)+c)%n;g=gcdu(x>ys?x-ys:ys-x,n);}while(g==1);}
 if(g!=n)return g;}}
static U fp[64];static int fe[64],nfp;
static void addp(U p){for(int i=0;i<nfp;i++)if(fp[i]==p){fe[i]++;return;}fp[nfp]=p;fe[nfp++]=1;}
static void fac(U n){if(n==1)return;if(mr(n)){addp(n);return;}U d=rho(n);fac(d);fac(n/d);}
static void factor(U n){nfp=0;for(U p=2;p<200&&p*p<=n;p++){while(n%p==0){addp(p);n/=p;}}if(n>1)fac(n);}

typedef struct { U *v; size_t cap,n; } Set;
static U shash(U x){x^=x>>30;x*=UINT64_C(0xbf58476d1ce4e5b9);x^=x>>27;x*=UINT64_C(0x94d049bb133111eb);return x^(x>>31);}
static void sgrow(Set*s){size_t nc=s->cap?2*s->cap:1024;U *nv=calloc(nc,sizeof(U));assert(nv);for(size_t i=0;i<s->cap;i++)if(s->v[i]){size_t k=shash(s->v[i])&(nc-1);while(nv[k])k=(k+1)&(nc-1);nv[k]=s->v[i];}free(s->v);s->v=nv;s->cap=nc;}
static int shas(Set*s,U x){assert(x!=0);if(!s->cap)return 0;size_t k=shash(x)&(s->cap-1);while(s->v[k]){if(s->v[k]==x)return 1;k=(k+1)&(s->cap-1);}return 0;}
static int sadd(Set*s,U x){assert(x!=0);if(!s->cap||10*(s->n+1)>7*s->cap)sgrow(s);size_t k=shash(x)&(s->cap-1);while(s->v[k]){if(s->v[k]==x)return 0;k=(k+1)&(s->cap-1);}s->v[k]=x;s->n++;return 1;}
static U r,R2,R3;static unsigned char *alive1,*sq;static Set cov2={0},cov3={0},q3only={0},p5only={0};static U inv_mod(U a,U m){I t=0,nt=1;I rr=m,nr=a%m;while(nr){I q=rr/nr,x;x=t-q*nt;t=nt;nt=x;x=rr-q*nr;rr=nr;nr=x;}assert(rr==1);return t<0?t+m:t;}
static U cen(U a,U b,U W){return (W-mulm(a%W,inv_mod(b%W,W),W))%W;} 

/* ---- level 1 ---- */
static U l1;static Set l1cov={0};
static void mark1(U x){x%=r;if(x)sadd(&l1cov,x);}
static void level1(void){U N=r;
 for(U a=1;2*a*a<=N;a++)for(U d=1;2*a*a*d<=N;d++){U V=N+4*a*a*d;for(U c=1;4*a*c*d-1<=V;c++){U f=4*a*c*d-1;if(V%f)continue;U e=V/f;if(c*e<2*a)continue;U b=c*e-a;
  if(a%r&&b%r&&c%r&&d%r){mark1(cen(a,b,r));mark1(cen(b,a,r));}}}
 U F=r;for(U a=1;a<=(F+1)/2;a++)for(U d=1;a*d<=(F+1)/2;d++)for(U c=1;a*c*d<=(F+1)/2;c++){if(4*a*c*d<=F)continue;U f=4*a*c*d-F,V=4*a*a*d+1;if(V%f)continue;U e=V/f;if(c*e<2*a)continue;U b=c*e-a;
  if(c%r&&e%r){assert((Z)4*a*b*d==(Z)e*F+1);mark1(cen(a,b,r));mark1(cen(b,a,r));}}
}
/* ---- generic triple enumeration of M = x*y*z with callback ---- */
static int nP;static U Pp[64];static int Pe[64];
typedef void(*cb_t)(U,U,U);
static void rec3(int i,U x,U y,U M,cb_t cb){if(i==nP){cb(x,y,M/(x*y));return;}
 U px=1;for(int u=0;u<=Pe[i];u++){U py=1;for(int v=0;v<=Pe[i]-u;v++){rec3(i+1,x*px,y*py,M,cb);py*=Pp[i];}px*=Pp[i];}}
static void triples(U M,cb_t cb){factor(M);nP=nfp;for(int i=0;i<nP;i++){Pp[i]=fp[i];Pe[i]=fe[i];}rec3(0,1,1,M,cb);}

/* ---- P3 ---- */
static U Ncur,Ecur,p3dist,p3data;
static void p3hit(U a,U b,U c,U d){if(a%r==0||b%r==0||c%r==0||d%r==0)return;p3data++;
 U x[2]={cen(a,b,R2),cen(b,a,R2)};for(int i=0;i<2;i++){if(!alive1[x[i]%r])continue;if(sadd(&cov2,x[i]))p3dist++;}}
static void p3cb(U a,U b,U d){if(a>b)return;U s=a+b;if(s%Ecur)return;p3hit(a,b,s/Ecur,d);}
static void PK_large(U N,U E,void(*hit)(U,U,U,U)){U T=(N/E+1)/2;
 for(U a=1;a<=T&&2*a*a<=N;a++)for(U d=1;a*d<=T&&2*a*a*d<=N;d++){U V=N+4*a*a*d;U u=4*a*d;for(U c=1;c<=T/(a*d);c++){U f=u*c-1;if(V%f)continue;U e=V/f;if(e<E||c*e<2*a)continue;
   U b=c*e-a;assert((Z)4*a*b*d==(Z)N+e);hit(a,b,c,d);}}}
static void P3(void){U N=R3;U E=1;while(E*E<N)E++;E*=4;Ncur=N;
 for(U e=1;e<E;e++){if((N+e)%4||e%r==0)continue;Ecur=e;triples((N+e)/4,p3cb);}
 PK_large(N,E,p3hit);}
/* ---- Q3 ---- */
static U q3marg,q3data,q3small_e,q3small_f,q3large;static U F3,E0,T0;
static void q3hit(U a,U b,U c,U d,U e){if(c%r==0||e%r==0)return;q3data++;
 U x[2]={cen(a,b,R3),cen(b,a,R3)};for(int i=0;i<2;i++){if(!alive1[x[i]%r]||shas(&cov2,x[i]%R2))continue;if(sadd(&cov3,x[i])){sadd(&q3only,x[i]);q3marg++;}}}
static void q3e_cb(U a,U b,U d){if(a>b)return;U s=a+b;if(s%Ecur)return;q3small_e++;q3hit(a,b,s/Ecur,d,Ecur);} /* all e< E0 */
static U fcur;
static void q3f_cb(U a,U c,U d){U V=4*a*a*d+1;if(V%fcur)return;U e=V/fcur;if(e<E0)return;if(c*e<2*a)return;U b=c*e-a;assert((Z)4*a*b*d==(Z)e*F3+1);q3small_f++;q3hit(a,b,c,d,e);}
static U Vc,Vu,Vlo,Vhi,Vc_c,Vc_d;static U dv[1<<16];
static void Q3(void){U F=F3=R3;E0=2*r*r;T0=2*r*r;
 for(U e=1;e<E0;e++){if(((Z)e*F+1)%4)continue;Ecur=e;triples((U)(((Z)e*F+1)/4),q3e_cb);}
 for(U f=1;f<T0;f++){if((F+f)%4)continue;fcur=f;triples((F+f)/4,q3f_cb);}
 /* both large: e>=E0, f>=T0, a<=b.  ef=4a^2d+1, a=(F+f)/(4cd) -> c^2 d <= (F+f)^2/(4(ef-1)) <= (2F+2)^2/(4(E0T0-1)) */
 U Ub=(U)(((Z)(2*F+2)*(2*F+2))/(4*((Z)E0*T0-1)));
 for(U c=1;c*c<=Ub;c++)for(U d=1;c*c*d<=Ub;d++){Z V=(Z)F*F+4*c*c*d;assert(V<((Z)1<<63));U u=4*c*d;
  factor((U)V);int nd=1;dv[0]=1;for(int i=0;i<nfp;i++){int cur=nd;U pw=1;for(int k=0;k<fe[i];k++){pw*=fp[i];for(int j=0;j<cur;j++){assert(nd<(1<<16));dv[nd++]=dv[j]*pw;}}}
  for(int j=0;j<nd;j++){U f=dv[j];if(f<T0||f>F+2)continue;if((F+f)%u)continue;U a=(F+f)/u;U VV=4*a*a*d+1;if(VV%f)continue;U e=VV/f;if(e<E0||c*e<2*a)continue;U b=c*e-a;
   assert((Z)4*a*b*d==(Z)e*F+1);q3large++;q3hit(a,b,c,d,e);}}
}
/* ---- P5 ---- */
static U p5marg,p5data,p5E;static U cumAll[8],cumAlive[8],cumPer[8];static int curj;static Set seen5={0},seen5a={0};static U pershift;
static void p5hit(U a,U b,U c,U d){if(a%r==0||b%r==0||c%r==0||d%r==0)return;p5data++;
 U x[2]={cen(a,b,R3),cen(b,a,R3)};for(int i=0;i<2;i++){
  if(curj>=0){ if(sadd(&seen5,x[i]))cumAll[curj]++; pershift++;
    if(alive1[x[i]%r]&&sadd(&seen5a,x[i]))cumAlive[curj]++; }
  if(!alive1[x[i]%r]||shas(&cov2,x[i]%R2)||shas(&cov3,x[i]))continue;sadd(&cov3,x[i]);sadd(&p5only,x[i]);p5marg++;}}
static void p5cb(U a,U b,U d){if(a>b)return;U s=a+b;if(s%Ecur)return;p5hit(a,b,s/Ecur,d);}
static U shiftset[512];static int nss;
static void P5(void){U N=R3*r*r;p5E=16*r*r;Ncur=N;
 for(U e=1;e<p5E;e++){if((N+e)%4||e%r==0)continue;curj=0;while((r*r<<curj)<=e)curj++;Ecur=e;
   /* per-shift distinct centres: count via small local set */
   pershift=0;triples((N+e)/4,p5cb);cumPer[curj]+=pershift;}
 curj=-1;PK_large(N,p5E,p5hit);}

static int cmpU(const void*a,const void*b){U x=*(const U*)a,y=*(const U*)b;return (x>y)-(x<y);}
static void dump_set(const char*prefix,const char*name,Set*s,U mod,int filter_nonsq){char path[4096];snprintf(path,sizeof(path),"%s.%s.tsv",prefix,name);FILE*f=fopen(path,"w");assert(f);fprintf(f,"# r=%lu family=%s modulus=%lu\n",r,name,mod);U *v=malloc((s->n?s->n:1)*sizeof(U));assert(v);size_t n=0;for(size_t i=0;i<s->cap;i++)if(s->v[i]&&(!filter_nonsq||!sq[s->v[i]%r]))v[n++]=s->v[i];qsort(v,n,sizeof(U),cmpU);for(size_t i=0;i<n;i++)fprintf(f,"%lu\n",v[i]);assert(fclose(f)==0);free(v);}
int main(int argc,char**argv){assert(argc==2||argc==4);r=atoll(argv[1]);assert(r>=17&&r<=1600);R2=r*r;R3=R2*r;
 alive1=calloc(r,1);assert(alive1);
 sq=calloc(r,1);assert(sq);for(U i=1;i<r;i++)sq[i*i%r]=1;
 level1();U nons=0;for(U i=1;i<r;i++)if(!sq[i]){nons++;if(shas(&l1cov,i))l1++;else alive1[i]=1;}
 P3();Q3();P5();
 printf("r %lu nonsq %lu L1 %lu P3marg %lu P3data %lu Q3marg %lu Q3data %lu (smalle %lu smallf %lu large %lu) P5marg %lu P5data %lu\n",r,nons,l1,p3dist,p3data,q3marg,q3data,q3small_e,q3small_f,q3large,p5marg,p5data);
 /* cumulative over j: e < r^2 2^j */
 U a=0,b=0,c=0;printf("P5small r %lu",r);for(int j=0;j<5;j++){a+=cumAll[j];b+=cumAlive[j];c+=cumPer[j];printf(" j%d:all%lu/alive%lu/pershift%lu",j,a,b,c);}puts("");
 /* Exact native-modulus sparse sets only; no r^3 universe/bitmap is allocated.
    Output fields: r L1 P3marg Q3marg P5marg; each count is native modulus
    (r, r^2, r^3, r^3), and each deeper marginal excludes all earlier families. */
 /* exact alive mass after depth 3, as numerator over 2 r^3:  (r-1)/(2r) - L1/r - P3/r^2 - (Q3+P5)/r^3 */
 I num=(I)(r-1)*R2-2*(I)l1*R2-2*(I)p3dist*r-2*(I)(q3marg+p5marg);
 printf("alive_after_depth3_numer_over_2r^3 %ld ppm %.3f\n",(long)num,1e6*(double)num/(2.0*R3));
 printf("ROW %lu %lu %lu %lu %lu\n",r,l1,p3dist,q3marg,p5marg);
 if(argc==4){assert(strcmp(argv[2],"--dump-prefix")==0);dump_set(argv[3],"L1",&l1cov,r,1);dump_set(argv[3],"P3",&cov2,R2,0);dump_set(argv[3],"Q3",&q3only,R3,0);dump_set(argv[3],"P5",&p5only,R3,0);}
 return 0;}
