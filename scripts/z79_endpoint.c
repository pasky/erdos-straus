/* Point P, exact arithmetic. e,J,HZ consume complete GNU factor records with
   verified products. Hd uses GMP perfect-square windows; positive tests also
   available at small L using caller-provided cutoffs.  2<=L<=14. */
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <gmp.h>
typedef uint64_t U;typedef __uint128_t Z;
static Z N,W,B,emax;static U p,q,C,vis,hits,keys;static int gen;
static void pr(Z v){if(v>=10)pr(v/10);putchar(48+(int)(v%10));}
static void test(Z a,Z b,Z d){if(!a||a>b||!d||a%17==0||b%17==0||d%17==0||(p*a+q*b)%W)return;
 if(a>(N+emax)/4/d/b)return;Z v=4*a*b*d;if(v<=N)return;Z e=v-N;if(e%17==0||(a+b)%e||((a+b)/e)%17==0)return;
 printf("hit ");pr(a);putchar(' ');pr(b);putchar(' ');pr(d);putchar('\n');hits++;}
static void at_a(Z H,Z a){if(!a||a>W*H/(p+q))return;Z n=W*H-p*a;if(n%q)return;Z b=n/q;
 if(a>(N+emax)/4/b)return;Z m=4*a*b;test(a,b,N/m+1);}
#define CAP 100000
static Z A[CAP],D[CAP];
static Z parse(char**s){while(isspace((unsigned char)**s))(*s)++;assert(isdigit((unsigned char)**s));Z n=0;do{n=n*10+**s-'0';(*s)++;}while(isdigit((unsigned char)**s));return n;}
static int factors(Z n,Z *ds){assert(n);if(gen){pr(n);putchar('\n');return 0;} char buf[4096];assert(fgets(buf,sizeof buf,stdin));char *s=buf;assert(parse(&s)==n&&*s++==':');Z rem=n,last=0;int nd=1,old=1;ds[0]=1;
 for(;;){while(isspace((unsigned char)*s))s++;if(!*s)break;Z t=parse(&s);assert(t>=2&&t>=last&&rem%t==0);rem/=t;if(t!=last)old=nd;assert(nd+old<=CAP);for(int j=0;j<old;j++)ds[nd+j]=ds[nd+j-old]*t;nd+=old;last=t;}assert(rem==1);return nd;}
static void zset(mpz_t z,Z v){mpz_import(z,1,-1,sizeof v,0,0,&v);}static Z zget(mpz_t z){Z v=0;size_t n;assert(mpz_sizeinbase(z,2)<=128);mpz_export(&v,&n,-1,sizeof v,0,0,z);return v;}
static void hd(void){mpz_t sq,top,bot,z;mpz_inits(sq,top,bot,z,NULL);
 for(U H=1;H<=C;H++){Z V=W*H;zset(sq,V);mpz_mul(sq,sq,sq);
 for(U d=1;d<=C/H;d++){vis++;Z hi=(p*q*(N+1)+d-1)/d,lo=p*q*(N+emax)/d;
 zset(z,hi);mpz_sub(top,sq,z);if(mpz_sgn(top)<0)continue;mpz_sqrt(top,top);Z up=zget(top);
 zset(z,lo);mpz_sub(bot,sq,z);Z low=0;if(mpz_sgn(bot)>0){mpz_sqrt(bot,bot);low=zget(bot);}assert(up<V&&low<=up);
 for(int k=0;k<2;k++){Z left=k?V+low:V-up,right=k?V+up:V-low;for(Z a=(left+2*p-1)/(2*p);a<=right/(2*p);a++){if(!a||a>V/(p+q)||(V-p*a)%q)continue;test(a,(V-p*a)/q,d);}}
 }}mpz_clears(sq,top,bot,z,NULL);}
int main(int argc,char**argv){assert(argc==7);int L=atoi(argv[1]);p=atoi(argv[2]);q=atoi(argv[3]);char *mode=argv[4];C=strtoull(argv[5],0,10);gen=atoi(argv[6]);assert(L>=2&&L<=14&&p&&q&&p+q<=200&&C<100000000&&C>0);W=1;for(int i=0;i<L;i++)W*=17;B=W/17;N=W*B;
 /* Small synthetic endpoint tests use the elementary e<=N; actual levels
    use 466 ceil(sqrt W). All products in test() guarded by division. */
 emax=N;if(L>=12&&p*q==5&&p+q==6){U z=1;while((Z)z*z<W)z*=2;U l=z/2;while(z-l>1){U m=(l+z)/2;if((Z)m*m>=W)z=m;else l=m;}emax=466*(Z)z;}
 if(!strcmp(mode,"bound")){assert(!gen);pr(emax);putchar('\n');return 0;}
 if(!strcmp(mode,"e")){for(U e=4-(U)(N%4);e<=C;e+=4){if(e%17==0)continue;keys++;Z M=(N+e)/4;int n=factors(M,A);for(int i=0;i<n;i++){Z a=A[i];if(a>M/a)continue;Z rest=M/a;for(int j=0;j<n;j++){Z b=A[j];if(b>=a&&rest%b==0)test(a,b,rest/b);}}}}
 else if(!strcmp(mode,"J")){for(U J=1;J<=C;J++){Z v=q*B+J;if(v%4)continue;keys++;int n=factors(v/4,A),nd=factors(p*B+J,D);for(int i=0;i<n;i++){Z M=4*A[i];for(int j=0;j<nd;j++){Z e=D[j];if(e>emax||q*e>=W*J||(N+e)%M)continue;Z z=W*J-q*e;if(z%(p*M))continue;Z a=z/(p*M);if(a&&A[i]%a==0)test(a,(N+e)/M,A[i]/a);}}}}
 else if(!strcmp(mode,"HZ")){for(U H=1;H<=C;H++)for(U Zed=1;Zed<=C/H;Zed++){if(B*Zed<=q*H)continue;Z n=B*Zed-q*H;if(n%p)continue;keys++;int na=factors(n/p,A);for(int i=0;i<na;i++)at_a(H,A[i]);}}
 else {assert(!strcmp(mode,"Hd")&&!gen);hd();}if(!gen){assert(getchar()==EOF);printf("end %d %lu %lu %s %lu %lu %lu %lu\n",L,p,q,mode,C,keys,vis,hits);}}
