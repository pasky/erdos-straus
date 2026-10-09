#!/usr/bin/env python3
"""R100 extra checks: (1) symbolic identity for the 7 ES parametrisations used in review_m13c_tree.py;
(2) negative controls for that checker; (3) open-leaf moduli / split primes claims; (4) roots."""
import copy, gzip, json, sys
import sympy as sp
sys.path.insert(0, "scripts")
import review_m13c_tree as R

n, a, b, c, d, e, f = sp.symbols("n a b c d e f", positive=True)
def ident(x, y, z):
    return sp.simplify(4/n - 1/x - 1/y - 1/z) == 0
# auxiliary coordinates as rational functions, exactly as in review_m13c_tree.solution
fams = {
 "I1": dict(c=(n+f)/(4*a*d), e=(4*a**2*d+1)/f, T="I", bce=True),
 "I2": dict(b=(n*a+c)/f, d=(n+f)/(4*a*c), T="I"),
 "I3": dict(a=(n+f)/(4*c*d), b=(n*(n+f)+4*c**2*d)/(4*c*d*f), T="I"),
 "I4": dict(c=(a+b)/e, d=(n*e+1)/(4*a*b), T="I"),
 "II1": dict(c=(a+b)/e, d=(n+e)/(4*a*b), T="II"),
 "II2": dict(c=(f+1)/(4*a*d), e=(n+4*a**2*d)/f, T="II", bce=True),
 "II3": dict(c=(n+4*a**2*d+e)/(4*a*d*e), T="II", bce=True),
}
for k, D in fams.items():
    v = dict(a=a, b=b, c=c, d=d, e=e)
    for key in "abcde":
        if key in D: v[key] = D[key]
    if D.get("bce"): v["b"] = v["c"]*v["e"] - v["a"]
    A, B, C, Dd = v["a"], v["b"], v["c"], v["d"]
    xyz = (A*B*Dd*n, A*C*Dd, B*C*Dd) if D["T"] == "I" else (A*B*Dd, A*C*Dd*n, B*C*Dd*n)
    print(k, "identity", ident(*xyz))

path = "data/mordell13c/tree6_6000.json.gz"
t = json.load(gzip.open(path))
# (3) open moduli and split primes
B = 2**4 * 3**2 * 5**2 * 7**2 * 11 * 13
for p in sp.primerange(17, 84): B *= p
splits = set(); bad = 0
def walk(nd):
    global bad
    if "children" in nd:
        splits.add(nd["split"]); [walk(ch) for ch in nd["children"]]
    elif "open" in nd and B % nd["L"]: bad += 1
for r in t["roots"]: walk(r)
print("split primes:", sorted(splits), "max", max(splits), "open moduli not dividing B:", bad)
print("roots:", sorted(r["x"] for r in t["roots"]), "Legendre(.,13):", [sp.legendre_symbol(r["x"] % 13, 13) for r in t["roots"]])

# (2) negative controls
def run(tt):
    import tempfile, os
    fn = tempfile.mktemp(suffix=".json.gz")
    with gzip.open(fn, "wt") as fh: json.dump(tt, fh)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        _, err = R.main(fn)
    os.remove(fn); return len(err)
def first(nd, pred):
    if pred(nd): return nd
    for ch in nd.get("children", []):
        r = first(ch, pred)
        if r: return r
t1 = copy.deepcopy(t); lf = first(t1["roots"][0], lambda z: "leaf" in z); lf["leaf"][3][2] += 2
print("NC1 perturbed param ->", run(t1), "errors")
t2 = copy.deepcopy(t); sp_ = first(t2["roots"][1], lambda z: "children" in z); sp_["children"].pop()
print("NC2 deleted child ->", run(t2), "errors")
t3 = copy.deepcopy(t); lf = first(t3["roots"][2], lambda z: "leaf" in z); lf["x"] += lf["leaf"][0] if False else 0
lf["leaf"][1] = (lf["leaf"][1] + 2) % lf["leaf"][0]
print("NC3 wrong residue ->", run(t3), "errors")
t4 = copy.deepcopy(t); op = first(t4["roots"][3], lambda z: "open" in z); op.pop("open"); op["leaf"] = [4, 1, "II1", [1, 1, 2]]
print("NC4 open leaf faked as II1(1,1,2) ->", run(t4), "errors")
