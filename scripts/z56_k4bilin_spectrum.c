/* z56 K4BILIN: "Type II spectrum" test for the S-weighted dense sequence
     a*_n = r*(n+4) r*(4n+1) = 16 * 2^{omega(n+4)+omega(4n+1)} * 1_S(n+4) 1_S(4n+1),   n = 97 (mod 120),
   against the multiplicative local model  w_n = f(n),  f(n) = prod_{l | n} (l-1)/(l-1+2chi(l))  (n = 97 mod 120),
   which has w-density g*(l) = 1/(l+2chi(l)) of {l | n}, the same as a* (Lemma T* of Z56_K4BILIN.md).
   For classes C of n we print rho(C) = (sum_C a* / sum_C w) / (sum_all a* / sum_all w):
     primes; P2 = p*q (p<=q primes) with log p/log X in [t, t+0.05); Omega(n) = 3; n in S; lambda(n)=+1 / -1.
   rho = 1 is the Type I + Type II prediction (EVIDENCE only).  Usage: ./spectrum X
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static int *primes; static int np;
static void mkprimes(int L){ char *s=calloc(L+1,1); primes=malloc(sizeof(int)*(L/2+10)); np=0;
  for(int i=2;i<=L;i++){ if(!s[i]){primes[np++]=i; for(long j=(long)i*i;j<=L;j+=i) s[j]=1;} } free(s);}
static long inv_mod(long a,long m){ long old_r=((a%m)+m)%m, r=m, old_s=1, s=0; while(r){ long q=old_r/r,t; t=old_r-q*r; old_r=r; r=t; t=old_s-q*s; old_s=s; s=t;} long v=old_s%m; if(v<0)v+=m; return v; }
int main(int argc,char**argv){
  long X = argc>1? atol(argv[1]) : 10000000L; const long M=120, n0=97;
  long K = (X - n0)/M + 1;           /* indices i: n = n0 + M i */
  long LIM = (long)sqrt(4.0*X+1)+2; mkprimes((int)LIM);
  uint64_t *rn = malloc(K*8), *r1 = malloc(K*8), *r2 = malloc(K*8);
  int8_t *w1 = calloc(K,1), *w2 = calloc(K,1), *ok1 = malloc(K), *ok2 = malloc(K), *Om = calloc(K,1), *sq = calloc(K,1), *nS = malloc(K);
  uint32_t *spf = calloc(K,4); float *f = malloc(K*4);
  for(long i=0;i<K;i++){ long n=n0+M*i; rn[i]=n; r1[i]=n+4; r2[i]=4*n+1; ok1[i]=ok2[i]=1; f[i]=1; nS[i]=1; }
  for(int k=0;k<np;k++){ long l=primes[k]; if(l<7) continue;
    long Ml = M*l; long invM = inv_mod(M % l, l);
    int chi = (l%4==1)? 1 : -1;
    /* n = n0 + M i = c (mod l)  <=>  i = (c - n0) * invM (mod l) */
    long cs[3] = {0, ((-4)%l+l)%l, (l - inv_mod(4,l))%l };
    for(int which=0; which<3; which++){
      long i0 = (((cs[which] - n0) % l + l) % l) * invM % l;
      for(long i=i0;i<K;i+=l){
        if(which==0){ int e=0; while(rn[i]%l==0){ rn[i]/=l; e++; } Om[i]+=e; if(e>1) sq[i]=1; if(!spf[i]) spf[i]=l; f[i]*= (float)((l-1.0)/(l-1.0+2*chi)); if(chi<0) nS[i]=0; }
        else if(which==1){ int e=0; while(r1[i]%l==0){ r1[i]/=l; e++; } if(chi>0) w1[i]++; else ok1[i]=0; }
        else { int e=0; while(r2[i]%l==0){ r2[i]/=l; e++; } if(chi>0) w2[i]++; else ok2[i]=0; }
      }
    }
    (void)Ml;
  }
  double At=0, Wt=0;
  double Ap=0,Wp=0, A3=0,W3=0, AS=0,WS=0, Aev=0,Wev=0, Aod=0,Wod=0;
  enum{NB=10}; double AB[NB]={0}, WB[NB]={0}; double lX=log((double)X);
  for(long i=0;i<K;i++){ long n=n0+M*i;
    if(rn[i]>1){ Om[i]++; if(!spf[i]) spf[i]=(uint32_t)rn[i]; uint64_t q=rn[i]; double c=(q%4==1)? (q-1.0)/(q+1.0) : (q-1.0)/(q-3.0); f[i]*=(float)c; if(q%4==3) nS[i]=0; }
    if(r1[i]>1){ if((r1[i]&3)==1) w1[i]++; else ok1[i]=0; }
    if(r2[i]>1){ if((r2[i]&3)==1) w2[i]++; else ok2[i]=0; }
    double a = (ok1[i]&&ok2[i]) ? 16.0*(double)(1L<<(w1[i]+w2[i])) : 0.0; double w=f[i];
    At+=a; Wt+=w;
    if(Om[i]==1){ Ap+=a; Wp+=w; }
    if(Om[i]==3){ A3+=a; W3+=w; }
    if(Om[i]==2 && !sq[i]){ double t=log((double)spf[i])/lX; int b=(int)(t/0.05); if(b>=0&&b<NB){ AB[b]+=a; WB[b]+=w; } }
    if(nS[i]){ AS+=a; WS+=w; }
    if(Om[i]%2==0){ Aev+=a; Wev+=w; } else { Aod+=a; Wod+=w; }
  }
  double R=At/Wt;
  printf("# X=%ld  class n=97 mod 120; global ratio sum a*/sum w = %.5f\n", X, R);
  printf("# rho(C) = (sum_C a*/sum_C w)/global ; C, rho, sum_C a*, sum_C w\n");
  printf("primes        %.4f  %.4e  %.4e\n", Ap/Wp/R, Ap, Wp);
  for(int b=0;b<NB;b++) if(WB[b]>0) printf("P2 p~X^[%.2f,%.2f)  %.4f  %.4e  %.4e\n", 0.05*b, 0.05*b+0.05, AB[b]/WB[b]/R, AB[b], WB[b]);
  printf("Omega=3       %.4f  %.4e  %.4e\n", A3/W3/R, A3, W3);
  printf("n in S        %.4f  %.4e  %.4e\n", AS/WS/R, AS, WS);
  printf("lambda=+1     %.4f  %.4e  %.4e\n", Aev/Wev/R, Aev, Wev);
  printf("lambda=-1     %.4f  %.4e  %.4e\n", Aod/Wod/R, Aod, Wod);
  return 0;
}
