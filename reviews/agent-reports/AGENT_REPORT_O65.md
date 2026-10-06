# AGENT_REPORT_O65 — sieve-limits-note v5

Branch `side-agent/sieve-paper-v5-2` (not merged). File: `paper/sieve-limits-note.tex` v4 → v5,
compiled with pdflatex ×3: 71 pp., no undefined refs/citations, no multiply-defined labels; the
only overfull box is the pre-existing 1.29pt one of v4 (lines ≈3818–3825). README entry in
`paper/README.md`. After the parent's instruction, `main` was merged (EXCEPTIONAL_LARGESIEVE4.md, ledger (D)28,
reviewed) and LS4 was added as §14.6 (item 1b below).

## Change list for a referee (v4 → v5)

Numbers are those of the v5 PDF.

1. **§14.5 (new) Smooth–rough splitting: one large prime per modulus** (source LS3 =
   EXCEPTIONAL_LARGESIEVE3.md, review R59; ledger (D)27).
   * Thm 14.12 = LS3 Thm 1.1 [proved, elementary], with HY + Jensen + Hölder proof sketch.
   * Bounded-density measure on the smooth part (LS3 Lemma 2.1), stated in prose with its
     label [proved given KA2 §§2–4; Case A mod ElT Prop 1.4].
   * Thm 14.13 = LS3 Thm 3.1: cap `C(log N)^{3/4}(log log N)^3` for every CRT-admissible large sieve,
     any frequencies, over mixtures with ≤1 prime factor `> exp((log N)^{1/4})` per modulus;
     same labels. Remark: extends the *scope* of Thm 14.3 (LSslice), not its strength (R59 D5);
     the `(log log N)^3` is KA2's Rankin loss (removal by Lemma 10.9 not checked).
   * Scope paragraph on arbitrary mixtures (z-smooth frequencies only, with the
     nonempty-fibre proviso; mixed frequencies not covered) — R59 D2 wording.
   * Hyp 14.14 (H_rough) [conjecture], explicitly a *sufficient* condition only (R59 D1);
     two-copy form (LS3 Lemma 4.1) in prose [proved].
   * Lemma 14.15 = LS3 Lemma 4.2 (residue concentration) [proved]; KP-route failure and
     one-step-bound losses marked Assessment (R59 D3).
   * (E1) in §14.4 re-scoped; §14 intro lists LS3, SPW, SPW2.
1b. **§14.6 (new) Damped collisions: residue-sparse mixtures at every level** (source LS4 =
   EXCEPTIONAL_LARGESIEVE4.md, review R62 `exceptional-largesieve4-review.md`: no FATAL/MAJOR,
   minors D1–D6 applied; ledger (D)28).
   * Lemma 14.16 = LS4 Lemma 1.1 (damped-collision reduction) [proved], with proof.
   * Conditioned-law collision bound `e^{2B}/Q'(G_B)²` (LS4 Lemma 2.1, Prop 4.1) in prose [proved].
   * Thm 14.17 = LS4 Thm 4.2: all-level cap `(log N)^{3/4} + Cγ^{-3}(log N)^{3/4}(log log N)^3` for every
     forced mixture **from (A*)** [proved implication; inputs as Thm 14.13]; `N₀(γ) = exp(Cγ^{-4})` (R62 D1).
     "Far weaker than H_LS∞" marked Assessment.
   * Pinned pivotal bound (LS4 Lemma 5.1) in prose [proved].
   * Thm 14.18 = LS4 Thm 5.2 + Cor 5.3: the same cap for residue-sparse multi-rough classes (RS_γ),
     in particular H-small classes (`−4, −1, −1/4, −4d, −1/(4d)` mod any M, ...) with γ = 1/4 [proved].
     Strictly extends Thm 14.13; closes LS3's nonempty-fibre proviso for the families covered (R62);
     contains Lemma 14.15's family ("residue concentration is the easy case"; §14.5 text updated).
   * Open: (A*) for residue-dense multi-rough classes; (CC) [conjecture].
   * Propagated to abstract, intro item 6, intro exclusions item, §16 item 1 and 8, §17 (iii)/(vi),
     "New in version 5", "Gone since version 4".

2. **§14.9 Hybrid methods** (sources SPW = EXCEPTIONAL_SPW.md, review R40; SPW2 =
   EXCEPTIONAL_SPW2.md, review R53; ledger (D)26 updates).
   * v4's Hypothesis "SPW (open)" is now Definition 14.28 (label kept `hyp:SPW`); text says the
     fixed-margin form stated in v4 is false.
   * Prop 14.29 (IF2 Prop 9.1, Lemma 9.3): the "SPW with σ bounded below gives the cap" sentence
     removed (vacuous now).
   * Thm 14.30 = SPW Thm 3.2 [proved]: `σ ≲_C (log N)^{-1/2}`, with proof sketch; exact certificates
     σ ≤ 72/185 (N=300), σ ≤ 0.381133 (N=1150); "σ* = 2/5" LP pattern declared a small-N artefact;
     Flat margin (SPW Cor 3.3) and BDW (SPW §2) in prose.
   * Lemma 14.31 = SPW Lemma 1.4 + SPW2 Lemma 1.1 [proved implication; sufficiency only, R53 M1]:
     saving ≤ `S' + log(K/η) + log(1+Δ'/K) + log(1+c) + O(1)`; includes R53 m1 (Thm 14.27 usable
     without its t, 1/Δ hypotheses). Consequences (3/4-cap iff ℓ_N = O((log N)^{3/4}) *for this
     route*; polynomial margins give only `B ≥ N^{1−c−o(1)}`). The (log N)^{3/4} form of S' stays
     pointer-level, as in v4.
   * Hyp 14.32 (weak SPW) [open] — replaces SPW as the target everywhere (intro item 6, §16 item 3,
     §17 (iv)).
   * Thm 14.33 = SPW2 Thm 3.1 (K-free edge bound, `η ≲ (log N)^{-1/3}`) [proved]; SPW2 LPs to N ≤ 80
     [evidence]. The v4 remark "Δ₀ must be ≤ e^{S_A}" is superseded by Lemma 14.31.
3. **§16 Exclusions / §17 Open problems.** Item 1 and (iii): large sieve outside only for classes with
   ≥2 primes > `exp((log N)^{1/4})` (H_rough would suffice; z-smooth frequencies covered under the
   nonempty-fibre proviso). Item 3 and (iv): weak SPW instead of SPW; fixed-margin SPW refuted. Item 8
   and (vi): Thm 14.13 needs no bound on family primes (LS3 Thm 3.1: "no bound on their size").
   "New in version 5" and "Gone/changed since version 4" paragraphs.
4. **§18 (new) One sieve limit behind both ceilings** (source CU = CEILINGS_UNIFIED.md, review
   `ceilings-unified-review.md`; ledger (H)29).
   * Pointwise background: W(p), Mordell-hard; OMEGA13 Thm 5.1, OMEGA14 Thm 4.5/Cor 4.6 with their
     published inputs; Haar exponent `𝓛³ ≪ log(1/δ*) ≪ 𝓛³(log 𝓛)^5` (CU Prop 1.1, OMEGA13 Thm 3.4).
   * Thm 18.1 = CU Thm 4.1 (two-sided order-k limit) [proved; no novelty claimed].
   * CU Prop 4.2 (atoms block level `≤ c𝓛⁴` minorants) in prose, labels/ineffectivity stated.
   * Thm 18.2 = CU Thm 4.3 [proved as a conjunction; item (3) proved within the scopes, Assessment
     outside]; `a/(a+1)`, `1/(a+1)` extrapolation [conditional]; the reviewer's caution that (U−) for the
     subfamily does not bound majorants of the full avoider (that is Thm 10.12) is stated.
   * π(N) form: CU Thm 2.1 / Prop 3.1, explicitly "a reproof, not an improvement"; Haar-side route =
     the 3/4 note's route; CU Cor 3.3.
   * One-sentence pointer to OMEGA16 ((H)30): LS ⇒ 1/3 [conditional]; EH/GEH/BV via linear
     certificates capped at 1/4 (Prop 3.1). Beyond the brief; remove if the parent prefers.
5. **Abstract, intro, bibliography.** Version 5; abstract adds weak SPW / refutation, the rough-slice cap,
   and the unified picture; intro source list (now 25 documents; v4 said "eighteen" but listed 17),
   review list, a "version 5 adds" sentence, results items 6 and 9 (new). Bib: LS3, LS3r, LS4, LS4r, SPW, SPWr,
   SPW2, SPW2r, CU, CUr, O13, O14, O16.

## Points a referee should check

* Thm 14.13's statement "no bound on modulus size": taken from LS3 Thm 3.1; the J-integral runs to ∞
  over KA2's first-moment bound 𝔐(y), which is uniform over the universe — confirm.
* Lemma 14.31 cites SPW2's remark that Thm 14.27 holds without its t, 1/Δ hypotheses; the v5 text of
  Thm 14.27 itself still carries them (unchanged from v4).
* §18 cites OMEGA13/14/16 only through their internal statements; their published inputs are named
  but not individually cited in the bibliography.
* No new mathematics in v5; everything is transcribed from reviewed sources, with proof sketches
  shortened.
