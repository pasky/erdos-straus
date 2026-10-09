/* R98b from scratch: for pairs a<=b, ab<=B, 17∤ab, m=4ab: for each divisor e|a+b find least odd K>=1 with
   17^K ≡ -e (mod m) and 17^K+e >= m (K_min); E_inf = #triples with some such K. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int cmp(const void*x,const void*y){long a=*(long*)x,b=*(long*)y;return (a>b)-(a<b);}
int main(int argc,char**argv){
  long B=atol(argv[1]); long pairs=0,sumtau=0,E=0,le13=0,cap=1<<20; long *km=malloc(cap*sizeof(long));
  long mmax=4*B+8; long *first=malloc(mmax*sizeof(long)); /* first[e]: K_min for residue e, -1 none */
  for(long a=1;a*a<=B;a++) for(long b=a;a*b<=B;b++){
    if(a%17==0||b%17==0) continue;
    pairs++; long m=4*a*b, s=a+b;
    /* divisors of s */
    long divs[4096]; int nd=0; for(long q=1;q*q<=s;q++) if(s%q==0){divs[nd++]=q; if(q*q!=s) divs[nd++]=s/q;}
    sumtau+=nd;
    /* iterate odd K: x=17^K mod m; also track true 17^K up to > m */
    long x=17%m, big=17; long Kthr=-1; /* first odd K with 17^K>=m */
    int need=nd; for(int i=0;i<nd;i++) first[divs[i]]=-1;
    /* mark which residues are divisors */
    long K=1; long x0=-1; long periods_after_thr=0; long Kstart=-1;
    while(1){
      long e=(m-x)%m; /* e ≡ -17^K mod m, in [0,m) */
      int ok_size = (big>=m) || (big+e>=m);
      if(e>0 && e<=s && s%e==0 && first[e]==-1 && ok_size){ first[e]=K; need--; }
      if(need==0) break;
      if(big>=m && Kstart<0){Kstart=K; x0=x;}
      long xn=(x*289)%m; K+=2; if(big<m) big*=289;
      x=xn;
      if(Kstart>=0 && K>Kstart && x==x0) break; /* full period of odd powers past threshold */
    }
    for(int i=0;i<nd;i++){ long e=divs[i]; if(first[e]>0){ if(E>=cap){cap*=2;km=realloc(km,cap*sizeof(long));} km[E++]=first[e]; if(first[e]<=13) le13++; } }
  }
  qsort(km,E,sizeof(long),cmp);
  printf("B=%ld pairs=%ld sumtau=%ld E_inf=%ld frac=%.4f E/(BlnB)=%.4f #Kmin<=13=%ld median=%ld max=%ld\n",
    B,pairs,sumtau,E,(double)E/sumtau,E/(B*__builtin_log(B)),le13,km[(E-1)/2],km[E-1]);
}
