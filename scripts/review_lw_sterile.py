"""R180: numeric check of Thm 4.2: nu(l,c) (=-1 at q!=l, =c in Z_l) is not covered by any fixed-pair family of modulus <= D."""
import sys
D = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
def nu_mod(l, c, d):
    j, e = 0, d
    while e % l == 0: e //= l; j += 1
    lj = l ** j
    # CRT: r = c mod lj, r = -1 mod e
    if lj == 1: return (-1) % e
    if e == 1: return c % lj
    inv = pow(lj, -1, e)
    r0 = c % lj
    t = ((-1 - r0) * inv) % e
    return (r0 + lj * t) % d
def covers(l, c):
    out = []
    for x in range(2, D):
        for y in range(2, D // x + 2):
            d = x * y - 1
            if d > D: break
            if (nu_mod(l, c, d) + x) % d == 0: out.append(("xy", x, y)); 
        for z in range(x, D // x + 1):
            d = x * z
            if (nu_mod(l, c, d) + x + z) % d == 0: out.append(("xz", x, z))
        if len(out) > 3: break
    return out
for l in [2, 3, 5, 7, 11, 13, 17, 101]:
    print(l, "nu(l,l-1) covers:", covers(l, l - 1)[:4])
print("control nu(3,0):", covers(3, 0)[:2], " nu(5,1):", covers(5, 1)[:2])
