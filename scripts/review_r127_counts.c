/* R127 from-scratch: (a) slice count S(p) = #{(c,f): cf | p+c+f, f*g = 1 mod 4, g=(p+c+f)/(cf)}
   by direct enumeration over (c,f) [(c-1)(f-1) <= p+1]; (b) full ordered solution count f(n) of
   4/n = 1/x+1/y+1/z, split by how many of x,y,z are divisible by n (prime n): f_I = #exactly-one/3,
   f_II = #exactly-two/3.  Usage: review_r127_counts n [n ...]  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef uint64_t u64;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 Sslice(u64 p, int verbose){
  u64 S=0;
  for(u64 c=1;c<=p+2;c++){
    u64 fmax = (c==1)? p+2 : 1+(p+1)/(c-1);   /* (c-1)(f-1) <= p+1 since g >= 1 */
    for(u64 f=1; f<=fmax; f++){
      u64 s=p+c+f; if(s%(c*f)) continue; u64 g=s/(c*f);
      if((f*g)%4==1){S++; if(verbose) printf("  slice sol c=%llu f=%llu g=%llu  m=gf-1=%llu m''=gc-1=%llu\n",
        (unsigned long long)c,(unsigned long long)f,(unsigned long long)g,(unsigned long long)(g*f-1),(unsigned long long)(g*c-1));}
    }
  }
  return S;
}
static u64 ps[64]; static int es[64], np;
static u64 cnt_ord, cnt1, cnt2, cnt0, cnt3, n_g;
static void classify(u64 n,u64 x,u64 y,u128 z){
  int k=(x%n==0)+(y%n==0)+(int)(z%n==0);
  int perm = (x==y&&y==z)?1:((x==y||y==z)?3:6);
  cnt_ord+=perm; if(k==1)cnt1+=perm; else if(k==2)cnt2+=perm; else if(k==0)cnt0+=perm; else cnt3+=perm;
}
static u64 A_,B_,X_,N_;
static void gen(int i,u128 u){
  if(i==np){
    if(u>(u128)B_) return;
    if((u+B_)%A_) return;
    u128 y=(u+B_)/A_; if(y<X_) return;
    u128 v=((u128)B_*B_)/u; u128 z=(v+B_)/A_;
    if(((v+B_)%A_)) { fprintf(stderr,"BUG v\n"); exit(1);} 
    classify(N_,X_,(u64)y,z); return; }
  u128 q=1;
  for(int e=0;e<=2*es[i];e++){ if(u*q>(u128)B_) break; gen(i+1,u*q); q*=ps[i]; }
}
static void addfac(u64 q,int e){for(int i=0;i<np;i++) if(ps[i]==q){es[i]+=e;return;} ps[np]=q;es[np]=e;np++;}
static uint32_t *spf; static u64 nprimes_of_n[64]; static int nnp;
static void factorB(u64 x,u64 B){ /* primes of B are among primes of n and of x */
  u64 cand[128]; int nc=0;
  for(int i=0;i<nnp;i++) cand[nc++]=nprimes_of_n[i];
  while(x>1){u64 q=spf[x]; cand[nc++]=q; while(x%q==0)x/=q;}
  for(int i=0;i<nc;i++){ int dup=0; for(int j=0;j<i;j++) if(cand[j]==cand[i]) dup=1; if(dup) continue;
    int e=0; while(B%cand[i]==0){B/=cand[i];e++;} if(e) addfac(cand[i],e);} 
  if(B!=1){fprintf(stderr,"BUG factor\n");exit(1);} }
static void fullcount(u64 n){
  cnt_ord=cnt1=cnt2=cnt0=cnt3=0;
  u64 L=(3*n)/4+2; spf=calloc(L+1,sizeof(uint32_t));
  for(u64 i=2;i<=L;i++) if(!spf[i]) for(u64 j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i;
  nnp=0; {u64 m=n; for(u64 q=2;q*q<=m;q++) if(m%q==0){nprimes_of_n[nnp++]=q; while(m%q==0)m/=q;} if(m>1) nprimes_of_n[nnp++]=m;}
  for(u64 x=n/4+1; x<=(3*n)/4; x++){
    if(4*x<=n) continue;
    u64 A=4*x-n; u64 B=n*x; u64 g=gcd(A,B); A/=g; B/=g;
    np=0; factorB(x,B);
    A_=A;B_=B;X_=x;N_=n; gen(0,1);
  }
}
int main(int argc,char**argv){
  for(int a=1;a<argc;a++){
    u64 n=strtoull(argv[a],0,10); int full = n<100000000ULL;
    u64 S=Sslice(n, 1);
    printf("n=%llu S=%llu\n",(unsigned long long)n,(unsigned long long)S);
    if(full){ fullcount(n);
      printf("n=%llu f=%llu  exactly0=%llu one=%llu two=%llu three=%llu  f_I=%llu%s f_II=%llu%s\n",(unsigned long long)n,
        (unsigned long long)cnt_ord,(unsigned long long)cnt0,(unsigned long long)cnt1,(unsigned long long)cnt2,(unsigned long long)cnt3,
        (unsigned long long)(cnt1/3),cnt1%3?"(!)":"",(unsigned long long)(cnt2/3),cnt2%3?"(!)":""); }
    fflush(stdout);
  }
}
