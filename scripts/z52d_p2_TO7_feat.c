// z52d Pass 2 TO7: per-(p,k,type) features for e-slice a=1 tests. p ≡ 1 mod 4 prime ≤ X; k ≡ 3 mod 4, k ≤ T.
// type 0 = Type I: M=(k p+1)/4 ; type 1 = Type II: M=(p+k)/4.
// Record (binary, little-endian, 12 bytes): uint32 p; uint16 k; uint8 type; uint8 omega; uint8 flags; uint8 pad; uint16 pad2; (flags bit0 = divisor hit b≡-1 mod k,
//  bit1 = squarefree M, bit2 = -1 in subgroup gen by prime-factor residues mod k, bit3 = -1 in subset products of distinct prime-factor residues mod k,
//  bit4 = M has a square factor > 1 among... (unused), ) and uint32 P1 (largest prime factor of M).
// usage: z52d_p2_TO7_feat X T out.bin
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef struct { uint32_t p; uint16_t k; uint8_t type, omega, flags, pad; uint16_t pad2; uint32_t P1; } rec_t;
static uint32_t *spf;
static int has_div_cong(long M, long k, int *om, int *sqf, uint32_t *P1, long *pr_out, int *ex_out, int *npo){
  int np=0; long pr[64]; int ex[64]; long m=M; *P1=1; *sqf=1;
  while(m>1){ long q=spf[m]; if(q==0) q=m; int e=0; while(m%q==0){m/=q;e++;} pr[np]=q; ex[np]=e; if(e>1) *sqf=0; if(q>*P1) *P1=q; np++; }
  *om=np; *npo=np;
  static long divs[1<<16]; int nd=1; divs[0]=1;
  for(int i=0;i<np;i++){ int cur=nd; long pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
  int hit=0; for(int j=0;j<nd;j++) if(divs[j]%k==k-1){ hit=1; break; }
  for(int i=0;i<np;i++) pr_out[i]=pr[i];
  return hit;
}
int main(int argc, char**argv){
  long X=atol(argv[1]); int T=atoi(argv[2]);
  long N = (long)X*T/4 + X + 16;
  spf = calloc(N+1, sizeof(uint32_t));
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
  FILE*f=fopen(argv[3],"wb");
  for(long p=5;p<=X;p+=4){
    if(spf[p]!=p) continue;
    for(long k=3;k<=T;k+=4){
      for(int type=0;type<2;type++){
        long M = type==0 ? (k*p+1)/4 : (p+k)/4;
        if(M<1) continue;
        int om,sqf,npo; uint32_t P1; long pr[64]; int ex[64];
        int hit = has_div_cong(M,k,&om,&sqf,&P1,pr,ex,&npo);
        // residues of prime factors mod k (k>=3); -1 == k-1
        int rs[64]; int nr=0; for(int i=0;i<npo;i++) rs[nr++]= (int)(pr[i]%k);
        // subgroup generated (closure) : BFS over residues of gcd=1 elements
        char in[1<<12]; memset(in,0,k); in[1%k]=1; int changed=1;
        // closure: start set {1}; repeatedly multiply by generators
        int cnt=1; int *lst=malloc(sizeof(int)*k); lst[0]=1%k;
        for(int i=0;i<nr;i++){ int g=rs[i]; if(g==0) continue; /* unit check */ }
        // generate group by repeated multiplication until stable
        int gen_hit=0;
        {
          char S[1<<12]; memset(S,0,k); S[1%k]=1; int sz=1; int prev=0;
          while(sz!=prev){ prev=sz; for(int a=0;a<k;a++) if(S[a]) for(int i=0;i<nr;i++){ int b=(a*rs[i])%k; if(!S[b]){S[b]=1; sz++;} } }
          gen_hit = S[(k-1)%k] ? 1 : 0;
        }
        // subset products of distinct prime factors (each used at most once), including empty product 1
        int sp_hit=0;
        {
          char R[1<<12]; memset(R,0,k); R[1%k]=1;
          for(int i=0;i<nr;i++){ char R2[1<<12]; memcpy(R2,R,k); for(int a=0;a<k;a++) if(R[a]) R2[(a*rs[i])%k]=1; memcpy(R,R2,k); }
          // -1 must be a NONEMPTY product in the target condition: for k>1 empty product is 1 != -1 so fine
          sp_hit = R[(k-1)%k] ? 1 : 0;
        }
        rec_t r; memset(&r,0,sizeof r);
        r.p=(uint32_t)p; r.k=(uint16_t)k; r.type=(uint8_t)type; r.omega=(uint8_t)(om>255?255:om);
        r.flags = (uint8_t)((hit?1:0) | (sqf?2:0) | (gen_hit?4:0) | (sp_hit?8:0));
        r.P1 = P1;
        fwrite(&r,sizeof r,1,f);
        free(lst);
      }
    }
  }
  fclose(f);
  return 0;
}
