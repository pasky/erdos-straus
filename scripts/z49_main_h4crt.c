// Prime-Haar CRT model of H4: n has independent uniform unit residues mod high powers of each prime, n ≡ 1 (24).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef uint64_t u64; typedef int64_t i64;
static u64 s[2]={0x12345678abcdefULL,0x9e3779b97f4a7c15ULL};
static u64 rnd(void){u64 s1=s[0];const u64 s0=s[1];s[0]=s0;s1^=s1<<23;s[1]=s1^s0^(s1>>17)^(s0>>26);return s[1]+s0;}
static int *spf; static u64 *rp, *pw; static u64 *stamp; static u64 cur=0;
static u64 res_pp(u64 l){ // n mod l^E
  if(stamp[l]!=cur){ stamp[l]=cur; u64 q=pw[l]; u64 r;
    if(l==2){ r=(rnd()%(q/8))*8+1; } else if(l==3){ r=(rnd()%(q/3))*3+1; }
    else { do r=rnd()%q; while(r%l==0); }
    rp[l]=r; }
  return rp[l]; }
static i64 egcd_inv(i64 a,i64 m){ i64 g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; i64 b=a1; // inverse of a mod m
  i64 old_r=b,r=m,old_s=1,s_=0; while(r){i64 qq=old_r/r; i64 t=old_r-qq*r; old_r=r; r=t; t=old_s-qq*s_; old_s=s_; s_=t;} (void)g;(void)x;(void)x1;
  i64 v=old_s%m; if(v<0)v+=m; return v; }
static long CAP;
// factor x<=4*CAP*CAP? we only factor a and v (<=CAP) separately and 4.
static int fac(u64 x, u64 *pr, int *ex){ int k=0; while(x>1){ u64 l=spf[x]; int e=0; while(x%l==0){x/=l;e++;} pr[k]=l; ex[k]=e; k++;} return k; }
static u64 crt_mod(u64 *pr,int *ex,int k){ // n mod prod pr^ex
  u64 x=0, M=1;
  for(int i=0;i<k;i++){ u64 q=1; for(int j=0;j<ex[i];j++) q*=pr[i]; u64 r=res_pp(pr[i])%q;
    // combine x mod M with r mod q
    i64 inv=egcd_inv((i64)(M%q),(i64)q); u64 d=(r+q-(x%q))%q; u64 tt=(u64)(((u128)d*inv)%q); x = x + M*tt; M*=q; }
  return x; }
int main(int argc,char**argv){ long samples=atol(argv[1]); CAP=atol(argv[2]); s[0]^=atol(argv[3]);
 long L=CAP+10; spf=calloc(L+1,sizeof(int)); for(long i=2;i<=L;i++) if(!spf[i]) for(long j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i;
 rp=calloc(L+1,8); pw=calloc(L+1,8); stamp=calloc(L+1,8);
 for(long l=2;l<=L;l++) if(spf[l]==l){ u64 q=1; while((u128)q*l < ((u128)1<<40)) q*=l; pw[l]=q; }
 long hist[64]={0}, over=0;
 for(long it=0;it<samples;it++){ cur++; long H=-1;
  for(long v=2; v<=CAP; v++){
    u64 pr[32]; int ex[32]; int k=fac(v,pr,ex);
    u64 nv=crt_mod(pr,ex,k); u64 a=(v-nv)%v; if(a==0) continue; // a = -n mod v
    // need n mod 4*a*v: factor 4*a*v (gcd(a,v) may be >1 -> then no edge possible for prime-like n? if g=gcd(a,v)>1 then g | n -> impossible since units) 
    u64 g=a, h=v; while(h){u64 t=g%h; g=h; h=t;} if(g>1) continue;
    u64 m=4*a*v; u64 pr2[40]; int ex2[40]; int k2=0;
    // factor 4*a*v from factors of a, v, 4
    { u64 pa[32]; int ea[32]; int ka=fac(a,pa,ea); int e2=2; 
      for(int i=0;i<ka;i++){ if(pa[i]==2) e2+=ea[i]; else {pr2[k2]=pa[i];ex2[k2]=ea[i];k2++;} }
      for(int i=0;i<k;i++){ if(pr[i]==2) e2+=ex[i]; else {pr2[k2]=pr[i];ex2[k2]=ex[i];k2++;} }
      pr2[k2]=2; ex2[k2]=e2; k2++; }
    u64 nm=crt_mod(pr2,ex2,k2); // n mod m
    u64 s_=(nm+a+v)%m; if(s_%(a*v)) continue; // edge iff a v | n+a+v
    u64 t4=(s_/(a*v))&3; // t mod 4
    int slot=(t4==0)||((a&3)==0)||((v&3)==0)||(((t4*a+3)&3)==0)||(((t4*v+3)&3)==0);
    if(slot){H=v;break;}
  }
  if(H<0) over++; else { int b=0; while((1L<<(b+1))<=H) b++; hist[b]++; }
 }
 printf("samples=%ld cap=%ld over=%ld\n",samples,CAP,over);
 for(int k=2;k<=20;k++){ long c=over; for(int b=k;b<64;b++) c+=hist[b]; if((1L<<k)<=CAP) printf("X=%ld P(H>=X)=%.4g  count=%ld\n",1L<<k,(double)c/samples,c); }
}
