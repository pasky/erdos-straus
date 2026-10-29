"""z50 ncrt §4: divisor switching.  (a) every word (t,u,v) of n has min(uv, tv-1, tu-1) <= (2n+4)^{2/3};
(b) per-n counts of words whose cheapest modulus is <= T, versus single-grouping counts, averaged over n in a range;
the ratio cheapest/endpoint-grouping stays bounded (<= 3) as T grows.  Usage: python z50_ncrt_switch.py N0 N1"""
import sys, math
N0, N1 = map(int, sys.argv[1:3])
def words(n):
    # (t u - 1)(t v - 1) = t n + 1 ; enumerate t and divisors a = tu-1 <= sqrt(tn+1), a = -1 mod t
    out = []
    t = 1
    while True:
        m = t * n + 1
        found_any = False
        a = t - 1 if t > 1 else 1
        # a ranges over a = -1 (mod t), a >= t-1 (u >= 1), a*a <= m
        a = t - 1 if t >= 2 else 1
        step = t
        if a < 1: a += step
        while a * a <= m:
            if m % a == 0:
                b = m // a
                if (b + 1) % t == 0:
                    u, v = (a + 1) // t, (b + 1) // t
                    if u >= 1 and v >= 1 and t * u * v - u - v == n:
                        out.append((t, u, v))
            a += step
        if t * 1 * 1 * 1 > n + 2 and t > 2 * n + 4: break
        t += 1
        if t > 2 * n + 4: break
    return out
worst = 0.0; Ts = [10, 30, 100, 300, 1000]
cnt_min = {T: 0 for T in Ts}; cnt_end = {T: 0 for T in Ts}; cnt_pair = {T: 0 for T in Ts}
for n in range(N0, N1):
    for (t, u, v) in words(n):
        ms = [u * v, t * v - 1, t * u - 1]
        mn = min(ms)   # modulus 1 (tu-1 = 1) is the trivial class: the free words of tau(n+1), tau(2n+1)
        worst = max(worst, mn / (2 * n + 4) ** (2 / 3))
        for T in Ts:
            if mn <= T: cnt_min[T] += 1
            if min(t * u - 1, t * v - 1) <= T: cnt_end[T] += 1
            if u * v <= T: cnt_pair[T] += 1
K = N1 - N0
print("n in [%d,%d): max over words of min-modulus/(2n+4)^(2/3) = %.4f" % (N0, N1, worst))
for T in Ts:
    print("T=%5d  per-n words: cheapest<=T %.3f | endpoint(either)<=T %.3f | pair<=T %.3f | (log T)^2/2 = %.3f | ratio cheapest/endpoint %.2f"
          % (T, cnt_min[T] / K, cnt_end[T] / K, cnt_pair[T] / K, math.log(T) ** 2 / 2, cnt_min[T] / max(1, cnt_end[T])))
