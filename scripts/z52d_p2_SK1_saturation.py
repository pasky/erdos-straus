# z52d pass2 SK1 (Z0990): is f = 4xyz - p(xy+xz+yz) irreducible, and does it vanish on a coordinate plane?
# If f is irreducible and xyz is not a zero divisor mod f, then the saturation (f) : (xyz)^inf = (f).
import sympy as sp
x, y, z, p = sp.symbols('x y z p')
f = 4*x*y*z - p*(x*y + x*z + y*z)
fl = sp.factor_list(f)
print("factor_list(f) with p symbolic:", fl)
for pv in [5, 13, 17, 37, 401, 577, 2521]:
    fv = sp.expand(f.subs(p, pv))
    print("p=%d:" % pv, sp.factor_list(fv)[1][0][1] if len(sp.factor_list(fv)[1]) else None, "n_factors", len(sp.factor_list(fv)[1]))
for name, sub in [("x=0", {x: 0}), ("y=0", {y: 0}), ("z=0", {z: 0})]:
    print(name, "restriction:", sp.factor(f.subs(sub)))
