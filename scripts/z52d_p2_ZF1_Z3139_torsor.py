# Z3139: universal torsor of the minimal resolution of the Cayley (4A1) cubic = closure of U_n, and its
# specialisation to Elsholtz–Tao's Sigma^I_n.  Symbolic checks (sympy).
import sympy as sp, itertools
l = sp.symbols('l1:5'); E = {}
for i,j in itertools.combinations(range(1,5),2): E[(i,j)] = E[(j,i)] = sp.Symbol(f'e{i}{j}')
pairs = list(itertools.combinations(range(1,5),2))
# master relation (lift of L1+L2+L3+L4 = 0 on P^2 through the complete quadrilateral)
R = sum(l[i-1]*sp.Mul(*[E[(i,j)] for j in range(1,5) if j!=i]) for i in range(1,5))
# anticanonical coordinates t_i = prod_{j!=i} l_j * prod_{pairs not containing i} e_ab
t = [sp.Mul(*[l[j-1] for j in range(1,5) if j!=i])*sp.Mul(*[E[p] for p in pairs if i not in p]) for i in range(1,5)]
sigma3 = sp.expand(sum(sp.Mul(*[t[j] for j in range(4) if j!=i]) for i in range(4)))
q, r = sp.div(sigma3, sp.expand(R), *l)
print("Cayley sigma3(t) divisible by master relation R:", sp.simplify(r)==0, "| quotient factors:", sp.factor(q))
# diagonals: d_{ab|cd} e_cd = l_a e_a? e_a? + l_b e_b? e_b?  (two forms; consistency <=> R = 0)
def diag(a,b):
    c,d = [k for k in range(1,5) if k not in (a,b)]
    f1 = (l[a-1]*E[(a,c)]*E[(a,d)] + l[b-1]*E[(b,c)]*E[(b,d)])/E[(c,d)]
    f2 = -(l[c-1]*E[(c,a)]*E[(c,b)] + l[d-1]*E[(d,a)]*E[(d,b)])/E[(a,b)]
    return sp.simplify(sp.numer(sp.together(f1-f2)) - 0)
for (a,b) in [(1,2),(1,3),(2,3)]:
    num = sp.expand(sp.numer(sp.together(diag(a,b))))
    print(f"diagonal {a}{b}: two expressions agree mod R:", sp.simplify(sp.expand(num) - sp.expand(R)*sp.simplify(num/R))==0, "num/R =", sp.factor(num/R))
# specialisation to ET Sigma^I_n: (a,b,c,d,e,f) = (e34,e24,e14,-l4/4, d23, d13), w-face (l1,l2,l3,e12,e13,e23) = (1,1,1,1,1,n)
a,b,c,d,n = sp.symbols('a b c d n', positive=True)
sub = {l[0]:1,l[1]:1,l[2]:1,E[(1,2)]:1,E[(1,3)]:1,E[(2,3)]:n,E[(3,4)]:a,E[(2,4)]:b,E[(1,4)]:c,l[3]:-4*d}
lam = sp.Rational(-1,4)
xyzw = [sp.simplify(lam*ti.subs(sub)) for ti in t]
print("(x,y,z,t4) =", xyzw, " ET pi^I_n = (abdn, acd, bcd), t4 should be -n/4")
print("master relation ->", sp.expand(R.subs(sub)), "  (ET (2.3): 4abcd = na + nb + c)")
for (A,B) in [(2,3),(1,3),(1,2)]:
    C,D = [k for k in range(1,5) if k not in (A,B)]
    print(f"diag {A}{B}|{C}{D}:  d*{E[(C,D)].subs(sub)} =", sp.expand((l[A-1]*E[(A,C)]*E[(A,D)] + l[B-1]*E[(B,C)]*E[(B,D)]).subs(sub)))
# Type II chart: w-face (l1,l2,l3,e12,e13,e23) = (n,1,1,1,1,1)
sub2 = {l[0]:n,l[1]:1,l[2]:1,E[(1,2)]:1,E[(1,3)]:1,E[(2,3)]:1,E[(3,4)]:a,E[(2,4)]:b,E[(1,4)]:c,l[3]:-4*d}
print("Type II chart (x,y,z,t4) =", [sp.simplify(lam*ti.subs(sub2)) for ti in t], "; master ->", sp.expand(R.subs(sub2)), " (ET Prop 2.7: 4abcd = a + b + nc)")
