/* z52d pass2 SK3, item Z2003: definitions from FRONTIER 2.2:
   P(n) = {(u,B): gcd(u,B)=1, u+B odd, 4uB-u-B <= n}, q=4uB,
   M0(p)=sum_P 1/phi(q), T(p)=sum_P (-uB/p)/phi(q), M_BM(p)=M0-T.
   Prints, for primes p = 1 mod 4 in [P0,P1] (step PSTEP), the ratio T/M0 (worst case = +1),
   M_BM/log^2 p, and the share of T coming from pairs with u<=B and uB <= p^{1/2}, <= p, > p.  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
static uint64_t gcdu(uint64_t a, uint64_t b){ while(b){uint64_t t=a%b;a=b;b=t;} return a; }
static uint64_t phi_of(uint64_t n){ uint64_t r=n; for(uint64_t q=2;q*q<=n;q++) if(n%q==0){ while(n%q==0) n/=q; r-=r/q;} if(n>1) r-=r/n; return r; }
int main(int argc,char**argv){
    uint64_t P0=strtoull(argv[1],0,10), P1=strtoull(argv[2],0,10); int PSTEP=atoi(argv[3]);
    /* primes by sieve */
    char *comp=calloc(P1+1,1); comp[0]=comp[1]=1;
    for(uint64_t i=2;i*i<=P1;i++) if(!comp[i]) for(uint64_t j=i*i;j<=P1;j+=i) comp[j]=1;
    /* phi table for q up to 4*(P1)  (uB <= (p+u+B)/4 <= p/4+...); compute lazily via array */
    uint64_t QMAX = 4*P1/4 + 4*P1; /* generous: 4uB <= p + u + B <= 2p+ ... */
    uint32_t *ph = malloc((QMAX+1)*sizeof(uint32_t));
    for(uint64_t q=0;q<=QMAX;q++) ph[q]=0;
    for(uint64_t q=1;q<=QMAX;q++) for(uint64_t m=q;m<=QMAX;m+=q) ph[m]+=0; /* placeholder */
    /* simple phi sieve */
    for(uint64_t q=0;q<=QMAX;q++) ph[q]=q;
    for(uint64_t q=2;q<=QMAX;q++) if(ph[q]==q) for(uint64_t m=q;m<=QMAX;m+=q) ph[m]-=ph[m]/q;
    int cnt=0; double worstTM=-9, minMBM=1e9; uint64_t worstp=0, minp=0; double sumTM=0; int np=0;
    double minM8[2]={1e9,1e9}, sumM8[2]={0,0}; int nM8[2]={0,0}, below1402[2]={0,0};
    for(uint64_t p=P0;p<=P1;p+=PSTEP){
        if(comp[p]||p%4!=1) continue;
        /* Legendre table */
        char *qr=calloc(p,1); for(uint64_t x=1;x<p;x++) qr[(x*x)%p]=1;
        double M0=0,T=0,Ts=0,Tm=0,Tl=0; /* Ts: uB<=sqrt p ; Tm: sqrt p<uB<=p ; Tl: uB>p */
        for(uint64_t u=1;;u++){
            /* minimal B=1: 4uB-u-B = 3u-1 <= p ; if 3u-1>p stop */
            if(3*u-1>p) break;
            for(uint64_t B=1;;B++){
                uint64_t n=4*u*B-u-B;
                if(n>p) break;
                if(((u+B)&1)==0) continue;
                if(gcdu(u,B)!=1) continue;
                uint64_t q=4*u*B;
                double w=1.0/ph[q];
                uint64_t r=(p - ((u*B)%p))%p; /* -uB mod p */
                int leg = (r==0)?0:(qr[r]?1:-1);
                M0+=w; T+=leg*w;
                double uB=(double)(u*B);
                if(uB<=sqrt((double)p)) Ts+=leg*w; else if(uB<=p) Tm+=leg*w; else Tl+=leg*w;
            }
        }
        free(qr);
        double L=log((double)p), TM=T/M0, MBM=(M0-T)/(L*L);
        sumTM+=TM; np++;
        { int k=(p%8==1)?0:1; if(MBM<minM8[k]) minM8[k]=MBM; sumM8[k]+=MBM; nM8[k]++; if(MBM<0.1402) below1402[k]++; }
        if(TM>worstTM){worstTM=TM;worstp=p;}
        if(MBM<minMBM){minMBM=MBM;minp=p;}
        if(cnt<6 || p%(PSTEP*1)==0) { if(cnt<12) printf("p=%llu T/M0=%.4f MBM/L2=%.4f  shares Ts=%.3f Tm=%.3f Tl=%.3f\n",(unsigned long long)p,TM,MBM,Ts/M0,Tm/M0,Tl/M0); cnt++; }
    }
    printf("primes(=1 mod 4) in [%llu,%llu] step %d: n=%d mean T/M0=%.4f worst T/M0=%.4f at p=%llu; min M_BM/log^2p=%.4f at p=%llu\n",
      (unsigned long long)P0,(unsigned long long)P1,PSTEP,np,sumTM/np,worstTM,(unsigned long long)worstp,minMBM,(unsigned long long)minp);
    printf("mod 8 split: p=1 mod 8: n=%d mean M_BM/L2=%.4f min=%.4f frac<0.1402=%.4f | p=5 mod 8: n=%d mean=%.4f min=%.4f frac<0.1402=%.4f\n",
      nM8[0], sumM8[0]/(nM8[0]?nM8[0]:1), minM8[0], nM8[0]?(double)below1402[0]/nM8[0]:0, nM8[1], sumM8[1]/(nM8[1]?nM8[1]:1), minM8[1], nM8[1]?(double)below1402[1]/nM8[1]:0);
    return 0;
}
