# PAPERS_V3 — task O16 changelog

Branch: `side-agent/papers-v3` (from main at `9940611`). Commits `2eb4479..6a0b6f9`.
Sources: `EXCEPTIONAL_KARY2.md` (Thm 5.1, Thm 5.2, Cor 6.1, Remark 5.4, §6), its two reviews
`reviews/exceptional-kary2-review.md` and `reviews/exceptional-kary2-review-2.md` (round 2, including the
cosmetic R2-1), and `DISCOVERIES.md` (D)18.

## (1) `paper/sieve-limits-note.tex` → version 3

Compiles clean with 3 pdflatex passes: no undefined references, no overfull boxes. There are four
underfull boxes, all present in v2: three bibliography `\texttt` lines and one body paragraph
(Hypothesis 12.2 / Theorem 12.1).

* **New §10, "The main theorem: every mixture of forced classes, no B"** (`sec:noB`). It is inserted
  after the fixed-B section (§9, retitled "The 3/4 cap for every fixed-B family of classes ℛ(M)";
  `thm:karycap` is unchanged).
  * §10.1 lists where B entered (B1–B3) and notes that the number of prime factors never enters
    (KARY2 §1, Rem 5.3).
  * Def 10.1 introduces the four class types, with selector classes `0 mod p` (not forced) and the
    whole avoider set 𝒜(𝔊) ⊂ ℤ.
  * Lemma 10.2 (no squares; KARY2 Lemmas 2.1–2.2) has full proofs.
  * Lemma 10.3 is the square base `R_W^□` (KARY2 Lemma 2.3).
  * Lemma 10.4: first moments, `(log y)³(log log y)³`, with the bounded-B clause (KARY2 Lemmas 3.1–3.6
    and Cor 3.7). Proof sketch; Case A is **proved mod ElT Prop 1.4**. A following remark gives the
    `(log log)³` source, and the shifted-smooth bound is marked open.
  * Lemma 10.5: second moment and leak (KARY2 Lemmas 4.1–4.3). Proof sketch; no external input.
  * **Thm 10.6** = KARY2 Thm 5.1 (`Cλ^{3/4}(log λ)^{3/4}`, no B). **Thm 10.7** = KARY2 Thm 5.2 (bounded
    B, all four types).
  * **Thm 10.8 (`thm:main`, replaces the old two-case main theorem)** = KARY2 Cor 6.1, with the proof
    (projection, then Lemma `lem:budget` at level (A+2)log N). It records the subsumption of old
    cases (i) and (ii), and that a selector admissible set is the same as adding selector classes.
  * **Remark 10.9** = KARY2 Rem 5.4: the 3/4 note's majorant is literally covered, with B < 1/120.
    It uses the R2-1 wording: selector primes ≤ W are absorbed by the base and those in (W,y] cost
    O(log log y); there is no "smaller R-term" claim.
  * A closing paragraph lists what the class contains and what is "not transferred" (the large sieve,
    per-frequency rounding).
* **Abstract and intro.** The abstract is restated around the new main theorem, with the
  `(log log N)^{3/4}` loss, `(log N)^{3/4}` under bounded B, and ElT for Case A. Results item 1 is
  rewritten. Item 2 gains the square-base and Rankin/Cauchy–Schwarz tools. The internal-document list
  now has nine entries (+KA2), and the review list adds KA2r and KA2r2.
* **Attribution.** The PYY/BGP/Prékopa/Tao paragraph is kept and extended. The §10 inputs are
  standard (Mordell, Rankin, Shiu, small-divisor domination cf. Landreau). ElT Prop 1.4 is
  "published, not re-proved". The no-square property is "in the spirit of" the Mordell–Schinzel
  obstructions quoted in ElT; Schinzel is not used or checked.
* **New bibliography entries:**
  * KA2, KA2r, KA2r2;
  * Landreau, Bull. LMS 21 (1989) 366–368, checked against Crossref.
* **§6 (dominant prime).** The intro now says that for architectures the conclusions are special
  cases of Thm 10.8's bounded-B clause (B = C).
* **§3 (architecture).** One sentence was added: selector R = selector classes, so Thm 10.8 needs
  no admissible set.
* **§11 (campaign).** The 3/4-note subsection now points to Rem 10.9.
* **§12 (Λ²).** Results item 4 and Remark `rem:L2vsmain` say that without B, Thm 10.6 supersedes the
  Λ² caps, but only for majorants ≥ 1 on the *whole* avoider set. For `g² ≥ 1` only on avoiders in
  `R_W` (the TW2 setting) this is explicitly not claimed.
* **§14 "What the theorems exclude".** Rewritten to give exactly the (D)18 / KARY2 §6 list:
  1. the large sieve beyond prime slices;
  2. inter-frequency cancellation;
  3. weights < 1;
  4. majorants ≥ 1 only on [1,N], the exceptional set or exceptional primes (the mean side of the
     prime law is not claimed);
  5. non-CRT input;
  6. other class types, via properties (a)–(c), including non-selector admissible sets and the
     Schinzel pointer (unchecked);
  7. primes beyond N^{O(1)}.

  Two additions follow the list. The `(log log N)^{3/4}` gap is open without B and excluded under
  bounded B. A "No longer excluded" paragraph covers unbounded B, (a,D)/Case-A without a dominant
  prime, mixtures, twins, ω(G), selector admissible sets, and large multipliers.
* **§15 "Open problems".** The list for θ > 3/4 is now (i) other class types or a non-selector
  admissible set; (ii) partial-avoider majorants; (iii) non-CRT, inter-frequency, weights < 1, or the
  large sieve beyond slices; (iv) primes beyond N^{O(1)}. The old "Removing B for general majorants
  [open]" paragraph is replaced by "done (Thm 10.6), loss (log λ)^{3/4}, not log λ as TW4 §11
  predicted". A new open item asks for the exact exponent without B. `H_MS` now "would close (i) for
  forced classes with a bounded-saving admissible set". The Λ² middle-window paragraph now concerns
  only the Λ² method.
* **Date line:** "version 3".

Judgement call for the parent: I moved "large multipliers" (old §13 item 7, old open item (ii)) to
"no longer excluded". The reason is that Cor 6.1 allows arbitrary moduli, and the level is
controlled by `Σ|a_i| < N` via projection plus Lemma 2.9, so multiplier conditions of the four types
are inside. Please confirm.

## (2) `paper/es-threequarter-note.tex`

The only change is in §9: the remark "scope of the ceiling" (the heuristic caveat) is replaced by
"Remark (the ceiling is a theorem for this architecture)". It cites
`[SL, Thm 10.8, Rem 10.9]` and `[KA2, Cor 6.1, Rem 5.4]`, and states:
* `ν_X = S_y Q_r(H_X)` is a majorant of the whole avoider set of atoms plus `{0 mod p : p ≤ y}`;
* the atoms are ℛ(kℓ)-classes with B < 1/120;
* the primes are ≤ X ≤ N and `T_abs ≤ N^{1/2}`.

It then gives the exact scope (the method form, `C(log N)^{3/4}` under bounded B, the `(log log)^{3/4}`
general loss) and the seven exclusions. The ElT proviso is irrelevant here, since this case needs
only ℛ(M) and selector classes. It is labelled internally reviewed only, and the remark says
"nothing used in the proof of Thm main". Two bibliography entries were added (KA2, SL). The
section title and all other text are unchanged. It compiles clean with 3 passes.

The theorem numbers 10.8 and 10.9 are hard-coded in the 3/4 note. They must be updated if the
sieve note is renumbered.

## Round 2: referee `reviews/papers-v3-review.md` (branch `side-agent/review-papers-v3`)

All defects are applied. Both papers recompile clean (3 passes): no undefined references and no
overfull boxes. The sieve note's underfull boxes are the same ones as in v2. Its labels are
unchanged: `thm:main` is 10.8 and `rem:TQcovered` is 10.9.

* **D1 ("subsumes" overclaim).** Old case (ii) (`thm:karycap`) is now said to be subsumed only for
  whole-avoider majorants. The `R_W`-restricted form of karycap is not implied by Thm 10.8 and is
  stated to remain separate. "Proof device" now applies to `R_W^□` only. The §6 intro is rescoped
  the same way: selector admissible set, ν ≥ 1 on the whole avoider set, family primes ≤ N^A.
* **D2 (prime size).** The full hypothesis, all family primes ≤ N^A (selector primes and the primes
  of the small parts q₀ included), was added in four places:
  * the §3 remark after Def `def:arch`, noting that (A3) bounds only the slice primes;
  * the paragraph after Thm 10.8;
  * "No longer excluded";
  * the open-problems preamble.

  The multiplier item also carries Q1's qualifier: the multiplier conditions must themselves be
  classes of the four types.
* **D3 (3/4 note).** The B-letter clash is resolved: the remark now writes `G ≤ P(G)^{1+β}` with
  `β = 2κ < 1/120`.
* **D4.** "What the class contains" now restricts the sequential, Λ² and Selberg majorants to those
  that are ≥ 1 on the whole avoider set. It names `thm:gapped`, `thm:karycap` and the TW2 Λ²
  majorants as `R_W`-only, with a pointer to Rem `rem:L2vsmain`.
* **D5.** Exclusion item 6 now says that any admissible set not expressible by selector classes
  (or by classes of the four types) has an uncontrolled R-term. The one exception noted is `R_W`
  for fixed-B ℛ(M) families (karycap).
* **D6.**
  1. The bounded-B exclusion of `(log N)^{3/4}ω` gains now cites the bounded-B clause of
     Thm `thm:main`.
  2. The abstract says "(and selector classes `0 mod p`)".
  3. A keep-in-sync comment for 10.8/10.9 was added in both notes. The 3/4 note now leads with the
     stable `[KA2, Cor 6.1, Rem 5.4]`, with `[SL, Thm 10.8, Rem 10.9]` as "see also".
  4. This changelog: "§5" is corrected to §6, and the underfull-box count is corrected.

The referee's optional observation (that the `R_W`-restricted Thm 10.6 is probably within reach)
was **not** added, as the referee advised.
