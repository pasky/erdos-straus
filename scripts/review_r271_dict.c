/* R271 from-scratch check of HARD_PAIR Thm 1.2 / Cor 1.3 (does not reuse z34_* code).
   For each prime p = 1 mod 4, p <= N:
   (A) Type A cp + a + 1 = 4acd by enumerating a (c(4ad-p) = a+1, d unique per a);
   (B) slice scan over all q = 3 mod 4 (composite included), q <= QM*p: c_q = -p^{-1} mod q, test c_q | h;
   (C) integral Astra sources: q = 4 m^2 H - 1 with q | p m^2 + 1, m^2 <= (p+5)/4, q <= QM*p;
   (D) split classification of Type A slices: -p a QR mod every prime factor of q.
   Usage: review_r271_dict N QM   */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static int *spf;
static ll pw(ll b, ll e, ll m){ ll r=1; b%=m; if(b<0)b+=m; while(e){ if(e&1) r=(__int128)r*b%m; b=(__int128)b*b%m; e>>=1;} return r; }
static ll inv(ll a, ll m){ ll g=m, x=0, x1=1, a1=a%m; ll b=a1; /* ext gcd */
  ll r0=m, r1=b, s0=0, s1=1; while(r1){ ll t=r0/r1, tmp; tmp=r0-t*r1; r0=r1; r1=tmp; tmp=s0-t*s1; s0=s1; s1=tmp; }
  (void)g;(void)x;(void)x1; if(r0!=1) return -1; s0%=m; if(s0<0) s0+=m; return s0; }
int main(int argc, char **argv){
  ll N = atoll(argv[1]); ll QM = atoll(argv[2]);
  ll L = QM*N*4+10; spf = calloc(L+1, sizeof(int));
  for(ll i=2;i<=L;i++) if(!spf[i]) for(ll j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i;
  char *markA = calloc(L+1,1), *markB = calloc(L+1,1);
  ll np=0, nsol=0, nsplit=0, nnon=0, nsq=0, nfail=0, nnoint=0, mism=0, bad11=0;
  ll maxratio_num=0; int first=0;
  for(ll p=5;p<=N;p+=4){ if(spf[p]!=p) continue; np++;
    memset(markA,0,QM*p+10); memset(markB,0,QM*p+10);
    ll cntA=0, cntSq=0;
    for(ll a=1; 3*a <= p+1; a++){ ll d = p/(4*a)+1; ll g = 4*a*d - p; if(g > a+1) continue;
      if((a+1)%g) continue; ll c=(a+1)/g; ll q=4*c*d-1;
      if(c*p+a+1 != 4*a*c*d){ printf("IDENTITY FAIL p=%lld\n",p); mism++; }
      if(q > QM*p){ printf("q beyond scan p=%lld q=%lld\n",p,q); mism++; continue; }
      if(markA[q]){ printf("two TypeA on one slice p=%lld q=%lld\n",p,q); mism++; }
      markA[q]=1; cntA++;
      ll cq = (q - inv(p%q,q))%q; if(cq!=c){ printf("c!=c_q p=%lld q=%lld\n",p,q); mism++; }
      if(12*c > p+7){ printf("c bound fail p=%lld c=%lld\n",p,c); mism++; }
      /* split? */
      int split=1; ll t=q; while(t>1){ ll l=spf[t]; while(t%l==0) t/=l; if(pw((l-p%l)%l,(l-1)/2,l)!=1) split=0; }
      if(split) nsplit++; else nnon++;
      ll r=1; while(r*r<c) r++; if(r*r==c) cntSq++;
    }
    /* (B) */
    ll cntB=0;
    for(ll q=3;q<=QM*p;q+=4){ if(q%p==0) continue; ll cq=(q-inv(p%q,q))%q; ll h=(q+1)/4; if(h%cq==0){ markB[q]=1; cntB++; if(!markA[q]){ printf("B not A p=%lld q=%lld\n",p,q); mism++; } } }
    if(cntB!=cntA){ printf("count mismatch p=%lld A=%lld B=%lld\n",p,cntA,cntB); mism++; }
    /* (C) */
    ll cntC=0;
    for(ll m=1; 4*m*m <= p+5; m++){ ll M=4*m*m; for(ll q=M-1; q<=QM*p; q+=M){ if((p*m*m+1)%q==0){ cntC++;
          if(!markA[q]){ printf("C not A p=%lld q=%lld m=%lld\n",p,q,m); mism++; }
          ll cq=(q-inv(p%q,q))%q; if(cq!=m*m){ printf("C c_q != m^2 p=%lld\n",p); mism++; } } } }
    if(cntC!=cntSq){ printf("square mismatch p=%lld C=%lld sq=%lld\n",p,cntC,cntSq); mism++; }
    nsol+=cntA; nsq+=cntSq;
    if(cntA==0){ nfail++; printf("TypeA failure p=%lld\n",p);
      ll t=(p+1)/2; while(t>1){ ll l=spf[t]; t/=l; if(l%4==3){ printf("  Cor1.3(ii) FAIL l=%lld\n",l); bad11++; } } }
    if(cntA>0 && cntSq==0){ nnoint++; if(first<12){ printf("noint %lld\n",p); first++; } }
  }
  printf("primes %lld TypeA %lld split %lld nonsplit %lld (%.4f) square-c %lld fails %lld TypeA-but-no-integral %lld mismatches %lld cor(ii)fail %lld\n",
    np,nsol,nsplit,nnon,(double)nnon/nsol,nsq,nfail,nnoint,mism,bad11);
  return 0; }
