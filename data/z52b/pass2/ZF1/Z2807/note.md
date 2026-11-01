# Z2807 — the "twisted parity" ψ(n) = (n/p): where a Selberg-type barrier exists and where it does not

**(i) Generic sequences: the barrier exists (PROVED, Selberg's construction with λ replaced by ψ).**
Let 𝒜 = integers in an interval I (or any sequence whose sieve data are integers-in-APs counts), |I| = x, p ∤ d.
With weight w(n) = 1 + ψ(n) ≥ 0 (which vanishes exactly on the ψ = −1 terms),
|𝒜_d^w| = Σ_{n∈I, d|n} (1 + ψ(n)) = |𝒜_d| + ψ(d) Σ_{m ∈ I/d} ψ(m) = |𝒜_d|·(1 + O(p^{−δ})) for x/d ≥ p^{1/4+ε} (Burgess,
uniform in the shift). So the weighted sequence has the same density function g(d) and remainders up to level
D = x p^{−1/4−ε}: no sieve using only these axioms at level ≤ D can give a positive lower bound for #{n ∈ 𝒜 : ψ(n) = −1}
(nor, symmetrically with 1 − ψ, for ψ = +1). Numerics (A = [1, p/4]): max_{d≤D} |Σ_{d|n}ψ(n)|/|𝒜_d| = 0.016, 0.073, 0.26, 0.70
at D = 10, 10², 10³, 10⁴ for p = 1 000 081, and 0.004, 0.012, 0.022, 0.097 for p = 10 000 537 — the axioms are matched
while x/d ≳ p^{1/4+ε}, and break where Burgess stops.
(Of course ψ is a congruence condition mod p, so the barrier is only for level < p; ES's natural range is A ≤ p.)

**(ii) On ES words the barrier is void (PROVED in repo + certified check).** For words p = mcs − c − s, A = ms − 1,
the ES sign χ(w) = ψ(A) is a function of (c, m, s) mod 8 (CHI_FLIP Cor 1.2, R198 self-contained proof; DK Cor 4.1).
Hence on the word set 1 + ψ(A) = 2·1[w ∈ (+1)-cells mod 8]: killing the ψ = −1 terms changes the counts in classes
mod 8, i.e. violates the sieve axioms at modulus 8. Check (scripts/z52d_p2_ZF1_Z2807_twisted_parity.py): 32 898 words
at primes p ≡ 1 (8) in [10⁵, 1.2·10⁵], 80 cells seen, 60 with sign −1 (= DK's 15/20), 0 violations of cell constancy.
For the (★) line (E_a⁴) there is no sign layer at all (PARITY_AUDIT §0).

**Conclusion.** The twisted parity is a genuine Selberg-type barrier only for sieves over sequences on which ψ is
non-local; ES's sign is 2-adically local along words, so the ES obstruction is the class/size (B2) layer, in line with
PARITY_FIXED_P Assessment 2.2 ("parity is not the binding constraint") and PARITY_AUDIT §0. Liouville parity of solutions
is unbiased (PARITY_FIXED_P §2 EVIDENCE; Z2603 here for slices).
