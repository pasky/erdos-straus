# AGENT REPORT O34 (branch side-agent/omega9-exponent): exponent beyond 1/13

Deliverable: `POINTWISE_OMEGA9.md`, `scripts/omega9_charcheck.py`,
`data/omega9/charcheck.txt`, source `sources/omega9/montgomery-mnt3.pdf`
(+README with SHA-256). OMEGA8 §6 repaired per R30c (M1, m1–m8) and R34a.

## Result (checkpoint 1; self-reviewed once, needs parent's hostile review)

* **Thm 1.1 (linear transfer; PROVED modulo Gallagher's theorem (G)).**
  This replaces PO Thm 4.1. Its condition
  `log x ≥ C(1+log(M_1/μ))·max(log Z,K)` becomes `log x ≥ C(1+log A)·log Z`
  with `A=E_Haar|B|/μ`. Mechanism: expand `B(n)1[n≡1 (Q)]` in characters
  mod `QD`. Each coefficient is `E_D[Bχ̄_D]/φ(Q)`, bounded by
  `E|B|/φ(Q)`, not by `M_1`. All supported characters have conductor
  `≤Z`, and there are `≤Z²` of them by injectivity. Gallagher's sum over
  all primitive characters of conductor `≤Q_G` (MV III Thm 28.19, with
  the exceptional-zero variant) controls them simultaneously. The
  exceptional zero is handled as in PO: case A by the λ factor, case B by
  the twist condition.
* **Lemma 2.1 (trivial).** BRW gives `E|B| ≤ (1+2η)E B`, so `A≤1.03`.
* **Thm 2.2 (PROVED mod (G) + ET Prop 1.4):**
  `W(p) ≥ exp(c(log p)^{1/7})` for infinitely many Mordell-hard p;
  `log L_h(T) ≪ 𝓛^7`. This replaces O8 Thm 6.3 (1/13). The inputs are
  O8's system and minorant (Thm 3.4, Lemma 6.1, Lemma 3.3), unchanged. The
  transfer costs only `log Z ≤ log Q_Π + 2(3k+2d+1)𝓛 ≪ 𝓛^7`.
  Thorner–Zaman is no longer used.
* **Thm 2.3 (PROVED mod (G)):** `log W ≥ (1/log2−o(1))log₂p·log₃p`, which
  doubles O8 Thm 4.4's constant.

## Self-review R34a (deep subagent): no FATAL; repairs applied

* MAJOR 1: (G)'s exceptional-case bound was mis-transcribed; the factor
  `(1−β_1)log x` multiplies both terms. Fixed. The proof now uses
  `u<L`, and the Page bound is needed only for the imprimitive remainder.
* MAJOR 2 (in OMEGA8, from R30c m7/m8): "`K ≥ log(1/μ)` for every
  minorant" is false. The disjoint-cell representation of F has `M_1=μ`.
  The claim is now restricted to the BRW expansion as written
  (`M_1≥1`). It does not affect OMEGA9.
* Minors: upper-bound wording instead of `≍`; the remainder uses `≤Z²`
  characters, and `log D≤1.04 max d_i`, so N and `loglog(QD)` disappear
  from Thm 1.1. The script dropped all primes `≤D`; this is fixed and the
  data regenerated (rel. error −0.09% vs bookkeeping 20%). Also fixed:
  the BV range `4x^{1/3}`, `ℓ≡3 (4)`, δ in place of δ*, and the "distinct
  T" wording.

## Things a reviewer should attack

* (G) as quoted from a **draft** book (MV III, PSU course PDF), Thm 28.19,
  pp. 229–230. Gallagher's paper itself was not obtained. Is the sum over
  q≤Q including q=1 with `E_0`? Is the implied constant absolute and
  effective?
* Thm 1.1 Case A: `λ ≥ min(u,1)/2`, and the Page bound for the `R_1`
  remainder.
* Coefficient identity `c(χ_Qχ_D)=E_D[Bχ̄_D]/φ(Q)`, and that `μ_ψ=E_D[Bψ]`
  for the imprimitive `χ_D` induced by ψ. The toy check covers 23040
  characters.
* That O8 Thm 3.4's hypotheses for the class of one mod `Q_Πℓ_aux` are
  exactly Thm 1.1's.

## Not done / next

* No STATUS/DISCOVERIES edits (parent's call). If confirmed, the following
  are superseded: (H)16's 1/14, O8 Thm 6.3, and O8 §6.5/6.6's
  "PO-Thm-4.1 ceilings", which concern PO Thm 4.1 only.
* Exponent 1/6 needs **both** of the following.
  * ESW. R30c M1(i), the missing q-ary ℓ¹ bound, is moot now that K
    does not matter.
  * A smaller quarantine, `log Q_Π ≪ 𝓛^6`. One idea is a uniform
    per-prime bound `w_ℓ ≪ 𝓛^{O(1)}/ℓ` (a Shiu-type upper divisor sum in
    progressions). All bad primes would then be `≤𝓛^{O(1)}`.
* Opening (b) (sieving singles separately) now matters only through
  `log Z`. It is not pursued.

## Round 2: parent's hostile reviews R34a, R34b (both: Thm 1.1, 2.2, 2.3 SOUND; no FATAL/MAJOR)

Merged `side-agent/review-omega9a` and `side-agent/review-omega9b`. All
minors are applied.
* R34a m1–m2: fix `κ:=max(3κ_0,1/c_1)`. Cite MV's Exceptional Zero
  Statement (28.61)–(28.62) for uniqueness of χ_1. Add a source caveat:
  the MV draft's proof slip is repairable, and the statement is
  Gallagher's Thm 7.
* R34a m3: one-line proof of `λ≥min(u,1)/2` for all u.
* R34a m4 / R34b m1: Case A needs `x ≥ C·A·Z^4`. This is now listed
  (`x≥Z^5`).
* R34a m5: in Case A, `q_1|Q`.
* R34a note: `E_D` = O8's Haar mean.
* R34b m2: Wigert's `log2` is derived (single τ in O2 Lemma 11.1).
* R34b m3: O8 §6.6 wording (`𝓛^4`, and "no `log(1/μ)` or `M_1`").
* R34b m4: O8 header renumbered, with 1/13 and 1/4 marked superseded / PO-only.
* R34b observation added to O9 §3: with `z=𝓛^a`, `log Q_Π ≫ 𝓛^{1+a}/log𝓛`
  is a choice-specific floor (≈1/3 at a=2); the only z-free floor is
  `log Z>𝓛`.
* R34b: the bottleneck is the junta term `d𝓛` (≈860× `log Q_Π` in the
  tally). Lemma 6.1's ℓ¹ bound is not needed by O9.

## Phase 2 (OMEGA9 §4): the junta term d𝓛 — checkpoint 2 (unreviewed)

* **Lemma 4.1 (PROVED; exact toy check `scripts/omega9_junta_lb.py`).**
  Take disjoint single-value events of width k on `[q]`. Then
  `energy(F;t) ≥ (1−π)^{2m}Σ_{j>t/k}binom(m,j)ρ^j`. In the limit
  `q→∞` this gives `energy(F;t)/δ → Pr[Po(S)>t/k]`.
* **Cor 4.2 (PROVED).**
  * Any junta-t approximation with ℓ² error `≤δ/3` needs `t ≥ k(S−1)`.
  * O8's EL precision needs `t ≥ (3.59−o(1))kS`.
  * So for general width-k, mass-S systems, an ES-tail argument needs
    junta `≍kS`. ESW (`d≍k·k_0`) would be optimal, and the bit factor
    `b≍𝓛` is the only removable loss.
  * Under ET (worst case: mass `≍S*` at width k), the floor of this method
    is `d𝓛 ≳ kS*·log z`. **1/6 is the ceiling of width-and-mass-only
    arguments.** Beating it needs ES-specific structure: where the mass
    actually sits, and the actual S.
* **§4.3 (identity PROVED; rest Assessment).** The identity
  `Σ_U binom(|U|,s)‖F^{=U}‖² = Σ_{|V|=s}‖L_VF‖²` reduces ESW to cube sums.
  These vanish unless (a) relevant events cover V and (b) no V-avoiding
  event occurs. A union bound using (a) alone would give ESW
  (`d≍k(S+log 1/ε)`, no b) if relevance events were independent. Hubs
  break this: the cover sum is `≈P(H)^{1−s}(2eS_H/s)^s`, while the truth
  carries `e^{−Θ(S_H/P(H))}` from (b). So ESW needs conditional
  (local-lemma-type) suppression, the same missing ingredient as O8 §2.4.
  ESW remains **open**.
* Quarantine: not attacked in this round. The plan is unchanged: a
  uniform per-prime bound `w_ℓ≪𝓛^{O(1)}/ℓ` (Shiu-type). It pays off only
  together with ESW.
* Stopping here: context is near the limit.
