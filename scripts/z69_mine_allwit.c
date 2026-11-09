// z69 MINE: list ALL U7 witnesses f (f = 7 mod 8, r = -p mod f in [1,f-1], r | f+1) of each input n (stdin),
// n odd <= ~1e12. Exhaustive in O(sqrt n * small):
//   (a) f <= F := floor(sqrt(n))*2+8 : direct check;
//   (b) f > F: canonical word (r, y, t), t = (n+r)/f <= (n + (f+1)/2)/f < n/F + 1, and r | n + t
//       (since n + t = r(y t - 1)); so enumerate t <= n/F + 1, divisors r of n + t, f = (n+r)/t, verify.
// Output: "W n count" then lines "f r y t" (y=(f+1)/r).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
typedef __uint128_t u128;
static u64 *primes; static int np;
static int cmpu(const void*a,const void*b){u64 x=*(u64*)a,y=*(u64*)b;return x<y?-1:x>y;}
static int divisors(u64 m, u64 *d){ // trial division with primes up to 1e6
  int nd=1; d[0]=1;
  for(int i=0;i<np && primes[i]*primes[i]<=m;i++){ u64 q=primes[i]; if(m%q) continue; int e=0; while(m%q==0){m/=q;e++;}
    int cur=nd; u64 pw=1; for(int k=1;k<=e;k++){pw*=q; for(int j=0;j<cur;j++) d[nd++]=d[j]*pw;} }
  if(m>1){ if(m > primes[np-1]*primes[np-1]) {fprintf(stderr,"factor bound\n"); exit(2);} int cur=nd; for(int j=0;j<cur;j++) d[nd++]=d[j]*m; }
  return nd;
}
static int iswit(u64 n,u64 f){ if(f%8!=7) return 0; u64 r=(f - n%f)%f; if(r==0) return 0; return (f+1)%r==0; }
int main(){
  int LIM=1000000; char *c=calloc(LIM+1,1); primes=malloc(sizeof(u64)*80000); np=0;
  for(int i=2;i<=LIM;i++) if(!c[i]){ primes[np++]=i; for(long j=(long)i*i;j<=LIM;j+=i) c[j]=1; }
  u64 n; u64 *d=malloc(sizeof(u64)*100000); u64 *ws=malloc(sizeof(u64)*2000000);
  while(scanf("%llu",&n)==1){
    u64 s=1; while((s+1)*(s+1)<=n) s++;
    u64 F=2*s+8; int nw=0;
    for(u64 f=7; f<=F && f<=2*n+1; f+=8) if(iswit(n,f)) ws[nw++]=f;
    u64 T=n/F+1;
    for(u64 t=1;t<=T;t++){ int nd=divisors(n+t,d);
      for(int i=0;i<nd;i++){ u64 r=d[i]; u64 m=n+r; if(m%t) continue; u64 f=m/t; if(f<=F || f>2*n+1) continue; if(iswit(n,f)) ws[nw++]=f; } }
    qsort(ws,nw,sizeof(u64),cmpu); int k=0; for(int i=0;i<nw;i++) if(i==0||ws[i]!=ws[i-1]) ws[k++]=ws[i]; nw=k;
    printf("W %llu %d\n",n,nw);
    for(int i=0;i<nw;i++){ u64 f=ws[i]; u64 r=f-n%f; printf("%llu %llu %llu %llu\n",f,r,(f+1)/r,(n+r)/f); }
    fflush(stdout);
  }
  return 0;
}
