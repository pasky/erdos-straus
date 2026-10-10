/* R128 from-scratch f_II(n) sieve via form 4: for each (a,c,d), gcd(a,c)=1, f=4acd-1, the n with
   f | a + n c form one AP n == -a c^{-1} (mod f); b=(a+nc)/f; keep a<=b (weight 2, or 1 if a==b).
   Bounds (a<=b): 4a^2 d <= n+2a ; c <= (2N+2a+1)/(4ad).  Mode ALL (N<=5000): all n with gcd(abd,n)=1;
   else primes only (coprimality automatic).  Prints per-n counts (ALL) or prime stats. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
typedef long long ll;
static ll gcdl(ll a,ll b){while(b){ll t=a%b;a=b;b=t;}return a<0?-a:a;}
static ll inv(ll a,ll m){ll g=m,x=0,x1=1,a1=a%m; ll b=a1; ll r0=m,r1=b,s0=0,s1=1; while(r1){ll q=r0/r1,t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;} (void)g;(void)x;(void)x1; return ((s0%m)+m)%m;}
int main(int argc,char**argv){ ll N=atoll(argv[1]); int ALL = N<=5000;
 unsigned *cnt=calloc(N+1,4); unsigned short *d1=calloc(N+1,2),*c1=calloc(N+1,2); char *comp=calloc(N+1,1);
 for(ll i=2;i*i<=N;i++) if(!comp[i]) for(ll j=i*i;j<=N;j+=i) comp[j]=1;
 for(ll a=1; 4*a*a<=N+2*a; a++) for(ll d=1; 4*a*a*d<=N+2*a; d++) for(ll c=1; 4*a*c*d<=2*N+2*a+1; c++){
   if(gcdl(a,c)!=1) continue; ll f=4*a*c*d-1;
   ll r = (f - (a%f)*inv(c%f,f)%f)%f;  /* n == -a/c mod f */
   ll nmin = (a*f - a + c - 1)/c; if(nmin<1) nmin=1;  /* a<=b <=> a f <= a + n c */
   ll n = r + ((nmin - r + f - 1)/f > 0 ? (nmin - r + f - 1)/f : 0)*f; if(n<nmin) n+=f; if(n==0) n+=f;
   for(; n<=N; n+=f){ if(!ALL && comp[n]) continue; ll b=(a+n*c)/f; if(b<a) continue;
     if(ALL && gcdl(a*b*d,n)!=1) continue;
     int w=(a==b)?1:2; cnt[n]+=w; if(d==1) d1[n]+=w; if(c==1) c1[n]+=w; } }
 if(ALL){ for(ll n=2;n<=N;n++) printf("%lld %u\n",n,cnt[n]); return 0; }
 /* stats */
 printf("# k #p minf argmin mean(f/log3) min(f/log3) argmin #d1=0 #c1=0\n"); ll zero=0;
 for(int k=3;(1LL<<k)<=N;k++){ ll lo=1LL<<k, hi=(1LL<<(k+1))-1; if(hi>N) hi=N; ll np=0,mn=1LL<<60,am=0,nd=0,nc=0; double s=0,mr=1e9; ll amr=0;
   for(ll p=lo;p<=hi;p++){ if(comp[p]||p<5) continue; np++; double L=log((double)p); double r=cnt[p]/(L*L*L); s+=r;
     if(cnt[p]<mn){mn=cnt[p];am=p;} if(r<mr){mr=r;amr=p;} if(!d1[p]) nd++; if(!c1[p]) nc++; if(!cnt[p]) zero++; }
   printf("%2d %7lld %5lld %9lld %.4f %.4f %9lld %5lld %3lld\n",k,np,mn,am,s/np,mr,amr,nd,nc); }
 printf("# primes 5..%lld with f_II=0: %lld\n",N,zero);
 /* class means mod 840 for p>=1e5 */
 double cs[840]={0}; ll cn[840]={0};
 for(ll p=100000;p<=N;p++) if(!comp[p]){double L=log((double)p); cs[p%840]+=cnt[p]/(L*L*L); cn[p%840]++;}
 printf("# smallest class means mod 840 (p>=1e5):\n"); int used[840]={0};
 for(int t=0;t<8;t++){int bi=-1; for(int r=0;r<840;r++) if(cn[r]&&!used[r]&&(bi<0||cs[r]/cn[r]<cs[bi]/cn[bi])) bi=r; used[bi]=1; printf("  %3d %.4f\n",bi,cs[bi]/cn[bi]);}
 printf("  839 %.4f\n",cs[839]/cn[839]);
 FILE *o=fopen(argc>2?argv[2]:"/dev/null","w"); for(ll p=5;p<=N;p++) if(!comp[p]) fprintf(o,"%lld %u %u %u\n",p,cnt[p],d1[p],c1[p]); fclose(o);
 return 0;}
