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

---

# Checkpoint 3: below θ=1/3 (POINTWISE_OMEGA2 §10)

## (a) Hypergraph lemma: done (PROVED)

* **Lemma 10.1 (private covers).** Each member of a private cover has a prime
  that no other member touches. The private-cover count `G^cov` majorises
  `binom(N,u)`, and it can replace `e_{L+1}(a)` in Lemmas 1.2–1.3.
  Brute-force check: the abstract script, 0 failures.
* **Lemma 10.2.** For private families of hyperedges with at most k primes:
  `Σ_{u≤U_0}w^uEG^cov_u ≤ exp((1+w)S_1+2ek(1+w)^kS_H)`, provided
  `Σ_j (kU_0)^jΔ^{(j+1)} ≤ [2ek(1+w)^k]^{−1}`.
  * Private vertices make every attached hyperedge bring a new vertex.
    This removes the pseudoforest "closing" problem.
  * The price is the codegree factor `(kU_0)^j`.
* **Theorem 10.3 (hypergraph criterion).**
  * Degrees are handled by the Markov hub quarantine, as before.
  * The new hypothesis is (CD_k), on *maximal* codegrees at scale
    `(C_k(Σ+1))^{−j}`.
  * It is not circular: `C_k` depends on Σ only.

## (b) Exact conditional statements

* **Theorem 10.4 (PROVED implication).**
  * H_CD(θ) implies H_MIN(θ). H_CD(θ) asks for a quarantine of mass
    `T^{o(1)}` after which `w_ℓ≤T^{−ε}` and `Δ^{(j+1)}≤T^{−ε}` for
    `2≤j+1≤k−1`.
  * If H_CD(θ) holds for all `θ>κ`, then `W(p) ≥ (log p)^{1/κ−o(1)}` i.o.
    (modulo Thorner–Zaman).
  * For `θ>1/3`, H_CD holds and this recovers Thm 5.1.
* **Unconditionally, (a) gives nothing beyond exponent 3 (Prop 10.5).**
  * Neither the crude counts nor `F_I≤n^η` certify (W_k)/(CD_k) below 1/3.
  * Individual Type I bounds cannot see residue classes, so they never
    control codegrees.
  * The Haar side needs only averaged per-prime masses: Thm 9.2 gives
    `η/(1+η)`. The prime side needs codegrees as well, which is the
    precise asymmetry between the two sides.

## Self-review found and fixed a critical error

* The first draft of (b) used a residue-uniform "AP-TI*(κ)". The reviewer
  showed it is **false**: the hub residue (ℓ,−4) has `deg≫1/log ℓ`. It is
  withdrawn in the text, with the counterexample.
* Pushing this further gave **Prop 10.6 (PROVED)**. At every `θ<1/3` the
  vertices `(ℓ,−4d²)` give pair codegrees
  `Δ_{{v_1,v_2}} ≥ (c_θ−o(1))/φ(4d)` with `c_θ=log(1/(3θ))`, via the triples
  `ℓ_1ℓ_2ℓ_3≡−1 (4d)`, `D=d²`.
* **Assessment (not proved): codegree-level hub obstruction.** Assume a
  product-set quarantine-cost lower bound, which is not proved. Then no
  quarantine of mass `T^{o(1)}` makes (CD_3) hold, so Theorem 10.3, as
  proved, cannot certify any `θ<1/3` for ES. This is the codegree analogue
  of PO Prop 6.3.
* A heuristic count says the true private-family moments on `−4d²`
  clusters are harmless: `(c²e²/d)^h`. So **the open step is a sharper
  Lemma 10.2** that pays once per *shared* vertex, not a new arithmetic
  input.
* Also fixed:
  * Prop 10.5 is worded as an estimate failing to certify, not as a
    statement about the truth;
  * prime-power bookkeeping;
  * the codegree-quarantine "circularity" is downgraded to a statement
    about the Markov budget only;
  * the unsupported claim "AP-TI* ⇒ §9 AP-TI" is removed.

## Not done

* (c), attacking AP-TI on average over ℓ, was not started.
* The sharper Lemma 10.2 (shared-vertex accounting) is the natural next
  combinatorial step. A proof of the quarantine-cost lower bound in §10.4
  would turn that Assessment into a proved obstruction for the current
  lemma.

---

# Checkpoint 4: sharper Lemma 10.2 attempt → named gap; new Haar theorem (§11)

## Prime side: reduced to a sharper named gap (G_pair); exponent stays 3

* **The shared-vertex accounting does not help.** A dense `−4D` cluster
  with more members than shared vertices genuinely carries
  `(s·c/d)^{h−s}` private families. So the size-dependent codegree
  requirement `Δ^{(2)}≲1/L` is real, not an artefact of Lemma 10.2.
* Removing heavy pairs by adding them as events is consistent only if the
  heavy-pair mass satisfies `μ(t)≤ε/t` at `t≍1/L`.
* **Prop 11.4 (PROVED, PNT for fixed moduli).** The classes `−4D` (D with
  minimal root `D*`) give pair codegrees `≥(c_θ−o(1))/φ(4D*)`. Hence
  `μ(t) ≫ c_θ³ t^{−1}log(1/t)`, because of the divisor-type multiplicity
  `2^{ω(D*)}`.
* So the closure fails by a factor `log L` at every fixed θ<1/3. This
  Assessment rests on the proved lower bound.
* **Gap G_pair.** One needs either a minorant whose truncation level is
  not tied to the total event mass, or a joint (over D) treatment of the
  `−4D` hub classes that is cheaper than removing pairs one by one.

## New result: Theorem 11.3, the Haar side is now (essentially) polylogarithmic

* **Iterated bad-prime quarantine (Lemma 11.2).** Repeatedly quarantine
  every free prime whose per-prime event mass exceeds `c_0`. The process
  stops with `|𝓑| ≤ kS*/c_0`. Here
  `S* = Σ_{atoms} max_Π 1/φ(r_Π)` (Lemma 11.1). It has the same
  `T^{o(1)}` bound as Lemma 4.1, because `m_Π | gcd(M,4D+1)`.
* **Theorem 11.3 (PROVED).** `log(1/δ*(T)) ≪ (log T)^3(S*+1)`. This gives
  `T^{o(1)}` unconditionally, improving PO Thm 9.3's `T^{1/3+o(1)}`. Modulo
  ET Prop 1.4 it gives `≪(log T)^7 log log T`, which is PO's polylog Haar
  target and was previously only conditional on H_PP.
* EVIDENCE (`omega2_iterq.py`, T up to 10⁶): the iteration stops after
  2 rounds, `|𝓑|` = 99/171/345, and the local-lemma margin is wide
  (`max Σx ≤ 0.08`). These runs are finite-T certificates of the Haar
  bound.
* **Consequence for the prime side.** The per-prime conditions (G), (W)
  are free in every construction. Below 1/3 the only obstacle is G_pair.

## Please review hardest

* Lemma 11.2's counting step (each atom is counted at most k times, with
  its max-over-Π weight). This is the crux of Theorem 11.3.
* Lemma 11.1, i.e. that the Lemma 2.3/4.1 argument runs with
  `m = gcd(M,4D+1)`.
* That Theorem 11.3 really closes PO §9's open H_PP problem. PO's Thm 9.4
  needed per-prime bounds at *all* primes `>z`; we quarantine the
  `T^{o(1)}` exceptions instead.
* Suggested ledger: (H)10 Haar side → "`log(1/δ*)≤T^{o(1)}` (PROVED);
  polylog modulo ET Prop 1.4 (POINTWISE_OMEGA2 Thm 11.3)".

---

# Round-3 review repairs and paper update (workstream closed for now)

* **POINTWISE_OMEGA2, review r3 D1–D14.** All applied in one commit
  ("review r3 repairs D1-D14"):
  * D1: the iteration wording is now "one round of additions; the second
    pass adds nothing".
  * D2: no growth exponent is claimed for `|𝓑|`.
  * D3: the sharper form `(log T)^7/log log T` modulo ET.
  * D4: the per-prime part of H_CD(ii) is weakened to the constant level,
    which Lemma 11.2 makes automatic.
  * D5: the symmetrisation sentence in Lemma 10.2.
  * D6: general prime-power lifts.
  * D7: `Φ=∅` for `θ>1/3`.
  * D8: Prop 10.6 states which system it is computed in, and that it
    survives the `T^{o(1)}` extra quarantine.
  * D9: Prop 10.5 relabelled (upper bounds PROVED, non-certification
    Assessment).
  * D10: Prop 11.4 stated uniformly for `D*≤(log T)^A` (Siegel–Walfisz),
    with a note on the BV/BDH averaged form when L is not polylog.
  * D11: "if", not "iff". The claim is that pair-by-pair removal fails, not
    that every treatment fails.
  * D12: the §10.4/§10.5/summary claims that "a sharper Lemma 10.2 is the
    open step" are marked superseded by §11.4, which now carries the
    reviewer's derivation of the super-exponential dense-cluster count.
  * D13: `≫` instead of `≍` for the `−4d²` codegrees.
  * D14: the summary table's Haar column is updated to Thm 11.3.
* **paper/es-omega-note.tex.**
  * New Theorem `thm:iterq` [Proved; polylog form modulo ET Prop 1.4]:
    `log(1/δ*(T)) ≪ (log T)^3(S*+1)`, i.e. `T^{o(1)}` unconditionally and
    `≪(log T)^7/log log T` modulo ET. A compact full proof is included
    (S* via `m=gcd(M,4D+1)`, the iterated quarantine with
    `|𝓑|≤kS*/c_0`, LLL).
  * A remark follows it: the theorem makes the per-prime hypothesis
    unnecessary, and the prime side below 1/3 is limited by pair codegrees
    (Assessment). The numerical certificate `log(1/δ*(10^6))≤3.6·10³` is
    labelled EVIDENCE.
  * The abstract, the intro sentence ("Exponent 3 matches…"; it no longer
    claims this is the best Haar bound) and the summary of status are
    updated.
  * Clean pdflatex ×3: 24 pp, 0 warnings, 0 overfull/underfull.

**State at close.**

* Prime side: `W(p) ≥ (log p)^{3−o(1)}` i.o. (Thm 5.1). Below θ=1/3 the
  obstacle is the named gap G_pair (§11.4).
* Haar side: `log(1/δ*) ≤ T^{o(1)}`, polylog modulo ET (Thm 11.3).
