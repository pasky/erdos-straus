// For random n ≡ 1 mod 24 of given bit size (or primes from a range), compute H4(n) = least v with a bichromatic(slot) parent edge.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static uint64_t s[2]={0x12345678abcdefULL,0x9e3779b97f4a7c15ULL};
static uint64_t rnd(void){uint64_t s1=s[0];const uint64_t s0=s[1];s[0]=s0;s1^=s1<<23;s[1]=s1^s0^(s1>>17)^(s0>>26);return s[1]+s0;}
int main(int argc,char**argv){ int bits=atoi(argv[1]); long samples=atol(argv[2]); long cap=atol(argv[3]); s[0]^=atol(argv[4]);
 long hist[64]={0}; long over=0;
 for(long it=0;it<samples;it++){
   u128 n=((u128)rnd()<<64)|rnd(); if(bits<128) n &= (((u128)1)<<bits)-1; n|=((u128)1)<<(bits-1);
   n = n - (n%24) + 1;
   long H=-1;
   for(long v=2; v<=cap; v++){
     long a = (long)(v - (long)(n % (u128)v)) % v; if(a==0) continue; // a = -n mod v, need 1<=a<v
     // edge iff a*v | n + a + v
     u128 m = n + (u128)a + (u128)v;
     if(m % (u128)((u128)a*v)) continue;
     u128 t = m / ((u128)a*v);
     int slot = ((t&3)==0)||((a&3)==0)||((v&3)==0)||((((t*(u128)a)-1)&3)==0)||((((t*(u128)v)-1)&3)==0);
     if(slot){H=v;break;}
   }
   if(H<0) over++; else { int b=0; while((1L<<(b+1))<=H) b++; hist[b]++; }
 }
 // survival P(H>2^k)
 long cum=over; printf("bits=%d samples=%ld cap=%ld over=%ld\n",bits,samples,cap,over);
 for(int b=63;b>=0;b--){ if(b<=20) {} }
 for(int k=2;k<=20;k++){ long c=over; for(int b=k;b<64;b++) c+=hist[b]; if((1L<<k)<=cap) printf("X=%ld P(H>=X)=%.3g\n",1L<<k,(double)c/samples); }
}
