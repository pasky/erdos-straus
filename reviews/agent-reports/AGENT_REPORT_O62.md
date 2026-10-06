# AGENT REPORT O62 — (H_rough) via damped collisions (checkpoint 1)

Branch `side-agent/hrough`, document `EXCEPTIONAL_LARGESIEVE4.md`,
scripts `scripts/largesieve4_checks.py`, `scripts/largesieve4_toy_es.py`.

## Results (labels as in the document)

1. **Damped-collision reduction (Lemma 1.1, PROVED).** If
   `|σ̂(θ)|^{2β} ≤ Π_{ℓ∈supp θ}w_ℓ` (w_ℓ ≤ 1), then
   `𝓡_{2+2β}(σ) ≤ E_{σ⊗σ}Π_ℓ(1+w_ℓh_ℓ) = E_T𝓡_2(σ_T)` (T random, ℓ ∈ T w.p.
   w_ℓ). The signed Möbius quantity P_S of LS3 §4 is never inverted; only
   a positive two-copy quantity remains.
2. **Tilted pair law (Lemma 2.1, PROVED)** and **(B) is free
   (Prop 4.1, PROVED):** conditioning K2's capped fibre law on the good
   path event `G_B = {no leak} ∩ {Σ_ℓ w_ℓp̃_ℓ ≤ B}` gives damped collision
   `≤ e^{2B}/Q'(G_B)²`; with Markov this needs **first moments only**
   (no large deviations, no comparison-at-level hypothesis).
3. **Theorem 4.2 (PROVED implication):** the all-level large-sieve cap
   for **all** forced mixtures — via the Hölder/H_rough route, *not* LS2's
   (H_LS∞) criterion itself (cap `(log N)^{3/4} + Cγ^{−3}(log N)^{3/4}(log log N)³` for every
   CRT-admissible large sieve at any level) follows from a purely
   qualitative-looking sup decay (A*) of the conditioned fibre laws, at
   **any fixed rate γ** with per-prime losses up to `z^{γ/2}`.
4. **Lemma 5.1 (PROVED):** pinned-coordinate Efron–Stein bound
   `|σ̂(θ)| ≤ Q'(G)^{−1}Π_{ℓ∈S}4U(R_ℓ)/(1−δ_ℓ)` for any *deterministic* set
   R_ℓ containing the ℓ-residues of all classes through ℓ — exact product
   decay, no correlation decay needed.
5. **Theorem 5.2 (PROVED, LS3-Thm-3.1 inputs):** the 3/4 cap at every
   frequency level holds for every mixture whose classes with ≥ 2 primes
   above `z = exp((log N)^{1/4})` are residue-sparse
   (`U(Res_ℓ) ≤ ℓ^{−γ}` at each prime > z); one-rough-prime classes
   arbitrary. Strictly extends LS3 Thm 3.1.
   **Cor 5.3:** in particular for all small-height classes `−r/s`,
   `r, s ≤ z^{1/4}/2`, over all moduli — including LS3 Lemma 4.2's
   `−4 mod M` (all M ≡ 3 (4)), `−1`, `−1/4`, `−4d`, ... So **residue
   concentration is the easy case**, contrary to the LS3 §4.2 worry.

## What is still open (precisely)

(A*) for *residue-dense* multi-rough classes (generic ℛ(M) with many moduli
through a rough ℓ, whose projected residues can fill essentially all of
ℤ/ℓ). Then the deterministic residue set must be replaced by the random
set of classes whose other coordinates are matched, i.e. a covering
probability (§3.2, (CC), probability form). The trivial cover count gives
a per-prime factor `2^{|S|}T_S/ℓ` (T_S = max number of classes per
modulus), useful only for small supports with few classes per modulus,
and even that needs outside-coordinate bookkeeping not yet written;
beyond `log₂ z` primes the union bound over covers overcounts
(structured example in §3.2), and an assignment count controlling
divisors of `(Q+1)/4` over subset products Q ⊆ S is needed. CONJECTURE.

## Self-review (deep reviewer subagent, before handing over)

No FATAL; Lemmas 1.1, 2.1, 3.1, Prop 4.1, Thm 4.2, Lemma 5.1 (incl. prime
powers and the conditioned law), Thm 5.2, Cor 5.3 judged sound; the
reviewer independently checked Lemma 5.1 and Prop 4.1 on 19 capped,
conditioned prime-power examples. Repaired: (M1) the small-support count
had omitted the class choice per modulus (now `2^{|S|}T_S`); (M2) (CC)
restated in probability form (cardinality form wrong for prime powers);
(M3) "H_LS∞" renamed to "all-level cap via H_rough"; minor: Cor 5.3 uses
the projection mod ℓ, unit v in Lemma 3.2, `Q'(G_B) > 0`, (A*) exceptional
event in Thm 5.2 made explicit, "non-squares" remark corrected, J bound
uniformity in γ, script headers.

## Things the reviewer should check hardest

* Prop 4.1: the tilting identity with an inserted path functional, and
  `η ≤ p̃/(1−p̃)` for the capped rule (heavy steps uniform).
* Lemma 5.1: the pinned representation `Q'(x_S = v, G) = E^{(v)}[1_GΠk]`
  and the induction "neither pinned value in R_ℓ ⇒ identical paths,
  Λ-factors, G".
* Theorem 4.2's exceptional-event bookkeeping (leak tail above z,
  Markov for m_c, E₀) and the partial-summation bound for J with
  `α = 2βγ`.
* Cor 5.3's height notion (as a rational −r/s, not TUPLES2's rsm = A form).

Numerics: EVIDENCE only (§6). Replay in the document.
