# Structure forced on exceptional primes (Lemma 4.1 of Z56_FAMTRY.md), checked on the 14 (★)-zeros <= 1e10.
from sympy import factorint
Z=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
def classes(n,m): return sorted({q%m for q in factorint(n)})
print("p  p%24  p%7  p%11  cls4((p+1)/2)  cls4(4p+1)  cls8(p+2)  cls8(8p+1)  cls12((p+3)/4)  cls16(p+4)")
for p in Z:
    print(p, p%24, p%7, p%11, classes((p+1)//2,4), classes(4*p+1,4), classes(p+2,8), classes(8*p+1,8), classes((p+3)//4,12), classes(p+4,16))
