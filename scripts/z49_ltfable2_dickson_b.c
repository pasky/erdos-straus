// Fast search for instances of Proposition 3.3(b) (X = 4, k = 1): the 8 linear forms printed by
//   scripts/z49_ltfable2_dickson.py b 4 1 ...  must be simultaneously prime.  Deterministic Miller–Rabin for 64-bit.
// usage: dickson_b smax   -> prints s and p for every instance; the python script re-checks the conclusion by brute force.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static uint64_t mulmod(uint64_t a,uint64_t b,uint64_t m){ return (u128)a*b%m; }
static uint64_t powmod(uint64_t a,uint64_t e,uint64_t m){ uint64_t r=1; a%=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1; } return r; }
static int isprime(uint64_t n){
  if(n<2) return 0; static const uint64_t sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n==sp[i]) return 1; if(n%sp[i]==0) return 0; }
  uint64_t d=n-1; int r=0; while((d&1)==0){ d>>=1; r++; }
  for(int i=0;i<12;i++){ uint64_t x=powmod(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int j=1;j<r;j++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
int main(int argc,char**argv){
  uint64_t smax=strtoull(argv[1],0,10);
  // forms (c, m): from the python script for X=4, k=1 (l_1 = 13, Q0 = 840, Q1 = 176400, M = 29811600, p0 = 28929601)
  const uint64_t c[8]={28929601ULL,1112677ULL,9643201ULL,7232401ULL,5785921ULL,21697201ULL,23143681ULL,19286401ULL};
  const uint64_t m[8]={29811600ULL,1146600ULL,9937200ULL,7452900ULL,5962320ULL,22358700ULL,23849280ULL,19874400ULL};
  long found=0;
  for(uint64_t s=1;s<=smax;s++){ int ok=1; for(int i=0;i<8&&ok;i++) ok=isprime(c[i]+m[i]*s);
    if(ok){ printf("s=%llu p=%llu\n",(unsigned long long)s,(unsigned long long)(c[0]+m[0]*s)); fflush(stdout); if(++found>=3) break; } }
  printf("# searched s <= %llu, found %ld\n",(unsigned long long)smax,found); return 0; }
