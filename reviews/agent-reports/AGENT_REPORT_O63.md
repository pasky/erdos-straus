# AGENT REPORT O63 — m/n witness modulus at exponent 1/4 (branch side-agent/mn-quarter)

Deliverable: `POINTWISE_MN.md` (§§0–7), scripts `scripts/mn_jacobi.py`, `scripts/mn_hard.py`,
`scripts/mn_greedy.py`, Replay in POINTWISE_MN.md. Not merged.

## Results

1. **Lemma 1.1 (PROVED, brute-forced on 11 values of m, M ≤ 5·10⁴).** For an atom `(M,D)`, M odd,
   with e = squarefree part of mD (t = its 2-adic bit): `(−mD|ℓ) = (−e|ℓ)` for ℓ | M;
   `(−mD|M) = −(2|M)^t` if `M ≡ 3 (4)`, `= (2|M)^t(−1)^{(e_o−1)/2}` if `M ≡ 1 (4)`.
   **For m ≡ 0 (mod 4) it is always −1** (OMEGA13 Lemma 3.1 verbatim); `M ≡ 7 (8)` atoms are
   always −1 for every m.
2. **Prop 2.1 (PROVED).** For every `m ≢ 0 (4)` there are infinitely many prime atoms `M = ℓ`
   whose event classes meet both square cosets (m=5: ℓ=29; m=6: ℓ=5 hits the squares). So the
   square-class process fires and no "fixed quadratic pattern" coset replaces it. Square-consistent
   atoms are ~15–19% of all atoms for m = 5, 6, 7, 10.
3. **Thm 3.1 (m ≡ 0 (4); PROVED modulo (G), NT, fundamental lemma, OMEGA10 Thm 3.4 — substitution
   proof).** Haar exponent 3 (`𝓛³/log𝓛 ≪ log(1/δ*_m) ≪ 𝓛³(log𝓛)^5`) and
   `W_m(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o. Only m-specific changes: Lemma 1.1(d), NT
   with `Q_2(n) = mn−1` (ρ(p)=1 at p|m), progressions mod mn.
4. **Prop 3.2 (PROVED mod fundamental lemma).** Haar lower bound `≫ 𝓛³/log𝓛` for every m ≥ 4.
5. **Lemma 4.1 (PROVED mod (G)).** The prime-side transfer (OMEGA13 I3 / O9 Thm 1.1) works for any
   unit class r: if the exceptional character has `χ_1(r) = −1` its term is positive.
6. **Thm 5.1 (CONDITIONAL on ADM_m(K,Q_0)).** For `m ≢ 0 (4)`, the 1/4 and Haar-3 conclusions
   follow from one hypothesis: the *admissible unit process* (reveal digits uniformly among classes
   that do not complete a consistent atom, after a uniformly random hard prefix mod a fixed `Q_0`)
   has per-prime drift `Λ(ℓ) = ∏(1−f)^{−1} ≤ K` with probability ≥ 7/8. Implication proved by
   replacing OMEGA13's `2^{u}` potential by `∏ K/Λ` (supermartingale, pair potential checked).
7. **Evidence (§6).** Greedy full-quarantine runs (all ℓ ≤ T, T up to 3·10⁵, m = 5,6,7,9,10,11,13):
   max per-prime drift ≈ 4, attained at ℓ ≤ 19; `f_ℓ ≤ 0.55(log ℓ)³/ℓ` for ℓ > 50. Without a
   prefix, m = 7 dies at ℓ = 3 in 2/40 runs (2-adic digits) — hence the prefix.
8. **Cor 6.1 (unconditional fallback, every m; PROVED modulo ET + (G) + OMEGA10 — substitution
   proof checked line-by-line by a deep-mode subagent, spot-checked).** OMEGA12's class-of-one route
   gives exponent 1/5 and Haar `≪ 𝓛^5 log𝓛` for every m (incl. 5/n), improving TRANSFER's 1/7.
   Needed changes: ET Thm 7.1 with root bound C = 4 (mdx²+1 has 4 roots mod 2^k — verified), the
   2-adic coordinate in the graded quarantine for odd m (example m=5, M=464, D=3 — verified),
   parity assertions replaced by `ℓ ∤ mad`.

## Answer to the brief's key question
`(−mD|M) ≡ −1` iff `m ≡ 0 (mod 4)`. That is exactly where the 1/4 machinery breaks: for
`m ≢ 0 (4)` (Sierpiński's 5 included) OMEGA13 Lemma 3.1 fails, and the only missing input is the
existence of a bounded-drift random hard class (ADM_m), which numerics support. "Hard" for m/n:
Type-II-hard modulo Q, `H_m(Q)`; for `m ≡ 0 (4)` it contains all squares; for `m ≢ 0 (4)` it is not
a union of square cosets (`H_5(840)` is `{1,3,5} mod 7`).

## Items for the reviewer
* Thm 3.1 and Cor 6.1 are substitution proofs; please check them against OMEGA13 §§3,5 / OMEGA12.
* Thm 5.1's supermartingale: the stopping-before-violation device and the pair potential (§5 (d)).
* Lemma 4.1: confirm that O9's Case A is the only place where `χ(r)` enters with a sign.
* I did not verify any literature statement about which residue classes of 5/n are covered by
  known (Type I + II) identities; §3 only uses the Type II hard sets computed by `mn_hard.py`.

## Next steps (if sent back)
Prove ADM_m at least for medium/large ℓ (second moment of completed-atom counts; needs a Shiu-type
divisor bound in progressions to smooth moduli), and settle the small-prime prefix rigorously.
