/* Opus hostile cross-lab review of notes/z80/EXTREME.md: independent direct
   count of ALL sorted solutions x<=y<=z of 4/p=1/x+1/y+1/z, p prime (no ET
   parametrisation).  For x in (p/4,3p/4], g=4x-p, s=px:
   (gy-s)(gz-s)=s^2, y=(s+h)/g, h | s^2, h<=s.  Since p does not divide x,
   h=p^i*delta, delta | x^2; i=2 forces delta<=x/p<1, so i in {0,1}.
   i=0 -> exactly one multiple of p (I), i=1 -> two (II).  x factored by a
   segmented sieve.  Output: p,I,II,distinct,ordered,min_x,min_gap,min_Pplus */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <assert.h>
typedef unsigned long long U; typedef unsigned __int128 L;
static int *pr;static long npr;
static void sv(U lim){char*c=calloc(lim+1,1);pr=malloc(sizeof(int)*(lim/2+10));
  for(U i=2;i<=lim;i++)if(!c[i]){pr[npr++]=i;for(U j=i*i;j<=lim;j+=i)c[j]=1;}free(c);}
#define MF 16
typedef struct{int k;U q[MF];int e[MF];}Fa;
int main(int ac,char**av){
  puts("p,I,II,distinct,ordered,min_x,min_gap,min_Pplus");
  U *dv=malloc(8*4000000);
  for(int ii=1;ii<ac;ii++){U p=strtoull(av[ii],0,10);
    U lo=p/4+1,hi=3*p/4; /* x<=3p/4 */
    U lim=(U)sqrtl((long double)hi)+2;npr=0;sv(lim);
    for(long i=0;i<npr&&(U)pr[i]*pr[i]<=p;i++)assert(p%pr[i]);
    long long I=0,II=0,dist=0,ord=0;U mx=0,mg=0,mP=0;
    const U BL=1<<16;Fa*F=malloc(sizeof(Fa)*BL);U*rem=malloc(8*BL);
    for(U b=lo;b<=hi;b+=BL){U e=b+BL-1;if(e>hi)e=hi;
      for(U x=b;x<=e;x++){rem[x-b]=x;F[x-b].k=0;}
      for(long i=0;i<npr;i++){U q=pr[i];if(q*q>e)break;U x0=b+(q-b%q)%q;
        for(U x=x0;x<=e;x+=q){U*m=&rem[x-b];int k=0;while(*m%q==0){*m/=q;k++;}Fa*f=&F[x-b];f->q[f->k]=q;f->e[f->k++]=k;}}
      for(U x=b;x<=e;x++){Fa*f=&F[x-b];if(rem[x-b]>1){f->q[f->k]=rem[x-b];f->e[f->k++]=1;}
        U Pp=f->k?f->q[f->k-1]:1; for(int j=0;j<f->k;j++)if(f->q[j]>Pp)Pp=f->q[j];
        long nd=1;dv[0]=1;for(int j=0;j<f->k;j++){long m=nd;U pw=1;for(int t=0;t<2*f->e[j];t++){pw*=f->q[j];for(long a=0;a<m;a++)dv[nd++]=dv[a]*pw;}}
        assert(nd<4000000);
        U g=4*x-p,s=p*x;
        for(long j=0;j<nd;j++){U d=dv[j];
          for(int i=0;i<2;i++){U h=i?p*d:d; if(i&&d>x)continue; if(h>s)continue;
            if((s+h)%g)continue; U y=(s+h)/g; if(y<x)continue;
            L s2h=(L)s*s/h; assert((L)h*s2h==(L)s*s); L zn=(L)s+s2h; if(zn%g)continue; L z=zn/g;
            assert((L)y<=z);
            { /* sanity: 4xyz = p(xy+z(x+y)) modulo two 64-bit primes (exactness is (gy-s)(gz-s)=s^2 by construction) */
              const U m1=0xFFFFFFFFFFFFFFC5ULL; /* 2^64-59 prime */
              L Xm=x%m1,Ym=y%m1,Zm=z%m1,Pm=p%m1;
              L l=(4*Xm%m1)*Ym%m1*Zm%m1; L r=(Pm*((Xm*Ym%m1+Zm*((Xm+Ym)%m1))%m1))%m1; assert(l==r);
              const U m2=0xFFFFFFFFFFFFFF43ULL; /* 2^64-189 */
              Xm=x%m2;Ym=y%m2;Zm=z%m2;Pm=p%m2;l=(4*Xm%m2)*Ym%m2*Zm%m2;r=(Pm*((Xm*Ym%m2+Zm*((Xm+Ym)%m2))%m2))%m2;assert(l==r);}
            int mult=(y%p==0)+(z%p==0); /* x<p is never a multiple */
            assert((i==0&&mult==1)||(i==1&&mult==2));
            if(i==0)I++;else II++;
            int nd3=(x==y&&(L)y==z)?1:((x==y||(L)y==z)?2:3);
            dist+=nd3==3; ord+=nd3==3?6:(nd3==2?3:1);
            if(!mx||x<mx)mx=x; if(!mg||g<mg)mg=g; if(!mP||Pp<mP)mP=Pp;}}}
    }
    printf("%llu,%lld,%lld,%lld,%lld,%llu,%llu,%llu\n",p,I,II,dist,ord,mx,mg,mP);fflush(stdout);
    free(F);free(rem);free(pr);}
  return 0;}
