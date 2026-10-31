/* z52c_rh_types.c (RESIDUE_HARDNESS.md §1): exact tuple counts of the Elsholtz–Tao Type I and Type II certificate families
   at every integer v in [lo, hi], plain and with prime-local-density weights.
   Type II:  (a,b,c,d) in N^4, gcd(a,b) = 1, c | a+b, v = 4abd - s, s = (a+b)/c   (4/v = 1/(abd) + 1/(acdv) + 1/(bcdv));
             for fixed (a,b,c) the values form the AP v = -s (mod 4ab); it contains primes only if gcd(s, 2ab) = 1.
   Type I :  (a,b,e,d) in N^4, gcd(a,b) = 1, e | a+b, e*v = 4abd - 1 (4/v = 1/(abdv) + 1/(acd) + 1/(bcd), c = (a+b)/e);
             equivalently e | M := 4a^2 d + 1 and b = -a (mod e); for fixed (a,d,e) the values form an AP mod 4ad of units.
   (★) = Type II with c = 1 and gcd(a,b) = 1 (counted separately as RS).
   Weight w (prime model): prod over primes l > 13 dividing the AP modulus of l/(l-1), times 1[AP contains units mod 2*3*..*13
   and mod its modulus]; the factors at l <= 13 are dropped (they are handled by restricting to 13-rough v in class r).
   All counts are ORDERED in (a,b) (= ordered (y,z)); for primes p: TI = 2 k1(p), TII = 2 k2(p) up to y = z degeneracies.
   usage: ./z52c_rh_types lo hi outprefix [q0 [K J]]  -> outprefix_{TI,TIw,TII,TIIw,RS}.f32 (index v - lo)                         */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 gcdu(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
static u64 mulm(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static int isprime64(u64 n){ if(n<2) return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0; for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
static u64 rho(u64 n){ if(n%2==0) return 2; for(u64 c=1;;c++){ u64 x=2,y=2,d=1,q=1; int k=0;
    while(d==1){ x=(mulm(x,x,n)+c)%n; y=(mulm(y,y,n)+c)%n; y=(mulm(y,y,n)+c)%n; q=mulm(q,x>y?x-y:y-x,n); if(++k%64==0||q==0){ d=gcdu(q?q:(x>y?x-y:y-x),n); if(q==0) break; } }
    if(d==1){ x=2;y=2; do{ x=(mulm(x,x,n)+c)%n; y=(mulm(y,y,n)+c)%n; y=(mulm(y,y,n)+c)%n; d=gcdu(x>y?x-y:y-x,n);}while(d==1); }
    if(d!=n) return d; } }
static int nf; static u64 fp[64]; static int fe[64];
static void addp(u64 p){ for(int i=0;i<nf;i++) if(fp[i]==p){fe[i]++;return;} fp[nf]=p; fe[nf]=1; nf++; }
static void fac(u64 n){ if(n==1) return; if(isprime64(n)){ addp(n); return; } u64 d=rho(n); fac(d); fac(n/d); }
static void factor(u64 n){ nf=0; static const int sp[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
  for(int i=0;i<15;i++){ while(n%sp[i]==0){ addp(sp[i]); n/=sp[i]; } }
  fac(n); }
static int nd; static u64 dv[1<<16];
static void gendiv(int i,u64 d){ if(i==nf){ dv[nd++]=d; return; } u64 x=d; for(int e=0;e<=fe[i];e++){ gendiv(i+1,x); x*=fp[i]; } }
static int *spf; static float *wl; static long NTAB; static void factor(u64 n); /* wl[k] = prod_{l | k, l > 13} l/(l-1), k <= NTAB */
/* w(x*y) over DISTINCT primes l > 13 of x*y (R-review fix: wl[x]*wl[y] counted common primes twice); x <= NTAB, y any */
static float wpair(u64 x, u64 y){
  float w = wl[x]; u64 g;
  if(y <= (u64)NTAB){ u64 r=y; while(r>1){ u64 l=spf[r]; while(r%l==0) r/=l; if(l>13 && x%l) w*=(float)l/(float)(l-1); } return w; }
  factor(y); for(int i=0;i<nf;i++){ g=fp[i]; if(g>13 && x%g) w*=(float)g/(float)(g-1); } return w; }
int main(int argc,char**argv){
  long lo=atol(argv[1]), hi=atol(argv[2]); long W=hi-lo+1; char fn[512];
  long N=hi+10; NTAB=N; spf=calloc(N+1,sizeof(int));
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i;
  wl=malloc((N+1)*sizeof(float)); wl[1]=1;
  for(long k=2;k<=N;k++){ long l=spf[k], r=k; while(r%l==0) r/=l; wl[k]=wl[r]*(l>13 ? (float)l/(float)(l-1) : 1.0f); }
  float *TI=calloc(W,4),*TIw=calloc(W,4),*TII=calloc(W,4),*TIIw=calloc(W,4),*RS=calloc(W,4);
  /* optional 4th arg q0: also output the weighted counts restricted to tuples whose AP modulus is divisible by q0
     (the 'pair term' of RESIDUE_HARDNESS §1.2/§3), as TIwq, TIIwq */
  long q0 = argc>4 ? atol(argv[4]) : 0;
  /* optional 5th/6th args K J: only a = J (mod K) in both loops (parallel partial sums; outputs are additive) */
  long SK = argc>6 ? atol(argv[5]) : 1, SJ = argc>6 ? atol(argv[6]) : 0; float *TIwq=calloc(W,4),*TIIwq=calloc(W,4);
  /* ---- Type II, a <= b (weight 2 if a < b). v >= 4abd - (a+b) >= 2b(2a-1) so b <= hi/2. ---- */
  for(long a=1; 4*a*a-2*a<=hi; a++){ if(a%SK!=SJ) continue; for(long b=a; 4*a*b-a-b<=hi; b++){
    if(gcdu(a,b)!=1) continue; /* canonical: a/b = y/z in lowest terms (ET); else tuples (ka,kb,kc,d/k^2) repeat */
    long m=a+b; /* divisors c of m */
    nf=0; { long x=m; while(x>1){ long l=spf[x]; int e=0; while(x%l==0){x/=l;e++;} fp[nf]=l; fe[nf]=e; nf++; } }
    nd=0; gendiv(0,1);
    long q=4*a*b; float wab=wl[a]*wl[b]; float mult=(a<b)?2.0f:1.0f; int cop=1;
    for(int i=0;i<nd;i++){ long s=m/dv[i];
      int unit = (gcdu(s,2*a*b)==1); /* AP -s mod 4ab consists of units */
      float w = unit ? wab : 0.0f;
      long d0 = (lo+s+q-1)/q; if(d0<1) d0=1;
      int pq = q0 && (q%q0==0);
      for(long v=q*d0-s; v<=hi; v+=q){ long k=v-lo; TII[k]+=mult; TIIw[k]+=mult*w; if(pq) TIIwq[k]+=mult*w; if(dv[i]==1 && cop) RS[k]+=mult; }
    }
  }}
  /* ---- Type I, a <= b (weight 2 if a < b). ad <= (hi+1)/2; e | M = 4a^2 d + 1, b = -a mod e, b >= a. ---- */
  for(long a=1; 2*a<=hi+1; a++){ if(a%SK!=SJ) continue; for(long d=1; 2*a*d<=hi+1; d++){
    u64 M=4ULL*a*a*d+1; factor(M); nd=0; gendiv(0,1);
    long q=4*a*d; float wad = wl[a*d]; /* ad <= (hi+1)/2 <= NTAB: distinct primes of ad */
    for(int i=0;i<nd;i++){ u64 e=dv[i];
      /* b in [max(a, (e*lo+1)/(4ad)), (e*hi+1)/(4ad)], b = -a (mod e) */
      u128 bl=((u128)e*lo+1+q-1)/q; if(bl<(u128)a) bl=a; u128 bh=((u128)e*hi+1)/q; if(bl>bh) continue;
      u64 r=(u64)((e-(a%e))%e); /* b = r mod e */
      u128 b=bl + ((r + e - (u64)(bl%e))%e);
      for(; b<=bh; b+=e){ if(gcdu((u64)b,(u64)a)!=1) continue; u128 num=(u128)q*b-1; u64 v=(u64)(num/e); long k=(long)v-lo; if(k<0||k>=W) continue;
        /* ordered tuple (a,b,e,d): AP modulus 4ad; its mirror (b,a,e,d) (if b > a) has AP modulus 4bd (R-review fix: was
           given the 4ad weight too). The mirror's own weight/pair predicate are used. */
        TI[k]+=1; TIw[k]+=wad; if(q0 && q%q0==0) TIwq[k]+=wad;
        if((u64)b>(u64)a){ float wbd=wpair((u64)d,(u64)b); TI[k]+=1; TIw[k]+=wbd; if(q0 && ((u64)b%(u64)q0==0 || d%q0==0)) TIwq[k]+=wbd; } }
    }
  }}
  const char*nm[7]={"TI","TIw","TII","TIIw","RS","TIwq","TIIwq"}; float*ar[7]={TI,TIw,TII,TIIw,RS,TIwq,TIIwq};
  for(int j=0;j<(q0?7:5);j++){ sprintf(fn,"%s_%s.f32",argv[3],nm[j]); FILE*f=fopen(fn,"wb"); fwrite(ar[j],4,W,f); fclose(f); }
  return 0;
}
