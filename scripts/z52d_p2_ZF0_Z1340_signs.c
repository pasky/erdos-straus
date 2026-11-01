#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// K1': exact divisor sieve, not floating-point theta evaluation.
int main(int argc,char**argv){int X=argc>1?atoi(argv[1]):100000;int *a=calloc(X+1,sizeof(int));if(!a)return 2;printf("t,nmax,negative,zero,positive,min,max,first_positive_n\n");for(int t=2;t<=64;t++){for(int n=0;n<=X;n++)a[n]=0;uint64_t lim=(uint64_t)t*X+1;for(int sign=-1;sign<=1;sign+=2){int r=sign==1?t-1:1;for(uint64_t d=r;d<=lim;d+=t)for(uint64_t e=r;d*e<=lim;e+=t){uint64_t n=(d*e-1)/t;if(n<=(uint64_t)X)a[n]+=sign;}}int neg=0,zero=0,pos=0,mn=0,mx=0,first=-1;for(int n=0;n<=X;n++){neg+=a[n]<0;zero+=a[n]==0;pos+=a[n]>0;if(a[n]<mn)mn=a[n];if(a[n]>mx)mx=a[n];if(a[n]>0&&first<0)first=n;}printf("%d,%d,%d,%d,%d,%d,%d,%d\n",t,X,neg,zero,pos,mn,mx,first);}free(a);}
