// z60 LOPEZ: the mod-8 halves of U_II in the Jacobi form (Lemma L(J)).
//   U_II(n) >= 1  <=>  exists f ≡ 3 (mod 4) with (n/f) = -1 and r := (-n mod f) dividing f+1.
//   For f ≡ 7 (mod 8) the Jacobi condition is automatic (every divisor of f+1 is a Jacobi residue mod f).
// CLS = 7 : U_7(n): exists f ≡ 7 (mod 8), (-n mod f) | f+1
// CLS = 3 : U_3(n): exists f ≡ 3 (mod 8), (n/f) = -1, (-n mod f) | f+1   (i.e. r | f+1, r ≢ 2 mod 4)
// CLS = 0 : both (= U_II)
// Bitmap lookup for f <= FMAX, exact fallback over all f <= 2n+1 for the rest.
// Env overrides: Z60_FMOD/Z60_FRES (restrict f ≡ FRES mod FMOD; FMOD=0 means f ≡ 3 mod 4 all), Z60_TGT (0 U_II targets, 1 branch B, 2 branch A, 3 = B at all f plus A only at f ≡ 3 mod 8; use with FMOD=0).
// Usage: u7 CLS lo hi FMAX [primes_only] [mod4 (0 = all odd, 1, 3; 8 = n mod 840 in Mordell classes)]
// (without primes_only the P/C tag is meaningless: the prime sieve is skipped and every n is tagged P)
// Output: ZERO n P|C|S  lines and a summary.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static int CLS;
static int jac(u64 a,u64 n){ a%=n; int t=1; while(a){ while(!(a&1)){ a>>=1; u64 r=n&7; if(r==3||r==5) t=-t; } u64 tmp=a;a=n;n=tmp; if((a&3)==3&&(n&3)==3) t=-t; a%=n; } return n==1?t:0; }
static long FMOD=8, FRES=7; static int TGT=0; // env Z60_FMOD, Z60_FRES, Z60_TGT override CLS
static int classok(u64 f){ if(FMOD) return (long)(f%FMOD)==FRES%FMOD; int c=f&7; if(CLS==7) return c==7; if(CLS==3) return c==3; return c==3||c==7; }
// target type: 0 = r | f+1 (Jacobi filter at f ≡ 3 mod 8) = U_II targets; 1 = r | (f+1)/4 (branch B); 2 = 4 | r, r | f+1 (branch A)
static int tgt(u64 f,u64 r){ if(r==0||r>=f) return 0; if((f+1)%r) return 0; if(TGT==1) return ((f+1)/4)%r==0; if(TGT==2) return (r&3)==0;
  if(TGT==3){ if((f&7)==7) return ((f+1)/4)%r==0; return ((f+1)/4)%r==0 || (r&3)==0; } /* (★) everywhere + branch A only at f ≡ 3 (8) (cd odd) */
  if((f&7)==3 && (r&3)==2) return 0; return 1; }
static int hit(u64 n,u64 f){ u64 r=(f-n%f)%f; return tgt(f,r); }
static int tdprime(u64 n){ if(n<2) return 0; if(n%2==0) return n==2; for(u64 q=3;q*q<=n;q+=2) if(n%q==0) return 0; return 1; }
static int issq(u64 n){u64 r=(u64)sqrtl((long double)n); while(r*r>n)r--; while((r+1)*(r+1)<=n)r++; return r*r==n;}
int main(int argc,char**argv){
  if(argc<5){fprintf(stderr,"usage\n");return 1;}
  CLS=atoi(argv[1]); if(CLS==7){FMOD=8;FRES=7;} else if(CLS==3){FMOD=8;FRES=3;} else {FMOD=0;}
  if(getenv("Z60_FMOD")) FMOD=atol(getenv("Z60_FMOD")); if(getenv("Z60_FRES")) FRES=atol(getenv("Z60_FRES")); if(getenv("Z60_TGT")) TGT=atoi(getenv("Z60_TGT")); u64 lo=strtoull(argv[2],0,10),hi=strtoull(argv[3],0,10); long FMAX=atol(argv[4]);
  int primes_only=argc>5?atoi(argv[5]):0; int m4=argc>6?atoi(argv[6]):0;
  uint8_t **bm=calloc(FMAX+1,sizeof(uint8_t*));
  for(long f=3;f<=FMAX;f+=4){ if(!classok(f)) continue; bm[f]=calloc(f/8+1,1); if(!bm[f]) return 2;
    for(long r=1;r<f;r++){ if(!tgt(f,r)) continue; long t=f-r; bm[f][t>>3]|=1<<(t&7);} }
  u64 sq=primes_only?(u64)sqrtl((long double)hi)+2:2; char*small=calloc(sq+1,1); long*pr=malloc(sizeof(long)*(sq+1)); long np=0;
  for(u64 i=2;i<=sq;i++) if(!small[i]){pr[np++]=i; for(u64 j=i*i;j<=sq;j+=i) small[j]=1;}
  u64 SEG=1<<22; char*seg=malloc(SEG); long tested=0,late=0,zeros=0,zP=0,nsq=0; long maxf=0; u64 argm=0;
  for(u64 s=lo;s<hi;s+=SEG){u64 e=s+SEG<hi?s+SEG:hi; if(primes_only) memset(seg,0,e-s);
    if(primes_only) for(long i=0;i<np;i++){u64 q=pr[i]; if(q*q>=e) break; u64 st=((s+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<e;j+=q) seg[j-s]=1;}
    static const int MC[6]={1,121,169,289,361,529};
    for(u64 kb=(m4==8?s/840:0), nn=0;;){ u64 n;
      if(m4==8){ n=kb*840+MC[nn]; if(++nn==6){nn=0;kb++;} if(n>=e) { if(kb*840>=e) break; else continue; } if(n<s) continue; }
      else { n=s+nn; nn++; if(n>=e) break; if(!(n&1)||n<3) continue; if(m4&&(long)(n&3)!=m4) continue; }
      int isp=primes_only?!seg[n-s]:-1; if(primes_only&&!isp) continue;
      tested++; long best=0;
      for(long f=3;f<=FMAX;f+=4){ if(!bm[f]) continue; long t=(long)(n%f); if(bm[f][t>>3]&(1<<(t&7))){best=f;break;} }
      if(best){ if(best>maxf){maxf=best;argm=n;} continue; }
      if(issq(n)){ nsq++; continue; }
      late++; int found=0;
      u64 wf=0; for(u64 f=(FMAX/4)*4+3; f<=2*n+1; f+=4){ if(!classok(f)) continue; if(hit(n,f)){found=1;wf=f;break;} }
      if(found && getenv("Z60_LATE")){ printf("LATE %llu %llu\n",n,wf); }
      if(!found){ if(isp<0) isp=tdprime(n); zeros++; if(isp) zP++; printf("ZERO %llu %s\n",n,isp?"P":"C"); fflush(stdout);} } }
  printf("# FMOD=%ld FRES=%ld TGT=%d\n",FMOD,FRES,TGT); printf("# CLS=%d [%llu,%llu) FMAX=%ld primes_only=%d mod4=%d: tested %ld, odd squares (skipped, zero by T1) %ld, late %ld, zeros %ld (primes %ld); max bitmap witness %ld at %llu\n",
    CLS,lo,hi,FMAX,primes_only,m4,tested,nsq,late,zeros,zP,maxf,argm);
  return 0;}
