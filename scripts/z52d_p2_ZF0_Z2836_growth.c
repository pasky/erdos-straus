/* Positive conjugates T^-1 M(k) T=R^(k-2)L. DFS unique L/R words. */
#include <stdio.h>
#include <stdint.h>
static uint64_t bins[14];
static int lim=8192;
static void walk(int a,int b,int c,int d,int lastL){
 int n=a>b?a:b;n=n>c?n:c;n=n>d?n:d;
 if(n>lim)return;
 if(lastL){int j=0,h=1;while(h<n){h*=2;j++;}bins[j]++;}
 if(a+b<=lim&&c+d<=lim){walk(a+b,b,c+d,d,1);walk(a,a+b,c,c+d,0);}
}
int main(void){walk(1,0,0,1,0);puts("N,closure_count,three_letter_count");uint64_t total=0;
 for(int j=0;j<=13;j++){total+=bins[j];if(j<5)continue;int N=1<<j;uint64_t triples=0;
  for(int t=2;t<=(N+4)/4;t++)for(int u=2;u<=(N+2)/(2*t-1);u++){int vmax=(N+u)/(t*u-1);if(vmax>=2)triples+=vmax-1;}
  printf("%d,%llu,%llu\n",N,(unsigned long long)total,(unsigned long long)triples);
 }
}
