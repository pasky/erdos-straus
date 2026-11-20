"""First {1,3,5} times prime witness on the stored z76 hard panel; bounded misses only."""
from pathlib import Path
from math import isqrt
from hashlib import sha256
root=Path('data/z77/proth'); screens=Path('data/z58/screens')
def prime(n):
    if n<2 or n%2==0:return n==2
    d=n-1
    while d%2==0:d//=2
    for a in [2,325,9375,28178,450775,9780504,1795265022]: # deterministic below 2^64
        if a%n==0:continue
        v=pow(a,d,n);j=d
        while v not in (1,n-1) and j<n-1:v=v*v%n;j*=2
        if v!=n-1 and (j!=d or v!=1):return False
    return True

def run():
    B=5_000_000;sieve=bytearray(b'\1')*(B+1);sieve[:2]=b'\0\0';
    for i in range(2,isqrt(B)+1):
        if sieve[i]:sieve[i*i::i]=bytes((B-i*i)//i+1)
    menu=[f for f in range(7,B,8) if any(f%c==0 and sieve[f//c] for c in (1,3,5))];
    panel={int(l.split()[2]) for l in Path('data/z76/disproof/comp/hard.txt').read_text().splitlines() if l.startswith('hard ')}
    for file in ['star_prime_zeros.txt','r8_zeros_1e10.txt','gstar_zeros.txt']:
        panel.update(int(l.split()[0]) for l in (screens/file).read_text().splitlines() if l and l[0].isdigit())
    panel.update([193,2521,3361,66529,21841,76441,131,241,1590284203561]); P=sorted(n for n in panel if n%8==1 and n<2**64 and prime(n)); print('distinct primes',len(P));rows=[];miss=[]
    for n in P:
        f=next((f for f in menu if (r:=-n%f) and (f+1)%r==0),0)
        if not f:miss.append(n)
        rows.append((n,f))
    txt=''.join('%d %d\n'%r for r in rows);print('B',B,'misses',miss,'largest returned',max(f for n,f in rows),'sha256',sha256(txt.encode()).hexdigest());(root/'u7-panel.txt').write_text(txt)
if __name__=='__main__':run()
