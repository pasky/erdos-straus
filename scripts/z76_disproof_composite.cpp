// Positive-witness hunt only. Composite square-shifts with a stack of three dead primes.
#include <cassert>
#include <cstdio>
#include <cstdint>
using U=uint64_t;
int main(){
    const U step=420*13*17*29;
    for(U t=0;t<step;t+=60){
        U r=t%7;
        if(r!=0 && r!=1 && r!=6) continue;
        if((t*t+1)%(13*17*29))continue;
        for(U m=t;m<=1000000000;m+=step){
            U n=m*m+1; if(n<=100000000000ULL)continue;
            U R=0,G=0;
            for(U f=3; f<=200000003 && (!R||!G);f+=4){
                U u=f-n%f;
                if(!R && (f+1)/4%u==0)R=f;
                if(!G && f%8==7 && (f+1)%u==0)G=f;
            }
            // Zeros in the last fields would mean UNRESOLVED.
            std::printf("%llu %llu %llu %llu\n",(unsigned long long)m,(unsigned long long)n,(unsigned long long)R,(unsigned long long)G);
        }
    }
}
