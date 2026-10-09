# R114 — hostile referee report on `paper/es-typei-heegner-note.tex`

Referee: R114 side agent (branch `side-agent/referee-heegner`). Author branch `side-agent/typei-heegner-note`
merged at `f8a22a5`. Sources compared: `EXCEPTIONAL_TYPEI_LOGLOG.md`, `reviews/exceptional-typei-loglog-review.md`
(R111 rounds 1–2), `EXCEPTIONAL_MN3.md` §§1–3, ET arXiv v6 (`sources/elsholtz-tao-1107.1010.pdf`), DI 1982 scan
(`sources/o111/deshouillers-iwaniec-1982.pdf`, pp. 223, 230–232 read as images), Drappeau arXiv:1504.05549v4 and
Liu–Masri–Young arXiv:1206.3208 (both downloaded by me from arXiv; not in `sources/`).
Not accessible: Iwaniec *Spectral Methods* (book locators), Halberstam–Richert, Kim–Sarnak appendix, Jia 2012,
Duke 1988, Montgomery–Vaughan 1973 (statements checked from memory only).
From-scratch code: `scripts/review_r114_sep.py` (+ `.out.txt`). Working notes: `reviews/r114-scratch-notes.md`.

## Recommendation

**Accept as an internal CONDITIONAL note after the MINOR repairs below (applied in place, marked "(R114 repair)").**
No FATAL or MAJOR defect. The main theorem is correctly stated as CONDITIONAL on (SEL) for `Γ₀(4dq²)` with even
nebentypus mod 2q, uniformly in d ≥ 1 and odd squarefree q coprime to d, and the inherited ET/MN3 reduction is
flagged. The paper is faithful to EXCEPTIONAL_TYPEI_LOGLOG.md after R111 r2. All three "deviations" in
AGENT_REPORT_O114 are correct, and the first is a real fix of the source. After the repairs the note compiles cleanly (two consecutive passes: no warnings,
undefined references or bad boxes; 26 pp, up from 25). ES is not claimed.

Numbering note: the PDF numbers are not the label names. "Lemma 1.1" (label `L:1.1`) is **Lemma 8.1**, "Thm 8.1"
(label `L:8.1`) is **Theorem 8.2**, and MN3 Prop 2.3 / Prop 3.3 / Lemmas 3.1–3.2 are **Prop 2.4 / Prop 2.3 / Lemma 2.1 /
Remark 2.2**. Below I use the **PDF numbers**.

## Verdicts per claim

| Claim (PDF numbering) | Verdict | How checked |
|---|---|---|
| §1 ET quotations (Thm 1.1; p. 5; §9 p. 36 "[sic] Type II case"; (1.4); Jia) | SOUND | read in ET v6 text (p. 4–5 lines, p. 36 parenthesis literally "Type II case"; Jia cited for the f_II prime sum) |
| Hypothesis (SEL), Theorem A = Thm 8.2 | SOUND (CONDITIONAL label correct) | quantifiers match LOGLOG §5; used only in Prop 5.1 |
| §2 reduction `f_I(p) ≤ 2Σ_c w_c(p)`, (2.2), `b ≥ a/2` | SOUND | re-derived from ET Prop 2.2 (map (abdn,acd,bcd)) and Lemma 2.8 bounds; `bf = an + c`, `f ≤ 2n` |
| Lemma 2.1 (SL₂ form), Remark 2.2 (fibres) | SOUND | σ_d computed; fibres (a,c,f), (c,d,f), (a,b,c) re-derived |
| Prop 2.3 (R_bad, area 1/6) | SOUND | seven exponents, redundancies, integral 1/24+1/8 re-derived |
| Prop 2.4 (MN3 Prop 2.3) | SOUND as a citation | matches MN3 verbatim after renaming (a,b,A,B)→(u,v,U,V) |
| Lemmas 2.5–2.7 (weighted sums, BT outside R_bad, masses) | SOUND | re-derived (PV mean square, ρ_d ≤ 1∗χ_d, Prop 2.4 hypotheses incl. large-k tails) |
| Prop 2.8 (large c; MN3 Thm 3.8 step (1)) | SOUND | ET (8.1)–(8.2) read; split by c > N^η ⇔ ad ≪ N^{1−η} |
| Lemma 3.1 (distance formula) | SOUND | brute force: 5.1·10⁶ pairs, exact rationals, computed from the points themselves |
| **Lemma 3.2 (uniform separation, cosh ≥ 3/2)** | **SOUND, sharp** | brute force d ≤ 60, A ≤ 60: min cosh = 3/2 exactly, attained for d = 1, 5, 11, 19, 29, 31, 41, 55, 59; on the Type I subset (4d ∣ B) min cosh = 3 |
| §3.1 parity/sieve groups, M = 4dq², index φ(q)/2 (1 at q = 1), even-character decomposition | SOUND | conjugation re-derived; 23 000 random group-action tests, 0 failures |
| §3.2 box coordinates, counting identity, Fricke/e-cusp | SOUND | re-derived (w_Q, width A/F, height (F√d)⁻¹, area A√d, −1/(dw_Q) = (2a+i/√d)/e) |
| Lemma 4.1 (resolvent kernel) | SOUND | s₀ = (1+√5)/2 from s(s−1) = 1; Green function (1/2π)Q_{s−1}(cosh r) gives the 1/(2π√2) constant; decay (1+r)e^{−s₀r} |
| Lemma 4.2, **Prop 4.3 (Sobolev duality)**, Cor 4.4 | SOUND | packing ≪_{r₀} e^R, shell sum converges since s₀ > 1; duality ν(P₀) = ⟨(1−Δ)P₀,(1−Δ)⁻¹ν⟩; constant independent of group |
| §5 cited large sieves | SOUND | DI Thm 2 (p. 230), (1.34) (p. 231), Thm 5 (1.38) (p. 232), μ(a) (1.1) (p. 223) read on the scan; Drappeau Prop 4.7 (4.23)–(4.25) and Lemma 4.8 read in arXiv v4 (see m6) |
| Prop 5.1 (variance, CONDITIONAL on SEL) | SOUND | re-derived the (1−Δ)ψ reduction, the char-norm identity with h_q (including q = 1), the unfolding, the Mellin constant 1/(8πi), the Stirling bounds, the residues ½Γ(±it)𝒲(±it)…, the block sieve ≪ λ(K²+Z) (the 𝓛² there is superfluous) and the zero mode via Σ_𝔠\|Φ_{𝔠∞}\|² = 1 |
| §6 densities, Lemma 6.1 | SOUND | brute force over 𝔽_ℓ³ (ℓ ≤ 13): quadric size ℓ²+χℓ, both density formulas exact; SO-torus order ℓ−χ |
| Theorem 6.2 (per-d) incl. Deviation 1 (κ_c(q)) | SOUND | ℓ ∣ c, χ = 1 gives \|SL₂\|g = 2ℓ(ℓ−1) > ℓ² (confirmed numerically: 12, 40, 84, 220, 312). The source's uniform-in-c claim was wrong; the fix is harmless because the sieve takes ℓ ∤ 2cs |
| Lemma 6.3 (class-number bound) | SOUND | ℙ¹(ℤ/d) coset count, index 6/4, 2-adic identity; brute force d ≤ 80: root count ≤ r(d) (max ratio 1) |
| Prop 7.1 (K_a) and (7.5) | SOUND | identity an = f(ce−a) − c, CRT, T_ℓ, axial terms, Weil; summed bound re-derived |
| **Lemma 8.1 (degenerating savings)** | SOUND | identity Σ min(1/j,1/k) = Σ(2h−1)/h checked exactly to L = 200 |
| **Theorem 8.2 (assembly)** | SOUND (CONDITIONAL on SEL, relative to the cited inputs) | steps 1–5 re-derived. BT-layer (A, D ≥ N^{1/4} for k ≤ 𝓛/3); (i) D/A = N^δ, Q = N^{δ/4}, c₀; (ii) γ ≤ δ/2 from k ≥ 2j; (iii) margin −α/4; (iv) both branches, cdf weight via Lemma 2.5(c); sieve bookkeeping N^{−κδ/2} ≤ 1/k for k ≥ C₁ log 𝓛; layer sums via Lemma 8.1 |
| §9 strip ≈ 7/32, 21/128; DI Thm 5 with X = 1/(N₀Y); Kim–Sarnak 7/64 incl. nebentypus | SOUND as an Assessment | exponents recomputed; μN₀X = F'/(4q√d); Drappeau §4.1.2 confirms that θ ≤ 7/64 holds for B(q, χ) |
| §9 LMY comparison | SOUND | arXiv text: q prime, −D < −4 odd fundamental, q split, q ≤ D^{1/20−ε}, Thm 1.4 / Thm 7.1 |
| Problem 5 (Theorem L′, (log log N)^{1/3}) | SOUND | matches the MN3 §0/§2 statement |

## Defects (all MINOR; repairs applied in the .tex, marked "(R114 repair)")

**m1 (MINOR, citation).** §8, proof of Thm 8.2, step 2, the BT-layer paragraph: "Brun–Titchmarsh [ET, (A.10)] gives
`8ad 2^j/(φ(4ad) j log 2)`". ET (A.10) is `π(N;q,a) ≪ N/(φ(q) log(N/q))`, which is for an initial segment and has an
unspecified constant. The displayed explicit bound is the interval form `π(x+y;q,a) − π(x;q,a) ≤ 2y/(φ(q) log(y/q))`
of Montgomery–Vaughan, with y = 4ad·2^j. *Repair:* cite [MV] and state the interval form.

**m2 (MINOR, numbering clash).** §1, "Status and dependencies" cites "[MN3, Proposition 2.3]". In this paper,
Proposition 2.3 is MN3's Prop 3.3 (the bad region), while MN3's Prop 2.3 is Proposition 2.4 here. The agent report
also uses label names ("Lemma 1.1", "Thm 8.1"), but the PDF has Lemma 8.1 and Theorem 8.2. *Repair:* add "(here
Proposition 2.4)" in §1. The parent should use PDF numbers when forwarding.

**m3 (MINOR, wording).** §3, after the definition of 𝓕_d^I: "(4d, d) need not be 1". In fact (−4d, d) = d, which
is never 1 for d > 1. *Repair:* "(−4d, d) = d > 1 for d > 1".

**m4 (MINOR, notation).** Several symbols clash:
* In §8 the mass bound of Lemma 8.1 is called M ("take M ≍ N𝓛²"), but M = 4dq² is the level in §§3, 5, 6.
* In Prop 2.4 the letter l is the fixed exponent, while the proof of Lemma 2.7 uses l for a squarefree divisor
  ("fixed exponent 40").
* χ_d is defined twice, as (−4d/·) in Lemma 2.5 and as (−d/ℓ) in §6. The two agree at odd ℓ, but χ also denotes
  the nebentypus.

*Repair:* rename the Lemma 8.1 bound to 𝓜, and add a remark that the two χ_d agree on odd primes. The l clash is
harmless and is left alone.

**m5 (MINOR, unverified locators).** §1 marks only the Iwaniec-book locators as unverified. The Halberstam–Richert
locators (Theorem 4.1, Lemma 4.1) are also unverified: HR is not in `sources/`, and MN3 already says they were
"checked from memory". Montgomery–Vaughan and Kim–Sarnak were not accessible to me either. *Repair:* extend the
§1 sentence to these.

**m6 (MINOR, Drappeau normalisation).** §5: "With an even character of conductor q₀ ∣ q". In Drappeau §4.1.1,
q₀ is the *modulus* of χ ("χ a character modulo q₀ | q"). The paper's reading is still valid: on Γ₀(M) the multiplier
χ(d) depends only on the primitive character inducing χ, so one may take q₀ to be the conductor, and in any case
q₀ ≤ q. *Repair:* one clause saying so. I confirmed the Drappeau Prop 4.7 statement, (4.23)–(4.25), the
Whittaker normalisation, and Lemma 4.8 (second factor `1 + (q₀μ(a)N)^{1/2+ε}`) in arXiv v4. That file is not in
`sources/`.

**m7 (MINOR, honesty of the dependency paragraph).** §1 says the inherited ET/MN3 reduction was not re-checked by
R111. That remains true, but R114 has now re-derived the parts used (`f_I ≤ 2Σ_c w_c` from ET Prop 2.2/Lemma 2.8,
and the large-c step from ET (8.1)–(8.2)). *Repair:* add one sentence. The labels do not change.

**m8 (MINOR, presentation).** The statement of Theorem 8.2 says "Assume (SEL)" but does not repeat that the proof is
relative to the cited inputs. *Repair:* add "relative to the cited inputs listed in Section 1".

Observations that need no change:
* Prop 5.1: the 𝓛_*² in (5.8) and the hypothesis `Y ≤ λ𝓛_*^{−3}` are stronger than the proof uses (only Y ≤ λ and
  Y^{−1/𝓛_*} ≪ 1 are needed). This is harmless.
* Lemma 3.2: the constant 3/2 is sharp on 𝓕_d. On the Type I subset the minimum is 3 (also seen in R111).
* Γ_{M,q} has no elliptic points (4 ∣ M), so the e_z weights are all 1. The general bookkeeping is still correct.

## Things I could not check
* Iwaniec-book locators (§1.8, Thm 1.14, Thm 7.3).
* HR Thm 4.1/Lemma 4.1.
* The statement of Kim–Sarnak App. 2 (I relied on Drappeau §4.1.2 citing it for B(q, χ)).
* MV 1973 (constant 2 in the interval form).
* Jia 2012 and Duke 1988 (cited only in the literature paragraph).

None of these affects the logic beyond the standard forms of these results.

## Post-referee addition (O118)
After this referee pass the paper was extended (task O118): new title/abstract; Theorem 1 (unconditional,
`o(N log²N log log N)`, PROVED relative to DI Thm 7 and Drappeau Lemma 4.10) and Theorem 2 (`≪ N log²N` under (SEL)
or (EFF)); new §9 (write-up of EXCEPTIONAL_TYPEI_LOGLOG2, itself reviewed twice); §10 and open problems rewritten;
residual-spectrum fact now cited separately (Iwaniec §11, Huxley 1984; locators unverified). **This referee report
does not cover §9 or the new theorems**; a new referee pass is required.
