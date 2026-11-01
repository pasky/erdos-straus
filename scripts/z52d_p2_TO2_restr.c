// Z0510: 4/n = 1/x+1/y+1/z with restricted denominators. For every n in [2,N], enumerate ALL unordered solutions
// (x<=y<=z) and test restrictions: SF (x,y,z squarefree), PAR (exactly one of x,y,z even), CHAIN (x|y|z),
// PC (pairwise coprime), M4 (x,y,z all ≡1 mod 4). Output: per restriction, #n<=N with no solution and first such n.
// Usage: z52d_p2_TO2_restr N
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int *spf; static ll LIM;
static ll gcdl(ll a, ll b){ while(b){ ll t=a%b; a=b; b=t;} return a; }
static int *PR; static int NPR;
// squarefree test for arbitrary v: trial-divide by primes <= cbrt(v); remainder r has <=2 prime factors, non-squarefree iff r is a square >1
static int sqfree(ll v){
  for (int i=0;i<NPR;i++){ ll p=PR[i]; if (p*p*p > v) break; if (v%p==0){ v/=p; if (v%p==0) return 0; } }
  if (v<=1) return 1;
  ll r=(ll)__builtin_sqrt((double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++;
  if (r*r==v && r>1) return 0;
  return 1; }
int main(int argc, char **argv){
  ll N = atoll(argv[1]);
  LIM = (3*N*N)/4 + 10;            // b' <= n*x <= N*(3N/4)
  if (LIM > 40000000LL) LIM = 40000000LL;
  spf = calloc(LIM+1, sizeof(int));
  { int M=200000; char *c=calloc(M+1,1); PR=malloc(sizeof(int)*M); NPR=0; for(int i=2;i<=M;i++){ if(!c[i]){ PR[NPR++]=i; for(long j=(long)i*i;j<=M;j+=i) c[j]=1; } } }
  for (ll i=2;i<=LIM;i++) if(!spf[i]) for(ll j=i;j<=LIM;j+=i) if(!spf[j]) spf[j]=(int)i;
  const char *names[5] = {"SF","PAR","CHAIN","PC","M4"};
  ll firstfail[5] = {0,0,0,0,0}; ll nfail[5] = {0,0,0,0,0};
  ll firstsol_any = 0;
  for (ll n=2; n<=N; n++){
    int ok[5] = {0,0,0,0,0}; ll cntsol=0;
    for (ll x = n/4 + 1; 4*x < 3*n; x++){
      ll a = 4*x - n, b = n*x; if (a<=0) continue;
      ll g = gcdl(a,b); ll ap = a/g, bp = b/g;
      // factor bp
      ll pr[32]; int ex[32]; int np=0; ll v=bp;
      while(v>1){ int p=spf[v]; int e=0; while(v%p==0){v/=p;e++;} pr[np]=p; ex[np]=2*e; np++; }
      // enumerate divisors d of bp^2
      ll divs[20000]; int nd=1; divs[0]=1;
      for (int i=0;i<np;i++){
        int cur=nd; ll pp=1;
        for (int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) if(nd<20000) divs[nd++]=divs[j]*pp; }
      }
      ll bb = bp*bp;
      for (int i=0;i<nd;i++){
        ll d = divs[i]; ll t = d + bp;
        if (t % ap) continue;
        ll y = t/ap; ll e2 = bb/d; ll t2 = e2 + bp; if (t2 % ap) continue; ll z = t2/ap;
        if (y < x || z < y) continue;
        // solution (x,y,z) with x<=y<=z
        cntsol++;
        ll X[3]={x,y,z};
        int sf = sqfree(x)&&sqfree(y)&&sqfree(z);
        int ev = (x%2==0)+(y%2==0)+(z%2==0);
        int chain = (y%x==0)&&(z%y==0);
        int pc = gcdl(x,y)==1 && gcdl(y,z)==1 && gcdl(x,z)==1;
        int m4 = (x%4==1)&&(y%4==1)&&(z%4==1);
        if (sf) ok[0]=1; if (ev==1) ok[1]=1; if (chain) ok[2]=1; if (pc) ok[3]=1; if (m4) ok[4]=1;
        (void)X;
      }
    }
    if (cntsol && !firstsol_any) firstsol_any = n;
    for (int r=0;r<5;r++) if(!ok[r]){ nfail[r]++; if(!firstfail[r]) firstfail[r]=n; if (nfail[r]<=100000) printf("  fail %s n=%lld\n", names[r], n); }
  }
  printf("N=%lld first_n_with_any_solution=%lld\n", N, firstsol_any);
  for (int r=0;r<5;r++) printf("%s: n_without_restricted_solution=%lld first_such_n=%lld\n", names[r], nfail[r], firstfail[r]);
  return 0;
}
