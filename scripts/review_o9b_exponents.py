"""R34b: from-scratch tally of the OMEGA9 Thm 2.2 budget (all constants 1,
C_H=5), under ET S* = L^4 log L, z = L^2.  Prints each term and its local
log-log slope d log(term)/d log L, to identify the bottleneck."""
import math


def terms(L):
    z = L ** 2
    k = math.floor(L / math.log(z))
    b = math.ceil(math.log2(4) + 2 * L / math.log(2))      # log2(4T^2)
    S = L ** 4 * math.log(L)                                # ET upper bound S*
    logm = (k + 2) * L                                      # m <= T^{k+2}
    k0 = math.ceil(3 * S * math.log2(math.e) + math.log2(400 * (S + 1)) + 2 * logm / math.log(2))
    w = k * b
    d = 4 * 5 * w * k0
    piz = z / math.log(z)
    logQPi = (piz + 64 * k * k * S) * L + 4
    junta = 2 * (3 * k + 2 * d + 1) * L
    return dict(k=k, b=b, w=w, k0=k0, d=d, logQPi=logQPi, junta_dL=junta,
                logZ=logQPi + junta)


for L in (1e3, 1e6, 1e12, 1e24):
    t1, t2 = terms(L), terms(L * 1.01)
    print(f"L=1e{round(math.log10(L))}: " + ", ".join(
        f"{n}={v:.2e}(slope {math.log(t2[n]/v)/math.log(1.01):.2f})" for n, v in t1.items()))
