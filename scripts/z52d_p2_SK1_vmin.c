// z52d pass2 SK1 (item Z0847): Vmin(p) census at primes p = 1 mod 4 up to N.
// Vmin(p) = least v >= 3 with v in 4Z or v = -p (mod 8), such that p+v has a divisor d = tv-1 (d = -1 mod v).
// (Equivalent to the minwords word sieve: tuv - u - v = p  <=>  u*(tv-1) = p+v.)
// Usage: z52d_p2_SK1_vmin N VMAXSEARCH   ; memory ~4 bytes * N (uint32 spf table).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned long long u64;
static uint32_t *spf;
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10); long VS=atol(argv[2]);
  u64 L=N+VS+10;
  spf=calloc(L+1,sizeof(uint32_t)); if(!spf){fprintf(stderr,"alloc\n");return 1;}
  for(u64 i=2;i*i<=L;i++) if(!spf[i]) for(u64 j=i*i;j<=L;j+=i) if(!spf[j]) spf[j]=(uint32_t)i;
  // divisor enumeration buffer
  static u64 divs[4096];
  u64 cnt[1000]; memset(cnt,0,sizeof cnt);
  u64 nprime=0, nrec=0, maxV=0, over116=0, over87=0, over31=0, none=0;
  u64 recp[200], recv[200]; int nr=0;
  FILE *big=fopen(argv[3],"w");
  for(u64 p=5;p<=N;p+=4){
    if(spf[p]) continue; // composite (spf set) ; p=1 mod 4 odd
    nprime++;
    u64 vfound=0;
    for(u64 v=3; v<=(u64)VS; v++){
      if(!((v%4==0) || ((v+p)%8==0)) ) continue;
      u64 n=p+v; int ok=0;
      // factor n
      u64 m=n; u64 pr[20]; int ex[20]; int k=0;
      while(m>1){ u64 q=spf[m]? spf[m] : m; int e=0; while(m%q==0){m/=q;e++;} pr[k]=q; ex[k]=e; k++; }
      // enumerate divisors, test d % v == v-1
      int nd=1; divs[0]=1;
      for(int i=0;i<k;i++){ int cur=nd; u64 pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
      for(int j=0;j<nd;j++){ if(divs[j]%v==(v-1)){ ok=1; break; } }
      if(ok){ vfound=v; break; }
    }
    if(!vfound){ none++; fprintf(big,"NONE %llu\n",(unsigned long long)p); continue; }
    if(vfound<1000) cnt[vfound]++;
    if(vfound>maxV){ maxV=vfound; if(nr<200){recp[nr]=p; recv[nr]=vfound; nr++;} }
    if(vfound>87){ fprintf(big,"V>87 %llu %llu\n",(unsigned long long)p,(unsigned long long)vfound); }
    if(vfound>87) over87++; if(vfound>116) over116++;
    if(vfound>31) over31++;
  }
  printf("N=%llu primes_1mod4=%llu none_le_VS=%llu maxVmin=%llu\n",N,nprime,none,maxV);
  printf("#Vmin>31=%llu #>87=%llu #>116=%llu\n",over31,over87,over116);
  printf("records (p,Vmin):"); for(int i=0;i<nr;i++) printf(" (%llu,%llu)",recp[i],recv[i]); printf("\n");
  printf("dist (v:count) for v<=40:"); for(int v=3;v<=40;v++) if(cnt[v]) printf(" %d:%llu",v,cnt[v]); printf("\n");
  fclose(big);
  return 0;
}
