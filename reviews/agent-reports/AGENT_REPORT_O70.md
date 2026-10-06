# AGENT REPORT O70: novelty audit 2026-10b

* **Branch:** `side-agent/novelty-audit-2`.
* **Deliverable:** `reviews/novelty-audit-2026-10b.md`. It has 8 sections and a summary
  table.
* **Exploratory script (EVIDENCE only):** `scripts/o70_nc_lp.py`, output in
  `data/o70/nc_lp.txt`. It is a floating-point scipy LP.
* **Search limits:**
  * No internet. Only `sources/` and memory were used, and every claim carries a
    [checked] or [memory] tag.
  * Nothing in DISCOVERIES.md / STATUS.md was edited (per the brief).

## Findings that change current wording

1. **The planting lemma is undersold** (OMEGA14 Lemma 1.1, (H)27 "no novelty claimed").
   * BGP arXiv:1201.3261 §4.9, Thm 27 [checked in the archived text] bounds
     `n_c(k,p)`. This is the least n for which a k-wise independent law of
     Bernoulli(p) bits can avoid the all-ones point.
   * BGP's bounds are two-sided but leave gaps: the lower bound is `≈ k/(2(1−p))`, while
     the upper bound `C·k/(1−p)·log(1/(1−p))` holds only for `1−p = 1/q`, q a prime power.
   * Lemma 1.1, after flipping bits, gives `n_c ≤ (k+1)p/(1−p)+2k+2` for all p, with
     arbitrary marginals in general. That is within a factor ≈2 of BGP's lower bound.
   * The exploratory LP finds the truth within +3 of BGP's lower bound.
   * Relative to the TCS literature this is a modest positive contribution, unless a
     post-2012 paper closed the gap (not searchable here).
2. **The β-weighted LLL** (OMEGA13 Lemma 1.1, (H)26) is a standard asymmetric-LLL
   instance. It should be labelled "standard", not presented as a tool.
3. **Haar exponent 3.** Elsholtz–Tao Remark 1.2 [checked, `audit-elsholtz-tao-1107.1010.txt`
   ll. 222–226] already states the heuristic: a prime has a solution with probability
   `1 − O(exp(−c log³p))`. It also calls Vaughan-type large-sieve results its rigorous
   analogue. (H)25/(H)26 and the es-subexp note should cite this. The typical-size theorem
   is Vaughan's method applied to W.
4. **The Janson-type inequality** (HAAR Thm 1.4) is the Boppana–Spencer proof with Harris
   replaced by the HSS inflation bound. The suspected closest prior art is Lu–Székely /
   Mohr (memory, must-check).
5. **Energy/DNF note.** The current hedge is fair. Add Lovett–Wu–Zhang 2020 ("mild random
   restrictions") to the must-check list.
6. **LS4 Lemma 3.1** (coin-coupling Fourier bound) is the Lecomte–Tan Fact 9 device. Cite
   it there too.
7. **LARGESIEVE Thm 2.1 duality** is a minimax form of the classical large-sieve ⇔ Λ²
   equivalence (Montgomery 1968; Kobayashi 1973, memory). Cite it as known in substance.

## Proposed wording (for the parent to apply or adapt)

**STATUS.md, novelty-audit paragraph.** Append:
> A second audit (2026-10-05, `reviews/novelty-audit-2026-10b.md`, no internet) covers the
> OMEGA9–17 / WINDOW / KARY3 round.
> * **Standard:** the β-weighted LLL; the large-sieve/Λ² duality.
> * **Known method, new statement:** the Gallagher transfer; the Janson-type inequality
>   (closest suspected prior art Lu–Székely); the typical-size bound (Vaughan's method).
> * **Heuristically anticipated:** the Haar exponent 3 (Elsholtz–Tao Remark 1.2).
> * **Apparently new:** the energy bound and the constant-1 DNF tail (hedged); the planting
>   lemma, which sharpens Benjamini–Gurel-Gurevich–Peled Thm 27; the W(p) Ω-rates, the 1/4
>   ceiling and LS ⇒ 1/3; the window stacking exponent.

**DISCOVERIES.md**

* **(H)21, last sentence of the Cor 4.1 bullet.** Replace with:
  > "Nearest prior art: Lecomte–Tan (FOCS 2021, Fact 9: cover-probability bound, unsigned,
  > uniform measure). LMN/Håstad give `2^{−t/(Cw)}` with C≈20. Theorem 1.1 and the
  > constant 1 appear new, but the comparison with Håstad 2001, Lovett–Wu–Zhang 2020,
  > Furst–Jackson–Smith and the Fourier-growth literature is from memory
  > (`reviews/novelty-audit-2026-10b.md` §1)."
* **(H)25, "New tool" bullet.** Add:
  > "The proof is Boppana–Spencer's proof of Janson's inequality with the Harris step
  > replaced by the Haeupler–Saha–Srinivasan LLL inflation bound. Statement apparently new
  > for one-hot product spaces; Lu–Székely's LLL enumeration papers are the suspected
  > closest prior art (unchecked; audit 10b §2)."

  Also add after the first sentence:
  > "Exponent 3 is the rigorous profinite form of Elsholtz–Tao's Remark 1.2 heuristic
  > `1−O(exp(−c log³p))`."
* **(H)26, "Ingredients" bullet.** Change "a β-weighted local lemma …" to:
  > "a standard per-coordinate form of the asymmetric local lemma with weights
  > `x_E = β^{|supp E|}P(E)` (Lemma 1.1; no novelty; the campaign-specific point is the
  > choice β = 1+1/log𝓛)".
* **(H)27, planting bullet.** Replace "(the LP dual of lower-bound sieves; no novelty
  claimed)" with:
  > "(the LP dual of lower-bound sieves). In the identical-marginal case it gives
  > `n_c(k,p) ≤ (k+1)p/(1−p)+2k+2` for Benjamini–Gurel-Gurevich–Peled's threshold
  > (arXiv:1201.3261 Thm 27). This removes their `log(1/(1−p))` factor and prime-power
  > restriction and matches their lower bound up to a factor ≈2 (audit 10b §4; later
  > literature unchecked)."
* **(H)19 / (H)23.** Add:
  > "Thm 1.1 is a packaging of Gallagher's proof of Linnik's theorem (log-free density over
  > all characters of conductor ≤ Z) applied to a minorant weight. The method is standard;
  > the novelty is the covering-avoidance pipeline (audit 10b §5)."
* **(H)29.** Already says "no novelty claimed" for Thm 4.1. Add:
  > "both ceilings are instances of the large-dimension sieve limit `log D ≍ κ log z`
  > (β_κ ≍ κ), proved here as a barrier for all certificates in the stated classes".
* **(H)30.** Add:
  > "LS is a log-scale sifted-set analogue of Linnik's theorem. It is weaker than the
  > Granville–Pomerance / Heath-Brown least-prime conjectures for a single class. No prior
  > named statement known (audit 10b §5)."
* **(D)19.** Change "by exact duality (Thm 2.1, standard minimax)" to:
  > "by exact duality (Thm 2.1, a minimax form of the classical large-sieve ⇔ Selberg-Λ²
  > equivalence, Montgomery 1968 / Kobayashi 1973 [memory])".
* **(D)28 (LS4).** Add to Lemma 3.1:
  > "(the coin-coupling bound is the Lecomte–Tan Fact 9 device)".
* **(H)18.** Add:
  > "W1's lower half is implied by Fuchs–Hsu–Rickards–Schindler–Stange 2025 Thm 1.1(2);
  > W2 is FI09-type; the new content is the half-set lemma and the exact exponent
  > `1+J(Z)/2` (audit 10b §8)."
* **(H)20.** It already says "Selberg's example realised by primes". No change.
* **(H)16–(H)31 Ω headline.** Unchanged. The audit confirms that no prior quantitative
  Ω-result for an ES certificate parameter is known. Mordell/Yamamoto/Schinzel are
  qualitative only.

**Paper-level** (optional):
* `paper/es-subexp-note.tex`:
  * cite ET Remark 1.2 at the Haar-exponent statement and Vaughan/PW §4 at the
    typical-size theorem;
  * call the β-weighted LLL standard;
  * at the planting lemma, compare with BGP Thm 27.
* `paper/energy-dnf-note.tex`: add Lovett–Wu–Zhang 2020 to the must-check list.

## Must-check list for an external search
1. Lu–Székely 2007/2009 and Mohr 2013 (item 2).
2. Lovett–Wu–Zhang 2020 and Håstad 2001 (item 1).
3. Citing papers of BGP arXiv:1201.3261 on `n_c` / minimal AND probability (item 4).
4. CHHL 2019, Chattopadhyay–Hatami–Lovett–Tal, KLLM global hypercontractivity (item 1).
5. Montgomery 1968 and Kobayashi 1973 (item 7).
6. Pollack-type least primes under many local conditions (item 5).

Stopping here for parent review.
