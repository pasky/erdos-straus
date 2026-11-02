# z54 EXACTSUM literature check (research subagent, sources opened; summary)

1. Bourgain, "Decoupling, exponential sums and the Riemann zeta function", JAMS 30 (2017) 205-224, arXiv:1408.5794:
   **Theorem 6**: "(ε + 13/84, ε + 55/84) is an exponent pair." (VERIFIED from arXiv PDF.) Bourgain refers to
   Graham-Kolesnik Ch. 3 for the phase class.
2. (9/56 + ε, 37/56 + ε) is an exponent pair due to **Huxley-Watt**, "Exponential sums and the Riemann zeta function",
   Proc. LMS (3) 57 (1988) 1-24 (VERIFIED via Mueller-Nowak 1989 quotation: "Recently Huxley and Watt [2] have proved,
   that for any ε' > 0, (9/56 + ε', 37/56 + ε') is an exponent pair").
   Huxley, "Exponential sums and the Riemann zeta function V", Proc. LMS 90 (2005) 1-41: "(32/205 + ε, 269/410 + ε) is
   an exponent pair for every ε > 0" (VERIFIED).
3. Definition (Trudgian-Yang arXiv:2306.05599 §1.1, following Graham-Kolesnik): phases whose derivatives are close to
   those of y x^{-σ} (derivative convention), N < x <= 2N; bound sum_{n in I} e(f(n)) << (y/N^σ)^k N^l uniformly for
   I = (a,b] in [N,2N], under y >= N^σ. For f(x) = T/(x+c) with fixed 0 <= c < 1 the derivative closeness holds for N
   large (relative error O(1/N)); scale condition T >= N^2 in this convention (σ = 2). Used in Lemma 4.1 with
   y = hZ/(fq), N = J ~ K/q, y/J^2 ~ hZq/(fK^2) >= 1.
4. Dirichlet divisor problem: 131/416 (Huxley 2003) is the established exponent; arXiv:1709.04340 (Bourgain-Watt,
   517/1648) is withdrawn (gap). (Not used in Z54_EXACTSUM.)
The A^nB(0,1) pairs are classical van der Corput (A, B processes; Graham-Kolesnik Ch. 3), computed exactly in
scripts/z54_exactsum_window.py.
