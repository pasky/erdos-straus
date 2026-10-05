# AGENT REPORT O41 — `paper/es-window-note.tex` (window statistic note)

Branch `side-agent/window-paper`. Draft complete: `paper/es-window-note.tex` / `.pdf`
(20 pages, pdflatex clean: no warnings, no undefined references). Authorship
"Anonymous", date line "Draft, internal checks only, not externally refereed",
conventions of `pointwise-obstruction.tex`. Astra is not cited (the source notes do
not use it for this material).

## Contents and labels

| § | content | label in the note | source |
|---|---|---|---|
| 2 | window criterion (Thm 2.2, proof incl. two-unit-fraction lemma), ES ⟺ a_min<∞; window reciprocity; clean ⇒ fail; parity of bad part; window 3 exact | PROVED | POINTWISE_SIZE §8.1–8.2, notes Lemma 77.1 |
| 3 | half-set lemma | PROVED | XWIN Lemma 1.1 |
| 4 | large-sieve lemma (|S|≤4XV, proof from the arithmetic large sieve + Markov); fixed-set stacking Thm 4.2; tail Cor 4.3; uniform Thm 4.4 (Z≤C₀ log log N); remark (log log N)² tail, priority to notes §14 for the (log N)^θ range (not reproduced) | PROVED (Thm 4.4 modulo SW) | XWIN Thm 1.2, Cor 1.3, Thm 1.5, notes Lemma 12.1 |
| 5 | cited results, each with checked / from-memory note | — | — |
| 6 | Thm W1 with full proof; FHRSS cross-route; numerics; Cor (exact order 3/2) | PROVED modulo cited LS, Mertens-AP, BV, semi-linear sieve | WINDOW §2 |
| 7 | Thm W2 on EH, full proof; Cor (exact order 2 on EH); FI09/Sedunova/Nath–Xie precedent remark | CONDITIONAL (EH) | WINDOW §4 |
| 8 | quadric Lemma 8.1; Thm P1 (same sieve data, A⁻ never clean, A⁺ ≫x/(log x)^{3/2}); joint version restricted to (+,+) vs (+,−) | PROVED | WINDOW2 §§1–2 incl. R29 M1 restriction |
| 9 | random model (Assessment); Dickson remark (part (a) PROVED, unboundedness CONDITIONAL); data (EVIDENCE); X_win(10) (CONJECTURE); model fakes (MODEL) and certified LP fake with full scope paragraph (weakest EVIDENCE) | as stated | POINTWISE_SIZE §8.3–8.5, XWIN §1.3, WINDOW2 §3 |

## Changes relative to the source notes (deliberate)

* All **upper-bound sieving** (S2 of WINDOW §2.1 and the dimension-5/2 bound in
  W2) is now done with the note's own Lemma 4.1 (large sieve + Markov) instead of
  citing Selberg/HR Thm 3.12. This removes one citation; the cost is crude factors
  `(a/φ(a))^2`, `(a/φ(a))^3`, absorbed by the Euler products over m
  (`Σ(m/φ(m))^k/m ≪ (log)^{1/2}` on a density-1/2 set of primes).
* W2's sieve sequence is made an honest integer sequence `e_p` (P₃-part of n₃ times
  P₇-part of n₇; well defined since gcd(n₃,n₇)=1), so the cited linear sieve applies
  literally.
* W2 remainder: explicit Cauchy–Schwarz against `max_b|E|≪x/φ(k)` with EH at A=10
  giving `x/(log x)^3`.

## Cited from memory (not checked against a primary source here)

1. Arithmetic large sieve `|S|≤(X+Q²)/H(Q)` (Montgomery 1968; Montgomery–Vaughan 1973).
2. Semi-linear lower sieve, general hypotheses and the uniformity of `o(1)` in s∈[1,2]
   (Iwaniec 1976 / Opera de Cribro Thm 11.13). Only its *application* with this f(s)
   was checked (Teräväinen (6.4), archived).
3. Linear lower sieve `f₁(s)=2e^γ log(s−1)/s`, 2≤s≤3 (HR Thm 8.4 / OdC Thm 11.13).
4. Siegel–Walfisz (MV Cor 11.21 numbering from memory), BV (IK Thm 17.1 numbering
   from memory), Mertens in APs.
5. FI09 statement (Thm 2, Assumption A(θ)) was checked against the archived txt;
   Sedunova's and Nath–Xie's statements checked against archived txt; FHRSS Thm 1.1(2)
   checked against archived txt (statement only).
6. Mihnea–Dumitru verification to 10^18 (as cited in `pointwise-obstruction.tex`).

## Points a referee should check

1. Thm 2.2(3): converse direction, especially the case p | d₁ (symmetric to p | d₂).
2. Lemma 2.3 (reciprocity) for r=2 and the range 0<a<3p; Lemma 2.4 uses `(−p/a)=−(x_a/a)`.
3. Half-set lemma: the case g=h (classes of distinct primes) and the count β(a) in (5).
4. Lemma 4.1: the Markov step (law of q is the product Bernoulli law, E log q = Λ) and
   the constant 4 with Q=X^{1/2}.
5. Thm 4.2: distinctness of the sieved classes (ℓ>y=2max A+24), ℓ∤p for p>N/2>z,
   Mertens-AP giving exactly (1+J/2)log log N.
6. Thm 4.4: SW range (moduli ≤ C₀(log y)^{1/2} with y=exp(L²)); total SW error over
   O(L²) classes; the bookkeeping `e^{−(L−3log L−C)} = e^C L³/ℒ`.
7. Remark after Thm 4.4: `Σ_{a≤Z,a≡3(4)}φ(a)~Z²/π²` and the optimisation giving
   π²/(64 log 2). (Stated without proof.)
8. W1 Step 1: that c₁ is independent of ε (only the o(1) and the BV remainder depend on ε,
   absorbed for x≥x₀(ε)); s∈[1+ε,2].
9. W1 Step 4: the bound `a/φ(a)≤4m/φ(m)`; `m≤x^{2ε}`; log y≥(log x)/3; Euler product
   inequality `(1−1/ℓ)(1+ℓ²/(ℓ−1)³)≤1+3/ℓ²` (ℓ≥5).
10. W2: the integer sequence e_p and `|r_d|≤τ(d)max|E|`; (Ω₁) from Mertens mod 3 and 7;
    s∈[2+ε,3]; the T^{(q)} sieve (classes 0, q/a, (q−q')/a; ξ=y^{1/20}<z); the factor
    `(1−3/ℓ)^{-1}≤(1−1/ℓ)^{-3}(1+6/ℓ²)`; that m may be even for q=7 (a/φ(a) bound still holds).
11. W2's union bound `N_{3,7}≥S−T₁−T^{(3)}−T^{(7)}` (a p with both windows carrying 2 bad
    primes is subtracted twice, which is harmless).
12. Thm P1(1): the congruence bookkeeping (n₃≡1 mod 5, 3,7∉P₃) and that both signs give
    one reduced class mod 840d; the "consequently" paragraph (what exactly "sieve data
    only" means, OdC Ch. 11 axioms).
13. Remark 8.3 (joint): main term 3li(x)/φ(840d₁d₂) for both B^±; vanishing for
    gcd(d₁d₂,30)>1.
14. Lemma 8.1: primitive-norm characterisation, (−7/r)=(r/7), 2 splits in Q(√−7).
15. Remark 9.2 (Dickson): part (a) proof; the admissibility of the tuple is delegated to
    POINTWISE_SIZE Prop 8.4 (not reproved).
16. Remark 9.6: that the summary of the LP model (numbers 12769, 89×89, 2.6e−15, 0.744,
    θ₂∈(0.5,0.7], 10^5 mass ratio) matches WINDOW2 §3.5–3.7 and the scope paragraph is
    not weaker than the source's.
17. Numerical statements in Remarks 6.4, 9.3 vs `scripts/window_w1.py`,
    `pointwise_size_amin.py`, `xwin_tail_table.py` (not re-run by me).

## Not done / caveats

* No numerics re-run (all numbers copied from the reviewed notes).
* Not included: POINTWISE_SIZE Lemma 11.3 (failure never congruence-forced), XWIN §2
  window-tail proof (only referenced, priority to notes §14), WINDOW Prop 7.2 and the
  switching-cap discussion of WINDOW2 §§6–7 (one sentence only).
* `paper/README.md` not updated (left to the parent to avoid merge conflicts).
* The note has had no hostile review yet.
