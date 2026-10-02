# AGENT_REPORT_A2 — exceptional-set exponent beyond 3/4 (task a2)

Branch: `side-agent/theta-beyond-34`. Main deliverable: `EXCEPTIONAL_THETA.md`.

## Outcome

**(B): no improvement on θ = 3/4 is proved.** An obstruction is established
within the stated architecture.

The core is a new rigorous "sieve-limit" theorem. It converts the
mass-and-budget heuristic of the 3/4 note's ceiling section, `θ = B/(B+1)`,
into a proved statement for a precisely scoped class of architectures. It
also makes rigorous, for avoid-events of product systems, the LP-duality
statement that notes Assessment 75.7 called missing.

Labels: PROVED means internal proof only, with novelty unchecked. It may be
folklore in spirit; no source was found.

## Main results

### Theorem 2.5 (sieve limit for prime-slice CRT systems; PROVED)

Setting: conditions are independent across large primes ℓ once a small
residue c is fixed. Let ν be any nonnegative majorant of the avoider set,
built from congruence classes whose slice primes have total log at most λ.
The hypotheses are:
* every forbidden density satisfies `p_ℓ(c) ≤ 1/4` for `ℓ ≤ e^λ`;
* every admissible fibre has avoiders (`p_ℓ(c) < 1`);
* ν ≥ 0 on all of ℤ.

Then

    log(1/Eν) ≤ log(Q₀/|R|) + 19αλ + C₄ Σ_ℓ p̄_ℓ ℓ^{−α} + O(log²λ)   for every α > 0.

The term `log(Q₀/|R|)` is a saving the theorem leaves uncontrolled. It is
negligible for selector-type admissible sets.

The proof has three parts:
1. **Thinning:** `x = u∘w`.
2. **Band symmetrisation:** this reduces f to a polynomial in band counts,
   with multidegree in a weighted lower set.
3. **Interpolation:** the combination technique on lower sets, plus a
   binomial Lagrange-node lemma. The node lemma comes with explicit
   constants and is checked numerically.

### Theorem 2.7 (sequential windows; PROVED)

This extends Theorem 2.5 to systems where large primes are shared between
the multiplier parts of some conditions and the slice primes of others.
Prime powers are allowed in the non-terminal positions. The hypotheses are:
* (U): each condition has a unique prime, to exponent one, in its last
  window;
* the density bounds `p ≤ 1/4` and `p < 1` along the sequential law
  `Q_seq`.

The bound uses the inflated sequential profile (Lemma 2.8), and the level
term is charged once per window.

### Corollaries 3.4 and 3.6 (PROVED)

Consider any family of Case-B forced classes, in either grouping
(multiplier classes −4D mod M, or a-frame classes −(4D+a) mod 4a·g(D)).
Suppose every modulus has a dominant prime `P(M) ≥ M^{1/(1+C)}` for some
C < 1. Then:
* every nonnegative level-`N^A` CRT majorant (Bonferroni, Brun, Selberg,
  anything) saves at most `C(A,C)(log N)^{3/4} + O_C(1)`;
* for slice systems (Cor 3.4) the same holds for the Montgomery large
  sieve, summed over fibres.

This assumes the final bound has the form `N·Eν + (nonnegative rounding
bound)`. A method exploiting signed cancellation in the rounding errors is
outside the scope.

So **3/4 is sharp and no `(log log N)^ε` gain is possible** in this class.
The class contains Vaughan, PW, the 2/3-loglog note and the 3/4 note. The
profile input is Lemma 3.1, `Σ τ(A²)M/φ(M) ≪ x log²x`, proved via Shiu.

### Exact accounting (Lemmas 4.1–4.4; PROVED)

* In both campaign proofs the binding inequality is the pair
  (supply profile, level).
* Bonferroni depth (`r ≥ μ−2√μ` is forced), the BV level (EH changes
  constants only) and the selector are not binding.
* The 2/3-loglog note is sharp for its architecture: `h(𝒦) ≪ log log L_𝒦`
  with `L_𝒦 ≤ N` (Cor 3.5).

### Levers (table in §5.0)

* **Closed:** cost per condition / mass weighting; beyond-identity supply
  (the exact criterion `−1∈Rat_a` *is* the a-frame forced-class family,
  Lemma 3.2); both Case-B groupings; Bonferroni→Selberg; the ET first
  moment (consistent with B = 3).
* **Case A:** closed only conditionally, on the weighted divisor bound
  **H_A3**. Its unweighted form is numerically supported, but not proved.
* **Halász / multiplicative:** a non-multiplicativity counterexample is
  PROVED. The joint route is a model Assessment only (entropy θ* ≈ 0.52).
  It is *not* closed.
* **Open door:** H_MS for **balanced moduli** (no dominant prime), and
  multipliers far beyond the slice prime. By unweighted Dickman, the
  balanced moduli are about `1−log 2` of moduli; their share of the
  weighted supply is unproved. A concrete next
  step is in §5.6: the same-scale pair-condition toy LP.

## Evidence (numerical, labelled)

* **H_EM, complete-system void among real primes.** Tested on all
  4,045,501,204 primes in `[10¹², 10¹²+1.12·10¹¹)`. The ratio
  `−log P(void)/mass` falls from 1.39 to about 0.80 for Q ≤ 4000. There is
  no super-cubic effective mass; the classes clump.
* **Exchangeable LP.** In the tested cases, the floating-point LP optimum
  agrees with the Selberg square-majorant value to within 0.01 in −log.
  This is uncertified.
* **Reduction steps of Prop 2.4.** Brute-force LP on 40 random
  non-exchangeable instances; 0 violations.
* **Node lemma.** 99 cases; 0 violations.

## Self-review

A deep reviewer subagent ran on the first draft (verdict: "substantial
repairs needed"). All findings were applied:
* nonempty-fibre hypothesis added to Thm 2.5;
* the R-term made explicit as an uncontrolled saving;
* the universal two-sided Ψ claim removed (Ψ is one-sided in general);
* Cor 3.4 restricted to slice-only conditions with a selector admissible
  set;
* coprimality added to the Lemma 3.2 converse (counterexample p=5, q=15,
  D=25);
* Case A made conditional on a *weighted* H_A3;
* Halász downgraded to Assessment;
* the false lcm lower bound deleted;
* `log⁺` added in Lemma 4.1;
* the Christoffel wording corrected (square majorants only; counterexample
  `(k−1)(k−2)/2` for Poisson(1/2));
* the script issues fixed.

A second deep review covered Theorem 2.7 and Cor 3.6. It found the
induction sound, and all of its findings were applied:
* prime powers added to the setting;
* the conditioning on R repaired via "n = 1 lies in no forced class";
* the Shiu large-divisor tail added;
* the remaining two-sided Ψ claim removed;
* the H_MS statements corrected (Theorem 2.7 does not prove H_MS);
* the Dickman share marked as unweighted;
* the large-sieve claim restricted to slice systems;
* the report's wording fixed.

The repaired versions were not re-reviewed.

## Files

* `EXCEPTIONAL_THETA.md`
* `scripts/theta_sieve_limit.py`
* `scripts/theta_reduction_check.py`
* `scripts/theta_profile.py`
* `scripts/theta_void_primes.cpp`
* `data/theta/{profile.txt, void_primes_Q4000.txt}`
* Replay commands: §7 of the md.

Nothing was touched in `main`, `notes.md` or the sibling repos. No ledger
edits were made; suggested `DISCOVERIES.md` entries are for the parent to
decide:
* (D) new: Thm 2.5, Thm 2.7, Cor 3.4/3.6 (walls with exact scope);
* (E) new: H_MS, H_A3, H_EM.

Stopping here for parent review.

---

# Checkpoint 2 — follow-up on the open door (§5.6)

New material is in new subsections: §3.7, §3.8, §5.7 and §5.8. §§2–4
received repairs only (stale text, cross-references).

## (iii) H_A3 / Case A — settled (Lemma 3.7)

Lemma 3.7 proves

    Σ_{rh≤x} τ(4rh²+1)·rh/φ(rh) ≪ x log²x,

with the γ-weighted variant too. It follows from Elsholtz–Tao
Proposition 1.4, `Σ_{a≤A,b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)` for
`k ≪ (AB)^{O(1)}`. This is exactly their eq. (8.2), with a = h, d = r.

So Cor 3.4/3.6 now cover Case-A classes, with dominant prime in `G = 4rh`.

**Caveat:** ET Prop. 1.4 is used as an external published theorem and was
not re-proved.

## (ii) Weighted share of balanced moduli — positive proportion (Lemma 3.8)

Lemma 3.8 proves `Σ_{M≤x, P(M)≤√M} |ℛ(M)|/M ≫ (log x)³`. The
construction is `M = kℓ₁ℓ₂` with `ℓ₁, ℓ₂` at the same scale (log-ratio
≤ 1+η) and `log k ≍ η log Y`. The proof uses Bombieri–Vinogradov plus the
3/4 note's lattice lemma.

**Numerics (EVIDENCE).** The weighted share is 0.098, 0.121, 0.141, 0.157
and 0.171 at x = 10³, …, 10⁷. It runs slightly above the unweighted
log-density and is still creeping toward the Dickman value
`1 − log 2 = 0.307`.

So the open door carries a positive proportion of the cubic mass.

## (i) Balanced-modulus extension — partial

**Theorem 5.5 (PROVED, general).** For *any* CRT condition system, with no
slice or dominant-prime structure, every Λ²-majorant g² (g of level λ/2,
g ≥ 1 on A) has

    saving ≤ αλ/2 + Ξ_A(α),   Ξ_A = log P(A∩A'_α)/P(A)².

Here A' is the avoider of an ℓ^{−α}-noise-correlated copy. The proof is
via Efron–Stein and the noise operator.

**What follows from it:**
* for slice systems it recovers the Rankin functional (Cor 5.6);
* Prop. 5.7 gives an exact derivative formula for Ξ.

So the balanced door, *for Λ²-majorants*, reduces to a concrete
noise-stability bound: H_MS^{Sel}, `Ξ_A ≪ α^{−3}polylog`. That would give
the cap `λ^{3/4}polylog`.

**Assessment 5.8 (heuristic).**
* The diagonal term reproduces the H_MS functional with full-modulus cost.
* Off-diagonal "star" terms look subdominant (about α^{−2}). This rests on a
  first-moment surrogate measured only on dominant-prime moduli
  (`theta_deadly_values.py`).
* Missing ingredients:
  * a correlation inequality under the jointly conditioned law (Harris
    works in an independent-indicator model, but CRT is one-hot);
  * a lower bound on J;
  * lower-support and overlapping-rest terms;
  * the small-prime fibre term.

**No proof of H_MS for general majorants.**

**Why the window method of Theorem 2.7 does not extend (Assessment):**
same-scale pairs carry cubic mass, so wide windows pay those pairs in full,
and narrow windows multiply the level charge.

**Toy LP (§5.8; EVIDENCE, uncertified floating point).** At matched mass
and level, random pair systems save less than single-coordinate systems in
every sampled instance. No instance of balanced conditions beating the
single-slice behaviour was found. Toy sizes cannot probe the asymptotics.

## Status of the open door

* Balanced moduli: open for general majorants. For Λ² they are reduced to
  H_MS^{Sel}. Every piece of evidence (toy LP, void numerics, the
  structure of the diagonal term) points to closure at `λ^{3/4}·polylog`,
  not to a gain.
* Multipliers ≫ slice prime, and non-selector small subsystems: unchanged.

## Reviews

A hostile self-review of follow-up 2 found that:
* the global form of H_MS^{Sel} was needed (fibrewise is insufficient, with
  a counterexample);
* the diagonal "exact" claim was false (single-condition counterexample);
* the deadly-value test did not sample balanced moduli;
* Lemma 3.7 and Lemma 3.8 had repairable range and main-term errors;
* there were toy-LP misstatements, including a level-1 counterexample.

All of these are repaired. Theorem 5.5's proof and Prop. 5.7 were checked
as sound.

## New files

* `scripts/theta_balanced_share.py`
* `scripts/theta_pair_lp.py`
* `scripts/theta_deadly_values.py`
* `data/theta/{balanced_share,pair_lp,deadly_values}.txt`

Replay commands are in §7.

Stopping for parent review.
