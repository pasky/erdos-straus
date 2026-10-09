"""R99: classify relaxed solutions 'L u W c' g delta P1 X' (review_typei5_relax output) into case A / regimes."""
import sys
for line in open(sys.argv[1]):
    L, u, W, cp, g, de, P1, X = line.split(); L, u, W, cp, g, de, P1 = map(int, (L, u, W, cp, g, de, P1))
    T = 2**(L-4); X = (1 + W*u*(T*u - cp*g*de)//P1)//(4*cp*g)
    Q1 = (W*cp*de*de + T)//P1
    assert 16*cp*P1*X*X - W*Q1*u*u == 1
    y = cp*g*de; j = T*u//2 - y
    if j < 0: print(line.strip(), "caseA"); continue
    m = cp*de*de; rho = (T*u//2 + j)//P1; lam = (rho*j - m)//u
    assert (T*u//2 + j) % P1 == 0 and (rho*j - m) % u == 0
    sig = 8*W*m*j + 4*T*j - T*T*u
    print(line.strip(), "j=%d lam=%d sig=%d" % (j, lam, sig), "ii" if lam < 0 else "iii" if sig < 0 else "iv" if sig == 0 else "v")
