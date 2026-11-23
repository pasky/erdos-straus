/* Fixed-constant-term census by pointwise monic divisor decision, NOT the
   exceptional-fibre resultant proof. For quadratic A=T also compare an
   elementary separate five-curve test on every irreducible. */
#define FFL_NO_MAIN
#include "ffl_es.c"
#include <assert.h>
/* P=A*quot+R. Either X=quot or the free difference X-quot has lc 1
   or 2 in our characteristic. Enumerate divisors of X only, evaluating
   the same-side and mixed-side tests in R[T]/E. */
static int possible(const poly *p){
    poly Q0,rem,X,E,V,AV,mrem; p_divmod(&Q0,&rem,p,&Apoly);p_neg(&mrem,&rem);
    for(int j=-1;j<Q0.d;++j){uint64_t lim=j<0?1:2*qpow[j];
        for(uint64_t i=0;i<lim;i++){
            if(j<0){X=Q0;E=mrem;}else{
                p_from_idx(&V,j,i%qpow[j]);V.c[j]=1+(i>=qpow[j]);
                p_add(&X,&Q0,&V);p_mul(&AV,&Apoly,&V);p_add(&E,&AV,&mrem);
            }
            assert(E.d>=0);int el=E.c[E.d];if(el!=1&&el!=2)continue;
            static poly primes[64],dv[MAXDIV],rs[MAXDIV];static int ex[64],cd[MAXDIV],rd[64];
            int nf=factor(&X,primes,ex),num=divisors(primes,ex,nf,dv,cd,rd);
            for(int t=0;t<num;t++)p_divmod(NULL,&rs[t],&dv[t],&E);
            poly ax,ar; p_mul(&ax,&Apoly,&X);p_divmod(NULL,&ar,&ax,&E);
            for(int s=0;s<num;s++){
                poly f,h;p_mul(&f,&rs[s],&ar);p_divmod(NULL,&h,&f,&E);
                for(int t=0;t<num;t++){
                    poly z;if(el==1){p_add(&z,&h,&rs[t]);if(z.d<0)return 1;}
                    if(el==1+(dv[s].d==dv[t].d)){p_add(&z,&rs[s],&rs[t]);if(z.d<0)return 1;}
                }
            }
        }
    }return 0;
}
int main(int ac,char**av){if(ac!=4&&ac!=5)return 2;int q=atoi(av[1]),n=atoi(av[2]);K=atoi(av[3]);
    if(q<5||q>31||n<2||n>5||K<1||K>2||K>=n)return 2;
    field_init(q); if(PCH<5 || qpow[n]>1000000)return 2;
    int aix=(ac==5?atoi(av[4]):0);if(aix<0||(uint64_t)aix>=qpow[K])return 2;
    spf_build(n);p_from_idx(&Apoly,K,aix);int ok[1024]={0},irr[1024]={0};
    for(uint64_t i=0;i<qpow[n];i++){poly p;p_from_idx(&p,n,i);if(!is_irr_small(&p))continue;
        int b=p.c[0],hit=possible(&p);if(n<=3)assert(hit==!!decide(&p,0,NULL,NULL,NULL));poly rem;
        p_divmod(NULL,&rem,&p,&Apoly);int ri=0;for(int j=rem.d;j>=0;j--)ri=ri*q+rem.c[j];
        irr[ri]++;ok[ri]+=hit;
        if(n==2 && K==1 && aix==0){int u=gadd[gadd[b][p.c[1]]][1], z=gmul[b][u];
            assert(hit==(b==gneg[1]||b==gneg[2]||u==gneg[1]||z==gneg[1]||gmul[z][u]==gneg[1]));}
    }
    int all=0,hit=0,ex=0,ab=0,amax=0,id=0,covered=0;
    for(int R=1;R<(int)qpow[K];R++){int b=R%q,h=R/q;
        int ab1=K==2?gadd[gadd[gmul[b][b]][gmul[Apoly.c[1]][b]]][gadd[Apoly.c[0]][1]]:0;
        int special=(!h&&(b==gneg[1]||b==gneg[2])) || (K==2 && h==gneg[1] && !ab1);
        if(special){ex++;assert(ok[R]==irr[R]);ab+=irr[R];}
        else {if(n==K+1)assert(ok[R]<=6);if(ok[R]>amax){amax=ok[R];id=R;}
            if(irr[R] && ok[R]==irr[R])covered++;}
        hit+=ok[R];all+=irr[R];}
    if(aix)printf("Aidx=%d ",aix);
    printf("q=%d n=%d k=%d irr=%d hits=%d excFibres=%d excHits=%d maxOther=%d first=%d otherFull=%d\n",q,n,K,all,hit,ex,ab,amax,id,covered);
}
