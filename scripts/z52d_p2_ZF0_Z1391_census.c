/* Salez 1406.6307 Proposition 3, all seven equations, bounded constant triples.
   This is NOT Salez's original algorithm/order nor an exhaustive search in parameters. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
typedef int64_t I;
static unsigned char *comp,*mask; static int N,K; static I valid[7],attempt[7];
static I gcd(I a,I b){while(b){I t=a%b;a=b;b=t;}return a;}
static I inv(I a,I m){I b=m,u=1,v=0;while(b){I q=a/b,t=a-q*b;a=b;b=t;t=u-q*v;u=v;v=t;}return a==1?(u%m+m)%m:-1;}
static void check(int f,I p,I A,I B,I C,I D){
 if(p<3||p>N||comp[p]||(mask[p]&(1<<f)))return;
 attempt[f]++;
 if(A<=0||B<=0||C<=0||D<=0||(A+B)%C)return;
 I E=(A+B)/C,F=4*B*C*D-(f<3?1:p);
 if(E<=0||F<=0||gcd(A,B)!=1||gcd(B,C)!=1||gcd(C,D)!=1||gcd((I)((__int128)4*A*B*D%E),E)!=1||gcd(4*B*C*D,F)!=1)return;
 if(A%p==0||B%p==0||D%p==0||(f>=3&&C%p==0))return;
 if((__int128)4*A*B*C*D!=(f<3?(__int128)A+B+p*C:(__int128)p*(A+B)+C)){fprintf(stderr,"bad identity\n");exit(2);}
 mask[p]|=1<<f;valid[f]++;
}
int main(int argc,char**argv){N=argc>1?atoi(argv[1]):10000000;K=argc>2?atoi(argv[2]):24;clock_t st=clock();
 comp=calloc(N+1,1);mask=calloc(N+1,1);for(I i=2;i*i<=N;i++)if(!comp[i])for(I j=i*i;j<=N;j+=i)comp[j]=1;
 for(I a=1;a<=K;a++)for(I b=1;b<=K;b++)for(I c=1;c<=K;c++){
   I mod,r,iv;
   // 14a: constants B=a,C=b,D=c.
   mod=4*a*b*c-1;iv=inv(b,mod);r=(-a*iv%mod+mod)%mod;
   for(I p=r;p<=N;p+=mod)check(0,p,(a+p*b)/mod,a,b,c);
   // 14b and 15a: constants A=a,B=b,E=c, with E|(A+B).
   if((a+b)%c==0){mod=4*a*b;r=(mod-c%mod)%mod;
     for(I p=r;p<=N;p+=mod)check(1,p,a,b,(a+b)/c,(p+c)/mod);
     iv=inv(c,mod);if(iv>=0){r=(mod-iv)%mod;for(I p=r;p<=N;p+=mod)check(3,p,a,b,(a+b)/c,(p*c+1)/mod);}}
   // 14c: constants B=a,D=b,E=c.
   mod=4*a*b*c;r=(-(c+4*a*a*b)%mod+mod)%mod;
   for(I p=r;p<=N;p+=mod)check(2,p,(p+c)/(4*a*b),a,(p+c+4*a*a*b)/mod,b);
   // 15b: constants B=a,C=b,F=c.
   mod=4*a*b;r=(mod-c%mod)%mod;
   for(I p=r;p<=N;p+=mod)if((p*a+b)%c==0)check(4,p,(p*a+b)/c,a,b,(p+c)/mod);
   // 15c: constants B=a,D=b,F=c.
   if((4*a*a*b+1)%c==0){mod=4*a*b;r=(mod-c%mod)%mod;
     for(I p=r;p<=N;p+=mod){I C=(p+c)/mod,E=(4*a*a*b+1)/c;check(5,p,C*E-a,a,C,b);}}
   // 15d: constants C=a,D=b,F=c.
   mod=4*a*b;r=(mod-c%mod)%mod;
   for(I p=r;p<=N;p+=mod)if((p*p+4*a*a*b)%c==0){I B=(p+c)/mod;if((p*B+a)%c==0)check(6,p,(p*B+a)/c,B,a,b);}
 }
 I counts[840][9]={0},rev[7]={0},hist[128]={0},pr=0;
 for(int p=2;p<=N;p++)if(!comp[p]){pr++;hist[mask[p]]++;int f=7;if(p==2)f=8;else for(int i=0;i<7;i++)if(mask[p]&(1<<i)){f=i;break;}counts[p%840][f]++;for(int i=6;i>=0;i--)if(mask[p]&(1<<i)){rev[i]++;break;}}
 printf("residue,14a,14b,14c,15a,15b,15c,15d,uncovered,special_2\n");for(int r=0;r<840;r++){I s=0;for(int i=0;i<9;i++)s+=counts[r][i];if(s){printf("%d",r);for(int i=0;i<9;i++)printf(",%lld",(long long)counts[r][i]);puts("");}}
 fprintf(stderr,"N=%d K=%d primes=%lld seconds=%.3f\n",N,K,(long long)pr,(double)(clock()-st)/CLOCKS_PER_SEC);
 for(int i=0;i<7;i++)fprintf(stderr,"family=%d independent_hits=%lld reversed_first=%lld attempted=%lld\n",i,(long long)valid[i],(long long)rev[i],(long long)attempt[i]);
 fprintf(stderr,"uncovered_including_2=%lld first_uncovered:",(long long)hist[0]);int j=0;for(int p=3;p<=N&&j<30;p++)if(!comp[p]&&!mask[p]){fprintf(stderr," %d",p);j++;}fprintf(stderr,"\n");
}
