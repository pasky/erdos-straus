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

## 4. Defects

**D1 (MINOR, scope overclaim: "subsumes").**

Lines 1796–1803 (after Thm 10.8) say that Thm `thm:main` "subsumes the previous form of the main
theorem: case (i) … and case (ii) … (Thm `thm:karycap`). It needs no admissible set: the
quadratic-residue and square bases are proof devices". The §6 intro (lines 794–797) adds: "the
conclusions … of Theorem `thm:karycap` are special cases of the bounded-B clause of Theorem
`thm:main`". The changelog repeats the claim.

This is false as stated:
* Thm `thm:karycap` applies to majorants that are `≥ 1` only on **the avoider set in `R_W`**, the
  non-selector QR admissible set.
* v2's case (ii) was stated "with the quadratic-residue base `R_{W₀(B)}`" as the architecture's
  admissible set.
* Thm 10.8, from KARY2 Cor 6.1, needs `ν ≥ 1` on **all** of 𝒜.

So `R_W` was a hypothesis-weakening admissible set for karycap, not only a proof device. Case (i)
is subsumed: Cor `cor:dominant`'s `R` is selector plus family classes. Case (ii) is subsumed only
for whole-avoider majorants.

Fix:
* restrict "subsumes" to whole-avoider (selector-admissible) architectures;
* say that the `R_W`-restricted form of karycap is not implied by Thm 10.8 and remains separate;
* in §6, write "for CRT-majorant architectures with a selector admissible set";
* the "proof devices" phrase should apply to `R_W^□` only.

**D2 (MINOR, prime-size hypothesis weakened in two places).**

Thm 10.8 needs **every prime of every modulus of 𝒢** to be `≤ N^A`. Def `def:arch` (A3) bounds only
the *slice* primes. The prime-slice small part `q₀` is unbounded there, and so is a selector
modulus `P`.

The following sentences then overclaim:
* line 368: "in this form the main theorem … needs no admissible set at all";
* lines 1800–1803: "every CRT-majorant architecture (Def `def:arch`) for such a family, with a
  selector admissible set, saves at most …";
* lines 2549–2552 and 2614: large multipliers are inside Thm 10.8 because it "bounds the level
  through `Σ|a_i| < N` alone".

Fix: add "with all primes of the family (multipliers and selector primes included) `≤ N^A`" in
these places, or strengthen (A3) to say so. Also add Q1's qualifier, "multiplier conditions that
are themselves classes of the four types".

**D3 (MINOR, notation clash in the 3/4 note).**

`es-threequarter-note.tex` line 1337 says "`G ≤ P(G)^{1+B}` with B fixed (here `B < 1/120`)".
In this note B already means the large constant `B = B(κ,D) ≥ B₀` in `y = Bt³`
(lines 116 and 1006). A reader of the note will read "here B < 1/120" as contradicting
`B ≥ B₀`.

Fix: use another letter, e.g. "`G ≤ P(G)^{1+β}`, β fixed (here `kℓ ≤ ℓ^{1+2κ}`, so
`β = 2κ < 1/120`)".

**D4 (MINOR, inclusion list contradicts Rem `rem:L2vsmain`).**

"What the class contains" (line 1844) lists "the sequential, Λ² and Selberg-type majorants of
Sections 4–12". Several of these are majorants only of `𝒜 ∩ R_W`:
* Thm `thm:gapped` and karycap;
* the TW2 `g²` of §12.

Rem `rem:L2vsmain` explicitly does *not* claim the TW2 case. The sentence is inherited from KARY2
§6's list.

Fix: append "when they are `≥ 1` on the whole avoider set".

**D5 (NIT, exclusion item 6 heading vs body).**

The heading reads "Other class types, including non-selector admissible sets". The body only
discusses admissible sets that exclude classes failing (a). Fix:
* state generally that any admissible set not expressible by selector classes has an uncontrolled
  `log(Q₀/|R|)` (Rem `rem:Rterm`; ET §6 3(iii));
* note the one exception now in the paper: `R_W` for fixed-B ℛ(M) families, Thm karycap (cf. D1).

**D6 (NIT, citations and wording).**
1. Line 2541: "Under bounded B it is excluded (Thm `thm:Bcapall`)". The exclusion of
   `(log N)^{3/4}ω(N)` gains is the bounded-B clause of Thm `thm:main`; Thm 10.7 is the
   majorant cap. Cite Thm `thm:main`.
2. Abstract line 45: "a family of forced congruence classes". The family also contains the
   non-forced selector classes. Add "(and selector classes)" or say "of the classes below".
3. Add the keep-in-sync comment for the hard-coded cross-paper numbers (Q3).
4. Changelog: "§5 (dominant prime)" should be §6, and there are 4 underfull boxes, not 3 (§1).
   This is cosmetic and does not affect the papers.

## 5. Verdict

**MINOR REVISION.** The mathematics transcribed from KARY2 is faithful:
* Lemmas 10.2–10.5 and Thms 10.6–10.8;
* Thm 10.8's alternative coarsening via Cor `cor:budgetlevel`, which I checked and which is correct.

The scope statements for the coefficient sum, whole-avoider ν, `N^{O(1)}` primes, the four types,
the `(log log)^{3/4}` loss, ElT Prop 1.4 and the large sieve are correct in all the main
statements.

Both papers compile clean, and the attribution paragraph is intact.

D1 and D2 must be fixed before merge. Each is a one-sentence rescoping of a subsumption or coverage
claim. D3 (3/4 note) should be fixed as well, because that note is the externally visible one.
D4–D6 are optional polish.

On the author's questions:
* Q1: confirm, with D2's qualifiers;
* Q2: correct as scoped;
* Q3: fine, add a sync comment.
