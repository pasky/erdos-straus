/* bsG_Ak: values of the path determinant d_{A_k}(a_1..a_k) = K^-(a_1..a_k) (negative continuant, a_i >= 2) below N;
   prints the complement in [0,N) (Lorenzini's L_{A_k}) and the count of values.  DFS with lower bound "rest = 2".
   K^-: p_j = a_j p_{j-1} - p_{j-2}, p_0 = 1, p_{-1} = 0.  gcc -O2 -o /tmp/bsG_Ak scripts/bsG_Ak.c */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int k; static ll N; static unsigned char *hit;
static ll finish2(ll p, ll q, int rem){ for(int i=0;i<rem;i++){ ll t=2*p-q; q=p; p=t; } return p; }
static void dfs(int j, ll p, ll q){ /* j letters placed, (p,q) = (p_j, p_{j-1}) */
  if(j==k){ if(p<N) hit[p]=1; return; }
  for(ll a=2;;a++){ ll np=a*p-q; if(finish2(np,p,k-j-1)>=N) break; dfs(j+1,np,p); } }
int main(int argc,char**argv){ k=atoi(argv[1]); N=atoll(argv[2]); hit=calloc(N,1);
  dfs(0,1,0); ll c=0; printf("A_%d complement in [0,%lld):",k,N);
  for(ll n=0;n<N;n++) if(!hit[n]){ c++; if(c<=80) printf(" %lld",n); } printf("  [total %lld]\n",c); return 0; }
