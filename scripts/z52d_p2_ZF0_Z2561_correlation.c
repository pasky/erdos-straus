// Exact divisor/character recurrences, bounded to ~1 GB at 1e8.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef struct {uint64_t n,np,nm,sp,sm; long double d,d2,l,dl,hitp,hitm;} Stat;
void add(Stat*s,int d,int l){s->n++;s->d+=d;s->d2+=(long double)d*d;s->l+=l;s->dl+=d*l;if(l>0){s->np++;s->sp+=d;s->hitp+=d>0;}else{s->nm++;s->sm+=d;s->hitm+=d>0;}}
void out(const char*name,Stat*s){long double n=s->n,md=s->d/n,ml=s->l/n,cov=s->dl/n-md*ml;printf("%s n=%llu meanD=%.9Lf meanlambda=%.9Lf E_Dlambda=%.9Lf cov=%.9Lf pearson=%.9Lf meanDplus=%.9Lf meanDminus=%.9Lf hitplus=%.9Lf hitminus=%.9Lf\n",name,(unsigned long long)s->n,md,ml,s->dl/n,cov,cov/sqrtl((s->d2/n-md*md)*(1-ml*ml)),(long double)s->sp/s->np,(long double)s->sm/s->nm,s->hitp/s->np,s->hitm/s->nm);}
int main(int argc,char**argv){uint32_t N=argc>1?strtoul(argv[1],0,10):100000000;uint32_t*spf=calloc((size_t)N+1,4);uint16_t*tau=calloc((size_t)N+1,2),*sig=calloc((size_t)N+1,2);int8_t*lam=calloc((size_t)N+1,1);uint8_t*ex=calloc((size_t)N+1,1);if(!spf||!tau||!sig||!lam||!ex)return 2;
for(uint32_t p=2;p<=N;p++)if(!spf[p]){spf[p]=p;if((uint64_t)p*p<=N)for(uint64_t j=(uint64_t)p*p;j<=N;j+=p)if(!spf[j])spf[j]=p;}
tau[1]=sig[1]=lam[1]=1;for(uint32_t n=2;n<=N;n++){uint32_t p=spf[n],m=n/p;lam[n]=-lam[m];ex[n]=(m%p==0)?ex[m]+1:1;tau[n]=tau[m]/ex[n]*(ex[n]+1);if(p%4==1)sig[n]=sig[m]/ex[n]*(ex[n]+1);else if(p==2)sig[n]=sig[m];else {uint32_t r=n;for(int j=0;j<ex[n];j++)r/=p;sig[n]=(ex[n]%2)?0:sig[r];}}
// Independent brute divisor validation (not a new repo unit test).
for(uint32_t n=1;n<=10000&&n<=N;n+=2){int d=0;for(uint32_t a=3;a<=n;a+=4)d+=n%a==0;if(d!=(tau[n]-sig[n])/2){fprintf(stderr,"bad %u\n",n);return 3;}}
for(int pass=0;pass<2;pass++){uint32_t X=pass?N:N/10;printf("X=%u\n",X);Stat s[8]={0};for(uint32_t n=1;n<=X;n+=2){int d=(tau[n]-sig[n])/2,l=lam[n];add(s,d,l);add(&s[1+(n%4==3)],d,l);if(n%8==1)add(s+3,d,l);if(n%24==1)add(s+4,d,l);if(n%840==1)add(s+5,d,l);if(n%840==121)add(s+6,d,l);if(n%840==169)add(s+7,d,l);}const char*names[]={"odd","1mod4","3mod4","1mod8","1mod24","1mod840","121mod840","169mod840"};for(int i=0;i<8;i++)out(names[i],s+i);}
Stat s[6]={0};long double cnt=0,ll=0,dd=0,wll=0,l1=0,l2=0,d1=0,d2=0;for(uint32_t p=3;p<=(N-1)/8;p+=2)if(spf[p]==p){uint32_t a=4*p+1,b=8*p+1;int x=(tau[a]-sig[a])/2,y=(tau[b]-sig[b])/2;add(s,x,lam[a]);add(s+1,y,lam[b]);if(p%24==1){add(s+2,x,lam[a]);add(s+3,y,lam[b]);}if(p%840==1){add(s+4,x,lam[a]);add(s+5,y,lam[b]);}cnt++;ll+=lam[a]*lam[b];dd+=(long double)x*y;wll+=(long double)x*y*lam[a]*lam[b];l1+=lam[a];l2+=lam[b];d1+=x;d2+=y;}
const char*pn[]={"prime_C1","prime_C2","prime1mod24_C1","prime1mod24_C2","prime1mod840_C1","prime1mod840_C2"};for(int i=0;i<6;i++)out(pn[i],s+i);printf("pair primes<=%u count=%.0Lf E_ll=%.9Lf cov_ll=%.9Lf E_DD=%.9Lf cov_DD=%.9Lf E_DDll=%.9Lf\n",(N-1)/8,cnt,ll/cnt,ll/cnt-l1*l2/cnt/cnt,dd/cnt,dd/cnt-d1*d2/cnt/cnt,wll/cnt);free(spf);free(tau);free(sig);free(lam);free(ex);}
