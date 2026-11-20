# Hostile cross-review: `notes/z78/PROTH_ALLM.md` and `notes/z78/PROTH_RIGIDITY.md` (branch `side-agent/z78-proth-allm`, `git log main..`)

**Reviewer:** Claude (Anthropic), running in Claude Code as the requested cross-lab Opus reviewer. The harness does not
show me the exact model ID, so I do not state one. There were no provider or auth errors.
**Scope of review:** all 12 commits since `main` (b40458745). I re-derived §§1, 2, 4 and 5 of PROTH_ALLM by hand and
attacked the quantifiers. I audited the checker `scripts/z78_proth_check.py` line by line. I wrote independent replays
(`scripts/z78_opus_xreview.py`, `scripts/z78_opus_thm4_pari.py`) and re-proved PROTH_RIGIDITY §§1–4.
**Nothing here asserts ES for all m at all s.**

## 0. Verdict

| item | verdict |
|---|---|
| Thm 1 (ladder, infinitely many h, core s≡0 mod P(h)) | **Correct.** Re-proved; ladder replayed literally for h=5,11,17 |
| Thm 2 (cubic n=ky³+1, h=7^i) | **Correct.** Replayed at h=7 and h=49. It is an explicit *polynomial identity in y* (see F5) |
| Thm 3 (full families m=7,8,9,10) | **Accept (computer-assisted).** Checker sound; independent big-integer replay of every row (M rows: residue + Mordell) |
| Thm 4 (exact core criterion) | **Correct.** Both directions re-proved; brute-force exactness at h≤15 for every unit j |
| §4 compressed certificates | **Sound.** X^ℓ transfer re-proved and replayed at X-level for h=3,5,7,9; actual integers at h=3 |
| §4 index pattern 1/2/6 | EVIDENCE, as labelled. It extends through h≤135 (tested set). The lower bound ≥2 for 3∣h is *provable* (F6) |
| Prop 5, Prop 6, general multipliers | **Correct.** Exhaustive and random replays agree |
| PROTH_RIGIDITY Prop 1, Thms 2–3, Cor 4 | **Correct** relative to the cited theorems. Two small expository gaps (F10) |

The mathematics holds up. There are form and scope defects, and one must-fix (F1). The defects are listed in §6.

## 1. Thm 1: hand re-proof and attacks

* **Units.** If p | H and p | 1+2^a, then −1 ∈ ⟨2⟩ mod p. That group has odd order (dividing h), so this is impossible. ✓
* **Ladder.** Start from odd e, a unit mod h. We need je′≡w with e′=ef, so f ≡ w(je)^{-1} mod h. This f is a unit,
  and it can be made odd by adding h. The used factors are Φ_{2d}, d | e″, d ∤ e′. A later step uses only d ∤ (its own
  e′), which is a multiple of the current e″. So the steps are disjoint. ✓ Mod H the block is y_{je″}/y_{je′}. ✓
* **The −1 identity.** y₃/y₁ = 9·3^{-1} = 3 = y₁, using 3 ∤ h and 3 ∤ H (H ≡ 1 mod 3 for odd h). Next,
  2y_{−1} = 2+2^h ≡ 3, so y₁/y_{−1} = 2. Finally ∏_{i<b}(1+2^{2^i}) = 2^{2^b}−1 ≡ 2^{h−1}−1, using 2^b ≡ −1 mod h, and
  2(2^{h−1}−1) = 2^h−2 ≡ −1. ✓
* **Assembly.** P = 4L. For P | s, s/L is ≡ 0 mod 4, and stripping the h-primes leaves r ≥ 4 with r mod h a unit.
  s/(rL) is odd, so X^L+1 | 2^s+1. We have A ≡ 1 mod 16 and A ≡ −1 mod H. Since u ≡ 14 mod 16 (h ≥ 4), 7u−1 ≡ 1 mod 16,
  so A ≡ 7u−1 mod 16H. Then t ≡ 7 and v ≡ 7 mod 8, and 8 | n+t. ✓
* **Direct triple.** 4AuD = Au(tv−1) = A(A+1)v − Au = (A+1)(n+u) − Au = (A+1)n + u. ✓ This is unconditional; the
  good-word theorem is not even needed.
* **Quantifier attack.** The theorem covers only the core s ≡ 0 mod P(h), which has density 1/P. The ladder replay gives
  L with 6, 23 and 27 digits for h = 5, 11, 17. So "effectively computable" P is astronomically large. The note does say
  "P need not be small", but stating the magnitude would prevent over-reading. The no-cover clause uses EXPONENT_COVERING
  Thm 1.4 on the sub-family s ≡ 0 mod P. It is valid because every s divisible by P and by the menu's unit orders is
  allowed. ✓
* **Example family.** For h = 4^i+1: 3 ∤ h and 2^{2i} ≡ −1. ✓

## 2. Thm 2 (cubic): re-proof and attacks

* p | H implies 7 | ord_p(2) | p−1, so (−7/p) = (p/7) = 1. Since −7 is a unit mod p, the roots of z²−z+2 lift by
  Hensel. gcd(1680, H) = 1 because h is odd, 4 ∤ h and 3 ∤ h. ✓
* With A = y²−y+1: A ≡ −1 mod H, A ≡ 1 mod 16 and v = k(y+1) ≡ 7 mod 8. The word and triple are as in §1. ✓
* **Closure.** Take the profinite y = z at p | H and 0 elsewhere. Then n ≡ 1+z³ ≡ (z−1)² mod p, using z² = z−2, and
  this is nonzero. The 2-component is 1. ✓ The proof of EXPONENT_COVERING Thm 1.4 is family-agnostic (compact closure
  plus clopen classes), so it transfers to the tail of {y in the progression}. ✓
* **Replay.** h=7: z=105, y₀=13440. h=49: 2^49−1 = 127·4432676798593, z = 385643149929560, y₀ = 293119618929011280.
  Three y-values each were checked with an exact ES triple, n ≡ 1 mod 840, and n a nonzero QR mod every p | H.
* **Substantive caveat (F5).** x, y, z = ADn, uD, AuD are *polynomials in y* on the progression. Theorem 2 is therefore
  one polynomial ES identity on a cubic curve. Its interest is that its n-closure meets the profinite unit squares, which
  is consistent with Mordell–Schinzel because y is not a polynomial in n. "No finite ET cover" is thus no evidence of
  difficulty for this family. Say so. I checked the naive quadratic analogue (A = y²+1): it degenerates to a fixed
  linear class n ≡ −(u+k) mod uk. So the cubic is the first non-degenerate shape of this recipe, not a triviality.

## 3. Thm 3: checker audit and independent replay

* **Checker audit.** All checks pass.
  * Each non-X rule's modulus is frozen at the first s₀ ≥ 64 in its class via k2^{s₀}(2^P−1) ≡ 0 (mod M). This gives
    periodicity for all s ≥ s₀ in the class. ✓
  * W: 8A modulus; R1 = R2 = 0; v mod 8 from the reduced n; v ≥ 2 via k2^64+1+u ≥ 2A; five-slice test. ✓
  * II: gcd(b,f) = 1 is automatic from b | f+1. I derived b′ = be − a > 0, which holds because n ≥ k·2^64 ≫ f ≤ 29459;
    the checker does not assert it (F11). ✓
  * K: the modulus 4K₀f vs 4·lcm is correct for b ∈ {0,1}. ✓
  * X: the representative X = 2^{a+4h} mod 16H is ≡ 0 mod 16 and ≡ 2^a mod H. Φ_{2d} is computed by the Möbius product,
    whose factors are all units mod 16H. ✓
  * `left == []` holds in all four period files. ✓
* **Independent replay** (`scripts/z78_opus_xreview.py periods`, no imports from z78_proth_*):
  * Coverage was recomputed by an OR of per-modulus big-integer patterns (m=7,8,10) or by slice painting (m=9), plus
    300k random membership probes: **0 misses** in each file.
  * The five-slice triples are the explicit ones of DEDEKIND_ES Cor 1.2 / Thm 4.5, and the II and K triples are the
    explicit formulas.
  * **Every row** was evaluated at its first 2 (K: 3) representatives s ≥ 64 (those ≤ 2.5·10⁶) as an exact
    big-integer ES triple. This was 5 X exponents per family, including s/e = 4h, which exercises the stripping.
  * For s = 64..1199 plus 150 random s < 60000, the first-matching row was checked the same way.
  * M rows were checked as residue only (non-unit-square mod 840) and scaled when 3, 5 or 7 divides n. They rely on
    Mordell.
  * Totals per family (per-row): m=7 M22 D8 II14 W26 X5 K3; m=8 M16 D30 W78 II38 X5 K257; m=9 M18 D16 W48 II14 X5 K281;
    m=10 M16 D20 W58 II20 X5 K9. **All pass.**
* **Author's replay reproduces byte-for-byte:** `ulimit -v 1500000; uv run --offline --no-project python -B
  scripts/z78_proth_check.py small groups census period-…` equals `data/z78/proth/replay.txt` (2 s).
* The rows are periodic, the moduli are frozen, and s < 64 is checked directly. Thm 3 is therefore proved for m = 7..10
  and all s ≥ 0, relative to Mordell and the cited rules. It is computer-assisted and not Lean.

## 4. Thm 4 and §4: re-proof and attacks

* **Necessity.** Write d = p^α b with α > v_p(h). Only β ∈ {α, α−1} survive in Möbius, which gives pairs
  (B_{jp^αe}/B_{jp^{α−1}e})^{μ(b/e)}. Both indices have p-part p^{v_p(h)} in their gcd with h, so each pair lies in R. ✓
  For d | h, multiplying the indices by a unit j preserves the gcd, so the class is E_d. ✓ Repeated primes are fine. ✓
* **Sufficiency.** R is generated by {B_a/B_c : a in the gcd-g orbit} for any fixed c in the orbit, here c = jg.
  Surjectivity of (Z/h)^× → (Z/(h/g))^× gives every numerator. (X^{gℓ}+1)/(X^g+1) = ∏_{e|g} Φ_{2eℓ}(X) for a fresh prime
  ℓ ∤ h. These are disjoint from the exceptional d | h (since ℓ ∤ h) and from other fresh primes. Each *use* needs its
  own ℓ (the note says this). ✓
* **Brute-force exactness** (`thm4`, Dmax = 1500, every unit j). The attained set equals R·{∏E_d} *exactly*, and every
  Φ_{2d}(2^j) lies in its predicted R-coset, for h = 3,5,7,9,11,13,15. h=9: |U| = 432, [U:R] = 6, attainable 360 < 432,
  core only with exceptional slots (c = 33, T = {1,3}). This confirms "h=9 needs exceptional slots". h=3 needs them too.
* **Compressed-certificate transfer.** Φ_{2d}(X^ℓ) has constituents {2dℓ} ∪ ({2d} if ℓ ∤ d), so the constituents are
  disjoint across d. ✓ `realize` builds the actual X-level index sets for every unit j from `exact-core.json`:
  * h = 3, 5, 7, 9 all give 7u−1 mod 8u, with distinct constituents.
  * Common degrees L have 4, 34, 188 and 41 digits.
  * h=3 gives actual-integer ES at s = 11220, 33660, 100980 (j=1) and 56100 (j=2).
* **Beyond the tables** (`scripts/z78_opus_thm4_pari.py`, my own HNF code on PARI znstar/znlog):
  * h = 3..61: [U:R] agrees with `exact-core.json` for all 30 values, and a core certificate exists for each.
  * h = 63..101 (odd), 105, 117, 135: [U:R] = 1 if 3 ∤ h, 2 if 3 ∥ h, 6 if 9 | h. A core certificate exists in every
    case. [U:⟨all B⟩] = 1 throughout.
  * This uses the same library as the author (PARI) but independent code. The factorisations are PARI's (pseudoprime
    level). This is EVIDENCE.
* **The lower bound is a theorem (F6).** If 3 | h then 7 | H. For 3 ∤ a, 1+2^a mod 7 ∈ {3,5}, and 3/5 ≡ 2 and 5/3 ≡ 4
  are squares mod 7. For 3 | a, 1+2^a ≡ 2. Hence R ⊆ ker(quadratic character mod 7), so [U:R] ≥ 2. The extra factor 3
  at 9 | h does **not** come from 73 alone: (B₂/B₁)^{24} ≡ 8 mod 73. Leave it as evidence.
* **Attack on "decides the entire core congruence".** This is true for the z77 recipe: unit source j after stripping,
  c | k, and products of distinct Φ_{2d}(X). It does not cover unstripped (non-unit) j or non-cyclotomic divisors. The
  note's "A negative decision would exclude only THIS congruence recipe" is adequate; F9 asks to name the stripping.
* **Magnitude.** The certificates' multiplicities reach 65535 (h=17), 262143 (h=19) and ~1.15·10^18 (max over h ≤ 61).
  The implied periods are products of that many primes, i.e. astronomically large.

## 5. §5 and PROTH_RIGIDITY

* **Prop 5.** Re-proved. F+C ≡ 0 mod H with F+C even forces C ≥ 2H−F > H, so C = k and c = 1. Then F = H−1 is even,
  a contradiction. ✓ Exhaustive replay (`prop5`): h ∈ {7,9,11}, B ∈ {1,3,5}, s = B·2^{4·ord_h 2}, all (r,e), all
  subsets, all c | k. No hit on −1. ✓ Wording (F7): "c=1 since every proper divisor of the odd k is ≤ k/3 < H".
* **Prop 6.** Four 2-adic cases re-derived; for example v₂(A) = 2 gives t ≡ −5 ≡ 3 mod 8. ✓ Replay: 161 divisor words,
  k < 1500, a ≤ 6. a ≥ 3 always gives a negative sign, and for a = 1, 2 the stated exact criterion equals the actual
  sign. This is a sign lemma only; it gives no existence of A.
* **General multipliers.** The dyadic test was re-derived: A ≡ c mod 2^{e+3}, v odd, t ≡ ((c+1)/2^e)H^{-1} mod 8.
  * Replay (`dyadic`): every odd k < 1200 with ord_H(2) odd, r ∈ {e+3, e+4, 2e+5}, E ∈ {1,3,5,9,15}, all c | k, all
    subsets. The prediction equals the actual sign on 165 realised words, the Jacobi symbol (tu−1/n) agrees, and the
    ES triple holds.
  * Example claim, non-Mersenne: H = 23 (h=11, k=47) has all 10 unit j solved and 84 actual-integer ES instances.
    H = 18631 = 31·601 (h=25, k=37263) has all 20 solved and 3 actual instances.
* **Sign criterion foundation.** 8 | (n+t)tuv ⟺ (tu−1/n) = −1 held on 62,722 random words with n ≡ 1 mod 4, and all
  five-slice triples were verified.
* **RIGIDITY Prop 1.**
  * Polynomiality, positivity on [0,∞), d₁ = P, d₂ ≤ 2P, d₃ ≤ 4P. ✓
  * The interpolation weights are scale-free. ✓ Finitely many Egyptian-fraction tuples. ✓
  * Rescaling: ρ → 0, the limit identity Σ1/G_i = 4 has a nonconstant G_i, contradicting positivity of the r_i. ✓
  * A bounded affine variety is finite (Chevalley). ✓
* **RIGIDITY Thm 2.**
  * Case 1: x^{k′/d} ∈ Q with gcd(k′,d) = 1 gives d | v_p(x). Then a_m = Dv^p with v integral, and the curves
    Y² = DX^p+1 (genus (p−1)/2) and Y² = D(4^rX⁴−1) (genus 1) give finiteness by Siegel. ✓
  * Case 2: unit-square class R mod M. ✓
  * **Gap (F10a).** Schinzel's theorem is stated for x, y, z ∈ Z[t] on n = Mt+R. The note has H_i ∈ Q[n] integral on
    the class. One line is needed: M·H_i(R+Mt) ≡ M·H_i(R) ≡ 0 coefficientwise mod M, hence H_i(R+Mt) ∈ Z[t], with
    positive leading coefficients. Also record in the Label that the Mordell/Schinzel statement is used via ET's
    quotation (EXPONENT_COVERING says it was "not accessed directly").
* **RIGIDITY Thm 3.** Induction re-checked: van der Waerden blocks, a recurring (triple, step) pair, finitely many t ≤ W,
  the finite H_i list, removal on j = hu, and the finite set of Lh. ✓
* **RIGIDITY Cor 4.** Correct. Wording (F10b): from Σ1/r_i(J) = 4, letting J → ∞ gives Σ_{const} 1/r_i = 4, hence
  Σ_{nonconst} 1/r_i(J) ≡ 0, which contradicts positivity. The current text says "remaining constant reciprocals" even
  when two of the r_i are nonconstant.

## 6. Actionable fixes

* **F1 (must).** `notes/z78/WILD_ES.md` is cited in §1, in §5 and in the STATUS delta, but it does not exist on this
  branch; it lives on the "z78 wild" branch, commit 450d0e304. Either merge it first or drop the density-one clause from
  the §0 STATUS delta. That clause is another lane's result and cannot be promoted from this note.
* **F2.** "Target B" is undefined in the repo. Define it in one clause or rename §2.
* **F3.** Make the §0 Label complete:
  * Thm 1 elementary, plus EXPONENT_COVERING Thm 1.4 for no-cover;
  * Thm 2 rel. QR and Thm 1.4;
  * Thm 3 computer-assisted rel. Mordell, DEDEKIND_ES Thm 4.5/Cor 1.2, THIN_CYCLO §1, z77 §2;
  * Thm 4 rel. Dirichlet;
  * §4 rows CERTIFIED (engine: standalone Python checker; discovery: PARI);
  * Props 5–6 elementary.
  Write "EXPONENT_COVERING Cor. 1.5" explicitly in §3.
* **F4.** "independently checked periods" overstates the checking: it was the same lane's checker. Say "checked by a
  standalone verifier", cite this review's independent replay, and set Review: "cross-model (this file)".
* **F5.** State in Thm 2 that the triple is a polynomial identity in y, so the no-cover clause is not a difficulty
  claim.
* **F6.** Replace the "EVIDENCE only" index sentence. Use: "[U:R] ≥ 2 when 3 | h (PROVED, quadratic character mod 7);
  equality pattern 1/2/6 EVIDENCE for h ≤ 61 (author) and for h ∈ {63..101 odd, 105, 117, 135} (Opus replay)". Consider
  stating CONJECTURE: [U:R] = 1 whenever 3 ∤ h. This would make Thm 1's hypothesis 2^b ≡ −1 (mod h) unnecessary for
  the core.
* **F7.** Prop 5 wording: see §5.
* **F8.** Give the magnitudes of P: ladder L of 23–27 digits at h = 11, 17, and certificate multiplicities up to 2.6·10⁵
  fresh primes at h = 19. This stops "effectively computable" being read as practical.
* **F9.** In Thm 4, "the entire z77 core congruence" → "the z77 core congruence (unit source after stripping h-primes,
  c | k, distinct Φ_{2d})".
* **F10.** Rigidity: add the Z[t] reduction line and the Label provenance (a), and fix the Cor 4 wording (b). Set
  Review: cross-model (this file).
* **F11 (optional).** In the checker, assert the II positivity b′ > 0 at s₀, and drop the vacuous `unit_j` test
  `pow(2, j*j^{-1}, Q) == 2`. That test checks nothing about the X^ℓ transfer.

## 7. Triage recommendation (for the orchestrator)

* Thm 3 qualifies to replace the STATUS §1C row "1 ≤ m ≤ 6" by "1 ≤ m ≤ 10". It is computer-assisted, not Lean, and
  this review is the cross-lab review.
* Thm 1 supports one clause of the "infinitely many non-ET-coverable families" sentence. The clause must say "ES on the
  core s ≡ 0 mod P(h) for h = 4^i+1 (m = (h+1)/2)", not all exponents.
* Thm 2 and Thm 4 are FRONTIER-level (method), not STATUS.
* RIGIDITY is BARRIER-SCOPED, as triaged.
* No claim here bears on ES in general or on all m at all s.

## 8. Replay (from repo root)
```
ulimit -v 1500000
uv run --offline --no-project python -B scripts/z78_opus_xreview.py all dyadic realize        # ~56 s, peak 610 MB
uv run --offline --no-project --with cypari2 python -B scripts/z78_opus_thm4_pari.py $(seq 3 2 61)   # vs exact-core.json
for h in 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 101 105 117 135; do
  timeout 240 uv run --offline --no-project --with cypari2 python -B scripts/z78_opus_thm4_pari.py $h; done
uv run --offline --no-project python -B scripts/z78_proth_check.py small groups census period-7-55440.json \
  period-8-12252240.json period-9-411863760.json period-10-55440.json   # == data/z78/proth/replay.txt
```
