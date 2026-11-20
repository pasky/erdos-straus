/* Add translated Mordell progressions to the z75 R8 sieve. Re-use its CRT
   crossing, but only cross primality moduli AFTER the witness sieve: full
   Eratosthenes scans per block cost more than exact primality of survivors.
   Report integer/prime survivor counts (not the total number of primes).
   No presumption that every survivor is a zero: finish with exact(). */
#define main z75_ap_unused_main
#include "z75_push2_prime_ap.c"
#undef main

/* Exact at these heights: divide by every prime <= sqrt(last). */
static int *primes,nprime;
static void trial_table(I last){
    int lim=(int)sqrtl(last)+1;
    char *comp=calloc(lim+1,1); primes=malloc((lim+1)*sizeof *primes);
    assert(comp && primes);
    for(int t=2;t<=lim;++t)if(!comp[t]){
        primes[nprime++]=t;
        for(I j=(I)t*t;j<=lim;j+=t)comp[j]=1;
    }
    free(comp);
}
static int prime(I n){
    for(int i=0;i<nprime && (I)primes[i]*primes[i]<=n;++i)
        if(n%primes[i]==0)return 0;
    return 1;
}
int main(int ac,char **av){
    if(ac==2 && !strcmp(av[1],"check")){
        I n;char ty;
        while(scanf(" %c %ld",&ty,&n)==2){
            assert(n>0 && n<100000000000000LL && (ty=='C'||ty=='R'||ty=='A'));
            exact(n,ty=='C'?8:4,ty=='A');
        }
        return 0;
    }
    if(ac!=5)return 2;
    step=atol(av[1]);I res=atol(av[2]),lo=atol(av[3]),hi=atol(av[4]);
    assert(step>0 && step<=20000000 && res>=0 && res<step && lo>1000000000000LL && lo<hi && hi<100000000000000LL);
    first=lo+(res-lo%step+step)%step;
    I len=(hi-first)/step+1,last=first+(len-1)*step;
    assert(first<=hi);trial_table(last);
    const int k=8,b=40000;
    for(I u=1;u<=b;u++)for(I v=1;u*v<=b;v++){
        I t=u*v;if(u<=v)add(k*t,-u-v);add(k*t-1,-u);
    }
    /* Crossing small composite factors early is also cheap. */
    for(int i=0;primes[i]<=5000;i++)add(primes[i],0);
    qsort(s,ns,sizeof(*s),cmp);size_t z=0;
    for(size_t i=0;i<ns;i++)if(i==0||cmp(s+i,s+z-1))s[z++]=s[i];
    ns=z;
    enum{BLOCK=4194304};char *rej=malloc(BLOCK);assert(rej);
    I late=0,hard=0,miss=0;
    for(I base=0;base<len;base+=BLOCK){
        int bl=len-base<BLOCK?len-base:BLOCK;memset(rej,0,bl);
        for(size_t i=0;i<ns;i++){
            int j=s[i].r;for(;j<bl;j+=s[i].m)rej[j]=1;s[i].r=j-bl;
        }
        for(int j=0;j<bl;j++)if(!rej[j]){
            I n=first+step*(base+j);int ok=0;late++;
            for(int f=k*b+k-1;f<=2000000;f+=k){int r=f-n%f;if(((f+1)/k)%r==0){ok=1;break;}}
            if(!ok && prime(n)){hard++;miss+=!exact(n,k,0);}
        }
    }
    printf("# k=8 first=%ld last=%ld step=%ld length=%ld late_integers=%ld hard_primes=%ld miss=%ld\n",first,last,step,len,late,hard,miss);
    free(rej);free(primes);free(s);return 0;
}
