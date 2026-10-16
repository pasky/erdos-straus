# z22_primorial_windows — K divisible by all primes ≤ y: what a (log p)^{O(1)} cap would need (O250; CAP_BOUNDED §4)

**Idea (brief).** Make K_q smooth / divisible by P(y) so that many small generators give small-exponent
representations of the forced −1 (Erdős–Rényi / Cauchy–Davenport / sum-product).
**Screen.** (1) Fixed generator set: at p ≡ 1 (mod 4P(y)) every generator ≤ y is a QR mod p, so by the parity law
(CAP_BOUNDED Cor 1.2) no certificate supported on them (δ_p = 0) exists at any window/cap (R-O250 review fix: the
box is not finite, valuations are unbounded; the obstruction is Jacobi, not finiteness). (2) Moving windows with K ≡ 0 (mod P(y)): box ≥ (C+3)^{π(y)−1} vs
q ≍ e^{O(y)} (if q is that large) needs C ≳ y^{O(1)} = (log q)^{O(1)}; a deterministic covering step (Lemma 4.1) would
need Diophantine-generic discrete logs mod q − 1 (resonances at χ(s) = ±1) — not a Frobenius statement; no GRH route
seen (Assessment; cf. z12_grh_lattice_gap, itself tentative). Cauchy–Davenport gives only a factor ω(K) over the one-prime witness.
**Label.** Assessment; Lemma 4.1 PROVED (standard). Missing input stated precisely.
