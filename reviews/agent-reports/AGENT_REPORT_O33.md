# AGENT REPORT O33: novelty audit + paper for the sub-exponential W(p) bound

Branch `side-agent/omega-paper-v4`. Status: **checkpoint, draft complete, ready for a referee.**

## Deliverables

1. `reviews/novelty-audit-omega8.md` (Step A).
2. `paper/es-subexp-note.tex` / `.pdf` (Step B), 16 pages, compiles cleanly
   with pdflatex: no warnings, no undefined references.
3. A `paper/README.md` entry.

## Step A in brief

No internet in this pass, so the audit relies on archived sources and
memory, and says so throughout.

* **Statements (Thm 4.3/4.4): NEW.** No Ω-result for any ES witness
  parameter appears outside the campaign (consistent with the earlier
  audit). Caveat: W is campaign-defined.
* **Lemma 3.1 (BRW minorant): KNOWN** (Razborov's form of Bazzi). It must
  be credited as such, and the paper does.
* **Lemma 4.1: KNOWN technique** (LMN + Håstad + routine bit encoding).
* **Apparently new, low–medium confidence:** using a bounded-independence
  sandwich as a sieve minorant transferred to primes, and a switching-lemma
  bound on a sieve/covering-avoidance error term. The known number-theory
  uses of AC0 tools (Green, Bourgain on Möbius) run in the opposite
  direction. The nearest relatives are Hough and BBMST (covering systems,
  distortion method), and they match only the Haar side.
* Noted analogue: Selberg's Λ²-type lower sieve, `(1−Σ1_{p|n})(Σλ_d)²`, is
  the classical "1 − quadratic" minorant. BRW differs in two ways: its
  level is junta size rather than modulus size, and its correction is local
  (first occurring event).

## Step B: decisions and justification

* **New note rather than v4.** In v3 the core (§§7–12: support truncation,
  pseudoforest, hypergraph moments, multilevel minorants) is fully
  superseded. Its other content (slice parameter / least QNR, Haar Type I
  dictionary) is refereed and unrelated. A v4 would either carry ~1000
  lines of superseded machinery or delete refereed results. The new note
  cites v3 as `[Paper1]` and copies v3's atoms lemmas, quarantine, and §§4–5 (TZ, severe-zero lemma,
  transfer theorem) verbatim with proofs. Structure: §2 residual system, §3–4 analytic input/transfer,
  §5 LLL + Efron–Stein + BRW + size + twist, §6 switching-lemma tail, §7 assembly + Thms 1.1/1.2.
* **Astra:** v3 does not cite astra, and nothing in this note concerns the
  signed-seed line. Following v3's policy, there is no astra citation.
* **§6 of OMEGA8 (exponent 1/13) is not included.** Remark 7.2 says only
  that the exponent 14 is bookkeeping and that "sharper choices of the
  parameters appear to lower it somewhat; we do not pursue this here."

## Changes relative to OMEGA8 (for the referee to check)

1. **Events are built from distinct pairs `(r_Π, class)`, then lifted**
   (Def 2.5, Lemma 2.6). OMEGA8 split "atoms" and said that duplicates are harmless.
   With pairs, `w_ℓ = w_ℓ(Π)` holds exactly, including duplicate lifts,
   so the local lemma's neighbourhood sums are bounded by `c_0` with no
   further argument.
2. **Lemma 5.4 (size):** constant `+2` instead of `+3`, from an explicit
   count (`1+m+2m²+m³ ≤ 5m³`).
3. **Lemma 6.2 (tail):** the density ratio bound is `4/3`, from
   `(1−1/(4N))^{−N}`; OMEGA8 had `e^{1/2}`. `p = 1/(10w)` with
   `C_H = 5`, so `t = 10kbk_0`.
4. **Lemma 5.5 (twist):** written out in full, including
   `μ_ψ = E[Bψ]` (f is odd and squarefree, and its primes are free) and
   `E F' ≤ δ/0.98`. Final constant `0.031 μ < μ/4`.
5. **Lemma 2.3 (mass bound):** written out self-contained, including the
   ET dyadic step that gives (b), `S* ≪ 𝓛⁴ log𝓛` (A, B ≥ 2 blocks).
6. **New Assessment remark (Rem. 4.2):** here `K ≍ log Z ≍ 𝓛⁷`, so a
   Page-type PNT with error `O(xe^{−c√log x})` for `q ≤ e^{c√log x}` would
   also give `log x ≫ (log Z + K)² ≍ 𝓛^{14}`. So Thorner–Zaman's Linnik
   range is apparently **not** what sets the exponent here, unlike in v3.
   This is not proved and not used. A referee should confirm or delete it.

## Open items / things not checked

* Bibliographic details for Bazzi, Razborov, Braverman, Håstad, LMN,
  Kaas–Buhrman, Efron–Stein, Hoeffding, Green, Bourgain, Hough and BBMST
  were written from memory; the last four are flagged by a `TODO(verify)`
  comment in the .tex. The switching-lemma constant 5 follows O'Donnell
  §4.4, which R30a checked.
* The effectivity of ET Prop 1.4's constant has not been checked, and the
  paper says so.
* No literature search was possible. The first item for an external
  reviewer: citations of Bazzi/Razborov/Braverman in number theory.

## Replay

```
cd paper && pdflatex es-subexp-note.tex && pdflatex es-subexp-note.tex
```

## Response to referee R33 (MINOR REVISION; `reviews/es-subexp-note-review.md` on `side-agent/referee-subexp`)

Numbering below is the new one. Since Thm 2.3 was inserted, Lemma 2.3 → 2.4,
Def 2.5 → 2.6, Lemma 2.6 → 2.7, and §§3–8 are unchanged. Each point is a
separate commit.

1. **ET Prop 1.4 stated.** It is now a cited box, Theorem 2.3, with
   `log(1+κ)` included, and the text notes that κ=4 makes it a constant.
   ET's k was renamed κ, and the proof's local variable `A=srk` was
   renamed `A=srh`, so the paper's k is again only the support size.
   Lemma 2.4(b) cites Thm 2.3.
2. **`0<λ<2` moved out of the TZ box** into a remark right after it, with a
   one-line proof: `β₁>1/2`, `log x>2`, so `x^{β₁−1}/β₁<1`.
3. **Labels made consistent.** Thm 1.1 is now "modulo Thms 3.1, 2.3, 6.1"
   and Thm 1.2 "modulo Thms 3.1, 6.1". The status-conventions paragraph
   names the three cited inputs and says that classical facts (LLL,
   Efron–Stein, binomial median, divisor bound) are not listed in labels.
   §8 is updated to match.
4. **Remark 7.2** now says Paper1's `𝓛⁷/log𝓛` Haar bound holds "modulo
   [ET, Prop 1.4]".
5. **Literature relatives.**
   * Filaseta–Ford–Konyagin–Pomerance–Yu (JAMS 2007) is now cited as the
     closest Haar-side relative, hedged "to our knowledge".
   * Even–Goldreich–Luby–Nisan–Veličković is cited with one sentence:
     bounded independence fools rectangles, which is the prime-local
     case; Bazzi extends this to DNFs. Its STOC'92 data come from
     BGP ref. [16] in the archive; the journal version (RSA 1998) is
     from memory.
   * The novelty claim is unchanged.
6. **Bibliography.** The TODO(verify) comment is kept and extended to
   FFKPY, the EGLNV journal version, and the TZ journal data.
7. **Overfull boxes.** All eight are fixed, by splitting the displays in
   (5.1), Lemma 5.4, Lemma 5.5, Cor 6.3 and Thm 7.1 and rewording three
   paragraphs. pdflatex (2 passes) now reports no overfull or underfull
   boxes, no warnings and no undefined references, at 17 pages. My
   earlier "no warnings" grep had missed the overfull boxes: I grepped
   only for "warning", and the log reports them as "Overfull \hbox".
8. **Wording.**
   * (i) "equivalently" → "more precisely".
   * (ii) `log₂` is always the binary logarithm.
   * (iii) The stray "Distinctness…" paragraph after Thm 7.1 is removed.
     Def 2.6 now says that pair-then-lift is what makes Lemma 2.7(iii) an
     equality, that duplicate lifts are counted on both sides, and that
     duplicates are harmless in the indexed-family Lemmas 5.1/5.3/5.5.
   * (iv) Lemma 6.2(b) now sets `w := kb ≥ 1` (k ≥ 1 since supports are
     nonempty), so `p = 1/(10w) ≤ 1` and `d = 10kbk₀` exactly.

No mathematical content changed. Stopping for the parent.

## v2 (after merging main with POINTWISE_OMEGA9): change list for the referee

Branch `side-agent/omega-paper-v4`, merged with `main` @251f464. The paper is
`paper/es-subexp-note.tex`, "Draft v2", 18 pp. pdflatex (2 passes) gives no
overfull or underfull boxes, no warnings and no undefined references.

**Headline changes**
* Thm 1.1: exponent **1/14 → 1/7**, `log p ≤ C(log T)^7`, proved modulo
  Gallagher (Thm 3.2, with Thm 3.1), ET Prop 1.4 (Thm 2.3) and Håstad
  (Thm 6.1).
* Thm 1.2: constant **1/(2log2) → 1/log2**, proved modulo Gallagher and
  Håstad.
* **Thorner–Zaman is no longer used.** It is cited only for comparison
  (intro, Remark 4.2, §8). Removed: the TZ box, the severe-zero lemma, the
  TZ transfer theorem, Remark "Page-type" (old 4.2), the McCurley bib item,
  and the `M_1` bound of the old Lemma 5.4 with its product inequality.

**New or rewritten sections**
1. **§3 (analytic input).**
   * Thm 3.1: exceptional-zero statement, MV III (28.61)–(28.62),
     including the effective Page-type lower bound for `1−β₁`.
   * Thm 3.2: Gallagher's theorem, quoted from MV III Thm 28.19 (archived
     at `sources/omega9/`, pp. 229–230), including the exceptional-case
     replacement of both the left- and right-hand sides.
   * We fix `κ = max(3κ₀, 1/c₁)`.
   * A source caveat paragraph: MV III is a draft, its proof has slips
     (hence `κ ≥ 3κ₀`), and Gallagher's original was not seen.
   * Minor point to check: Thm 3.1 is stated "for every Y ≥ 3". MV's
     passage writes the product up to T and does not state a range.
2. **§4 Thm 4.1 (linear transfer), full proof.** It follows OMEGA9 Thm
   1.1, with its R34a/R34b repairs, rewritten. The proof covers:
   * the parameters `L`, `Q_G = x^{1/(κL)}`;
   * the character expansion `c(χ) = E_D[Bχ̄_D]/φ(Q)` and facts (a)–(c);
   * the remainder `R_1` (prime factors of QD, `≤ 2AZ³μ/φ(Q)`);
   * **Case 0**: no exceptional zero;
   * **exceptional case**: the `min(u,1)` bookkeeping, then **Case A**
     (χ_D principal: `λ ≥ min(u,1)/2`, and the Page bound with `q₁ | Q`
     absorbs `R_1`, needing `x ≥ C A Z⁴`) and **Case B** (χ_D
     nonprincipal: twist condition, `|μ_ψ| ≤ μ/4`).
   Remark 4.2 compares this with the Thorner–Zaman route
   (`K·log Z ≍ 𝓛^{14}`).
3. **§5.**
   * Lemma 5.4 is now the "cell structure of B" (cells on ≤ 3k+2t
     coordinates, unit classes, identity valid on ℤ), with no `M_1` bound.
   * The Cells paragraph notes that the Haar mean equals `E_D`.
   * New Lemma 5.5 (ℓ¹-tightness, OMEGA9 Lemma 2.1):
     `E|B| ≤ (1+2η) E B`. Lemma 5.6 (twist) is unchanged.
4. **§7 Thm 7.1 (assembly).**
   * The conclusion is now `log p ≤ C₆ log Z` with
     `log Z ≤ (π(z)+64k²S*)𝓛 + 2(3k+2t+1)𝓛 + 4`.
   * `A ≤ 1+2/99 < 1.03 ≤ Z^{1/4}`, from `E[F−B] ≤ δ/100 ≤ μ/99`.
   * The proofs of Thms 1.1/1.2 are redone: `t ≪ 𝓛⁶`, `log Z ≪ 𝓛⁷`; for
     Thm 1.2, `log₂p ≤ log(S*+1) + O(log𝓛)`.
   * Remark 7.2 (Assessment):
     - the bottleneck is now the junta term `t𝓛`;
     - the quarantine term matches Paper1's Haar bound (mod ET);
     - with z = 𝓛² the quarantine alone gives a floor `≍ 𝓛³/log𝓛`.
   * OMEGA8 §6 and OMEGA9's tail-lemma variant are still not used. The
     paper's own Lemma 6.2 (`t = 10kbk₀`) already gives `𝓛⁶`.
5. **Abstract and intro.**
   * New theorem statements.
   * A paragraph on the transfer as "Linnik's theorem with weights".
   * A note that v1 had 1/14 via TZ.
   * Novelty paragraph: Gallagher's theorem used as a *transfer device*
     for an arbitrary signed combination of progressions, with the cost
     governed by `E|B|` and the largest modulus, not by the number of
     cells. This is hedged: no systematic search, and Linnik-type bounds
     for many congruence conditions are classical.
6. **Status conventions and §8** are updated. Here "modulo Theorem 3.2"
   includes Thm 3.1.
7. **Bibliography.** Added Gallagher (Invent. Math. 11 (1970) 329–339;
   from OMEGA9/MV, not seen) and MV III (draft). TODO(verify) flags are
   kept.
8. **paper/README.md** is updated.

Stopping for the parent.

## Response to referee R33b (v2: MINOR REVISION, one MAJOR M1)

Each fix is a separate commit. The paper is now 19 pp. pdflatex (2 passes)
gives no overfull or underfull boxes, no warnings and no undefined
references.

* **M1 (Thm 3.1 not a theorem as stated).**
  * Thm 3.1 is now "Landau–Page; classical" ([Dav, Ch. 14], [MV I, Cor.
    11.10]). It says: at most one zero of `∏_{q≤Y}∏*L(s,χ)` in
    `Re s > 1−c₁/log Y`, **|Im s| ≤ Y**; if it exists it is real and
    simple, with χ₁ quadratic.
  * The Page bound `1−β ≥ c₂⁻¹q^{−1/2}(log q)^{−2}` is now stated for
    every real zero of every real primitive L-function.
  * A paragraph explains why the height cutoff is necessary, notes that
    MV III (28.61) omits it, and says that only real zeros are used.
  * Nothing downstream changed. Uniqueness is applied to a real zero
    (Im s = 0 ≤ Q_G).
* **m1 (κ ≥ 3κ₀ inconsistency).** The source caveat now derives the
  statement for every κ ≥ 3κ₀ from the printed κ = 3κ₀ case, following
  the referee's monotonicity argument. If
  `1/(κ log Q_G) ≤ 1−β₁ < 1/(3κ₀ log Q_G)`, then
  `x^{β₁}/β₁ ≤ 2x e^{−log x/(κ log Q_G)}` and the replaced right-hand side
  is ≪ the non-exceptional one. So `κ := max(3κ₀, 1/c₁)` is justified.
* **m2.** `log D ≤ ψ(max d_i) < 1.04 max d_i` now cites Rosser–Schoenfeld
  (Illinois J. Math. 1962).
* **m3.** Gallagher is cited without a theorem number ("not seen"). A
  sentence shows the use is robust to a possible range
  `exp(√log x) ≤ Q_G ≤ x^b`: we have `log x/log Q_G = κL ≥ 6c` and
  `log x ≥ (κL)²`. The latter is now listed explicitly among the
  parameter consequences in the proof of Thm 4.1, with its one-line
  justification `(1+log A)² ≤ (1+log A)(1+¼log Z)`.
* **m4.** The novelty paragraph now names the nearest analogues:
  Lagarias–Montgomery–Odlyzko 1979 and Thorner–Zaman (Chebotarev,
  ANT 2017), i.e. least primes in unions of classes or abelian Chebotarev
  classes, which concern nonnegative indicators. The claimed novelty is
  narrowed to the signed minorant, whose cost is `A = E|B|/E B`. It
  remains hedged.
* **m5.** Cor 6.3 is restated for *any* integer
  `k₀ ≥ 3S log₂e + log₂(400m²(S+1))`. Thm 7.1 now says explicitly that
  its `k₀` (in terms of T^{2k+4} and S*) satisfies this.
* **m6.** The m = 0 case now reads: "F ≡ 1; B = 1, so D = 1, μ = A = 1,
  the twist condition is vacuous; go directly to the transfer."
* **Bibliography.** Added MV I, Rosser–Schoenfeld, LMO and
  Thorner–Zaman (Chebotarev). The TODO(verify) comment is extended to
  these, plus the earlier items.

### Does M1 (and m1) affect POINTWISE_OMEGA9.md? Yes, in the quotation only; not in the proof.

* **The M1 omission is inherited.** OMEGA9 §1 (lines 59–61) cites "MV's
  Exceptional Zero Statement (28.61)–(28.62), p. 216, valid for zeros
  with `1−β<c_1/log Q_G`", with no height restriction. As literally
  quoted, this is the same non-theorem.
* **The proof is unaffected.** OMEGA9 Thm 1.1 uses the statement only for
  the **real** exceptional zero of (G): its uniqueness, the reality and
  quadraticity of χ₁, and the Page bound in Case A. All of these hold by
  the classical Landau–Page theorem (Davenport ch. 14).
* **Suggested repair for OMEGA9:**
  - restate the cited input with `|Im s| ≤ Q_G`, or as Landau–Page for
    real zeros, citing Davenport ch. 14 / MV I Cor. 11.10;
  - add the sentence "only real zeros are used".
* **The m1 inconsistency is also inherited.** OMEGA9 line 61 has
  `κ := max(3κ₀, 1/c₁)`, and line 63 says MV's proof matches "only for
  `κ = 3κ₀`". The same monotonicity sentence repairs it.
* I did not edit OMEGA9.

Stopping for the parent.
