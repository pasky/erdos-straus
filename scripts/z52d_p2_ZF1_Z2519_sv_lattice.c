// Z2519: ES (*) certificates p = 4uBC - u - B as small solutions (x,y)=(B,u) of the linear congruence
// y = A x (mod p), A = 4Cu - 1 (exact identity: B*A - p = u).  Compare the lattice statistics of
// L_A = {(x,y): y = A x mod p} at certificate residues A with the Strömbergsson–Venkatesh / Haar law
// (A uniform mod p: P(lambda1(L_A) <= r sqrt p) -> 3 r^2 / pi for r <= 1).
// usage: z52d_p2_ZF1_Z2519_sv_lattice p0 p1 step_mod(=4 -> p=1 mod 4) nrand seed
// output: summary histograms on stdout.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef __int128 i128;
static int isprime(ll n){ if(n<2)return 0; for(ll d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
// Gauss-reduce lattice with basis (1,A),(0,p); return squared length of shortest vector
static double lam1sq(ll A, ll p, ll *sx, ll *sy){
  i128 ax=1, ay=A, bx=0, by=p;
  // Lagrange–Gauss: keep |a| <= |b|; reduce b by a; stop when the reduced b is not shorter than a
  i128 na=ax*ax+ay*ay, nb=bx*bx+by*by;
  if(na>nb){ i128 t=ax;ax=bx;bx=t; t=ay;ay=by;by=t; i128 tt=na;na=nb;nb=tt; }
  for(;;){
    i128 dot=ax*bx+ay*by;
    i128 num=2*dot+na, den=2*na; i128 m=num/den; if((num%den!=0)&&((num<0)!=(den<0))) m--; // exact floor(dot/na+1/2)
    bx-=m*ax; by-=m*ay; nb=bx*bx+by*by;
    if(nb>=na){ *sx=(ll)ax; *sy=(ll)ay; return (double)na; }
    i128 t=ax;ax=bx;bx=t; t=ay;ay=by;by=t; i128 tt=na;na=nb;nb=tt;
  }
}
#define NB 40
int main(int argc,char**argv){
  ll p0=atoll(argv[1]), p1=atoll(argv[2]); int nrand=atoi(argv[4]); unsigned seed=atoi(argv[5]);
  srand(seed);
  // histograms of r = lambda1/sqrt p in bins of 0.05 on [0,2)
  long long hc[NB]={0}, hu[NB]={0}, hv[NB]={0}, hmin[NB]={0}; long long ncert=0,nunif=0,nprim=0,nshort=0;
  long long hlogv[24]={0}; // log_p of cert-vector sup norm, bins of 1/40 on [0,0.6)
  double sumR=0;
  for(ll p=p0;p<=p1;p++){
    if(p%4!=1 || !isprime(p)) continue; nprim++;
    double sp=sqrt((double)p); double best=1e99; long long R=0;
    for(ll u=1; 4*u-1<=p+u; u++){
      for(ll C=1; 4*u*C-1<=p+u; C++){
        ll m=4*u*C-1; if((p+u)%m) continue;
        ll B=(p+u)/m; R++;
        ll A=m%p; ll sx,sy; double l1=sqrt(lam1sq(A,p,&sx,&sy))/sp;
        double cv=sqrt((double)B*B+(double)u*u)/sp;
        int b=(int)(l1/0.05); if(b<NB) hc[b]++;
        b=(int)(cv/0.05); if(b<NB) hv[b]++; 
        if(fabs(cv-l1)<1e-9) nshort++;
        double sup=(B>u?B:u); int lb=(int)(log(sup)/log((double)p)*40); if(lb>=0&&lb<24) hlogv[lb]++;
        if(cv<best) best=cv; ncert++;
      }
    }
    sumR+=R;
    if(best<1e98){int b=(int)(best/0.05); if(b<NB) hmin[b]++;}
    for(int i=0;i<nrand;i++){ ll A=1+(((ll)rand()<<31)^rand())%(p-1); ll sx,sy; double l1=sqrt(lam1sq(A,p,&sx,&sy))/sp;
      int b=(int)(l1/0.05); if(b<NB) hu[b]++; nunif++; }
  }
  printf("# primes p=1(4) in [%lld,%lld]: %lld ; certificates (ordered (u,B,C)): %lld ; mean R = %.2f\n",p0,p1,nprim,ncert,sumR/nprim);
  printf("# fraction of certificates whose vector (B,u) IS a shortest vector of L_A: %.4f\n",(double)nshort/ncert);
  printf("# r_hi  CDF_cert_lambda1  CDF_unif_lambda1  Haar 3r^2/pi  CDF_certvec_norm  CDF_min_certvec_per_p\n");
  long long cc=0,cu=0,cv=0,cm=0;
  for(int b=0;b<NB;b++){ cc+=hc[b]; cu+=hu[b]; cv+=hv[b]; cm+=hmin[b]; double r=(b+1)*0.05;
    printf("%.2f %.5f %.5f %.5f %.5f %.5f\n", r,(double)cc/ncert,(double)cu/nunif, r<=1?3*r*r/M_PI:-1.0,(double)cv/ncert,(double)cm/nprim); }
  printf("# distribution of log_p(max(B,u)) over certificates (bin width 1/40)\n");
  for(int b=0;b<24;b++) printf("%.3f %.5f\n",(b+1)/40.0,(double)hlogv[b]/ncert);
  return 0;
}
