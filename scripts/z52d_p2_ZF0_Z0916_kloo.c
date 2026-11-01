/* stdin prime list, exact inverse recurrence and double cosine sum.
   Two symmetric x terms are paired; cosine table uses libm (no recurrence drift). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
int main(){int p,n=0;int*iv=malloc(1000001*sizeof(int));double*co=malloc(1000001*sizeof(double));puts("p,K,Knorm");while(scanf("%d",&p)==1){iv[1]=1;for(int x=2;x<=p/2;x++)iv[x]=p-(int)((int64_t)(p/x)*iv[p%x]%p);for(int x=0;x<=p/2;x++)co[x]=cos(2*acos(-1.)*x/p);double sum=0,err=0;for(int x=1;x<=p/2;x++){int r=(x+iv[x])%p;if(r>p/2)r=p-r;double y=2*co[r]-err,t=sum+y;err=(t-sum)-y;sum=t;}printf("%d,%.14g,%.14g\n",p,sum,sum/sqrt(p));if(++n%1000==0){fflush(stdout);fprintf(stderr,"n=%d p=%d cpu=%.1f\n",n,p,(double)clock()/CLOCKS_PER_SEC);}}free(iv);free(co);}
