"""R139 from-scratch checks of 17D Lemmas 2.1-2.3 and Remark 2.4 on brute-forced data.
P: all N-points of Sigma^II_N, N=17^K (K=1,3,5): 4abd = N+e, e|a+b, c=(a+b)/e (both orders, no filters).
Q: all N-points of Sigma^I_F, F=17^k (k=1,3,5): 4abcd = F(a+b)+c, i.e. 4abd = eF+1, c=(a+b)/e."""
import random, math, sys
random.seed(139)
def Pdata(K):
    N = 17**K; out = []
    a = 1
    while (4*a-1)*3 <= 4*N+1:
        bmax = (4*N+1)//(4*a-1)
        bmax = (bmax+1)//4
        for b in range(1, bmax+1):
            m = 4*a*b; e = (-N) % m
            if e == 0 or e > a+b or (a+b) % e: continue
            d = (N+e)//m; c = (a+b)//e
            assert 4*a*b*c*d == a+b+N*c
            out.append((a,b,c,d,e))
        a += 1
    return out
def Qdata(k):
    """all points with a<=b: b = (Fa+c)/f, f = 4acd-F >= 1; a<=b <=> f <= F + c/a, so 4acd <= 2F + c."""
    F = 17**k; out = []
    for a in range(1, F+1):
        for c in range(1, 2*F+1):
            if 4*a*c > 2*F + c: break
            for d in range(1, 2*F+1):
                if 4*a*c*d > 2*F + c: break
                f = 4*a*c*d - F
                if f < 1 or (F*a+c) % f: continue
                b = (F*a+c)//f
                if b < a or (a+b) % c: continue
                e = (a+b)//c; assert 4*a*b*c*d == F*(a+b)+c; out.append((a,b,c,d,e))
    return out
fails = 0
for K in (1,3,5):
    N = 17**K; L = (K+1)//2; W = 17**L; assert W*W == 17*N
    D = Pdata(K); print("K",K,"P-points (ordered):",len(D))
    for (a,b,c,d,e) in D:
        if not (4*a*b <= N+a+b): fails += 1; print("L2.2i", a,b)
        # Lemma 2.1(i): box -f mod W, f=4acd-1; for random u=-p/q, membership iff 17∤b and qa≡pb
        f = 4*a*c*d-1
        if b % 17:
            assert (b*f - a) % W == 0
        for _ in range(20):
            q = random.randint(1,60); p = random.randint(-60,60)
            if p == 0 or math.gcd(p,q) != 1 or (p*q) % 17 == 0: continue
            u = (-p*pow(q,-1,W)) % W
            if u % 17 != 5: continue
            inbox = ((-f) - u) % W == 0
            if inbox != (b % 17 != 0 and (q*a-p*b) % W == 0): fails += 1; print("L2.1i", a,b,p,q)
        # Remark 2.4: choose p,q with qa ≡ pb mod W, arbitrary lift; also coprime-free
        for _ in range(10):
            q = random.randint(1, 10**6)
            if b % 17 == 0:
                # no inverse; take p with q a - p b ≡ 0 mod W if solvable
                g = math.gcd(b, W)
                if (q*a) % g: continue
                p = ((q*a//g) * pow(b//g, -1, W//g)) % (W//g) + random.randint(-50,50)*(W//g)
            else:
                p = (q*a*pow(b,-1,W)) % W + random.randint(-50,50)*W
            assert (q*a-p*b) % W == 0
            z = (q*a-p*b)//W
            lhs = e*(c*(p*p*b+q*q*a)+17*z*z); rhs = a*b*((p+q)**2+68*d*z*z)
            if lhs != rhs: fails += 1; print("R2.4 identity", a,b,p,q)
            if ((p+q)**2+68*d*z*z) % e: fails += 1; print("R2.4 div", (a,b,c,d,e),p,q,z, "17|b" if b%17==0 else "")
        # Lemma 2.3(ii): no datum on ray (2λ,3λ) whose box contains -2/3
        if 3*a == 2*b and b % 17: fails += 1; print("L2.3 P ray", a,b)
for k in (1,3):
    F = 17**k; D = Qdata(k); D1 = [x for x in D if x[0] <= x[1]]
    print("k",k,"Q-points (ordered):",len(D), " a<=b:", len(D1), " 17∤e:", sum(1 for x in D1 if x[4]%17))
    for (a,b,c,d,e) in D:
        if a <= b and a*c*d > (F+1)//2: fails += 1; print("L2.2ii", a,b,c,d)
        assert (4*a*b*d - e*F) == 1 and (4*a*a*d*b - a) % F == 0
        if 3*a == 2*b: fails += 1; print("L2.3 Q ray", a,b)
print("failures:", fails)
