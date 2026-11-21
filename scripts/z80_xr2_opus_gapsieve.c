/* Opus round-2 independent threshold census for EXTREME §7 (no code shared with
   z52d/z80_gap_sieve).  Lists EVERY prime p in [lo,hi], p mod 840 in the six Mordell
   classes, with g(p)>T, together with g(p).
   Sieve: own segmented Eratosthenes on each class progression; then for every window
   m=3,7,..,T and every PRIME q<=Q with q=-1 (mod m) cross p=-m (mod q) [equivalent to p=-m mod 4q as p+m=0 mod 4]: then q | x=(p+m)/4
   and the divisors q,1 of p*x sum to 0 mod m, so g(p)<=m<=T (positive certificate only).
   Also composite d<=1e5 coprime to 210, d=-1 (mod m), same certificate.
   Survivors: exact g by the brute-force engine of z80_xr2_opus_gap.c (h | s^2 criterion).
   Usage: lo hi T Q */
#define main opus_gap_unused_main
#include "z80_xr2_opus_gap.c"
#undef main
#define SL (1<<23)
static unsigned char bits[SL];
static long long egcd(long long a,long long b,long long*x,long long*y){if(!b){*x=1;*y=0;return a;}long long x1,y1,g=egcd(b,a%b,&x1,&y1);*x=y1;*y=x1-(a/b)*y1;return g;}
/* first index j>=0 with n0+840*j = c (mod M), or -1 if incompatible; period via *per */
static long long first_j(u64 n0,long long c,long long M,long long*per){long long x,y;long long g=egcd(840%M,M,&x,&y);
 long long need=((c-(long long)(n0%M))%M+M)%M;if(need%g)return -1;long long Mg=M/g;*per=Mg;
 long long inv=((x%Mg)+Mg)%Mg;return (long long)((__int128)(need/g)*inv%Mg);}
int main(int ac,char**av){if(ac!=5)return 1;u64 lo=strtoull(av[1],0,10),hi=strtoull(av[2],0,10);int T=atoi(av[3]);long Q=atol(av[4]);
 for(int q=2;nsp<200;q++){int ok=1;for(int i=0;i<nsp&&sp[i]*sp[i]<=q;i++)if(q%sp[i]==0){ok=0;break;}if(ok)sp[nsp++]=q;}
 u64 R=(u64)sqrtl((long double)hi)+2;u64 RQ=R>(u64)Q?R:(u64)Q;unsigned char*c=calloc(RQ+1,1);u64*bp=malloc(sizeof(u64)*(RQ/2+10));long nb=0;
 for(u64 i=2;i<=RQ;i++)if(!c[i]){bp[nb++]=i;for(u64 j=i*i;j<=RQ;j+=i)c[j]=1;}free(c);
 /* crossing list (m,q): for odd q not dividing 840, q | x=(p+m)/4 iff p=-m (mod q). */
 long ncr=0,cap=1<<22;int*cm=malloc(sizeof(int)*cap);u64*cq=malloc(sizeof(u64)*cap);u64*ci=malloc(sizeof(u64)*cap);
 for(int m=3;m<=T;m+=4)for(long t=0;t<nb&&bp[t]<=(u64)Q;t++)if((bp[t]+1)%m==0&&840%bp[t]){if(ncr>=cap){fprintf(stderr,"cap\n");return 5;}cm[ncr]=m;cq[ncr]=bp[t];long long x,y;egcd(840%bp[t],bp[t],&x,&y);ci[ncr]=((x%(long long)bp[t])+bp[t])%bp[t];ncr++;}
 /* also every composite d<=DC coprime to 210 with d=-1 (mod m): d | x gives divisors d,1 (still a positive certificate). */
 { const u64 DC=100000; for(int m=3;m<=T;m+=4)for(u64 d=m-1;d<=DC;d+=m){if(d%2==0||d%3==0||d%5==0||d%7==0)continue;int isp=1;for(u64 r=2;r*r<=d;r++)if(d%r==0){isp=0;break;}if(isp)continue;
   if(ncr>=cap){fprintf(stderr,"cap\n");return 5;}cm[ncr]=m;cq[ncr]=d;long long x,y;egcd(840%d,d,&x,&y);ci[ncr]=((x%(long long)d)+d)%d;ncr++;}}
 u64*inv=malloc(sizeof(u64)*nb);for(long t=0;t<nb;t++){u64 q=bp[t];if(840%q==0){inv[t]=0;continue;}long long x,y;egcd(840%q,q,&x,&y);inv[t]=((x%(long long)q)+q)%q;}
 const int cls[6]={1,121,169,289,361,529};u64 surv=0,cand=0,found=0;
 for(int a=0;a<6;a++){u64 n0=lo+((cls[a]+840-lo%840)%840);
  for(u64 base=n0;base<=hi;base+=840ULL*SL){u64 len=(hi-base)/840+1;if(len>SL)len=SL;memset(bits,0,len);u64 last=base+840ULL*(len-1);
   for(long t=0;t<nb;t++){u64 q=bp[t];if(q*q>last)break;if(840%q==0)continue;
    u64 j=(u64)((__int128)((q-base%q)%q)*inv[t]%q);if(base+840ULL*j==q)j+=q;for(u64 k=j;k<len;k+=q)bits[k]=1;}
   for(u64 k=0;k<len;k++)if(!bits[k])cand++;
   for(long i=0;i<ncr;i++){u64 q=cq[i];u64 need=(q-(base+cm[i])%q)%q;u64 j=(u64)((__int128)need*ci[i]%q);for(u64 k=j;k<len;k+=q)bits[k]=1;}
   for(u64 k=0;k<len;k++)if(!bits[k]){u64 p=base+840ULL*k;surv++;if(p<=(u64)T+4){continue;}int g=gap(p);if(g>T){found++;printf("BIG %llu %d\n",(unsigned long long)p,g);fflush(stdout);}}
  }}
 printf("DONE lo=%llu hi=%llu T=%d Q=%ld crossings=%ld Mprimes=%llu exact_survivors=%llu bigcount=%llu\n",(unsigned long long)lo,(unsigned long long)hi,T,Q,ncr,(unsigned long long)cand,(unsigned long long)surv,(unsigned long long)found);return 0;}
