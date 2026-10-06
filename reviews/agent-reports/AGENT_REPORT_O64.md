# AGENT_REPORT_O64 — `paper/es-subexp-note.tex` v5

Branch `side-agent/subexp-paper-v5`. Status: CHECKPOINT 1 (for parent / referee review).
Compiles with pdflatex ×2: 51 pp., 0 undefined references, 0 overfull boxes.
ES is not claimed anywhere; labels follow the note's status conventions (extended, see C7).

## v5 change list for the referee

The proof of Theorem 1.1 (exponent 1/4) and §§2–10 are **unchanged** from v4 (refereed R56),
except cross-references (C8). Everything new is in the introduction, §§11–13 and §14.

| # | where | change | source | label in the paper |
|---|---|---|---|---|
| C1 | §11 preamble, (A1)–(A3) | imports three facts of the 3/4 note [TQ]: Lemma 2.2 (distinct unit residues at ℓ, ≤ℓ^{1/3} atoms), Cor 4.3 + Lemma 3.2 (`a t³ ≤ μ_c ≤ C_u t³` for every unit c), Lemma 8.1 + Thm 8.2 (Bonferroni majorant ν_X, its ledger and integer mean). Checks that the atoms are multiplier congruences of W (w=(kℓ+1)/(4uv)) with `kℓ ≤ K_X X ≤ T` for `X=T^{1/(1+ϰ)}`. Note's κ renamed ϰ (κ is Gallagher's constant here). Numbering of [TQ] verified on a fresh compile of `es-threequarter-note.tex`. | CEILINGS_UNIFIED §1–2 | — |
| C2 | Prop 11.1 | Haar lower bound `δ*(T) ≤ e^{−at³}`, so `𝓛³ ≪ log(1/δ*) ≪ 𝓛³(log𝓛)^5`; full proof (fibre product). The md's factor 8 is not needed (the bound holds for every unit c, so after conditioning on n≡1 (24)). | CEILINGS_UNIFIED Prop 1.1 | proved modulo [TQ] |
| C3 | Thm 11.2 (= Thm 1.2) | typical size `#{p≤x: W(p)>T} ≪ π(x)e^{−c𝓛³}`, `𝓛 ≤ c₁(log x)^{1/4}`; full proof (Cases A/B; Page's theorem (11.1) only in Case B). Remark: reproof of the prime case of [TQ], not an improvement; majorant vs minorant asymmetry; two-sided law = Assessment. | CEILINGS_UNIFIED Thm 2.1 | proved modulo [TQ] and Page's theorem |
| C4 | Prop 11.3 | no positive minorant of level `log D ≤ c𝓛⁴` on any fibre with `log Q ≤ T^{0.05}`; full proof through the paper's Lemma 10.2 (level barrier) with big coordinates ℓ∈(X^{1/2},X], `k=⌊2log D/t⌋`, `p*=2X^{−1/3}`. Consequence for Cor 10.7: gap `(log log p)^{1/4}`. | CEILINGS_UNIFIED Prop 4.2 | proved modulo [TQ] |
| C5 | Rem 11.4 | one sieve limit behind 3/4 and 1/4 (Thm 4.1 two-sided order-k limit: planting = Lemma 10.1; binomial extrapolation = [SL, Lemma 8.3]; Bonferroni; level `𝓛·𝓛³`; budgets log N vs log x; [SL, Thm 10.14] for the 3/4 cap). | CEILINGS_UNIFIED Thm 4.1/4.3 | conjunction of proved statements within scopes; Assessment as mechanism |
| C6 | §12 | Lemma 12.1 (pseudorandomness of the planted law, `|E_ρ h| ≤ (4r*)^{k+1}`, = 0 for `|I|≤k`) and Thm 12.2 (Wiener-norm barrier `E B ≤ e^{−c𝓛⁴/log𝓛}Σ|c_i|`) with full proofs; Def of linear certificates, Thm 2.2 and Lemma 2.3 of O15 stated in text; Cor 12.3 (full-orbit uniform linear certificates capped at 1/4; proof sketched, pointer); Siegel-model statement (O15 Thm 3.1); Prop 12.4 (EH-type hypotheses cap at 1/4, = O16 Prop 3.1, full proof); full GRH explicitly *not* covered; scope paragraph (O15 §6). Big coordinate in §12 = whole ℓ-adic component (needed so that additive characters are reduced products; the events read it mod ℓ, so Thm 10.6's `R(x) ≥ μ*` is unchanged). Remark: with the [TQ] atoms η=e^{−c𝓛⁴} (not used, flagged). | POINTWISE_OMEGA15, OMEGA16 §3 | Lemma 12.1 proved; Thm 12.2 mod G+LP+FL; Cor 12.3, Prop 12.4 proved implications, same inputs |
| C7 | §13 | Def unit-class sieve system; Hypothesis LS(C) (conjecture); remarks (Linnik case, `C log T` slack needed, Cramér form false); Thm 13.1 (= Thm 1.5) LS ⇒ `W(p) ≥ exp(c_C(log p)^{1/3}(log log p)^{−5/3})` i.o., full proof via Thm 3.3's quarantine; LS(Φ) variant; dimension count 1/4 vs 1/3; LS beyond linear certificates; other strengths (Cramér, PS_log, main-term forms too strong, light case by BT); Prop 13.2 product sets: (a) with proof (uses Lemma 2.2 Jacobi), (b) mod BDH with sketch + pointer; HL_prod ⇒ only `(log p)^{2±o(1)}`. | POINTWISE_OMEGA16 §§1,2,4,5 | Thm 13.1 conditional on LS, proved modulo NT; Prop 13.2(a) proved, (b) mod BDH |
| C8 | §10 | Cor 10.7: sentence on the `𝓛⁴` improvement modulo [TQ]; Scope paragraph points to §§12–13; Rem 10.9 (heuristic 1/3) points to §§12–13. | — | — |
| C9 | Intro | restructured: Thm 1.1 (unchanged) → Thm 1.2 typical size → Thm 1.3 Haar exponent (lower bound `c𝓛³` mod [TQ], `𝓛³/log𝓛` mod FL) → Thm 1.4 ceiling (both levels) + the `𝓛·𝓛³` reading → "Beyond the ceiling" (Wiener barrier, orbit-uniform cap) → Thm 1.5 (LS ⇒ 1/3) → one-paragraph summary of the picture → Versions (v4, v5 added). Effectivity sentence restricted to Thm 1.1 ([TQ]-based results ineffective). Status conventions: [TQ] (internally proved, not externally refereed), Page's theorem, BDH, "Conditional on LS". Literature: no priority claim for LS. | — | — |
| C10 | Abstract | rewritten for the full story; ends with "all results modulo the cited theorems; the companion note is internally proved but not externally refereed". | — | — |
| C11 | §14 status, bib | new items for §§11–13; Not-claimed list extended (1/3 unconditionally, truth of LS, scopes of Cor 12.3/Prop 12.4); Assessment list extended. Bib: [TQ], [SL], [O15], [O16] (the last two are repository working notes, cited as such). | — | — |

## Points the referee should check (self-identified)

1. **Dependence on [TQ].** Props 11.1, 11.3 and Thm 11.2 rest on an internally proved, not
   externally refereed note. The labels say so; Theorem 1.3's lower bound is also given in the
   FL-only form (`𝓛³/log𝓛`, Thm 4.4), so nothing earlier depends on [TQ].
2. **Thm 11.2, Case B.** Page's theorem (11.1) is quoted from memory as in CEILINGS_UNIFIED
   (Davenport Ch. 20), not re-checked against a PDF; the proof needs only the range
   `q ≤ exp(c₂√log x)` and error `x e^{−c₃√log x}`. The non-coprime terms are bounded crudely by
   `Σ|c_i| log q_i (log x)²`.
3. **§12 big coordinate convention** (C6) differs from §10 (where higher ℓ-digits are small);
   both are legitimate for Lemma 10.2; check that Thm 10.6's proof is indeed unchanged.
4. **Cor 12.3** and the Siegel statement are stated with proof sketches/pointers to O15, not full
   proofs (as the brief allows); Prop 12.4 and Lemma 12.1/Thm 12.2 have full proofs.
5. **Prop 13.2(b)** proof only sketched (pointer to O16 Prop 4.1(b)); BDH cited as [Dav, Ch. 29].

## Not done
* No new mathematics; no numerics re-run (the brief is a writing task).
* Bibliography TODOs of v4 ([ErdosSpencer], [Janson], [FI] numbering) unchanged.

## Self-review (deep reviewer subagent, `review` since main) and repairs
No proof defect found in Props 11.1/11.3, Thm 11.2, Lemma 12.1, Thms 12.2/13.1, Prop 13.2(a);
[TQ] numbering confirmed. Five defects, all repaired:
* P1 Prop 12.4: `N_x` (coprime to *all* moduli) vs `N_{x,q}` was inconsistent. Now `N` = all primes
  `≤x` in H (certificate mass), `N_{x,q}` = those coprime to q, statements centred at `N_{x,q}`;
  averaged statements need allowance `≥ 2log x × #terms` (stated as a hypothesis).
* P2 Siegel paragraph: restored O15's mass caveat (masses differ by `ε|E_ρχ₁| ≤ (4r*)^{k+1}`,
  equal when `s ≤ k`).
* P2 status §14: Thm 1.3 via NT + FL only in the `(log T)³/log log T` form; lossless form needs [TQ].
* P2 intro/abstract: "W(p) = (log p)^{2±o(1)}" replaced by what Prop 13.2 proves (HL_prod ⇒
  `≥(log p)^{2−o(1)}`; product-subset route certifies no more than `(log p)^{2+o(1)}`).
* P3 status conventions + after (11.1): Page's theorem and BDH were recalled from Davenport, not
  re-checked against a source — now disclosed.

## Response to referee R64 (`reviews/es-subexp-note-review-v5.md`, worktree-0017)
All items applied; pdflatex ×2: 51 pp., 0 undefined, 0 overfull, no PDF-string warning.
* **D1** Rem 11.4: majorant bound now cited as [SL, Thm 8.5 and Cor 8.6] via Lemmas 8.3–8.4,
  applied fibrewise, with the proviso `p* ≤ 1/4`.
* **D2** Rem 11.4: scope of [SL, Thm 10.14] added (CRT majorants ≥0 on ℤ, coefficient sum < N,
  family primes ≤ N^A; Case A modulo Elsholtz–Tao §7); [SL] added to the status conventions.
* **D3** sentence after Thm 11.2 on a matching lower bound now tagged "Assessment, not checked"
  and phrased as an expectation.
* **D4** status conventions: results of [O15], [O16], [SL] are labelled "proved *in*" those notes,
  proofs sketched/referenced. Cor 12.3 label: "proved implication in [O15, Cor 2.4], same
  inputs; sketch here"; Siegel statement: "proved in [O15, Thm 3.1], statement only here";
  Prop 13.2(b): "proved in [O16] modulo BDH; sketch below"; §14 item adjusted.
* **D5** Prop 12.4, intro and abstract: BV/EH/GRH enter only through their consequences for the
  unweighted prime counts at the single scale x; multi-scale / `log p`-weighted information is
  outside the framework (pointer to Scope).
* **D6** §13 (i): "implies LS(C′) for some C′ = C′(C, c₀)"; intro product-set ceiling marked
  "modulo BDH".
* **N1** §11 title bookmark: `\texorpdfstring{$\Lc^4$}{L\textasciicircum 4}`.
