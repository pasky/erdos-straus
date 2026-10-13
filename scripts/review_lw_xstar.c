/* R180: x*(n) = least x>=2 with d | n+x, d = -1 mod x, d >= 2x-1, (n+x)/d >= 2 (minimal outer letter). n < N, x <= XM. */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
int main(int c, char **v){
  ll N = c>1 ? atoll(v[1]) : 100000000LL; int XM = 16;
  unsigned char *xs = malloc(N); for(ll i=0;i<N;i++) xs[i]=99;
  for (int x=XM; x>=2; x--)                       /* descending so smallest x wins */
    for (ll d=2*x-1; 2*d-x < N; d+=x)             /* d = -1 mod x */
      for (ll n=2*d-x; n<N; n+=d) xs[n]=x;
  int E[] = {2,3,5,6,9,11,14,15,35,105,510}; 
  for (int i=0;i<11;i++) if (xs[E[i]]!=99) printf("E_W member %d has x*=%d!\n",E[i],xs[E[i]]);
  ll other=0, cnt[100]={0}; int rec=0;
  for (ll n=2;n<N;n++){ int isE=0; for(int i=0;i<11;i++) if(E[i]==n) isE=1; if(isE) continue;
    if (xs[n]==99){ other++; if(other<10) printf("no x<=%d at n=%lld\n",XM,n); continue; }
    if (xs[n]>rec){ rec=xs[n]; printf("record x*=%d at n=%lld\n",rec,n);} 
    if (n>=10000000LL) cnt[xs[n]]++; }
  printf("n<%lld outside E_W with x*>%d: %lld\n",N,XM,other);
  printf("[1e7,N) #{x*>X} X=2..10:"); for(int X=2;X<=10;X++){ll s=0; for(int y=X+1;y<100;y++) s+=cnt[y]; printf(" %lld",s);} puts("");
  ll t=64858079LL; if (t<N) printf("x*(64858079)=%d, neighbours %d %d\n",xs[t],xs[t-1],xs[t+1]);
  return 0; }
