/* z78 cross-review: shared 64-bit factorisation (trial division, Pollard-Brent, deterministic MR). */
static U mulm(U a,U b,U m){return (Z)a*b%m;}
static U powm(U a,U e,U m){U t=1;a%=m;while(e){if(e&1)t=mulm(t,a,m);a=mulm(a,a,m);e>>=1;}return t;}
static int mr(U n){if(n<2)return 0;static const U B[]={2,3,5,7,11,13,17,19,23,29,31,37};
 for(int i=0;i<12;i++){if(n%B[i]==0)return n==B[i];}
 U d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
 for(int i=0;i<12;i++){U x=powm(B[i],d,n);if(x==1||x==n-1)continue;int ok=0;for(int k=1;k<s;k++){x=mulm(x,x,n);if(x==n-1){ok=1;break;}}if(!ok)return 0;}
 return 1;}
static U gcdu(U a,U b){while(b){U t=a%b;a=b;b=t;}return a;}
static U rho(U n){if(n%2==0)return 2;for(U c=1;;c++){U y=2,x,g=1,q=1,ys=0;U m=128,rr=1;
 do{x=y;for(U i=0;i<rr;i++)y=(mulm(y,y,n)+c)%n;U k=0;
  do{ys=y;for(U i=0;i<m&&i<rr-k;i++){y=(mulm(y,y,n)+c)%n;q=mulm(q,x>y?x-y:y-x,n);}g=gcdu(q,n);k+=m;}while(k<rr&&g==1);rr*=2;}while(g==1);
 if(g==n){do{ys=(mulm(ys,ys,n)+c)%n;g=gcdu(x>ys?x-ys:ys-x,n);}while(g==1);}
 if(g!=n)return g;}}
static U fp[64];static int fe[64],nfp;
static void addp(U p){for(int i=0;i<nfp;i++)if(fp[i]==p){fe[i]++;return;}fp[nfp]=p;fe[nfp++]=1;}
static void fac(U n){if(n==1)return;if(mr(n)){addp(n);return;}U d=rho(n);fac(d);fac(n/d);}
static void factor(U n){nfp=0;for(U p=2;p<200&&p*p<=n;p++){while(n%p==0){addp(p);n/=p;}}if(n>1)fac(n);}
