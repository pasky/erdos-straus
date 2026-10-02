# AGENT_REPORT_O2 — checkpoint 1 (branch `side-agent/omega-hub`)

## Headline

**H_MIN(θ) holds for every θ>1/3**, hence (with PO Theorem 4.1, i.e. modulo
Thorner–Zaman, as for PO Thm 5.1):

```
W(p) ≥ (log p)^3 · exp(−C log log p / log log log p)   for infinitely many Mordell-hard p,
log L_h(T) ≤ T^{1/3+o(1)}.
```

This is POINTWISE_OMEGA2.md Theorem 5.1. Label: **PROVED modulo
Thorner–Zaman** (same citation as PO Thm 5.1; effective). It is not yet
reviewed by the parent. It improves exponent 2 to 3, refutes `H_MOD(A)` for
all `A<3`, and brings the prime side level with the best proved Haar bound
(PO Thm 9.3, `T^{1/3+o(1)}`).

## How the hub obstruction is bypassed

PO Prop 6.3 (still true) kills *event-count* truncation. The new minorant
(POINTWISE_OMEGA2 §§1–3) has three ingredients.

1. **Support truncation.** Lemma 1.1 gives
   `B_L = Σ_{F⊆A(n), |supp F|≤L}(−1)^{|F|}`, in exact closed form. Lemma 1.2
   gives the pointwise minorant `B_L − 4^{L+1}e_{L+1}(a) ≤ 1[no event]`,
   where `a_ℓ` counts the occurring events at ℓ. The error is exponential
   in the number of *primes*, not events, so a K_{r,r} hub costs `16^r`
   against `y^{−2r}`.
2. **Mass bound.** After grouping by support, the coefficients are at most
   `2^{|U|}`. So `M_1 ≤ E∏(1+2a_ℓ)` (Lemma 1.3).
3. **Pseudoforest moment bound.** Lemma 2.1:
   `log E∏(1+z a_ℓ) ≤ zS_1 + O_z(S_2)`, provided every vertex
   `(ℓ, c mod ℓ)` has degree `≤e^{−3z−2}`. Lemma 2.2 enforces this by
   forbidding the high-degree hub *vertices*. Markov bounds the cost:
   `≤2S_2/δ` in total, and `≤w_ℓ/δ` per prime.

Theorem 3.1 (pure CRT combinatorics) adds the LLL lower bound and the twist
condition, using the conditional LLL (Haeupler–Saha–Srinivasan). §4 applies
it to ES:
* class-of-one quarantine at `y=T^{1/3}e^{2𝓛/log 𝓛}`, plus `T^{o(1)}` bad
  primes;
* all surviving events have support ≤2;
* per-prime masses are `o(1)` by the crude count;
* the global mass is `T^{o(1)}`, by PO Lemma 9.2 extended to an arbitrary
  quarantine set (Lemma 4.1).

## Verification done

* `scripts/omega2_abstract_check.py`: brute force of Lemmas 1.1–1.2 on random
  systems, ≈1.37M cases, 0 failures.
* `scripts/omega2_es.py checkI`: implication (I) checked directly on
  CRT-built integers at `T=1000, 3000`. 300 forced survivors, all with
  `W(n)>T`.
* Finite-T illustration of Construction 4.2 at `10^4, 10^5`. It is not an
  instance of the theorem, since the constants (`δ=e^{−50}`) are
  astronomical.
* An independent deep self-review (the `review` tool, codex) re-derived
  every lemma and found **no fatal defect**. Its five repairs are applied
  in commit "Self-review repairs":
  * `2|Q` added to Setting 3.0;
  * `+1` added in the budgets;
  * k-cutoff in Lemma 4.1;
  * θ<1/3 wording;
  * the script now really checks (I), and the vacuous Lemma 1.2 line at
    `10^5` is disclosed.

## Not done / open

* **θ<1/3.** It needs an H_PP-type per-prime bound and a hypergraph version
  of Lemma 2.1 (codegree issue, §7). Both are open; this is labelled
  Assessment.
* **H_PP with polylogarithmic z** (second part of the brief). Not attempted
  beyond the §7 remarks. I have a lead on the single-prime part: it reduces
  to bounding `|F_ℓ^{full}|` individually, and for `r'=1` the solutions
  correspond to pairs `(v,t)` with `v | ℓ+t`, `4t | ℓ+v`. This might give
  `|F^{full}_ℓ| ≤ ℓ^{1/2+o(1)}`, i.e. the single part of H_PP for
  `z≥(log T)^{2+ε}`. The multi-prime part is the real obstacle. Not
  written up.

## Suggested ledger updates (for the parent; I did not edit them)

* DISCOVERIES (H)8: append "exponent improved to 3 by POINTWISE_OMEGA2
  Thm 5.1 (H_MIN(θ) for θ>1/3)".
* (F)10: `H_MOD(A)` refuted for every `A<3`.
* (H)8 / PO §6.3: Prop 6.3 is an obstruction only to event-level
  Bonferroni.
* STATUS.md, line "Unconditionally, `W(p)≥(log p)^{2−o(1)}`…": change to
  exponent 3.
* paper/es-omega-note.tex would need a new section. It is untouched.

## Requested review focus

Lemma 2.1 (the expansion and the pseudoforest structure), Theorem 3.1
Step 4 (twist via conditional LLL), Lemma 4.3 (G)/(W) exponents, and the
application of PO Thm 4.1/6.2 in Thm 5.1.

---

# Checkpoint 2 (H_PP single-prime lead; POINTWISE_OMEGA2 §§8–9)

Review repairs D1–D2 from `reviews/pointwise-omega2-review.md` are applied
in commit `9bb341d`. §§1–5 are otherwise unchanged.

## Outcome: the lead is resolved, mostly negatively, with one structural theorem

1. **Lemma 8.1 (PROVED; EVIDENCE: 32 241 atoms, all odd r≤2001, 0
   mismatches).** The single-coordinate atoms with rough part r (any m,
   `D≤A`) are *exactly* the Elsholtz–Tao Type I points of `Σ_I^r` with
   `a≤b` (d squarefree):
   `a=r', b=k, c=(r'+k)/m, d=s, e=m, f=(4D+1)/m`, class `−a/b mod r`. So
   `|F_ℓ^{full}| ≤ 2F_I(ℓ)`. PO §9's "atoms" are ES Type I representations
   of the rough part.
2. **Prop 8.2.**
   * `|F_ℓ^{full}| ≤ ℓ^{3/5+o(1)}`: PROVED modulo ET Prop 1.7, cited.
   * The r'=1 pairs, i.e. my `(v,t)` lead, give `≪√ℓ log ℓ`, and
     `r'≤ℓ^{o(1)}` gives `ℓ^{1/2+o(1)}`: PROVED, elementary. In ET
     coordinates the pairs are `(f,c)` with `cf | a(ℓ+f)+c`.
3. **`ℓ^{1/2+o(1)}` for all r' is NOT proved.**
   * It would improve ET Prop 1.7 at primes.
   * Remark 8.3 checks ET's claim that 3/5 is the divisor-method limit.
     There is an explicit box (`a≍n^{2/5}, c≍n^{1/5}, d≍n^{2/5}`) where
     every determining quantity (`e, f, cd, ac, a²d, ab, bd, bf`) has size
     `≥n^{3/5}`.
   * EVIDENCE: most triples have `r'>1`, and `r'` reaches about `ℓ/4`.
4. **Theorem 9.2 (PROVED implication).** `F_I(n) ≤ n^{η+o(1)}` gives:
   * `w_ℓ ≤ T^{η/(1+η)+o(1)}/ℓ`;
   * H_PP(`T^{η/(1+η)+ε}`);
   * `log(1/δ*) ≤ T^{η/(1+η)+o(1)}`.
5. **Assessment of what the single part buys: essentially nothing.**
   * ET's η=3/5 gives Haar exponent 3/8, which is *worse* than PO Thm 9.3's
     1/3.
   * η=1/2, the lead's target, gives exactly 1/3. The crude bound
     `(T/r)τ²` and `r^{1/2}` cross at `T^{1/3}`.
   * Beating 1/3 needs η<1/2.
   * The single part of H_PP holds for `z≥(log T)^{5/2+ε}` (modulo ET). It
     was never the bottleneck, since bad-prime quarantine costs `T^{o(1)}`
     in both PO Thm 9.3 and Construction 4.2. So H_PP reduces to its
     multi-prime part.
6. **The precise remaining per-prime target.**
   * It is the progression average (AP-TI):
     `Σ_{r≤T, ℓ|r} F_I(r)/r ≤ T^{κ+o(1)}/ℓ`, uniformly in ℓ.
   * In ET coordinates it reduces to bounding the first terms
     `Σ_{a,d,f} 1/(ad·c_0)` with `c_0 ≡ f(4ad)^{−1} (mod ℓ)`. The regular
     part is polylog by ET Prop 1.4.
   * This is the Kloosterman-type input that PO §9 flagged, now explicit.
   * AP-TI with κ=o(1) would give `log(1/δ*)=T^{o(1)}` on the Haar side.
     The prime side below 1/3 additionally needs a hypergraph Lemma 2.1.

## Suggested ledger additions (for the parent)

* (H)10, Haar side:
  * "single-coordinate atoms = ET Type I points (POINTWISE_OMEGA2 Lemma
    8.1)";
  * "`F_I≤n^η` ⇒ Haar exponent `η/(1+η)` (Thm 9.2); η<1/2 is needed to
    beat 1/3; the single part of H_PP is not the bottleneck".
* The `F_ℓ^{full}` heuristic in PO §9, "|F^full|≈(log ℓ)^{2+}", should cite
  ET for the proved `ℓ^{3/5+o(1)}`.

## Review focus

* Lemma 8.1, the converse direction and injectivity.
* Prop 8.2.2, the gcd step `ℓ∤c` and the two cases.
* Thm 9.2, the split at `R=T^{1/(1+η)}` and the use of PO Thm 9.4 with
  `S_tot=T^{o(1)}` only.
* Remark 8.3's box: is it really consistent with ET Lemma 2.8?

---

# Paper update (`paper/es-omega-note.tex`, 21 pp, clean 3-pass pdflatex: 0 warnings, 0 over/underfull)

* **Title, abstract and headline Theorem 1.1:** `W(p) ≥ (log p)^3·exp(−C log log p/log log log p)`
  i.o., PROVED modulo Thorner–Zaman.
* **The exponent-2 proof** is kept as the warm-up Theorem 6.1 (`thm:two`).
  The D2-style inversion fix is applied there too.
* **New sections:**
  * §7: support-truncated inclusion–exclusion (Lemmas closed, pointwise and
    meanmass).
  * §8: the pseudoforest bound and the hub-vertex quarantine. The simple
    edge graph and the rooted-tree overcount are stated, as in D1.
  * §9: the conditional local lemma, with a short proof citing Alon–Spencer
    and HSS, and Theorem 9.2 (`thm:crit`).
  * §10: the proof of the main theorem, with a general-Π mass lemma.
* **§11 (limits):**
  * H_min is stated as true for θ≥1/3 and open below.
  * Prop. bonf is scoped as an obstruction to event-count truncation only.
  * The requirements below 1/3 are listed.
* **§13 (Haar):**
  * Lemma `lem:dict`, the Type I dictionary, worded as "direct computation"
    (D3).
  * ET 3/5 is cited "modulo the proof of ET Prop 1.7" (D4).
  * Theorem `thm:eta`, labelled "Proved implication", gives κ=η/(1+η).
  * An Assessment remark.
* **Summary of status** is rewritten. The joint W/ck_min statement still
  refers to the exponent-2 primes (`thm:two`); it was not strengthened.
* **New bibitem:** HSS (Haeupler–Saha–Srinivasan, J. ACM 58 (2011)).

---

# Referee report v2 (`es-omega-note-review-v2.md`, MINOR REVISION): mapping

| Item | Applied |
|---|---|
| P1 | Lemma `meanmass`: `M_1` defined before the lemma (cells, after merging). Full proof given: the `E\|B*−1\|` bound via Lemma `pointwise`; the κ identity; the cancellation for uncovered ℓ, including non-unit cells; the coverage step `1_c≤∏a_ℓ`. |
| P2 | Thm `crit` proof: LLL numerics (`x_E≤1/8`, `1−x≥e^{−1.1x}`, `Σx=2(S_1^++S_2^+)`); `M_1≤e^Λ+4^{L+1}16^{−L−1}e^Λ≤2e^Λ`; twist written out (`2\|Q` ⇒ f odd ⇒ squarefree; factorisation `ψ=χ_0(X_{ℓ_0})ψ'`; conditioning; mean zero; `P(Forb)`). |
| P3 | New Proposition `prop:hmin` [Proved]: H_min(θ) for θ≥1/3. It is the first half of §10, and the proof of Thm 1.1 now cites it. The Hypothesis header cites it. The Summary lists it under *Proved*. |
| P4 | New Lemma `ppl` [Proved]: the LLL step, giving `δ*≥(8/φ(Q_z))e^{−4S_tot}` under the per-prime condition. Remark `rem:pp` (modulo ET) and Thm `eta` both cite it. |
| P5 | New Proposition `prop:a1` [Proved] with its proof (the `a=1` count is `≪√ℓ log ℓ`); marked as not used below. |
| P6 | Wording changed to "points of Elsholtz–Tao's Type I variety" (abstract) and "governed by the Type I variety `Σ_I^r`" (text and subsection title). |
| P7 | Status conventions extended: *Proved modulo the proof of X*, *Classical*, *Proved implication*, *Assessment*. Header of Thm `slice-intro`: "Proved; (b) modulo LW". Header of Lemma `lll`: "classical, proof included". |
| P8 | It goes through cleanly. New Corollary `cor:joint` [Proved modulo TZ]: jointly `W≥(log p)^{3−o(1)}` and `ck_min≥(log p)^{1−o(1)}`. The argument: `p≡1` mod 24 and mod every `ℓ≤y`, then reciprocity, then Lemma `np` with `y≥(log p)^{1−o(1)}`. Recorded first in POINTWISE_OMEGA2 §5 as Corollary 5.2, so the paper does not exceed its source. |

Build: pdflatex ×3, 23 pp, 0 warnings, 0 overfull/underfull, 0 undefined references.
