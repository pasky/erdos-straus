# Hostile review: EXCEPTIONAL_LARGESIEVE.md (branch `side-agent/largesieve-limit` @ 198527f)

Reviewer branch `side-agent/review-largesieve`. Files brought in with
`git checkout 198527f -- EXCEPTIONAL_LARGESIEVE.md reviews/agent-reports/AGENT_REPORT_O17.md scripts`.
Context read: KARY2 Thm 5.1/5.2, Cor 6.1, §6 "not transferred"; ET §1,
Remark 2.6, Cor 3.4; NONCRT §§2.4, 8; `paper/vaughan-loglog-note.tex` §5
(its large-sieve use); `paper/es-threequarter-note.tex` §9 (Montgomery's
statement).

**Overall verdict: SOUND.** I found no error that breaks a PROVED claim.
Theorem 3.1 really does close the "large sieve beyond prime slices"
exclusion of KARY2 §6 / ET §6.1 for frequencies of polynomial level. It
inherits the status of KARY2 Thm 5.1 (internal-reviewed; Case A uses ElT
Prop 1.4). The defects below are about scope, wording and labels. None of
them is fatal. D1 and D3 should be fixed before the result enters the ledger.

## Numerics

* `scripts/ls_duality_check.py` rerun (≤2 cores, `ulimit -v 8000000`):
  all four checks pass and match §8 (`max|F*m−1| = 1.22e−14`,
  `max|F*−S| = 4.8e−14`, Ex 5.2 values 1.166667/1.181818, Thm 4.1 ratios
  < 1). It runs in about 2 s, not 10 s.
* Independent `reviews/exceptional-largesieve-review-check.py` (EVIDENCE):
  * (a) Cor 2.2 on **genuine** Montgomery–Vaughan systems,
    `w = 1/(N−1+Q²)`, with the LS operator norm checked to be ≤ 1. In
    every case the dual optimiser `g*` gives `ν* = |g*|² ≥ 0` on ℤ/M'
    and `≥ 1` on 𝒜, `Eν* = Σ|γ|²`, `F*·m = 1`, and `1/F* ≥ N·Eν*`.
    The last inequality is very loose when `Q² ≫ N`, as expected.
  * (b) Thm 4.1's final inequality `F_w(π) ≤ (𝓡/N)^{1/(1+β)}`, on genuine
    LS systems.
  * (c) Thm 6.2 against the QP optimum `D*` for Gallagher kernels on
    small mixtures that include prime-power and composite classes.

## Per-item verdicts

### Thm 2.1 / Cor 2.2 (duality): SOUND
* (≥): since π is real, `Σπ g = Σγ conj(π̂)`, and Cauchy–Schwarz with
  weights `w` gives the bound. Correct.
* (≤): `P(𝒜)` is a finite simplex and the unit ball of `ℂ^{Θ_ℚ}` is
  compact convex. φ is ℝ-bilinear and continuous. Von Neumann/Sion
  applies. The minimum over the simplex of a linear functional sits at a
  vertex, which gives `min_{n∈𝒜} Re h_c(n)`. I checked signs and
  conjugations: `g = conj(h_{c*})/√F*` has `Re g = Re h/√F* ≥ 1`. The
  minimax is overkill (the Hilbert projection theorem would do), but it
  is correct.
* Fact 1.1 (`a_n = e(−nθ)`): `w_θ ≤ 1/N`. It needs (LS) on only one
  interval of length N. Correct.
* `|g*|²` is a real combination of class indicators with moduli dividing
  `lcm(den θ, den θ')`. It is ≥ 0 on ℤ and ≥ 1 on all of 𝒜 (not just
  mod M', since 𝒜 is a union of classes mod M'). Parseval gives
  `Eν* = Σ|γ|²`. Correct.
* **Is the large sieve as actually used in this class?** Yes.
  * Montgomery's statement (es-threequarter §9; vaughan note (LS)) is
    `|𝒩| ≤ (Y+Q²)/S(Q)`. It is the Farey inequality with
    `w = (Y+Q²)^{−1}`, plus Montgomery's lemma
    `Σ*_a|π̂(a/q)|² ≥ h(q)` for squarefree `q | ΠP`, with the other q
    dropped. Montgomery's lemma uses only that the support avoids `Ω(p)`
    mod `p | q`, so `L = S(Q)/(Y+Q²) ≤ F_w(π)` for every `π ∈ P(𝒜)`.
    This is CRT-admissible.
  * The same holds for MV's `N−1+δ^{−1}` and for the weighted
    `(N+(3/2)δ_θ^{−1})^{−1}` forms. Fact 1.1 makes the specific weights
    irrelevant.
  * The *dual* form `Σ_{n∈I}|Σ_θ b_θ e(nθ)|² ≤ (N+δ^{−1})Σ|b|²` used as a
    Selberg-type majorant is literally the right-hand side of Thm 2.1.
  * The multiplicative (character) large sieve is covered too, though
    the file never says so (D1).

### Thm 3.1 / Cor 3.2 (cap for mixtures): SOUND, conditional on KARY2 Thm 5.1
* **Level.** A term of `ν_c` with modulus `d | lcm(den θ, den θ')`
  becomes a term with modulus `Q₀d` after `n = c + Q₀m`. Its W-rough
  level is at most `λ(Q₀) + λ(θ) + λ(θ')` (each prime counted once, as
  in KARY2). KARY2 Thm 5.1 uses the level only per term: d-locality in
  blocks, at most one prime in the linear block, nothing above `e^λ`.
  So `λ = λ(Q₀) + 2λ_Θ` is the right input.
* **W-smooth parts** of ν's moduli are unbounded here (Farey `q = 2^k`,
  the smooth part of Q₀). KARY2 Thm 5.1 allows this as stated: its
  level counts only `ℓ > W`. Mechanically, either project ν onto
  `gcd(·, M₀)` as in KARY2 Cor 6.1, or lift the base `R_W^□`: unit
  squares mod `p^e` have density `(p−1)/2p` (p odd) or `1/8`
  (`p = 2`, `e ≥ 3`) at every exponent, so the R-term stays ≤ 2W.
  Either way it is fine, but the file should say so (D4).
* **No rounding term.** Correct, and this is the key point. Fact 1.1
  supplies N directly, so no coarsening (ET Lemma 2.9) and no
  `Σ|a_i| < N` are needed, unlike KARY2 Cor 6.1.
* **Fibre assembly.**
  * `1/L_c ≥ N_c Eν_c ≥ ⌊N/Q₀⌋Eν_c`, with `ν_c ≡ 1` for trivial fibres
    and `≡ 0` for empty ones.
  * `Eν = Q₀^{−1}Σ_c Eν_c`.
  * `Q₀⌊N/Q₀⌋ ≥ N/2`.
  * A fibre bound that uses fewer classes (a superset of `𝒜_c`) is
    still admissible, since `P(𝒜_c) ⊂ P(𝒜'_c)`.

  All correct.
* **The 2/3 note** (vaughan-loglog §5) fits the theorem:
  * `Q₀ = L_K ≤ N^{2δ}`;
  * Farey with squarefree `s ≤ Y^{1/2}`;
  * the classes `Ω_c(ℓ)` are ℛ(kℓ)-classes (`k ≡ 1`, `ℓ ≡ 3 mod 4`) for
    `ℓ ∈ (X^{1/2}, X]`;
  * `k ≤ δ log N = ℓ^{o(1)}`, so bounded B'. Thm 5.2 then gives
    `C(log N)^{3/4}` without the loglog factor.

  The note's non-reduced fibres ("+K") and its E_pr→E semigroup step lie
  outside the theorem, but they only enlarge the bound (D3).
* Cor 3.2: `λ ≤ 3A log N`. Correct.

### Thm 4.1 / Cor 4.2 / Rem 4.4 (prime slices, any rational frequencies): SOUND
I checked every step.
* `|φ| ≤ g`, `Σ_{a≢0}|φ|² = g` (Parseval: `(ℓf − f²)/(ℓ−f)²`).
* `Σ|φ|^{p'} ≤ g^{2β}·g ≤ 4(f/ℓ)ℓ^{−α}`, using `2β(1−κ) = α` and
  `2^{2β} ≤ 2`.
* Uniqueness of `θ = θ₀ + Σa_ℓ/ℓ` (CRT, `ℓ ∤ Q₀`).
* Hausdorff–Young on ℤ/Q₀ (probability measure on the group, counting
  measure on the dual), `p ∈ [3/2, 2]`.
* `‖f‖_p^{p'} = (Q₀/|R'|)(E_{R'}|X|^p)^{p'/p}`, then the power-mean
  (Jensen) step.
* The Markov step and `E_{R'}e^{Σ} ≤ e^{2E_RΣ}`.
* Hölder with exponents `(1+β)/β, 1+β`; Fact 4.0 (random signs) and
  Fact 1.1.
* Final: `log(N/B) ≤ (β log N + log 𝓡)/(1+β)`.

Rem 4.4 (fibrewise, `Q₀ = 1`, Jensen over `c ∈ R`) and Cor 4.2
(`α = (log N)^{−1/4}`, `Q₀/|R| = P/φ(P)`) are correct. One caveat on ℓ₀
is D5.

### §5.1, Example 5.2: SOUND (one interpretive overreach, D6/D7)
* Ex 5.2(1): given a residue mod `ℓ_j`, at most `ω_j < ℓ'_j` residues mod
  `ℓ'_j` are excluded, and symmetrically. Pairs are disjoint and Q₀ is
  coprime, so `Ω_c(ℓ) = ∅`.
* Ex 5.2(2): `Σ_{d|m}D_d(π) = mΣπ(b)² ≥ m/(m−ω)`. Correct.
* The script's 35/143 analogues confirm both.

### Thm 6.2 / Cor 6.3 (larger sieve): SOUND
* The pair-count identity, `Z ≤ (W−h)/(D−h)`, Lemma 6.1 and
  `D(π) = D_u + X(π)` are all correct.
* Gallagher case:
  * `D* > log N` forces `Q ≥ Ne^{−c₀−X}`;
  * `W − h ≥ Q/4` when `X < (log N)/3`;
  * `e^u/u ≥ e` gives `log(N/B) ≤ X + log 4 + c₀ − 1`.
* Cor 6.3:
  * χ² is convex in π;
  * a uniform lift preserves χ²;
  * `χ²(Unif(ℤ/ℓ∖F)) = g`;
  * units mod `p^v` give `1/(p−1)`;
  * `Σ_v ℓ^{−v} ≤ 2/ℓ`;
  * `log ℓ/ℓ ≪ ℓ^{−1/2}`;
  * the case `X ≥ (log N)/3` is absorbed since saving ≤ log N ≤ 3X.

  Correct. The kernel claim in the summary is right as stated.

### §7 (escape list): mostly SOUND; D4 sharpens (E1), D8 refines (E2).

## Numbered defects

**D1 (moderate; scope of "CRT-admissible").** The class is defined for
(LS) applied to `a_n = 1_A(n)`, with irrational θ discarded by definition.
The file should say this explicitly in three places.
* "Any frequencies" in Thm 4.1, §0 and the report means *any rational
  frequencies*. Irrational points are excluded by definition, not by
  proof. That is harmless, because a CRT lower bound cannot use them, but
  it should be stated.
* Not covered as stated:
  * (LS) applied to twisted sequences `a_n = 1_A(n)ψ(n)` with ψ periodic
    but not fibre-constant;
  * hybrids: large sieve in some fibres, majorant-plus-rounding (KARY2
    Cor 6.1) in others.

  Neither appears in the literature on this problem. Each needs a
  sentence: the second follows by combining Thm 3.1 with KARY2 Cor 6.1
  fibre by fibre, after coarsening the majorant fibres. Otherwise the
  §0/§7 claim "every form … and all variants" is too broad.
* Covered but unstated: the multiplicative large sieve
  `Σ_q (q/φ(q))Σ*_χ|Σa_nχ(n)|²`. By Gauss sums,
  `q Σ_{χ prim}|Σaχ|² ≤ φ(q)Σ*_a|S(a/q)|²` holds for every sequence. So
  any CRT lower bound in character form is also one for the additive
  Farey system, and Thm 3.1 applies. Add this.

**D2 (minor; weighted sequences).**
* The §0 table and AGENT_REPORT list "weighted sequences" under Thm 3.1
  without Rem 2.4's comparability proviso.
* Rem 2.4's example is off: for Λ on primes in `(N/2, N]`,
  `log(a_max/a_min) = O(1/log N)`, not `log 2` (the log 2 comes from
  restricting to (N/2, N]).
* The `log(a_max/a_min)` loss is in any case avoidable. An honest
  method's bound is `≥ a_max·m_w` (it cannot know `Σa²/Σa`), so its
  saving against `N·a_max` is `≤ log(1/Eν)`.

**D3 (minor; the 2/3 note should be verified in the text).** The bottom
line claims Vaughan, PW §4 and the 2/3 note are covered, but the
parameter check is not written out. It should state:
* `Q₀ = L_K ≤ N^{2δ}`, so `Q₀ ≤ N/2`;
* `λ_Θ ≤ ½log N`;
* `Ω_c(ℓ)` consists of ℛ(kℓ)-classes;
* bounded B', hence `C(log N)^{3/4}` by Thm 5.2;
* the "+K" non-reduced fibres and the semigroup E_pr→E transfer only
  enlarge the bound.

PW §4 was not re-read by the author or by me. The claim for it rests on
PW being "Vaughan's argument" (vaughan note, intro).

**D4 (minor; W-smooth parts, plus an available strengthening).**
* Thm 3.1's proof should state that the unbounded W-smooth parts of ν's
  moduli are allowed by KARY2 Thm 5.1 (only `ℓ > W` is charged), via
  projection to `gcd(·, M₀)` or a lift of `R_W^□` at unchanged density.
* Rem 3.3 can be sharpened. Averaging `g*` over every CRT digit not seen
  by 𝒜 kills **every** frequency whose denominator does not divide `M₀`
  (not only those with primes outside `M₀`). So `λ_Θ` may be computed on
  `gcd(den θ, M₀)`. This shrinks (E1) to frequencies whose level inside
  the family modulus is super-polynomial.

**D5 (minor; ℓ₀ in Cor 4.2 / Cor 6.3).** Thm 4.1 needs
`f_ℓ ≤ min(ℓ/2, ℓ^κ)` for **all** `ℓ ∈ 𝒫`. ET Cor 3.4's hypothesis
`ℓ ≥ ℓ₀(C)` was chosen for `f ≤ ℓ/4`. With `κ = (1+C)/2` one needs
`ℓ^{C+o(1)} ≤ ℓ^{(1+C)/2}`, i.e. an enlarged `ℓ₀(C)`. That is legitimate
(it is a hypothesis on the family), but it should be said. Slice primes
below ℓ₀ cannot simply be dropped: that would enlarge 𝒜 and change the
CRT class. They have to be absorbed into Q₀.

**D6 (minor; labels and an interpretive claim).**
* The §0 table cites "Prop 5.1", but no Proposition 5.1 exists (§5.1 is
  prose).
* §6 uses "CRT-admissible kernel bound" without defining it; only the
  optimum `(W−h)/(D*−h)` is defined. Add one line: `L ≤ D(π)` for all
  `π ∈ P(𝒜)`.
* After Ex 5.2, "by ET Lemma 3.8 … the mass that the small-prime-
  conditioned system misses is not lower order" goes beyond what is
  proved. Ex 5.2 shows invisibility for disjoint pairs only. That the
  balanced classes are invisible *en masse* (many moduli sharing ℓ) is
  plausible but unproved. Label it heuristic.

**D7 (minor; Ex 5.2(2) quantitatively).** `F*_w ≥ w(1+g_j)` with
`w = (N+m_j²)^{−1}` beats the trivial bound only if `m_j² < g_j N`, i.e.
`N ≳ m_j³/ω_j`. State this; otherwise "seen by the composite large sieve"
overstates.

**D8 (minor; (E2) conflates two things).** Gallagher's sieve *as used*
needs only `coll_q ≥ 1/ν(q)`. Capping that form needs only *support*
lower bounds `|𝒜 mod ℓ^v| ≥ ℓ^v(1−ε_ℓ)` with
`Σ ε_ℓ log ℓ/ℓ ≪ (log N)^{3/4}`. That is strictly weaker than (H_Gal)
(near-uniform marginals of one law), which is needed only for the
CRT-optimal kernel bound `D*`. Split (E2) into these two, with the
support version as the first target.

**D9 (minor; §8 label).**
* §8 item 2 (`F*_1 = S(Q)` for prime product systems) is a three-line
  theorem, not EVIDENCE. Montgomery's lemma gives ≥. The uniform product
  measure gives equality term by term (`Σ*_a|π̂(a/q)|² = h(q)` for
  squarefree `q | P`, and 0 for the other q).
* The script docstring says "F*_1 >= S(Q)" but asserts equality.
* The replay time is about 2 s, not 10 s.

**D10 (minor; framing).**
* Thm 2.1 is standard convex/Hilbert duality, the classical
  large-sieve/Selberg duality. The file says as much, but the report's
  "PROVED" items should not be read as a novelty claim for 2.1. The new
  content is Fact 1.1 plus feeding the level into KARY2 Thm 5.1.
* As in KARY2, W is absolute but astronomical (log W ≈ 10^{10}). For
  every practical N all W-rough levels vanish and the cap is pure
  asymptotics. Repeat this caveat in §0.

## Recommendation
Accept Thm 2.1/Cor 2.2, Thm 3.1/Cor 3.2, Thm 4.1/Cor 4.2/Rem 4.4,
Ex 5.2 and Thm 6.2/Cor 6.3 as PROVED (internal), with the Thm 3.1 status
"conditional on KARY2 Thm 5.1; Case A via ElT Prop 1.4". Apply D1–D10,
mainly wording. Once D1 and D3 are in, the ledger can replace the KARY2 §6
item "the large sieve beyond prime slices" with (E1) (sharpened by D4) and
(E2) (split by D8). The "Not covered: the large sieve beyond prime slices"
clause in `paper/es-threequarter-note.tex` §9 Remark and in KARY2 §6 would
then need updating, but not before this review is resolved.
