# z78 MASULLO_GRH_TRANSFER Lemma 4 census: for primes l = 3 (4), check the multiplicative stabiliser of D = divisors of (l+1)/4 in F_l^* is trivial.
# Replay: ulimit -v 2000000; timeout 300 uv run --offline --no-project python scripts/z78_masullo_kummer_stab.py 200000  (expect "done 0")
# for primes l = 3 mod 4, D = divisors of A=(l+1)/4 as residues; find nontrivial h with h*D = D (stabilizer)
import sys
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
def divs(a):
    r=[];i=1
    while i*i<=a:
        if a%i==0: r.append(i); r.append(a//i)
        i+=1
    return set(r)
bad=0
for l in primes(int(sys.argv[1])):
    if l%4!=3 or l<7: continue
    A=(l+1)//4; D=divs(A)
    for d in D:
        if d==1: continue
        if all((d*x)%l in D for x in D): print("stab",l,d); bad+=1
print("done",bad)
