# AGENT REPORT O81 — per-frequency weights below 1 (branch side-agent/weights-below-one)

Deliverable: `EXCEPTIONAL_WEIGHTS.md` (§0 summary table), `scripts/weights_translate_sieve.py`,
`data/weights/translate_sieve.txt`. Not reviewed. No θ > 3/4 claimed.

## Results
1. **Translation invariance (Lemma 1.1, trivial) + LP duality (Lemma 1.2).** Every per-frequency
   bound `Σ_θ w(θ)|ν̂(θ)|` with `w ≥ |W_N|` (smooth window) or `w ≥ |S_N|` (sharp) is ≥
   `M(N) := max_{t∈ℤ} #(𝒜∩(t,t+N])`, the shift-uniform avoider count. The best such bound
   equals `max{⟨g,1_𝒜⟩ : g ≥ 0, |Qĝ| ≤ w}`.
2. **Thm 2.1 (PROVED): general majorants + band-limited window ⇒ door ≍ M(N).** For Selberg's
   majorant window Φ_K (Φ̂ ⊂ [−K,K]), `M(N) ≤ min_ν R_{|W_N|}(ν) ≤ 12(K+1)M(N)`. The dual g is
   band-limited, so a de la Vallée Poussin reproducing kernel plus g ≥ 0 bounds ⟨g,1_𝒜⟩ by
   window counts. Consequence (per family 𝔊, M = M_𝔊; R81 repair, applied by reviewer): a 3/4 cap for this door holds **iff** `M_𝔊(N) ≥ N e^{−C(log N)^{3/4}}`
   (open question (W)). No arithmetic-free argument can cap it; an escape exists iff M(N) is
   below the sieve-limit scale (and then the escaping majorant is the LP optimum, as hard as
   the count).
3. **Thm 3.3 (PROVED): sharp weights (any w with w(0)=N, w ≥ c₀|sin πNθ| off 0), hit-pattern
   majorants, Q₀ = 1, prime slices with |F_ℓ| ≤ ℓ^γ (γ<1/3), boundedly many bad primes, all p_ℓ ≤ 1/4, and the
   uniform mass hypothesis (M) ⇒ saving ≤ C(log N)^{3/4},
   without (H_eq).** (R81 repair, applied by reviewer: for ℛ(ℓ)-slices only for primes ℓ ≥ ℓ₀, since |ℛ(ℓ)|/ℓ > 1/4 at ℓ = 3, 7, 11, 23, 47; the Q₀ > 1 extension is not claimed.) Proof: `|S_N| ≥ sin²(πNθ)` turns `M_S` into `½A_S(1−Πφ_ℓ(N))`; one prime
   ℓ₀ ∤ N gives `1−|φ_{ℓ₀}(N)| ≥ 9/(256|F|²)` (anti-concentration, Lemma 3.2); the loss |F|² is
   absorbed into modified Walsh weights `s_ℓ = log(ℓ/(2|F_ℓ|³))`.
4. **Smooth windows, hit-pattern (§4):** (H_eq) ⇐ characteristic-function bound (Lemma 4.1);
   proved for a single prime ≥ 2|F|N/c (Lemma 4.2, loss √|F|). Several primes: still
   CONJECTURE.
5. **Sharp weights, general majorants (§6):** only ≥ M(N) known. (An earlier "window sieve
   limit (W′)" route was shown redundant by the self-review: LP₁(h/N) ≤ M(N) via ν ≡ M(N)/N.)
6. **M(N) itself (§5):** #(𝒜_X∩[1,N]) ≤ M_{𝔊_X}(N) ≤ N e^{−c(log N)^{3/4}} and E_pr(N) ≤ K + y + M_{𝔊_X}(N) (R81 repair, applied by reviewer: "E(N) ≤ M(N)" withdrawn); random-translate and greedy lower
   bounds are far below. Toy numerics (EVIDENCE, §5.1, N=300/1000): local-search M(N) savings 2.4/3.0 vs
   large-sieve bound 0.7/0.9 vs random translates 12.5/15.9 — consistent with (W), no exponent info.

## What remains (exact)
* (W) `min_{𝔊∈𝔉_A} M_𝔊(N) ≥ N e^{−C(log N)^{3/4}}` over the class 𝔉_A of forced-class families with moduli ≤ N^A (R81 repair, applied by reviewer: M depends on the family; per family it is (W_𝔊)) — closes ALL per-frequency doors
  (every weight, every majorant class). Its negation gives a (non-constructive) escape.
* (H_eq) for several primes (hit-pattern + smooth windows).
* Sharp weights + general majorants: is the best bound ≍ M(N), or w ≥ 1-type capped? (W) closes it.

## Self-check notes for the reviewer
* Thm 3.3 relies on NC Prop 2.1/Thm 2.3 only through the tail estimate; the weight change
  `s_ℓ = log(ℓ/(2|F|³))` must keep NC Cor 2.5's Φ̄ computation (checked in the proof sketch,
  worth re-deriving). The Erdős–Turán/Vaaler claim is hedged (weights not checked to dominate
  c₀|sin πNθ|).
* Thm 2.1 constants: |v| ≤ 5δ min(1,(πδx)^{−2}), block sum ≤ 12δM(L).

## Self-review (reviewer subagent, deep) — applied
No FATAL. MAJOR: (i) §6's (W′) was redundant (LP₁(h/N) ≤ M(N)) — removed, now Remark 6.1;
(ii) summary scope of Thm 3.3 omitted (M) and w(0)=N — fixed. MINOR: ceilings in Lemmas 4.1/4.2,
Ψ̌(−θ), duality attainment (w(0)>0), fixed K in Cor 2.2, moduli reduction restricted to prime
slices — all fixed. Passed: Thm 2.1 (constants), Lemmas 3.1–3.2, Thm 3.3 tail transfer, Prop 5.1.
