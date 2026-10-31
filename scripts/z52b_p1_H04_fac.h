/* small 64-bit factoring helpers (Miller-Rabin + Pollard-Brent) for z52b pass1 H04 */
#include <stdint.h>
#include <stdlib.h>
typedef unsigned __int128 u128; typedef uint64_t u64;
static u64 mulm(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powm(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulm(r,a,m);a=mulm(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){if(n<2)return 0;static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
 for(int i=0;i<12;i++){if(n%sp[i]==0)return n==sp[i];}
 u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
 for(int i=0;i<12;i++){u64 x=powm(sp[i],d,n);if(x==1||x==n-1)continue;int ok=0;for(int r=1;r<s;r++){x=mulm(x,x,n);if(x==n-1){ok=1;break;}}if(!ok)return 0;}return 1;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){if(n%2==0)return 2;for(u64 c=1;;c++){u64 y=2,x,g=1,q=1,ys=2;u64 r=1,m=128;
 do{x=y;for(u64 i=0;i<r;i++)y=(mulm(y,y,n)+c)%n;u64 k=0;do{ys=y;for(u64 i=0;i<m&&i<r-k;i++){y=(mulm(y,y,n)+c)%n;q=mulm(q,x>y?x-y:y-x,n);}g=gcdu(q,n);k+=m;}while(k<r&&g==1);r<<=1;}while(g==1);
 if(g==n){do{ys=(mulm(ys,ys,n)+c)%n;g=gcdu(x>ys?x-ys:ys-x,n);}while(g==1);} if(g!=n)return g;}}
/* factor n into primes pr[] with exponents ex[]; returns count */
static int factor_rec(u64 n,u64*pr,int*ex,int k){if(n==1)return k;if(isprime(n)){for(int i=0;i<k;i++)if(pr[i]==n){ex[i]++;return k;}pr[k]=n;ex[k]=1;return k+1;}
 u64 d=rho(n);k=factor_rec(d,pr,ex,k);return factor_rec(n/d,pr,ex,k);}
static int factor(u64 n,u64*pr,int*ex){int k=0;static const int sm[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
 for(int i=0;i<15;i++){if(n%sm[i]==0){pr[k]=sm[i];ex[k]=0;while(n%sm[i]==0){n/=sm[i];ex[k]++;}k++;}}
 return factor_rec(n,pr,ex,k);}
/* does n (factored) have a divisor ≡ target mod m ? enumerates residues of divisors */
static int has_div_class(u64*pr,int*ex,int k,u64 m,u64 target){
 static u64 buf[1<<16];int nb=1;buf[0]=1%m;
 for(int i=0;i<k;i++){int cur=nb;u64 pm=pr[i]%m,pw=1;for(int e=1;e<=ex[i];e++){pw=mulm(pw,pm,m);for(int j=0;j<cur;j++){if(nb>=(1<<16))return -1;buf[nb++]=mulm(buf[j],pw,m);}}}
 for(int j=0;j<nb;j++)if(buf[j]==target%m)return 1;return 0;}
