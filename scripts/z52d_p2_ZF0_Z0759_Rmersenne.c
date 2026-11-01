// Z0759: exact R(n) for single large n (here n = 2^k - 1), R(n) = #{(C,u,v) >= 1 ordered : n = 4Cuv - u - v}
// (= sum_C #{d | 4Cn+1 : d = -1 mod 4C}, same count as col2 of scripts/z52b_fingerprint_words.c).
// Method: for u <= v (equivalently 4u^2 - 2u <= n) put w = 4Cu - 1 = (n+u)/v: w | n+u, w = -1 mod 4u, w*u <= n+u.
// Segmented sieve factors n+u for u in [1,U], U ~ sqrt(n)/2, with all primes <= sqrt(n+U); divisors enumerated per entry.
// R = 2*#{u<v} + #{u=v}. Also reports per-u contributions for small u and the list of (u,C,v) solutions with u<=v (first 40).
// usage: ./a.out k [k2]  (computes for n=2^k-1, k..k2);  ./a.out -n < list_of_n   (arbitrary n < 2^62, one per line; prints n R R_{min(u,v)<=2} R_{min(u,v) in B_k}; B_k={1,2} u {2^i+1: i=k mod 2}, k=floor(log2 n))
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static uint32_t *P; static long NP;
static void primes_upto(u64 L){ // simple segmented sieve
  u64 r=(u64)sqrtl((long double)L)+2; char *s=calloc(r+1,1); long cap=(long)(1.1*L/log((double)L)+1000); P=malloc(cap*4); NP=0;
  for(u64 i=2;i<=r;i++) if(!s[i]) for(u64 j=i*i;j<=r;j+=i) s[j]=1;
  uint32_t *sp=malloc(r*4); long ns=0; for(u64 i=2;i<=r;i++) if(!s[i]) sp[ns++]=i;
  u64 S=1<<24; char *b=malloc(S);
  for(u64 lo=2;lo<=L;lo+=S){ u64 hi=lo+S-1; if(hi>L)hi=L; memset(b,0,S);
    for(long t=0;t<ns;t++){ u64 q=sp[t]; if(q*q>hi)break; u64 st=((lo+q-1)/q)*q; if(st<q*q)st=q*q; for(u64 j=st;j<=hi;j+=q) b[j-lo]=1; }
    for(u64 j=lo;j<=hi;j++) if(!b[j-lo]) P[NP++]=(uint32_t)j; }
  free(b); free(sp); free(s);
}
#define MAXF 16
static u64 NL[1<<20]; static int NN=0;
int main(int argc,char**argv){
  int listmode=(argv[1][0]=='-');
  int k1=listmode?0:atoi(argv[1]), k2=listmode?0:(argc>2?atoi(argv[2]):k1);
  u64 nmax=(k2>=64)?0:((1ULL<<k2)-1);
  if(listmode){ u64 x; while(scanf("%llu",&x)==1){ NL[NN++]=x; if(x>nmax)nmax=x; } k1=0; k2=NN-1; } u64 Umax=(u64)((1+sqrtl(1+4.0L*nmax))/4)+2;
  u64 L=(u64)sqrtl((long double)(nmax+Umax))+2; primes_upto(L);
  fprintf(stderr,"primes to %llu: %ld\n",L,NP);
  u64 S=1<<22; uint32_t *fac=malloc(S*MAXF*4); uint8_t *nf=malloc(S);
  for(int k=k1;k<=k2;k++){
    u64 n=listmode?NL[k]:((1ULL<<k)-1); u64 U=(u64)((1+sqrtl(1+4.0L*n))/4)+2; while(U>0 && 4*(u128)U*U-2*U>n) U--;
    u64 sq=(u64)sqrtl((long double)(n+U))+1;
    u64 cnt_lt=0,cnt_eq=0,cnt12=0,cntB=0; int kk=63-__builtin_clzll(n); if(!listmode) kk=k; // parity class for the blocked set B_k
 int shown=0; char sol[4096]; sol[0]=0;
    for(u64 u0=1;u0<=U;u0+=S){ u64 len=S; if(u0+len-1>U) len=U-u0+1; memset(nf,0,len);
      for(long t=0;t<NP;t++){ u64 q=P[t]; if(q>sq)break; u64 r=(n+u0)%q; u64 i=r?q-r:0;
        for(;i<len;i+=q){ fac[i*MAXF+nf[i]++]=(uint32_t)q; } }
      for(u64 i=0;i<len;i++){ u64 u=u0+i, m=n+u, rem=m; u64 pr[MAXF+1]; int ex[MAXF+1], np=0;
        for(int j=0;j<nf[i];j++){ u64 q=fac[i*MAXF+j]; int e=0; while(rem%q==0){rem/=q;e++;} pr[np]=q; ex[np]=e; np++; }
        if(rem>1){ pr[np]=rem; ex[np]=1; np++; }
        // enumerate divisors
        static u64 dv[1<<17]; int nd=1; dv[0]=1;
        for(int j=0;j<np;j++){ int cur=nd; u64 pp=1; for(int e=1;e<=ex[j];e++){ pp*=pr[j]; for(int a=0;a<cur;a++) dv[nd++]=dv[a]*pp; } }
        u64 M=4*u;
        for(int a=0;a<nd;a++){ u64 w=dv[a]; if(w%M!=M-1) continue; if((u128)w*u>m) continue;
          u64 v=m/w; u64 C=(w+1)/M; if(v==u) cnt_eq++; else cnt_lt++; if(u<=2) cnt12+=(v==u)?1:2;
          { int inB=(u<=2); if(!inB && ((u-1)&(u-2))==0){ int i=__builtin_ctzll(u-1); if(((kk-i)&1)==0) inB=1; } if(inB) cntB+=(v==u)?1:2; }
          if(shown<40){ char b[96]; sprintf(b," (u=%llu,C=%llu,v=%llu)",u,C,v); if(strlen(sol)+strlen(b)<4000) strcat(sol,b); shown++; } }
      }
    }
    if(listmode){ printf("%llu %llu %llu %llu\n",n,2*cnt_lt+cnt_eq,cnt12,cntB); fflush(stdout); continue; }
    printf("k=%d n=%llu U=%llu R=%llu  [u<v:%llu u=v:%llu] sols(u<=v):%s\n",k,n,U,2*cnt_lt+cnt_eq,cnt_lt,cnt_eq,sol); fflush(stdout);
  }
}
