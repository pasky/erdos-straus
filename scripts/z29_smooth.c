// z29_smooth.c — O259: b = 1 line at primes p = m + 1, m Y-smooth, 4 | m, p <= X (up to ~1e15).
// Bounded search over the mutual-shift form (B1_LINE.md Lemma 1.1): least s <= S with a divisor t > s of p + s,
// (p + s)/t == -1 (mod s), 4 | s or 4 | t.  Factorisation by trial division + Pollard–Brent (__int128), Miller–Rabin
// deterministic for 64-bit.  Unresolved primes (no hit for s <= S) are printed for an exact segmented check.
// usage: z29_smooth X Y S      e.g. z29_smooth 1000000000000000 11 2000
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __uint128_t u128; typedef long long ll;
static u64 mulm(u64 a,u64 b,u64 m){ return (u128)a*b%m; }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 B[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%B[i]==0) return n==B[i]; } u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(B[i],d,n); if(x==1||x==n-1) continue; int ok=0; for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; } return 1; }
static u64 gcdu(u64 a,u64 b){ while(b){ u64 t=a%b; a=b; b=t;} return a; }
static u64 rho(u64 n){ if(!(n&1)) return 2; for(u64 c=1;;c++){ u64 y=2,x,g=1,q=1,ys=2; u64 m=128,r=1;
    do{ x=y; for(u64 i=0;i<r;i++) y=(mulm(y,y,n)+c)%n; u64 k=0; do{ ys=y; for(u64 i=0;i<m && i<r-k;i++){ y=(mulm(y,y,n)+c)%n; q=mulm(q,x>y?x-y:y-x,n);} g=gcdu(q,n); k+=m; }while(k<r && g==1); r<<=1; }while(g==1);
    if(g==n){ do{ ys=(mulm(ys,ys,n)+c)%n; g=gcdu(x>ys?x-ys:ys-x,n);}while(g==1); }
    if(g!=n) return g; } }
static u64 pf[64]; static int npf;
static void fac_rec(u64 n){ if(n==1) return; if(isprime(n)){ pf[npf++]=n; return; } u64 d=rho(n); fac_rec(d); fac_rec(n/d); }
static u64 pr[64]; static int ex[64]; static u64 dv[1<<17];
static int factor(u64 n){ npf=0; for(u64 q=2;q<1000 && q*q<=n;q++) while(n%q==0){ pf[npf++]=q; n/=q; } fac_rec(n);
  // sort + group
  for(int i=1;i<npf;i++){ u64 v=pf[i]; int j=i-1; while(j>=0&&pf[j]>v){pf[j+1]=pf[j];j--;} pf[j+1]=v; }
  int k=0; for(int i=0;i<npf;i++){ if(k&&pr[k-1]==pf[i]) ex[k-1]++; else { pr[k]=pf[i]; ex[k]=1; k++; } } return k; }
static int gendiv(int k){ int nd=1; dv[0]=1; for(int i=0;i<k;i++){ int cur=nd; u64 pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) dv[nd++]=dv[j]*pp; } } return nd; }
static int hit(u64 p,u64 s){ if(!((s&3)==0||(s&3)==3)) return 0; u64 n=p+s; int k=factor(n); int nd=gendiv(k);
  for(int i=0;i<nd;i++){ u64 t=dv[i]; if(t<=s) continue; u64 u=n/t; if((u+1)%s) continue; if(!((s&3)==0||(t&3)==0)) continue; return 1; } return 0; }
static u64 X; static int Y; static u64 S; static int sp[16]; static int nsp;
static u64 cnt=0,cnt1=0,unres=0,rec=0,rec5=0,recp=0; static u64 hist[16];
static void test(u64 m){ if(m%4) return; u64 p=m+1; if(p<5||!isprime(p)) return; cnt++; if(p%8==1) cnt1++;
  u64 first=0; for(u64 s=1;s<=S;s++) if(hit(p,s)){ first=s; break; }
  if(!first){ unres++; printf("UNRESOLVED p=%llu (no hit s<=%llu)\n",p,S); fflush(stdout); return; }
  int b=0; while((1ULL<<(b+1))<=first&&b<15) b++; hist[b]++;
  if(p%8==5){ if(first>rec5) rec5=first; } else if(first>rec){ rec=first; recp=p; printf("record (p=1 mod 8) least s=%llu at p=%llu\n",first,p); fflush(stdout);} }
static void gen(int i,u64 m){ if(i==nsp){ test(m); return; } u64 q=sp[i]; while(1){ gen(i+1,m); if(m>X/q) break; m*=q; } }
int main(int argc,char**argv){ X=strtoull(argv[1],0,10); Y=atoi(argv[2]); S=strtoull(argv[3],0,10);
  for(int q=2;q<=Y;q++){ int pq=1; for(int r=2;r*r<=q;r++) if(q%r==0) pq=0; if(pq) sp[nsp++]=q; }
  gen(0,1);
  printf("X=%llu Y=%d S=%llu: primes p=m+1 (m Y-smooth, 4|m): %llu (p=1 mod 8: %llu), unresolved %llu, max least s %llu (p=1(8), at %llu), %llu (p=5(8))\n",X,Y,S,cnt,cnt1,unres,rec,recp,rec5);
  printf("hist log2(least s):"); for(int b=0;b<16;b++) printf(" %llu",hist[b]); printf("\n"); return 0; }
