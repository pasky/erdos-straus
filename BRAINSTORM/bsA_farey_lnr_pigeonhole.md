# bsA_farey_lnr_pigeonhole — the Farey least non-residue λ(p): unconditional bounds and the gap to 3 (O174)

## Idea
DEDEKIND_ES Cor 4.6: for p ≡ 1 (8), five-slice ES(p) ⟺ λ(p) ≤ 3, where λ(p) = min{r(p/A) : (A/p) = −1} and r is
the Hirzebruch–Jung (HJ) length. The classical least non-residue n_p has n_p ≪ p^{0.152} unconditionally and
≤ 2 ln²p under GRH. Question: what can be proved about λ(p) itself? A deterministic, T1-safe mechanism (pigeonhole
against |QNR| = (p−1)/2, which is false at squares) is available. How far does it reach?

**Lemma 1 (PROVED, elementary).** For q < p prime, r(p/q) ≤ q. Hence λ(p) ≤ n_p.
*Proof.* One HJ step gives r(p/q) = 1 + r(q/c) with c = ⌈p/q⌉q − p ∈ [1, q−1]. Every fraction with numerator q has
HJ length ≤ q − 1, the maximum being q/(q−1) = [[2,…,2]]. ∎

**Lemma 2 (PROVED; numerically exact for p = 101, 997, 1009, all A).** For gcd(A,n) = 1, 0 < A < n:
r(n/A) + r(n/(n−A)) = Σ_{i≥0} a_i(n/A), the total of the regular partial quotients (Stern–Brocot depth).
*Proof.* With n/A = [a₀; a₁, …, a_k], a_k ≥ 2, the HJ string is a₀+1, 2^{a₁−1}, a₂+2, 2^{a₃−1}, … (last entry +1).
Its length is 1 + Σ_{odd} a_i if k is even and Σ_{odd} a_i if k is odd. The partner n/(n−A) has the regular CF
[1; a₀−1, a₁, …]. This shifts the parity of the indices, so its HJ length is the complementary sum. The sum of the two
lengths is Σ_{i≥0} a_i in both parities of k (checked case by case, and numerically). ∎

**Theorem 3 (PROVED relative to Yao–Knuth 1975).** For primes p ≡ 1 (4):
λ(p) ≤ (6/π²) ln²p + O(ln p (ln ln p)²).
*Proof.* Since (−1/p) = 1, A ↦ p − A preserves the QNR set. By Lemma 2, every QNR A has
min(r(p/A), r(p/(p−A))) ≤ S(A)/2, where S(A) = Σ a_i(p/A). Hence λ(p) ≤ (1/2)·avg_{QNR} S ≤ (1/2)·Σ_{A<p} S(A)/((p−1)/2).
Yao–Knuth (PNAS 72 (1975) 4720, abstract verified) give Σ_{A≤p} S(A) = (6/π²) p ln²p + O(p log p (log log p)²). ∎
*Remark.* Under GRH, Lemma 1 and Bach's bound only give λ ≤ 2 ln²p. So the unconditional Farey bound is better
than the GRH archimedean one. If the fixed-denominator law of large numbers for S(A) holds (Rukavishnikova, Math.
Notes 90 (2011); statement NOT verified from the source), the median replaces the mean and
λ(p) ≤ (c + o(1)) ln p ln ln p, with c the median constant. Numerically (`bsA_hjlen.py stats 30000`) the median of
r(p/·) is ≈ 0.72 ln p ln ln p and its mean ≈ 0.38 ln²p, decreasing slowly towards 3/π² ≈ 0.30.

## Literature
Yao–Knuth (above). Rukavishnikova (above, unverified). Hensley, *Continued Fractions* (2006), ch. 4 (fixed-denominator
CF statistics; from memory). Moshchevitin–Shkredov, Pacific J. Math 309 (2020), arXiv:1911.07487 (modular Zaremba:
bounded quotients for a multiple q of p, *not* for denominator p; no QNR/coset version found). No paper found that
measures the least non-residue in a CF/Farey metric (research subagent, negative search).

## Barrier screen
* **B3 (scale)** is the whole story. Pigeonhole needs a ball with > (p−1)/2 elements, i.e. radius R ≍ ln p ln ln p.
  ES needs radius 3, where |L_{≤3}(p)| ≍ log²p on average. At radius R = O(1), the ball has (log p)^{O(1)} elements.
  Any polylog-size set can lie inside QR_p (SYNTHESIS_SPARKS §3), so counting cannot reach radius O(1).
* **T1** is respected: the argument uses |QNR| = |QR|, which fails at n = m² (QNR set empty).
* B1/B2/B6 are not triggered at large R. At R = 3, the ball is the B2 divisor event (★).
* Profile (EVIDENCE, `bsA_profile.py 20000 23000`, 72 primes p ≡ 1 (8)): mean number of words and QNR fraction by length
  r = 2..9: (13, 0.48), (54, 0.70), (192, 0.69), (322, 0.41), (567, 0.51), (725, 0.54), (990, 0.54), (965, 0.48).
  The biases at r = 3, 4, 5 are the mod-8 cell laws of Cor 4.1, weighted by the word densities. They are not
  pointwise forcing.

## Cheap numerics
`scripts/bsA_hjlen.py` (HJ length via regular CF, validated against the direct HJ algorithm for all n < 400;
`stats` mode), `scripts/bsA_profile.py`. λ(p) ∈ {2, 3} for all p ≡ 1 (8), 10³ < p < 3·10⁴ (consistent with DK).

## Assessment
PROVED: Lemmas 1–2 and Theorem 3. These are new as stated, but elementary. Theorem 3 is the first unconditional
polylog bound on the "Farey least non-residue", and it beats the GRH conversion of n_p. **It has no ES content:** the
gap from radius ≍ ln²p (or ln p ln ln p) down to 3 is exactly the B3 scale gap, and no growing radius R(p) → ∞
corresponds to an Egyptian-fraction statement (the divisor form tp+1 = mm″, m ≡ m″ ≡ −1 (t) is *exactly*
length 3; HJ_DEEP §1). Promise 1/5 as a route. The quantity λ(p) is a clean new invariant, worth one remark.
