"""Check: ET (2.1),(2.2),(2.7) with e != 0 imply (2.1)-(2.9) (rational identities in a,c,d,e)."""
import sympy as sp
a, c, d, e = sp.symbols('a c d e', positive=True)
b = c*e - a
n = (4*a*b*d - 1)/e
f = (4*a**2*d + 1)/e
ids = {
 '2.1': 4*a*b*d - (n*e + 1), '2.2': c*e - (a + b), '2.3': 4*a*b*c*d - (n*a + n*b + c),
 '2.4': 4*a*c*d*e - (n*e + 4*a**2*d + 1), '2.5': 4*b*c*d*e - (n*e + 4*b**2*d + 1),
 '2.6': 4*a*c*d - (n + f), '2.7': e*f - (4*a**2*d + 1), '2.8': b*f - (n*a + c),
 '2.9': n**2 + 4*c**2*d - f*(4*b*c*d - n)}
for k, v in ids.items():
    print(k, sp.simplify(v) == 0)
