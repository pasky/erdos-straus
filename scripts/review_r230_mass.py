"""R230 from-scratch: class mass S'_e(X) = sum_{l<=X, l=3(4)} omega'_e(l)/l of the Thm 1.4 overflow-cube classes
(triples c0,d0 odd squarefree coprime, c0 d0 | K, rad R | c0, v_s(R) <= e, s^2 nmid K for s | R, 4 c0^2 d0 R^2 < l),
plus the shot-only mass S_e (Lemma 1.1: odd Q < l/2 with Q^{(e)} | K) for comparison.  Usage: X emax"""
import sys, math

def spf_sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, n + 1, i):
                if spf[j] == j: spf[j] = i
    return spf

def fac(n, spf):
    f = {}
    while n > 1:
        q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
    return f

def omega_cube(l, f, e):
    """count triples; f = factorisation of K"""
    odd = [(q, a) for q, a in f.items() if q != 2]
    lim = l / 4.0
    # recursive over primes: type 0 none, 1 in d0, 2 in c0 with rho=0..e (rho>=1 only if a==1)
    cnt = 0
    def rec(i, M):
        nonlocal cnt
        if M > lim: return
        if i == len(odd):
            cnt += 1; return
        q, a = odd[i]
        rec(i + 1, M)
        rec(i + 1, M*q)            # q | d0
        for rho in range(0, (e if a == 1 else 0) + 1):
            rec(i + 1, M*q*q*q**(2*rho))  # q | c0, v_q(R)=rho
    rec(0, 1)
    return cnt

def omega_shot(l, f, e):
    odd = [(q, a) for q, a in f.items() if q != 2]
    lim = l / 2.0
    cnt = 0
    def rec(i, Q):
        nonlocal cnt
        if Q > lim: return
        if i == len(odd):
            cnt += 1; return
        q, a = odd[i]
        rec(i + 1, Q)
        for v in range(1, a + e + 1):   # Q^{(e)} | K  <=>  v <= a + e
            if Q*q**v > lim: break
            rec(i + 1, Q*q**v)
    rec(0, 1)
    return cnt

if __name__ == "__main__":
    X = int(sys.argv[1]); emax = int(sys.argv[2])
    spf = spf_sieve(X // 4 + 2)
    isp = bytearray([1]) * (X + 1); isp[0] = isp[1] = 0
    for i in range(2, int(X**0.5) + 1):
        if isp[i]: isp[i*i::i] = bytearray(len(isp[i*i::i]))
    checkpoints = [2**k for k in range(10, 64) if 2**k <= X] + [X]
    Sc = [0.0]*(emax + 1); Ss = [0.0]*(emax + 1); ci = 0
    for l in range(3, X + 1, 4):
        if isp[l]:
            f = fac((l + 1)//4, spf)
            for e in range(emax + 1):
                Sc[e] += omega_cube(l, f, e)/l
                Ss[e] += omega_shot(l, f, e)/l
        while ci < len(checkpoints) and l + 4 > checkpoints[ci]:
            L = math.log(checkpoints[ci])
            print(f"X={checkpoints[ci]:>9} logX={L:5.2f} cube S'_e: " + " ".join(f"{s:7.3f}" for s in Sc)
                  + " | shots S_e: " + " ".join(f"{s:7.3f}" for s in Ss), flush=True)
            ci += 1
