"""z39: per-level Kronecker decomposition of the ES word count (METAPLECTIC_ES Thm K).

(1) Kronecker's identity  sum_{r,s>=0} x^r y^s Q^{rs} - sum_{r,s>=1} x^-r y^-s Q^{rs}
      = (Q;Q)^2 theta(xy)/(theta(x)theta(y)),  theta(x) = (x;Q)(Q/x;Q),
    checked as a q-series at x = y = q^{t-1}, Q = q^t (a t-torsion point), t = 2..T.
(2) Thm K coefficient form: P_t(n) = D^-(N) - boundary, Q_t(n) = D^+(N), N = tn+1, where
    P_t = sum_{u,v>=2} q^{tuv-u-v} (ES words of level t), Q_t = sum_{r,s>=0} q^{trs+r+s}.
(3) size split of R(n) into even part E = sum_t (D^- + D^+)/2 and odd part O = sum_t (D^- - D^+)/2 at primes.
usage: python z39_kronecker.py [T] [M] [P0]
"""
import sys
from math import isqrt

T = int(sys.argv[1]) if len(sys.argv) > 1 else 12
M = int(sys.argv[2]) if len(sys.argv) > 2 else 400
P0 = int(sys.argv[3]) if len(sys.argv) > 3 else 100000


def mul(a, b, M):
    c = [0] * (M + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(0, M + 1 - i):
                if b[j]:
                    c[i + j] += x * b[j]
    return c


def inv(a, M):
    # a[0] = 1 assumed
    b = [0] * (M + 1)
    b[0] = 1
    for n in range(1, M + 1):
        b[n] = -sum(a[k] * b[n - k] for k in range(1, n + 1) if a[k])
    return b


def poch(shift, step, M):
    """prod_{k>=0} (1 - q^{shift + step k}), shift >= 1"""
    a = [0] * (M + 1)
    a[0] = 1
    e = shift
    while e <= M:
        b = a[:]
        for i in range(M + 1 - e):
            b[i + e] -= a[i]
        a = b
        e += step
    return a


def kron_numeric(t, qv=0.3 + 0.2j, R=200):
    X = qv ** (t - 1)
    Q = qv ** t
    lhs = 0
    for r in range(R):
        for s in range(R):
            lhs += qv ** ((t - 1) * (r + s) + t * r * s)
            if (t - 1) * (r + s) + t * r * s > 400:
                break
    for r in range(1, R):
        for s in range(1, R):
            term = qv ** (t * r * s - (t - 1) * (r + s))
            lhs -= term
            if abs(term) < 1e-30 and s > 3:
                break

    def pq(x):
        p = 1
        for k in range(400):
            p *= 1 - x * Q ** k
        return p

    def th(x):
        return pq(x) * pq(Q / x)
    rhs = pq(Q) ** 2 * th(X * X) / th(X) ** 2
    return abs(lhs - rhs)


def divisors(N):
    ds = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            ds.append(i)
            if i * i != N:
                ds.append(N // i)
        i += 1
    return ds


def check_K(T, M):
    bad = 0
    for t in range(2, T + 1):
        P = [0] * (M + 1)
        Qs = [0] * (M + 1)
        for u in range(2, M + 2):
            for v in range(2, M + 2):
                e = t * u * v - u - v
                if e > M:
                    break
                P[e] += 1
        for r in range(0, M + 1):
            for s in range(0, M + 1):
                e = t * r * s + r + s
                if e > M:
                    break
                Qs[e] += 1
        for n in range(1, M + 1):
            N = t * n + 1
            ds = divisors(N)
            dm = sum(1 for d in ds if d % t == (t - 1) % t)
            dp = sum(1 for d in ds if d % t == 1 % t)
            bnd = sum(1 for d in ds if d % t == (t - 1) % t and (d <= t - 1 or N // d <= t - 1))
            if P[n] != dm - bnd or Qs[n] != dp:
                bad += 1
    return bad


def split_at_primes(P0, cnt=30):
    from sympy import isprime
    out = []
    n = P0
    while len(out) < cnt:
        n += 1
        if not isprime(n):
            continue
        E = O = B = 0
        for t in range(2, (n + 4) // 4 + 1):
            N = t * n + 1
            ds = divisors(N)
            dm = sum(1 for d in ds if d % t == (t - 1) % t)
            dp = sum(1 for d in ds if d % t == 1 % t) - 2  # drop trivial divisors 1, N
            bnd = sum(1 for d in ds if d % t == t - 1 and (d <= t - 1 or N // d <= t - 1))
            E += (dm + dp) / 2
            O += (dm - dp) / 2
            B += bnd
        out.append((n, E, O, B, E + O - B))
    return out


if __name__ == "__main__":
    for t in range(2, 7):
        print("kronecker t=%d |lhs-rhs| = %.2e" % (t, kron_numeric(t)))
    print("Thm K coefficient check t<=%d n<=%d: failures =" % (T, M), check_K(T, M))
    if P0 > 0:
        rows = split_at_primes(P0, 20)
        import statistics
        print("primes near %d: mean E=%.2f mean O=%.2f mean boundary=%.2f mean R=%.2f" % (
            P0, statistics.mean(r[1] for r in rows), statistics.mean(r[2] for r in rows),
            statistics.mean(r[3] for r in rows), statistics.mean(r[4] for r in rows)))
        print("sd O = %.2f" % statistics.pstdev([r[2] for r in rows]))
