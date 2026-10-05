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
