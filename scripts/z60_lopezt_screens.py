# z60 LOPEZT: mandatory screens from data/z58/screens/, in (U5) coordinates.
# For each n: least BN witness g (g=3 mod 4, (-n mod g) | (g+1)/4), least B4 witness g ((-n*4^-1 mod g) | (g+1)/4),
# and (K=8) least B4_8 witness (g=7 mod 8, (-n*8^-1 mod g) | (g+1)/8). Search g <= GCAP (a witness found is a certificate;
# "none" below GCAP is NOT a proof of absence; absences are taken from the certified files).
import sys
GCAP=4_000_000
def least(n,K,branch):
    for g in range(K-1, GCAP, K):
        if n%g==0: continue
        Q=(g+1)//K
        if branch=="BN": r=(-n)%g
        else: r=(-n*pow(K,-1,g))%g
        if r and Q%r==0: return g
    return None
def load(f): return [int(l.split()[0]) for l in open(f) if l.strip() and not l.startswith('#')]
D='data/z58/screens/'
star=load(D+'star_prime_zeros.txt'); gstar=load(D+'gstar_zeros.txt'); r8=load(D+'r8_zeros_1e10.txt'); comp=load(D+'composite_zeros_le8e6.txt')
print("== 12 R8-zero primes in [1e10,1.1e10]: least B4 witness (K=4), least B4_8 witness (K=8), least BN witness")
for n in r8: print(n, least(n,4,"B4"), least(n,8,"B4"), least(n,4,"BN"))
print("== 14 star (BN) zeros: least B4 witness"); print([(n,least(n,4,"B4")) for n in star])
print("== 38 G*-zeros: B4 witness for all?, BN witness (None expected exactly for the 14 star zeros)")
w=[(n,least(n,4,"B4"),least(n,4,"BN")) for n in gstar]
print("all have B4:", all(x[1] for x in w), "; with BN witness:", sum(1 for x in w if x[2]), "; BN-less set == star zeros:", sorted(x[0] for x in w if not x[2])==sorted(star), "; star subset of gstar:", set(star)<=set(gstar))
print("== 285 composite BN-zeros: B4 witness count and the exceptions")
c=[(n,least(n,4,"B4")) for n in comp]
print("count:",len(c),"; with B4 witness:",sum(1 for x in c if x[1]),"; without:",[x[0] for x in c if not x[1]])
