/* Bounded-memory fresh window census. stdout: p,a_min,mII,qF,capF.
   qF is least q=3 mod 8 prime with (q/p)=-1, only for p=1 mod 8.
   capF is exact, allowing odd-prime overflow only (K is odd at qF).
   Build gcc -O2 -Wall -Wextra; run N<=10000000. ~55 MB. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
static int sp[2501001];
static unsigned char composite[10000001];
static int primes[16], powers[16], nf;
static long modpow(long a,int b,int m){long z=1;for(;b;b>>=1,a=a*a%m)if(b&1)z=z*a%m;return z;}
static void factor(int k){nf=0;while(k>1){int s=sp[k],b=0;while(k%s==0){k/=s;b++;}primes[nf]=s;powers[nf++]=b;}}
static int hit(int m,int target,int cap){
 unsigned char a[2001]={0},c[2001];a[1]=1;
 for(int j=0;j<nf;j++){
  memset(c,0,(size_t)m);int s=primes[j]%m,b=powers[j];
  /* Inverse by Euclid, valid also at composite windows. */
  int x=0,y=1,r=m,t=s;while(t){int z=r/t,w=r-z*t;r=t;t=w;w=x-z*y;x=y;y=w;}
  assert(r==1);x=(x%m+m)%m;int start=(int)modpow(x,b,m),v=start;
  for(int e=-b;e<=b;e++,v=(int)((long)v*s%m))for(int h=0;h<m;h++)if(a[h])c[(long)h*v%m]=1;
  if(primes[j]!=2){v=(int)modpow(s,b,m);int s2=s*s%m;for(int e=1;e<=cap;e++){v=v*s2%m;for(int h=0;h<m;h++)if(a[h])c[(long)h*v%m]=1;}}
  memcpy(a,c,(size_t)m);
 }
 return a[(target%m+m)%m];
}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 int N=atoi(argv[1]);assert(N>=2000&&N<=10000000);
 int lim=(N+2000)/4;for(int i=2;i<=lim;i++)if(!sp[i]){sp[i]=i;if((long)i*i<=lim)for(int j=i*i;j<=lim;j+=i)if(!sp[j])sp[j]=i;}
 for(int i=2;(long)i*i<=N;i++)if(!composite[i])for(int j=i*i;j<=N;j+=i)composite[j]=1;
 puts("p,a_min,mII,qF,capF");
 for(int p=5;p<=N;p+=4)if(!composite[p]){
  int amin=0,mii=0,qf=0,cf=-1;
  for(int m=3;m<=2000;m+=4){if(m%p==0)continue;factor((p+m)/4);int yes=hit(m,-1,0);if(!amin&&(yes||hit(m,-p,0)))amin=m;if(yes){mii=m;break;}}
  assert(amin&&mii);
  if(p%8==1){for(int q=3;q<=2000;q+=8)if(!composite[q]&&q%p&&modpow(q,(p-1)/2,p)==p-1){qf=q;break;}assert(qf);factor((p+qf)/4);for(cf=0;cf<qf;cf++)if(hit(qf,-1,cf))break;assert(cf<qf);}
  printf("%d,%d,%d,%d,%d\n",p,amin,mii,qf,cf);
 }
 return 0;
}
