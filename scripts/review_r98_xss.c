/* R98 from-scratch targeted search at the point x(u11,u13) (x_q=1 off T={11,13}) for ET classes of
   families II3, I3, I1, II2 (ET Prop 1.9) with e (resp. f) <= X, NO cap on the T-level.
   Membership conditions (re-derived by R98 directly from the ET class definitions by CRT):
   II3 (a,d,e),(4ad,e)=1, n≡-4a^2d-e (4ade):  e≡-1 (4(ad)'), e≡-u_q (q^{v_q(ad)}), e'|4a^2d+1, q^{v_q(e)}|4a^2d+u_q
   I3  (c,d,f),(4cd,f)=1, n≡-f (4cd), n^2≡-4c^2d (f): f≡-1 (4(cd)'), f≡-u_q (q^{v_q(cd)}), f'|4c^2d+1, q^{v_q(f)}|u_q^2+4c^2d
   I1  (a,d,f), f|4a^2d+1, n≡-f (4ad):        f≡-1 (4(ad)'), f≡-u_q (q^{v_q(ad)}), f|4a^2d+1
   II2 (a,d,f), 4ad|f+1, n≡-4a^2d (f):        f'|4a^2d+1, q^{v_q(f)}|4a^2d+u_q
   Completeness: for II3/I3/I1 the T-free parts a',d' divide (e+1)/4; the T-exponents satisfy
   v_q(ad) <= v_q(e+u_q) (finite since e+u_q != 0); for II2 a,d|(f+1)/4 entirely.
   usage: review_r98_xss u11 u13 X   (u_q positive integers prime to q) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static uint32_t *spf;
static uint64_t mulm(uint64_t a,uint64_t b,uint64_t m){return (uint64_t)((u128)a*b%m);}
static int vq(uint64_t x,uint64_t q){int k=0; while(x%q==0){x/=q;k++;} return k;}
static uint64_t pw(uint64_t q,int k){uint64_t r=1; while(k--) r*=q; return r;}
/* value of 4*A^2*D + add  mod m, A,D given mod-reducible */
static uint64_t f4(uint64_t A,uint64_t D,uint64_t add,uint64_t m){
  if(m==1) return 0; uint64_t a=A%m; uint64_t r=mulm(mulm(mulm(4%m,a,m),a,m),D%m,m); return (uint64_t)(((u128)r+add)%m);}
static int ndiv; static uint64_t divs[1<<16];
static void divisors(uint64_t n){ /* divisors of n */
  ndiv=1; divs[0]=1;
  while(n>1){uint32_t p=spf[n]; int e=0; while(n%p==0){n/=p;e++;}
    int cur=ndiv; uint64_t pk=1; for(int k=1;k<=e;k++){pk*=p; for(int i=0;i<cur;i++) divs[ndiv++]=divs[i]*pk;}}
}
int main(int argc,char**argv){
  uint64_t u[2]={strtoull(argv[1],0,10),strtoull(argv[2],0,10)}; uint64_t X=strtoull(argv[3],0,10);
  const uint64_t Q[2]={11,13};
  uint64_t S=X/4+2; spf=calloc(S+1,4);
  for(uint64_t i=2;i<=S;i++) if(!spf[i]) for(uint64_t j=i;j<=S;j+=i) if(!spf[j]) spf[j]=(uint32_t)i;
  long hits=0, tested=0;
  for(uint64_t e=3;e<=X;e+=4){
    uint64_t N=(e+1)/4;
    int ve[2]; uint64_t eq[2], ep=e;
    for(int t=0;t<2;t++){ve[t]=vq(e,Q[t]); eq[t]=pw(Q[t],ve[t]); ep/=eq[t];}
    int vm[2]; for(int t=0;t<2;t++) vm[t]= ve[t]?0:vq(e+u[t],Q[t]);
    /* ---- II2: all (a,d) with ad | N ---- */
    divisors(N);
    { int nd=ndiv; static uint64_t dv[1<<16]; for(int i=0;i<nd;i++) dv[i]=divs[i];
      for(int i=0;i<nd;i++){ uint64_t a=dv[i], r=N/a;
        for(int j=0;j<nd;j++){ uint64_t d=dv[j]; if(r%d) continue; tested++;
          if(f4(a,d,1,ep)) continue;
          int ok=1; for(int t=0;t<2;t++) if(ve[t] && f4(a,d,u[t]%eq[t],eq[t])) ok=0;
          if(ok){hits++; printf("II2 a=%llu d=%llu f=%llu\n",(unsigned long long)a,(unsigned long long)d,(unsigned long long)e);}
        }}
    }
    /* ---- II3, I3, I1: T-free (a',d') with a'd' | N'' ---- */
    uint64_t Nn=N; while(Nn%11==0) Nn/=11; while(Nn%13==0) Nn/=13;
    divisors(Nn);
    int nd=ndiv; static uint64_t dv2[1<<16]; for(int i=0;i<nd;i++) dv2[i]=divs[i];
    for(int i=0;i<nd;i++){ uint64_t ap=dv2[i], r=Nn/ap;
      for(int j=0;j<nd;j++){ uint64_t dp=dv2[j]; if(r%dp) continue;
        for(int ia=0;ia<=vm[0];ia++) for(int id=0;ia+id<=vm[0];id++)
        for(int ja=0;ja<=vm[1];ja++) for(int jd=0;ja+jd<=vm[1];jd++){
          uint64_t a=ap*pw(11,ia)*pw(13,ja), d=dp*pw(11,id)*pw(13,jd); /* fits: <= N*(e+u) small */
          tested++;
          /* II3 */
          if(!f4(a,d,1,ep)){ int ok=1; for(int t=0;t<2;t++) if(ve[t] && f4(a,d,u[t]%eq[t],eq[t])) ok=0;
            if(ok){hits++; printf("II3 a=%llu d=%llu e=%llu\n",(unsigned long long)a,(unsigned long long)d,(unsigned long long)e);} }
          /* I3 (c=a): f'|4c^2d+1, q^v | u^2+4c^2d */
          if(!f4(a,d,1,ep)){ int ok=1; for(int t=0;t<2;t++) if(ve[t] && f4(a,d,mulm(u[t]%eq[t],u[t]%eq[t],eq[t]),eq[t])) ok=0;
            if(ok){hits++; printf("I3 c=%llu d=%llu f=%llu\n",(unsigned long long)a,(unsigned long long)d,(unsigned long long)e);} }
          /* I1: f | 4a^2d+1 */
          if(!f4(a,d,1,e)){hits++; printf("I1 a=%llu d=%llu f=%llu\n",(unsigned long long)a,(unsigned long long)d,(unsigned long long)e);}
        }
      }
    }
  }
  fprintf(stderr,"u=(%llu,%llu) X=%llu tested=%ld hits=%ld\n",(unsigned long long)u[0],(unsigned long long)u[1],(unsigned long long)X,tested,hits);
  return 0;
}
