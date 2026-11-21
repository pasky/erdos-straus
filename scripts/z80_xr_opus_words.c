/* Opus hostile cross-lab review of notes/z80/EXTREME.md: independent word
   engine (own code, shares nothing with z80_extreme_words.c/wordfactor.py).
   Words: positive (u,t,v) with t*u*v-u-v = n, labelled (u,t,v) counted once.
   Partition by the minimal letter:
     A: u<=t, u<=v      -> factor n+u by a segmented sieve, f=tu-1 | n+u
     B: v<u, v<=t       -> mirror of A-triples with u<v
     C: t<u, t<v        -> t=1: divisor pairs of n+1 (from the same sieve, u=1);
                           t>=2: loop u<=v with (tu-1)^2<=tn+1, test divisibility.
   Second, separate certificate for R_k (k=4,8): for every u with k*u*u-2u<=n,
   enumerate all divisors f of n+u (sieve-factored) with f == -1 mod k*u and
   B=(n+u)/f>u; unordered count.  Primality of n by trial division to isqrt(n).
   Output: n,prime,R,R8,U7,ES5,HJmin,words,R4pairs,R8pairs */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <assert.h>
typedef unsigned long long U64; typedef __int128 L;
static U64 isq(U64 x){U64 r=(U64)sqrtl((long double)x);while(r*r>x)r--;while((r+1)*(r+1)<=x)r++;return r;}
static int *pr; static long npr;
static void sieve(U64 lim){char *c=calloc(lim+1,1);pr=malloc(sizeof(int)*(lim/2+10));npr=0;
  for(U64 i=2;i<=lim;i++)if(!c[i]){pr[npr++]=(int)i;for(U64 j=i*i;j<=lim;j+=i)c[j]=1;}free(c);}
static int jacobi(L a,L n){int s=1;a%=n;if(a<0)a+=n;while(a){while(!(a&1)){a>>=1;L r=n%8;if(r==3||r==5)s=-s;}
  L tmp=a;a=n;n=tmp;if(a%4==3&&n%4==3)s=-s;a%=n;}return n==1?s:0;}
/* factorisation of n+u for u in [lo,hi): fills per-u lists */
#define MAXF 24
typedef struct{int k;U64 q[MAXF];int e[MAXF];} Fac;
static void factor_block(U64 n,U64 lo,U64 hi,Fac *F,U64 *rem){
  for(U64 u=lo;u<hi;u++){rem[u-lo]=n+u;F[u-lo].k=0;}
  for(long i=0;i<npr;i++){U64 q=pr[i];U64 r=(q-(n%q))%q; /* u == -n mod q */
    U64 u0=lo+((r+q-(lo%q))%q);
    for(U64 u=u0;u<hi;u+=q){U64 *m=&rem[u-lo];int e=0;while(*m%q==0){*m/=q;e++;}
      assert(e>0);Fac*f=&F[u-lo];assert(f->k<MAXF);f->q[f->k]=q;f->e[f->k]=e;f->k++;}}
  for(U64 u=lo;u<hi;u++)if(rem[u-lo]>1){Fac*f=&F[u-lo];
    /* cofactor has no prime <= sieve limit; sieve limit^2 > n+u so it is prime */
    assert(f->k<MAXF);f->q[f->k]=rem[u-lo];f->e[f->k]=1;f->k++;}
  for(U64 u=lo;u<hi;u++){L p=1;Fac*f=&F[u-lo];for(int j=0;j<f->k;j++)for(int i=0;i<f->e[j];i++)p*=f->q[j];assert(p==(L)(n+u));}
}
static U64 *dv;static long ndv;
static void divs(Fac*f){ndv=1;dv[0]=1;for(int j=0;j<f->k;j++){long m=ndv;U64 pw=1;
  for(int i=0;i<f->e[j];i++){pw*=f->q[j];for(long a=0;a<m;a++)dv[ndv++]=dv[a]*pw;}}}
static U64 n;static long long W,R,R8,U7,ES5;static L HJ;
static void word(U64 u,U64 t,U64 v){assert((L)t*u*v-u-v==(L)n);W++;R+=t%4==0;R8+=t%8==0;U7+=((L)t*u)%8==0;
  L a=(L)t*u-1,b=(L)t*v-1;ES5+=(u%4==0||t%4==0||v%4==0||a%4==0||b%4==0);
  if(u>=2&&t>=2&&v>=2&&jacobi(a,n)==-1&&(!HJ||a<HJ))HJ=a;}
int main(int ac,char**av){
  dv=malloc(sizeof(U64)*2000000);
  puts("n,prime,R,R8,U7,ES5,HJmin,words,R4pairs,R8pairs");
  for(int ii=1;ii<ac;ii++){n=strtoull(av[ii],0,10);assert(n%4==1&&n>5);
    U64 U4=isq(n/4)+2;while(4*U4*U4-2*U4>n)U4--;
    U64 T=1;while((T+1)*(T+1)*(T+1)-2*(T+1)<=n)T++;
    U64 Umax=(U4>T?U4:T)+1;
    U64 lim=isq(n+Umax)+1;sieve(lim);
    int prime=1;for(long i=0;i<npr&&(U64)pr[i]*pr[i]<=n;i++)if(n%pr[i]==0){prime=0;break;}
    W=R=R8=U7=ES5=0;HJ=0;long long P4=0,P8=0;
    const U64 BL=1<<16;Fac*F=malloc(sizeof(Fac)*BL);U64*rem=malloc(8*BL);
    for(U64 lo=1;lo<=Umax;lo+=BL){U64 hi=lo+BL;if(hi>Umax+1)hi=Umax+1;factor_block(n,lo,hi,F,rem);
      for(U64 u=lo;u<hi;u++){divs(&F[u-lo]);U64 N=n+u;
        for(long j=0;j<ndv;j++){U64 f=dv[j];
          if(u<=T && (f+1)%u==0){U64 t=(f+1)/u,v=N/f;if(t>=u&&v>=u){word(u,t,v);if(u<v)word(v,t,u);}}
          for(int k=4;k<=8;k+=4)if(u<=U4&&(f+1)%(k*u)==0){U64 B=N/f;if(B>u){assert((L)k*u*B*((f+1)/(k*u))-u-B==(L)n);if(k==4)P4++;else P8++;}}
          if(u==1){/* t=1, u',v'>=2: (u'-1)(v'-1)=n+1, f=u'-1 ; t<u',t<v' */
            U64 a=f+1,b=N/f+1;if(a>=2&&b>=2)word(a,1,b);} }}}
    for(U64 t=2;t<=T;t++){L M=(L)t*n+1;for(U64 u=t+1;;u++){L f=(L)t*u-1;if(f*f>M)break;if(M%f)continue;
        L g=M/f;if((g+1)%t)continue;U64 v=(U64)((g+1)/t);if(v<u)continue;word(u,t,v);if(v>u)word(v,t,u);}}
    printf("%llu,%d,%lld,%lld,%lld,%lld,%lld,%lld,%lld,%lld\n",n,prime,R,R8,U7,ES5,(long long)HJ,W,P4,P8);fflush(stdout);
    free(F);free(rem);free(pr);}
  return 0;}
