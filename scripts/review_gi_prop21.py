"""R170: numerical check of GROWING_IDENTITIES Prop 2.1 (tau in {1,q} part of A3 summed over chi of parity
(-1)^k with weight conj(chi(-1))) and of the size comparisons in Prop 2.2.  Uses only review_gi_trace.py.
"""
from math import gcd
from review_gi_trace import trace, characters, divisors, phi


def a3_tau_1q(N, k, q, chi):
    """tau = 1 and tau = q summands of A3 (incl. the -1/2 and min^{k-1})."""
    s = 0
    for d in divisors(N):
        dp = N // d
        s += -0.5 * min(d, dp) ** (k - 1) * (chi[d % q] + chi[dp % q])
    return s


def main():
    for (q, ns) in [(12, [97, 193, 313, 409]), (20, [97, 241, 337]), (24, [73, 97, 193])]:
        for k in (2, 3):
            par = (-1) ** k
            chis = [c for c in characters(q) if abs(c[q - 1] - par) < 1e-9]
            dimG1 = round(sum(trace(1, k, q, c)[0] for c in chis).real)
            for n in ns:
                N = q * n + 1  # N = 1 mod q (c=1, d=q/4 Type II form)
                E = sum((c[q - 1].conjugate()) * a3_tau_1q(N, k, q, c) for c in chis)
                claim = -0.5 * 2 * (phi(q) / 2) * sum(
                    min(d, N // d) ** (k - 1) * ((d % q == q - 1) + par * (d % q == 1)) for d in divisors(N))
                tot = [0, 0, 0, 0]
                for c in chis:
                    _, parts = trace(N, k, q, c)
                    for i in range(4):
                        tot[i] += c[q - 1].conjugate() * parts[i]
                T = sum(tot)
                tauN = len(divisors(N))
                deligne = dimG1 * tauN * N ** ((k - 1) / 2)
                es = sum(min(d, N // d) ** (k - 1) for d in divisors(N) if d % q == q - 1)
                print(f"q={q} k={k} N={N}: E={E.real:.1f} claim={claim:.1f} |A2|={abs(tot[1]):.1f} "
                      f"|A3|={abs(tot[2]):.1f} A4={abs(tot[3]):.1f} |Tr|={abs(T):.2f} dimS_k(G1)={dimG1} "
                      f"Deligne={deligne:.0f} ES-class={es} phi(q)/2*ES={phi(q) / 2 * es:.0f}")


if __name__ == "__main__":
    main()
