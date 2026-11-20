/* Independent all-tuples height checker. No lcm/denominator-pattern sieve:
   test local equations with explicit mod 8 and odd-prime quadratics.
   U: the distinguished entry divisible by the numerator of the normalized
   reciprocal-sum RHS's denominator (input n prime). */
#include <assert.h>
#include <stdio.h>
#include <string.h>
typedef long long I;
static I gcd(I a,I b){if(a<0)a=-a;if(b<0)b=-b;while(b){I t=a%b;a=b;b=t;}return a;}
static unsigned char qr[4600][4600];static int ps[700],np;
static int mod(I a,int p){return (a%p+p)%p;}
static int loc(I A,I B,I C,I D,int p){int v[3],z=0,t=mod(D,p);for(int i=0;i<3;i++){int r=mod((I[]){A,B,C}[i],p);if(r)v[z++]=r;}
 if(!z)return 0;if(p<=5){int o[3]={(int)mod(A,p),(int)mod(B,p),(int)mod(C,p)};for(int i=1;i<p;i++)for(int j=1;j<p;j++)for(int k=1;k<p;k++)if((o[0]*i*i+o[1]*j*j+o[2]*k*k)%p==t)return 1;return 0;}
 if(z==3)return 1;if(z==1)return qr[p][v[0]*t%p];if(!t)return qr[p][p-v[0]*v[1]%p];
 // p>=7: nonsingular affine binary conic has p +/- 1 solutions, at most 4 on axes.
 return 1;}
static int test(I A,I B,I C,I D,int top){I g=gcd(gcd(A,B),gcd(C,D));A/=g;B/=g;C/=g;D/=g;if((A+B+C-D)%8!=0)return 0;
 for(int i=0;i<np&&ps[i]<=top;i++){int p=ps[i];if(p>5&&A%p&&B%p&&C%p)continue;if(!loc(A,B,C,D,p))return 0;}return 1;}
static void solve(char V,int n,int k,int bound){int best=bound+1;
 if(V=='U'){for(I g=n;g<=bound;g+=n)for(I a=1;a<=bound;a++)for(I b=a;b<=bound;b++)if((g>b?g:b)<best&&test(n*a*b,n*g*b,n*g*a,k*g*a*b,n>bound?n:bound)){best=g>b?g:b;}}
 else for(I a=1;a<=bound;a++)for(I b=a;b<=bound;b++)for(I c=1;c<=bound;c++)for(I d=1;d<=(V=='X'?bound:1);d++){
 I H=b>c?b:c;if(d>H)H=d;if(H<best&&test(-a,-b,k*a*b*c*d,V=='X'?n*c:n, n>bound?n:bound))best=H;}
 printf("%c n=%d k=%d searched through H=%d min=%d\n",V,n,k,bound,best);assert(best==bound);}
int main(void){for(int i=3;i<4600;i+=2){int p=1;for(int j=3;j*j<=i;j+=2)if(i%j==0)p=0;if(p){ps[np++]=i;for(int j=1;j<i;j++)qr[i][j*j%i]=1;}}
 solve('X',4545,4,10);solve('X',4549,4,2);solve('U',131,8,786);solve('U',241,8,1928);solve('U',137,8,548);solve('S',131,8,4);solve('S',241,8,8);solve('S',137,8,4);
 // Independent Type A check: enumerate all a,b with n=4abc-4a-b;
 // b<=n+4a, and b(4ac-1)=n+4a with b>=2 for n=1 mod 4 (b=1 gives n=3 mod4).
 for(int i=0;i<3;i++){I n=(I[]){193,2521,66529}[i];int count=0;
 for(I b=2;b<=n+4*((n+2)/4+1);b++){/* a(4bc-4)=n+b implies a <=(n+b)/(4b-4) */
 for(I a=1;a*(4*b-4)<=n+b;a++)if((n+b+4*a)%(4*a*b)==0)count++;}assert(!count);printf("A %lld count %d\n",n,count);}}
