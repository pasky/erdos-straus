// z51 dbreak round 4: the board's astra-5 quadratic-orthogonal residual for the 4Z-line prime family.
// Band: primes l ≡ 3 (mod 4) with y < l <= z, z = exp((ln N)^beta), y = sqrt(z)  (or explicit y z).
// F_l(n) = 1[n ≡ -4e (mod l) for some e with 4e | l+1],  c_l = w(l)/(l-1),  w(l) = tau((l+1)/4),
// R_l(n) = F_l(n) - c_l*(1[l∤n] - (n/l))  (= 0 on residues and on 0; = F_l - 2c_l on non-residues).
// R(n) = sum over the band.  Population: n = 8k+1 <= N, n > 1, non-squares.
// mode "exact": full enumeration (float accumulator per n); prints, for each t, (1/|pop|) sum exp(-tR),
//   the independent-model value, moments sum R^j (j<=6), a histogram of R, and the most negative n.
// mode "sample": S random n; prints "n R H Q" per sample (H = #hits, Q = sum c_l (n/l)).
// Usage: resid exact N beta [y z]     |  resid sample N beta S seed [y z]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

static int jacobi(long long a, long long n){ // n odd positive
  a%=n; if(a<0) a+=n; int r=1;
  while(a){ while((a&1)==0){ a>>=1; long long m=n&7; if(m==3||m==5) r=-r; }
    long long t=a; a=n; n=t; if((a&3)==3 && (n&3)==3) r=-r; a%=n; }
  return n==1? r: 0; }
static int tau(long long x){ int d=1; for(long long p=2;p*p<=x;p++){ int e=0; while(x%p==0){x/=p;e++;} d*=e+1; } if(x>1) d*=2; return d; }
static uint64_t rs=0x9E3779B97F4A7C15ULL; static uint64_t xr(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
// hit iff r := (-n mod l) = 4e with 4e | l+1; the case 4e = l+1 gives r = 1 (n ≡ -1 mod l).
static int ishit(long long nmod, long long l){ long long r=(l-nmod)%l; if(r==0) return 0; if(r==1) return 1; return (r%4==0) && ((l+1)%r==0); }

int main(int argc,char**argv){
  if(argc<4){ fprintf(stderr,"usage\n"); return 1; }
  int exact = strcmp(argv[1],"exact")==0;
  long long N=atoll(argv[2]); double beta=atof(argv[3]);
  double z = exp(pow(log((double)N),beta)), y=sqrt(z);
  int ai = exact? 4: 6;
  long long S=0; if(!exact){ S=atoll(argv[4]); rs^=(uint64_t)atoll(argv[5])*0x2545F4914F6CDD1DULL; }
  if(argc>ai+1){ y=atof(argv[ai]); z=atof(argv[ai+1]); }
  long long Z=(long long)z, Y=(long long)y;
  // primes l ≡ 3 mod 4 in (Y, Z]
  char *cp=calloc(Z+2,1); for(long long i=2;i*i<=Z;i++) if(!cp[i]) for(long long j=i*i;j<=Z;j+=i) cp[j]=1;
  long long np=0; for(long long l=3;l<=Z;l+=4) if(l>Y && !cp[l]) np++;
  long long *L=malloc(sizeof(long long)*np); double *C=malloc(sizeof(double)*np); np=0;
  double mu=0, sig2=0;
  for(long long l=3;l<=Z;l+=4) if(l>Y && !cp[l]){ int w=tau((l+1)/4); L[np]=l; C[np]=(double)w/(l-1); 
    double c=C[np]; mu+=c; double pnr=(double)(l-1)/(2.0*l), ph=(double)w/l;
    sig2 += ph*(1-2*c)*(1-2*c) + (pnr-ph)*4*c*c; np++; }
  double ts[6]={0.1,0.25,0.5,1.0,1.5,2.0}; int nt=6;
  double lmod[6]={0};
  for(long long i=0;i<np;i++){ long long l=L[i]; double c=C[i]; int w=(int)llround(c*(l-1));
    double pnr=(double)(l-1)/(2.0*l), ph=(double)w/l;
    for(int a=0;a<nt;a++){ double t=ts[a]; lmod[a]+=log((double)(l+1)/(2.0*l) + ph*exp(-t*(1-2*c)) + (pnr-ph)*exp(2*t*c)); } }
  printf("# N=%lld beta=%.3f y=%.1f z=%.1f primes=%lld mu=%.6f sigma2_model=%.6f\n", N, beta, y, z, np, mu, sig2);
  for(int a=0;a<nt;a++) printf("M t=%.2f model_log_mgf=%.6f model_norm=%.6f\n", ts[a], lmod[a], lmod[a]/(mu*ts[a]*ts[a]));
  long long K=(N-1)/8+1;
  if(!exact){
    for(long long s=0;s<S;s++){ long long k,n; do{ k=1+(long long)(xr()%(uint64_t)(K-1)); n=8*k+1; long long r=(long long)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; if(r*r!=n) break; }while(1);
      double R=0,Q=0; int H=0;
      for(long long i=0;i<np;i++){ long long l=L[i]; long long a=n%l; int j=jacobi(a,l); if(j==-1){ int h=ishit(a,l); H+=h; R+=h-2*C[i]; } Q+=C[i]*j; }
      printf("%lld %.6f %d %.6f\n", n, R, H, Q); }
    return 0;
  }
  float *R=calloc(K,sizeof(float)); if(!R){ fprintf(stderr,"oom\n"); return 1; }
  float *g=malloc(sizeof(float)*(Z+2));
  for(long long i=0;i<np;i++){ long long l=L[i]; double c=C[i];
    // g = -2c on non-residues, 0 on 0 and residues, 1-2c on hit classes (all non-residues)
    for(long long a=0;a<l;a++) g[a]=(float)(-2*c);
    g[0]=0.0f; for(long long b=1;2*b<l;b++) g[(b*b)%l]=0.0f;
    { long long q=(l+1)/4; for(long long d=1;d*d<=q;d++) if(q%d==0){ long long ds[2]={d,q/d}; for(int u=0;u<2;u++){ long long cl=(l-(4*ds[u])%l)%l; g[cl]=(float)(1-2*c); } } }
    long long r=1%l; for(long long k=0;k<K;k++){ R[k]+=g[r]; r+=8; if(r>=l) r-=l; } }
  unsigned char *sq=calloc(K,1); for(long long m=1;m*m<=N;m+=2) sq[(m*m-1)/8]=1;
  double se[6]={0}, mom[7]={0}; long long cnt=0; long long hist[2001]={0}; double hlo=-10, hw=0.02;
  // most negative 200
  int TOP=200; long long tn[200]; float tv[200]; int tc=0;
  for(long long k=1;k<K;k++){ if(sq[k]) continue; double r=R[k]; cnt++;
    for(int a=0;a<nt;a++) se[a]+=exp(-ts[a]*r);
    double p=1; for(int j=1;j<=6;j++){ p*=r; mom[j]+=p; }
    long long b=(long long)floor((r-hlo)/hw); if(b<0) b=0; if(b>2000) b=2000; hist[b]++;
    if(tc<TOP){ tn[tc]=8*k+1; tv[tc]=(float)r; tc++; } else { int mx=0; for(int i=1;i<TOP;i++) if(tv[i]>tv[mx]) mx=i; if(r<tv[mx]){ tv[mx]=(float)r; tn[mx]=8*k+1; } } }
  printf("# population (non-squares) = %lld\n", cnt);
  for(int a=0;a<nt;a++){ double lm=log(se[a]/cnt); printf("E t=%.2f log_mgf=%.6f norm=%.6f model_norm=%.6f excess_norm=%.6f\n", ts[a], lm, lm/(mu*ts[a]*ts[a]), lmod[a]/(mu*ts[a]*ts[a]), (lm-lmod[a])/(mu*ts[a]*ts[a])); }
  for(int j=1;j<=6;j++) printf("MOM %d %.10e\n", j, mom[j]/cnt);
  for(int b=0;b<=2000;b++) if(hist[b]) printf("HIST %.3f %lld\n", hlo+b*hw, hist[b]);
  for(int i=0;i<tc;i++) printf("NEG %lld %.6f\n", tn[i], tv[i]);
  return 0;
}
