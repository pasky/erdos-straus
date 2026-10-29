/* z51 forcing: forced-window statistics (EXSET_CHAR_FORCING §§2-4).
   For primes p == 1 (mod 8) in [P0, P1] (every STRIDE-th one), and every prime q == 3 (mod 4), 3 <= q <= Q, q != p:
     x = (p+q)/4,  window q is FORCED iff (q/p) = -1  (then x is a non-residue mod q).
     ok2  : -1 in R(x)   = { prod s^{e_s} : |e_s| <= v_s(x) } mod q        (solution with p | y, p | z)
     okF  : -1 in R(px)  = R(x) u p R(x) u p^{-1} R(x)                     (any solution with this x)
   For every forced Type-II failure the Kneser structure of Lemma 2.2 / Cor 2.3 is verified: some d | u, d > 1, with
   H = <g^{2d}>: no prime factor of x in -H, and Omega_out(x) := #{prime factors (with mult.) not in H} <= d - 1.
   Output: per q: forced, fail2, failF, unforced, unforced fail2; per p: number of forced windows and of forced successes.
   Usage: z51_forcing_windows P0 P1 STRIDE Q outprefix
   (STRIDE = spacing of sample points in units of 8; the first prime == 1 (8) at or after each point is used; STRIDE 1 = all) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll; typedef unsigned long long ull;
#define QMAX 4096
static int *primes; static int np;
static ll mulmod(ll a, ll b, ll m){ return (ll)((__int128)a*b % m); }
static ll powmod(ll a, ll e, ll m){ ll r=1%m; a%=m; if(a<0)a+=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static int isprime_ll(ll n){ if(n<2) return 0; for(int i=0;i<50;i++){ if(n==primes[i]) return 1; if(n%primes[i]==0) return 0; }
  ll d=n-1; int s=0; while(!(d&1)){d>>=1;s++;} static const ll W[12]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ ll x=powmod(W[i],d,n); if(x==1||x==n-1) continue; int c=0; for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){c=1;break;} } if(!c) return 0; } return 1; }
static int legendre(ll a, ll q){ ll r=powmod(a,(q-1)/2,q); return r==1?1:(r==0?0:-1); }
static int qs[1000], nq; static int *lg[1000]; /* discrete log tables */
static ll stat_forced[1000], stat_f2[1000], stat_fF[1000], stat_unf[1000], stat_uf2[1000], kneser_bad=0, kneser_chk=0;
static ll stat_omega_f[1000];
/* box test: is target in R = prod over (s,v) of {s^j : |j|<=v} (mod q)?  bitset over residues */
static int inbox(int q, ll *ps, int *es, int k, int extra_mul_count, ll *extra, int target){
  static char cur[QMAX], nxt[QMAX];
  memset(cur,0,q); cur[1]=1;
  for(int i=0;i<k;i++){ ll s=ps[i]%q; if(s==0) continue; ll si=powmod(s,q-2,q);
    memset(nxt,0,q);
    for(int r=1;r<q;r++) if(cur[r]){ nxt[r]=1; ll a=r,b=r; for(int j=1;j<=es[i];j++){ a=a*s%q; b=b*si%q; nxt[a]=1; nxt[b]=1; } }
    memcpy(cur,nxt,q); }
  if(cur[target]) return 1;
  for(int t=0;t<extra_mul_count;t++){ ll m=extra[t]%q; /* target in m*R ? <=> target/m in R */
    ll want = (ll)target*powmod(m,q-2,q)%q; if(cur[want]) return 1; }
  return 0;
}
int main(int argc,char**argv){
  if(argc<6){ fprintf(stderr,"usage\n"); return 1; }
  ll P0=atoll(argv[1]), P1=atoll(argv[2]); ll STRIDE=atoll(argv[3]); int Q=atoi(argv[4]); const char*out=argv[5];
  int LIM=2000000; char*comp=calloc(LIM+1,1); primes=malloc(sizeof(int)*200000); np=0;
  for(int i=2;i<=LIM;i++){ if(!comp[i]){ primes[np++]=i; for(ll j=(ll)i*i;j<=LIM;j+=i) comp[j]=1; } }
  nq=0; for(int q=3;q<=Q;q+=4){ if(!isprime_ll(q)) continue; qs[nq]=q; lg[nq]=calloc(q,sizeof(int));
    /* primitive root */ int g=2; for(;;g++){ int ok=1; int m=q-1; for(int f=2;f*f<=m || m>1; f++){ if(f*f>m){ f=m; } if(m%f==0){ if(powmod(g,(q-1)/f,q)==1){ok=0;} while(m%f==0) m/=f; } if(m==1) break; } if(ok) break; }
    ll a=1; for(int e=0;e<q-1;e++){ lg[nq][a]=e; a=a*g%q; } nq++; }
  char fn[512]; snprintf(fn,sizeof fn,"%s_perp.txt",out); FILE*fp=fopen(fn,"w");
  fprintf(fp,"# p nforced nforced_ok2 nforced_okF pattern (one char per q==3 mod 4 prime <=%d: S forced ok2, f forced ok only via p-ratio, F forced fail, u unforced ok2, . unforced fail2)\n",Q);
  ll cnt=0, idx=0;
  ll lastp=0;
  for(ll p0=P0 + ((1-P0%8)+8)%8; p0<=P1; p0+=8*STRIDE){
    ll p=p0; while(!isprime_ll(p)) p+=8; if(p>P1) break; if(p<=lastp) continue; lastp=p; idx++; cnt++;
    int nf=0,nf2=0,nfF=0; char pat[1000];
    for(int i=0;i<nq;i++){ int q=qs[i]; if(q==p) continue;
      ll x=(p+q)/4; ll ps[64]; int es[64]; int k=0; ll y=x;
      for(int j=0;j<np && (ll)primes[j]*primes[j]<=y;j++){ if(y%primes[j]==0){ int e=0; while(y%primes[j]==0){y/=primes[j];e++;} ps[k]=primes[j]; es[k]=e; k++; } }
      if(y>1){ ps[k]=y; es[k]=1; k++; }
      int forced = (legendre(p%q,q)==-1);
      ll ext[2]; ext[0]=p%q; ext[1]=powmod(p,q-2,q);
      int ok2=inbox(q,ps,es,k,0,ext,q-1);
      int okF=ok2?1:inbox(q,ps,es,k,2,ext,q-1);
      pat[i] = forced ? (ok2 ? 'S' : (okF ? 'f' : 'F')) : (ok2 ? 'u' : '.');
      if(forced){ nf++; nf2+=ok2; nfF+=okF; stat_forced[i]++; if(!ok2) stat_f2[i]++; if(!okF) stat_fF[i]++;
        int om=0; for(int t=0;t<k;t++) om+=es[t]; stat_omega_f[i]+=om;
        if(!ok2){ /* Kneser structure */ kneser_chk++; int u=(q-1)/2, found=0;
          for(int d=2; d<=u && !found; d++){ if(u%d) continue; int nout=0, bad=0;
            for(int t=0;t<k;t++){ int L=lg[i][ps[t]%q]; if(L%(2*d)!=0){ nout+=es[t]; if(L%(2*d)==u%(2*d)) bad=1; } }
            if(!bad && nout>=1 && nout<=d-1) found=1; }
          if(!found){ kneser_bad++; fprintf(stderr,"KNESER VIOLATION p=%lld q=%d\n",p,q); } } }
      else { stat_unf[i]++; if(!ok2) stat_uf2[i]++; }
    }
    pat[nq]=0; fprintf(fp,"%lld %d %d %d %s\n",p,nf,nf2,nfF,pat);
  }
  fclose(fp);
  snprintf(fn,sizeof fn,"%s_perq.txt",out); FILE*fq=fopen(fn,"w");
  fprintf(fq,"# primes p==1(8) in [%lld,%lld], stride %lld: %lld primes. Kneser checks %lld, violations %lld\n",P0,P1,STRIDE,cnt,kneser_chk,kneser_bad);
  fprintf(fq,"# q u forced fail2 failF fail2_rate failF_rate meanOmega_forced unforced unforced_fail2 rate\n");
  for(int i=0;i<nq;i++){ int q=qs[i];
    fprintf(fq,"%d %d %lld %lld %lld %.5f %.5f %.3f %lld %lld %.5f\n",q,(q-1)/2,stat_forced[i],stat_f2[i],stat_fF[i],
      stat_forced[i]?(double)stat_f2[i]/stat_forced[i]:0, stat_forced[i]?(double)stat_fF[i]/stat_forced[i]:0,
      stat_forced[i]?(double)stat_omega_f[i]/stat_forced[i]:0, stat_unf[i],stat_uf2[i], stat_unf[i]?(double)stat_uf2[i]/stat_unf[i]:0); }
  fclose(fq);
  printf("done: %lld primes, Kneser checks %lld, violations %lld\n",cnt,kneser_chk,kneser_bad);
  return 0;
}
