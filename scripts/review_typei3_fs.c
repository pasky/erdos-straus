/* R72 from-scratch f-graded certificate search at the sign point x = (w at 2; -1 at r; 1 elsewhere).
   Written independently of typei3_fsearch.c, directly from the definition (POINTWISE_TYPEI2 (2.2)):
   (c,k,F) certificate  <=>  v_r(c) odd, F | N = 1+4ck^2, F = -1 mod m' (odd r-free part of ck),
                             F = 1 mod r^{v_r(ck)}, F = -w mod 2^{v_2(4ck)}.
   For a divisor f of N: role F (F=f) or role e (F=N/f, f = F^{-1} mod 4ck, so f = -1 mod m', 1 mod r^v,
   w f = -1 mod 2^t).  Parametrise c = 2^al r^a c1, k = 2^ga r^b k1 (c1,k1 odd, prime to r).
   Necessary: c1 k1 | f+1, r^{a+b} | f-1, 2^t | f+w (role F) / w f+1 (role e), t = 2+al+ga,
   and f | 1 + 2^{2+al+2ga} r^{a+2b} c1 k1^2.  These are also sufficient (role e: N/f = f^{-1} mod 4ck).
   Usage: review_typei3_fs r w Ylo Yhi [mode]
     mode absent: print "C c k F role f t ga"  (all certificates with a divisor f in [Ylo,Yhi), w integer)
     mode "tmin": for f = 7 mod 16 print "B f tmin" where tmin = min over hits of max(4, ceil((s+2)/2)), s<=78
   Factorisation: per-block sieve of g=f+1 over the progression, inverse via Fermat. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64; typedef long long i64; typedef unsigned __int128 u128; typedef __int128 i128;
static u64 mm(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 pw(u64 a,u64 e,u64 m){u64 r=1%m;a%=m;while(e){if(e&1)r=mm(r,a,m);a=mm(a,a,m);e>>=1;}return r;}
static int v2i(i128 x){ if(x==0) return 1000; if(x<0)x=-x; int e=0; while(!(x&1)){x>>=1;e++;} return e; }
#define BL 262144
#define MF 20
static u64 cof[BL]; static int nfac[BL]; static u64 P[BL][MF]; static int E[BL][MF];
static void p128(u128 x){char b[60];int i=59;b[i]=0;if(!x){putchar('0');return;}while(x){b[--i]='0'+(int)(x%10);x/=10;}fputs(b+i,stdout);}
int main(int argc,char**argv){
  if(argc<5){fprintf(stderr,"usage\n");return 2;}
  i64 r=atoll(argv[1]), w=atoll(argv[2]); u64 Ylo=strtoull(argv[3],0,10), Yhi=strtoull(argv[4],0,10);
  int tmin_mode = argc>5 && !strcmp(argv[5],"tmin");
  /* sieve primes up to sqrt(Yhi+1) */
  u64 L=2; while(L*L<=Yhi+1) L++; L++;
  char *isc=calloc(L+1,1); u64 *pr=malloc(sizeof(u64)*(L+1)); int npr=0;
  for(u64 i=2;i<=L;i++){ if(isc[i]) continue; pr[npr++]=i; for(u64 j=i*i;j<=L;j+=i) isc[j]=1; }
  u64 Mod=4*(u64)r; u64 res=0; int found=0;
  for(u64 x=0;x<Mod;x++){ if(x%r==1 && (((i64)x+w)%4+4)%4==0){res=x;found=1;break;} }
  if(!found){fprintf(stderr,"no residue\n");return 2;}
  /* NB both roles: w f = -1 mod 4 <=> f = -w mod 4 since w^2=1 mod 8 for odd w. */
  u64 first = Ylo + ((res + Mod - Ylo%Mod)%Mod);
  u64 ntested=0, nhits=0;
  static u64 cp[1<<20], kp[1<<20];
  for(u64 b0=first; b0<Yhi; b0 += (u64)BL*Mod){
    u64 cnt=BL; if(b0+(BL-1)*Mod>=Yhi) cnt=(Yhi-1-b0)/Mod+1;
    for(u64 j=0;j<cnt;j++){ u64 g=b0+j*Mod+1; cof[j]=g; nfac[j]=0; }
    /* remove powers of 2 first */
    for(u64 j=0;j<cnt;j++){ while(!(cof[j]&1)) cof[j]>>=1; }
    for(int q=1;q<npr;q++){ u64 p=pr[q]; if(p*p>Yhi+1) break; if(p==(u64)r) continue;
      /* j with b0+1+j*Mod = 0 mod p  ->  j = -(b0+1) * Mod^{-1} mod p */
      u64 inv=pw(Mod%p,p-2,p); u64 j0=mm((p-(b0+1)%p)%p,inv,p);
      for(u64 j=j0;j<cnt;j+=p){ int e=0; while(cof[j]%p==0){cof[j]/=p;e++;} if(e){P[j][nfac[j]]=p;E[j][nfac[j]]=e;nfac[j]++;} }
    }
    for(u64 j=0;j<cnt;j++){
      u64 f=b0+j*Mod; if(f<Ylo||f>=Yhi||f<2) continue; ntested++;
      if(cof[j]>1){ if(cof[j]%r==0){fprintf(stderr,"BUG r|f+1\n");return 4;} P[j][nfac[j]]=cof[j];E[j][nfac[j]]=1;nfac[j]++; }
      int TF=v2i((i128)f+w), Te=v2i((i128)w*(i128)f+1);
      if(tmin_mode){ if(f%16!=7) continue; TF=Te=40; }
      else if(TF>=200||Te>=200){ fprintf(stderr,"infinite depth at f=%llu\n",f); return 3; }
      int T = TF>Te?TF:Te; if(T<2) continue;
      int V=0; { u64 q=f-1; while(q && q%r==0){q/=r;V++;} } if(V<1) continue;
      /* enumerate (c1,k1) with c1*k1 | A = odd part of f+1 */
      int nd=1; cp[0]=1; kp[0]=1;
      for(int q=0;q<nfac[j];q++){ int cur=nd; u64 p=P[j][q]; int e=E[j][q];
        for(int z=0;z<cur;z++){ u64 pi=1; for(int i=0;i<=e;i++){ u64 pj=1; for(int jj=0;i+jj<=e;jj++){ if(i||jj){ cp[nd]=cp[z]*pi; kp[nd]=kp[z]*pj; nd++; } pj*=p; } pi*=p; } } }
      int tmin=99;
      for(int d=0; d<nd; d++){
        u64 c1=cp[d], k1=kp[d];
        u64 base=mm(mm(c1%f,k1%f,f),k1%f,f);  /* c1 k1^2 */
        for(int a=1;a<=V;a+=2) for(int b=0;a+b<=V;b++){
          u64 R=mm(base,pw((u64)r,a+2*b,f),f);
          /* need 2^s R = -1 mod f with s = 2+al+2ga; t=2+al+ga */
          int smax = 2*T-2; u64 x=mm(R,4%f,f);
          for(int s=2;s<=smax;s++){ if(s>2){ x<<=1; if(x>=f) x-=f; }
            if((x+1)%f!=0) continue;
            if(tmin_mode){ int t=(s+3)/2; if(t<4)t=4; if(t<tmin)tmin=t; continue; }
            for(int role=0;role<2;role++){ int TR = role?Te:TF;
              for(int ga=0; 2*ga<=s-2; ga++){ int al=s-2-2*ga; int t=2+al+ga; if(t>TR) continue;
                nhits++; printf("C al=%d a=%d c1=%llu ga=%d b=%d k1=%llu role=%c f=%llu t=%d\n", al,a,c1,ga,b,k1, role?'e':'F', f, t);
              }}
          }
        }
      }
      if(tmin_mode && tmin<99) printf("B %llu %d\n",f,tmin);
    }
  }
  printf("DONE r=%lld w=%lld [%llu,%llu) tested=%llu hits=%llu\n",r,w,Ylo,Yhi,ntested,nhits);
  return 0;
}
