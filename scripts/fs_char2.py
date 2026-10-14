"""fs_char2.py (O216): char-2 Frobenius-square families of FF_STERILE_PUSH §4: E = 1 + T g, E^2 = 1 + T^2 g^2 = D, and E | T^2 g^2 + 1 (the residue of s). usage: uv run --with sympy python scripts/fs_char2.py"""
# check over F_2[T] (q=2) and F_4: Frobenius-square family identity (1 + c T g)^2 = 1 + c^2 T^2 g^2 and
# validity residue: for x ≡ 1 at E's primes, s = a0 + X/b0 ≡ 0 mod E, with a0 = b0 = g', A = T^2.
from sympy import symbols, Poly, GF
T=symbols('T')
p=2
for g in [Poly(T+1,T,modulus=p), Poly(T**2+T+1,T,modulus=p), Poly(T**3+T+1,T,modulus=p)]:
    E=Poly(1,T,modulus=p)+Poly(T,T,modulus=p)*g
    D=Poly(1,T,modulus=p)+Poly(T**2,T,modulus=p)*g*g
    assert E*E==D
    # residue of s = a0 + X/b0 mod E with P ≡ 1, X ≡ T^{-2}: s ≡ g + 1/(T^2 g) = (T^2 g^2 + 1)/(T^2 g) = E^2/(T^2 g)
    num=Poly(T**2,T,modulus=p)*g*g+Poly(1,T,modulus=p)
    print(g, 'E=',E, 'E^2==D', E*E==D, 'E | T^2g^2+1:', num.rem(E).is_zero)
