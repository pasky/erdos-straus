/* Rematch z75 anchors without consulting their outcomes. Only the first two
   columns (tag, p) of its artifact are read. Reuse the deterministic 64-bit
   primality test, 61-smooth classifier and five positive-word detectors. */
#define main z75_panel_unused_main
#include "z75_push2_prime_panels.cpp"
#undef main
#include <iostream>
#include <sstream>

constexpr U M=32*27*25*49;
/* Find nearest feasible, unused control in the same trillion bin and
   within 0.1% of anchor p. Tie towards the higher n. */
static U match(U p,bool sm,bool sh){
    for(U d=M;d<=p/1000;d+=M)for(U n:{p+d,p-d}){
        if(n/LO!=p/LO || used.count(n) || near(n) || smooth(n-1)!=sm)continue;
        if(prime(n) && prime(12*n+1)==sh)return n;
    }
    return 0;
}
/* Enumerate actual square-offset Mordell inputs, not just AP mimics. For
   survivors of the word cap, output for the separate exact solver. */
static U counts[840],late[840],capped[840],capR[840],capA[840];
static constexpr U floor_n=1511088831001ULL;
static void screen(U n){
    U r=n%840; ++counts[r]; unsigned f;
    for(f=7;f<=2000000;f+=8){unsigned u=f-n%f;if(((f+1)/8)%u==0)break;}
    late[r]+=f>1000;
    if(f>2000000){++capped[r];printf("C %lu\n",n);}
    for(f=3;f<=2000000;f+=4){unsigned u=f-n%f;if(((f+1)/4)%u==0)break;}
    if(f>2000000){++capR[r];printf("R %lu\n",n);}
    for(f=3;f<=2000000;f+=4){unsigned u=f-n%f;if((u==1||u%4==0)&&(f+1)%u==0)break;}
    if(f>2000000){++capA[r];printf("A %lu\n",n);}
}
static int surgical(bool square){
    if(square){
    for(U m=2;m<=6000000;m+=2){
        U n=m*m+1, r=n%840;
        if(n<=floor_n || !(r==1||r==121||r==169||r==289||r==361||r==529) || !prime(n))continue;
        screen(n);
    }
    }else{
        gen(840,0); // both shift statuses, no square offsets
        for(auto arm:{&pos,&neg})for(U n:*arm)if(n>floor_n)screen(n);
    }
    for(int r:{1,121,169,289,361,529})if(counts[r])printf("# %s r=%d primes=%lu f_gt_1000=%lu cap8=%lu capR=%lu capA=%lu\n",square?"sq+1":"smooth61",r,counts[r],late[r],capped[r],capR[r],capA[r]);
    return 0;
}
int main(int ac,char**av){
    if(ac==2 && std::string(av[1])=="squares")return surgical(true);
    if(ac==2 && std::string(av[1])=="smooth")return surgical(false);
    assert(ac==1);
    std::vector<std::pair<std::string,U>> anchors;
    for(std::string line;std::getline(std::cin,line);){
        std::istringstream row(line);std::string tag;U p;
        if((row>>tag>>p) && (tag=="sm+" || tag=="sq")){
            anchors.emplace_back(tag,p);assert(used.insert(p).second);
        }
    }
    assert(anchors.size()==2048+720);
    puts("# family anchor n f_R f_A f_U7 f_S f_R8");
    for(auto [tag,p]:anchors){
        if(tag=="sm+"){
            U a=match(p,true,false), b=match(p,false,true), c=match(p,false,false);
            if(!a||!b||!c){printf("# incomplete quartet %lu %d %d %d\n",p,!!a,!!b,!!c);continue;}
            used.insert(a);used.insert(b);used.insert(c);
            emit("sm+",p,p);emit("sm-",p,a);emit("rough+",p,b);emit("rough-",p,c);
        }else{
            U c=match(p,smooth(p-1),prime(12*p+1));
            if(!c){printf("# incomplete pair %lu\n",p);continue;}
            used.insert(c);emit("sq",p,p);emit("sq_ctl",p,c);
        }
    }
    return 0;
}
