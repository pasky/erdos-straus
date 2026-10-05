# AGENT REPORT O50 — `paper/energy-dnf-note.tex` (branch `side-agent/energy-paper`)

**Deliverable.** `paper/energy-dnf-note.tex` / `.pdf` (15 pp. amsart 11pt: 14 pp. text + references),
"An energy bound for avoidance indicators, and Fourier tails of DNFs over
product spaces", author "Anonymous", Draft v1. A standalone combinatorics/TCS
note. Check script: `scripts/energy_note_check.py` (exact rationals; output
`data/energy_note/check_seed1.txt`, ALL CHECKS PASSED, ~6 min, one core).

Replay:
```
(ulimit -v 8000000; timeout 1200 env PYTHONPATH=scripts uv run python scripts/energy_note_check.py 1 1)
cd paper && pdflatex energy-dnf-note.tex && pdflatex energy-dnf-note.tex
```

## Content map (source → note)

| Note | Source on main | Label |
|---|---|---|
| Thm 1.1 (G_F ≤ 1 if all w_E ≤ 2) | OMEGA10 Cor 3.5; es-subexp-note Thm 6.5 | PROVED |
| Cor 1.2 energy tail, now with factor `P(F=0)(2−P(F=0))` | OMEGA10 Cor 4.1 (refined: uses `‖F^{=∅}‖²=(EF)²`) | PROVED |
| Cor 1.3 DNF: `W^{>t} ≤ 4p(2−p)2^{−(t+1)/k}`; `Σ2^{|U|/k}‖g^{=U}‖² ≤ 1+4p`; `I ≤ (4k/ln2)p`; q-ary set-valued literals | OMEGA10 §4 "Boolean form", R38b D3/D4c | PROVED |
| Lemma 2.2 (identities), Prop 2.3 (single event; threshold 2 necessary) | OMEGA10 §2 | PROVED |
| Lemma 3.1 cover bound | OMEGA10 Lemma 3.1 | PROVED |
| Lemma 4.1 polarization, Lemma 4.2 matching bound, Thm 4.3 (Q ≤ ∏_M(w−1), equality on matchings) | OMEGA10 Lemmas 3.2–3.3, Thm 3.4 | PROVED |
| Prop 6.1 base 2^{−1/k} sharp (incl. biased Boolean cube) | R38b §3.1; es-subexp Rem. sharp | PROVED |
| Ex 6.2 parities: uniform-cube rate between 3^{−t/k} and 2^{−t/k} | R38b §3.2 | PROVED (example); truth OPEN |
| Ex 6.3 adding an event can increase G (MONO false) | OMEGA10 §2 | PROVED (exact sign in script) |
| Conj 6.4 (C-exp), Conj 6.5 (FM) | OMEGA10 §2, §3 | CONJECTURE (evidence: internal) |
| Thm 7.1 filtration bound, Cor 7.2 modulus tail | OMEGA11 Lemma 1.1/Cor 1.2; es-subexp thm:filtration | PROVED |
| Rem 7.3 (ρ ≥ 1/log₂(1+ln2) ≈ 1.316 suffices instead of 2) | OMEGA11 Lemma 1.1 Remark (i) | PROVED (proof written out: superadditivity of convex `2^{x/ρ}−1`) |
| §8 application | es-subexp-note v3 (cited, not reproved) | Expository; rates "modulo Gallagher + ET" as in es-subexp |

## Points for a referee

1. **Novelty claims.** The note says "we believe new, no priority claim" and
   lists exactly what was checked (Lecomte–Tan and Tal checked online by R38b
   earlier; everything else from memory, flagged inline). Items flagged as from
   memory: O'Donnell's constant `2·2^{−t/(20w)}` (§4.4), Mansour'95 using
   `O(w log 1/ε)`, Boppana's `I ≤ 2w`, bibliographic data of [Boppana],
   [Mansour], [Tal] (TODO(verify) comment in the bib). A real literature search
   (sharp switching lemmas, Rossman, Fourier growth, noise operators with ρ>1 /
   "reverse" hypercontractivity) is still needed before submission.
2. **New refinements vs main** (please check): the factor `a(2−a)`,
   `a=P(F=0)`, in Cor 1.2/1.3 (from `Σ_{U≠∅} λ^{|U|}‖F^{=U}‖² ≤ 1−(EF)²`), and
   `Σ_U 2^{|U|/k}‖g^{=U}‖² ≤ 1+4p` (via Lemma 2.2(c), `G_h ≤ 2p`). Both are
   one-line consequences of Thm 1.1; both are checked exactly in sections C/D of
   the script.
3. **Prop 6.1 for Boolean DNFs**: the sharpness family is realised by p-biased
   bits, so the base is sharp for width-k DNFs under *biased product measures
   on {±1}^n*, not only for large alphabets. This is stated explicitly.
4. **Statements quoted as numerics, not proved**: `sup_m En·2^j ≈ 2/√(2πj)`
   (R38b computation); "hill climbs found nothing better than parities";
   the evidence for Conj 6.4/6.5. All labelled "earlier internal computation".
5. **Example 6.3**: chosen as the smallest instance (`[8]^2`, λ=√2). The
   `[5]^3` instance is mentioned from OMEGA10 without a re-check in the script.
6. **§8** is an exposition of es-subexp-note v3 (junta term via Cor 7.2 and the
   Bazzi–Razborov sandwich). It explicitly does not attribute the exponent 1/5
   to the energy bound alone, and says that in v2 the junta term was one of the
   two largest-order terms (the other being the quarantine), per OMEGA10 Thm 4.2.
7. **Length** 14 pp. text + 1 p. references (target 8–14).
8. Possible weak spot for a hostile reader: the "noise operator with ρ>1"
   framing in §1 (`G_F(ρ²)=‖T_ρF‖²`) — correct but only a remark; no claim is
   made about related literature.

## Not done / open
* Systematic literature search (no internet).
* Uniform-cube optimal rate; depth-3/AC0 analogue; sparsity (listed as open problems).

## Self-review (review subagent, deep mode) and repairs

No FATAL; core argument (polarization, deletion–contraction, matching
expectation, refinements, sharpness/Stirling, parity rate, filtration) verified.
Repairs applied:
* **M1** Thm 7.1: domain made explicit (`0 ≤ v_ℓ(E) ≤ f_ℓ`, offsets `i_0(ℓ) ≥ 0`;
  `v ≤ i_0` fixes nothing). Counterexample to the unrestricted statement
  (negative v) noted by the reviewer.
* **M2** CNFs: refined bounds hold with `p = P[h=+1]` (probability the CNF is
  false), not `P[h=−1]`; the `4·2^{−(t+1)/k}` bound unchanged.
* **M3** §8: Haar measure on `Ẑ^×` (units / fibres `1+ℓ^aℤ`), as in es-subexp.
* m4: `c_y` restored with the condition `supp 1_𝒥 = V`; contraction weights
  qualified (`J ∋ v`); factor 1 when `v ≤ i_0`.
* m5: script now checks the endpoint bounds `1+4p` and the influence bound
  (exact for k=1, float with 1e-12 slack else), and Thm 7.1 with random offsets
  `i_0 ∈ {0,1}`; §9 says the parity rates are printed, not asserted.
* m6: conjecture evidence described as floating-point / numerical LP; C-exp
  tested only in the exponential form.
* m7: "contraction" wording fixed (`‖T_ρF‖ > ‖F‖` for nonconstant F).
* m8: overfull boxes removed (0 remaining).
Script re-run after repairs: ALL CHECKS PASSED (`data/energy_note/check_seed1.txt`).

## Response to referee R50 (`reviews/energy-dnf-note-review.md`) — Draft v2

* **D2** (influence overstated): new Remark 5.1 proves the elementary
  certificate bounds `I ≤ 2kp` (uniform) and `Σ_v‖L_v g‖² ≤ 4kp` (product
  measures); §1 now says our `(4k/ln2)p` is *weaker* by `2/ln2` resp. `1/ln2`,
  and that `I ≤ 2w` (Boppana) / `I ≤ w` (Amano) are known (from memory, flagged).
  `I[g]` is now defined inside Cor 1.3.
* **D3**: `2/√(2πj)` restated as a (heuristic, unproved) j→∞ asymptotic, with
  the referee's numbers (0.2255 vs 0.2523 at j=10; 0.0876 vs 0.0892 at j=80).
* **D4**: added: extremal measures have atoms `p→0` depending on t; the base is
  sharp for the sup over all product measures; for a fixed measure with atoms
  bounded below the optimal rate is open.
* **D5**: `[5]^3` instance specified (48 points with exactly two nonzero
  coordinates, `A={x=(0,0,0)}`, λ=2^{1/3}, 0.75406→0.75467); now checked in the
  script (section F5, 50-digit arithmetic on exact rational components).
* **D6**: internal version history removed from §8; replaced by a self-contained
  remark on what the binary-encoding/LMN route costs (width and bit-length factors).
* **D7**: §8 now says `1_{E_j}u_j` has modulus ≤ `Te^τ`, cells of B ≤ `T³e^{2τ}`,
  `log d_i ≤ 3𝓛+2τ`.
* **D8** (literature): §1 now has a flagged "from memory, must be checked" list:
  Håstad 2001 (slight sharpening of LMN), Beame's primer / Razborov, Rossman's
  entropy proof, Håstad 2014; Furst–Jackson–Smith (product distributions) and
  Blais–O'Donnell–Wimmer (arbitrary product domains), with the explicit
  statement that a comparison is needed; Boppana/Amano; Fourier growth (Tal,
  Chattopadhyay–Hatami–Hosseini–Lovett) and noise operators with ρ>1. All new bib
  entries are covered by the TODO(verify) comment. **Still unresolved without
  internet** — must be done before external submission.
* **D9**: added a labelled heuristic paragraph re-deriving the switching-lemma
  constant `c_0 = 2eA ln2 ≈ 18.8` (A≈5, from memory), consistent with "20".
* **D10**: Remark 3.2 now contrasts `N=0` with LT's *indicator*
  `1[V covered]=1` (charge `2^{|V|}`), citing LT Fact 9.
* **D11**: `microtype` loaded with `expansion=false` (no font-expansion warning);
  `\emergencystretch` added; 0 overfull boxes.
* Readability (i)–(iii): I[g] defined in Cor 1.3; Lemma 4.2 notes induction over
  multisets and empty members of `𝒞/v`; Thm 7.1 proof states the per-prime
  consequence `λ_ℓ^{2v_ℓ(E)} ≤ 2`.

Length is now 16 pp. text + 1 p. references (the related-work list and the
influence remark added ~1.5 pp.). Script re-run: ALL CHECKS PASSED, exit 0.
