# Z64_SDEEP — conjecture (S) as a character-value problem (wave z64, lane SDEEP)

**ES is OPEN; nothing here proves or disproves ES, (MS), SQ₅ or (S).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Scripts `scripts/z64_sdeep_*`, data
`data/z64/sdeep/`. Brief: `z52bbriefs/z64_lanes.md` §SDEEP (+ z58 common rules, z53 depth brief).

*Status: CHECKPOINT 1 (statement, falsifier table, first lemma, pre-registered kill tests KS0–KS2 registered before
any lane computation).*

Notation (HJ_DEEP, DEDEKIND_ES (DK), FOREST_*). n ≡ 1 (mod 4); a *word* of n is (t,u,v) ∈ ℤ³_{≥2} with
tuv − u − v = n; A = tu − 1, A* = tv − 1, AA* = tn + 1, n/A = [[v,t,u]]; L₃(n) = {A}; χ_n(x) = (x/n) (Jacobi).
N₋(n), N₊(n) = numbers of words with χ_n(A) = −1, +1 (ordered words; reversal u ↔ v is a free involution at primes).

## 0. Mandatory falsifier table (for (S) itself and for the mechanisms of §3; re-stated at the end)

| screen | (S) / mechanism behaviour | where non-squareness / primality enters |
|---|---|---|
| **F1 odd squares** | χ_{m²} ≡ 1, so N₋(m²) = 0 for every odd m (T1, DK Prop 3.1); (S) excludes squares by hypothesis. Every mechanism below is a statement about N₋ or its sub-counts, all of which vanish at m²; a parity law (KS1) must therefore give "even" at squares. | only in χ_n ≢ 1 (n non-square), nowhere else. |
| **F2 C-even / numerator 8** | (S) uses all 15 Jacobi −1 cells (five slices 4 ∣ t,u,v,A,A*), not the (★) line or its C-even half; (S) holds at the 12 R₈-zero primes near 10¹⁰ (explicit words, Z63_EUCLID §7). A mechanism restricted to one slice must be screened on that slice's zero list; KS1 tests per-slice sub-counts separately. | — (no C-parity input). |
| **F3 composites** | (S) is conjectured for *all* non-square n ≡ 1 (4): no counterexample < 10⁹ (HJ_DEEP EVIDENCE 3.1 + R174); 284/285 (★)-zero composites have explicit −1 words, 105 is vacuous (L₃(105) = ∅). KS0 searches adversarial composites (d·m², near-squares) beyond 10⁹. | not needed for (S) (Assessment); needed for (W) only. |
| **F4 known zeros** | (S) holds at the 14 (★)-zero primes and the 38 𝔊*-zero primes (≤ 10⁹ census). KS1's laws are fitted on all primes p ≡ 1 (8) and must hold there too. | — |

## 1. Precise statements

* **(S) (CONJECTURE; HJ_DEEP §3).** For every non-square n ≡ 1 (mod 4) with L₃(n) ≠ ∅ there is a word with
  χ_n(A) = −1. At primes p ≡ 1 (4), p > 5: (S)(p) ⟹ ES(p) (DK Thm 4.5); L₃(p) ≠ ∅ is automatic (bsG_primes_trivial).
* **Sign dictionary (PROVED, prior work).** χ_n(A) = χ_n(uv) (A ≡ u·v⁻¹ mod n); = (−u/A) = (−t/A) for odd A
  (n ≡ −u mod A, reciprocity) — an n-free 2-adic function of (t,u); = −1 iff 4 divides one of t,u,v,A,A*
  (DK Thm 4.5; FOREST_CONNECTIVITY Thm 2.1; FOREST_DEEP_FABLE Thm A/B).
* **Target of this lane.** The brief's form Σ_{A∈L₃(n)} (1 − χ_n(A)) > 0: find structure on L₃(n) that a character can
  see, and push to (a) a theorem on an explicit infinite (non-congruence) family of primes, (b) a threshold under a
  named hypothesis, (c) a counterexample, or (d) a precise missing lemma.
* **Why not already closed.** Closed (do not redo): fixed finite slice menus (B2 Thm 2.2(iii), Lemma 3.2),
  sign-reversing injections (HJ_DEEP C5), constant parity laws of sub-counts (DK C5: 820 sub-counts; Z62_PARITY),
  forest connectivity mechanisms "1 reaches a QNR", "r reaches a QR", "1 ~ r" (FOREST_CONNECTIVITY, all fail on
  explicit sets), QNR-witness mechanisms in the forms of FOREST_INVERSE, linear index arguments on H₁(Γ₀(n); F₂)
  with a fixed known set (Z63_EUCLID Prop E3), fibre-wise character sums (each fibre is one integer's divisor set: B2).
  **Not closed:** (i) *non-constant* parity laws in which the parity of a sub-count of −1 words is a non-abelian
  Chebotarev invariant of p (only constant parities and statistical correlations with Rédei data were tested:
  DK C5, BRAINSTORM/nonab_frobenius_redei); (ii) (S) beyond 10⁹ in adversarial families; (iii) the
  trace/Salié form of the sign (§2) as a completion device.

## 2. First lemma (PROVED, elementary)

**Lemma 1 (the sign is a function of the trace).** Let n be odd and γ = [[a,b],[c,d]] ∈ Γ₀(n) (n ∣ c). If
gcd(tr γ + 2, n) = 1 then (d/n) = ((tr γ + 2)/n); if gcd(tr γ − 2, n) = 1 then (d/n) = ((tr γ − 2)/n).
*Proof.* ad ≡ 1 (mod n), so tr γ ± 2 ≡ d⁻¹ + d ± 2 = (d ± 1)²·d⁻¹ (mod n); take Jacobi symbols. ∎
*Application to words.* γ_w := [[A, t],[n, A*]] ∈ SL₂(ℤ) ∩ Γ₀(n), tr γ_w + 2 = A + A* + 2 = t(u+v). Hence
**χ_n(A) = (t(u+v)/n) = ((t(u+v) − 4)/n)** whenever these are coprime to n (always at primes n > t(u+v), and at
primes generally unless p ∣ t(u+v)). So (S)(n) ⟺ the multiset {t(u+v)} ⊂ ℤ is not contained in ker χ_n; the sign
is the genus character of the SL₂(ℤ)-class of γ_w attached to the factorisation (s+2)(s−2) of its discriminant
s² − 4 (s = tr), evaluated at the represented number n (making precise the BRAINSTORM item Z2825, left open there).
(Numerical check: §4.)

## 3. Mechanisms and PRE-REGISTERED KILL TESTS (registered before any lane computation)

**KS0 — the conjecture itself in adversarial families (counterexample hunt).** Decide (S)(n) exactly (full word
enumeration via a segmented factor sieve of n + u, u ≤ √(n/2); early exit at the first −1 word) for: (a) near-squares
n = m² + k, |k| ≤ 60, n ≡ 1 (4), sampled m up to ~10⁷ (n ≲ 10¹⁴); (b) n = d·m² for small non-square d ≡ 1 (4)
(χ_n = χ_d on words: a *fixed* small character); (c) n ≡ 1 (mod lcm(1..X)) near 10¹²–10¹⁴ (square-mimicking at
small primes, so all small-letter words are absent); (d) the composite R-zeros and Z₇. Record min N₋ and the least
−1-word height per family. **Kill (of (S)):** any non-square n with L₃(n) ≠ ∅ and N₋(n) = 0. **Secondary
(recorded):** if some family shows N₋ ≤ 2 at n > 10¹² that is a structured near-miss to report.

**KS1 — mechanism NAP (non-abelian parity law).** *Mechanism:* a sub-count c(p) of −1 words (counted per reversal
pair) with c(p) ≡ ρ(p) (mod 2) for a non-congruence invariant ρ of p; then c(p) is odd, hence (S)(p), on the
infinite Chebotarev family {ρ = 1} — a non-congruence family, escaping B1/Thm M via hatch "non-abelian Frobenius".
*Test:* all primes p ≡ 1 (mod 8), p ≤ 2·10⁶. Sub-count dictionary 𝒞: N₋/2, N₊/2, |L₃|/2, the per-slice counts
(4∣t; 4∣A or 4∣A*; 4∣u or 4∣v), the 15 −1 cells and 5 +1 cells of (t, {u,v}) mod 4, each also restricted to
t ≤ T (T = 2,3,4,8) and to min(u,v) ≤ U (U = 4, 8, 16) — all counted per reversal pair. Invariant dictionary 𝓡:
(2/p)₄; (−1/p)₈ (= [p ≡ 1 (16)]); (ℓ/p)₄ for ℓ ∈ {3,5,7,11,13} when defined; h(−4p)/4 mod 2 (Barrucand–Cohn);
h(−8p)/4 mod 2; h(−3p) mod 4 bit, h(−4p)/8 mod 2 on its domain; plus products of pairs of these and of the
abelian characters (3/p),(5/p),(7/p),(p mod 16 bits). **Kill (NAP DEAD on this dictionary):** no pair
(c, ρ) ∈ 𝒞 × 𝓡 (incl. products) has c ≡ ρ (or c ≡ ρ + 1) (mod 2) on ≥ 99 % of the primes where ρ is defined, and the
best agreement is within 4σ of what an abelian (p mod 840·16) law explains. **Survive:** some pair has ≥ 99 % →
examine exceptions, test to 10⁷, attempt a proof.

**KS2 — Salié completion of the signed count (theory, decided by proof not computation).** By Lemma 1 the
signed word count is a χ-twisted count of points (A, A*) of the modular hyperbola AA* ≡ 1 (mod n); Salié sums
evaluate the χ-twisted Kloosterman sums exactly (as sums over square roots mod n), turning the *signed* count over a
region into an *unsigned* count on a conic. **Kill:** if the word region is a union of single hyperbolas
AA* = tn + 1 (thickness one point in the t-direction, so Fourier completion costs ≥ the main term at every t),
then the completion only re-expresses each per-t divisor problem (B2/B3) — record as a scoped no-go with the exact
loss. **Survive:** a region of positive thickness whose points provably all are words (or a positive-weight
majorant supported on words) — then compute.

## 4. Computations (to come)

## 5. Results (to come)
