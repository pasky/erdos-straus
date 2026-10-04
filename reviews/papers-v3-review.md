# Referee report: papers v3 (branch `side-agent/papers-v3`, head `999393c`)

Subject: `paper/sieve-limits-note.tex` v3 (new §10, main theorem = KARY2 Thm 5.1/5.2/Cor 6.1),
the new sharpness remark in `paper/es-threequarter-note.tex` §9, and the changelog
`reviews/agent-reports/PAPERS_V3.md`.
Sources checked against: `EXCEPTIONAL_KARY2.md` (all), `reviews/exceptional-kary2-review.md`,
`reviews/exceptional-kary2-review-2.md` (incl. round 2, R2-1), `DISCOVERIES.md` (D)18,
`EXCEPTIONAL_THETA.md` §5.6/§6, `reviews/sieve-limits-note-review-v2.md`,
`reviews/novelty-audit-2026-10.md`, and the v2 text (`git show HEAD:paper/sieve-limits-note.tex`).
Reviewer branch: `side-agent/review-papers-v3`.

## 1. Compilation and cross-references

* Both papers compile clean with 3 `pdflatex` passes (in `/tmp`): 0 warnings, no undefined
  references, no overfull boxes. The 3/4 note has no underfull boxes.
* The sieve note has 4 underfull boxes, not 3 as the changelog says. Three are bibliography
  lines. The fourth is in the body (lines 2008–2014, badness 2050, "Under Hypothesis 12.2,
  Theorem 12.1 …"). It was already present in v2 at lines 1684–1690. It is cosmetic.
* The hard-coded numbers are correct for v3. The `.aux` gives `sec:noB` = §10,
  `thm:main` = Theorem 10.8 and `rem:TQcovered` = Remark 10.9. These match
  `[SL, Theorem 10.8, Remark 10.9]` in the 3/4 note.
* Changelog nit: the dominant-prime section is §6, not "§5".

## 2. Faithfulness of §10 to KARY2 (scope checks)

Checked item by item. Everything below is **faithful** unless listed in §4.

* **Coefficient-sum form.** Thm 10.8 (`thm:main`) has the bound `N·Eν + Σ|a_i|` with
  `Σ|a_i| < N`, as in Cor 6.1. "What the class contains" and exclusion item 2 state that the
  theorem needs `Σ|a_i|` rounding. The large sieve and NONCRT per-frequency rounding are listed as
  not transferred, as KARY2 §6 requires after review 2 D3.
* **ν ≥ 1 on all of 𝒜 ⊂ ℤ.** This appears in Thm 10.6, Thm 10.8, Def 10.1 ("**all** integers"),
  Results item 1 and exclusion item 4. Item 4 includes the review-2 D4 additions:
  * `𝒜 ∩ [1,N]` and the exceptional set;
  * exceptional primes beyond a selector;
  * "mean side capped, BV accounting open, not claimed".
* **Primes ≤ N^{O(1)}.** Thm 10.8 requires "every prime dividing a modulus of 𝒢 ≤ N^A", as in
  Cor 6.1. Exclusion item 7 restates this. See D2 for where the paper weakens it to "slice primes".
* **Class types.** Def 10.1 matches KARY2 Def 2.0. Selector classes are a fourth type and are
  marked not forced. Lemma 10.2 is a faithful, complete transcription of KARY2 Lemmas 2.1–2.2:
  I re-checked the Jacobi computation in (3), including `r` even and `r_o = 1`. Lemma 10.3 matches
  KARY2 Lemma 2.3, with `P_W` now defined and the selector case of (1) included.
* **Thm 10.8 proof.** It does not follow KARY2's route (Lemma 2.9 at `λ = Λ₀ + log T̄ + S` and a
  case split). It uses projection, then Lemma `lem:budget` at `λ = (A+2)log N` with
  `Eν' ≤ Eν + N^{−1}`, as in Cor `cor:budgetlevel`. I checked this route:
  * `log(1/Eν') ≥ min(S, log N) − log 2`;
  * the cap at level λ gives `min(S, log N) < log N` for `N ≥ N₀`, so `min = S`;
  * Lemma `lem:budget` uses only `log ℓ ≤ Λ₀` for the charged primes (here `> W`), and after
    projection every such prime is a family prime `≤ N^A`.

  The route is correct and avoids the ET side-note issue (`s` vs `S`). It also resolves the
  v2-review D2 (non-family primes) by the projection to `Q`.
* **(log log)^{3/4} loss without B.** The abstract, Results 1, Thm 10.6, the remark after
  Lemma 10.4, the paragraph after Thm 10.8, the paragraph after the exclusions, and the open
  problem "exact exponent" all agree with KARY2 §6 item 1 and Rem 3.8. They say the loss comes only
  from smooth-dominated moduli. A gain `(log N)^{3/4}ω`, `ω ≤ (log log N)^{3/4}`, is not excluded
  for unbounded B; it is expected not to exist, and that is open. Under bounded B it is excluded.
  "No power of log log N can be gained" (abstract) is scoped to bounded B, as review 2 asked.
  Thm 10.6's ledger (`s₁ = λ^{1/4}(log λ)^{−3/4}`, `16K₃·16^i + 4`, singletons
  `(8/3)K₃λ^{3/4}(log λ)^{3/4}`) matches KARY2 §5.
* **ElT Prop 1.4.** The status is correct everywhere:
  * "proved mod" for Case A in Lemma 10.4 and Thms 10.6, 10.7 and 10.8;
  * Lemma 10.5 (second moment/leak) says "no external input, Case A included", as KARY2 Lemma 4.3
    does;
  * "families without Case-A classes use no external input" appears in Thm 10.6 and §14;
  * attribution: "published and not re-proved here".
* **Large sieve.** Only the prime-slice large sieve is claimed: Remark `rem:LS`, Cor `cor:sliceCap`
  and the 2/3-note subsection. §10's "Not transferred", exclusion item 1 and Results 6 say that
  nothing extends to mixed families or composite moduli. This is faithful to KARY2 §6 and
  ET §6.1 item 8.
* **Remark 10.9** matches KARY2 Rem 5.4:
  * it uses the R2-1 wording and does not repeat the "smaller R-term" claim, which survives
    uncorrected in KARY2.md Rem 5.4 itself; the paper is the better text;
  * it uses `Q_r(H) = binom(H−1,r) ≥ 0` for even r and `Q_r(0) = 1`, and I checked these.

  It adds `T_abs ≤ N^{1/2}` and "primes ≤ X ≤ N". I checked both against the 3/4 note
  (eq:transfer and the proof of Thm 8.2, `log N ≥ C₀t⁴`): its bound sums ν_X over **all**
  integers `n ≤ N`, not over primes, so it is a whole-avoider majorant.
* **Attribution paragraph.** It is intact. The diff only appends to it; the PYY/BGP/Prékopa/Tao
  sentences are unchanged. The additions match the sources and the novelty audit:
  * Landreau is "cf.";
  * ElT is published and not re-proved;
  * the no-square property is "in the spirit of Mordell–Schinzel as quoted in ElT", and
    "Schinzel not used or checked" appears after Lemma 10.2 and in exclusion item 6 (KARY2 D6).

  The Landreau reference (Bull. LMS 21 (1989) 366–368) is plausible. I did not re-check it
  against Crossref.

## 3. The author's open questions

**Q1. Do multiplier conditions move to "no longer excluded"? Yes, with two qualifiers.**

The old item (v2 §14 item 7, ET §5.6(b) and §6 3(ii)) covered prime-slice conditions
`n ≡ b (mod q₀ℓ)` with a small part `q₀ ≫ ℓ` that the slice level leaves free. These are forced
classes of the four types: ℛ(kℓ)-classes in the 3/4 note, and `(a,D)`-classes with large `a`. So
they are members of 𝒢 with arbitrary moduli.

Thm 10.8 has no level or modulus-size hypothesis. Thm 10.6 charges every prime `> W`, and the level
`(A+2) log N` comes from `T < N` together with family primes `≤ N^A`, via projection and Lemma
`lem:budget`. The cost that ET could not lower-bound is therefore irrelevant: the cap holds whatever
the method pays.

Two qualifiers belong in the "no longer excluded" sentence (§14) and in open problem (i)'s
preamble (§15):
1. the multiplier conditions must themselves be classes of the four types;
2. all their primes, including those of `q₀`, must be `≤ N^A`.

The present wording, "bounds the level through `Σ|a_i| < N` alone", drops (2). See D2.

**Q2. The Λ² supersession claim (Results 4, Rem `rem:L2vsmain`, §15 last paragraph): correct as
scoped.**

A Λ² majorant `g²` with `g ∈ V_{λ/2}` and `g ≥ 1` on the whole avoider set of a four-type family
is a nonnegative CRT combination. Its level is `≤ λ` in Thm 10.6's sense, which charges only
primes `> W`, while TW2 charges all primes. So Thm 10.6 applies verbatim. "Up to powers of log L"
is the right hedge against the `(log L)^{O_r(1)}` of Thms `thm:rprime` and `thm:noB`.

The explicit non-claim for `g² ≥ 1` only on `𝒜 ∩ R_W` (the TW2 setting) is correct and necessary.
KARY2 states Thm 5.1 only for whole-avoider majorants.

*Optional observation, not claimed in any source.* KARY2's proof uses ν only on histories inside
the base `R_W^□`, and `R_W^□ ⊆ R_W` for equal `W`, since a unit square mod `p^e` is a QR mod `p`.
So the R_W-restricted version is probably within reach. It would need its own check (the W of TW2
versus the absolute W of KARY2, and `Q₀`), so do not add it without review.

The same R_W issue makes two *other* sentences overclaim. See D1 and D4.

**Q3. Hard-coded cross-paper numbers (3/4 note → `[SL, Theorem 10.8, Remark 10.9]`): acceptable.**

They are correct for v3 (§1), and the `SL` bibitem pins "version 3", so they stay well-defined
even if a v4 renumbers. Two cheap safeguards are recommended (D6):
* add a `% keep in sync with sieve-limits-note.tex v3: thm:main=10.8, rem:TQcovered=10.9` comment
  next to the citation;
* lead with the stable `[KA2, Cor 6.1, Rem 5.4]`, which the remark already cites.
