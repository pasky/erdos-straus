// R267 from-scratch E_k solver: primes p <= P (p ∤ k) with k/p != 1/x+1/y+1/z (x<=y<=z positive integers).
// Method: p/k < x <= 3p/k; A/B = k/p - 1/x reduced; 1/y+1/z = A/B  <=>  (Ay-B)(Az-B) = B^2, so solvable iff
// B^2 has a divisor u <= B with u ≡ -B (mod A).  Divisors enumerated from the factorisation of B | p*x.
// Mode "brute" cross-checks against a naive triple search for p <= Pb.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static int *spf; static long SN;
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int found; static u64 gA,gB,gmodB;
static u64 pr[64]; static int ex[64]; static int nf;
static void rec(int i,u128 u){ if(found) return; if(u>gB) return;
  if(i==nf){ if(((u%gA)+gmodB)%gA==0) found=1; return; }
  u128 v=u; for(int e=0;e<=2*ex[i];e++){ if(v>gB) break; rec(i+1,v); v*=pr[i]; } }
static int two_term(u64 A,u64 B){ // B factorised from global table
  if(A==0) return 0; gA=A; gB=B; gmodB=B%A; found=0; rec(0,1); return found; }
static void addfac(u64 n){ while(n>1){ u64 q = (n<(u64)SN)? (u64)spf[n] : 0; if(!q){ // n prime (only p)
      q=n; }
    int e=0; while(n%q==0){n/=q;e++;}
    int j; for(j=0;j<nf;j++) if(pr[j]==q){ex[j]+=e;break;} if(j==nf){pr[nf]=q;ex[nf]=e;nf++;} } }
static int solvable(u64 k,u64 p){
  for(u64 x=p/k+1; x*k<=3*p; x++){ u64 A=k*x-p, B=p*x; u64 g=gcdu(A,B); A/=g; B/=g;
    nf=0; // factor B = p^? * (x part)
    u64 xb=B; if(xb%p==0){ int e=0; while(xb%p==0){xb/=p;e++;} pr[nf]=p;ex[nf]=e;nf++; }
    addfac(xb);
    if(two_term(A,B)) return 1; }
  return 0; }
static int brute(u64 k,u64 p){ // naive: x<=y<=z, r = k/p-1/x = A/B, y in (B/A, 2B/A], z = By/(Ay-B)
  for(u64 x=p/k+1;x*k<=3*p;x++){ u64 A=k*x-p,B=p*x; u64 y0=B/A+1; if(y0<x) y0=x;
    for(u64 y=y0; y*A<=2*B; y++){ u64 d=A*y-B; if(d && (B*y)%d==0) return 1; } }
  return 0; }
int main(int argc,char**argv){
  u64 k=atoll(argv[1]); u64 P=atoll(argv[2]); int bru=argc>3;
  SN=3*P+10; spf=calloc(SN,sizeof(int));
  for(long i=2;i<SN;i++) if(!spf[i]) for(long j=i;j<SN;j+=i) if(!spf[j]) spf[j]=i;
  long cnt=0; u64 last=0;
  for(u64 p=3;p<=P;p++){ if(spf[p]!=(int)p) continue; if(k%p==0) continue;
    int s=solvable(k,p);
    if(bru){ int b=brute(k,p); if(b!=s) printf("MISMATCH k=%llu p=%llu solver=%d brute=%d\n",k,p,s,b); }
    if(!s){ cnt++; last=p; if(!bru) printf("E k=%llu p=%llu\n",k,p); } }
  printf("k=%llu P=%llu exceptions=%ld last=%llu\n",k,P,cnt,last);
}
