# Hostile review R63 of POINTWISE_MN.md (O63, branch side-agent/mn-quarter @ f97b37d)

Reviewer branch: side-agent/review-mn. Scripts: `scripts/review_mn_*.py` (from scratch).

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Lemma 1.1 | SOUND (see §L1) |
| Prop 2.1 | SOUND (§P21) |
| Thm 3.1 | SOUND (§T31; MINOR-1) |
| Prop 3.2 | SOUND (§P32) |
| Lemma 4.1 | SOUND (§L41) |
| Cor 6.1 | SOUND-AFTER-REPAIRS (§C61; MAJOR-1 = proof must be written out; MINOR-5) |
| Thm 5.1 (implication) | SOUND-AFTER-REPAIRS (§T51; MINOR-2..4); label CONDITIONAL honest |

**Overall.** No FATAL defect; no mathematical error found in any PROVED claim. One MAJOR (Cor 6.1 is
labelled PROVED but its substitution proof is only a bullet sketch, and three OMEGA12/OMEGA11 sentences
that are false for odd m are not replaced in the text) and six MINOR. Labels otherwise honest: Thm 5.1
is correctly CONDITIONAL, §6 correctly EVIDENCE. The key structural claim — the 1/4 machinery extends
exactly to m ≡ 0 (4) and breaks for m ≢ 0 (4) only at OMEGA13 Lemma 3.1 — is confirmed.

### Defect index
* MAJOR-1 — §6b / Cor 6.1: write the substitution proof out (items (i)–(v) in §C61); until then the
  label should say "substitution sketch".
* MINOR-1 — §3: "hard" = Type-II-hard only; say no Type I statement is made.
* MINOR-2 — §5: ADM_m must fix Y = Y(K) (the proof uses `Y = 𝓛^{C_K+4}`).
* MINOR-3 — §5(d): display `Π_new = pp'N²1[match]` → `Π·N·1[match]`.
* MINOR-4 — §5 AUP: for odd m, declare 2 an ordinary coordinate; drop "M odd ⇒ p_0 = P_H".
* MINOR-5 — Cor 6.1: output primes are ≡ 1 (Q), Type-II-hard only; say so near "Sierpiński's 5/n".
* MINOR-6 — §3: `H_5(840) = {r ≡ 1 (4), r mod 7 ∈ {1,3,5}}`; {1,3,5} is not "1 plus the non-residues".

## §L1 Lemma 1.1

Re-derived: `gcd(M,mA)=1` since `M=mA−1`; primes of D divide A, so `−mD = −e·□` with □ a unit mod M;
every prime q | e divides mA = M+1, so `M ≡ −1 (q)`, and reciprocity gives `(q|M)=(−1)^{((q−1)/2)((M+1)/2)}`.
(b),(c),(d) follow as written; the (d) case split (8|m, or m≡4 (8) with t=1 ⇒ v_2(D) odd ⇒ 2|A ⇒ 8|mA)
is correct and covers all t=1 cases (m≡0 (4) and t=0 ⇒ (b) gives −1 directly).

From-scratch check `scripts/review_mn_jacobi.py 6000 <m>` (sympy Jacobi computed directly on −mD mod M,
not via the formula): 22 values m ∈ {4..16,18,20,21,22,24,28,30,36,40}, every odd-M atom with M ≤ 6000:
0 failures of (a),(b),(c); symbol set = {−1} exactly for m ∈ {4,8,12,16,20,24,28,36,40}, = {±1} for every
m ≢ 0 (4) tested. The "iff" direction (m ≢ 0 (4) ⇒ some +1) is not part of Lemma 1.1 as stated; it is
supplied by Prop 2.1 (checked below) — the AGENT_REPORT's phrasing "always −1 iff m ≡ 0 (4)" is fine
given Prop 2.1.

Minor: (a) is stated for "every prime ℓ | M"; for m odd, M may be even (e.g. m=5, M=4) — the lemma
hypothesis "M odd" excludes this, but §3/§6 must remember that even-M atoms exist for odd m (see Cor 6.1).

## §P21 Prop 2.1 — SOUND

Re-derived both constructions: m odd, ℓ ≡ −1 (m), ℓ ≡ 5 (8) ⇒ 2 | A, D ∈ {1,2} give ratio (2|ℓ) = −1;
m ≡ 2 (4), q ≡ 3 (4), q ∤ m, ℓ ≡ −1 (mq), ℓ ≡ 1 (4) (CRT-compatible since v_2(mq)=1) ⇒ q | A and
(q|ℓ) = (ℓ|q) = (−1|q) = −1. Firing bound 1/((ℓ−1)/2) = 2/(ℓ−1) correct.
From-scratch `scripts/review_mn_prop21.py` (primes ℓ < 2·10⁴, 16 values m ≢ 0 (4)): 60–80% of prime
atoms meet both cosets for every m tested (e.g. m=5: 374/559; smallest m=5 example is ℓ=19, the
document's ℓ=29 is also verified: classes {9,13,14,19,23,24,26,27,28} with both symbols).
Note: Prop 2.1 is an *obstruction* statement (the OMEGA13 §3 mechanism cannot be reused); it proves
nothing positive and correctly is not used as an input anywhere.

## §T31 Thm 3.1 (m ≡ 0 (4)) — SOUND (minor editorial points only)

Checked the substitution list against OMEGA13 §3 (Lemmas 3.1–3.3, Thm 3.4) and §5 (I1–I3, property (I),
Thm 5.1, ℓ_aux) line by line. Every place where OMEGA13 uses m = 4:
* Lemma 3.1(a),(b) → MN Lemma 1.1(a),(d): verified above. The *consequence* clause (r square mod every
  prime of Q ⇒ r ≢ −mD (M) for M | Q) uses only `(r|M)=1 ≠ (−mD|M)`; holds verbatim.
* Lemma 3.2(a) drift: at an a=0 square step the hit probability of class −mD mod ℓ is
  `2/(ℓ−1)·1[(−mD|ℓ)=1]`, so `E p_new = (1+(−e|ℓ))p ≤ 2p`; a ≥ 1 steps exact. ✔.
* Lemma 3.2(b) `p_0 = P_H`: needs M odd (2-adic coordinate never constrained). m ≡ 0 (4) ⇒ M ≡ 3 (4). ✔
  (This is exactly the point that fails for odd m; see Cor 6.1 / Thm 5.1.)
* Lemma 3.3(A) NT: `Q(n)=n(mn−1)`, resultant 1; roots mod p: {0, m^{−1}} for p ∤ m, {0} for p | m, so
  ρ(p) ≤ 2 < p for p ≥ 3 and ρ(2)=1 < 2: no fixed prime divisor. `∏(1−ρ(p)/p) ≍_m (log x)^{−2}`. ✔
* Lemma 3.3(B) / Ξ: pure divisor sums over M ≤ T; the M ≡ −1 (m) restriction only shrinks the sums. ✔
* Thm 3.4 normalisation: OMEGA13 normalises on `n ≡ 1 (24)` (atom M=3, D=1). For m ≡ 0 (4), m ≠ 4,
  M = 3 need not be an atom; MN states the bound on all of Ẑ^× with the factor `φ(Q)^{−1}`, which is
  correct (and weaker by O(1)). ✔
* Forced steps at 3, 5, 7 for m with 3, 5 or 7 | m: those primes never divide any M, so the steps
  are pure cost (log 105). ✔ Twist I1(b): `ℓ_0 | f | d_i` is a prime of some M, so ℓ_0 ∤ m. ✔
* I2 junta, OMEGA10 Thm 3.4, O11 Thm 3.2 assembly, `#atoms ≤ T²`: abstract, m-free. ✔
* I3 / property (I) / ℓ_aux: verbatim with `−4D ↦ −mD`. ✔

**MINOR-1 (§3 "What hard means").** "p Type-II-hard modulo Q" is a statement about Type II solutions only;
for m ≠ 4 (and esp. m = 5) the reader may read "hard" as "not covered by any known identity" (Type I
identities also exist). Repair: one sentence that Thm 3.1(ii)/Cor 6.1 concern W_m (Type II, by TRANSFER
Lemma 5.0/completeness noted in the TRANSFER review), and make no claim about Type I coverage.

## §P32 Prop 3.2 — SOUND

Checked against POINTWISE_HAAR Thm 2.1 / Lemmas 2.2–2.4: `M ≡ −1 (mod mn)` ⇒ `M ≡ −1 (m)` and
`mn | mA ⇒ n | A`; (F1) needs `mD ≤ m T^{1/5} < √T ≤ M` (true for T ≥ T_0(m)), so distinct D give distinct
residues and `P(E)=1/φ(M)`; sifted progression length `X/(mn) ≥ X^{4/5}/m`; y-rough M are odd, so no
2-adic issue even for odd m; (2.1), Δ_a, Δ_b with `4n ↦ mn` only change constants. No Jacobi input. ✔

## §L41 Lemma 4.1 — SOUND

Checked against OMEGA9 Thm 1.1 proof (lines 140–195) in the coset form. On rH,
`c(χ_Qχ_D) = χ̄_Q(r)·E[Bχ̄_D]/φ(Q)`. Items 1–2 (conductor support, `|c| ≤ Aμ/φ(Q)`, `c(χ_0)=μ/φ(Q)`)
are |·|-statements. Case 0 uses only |c|. In the exceptional case, Case A (χ_D trivial, χ_1 = χ_Q real):
if `χ_1(r)=−1` then `c = −μ/φ(Q)` and the split term `−c·x^{β_1}/β_1 = +μx^{β_1}/(β_1φ(Q)) > 0`, so
`S(x) ≥ μx/φ(Q)(1 − 1/200 − 1/400) > 0` with no Page bound — correct (the (G) error bound
`≤ μx/(200φ(Q))·min(u,1)` from the preceding paragraph does not depend on the sign). Case B uses
`|ψ_1(r)|=1` only. `c(χ)` real for real χ (needed to split the term) holds since `χ̄(r) = ±1`.
Confirmed: Case A is the only place a character value at r enters with a sign. ✔

## §T51 Thm 5.1 (implication ADM_m ⇒ conclusions) — SOUND-AFTER-REPAIRS (MINOR-2, MINOR-3, MINOR-4)

Re-derived (a): at a step at (ℓ,a) with N fibre classes and forbidden fraction f, an uncompleted atom with
`v_ℓ(M) ≥ a+1` has `E p_new = p·N·P(hit its class) ≤ p·N/((1−f)N) = p/(1−f)` (= 0 if its class is
forbidden), and its Ψ is multiplied by `(1−f)`; completed atoms are forbidden ⇒ `p_new=0`; atoms with
`ℓ | M`, `v_ℓ(M) ≤ a` have p unchanged and Ψ multiplied by `(1−f) ≤ 1` (the text omits this case but it
only helps); `ℓ ∤ M` unchanged. Stopping *before* a Λ-violating step is legal (f predictable), keeps
`Λ ≤ K` hence `Ψ ≥ 1` along the whole stopped path, and coincides with the unstopped AUP on the ADM
success event. (b),(c) by optional stopping exactly as OMEGA13 Lemma 3.2 with `Ψ_0 = K^{ω_Y(M)}`.
(d): agreeing step `Π → Π·N·1[match]`, mean `≤ Π/(1−f)`, Ψ(F)Ψ(F') × `(1−f)²` ✔; disagreeing ⇒ 0 ✔.
Prefix: `E_{r_0∼U(H)}[p_0] ≤ δ_0^{−1}E_{Haar}[p_0] = P_H/δ_0`, and for pairs Haar reveals are exact
martingale steps for Π, so `E_Haar[Π after prefix] = Π^{Haar}_0` ✔. Property (I) is by construction
(every completed atom inconsistent with r; prefix atoms excluded by `r_0 ∈ H_m(Q_0)`). NT with
`f_2(p) ≤ Kβp/φ(p)` stays in the NT class (K fixed). No circularity found in the implication.

**MINOR-2 (§5, statement of ADM_m vs proof of Thm 5.1: Y depends on K).** ADM_m(K,Q_0) is stated "with
OMEGA13's β, η, Y", but the proof takes `Y = 𝓛^{C_K+4}` with `C_K` depending on K. Repair: state ADM_m
for `Y = 𝓛^{C}` with an explicit C = C(K) (or "for every fixed C ≥ 1"), so the hypothesis is a
well-defined statement about one process.

**MINOR-3 (§5 (d) display).** "`Π_new = p p' N²·1[match]`" omits the R/ρ factor; should read
`Π_new = Π·N·1[match]` (ρ = N is removed). Conclusion unchanged.

**MINOR-4 (§5 AUP definition, odd m).** The AUP says coordinates are "as in OMEGA13 §3", which has no
2-adic coordinate (M odd there). For odd m, even M exist and the prime 2 must be a coordinate (with
unit classes mod 2^k, N = 2^{k−1} at k ≥ 2, and N = 1 at level 1). The prefix happens to put 2 | Q_0,
but the AUP definition should say explicitly that 2 is an ordinary coordinate when m is odd (the same
point is raised for Cor 6.1 in §6b). Also Lemma 3.2(b)'s `p_0 = P_H` remark ("M odd") must be dropped
for odd m — it is replaced by the prefix factor `1/δ_0`, which the text does give.

Label CONDITIONAL on ADM_m is honest; ADM_m is a genuinely open probabilistic statement (the author's own
§6 "why not proved" is accurate: first moments diverge like Σ(log ℓ)³/ℓ, a second-moment union bound is
needed).

## §C61 Cor 6.1 (every m, exponent 1/5, Haar ≪ 𝓛^5 log𝓛) — SOUND-AFTER-REPAIRS (MAJOR-1: write the proof out)

I re-did the substitution myself against OMEGA12 §§2–6A, OMEGA11 Setting 2.0 / Lemmas 2.1, 2.2, 3.1 and the
ET source (`sources/elsholtz-tao-1107.1010.pdf`, read via pdftotext). Findings:

* **ET inputs (checked in the PDF).** Prop 1.4 is stated for `Σ_{a≤A,b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)`,
  any `k ≪ (AB)^{O(1)}` ✔. Thm 7.1 is for any polynomial with nonnegative coefficients `≤ N^l` and
  `ρ(p^j) ≤ C`, constant depending on (D,l,C) ✔. ET's own proof of Prop 1.4 uses Thm 7.1 for `kab²+1`
  with exactly "ρ_ka(p^j) ≤ 2 for odd p^j and ≤ 4 for p = 2", so C = 4 is ET's own case ✔. (7.10) is
  stated and proved for general k (with the 2-part of m and of a reduced away) ✔. Cor 7.4: coprime
  linear `an+b`, `a,b ≪ N^{O(1)}` ✔ (here `gcd(ma², b_a) | gcd(ma, ma²d_0+1) = 1`).
* **Lemma 2.1 parametrisation for general m** (`P = ma²d+1`, `g = gcd(M, mD+1) | a+b`,
  `macd = f + N`, `N ≥ (m/2)acd − 1 ≥ acd`, injectivity, involution `D ↦ A²/D` preserving g since
  `mA ≡ 1 (M)`): re-derived, and brute-forced from scratch (`scripts/review_mn_cor61.py`, all m = 4..30,
  M ≤ 3000, 106 865 atoms incl. even M): 0 defects.
* **Class of one never an event** (TRANSFER Lemma 5.1(ii), incl. even M): 0 counterexamples in the same run.
* **Root counts.** `mdx²+1`: max 4 roots mod 2^k (k ≤ 11, md < 400), ≤ 2 mod odd prime powers ✔.
* **2-adic example** m=5, M=464, D=3: A=93, `gcd(464,840)=8 | 16 = 5D+1`, class `−15 ≡ 1 (16)` ✔.
* OMEGA12 Lemma 3.1 small-q argument with "ℓ | mad ⇒ ℓ ∤ N, else c in one class mod q" covers q = 2^i ✔.
* O11 Lemma 2.2 charging is prime-independent (threshold `c(a+1)logℓ/𝓛`, `Σ v_ℓ log ℓ = log M`) ✔;
  O11 Lemma 3.1 needs only `8 | Q` (true if `a_2 ≥ 3` at start) and `f_2` coprime to Q (then odd) ✔;
  Lemma 6.2's `e³` product needs every unstepped prime to be `> 𝓛`, true if 2 starts at `a_2 = 3` ✔.

No mathematical error found. But:

**MAJOR-1 (§6b, Cor 6.1 label "PROVED").** §6b is a bullet summary of a subagent's check, not a written
substitution proof; several OMEGA12/OMEGA11 sentences that are literally *false* for odd m are not
listed with their replacements. A reader cannot verify "PROVED" from the document. Repair: write a
substitution list like Thm 3.1's, at least:
 (i) O11 Setting 2.0: `Q = 2^{a_2}∏_{ℓ odd}ℓ^{a_ℓ}`, coordinate `X_2 = n mod 2^{f_2}` on `n ≡ 1 (2^{a_2})`,
     start `a_2 = 3`, raised by the same threshold rule; Lemma 2.1 fibre probability `2^{−(v−a_2)}`;
     survival `gcd(M,Q) | mD+1`; (I) via TRANSFER Lemma 5.1(ii).
 (ii) OMEGA12 Lemma 3.1 "q = 2 omitted harmlessly: N divides the odd M" — false for odd m (N can be
     even); replace by the ℓ | mad dichotomy, which includes ℓ = 2.
 (iii) OMEGA12 Lemma 4.1 "Every q | P is odd" and "Q is odd-valued, so ρ_Q(2^j) = 0" — false when md is
     odd. Replace: q = 2^i allowed with ≤ 4 roots x_0; `ρ_Q(2^j) ≤ 4`; Euler factor `≤ 1+4/(ℓ−1)`;
     Thm 7.1 with C = 4; "two roots" → "≤ 4 roots"; `P < 32Z³` → `P < 8mZ³`; coefficient bound
     `≤ N'^5` needs `A ≥ A_0(m)` (small A absorbed).
 (iv) Lemma 6.2: start includes `a_2 = 3`, cost `log(8∏…)` unchanged.
 (v) Prime side: p ≡ 1 (Q) gives Type-II-hardness modulo Q because class 1 is hard (not "Mordell-hard").
With these written, the label "PROVED modulo (G), ET Prop 1.4/Thm 7.1/Cor 7.4/(7.10), OMEGA10 Thm 3.4"
is justified; until then it should read "PROVED (substitution sketch; see review R63)".

**MINOR-5 (Cor 6.1 / Thm 3.1 output primes).** The Cor 6.1 primes satisfy p ≡ 1 (Q) with `840 | Q`, so
for m = 5 they are `≡ 1 (mod 5)` etc. They are Type-II-hard only; whether 5/p for such p has a Type I
or other easy solution is not addressed. Say so explicitly next to "in particular for Sierpiński's 5/n".

## §H "What hard means" (§3) and §6 evidence — numerics re-done from scratch

`scripts/review_mn_hard.py` (independent of `mn_hard.py`/`mn_greedy.py`):
* `|H_4(840)| = 24` and it equals the set of classes that are squares mod 3, 5, 7 ✔ (doc: 24 ✔).
  `1 ∈ H_m(840)` for m = 4..8 ✔.
* **MINOR-6 (§3, line ~92).** "`H_5(840)` is `{1,3,5} mod 7`, which is 1 plus the non-residues" is wrong
  twice: (a) `H_5(840) = {r ≡ 1 (mod 4)} ∩ {r mod 7 ∈ {1,3,5}}` (48 classes; the atom M = 4, D = 1 kills
  `r ≡ 3 (4)`), and (b) the non-residues mod 7 are {3,5,6}, so {1,3,5} is "1 and two of the three
  non-residues". The intended point (not a union of square cosets) survives. Repair the sentence.
* m = 7 small-prime death (§5/§6): with T = 2·10⁴ (`e_2 = 11`, `e_3 = 9`), every 2-adic unit is allowed
  (no M = 2^a is ≡ 6 (7)), and exactly 64/1024 = 6.25% of 2-adic classes leave *no* admissible unit
  mod 3⁹. This matches the doc's 2/40 deaths and confirms that a prefix is genuinely needed. ✔
* I did not re-run the full greedy drift experiment (max Λ ≈ 4); it is labelled EVIDENCE and nothing
  is derived from it, so it does not affect any PROVED label. The heuristic `E f_ℓ ≍ (log ℓ)³/ℓ` is
  correctly labelled heuristic.

## §6 "why ADM is not proved" — Assessment

Accurate and honest. One addition worth stating: ADM_m is needed *uniformly in T* for every `ℓ ≤ Y(K)`
with Y → ∞, and Σ_ℓ (log ℓ)³/ℓ diverges, so even the first-moment heuristic only gives Λ(ℓ) ≤ K for
"most" ℓ; a union bound needs tail bounds for f_ℓ at *every* large ℓ, which the second-moment route
the author sketches would have to supply. No overclaim found.
