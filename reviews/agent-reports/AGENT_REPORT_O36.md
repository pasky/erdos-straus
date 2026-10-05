# AGENT_REPORT_O36 — sieve-limits note v4, 3/4-note sharpness remark, README

Branch `side-agent/sieve-paper-v4` (main merged in after (D)26 landed). Not merged
into main. Commits: a42f68b, 3380b61, c0ef413, fd0cbf9, d1d0808, 7288bde, af9749b,
afabbab (+ this report). Both papers compile cleanly with pdflatex (sieve-limits:
62 pp., one 1.3pt overfull hbox in §15; 3/4 note: none).

## Provenance warning for the referee

* §10's changes were written by me directly from EXCEPTIONAL_KARY3.md §§1–4.
* **The two new sections §14 (large sieves, prime laws, interval counts) and
  §15 (tuple counts, truncated weights) were drafted by two subagents** from
  LS, LS2, PL, IF, TU, TU2, KA3 §§5, 7 and DISCOVERIES (D)19–(D)25. I wrote the
  §14 hybrid subsection (IF2, (D)26) myself. I checked the drafts only by spot
  checks: the statements of LS Thm 3.1 and IF Thms 2.2/2.5 against the sources,
  the IF2 Thm 5.2 proof, and all theorem headers and labels. I did not re-derive
  every statement of §§14–15. These two sections need the most scrutiny.

## paper/sieve-limits-note.tex (v3 → v4)

**Title/date:** version 4.

**Abstract:** rewritten. The main cap is `O_A((log N)^{3/4})` with no B (the v3 `(log log N)^{3/4}` is
removed). New tools: local weight `Z_y` + Shiu in progressions; Elsholtz–Tao §7 uniform in k, with
slips. New coverage: large sieve, Gallagher, prime majorants, interval counts ≤ N/2, tuple order. New
reductions: hybrids → combinatorial hypothesis; super-polynomial frequencies need sparsity. Forced
zeros / TC^alt.

**§1 intro:**
* The document list now has 18 entries (KA3, LS, LS2, PL, IF, IF2, TU, TU2 added) and the review list
  has 20 (KA3rev, LSrev, LS2rev, LS2revb, PLrev, IFrev, IF2rev, TUrev, TU2rev added).
* New sentence: some statements were added after review and checked by the coordinator only.
* Attribution: Case A now uses ElT Prop 1.4, Thm 7.1, Cor 7.4 and (7.10). Only the uniformity of
  (7.10) is re-derived. `Z_y` is described as an elementary device, no reference known.
* Results list rewritten. Item 1 is the new main theorem. Item 2 adds the local-weight tool. Item 4
  says the Λ² caps are superseded for all r, the middle range included. New items 6 (§14) and 7 (§15).
  Item 8 is the new exclusions summary.

**§10 (sec:noB):**
* Intro paragraph: the first moments come from KA3 (review KA3rev, all SOUND). The labels rest on the
  KA2/KA framework as reviewed (KA3's "PROVED given K2/EK as reviewed" proviso).
* The old Lemma `lem:firstnoB` (KA2, `(log y)^3(log log y)^3`, Rankin + Cauchy–Schwarz sketch) and the
  remark after it are **replaced** by:
  * a definitions paragraph (Γ = 1∗h, `Z_y`, `S_y`);
  * Lemma 10.4 `lem:localweight` (KA3 L2.1, (2.1′)), full proof;
  * Lemma 10.5 `lem:Zmoments` (KA3 L2.2), full proof;
  * Lemma 10.6 `lem:smoothR` (KA3 L2.3), full proof via Shiu;
  * the three ElT §7 inputs, with (7.10) as display `eq:ET710`;
  * Remark 10.7 `rem:ETslips`: uniformity in k and the two slips (square q; the missing reciprocity
    sign for q > kA). Cites KA3 §3 and KA3rev's uniformity check, steps 3 and 5;
  * Lemma 10.8 `lem:smoothA` (KA3 L3.1), full proof with the split `r ≷ K^{1/4}`;
  * Lemma 10.9 `lem:firstnoB` (KA3 Cors 2.4, 3.2, 3.3 + KA2 Lemmas 3.3, 3.3′): `𝔐(y) ≤ K₃′(W)(log y)³`.
    Label: Case A proved mod Prop 1.4 + §7. Bounded-B clause kept (only Prop 1.4);
  * Remark 10.10 `rem:rankinloss` (Assessment): where v3 lost the factor; EVIDENCE numerics.
* Theorem 10.12 `thm:noBcap`:
  * cap `Cλ^{3/4}`, with `s₁ = λ^{1/4}` in place of `λ^{1/4}(log λ)^{−3/4}`;
  * the proof ledger is updated (linear block, primes above `e^λ`);
  * new paragraph comparing with v3; W unchanged;
  * header label: Case A mod ElT Prop 1.4, Thm 7.1, Cor 7.4, (7.10); the "only external input is
    Shiu" clause applies when there are no Case-A classes.
* Theorem 10.13 `thm:Bcapall` is kept: it needs only ElT Prop 1.4. The text after it is updated.
* Theorem 10.14 `thm:main`:
  * `s ≤ C_A(log N)^{3/4}` for every family, and no ω(N) → ∞ gain;
  * the bounded-B clause is dropped (now redundant);
  * the proof uses Theorem 10.12 only, with `λ = (A+2)log N`;
  * the sync comment is updated;
  * the paragraph after it replaces the "(log log N)^{3/4} irrelevant / not excluded" text with "the
    gap is now closed".
* "Not transferred" paragraph → "Not covered by Theorem 10.14 itself, but capped in §14" (large sieve
  via duality; interval counts ≤ N/2).

**§7 Remark `rem:LS`:** adds a pointer to Thm 14.2 for mixed/composite settings.

**§12 (Selberg):**
* Remark `rem:L2vsmain` rewritten. KA3 Lemma 7.1 says TW2/TW4's admissible g is ≥ 1 on the avoiders
  of 𝓕 itself; the fibre law and base are proof devices. So g² is a whole-avoider majorant of level
  ≤ λ, and every Λ² cap (Thms twoprimecap, rprime, noB, uniformity) is superseded as a cap by
  `CA₀^{3/4}L^{3/4}` for all r, with or without B.
* Flagged: KA3 Lemma 7.1 came after review and was checked by the coordinator only.
* **Referee check:** v3 had said "for g² ≥ 1 only on avoiders in R_W, as in TW2 §3, we do not claim
  this". I checked TW2 Setting 3.0 / Thm 5.1 ("every g ∈ V_{λ/2} with g ≥ 1 on the avoiders of 𝓕"),
  which agrees with KA3 L7.1, so the v3 caveat was over-cautious.
* Middle-range paragraph after Thm `thm:noB`: open only for the Λ² mechanism, not as a cap.

**New §14 `sec:LS`, "Large sieves, prime laws and interval counts" (subagent draft + my §14.x hybrids):**
* Duality: Thm 14.1 `thm:LSdual` (LS Thm 2.1/Cor 2.2, standard), with Rem 2.5 and Prop 2.6 in text.
* Large-sieve cap: Thm 14.2 `thm:LScap` (LS Thm 3.1/Cor 3.2 + KA3 §4.3: `C_A(log N)^{3/4}`; supersedes
  rem:LS).
* Prime slices: Thm `thm:LSslice` (LS Thm 4.1).
* Comparison measure and its consequences:
  * Lemma `lem:compmeas` (LS2 L1.1, 1.2);
  * Thm `thm:hybrid` (LS2 Thm 2.4/Cor 2.5);
  * Thm `thm:LSprimes` (LS2 Thm 3.1).
* Larger sieve:
  * Thm 14.7 `thm:gallagher` (LS2 Thm 4.3, unconditional, `26 log log N + C`);
  * Thm `thm:compkernel` (LS2 Thms 4.2, 9.1, Prop 9.2).
* What (E1) needs:
  * Prop `prop:E1` (LS2 Props 5.1–5.2);
  * Conjecture 14.10 `conj:HLS` (H_LS∞);
  * Thm 14.11 `thm:band` (LS2 §8).
* Prime majorants:
  * Thm 14.12 `thm:PLcap` (PL Thm 3.1, **stated with (log λ)^{3/4}**; the improvement is
    pointer-level per KA3 §4.3);
  * Cor `cor:PLmethods`;
  * Prop `prop:finiterange` (LS2 Prop 6.1).
* Interval counts:
  * Thm `thm:IFminorant` (IF Thm 2.2, full proof);
  * Cor 14.16 `cor:IFcap`;
  * Thm `thm:IFbudget` (IF Thm 2.5);
  * the hybrid gap.
* **Subsection §14.x `sec:hybrid` (mine, from IF2 and (D)26):**
  * definitions;
  * Lemma 14.18 `lem:signrule` (IF2 L3.1 + Ex 3.2);
  * Cor 5.1 in text;
  * Hypothesis `hyp:Flat`;
  * Thm 14.20 `thm:hybridcap` (IF2 Thm 5.2, PROVED implication conditional on Flat, stated with
    `(log log N)^{3/4}` as in the source). It is followed by an "observation of this note,
    pointer-level, not reviewed" that the black-box use gives `C(log N)^{3/4}` with Thm 10.12;
  * Hypothesis `hyp:SPW`;
  * Prop 14.22 `prop:SPW` (IF2 Prop 9.1 + Lemma 9.3);
  * EVIDENCE (LPs) and the open items.
* Subagent-flagged doubts to check:
  * "proved via Theorem 10.12" with `Cλ^{3/4}` is used for IF Thm 2.5 and LS2 Thms 2.4/4.2/9.1 and
    L1.1. KA3 §4.3 lists only LS Thm 3.1, IF Cor 2.3 and PL, but LS2's update note and (D)24/(D)25
    cover the rest.
  * The new bibitem Vaaler (Bull AMS 12, 1985) is cited for Selberg's minorant.

**New §15 `sec:TU`, "Tuple counts and truncated weights" (subagent draft):**
* TU material:
  * Lemma `lem:shiftform` (TU L1.3);
  * Hypothesis `hyp:TC`;
  * Thm `thm:TCbrun` (TU Thm 2.1, Cors 2.2–2.3; proved implication);
  * Prop `prop:TCrange` (TU Props 2.4, 4.2);
  * Def `def:mixed`;
  * Thm `thm:truncslice` (TU Thm 3.1);
  * Cors `cor:orderslice`, 15.8 `cor:classorder` (TU Cor 3.4 + KA3 §4.3; **two-line proof written by
    the subagent; KA3 gives this only as a pointer, unreviewed**);
  * Prop `prop:fixedshift`.
* KA3 §5 material:
  * Def `def:trunc`;
  * Thm 15.11 `thm:trunc` (KA3 Thm 5.1, sketch);
  * Cors 15.12 `cor:primeorder`, 15.13 `cor:boundedr` (with the scope warning). I added the Case-A
    "proved mod ElT" proviso to these three headers.
* Prop 15.14 `prop:blocksparse` (TU2 Prop 7.1), kept **relative to KA2 Thm 5.1, with (log λ₀)^{3/4};
  removal not checked**.
* Lemma 15.15 `lem:packing` (KA3 L7.2, full proof; flagged post-review, coordinator-checked) and the
  window `eq:window`.
* TU2 material:
  * Lemma `lem:forms` (TU2 L1.1, Cor 1.2);
  * Thm `thm:forcedmass` (TU2 Thms 2.1–2.2);
  * Cor `cor:TCexcess` (necessary condition; that literal TC_θ is false is an Assessment);
  * Hypothesis `hyp:TCalt`;
  * Thm 15.20 `thm:euler` (TU2 Thm 4.1/Cor 4.2, proved implication);
  * Cor 15.21 `cor:prime23` (TU2 Cor 6.1), with an Assessment on the needed level.
* §15 "What is open" list.
* Doubt flagged by the subagent: the wording after `lem:packing` ("closing the window from the literal
  hypothesis would require a better level cap") is meant to match (D)24's "cannot be closed from it
  alone".

**§16 `sec:excluded`:** rewritten, now 8 items:
1. large sieve at super-polynomial frequency levels;
2. bad composite larger-sieve kernels;
3. cancellation above modulus N/2, with hybrids/Flat/SPW (IF2 included as instructed);
4. weights < 1;
5. partial-avoider majorants (PL, Prop 6.1, the open "ν ≥ 0 only at primes ≤ N");
6. non-CRT input (tuple counts, the class-order window);
7. other class types; (b) is now `≪ (log y)^3`;
8. primes beyond N^{O(1)} (what is covered without the bound).

The closing paragraph says the exact exponent is settled for Thm 10.14 and is pointer-level for the
prime-measure results. The "No longer excluded" paragraph now says "compared with version 2" and adds
a "New in this version" list. The external-input sentence is updated. After Lemma
`lem:balancedsupply`, "up to (log λ)^{3/4}" became "with the same cap".

**§17 `sec:open`:**
* The list is rewritten as (i)–(vi): class types; partial majorants; super-polynomial LS / kernels;
  direct counts or hybrids above N/2 (Flat/SPW); non-CRT tuple counts (TC^alt) and the class-order
  window; primes beyond N^{O(1)}.
* "Gone since version 2/3" paragraphs.
* "Exact exponent without B" is now settled (the shifted-smooth Ψ bound is not needed, still open).
* New "Constants" paragraph.
* The paragraph "Removing B for general majorants … loses (log λ)^{3/4}" is deleted.
* H_MS, Conj kary, Prop twinconditional, sparse NS and non-CRT counts are unchanged.

**Bibliography:** added KA3, KA3rev, Gallagher, IF, IFrev, IF2, IF2rev, LS, LSrev, LS2, LS2rev, LS2revb,
PL, PLrev, TU, TUrev, TU2, TU2rev, Vaaler.

## paper/es-threequarter-note.tex

The remark "the ceiling is a theorem for this architecture" (≈ l. 1321–1350):
* It now cites KA2 Cor 6.1 / Rem 5.4, **KA3 Cor 4.2**, and SL Thm 10.14 / Rem 10.15 (was 10.8 / 10.9;
  the sync comment is updated).
* The saving is `≤ C(log N)^{3/4}` with no condition on moduli. A parenthetical notes that the note's
  atoms (β < 1/120) were already covered by KA2 Thm 5.2 and that the general `(log log N)^{3/4}` is
  removed in KA3. This replaces "… and ≤ C(log N)^{3/4}(log log N)^{3/4} in general".
* New sentence: no ω(N) → ∞ gain is possible, and the same cap holds for CRT-admissible large sieves
  at polynomial level (SL Thm 14.2).
* The "Not covered" list is updated, citing SL §16. The Case-A input is ElT Prop 1.4 + §7; ℛ(M) and
  selector classes use only Shiu.
* Bibliography: KA3 added; SL is now version 4.

## paper/README.md

* New top entry for sieve-limits v4: contents, ledger items, ElT dependence, "not yet refereed".
* The 3/4-note entry points to the updated sharpness remark.

## Not done / for the parent

* Not included: anything not on main. IF2 was included after (D)26 landed, per the parent's note.
* The 1.3pt overfull box in §15 is left as is.
* DISCOVERIES (D)24 cites "§§7–8 (Lemmas 7.1, 7.2, 8.1)", but the KA3 file has no Lemma 8.1 (§8 is
  numerics). The note cites KA3 §§6–7 and Lemma 7.1. The ledger wording may need a fix.

## Response to referee R36 (reviews/sieve-limits-note-review-v4.md; minor revision)

All points addressed; both papers recompile (sieve-limits: no undefined refs; the 1.3pt overfull
box in §15 remains; numbering of Thm 10.14 / Rem 10.15 / Thm 14.2 / §16 unchanged, so the 3/4
note's cross-references stay valid). Commits ffe4c02, ef99ede, e61954a (+ compile fix 9f393c0),
acae6a9, R36 m18 commit, b6ce75e (KARY3).

* **M1** — abstract: the lossless cap `O_A((log N)^{3/4})` is now claimed only for polynomial-level
  large sieves (twisted/multiplicative/hybrid/fibrewise), interval counts ≤ N/2 and bounded-order
  tuple input; prime order k gets `O_A((log N)^{3/4}+k log log N)`; the large sieve for primes and
  prime-only majorants get `O_A((log N)^{3/4}(log log N)^{3/4})` (lossless only at pointer level).
  Intro item 6 likewise (LSprimes and PLcap with the loglog proviso). §16 "New in this version" and
  §17 "Gone since version 3" carry the same provisos.
* **m1** — §14 preamble: "no fatal defect; the IF review found one major scope overclaim (hybrids),
  repaired by restriction; other repairs minor".
* **m2** — Gallagher sketch: χ² = (p+1)/(p−1) ≤ 2 at odd p ≤ W, ≤ 7 at p = 2; Mertens and
  𝔏 log W = o(1).
* **m3** — substitution sources: KA3 §4.3 for LS Thm 3.1 / IF Cor 2.3; LS2's update note and (D)24 for
  LS2; IF Thm 2.5 "checked in this note".
* **m4** — Thm 14.6 header: "Case A as in Theorem 14.12".
* **m5** — Prop 14.9(1): `max(λ₀, 2rA log N + λ(Q₀))` restored.
* **m6** — IF2 Cor 5.1 in text: family primes ≤ N^A added; cited as "[IF2, Cor 5.1] with Theorem 14.17".
* **m7** — Thm 14.5 type (ii) and Thm 14.17: projection to the family period first; Thm 14.17 case
  split (s ≤ log(2+12c), else T_> < N/12) added. Prop 14.22: Vaaler-bound caveat (quoted from review,
  numbering not re-checked) and bounded Δ₀ noted. (Sp) wording softened in §14 ("needs something
  like"/"family-specific input such as"), and in the abstract and §16 item 1 (m17). Thm 14.12 sketch:
  "the base is the set of unit squares, which avoids every W-smooth class by Lemma 10.2" (non
  sequitur removed).
* **m8** — §15 opening cites the non-CRT item via `\label{it:nonCRT}` (item 6).
* **m9** — "for θ > 3/4" inserted.
* **m10** — Cor 15.8: k ≥ 1; header "proof given here; KA3 §4.3 only points to it; given KA/KA2 as
  reviewed".
* **m11** — Cor 15.13: hypotheses spelled out (family primes ≤ N^A, W fixed, term types, λ₀ = A log N).
* **m12** — window: "for family moduli ≤ N^A … except as narrowed by Prop 15.14"; the ledger
  inspection claim marked Assessment, "for k ≤ L³". KARY3 §0 table and §7 item 1 reworded to
  "would require a better level cap" (separate commit b6ce75e). DISCOVERIES (D)24 still says "cannot be
  closed from it alone" — **for the parent** (ledger is main-owned; I did not edit it).
* **m13** — "tuples that are not pure class −1 (heuristically, multi-form tuples)".
* **m14** — open list: literal TC_θ / TC^𝔄_θ on (2/3,1) and θ = 1; removing (log λ₀)^{3/4} from
  Prop 15.14. ℓ₀ in Cor 15.21 defined (τ(A_ℓ²)/ℓ ≤ 1/4 for ℓ ≥ ℓ₀). Def 15.10's notion renamed
  "(λ₀,k)-mixed over W".
* **m15** — Rem 12.8: the v3 bounded-B half (R_W reading, "still gives … removal of B") deleted; one
  reading remains (whole-avoider Λ² majorants, KA3 L7.1), one "still gives" sentence. §10 "What the
  class contains" no longer lists TW2's Λ² majorants as R_W-only.
* **m16** — Status-labels paragraph: "PROVED for results resting on Thm 10.12 / Lemma 10.9 means given
  the KA/KA2 framework as reviewed".
* **m17** — "the removal of the factor"; item-1 softening; §17 pointer-level proviso for prime-only
  majorants and the k log log N term for prime order.
* **m18** — 3/4 note "Not covered" list ends "…, and the other items of [SL, §16]".
