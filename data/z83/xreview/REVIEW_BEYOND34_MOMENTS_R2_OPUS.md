<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="9468e7d4e">
A separate reviewer subagent was asked to review the changes in `git log 9468e7d4e..`. Its request and review follow.

Request: review changes since 9468e7d4e carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus Wave z83 Lane 6 ROUND 2 review. Audit new §§8–11 and §0 of notes/z83/BEYOND34_MOMENTS.md. Independently recompute the W word ceiling, including square exclusion and cofactor bounds on units, and T's least-middle-letter binary phase and CRT model floor incl. list encodability, conditioning, BV/BT, sieve constants and all growing parameters. Verify literature UHL quantifiers (esp. BFT model Theorem 1.3 versus hypothesis 1.5), actual square-centre Q reweighting/scope, conditional calibration and EH/BCR limitations, and §11 normal order/area. Compare S with git show e78d466c0:notes/z83/ES_JUGULAR.md. Recheck no claim contradicts LM, no spurious implication to ordinary ES. Cap any replay at ≤15 minutes; use ulimit -v 6000000, timeout ≤1800, Python via uv run --offline --no-project python -B. Report every issue and verdict in full.

Commit log:
commit 0da3c193e5304c850441ae0546a1d8d662616d73
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:44:52 2026 +0100

    Match the native word ceiling and bound the least good middle letter on primes

 data/z83/b34_moments/word_checks.txt |  3 ++
 notes/z83/BEYOND34_MOMENTS.md        | 65 ++++++++++++++++++++++--
 scripts/z83_b34_words.py             | 95 ++++++++++++++++++++++++++++++++++++
 3 files changed, 159 insertions(+), 4 deletions(-)

Review:
**Verdict: ACCEPT WITH FIXES.** Commit `0da3c193e` adds the new §0 and §§8–11 of `notes/z83/BEYOND34_MOMENTS.md`, `scripts/z83_b34_words.py` and `data/z83/b34_moments/word_checks.txt`. I found no fatal error. The note contradicts neither z80 LM nor the `ES_JUGULAR.md` note at `e78d466c0`. It makes no implication to ordinary ES, the square controls, numerator eight or the (★)/U₇ zero controls. There is one statement-level error in the new Theorem T (a model "floor" (lower bound) that fails as worded), one literature misquote, and several labelling and scope problems.

## What I replayed (under 15 minutes in total, `ulimit -v 6000000`)
- **The new script.** `z83_b34_words.py` finished in 0.9 s and its output matches `word_checks.txt` exactly.
- **Word sign identities, separate engine.** I used SymPy's Jacobi and Legendre symbols on 27,423 interior words, at primes p ≡ 1 (24) in [10⁵, 1.4·10⁵] with 1 ≤ t < 120. All of the following held, with 0 failures:
  - identity (7), χ(xv) = χ(f) = (−x/f_odd);
  - the pair-chart sign formula (−v/x_odd)(−x/v_odd);
  - negative sign whenever 4 | t;
  - negative sign whenever 8 | tx (the U₇ case).
- **Proposition Q construction.** At X = 10⁴⁰, s ≡ 5 mod 8∏r gives t* ∈ [1.2X, 1.8X]. The modulus is below √X, and all 33 displayed shifts of t* are composite.
- **Calibration rates.** The rate hI(a/h) is 0.05324, 0.0382, 0.0157 and 0.0033 at η = .751, .8, .9 and 1. The quantity a·log(3a/h) is 0.92 at its largest (< 2), so cL² ≥ 1 holds. The rate equals 0.05324 at η = .751, consistent with z82's Proposition C.
- **§11 constant.** 3/4 + 4(1/6800 + 1/24336 − 977/25248600 + 1/34632) = 238447111/317627388 exactly, matching z80 (T).

## Substance, checked and correct
- **Theorem W (two-thirds word ceiling).**
  - (7): fv ≡ x mod p, (2/p) = 1, then reciprocity at p ≡ 1 (4) and p ≡ −x mod f. Correct.
  - 4 | t case: f ≡ 3 (4), every odd r | x has (r/f) = 1, and (2/f) = 1 when 8 | tx. So (7) = −1. Correct.
  - Square exclusion: the pair 4|t and recovered-endpoint U₇ refinements are handled by lifting to a large integer square. The gcd(S, f′) = 1 step works because a common prime would divide x, and (x, f′) = 1.
  - Opposite-colour refinements are handled by containment. That is legitimate.
  - The endpoint first moment (6) at a = 1 really does drop the (log log y)² of `EXSET_BEYOND_CRT.md` Lemma 2.3. The dyad sum Σ log V·min(1, (log y/log V)⁴) is ≍ (log y)².
  - Heavy leak: the Γ/Γ_old ratio is at most ∏_{p<r}(1−1/p)⁻¹ ≪ log r, and the Shiu range r^j < Y^{3/4} is valid.
  - Cost split at s* = L^{1/3}: singletons cost s*², and the block mass/depth ratio is 2^{3i}. This gives λ^{2/3} with no log loss.
  - It is consistent with z80 LM: it improves LM's (log λ)^{2/3} factor and adds a unit-fibre version, which LM explicitly did not claim.
  - Attainment via M at γ = 1/3: 4 | t, 8 | tx, and both parities of d. Correct.
- **Theorem T, upper bound (binary phase).**
  - Marks are exclusive across windows t (t < r). f = ad ≡ −1 (mod t) gives integral x and v, and the word identity p = txv − x − v checks out. The good sign is forced by 4 | t.
  - Σ_t N_t/φ(t) ≍ B² holds uniformly in the pin, and Σ_t N_t²/t ≪ B⁴.
  - Bad moduli: Σ_bad 1/t ≪ l²B^{1−A}. Removing them costs o(B²) by Cauchy.
  - List encodability works. A list's prime residues mod t are deterministic, so a unique match among all candidate labels makes one congruence mod a sufficient.
  - The binary unimodular-minor argument is correct. Unlike ternary vectors, there is no ε′ = −ε degeneracy, so no (5/9)^j condition is needed.
  - Rates: W_t = e^H·B² ≍ TB = c₀L^{(1+α)/2}, and MT ≍ c₀²L. The constants are fixed before c₀.
  - For B ≥ cL^{1/3}, the route through M gives 2/3. The polylog variant, which needs (ξ−γ)β > log 2 and 2γ < ξ, also checks.
- **Theorem T, model floor.** The candidate-residue count T_t·2^J, E 2^J ≪ 2s/log R, a block mass of ≍ sB, s* = (L/B)^{1/2} and B² ≤ L/s* for B ≤ L^{1/3} together give (LB)^{1/2}. This matches the upper bound. It is consistent with M for γ ≤ 1/3.
- **Proposition Q.**
  - The all-composite fibre has mass ≥ 3/4 − o(1).
  - Taking r ≡ 2 (3) up to L/2 works: if r = h+6 is prime and r ≡ 1 (3), then 3 | q = 4r − 25.
  - The log modulus is (3/8 + o(1))L.
  - At the square centre every letter is +1 mod q.
  - The (M) offsets fit the first band. For (DR) the band is (L, 2L] and z^J = X^{σ/2}.
  - The "menu" extension costs O(L^η log L).
- **Literature quantifiers, checked against the PDFs.**
  - Montgomery–Soundararajan Thm 3 (20) and its range log N ≤ H ≤ N^{1/K}: correct.
  - Kuperberg Conj. 1.3 (7) and Tao Conj. 1.3 (1.1), including x ≥ 10, (log log x)⁵ and the inadmissible sets: correct.
  - Granville–Lumley (10): correct.
  - Leung 2407.05380 Conj. 1.1 and 2401.04000 (assumes RH and LI): correct.
  - Jha Def. 1.3, with error x·e^{−ψ log₂ x}: correct.
  - Banks–Ford–Tao Thm 1.3 is a theorem about the random set R (c ∈ [1/2, 1), |H| ≤ log^c x, shifts up to exp(log^{1−c}x/log₂x), the stated error). It is correctly distinguished from the hypothesis on a set A in Thm 1.5.
- **§11.** The corner and AM–GM areas, the 3/16 bound under BV, the 3/4 bound under the upper transfer, and (T) are all correct. It is a light corollary of z80, and it says so.
- **Comparison with `ES_JUGULAR.md` at `e78d466c0`.** Its sign identity χ(xv) = χ(a) matches (7). Its Theorem A (R = all nonresidues) gives "reachable negative endpoint" correctly. 4 | t ⇒ negative matches its slot remark.

## Issues to fix
1. **T's model floor is false as worded (statement-level error).** It is stated "for the fixed-(t,x) endpoint cylinders with t ≤ K". Take t = x = 2: then f = 3 and the class n ≡ 1 (mod 3) contains the whole 1 mod 24 fibre, so the void is empty. This is the interior word (2, 2, (p+2)/3) at every such prime; it has positive sign, since (−2/3) = +1. The proof uses only the cylinders with (7) = −1 ("uses the sign, as in W"). The theorem statement, and the proposed FRONTIER line ("sharp chart exponent"), must say **good-sign (square-excluding) fixed-middle-letter endpoint cylinders**.
2. **Banks–Ford–Tao misquote.** Thm 1.5 has |H| ≤ κ log x/(2 log log x), not "k ≤ 2κ log x/log log x" (off by a factor of 4). The "every fixed η < 1" conclusion is unaffected.
3. **Labels.**
   - Theorem T's "rel." list omits M (z75 supply) and z82 §§6.2–6.3. Both are used for α ≥ 1/3 and for the envelopes.
   - Theorem W's list says "§§2 and 9" (it cites itself) and omits `EXSET_BEYOND_CRT.md` Lemma 2.4 and Shiu Thm 1.
   - §9 relies interpretively on Theorem A of `ES_JUGULAR.md`. That note has "Review: none", is only on the side branch, and is not an ancestor of HEAD, so the pointer dangles here. Say this explicitly.
4. **Triage.** T is marked RECORD, but there is no STATUS delta and it concerns a new observable. Either reclassify it (BARRIER-SCOPED plus FRONTIER §6) or say "RECORD-type, new observable, no STATUS row proposed".
5. **Q is overstated.** The reweighted law also moves each univariate F_q mean from L^{−I*} to ≥ 3/4. It therefore breaks first-order statistics, which undercuts "stronger than merely observing that (M) is not worded as a primality test". There are two options:
   - Tone this down.
   - Or strengthen Q. Move only δ = L^{−A} of the mass, with A > I*. The bit table stays exact, each m_q changes by a relative o(1), and ∏m_q stays X^{o(1)}. Yet δ·z^J = X^{σ/2−o(1)} still violates (DR) even with a normaliser that depends on the law, and δ still exceeds (M)'s right-hand side.
6. **Buried result.** The polylog claim (W_t ≍ L^{1/2}l^{1/2} at K = L^β, β > log 2) sits inside the proof of T. Put it in the statement with its own label. §11 is also missing from §0.
7. **§0 Scope.** The commit dropped V's clause "both types of bounded-gap certificate at primes are included in the class model". Restore it or justify the removal. The Result line is one sentence carrying three claims, and it omits "p ≡ 1 (24)".
8. **Notation overload, carried over from R1.** T is the theorem, the log cutoff and T_t. W is the theorem, W_t and the cutoff exponent. v is both the word letter and the z75 label.
9. **Script and description.**
   - The toy Q in `audit_table` uses bit shifts {0,1,2,4,6,9,14}, which do not include all the window offsets (q+1)/4 that it tests, and it finds t* by search rather than by the CRT recipe.
   - `audit_seed` never asserts x ≥ 2.
   - The CERTIFIED text should state these limits. The CERTIFIED block also covers §§8–10 but is placed in §11.

## Debate points (not defects)
- W's novelty is narrow: it removes (log λ)^{2/3} and adds the unit fibre and the colour charts. The primary exponent 2/3 is old.
- Q is a scoped example. The note correctly concedes that it says nothing against BFT-type uniformity over all menus. Fooling every menu in [0, L²] at once would need an atom of mass about X^{−1}, which does not reach (DR)'s X^{−σ/2}.
- The η = 1 calibration does survive the odd-square screen. Squares contribute X^{−1/2}, the same size as (P)'s additive e^{−kl}, and well below the main term X^{−0.0016}.
- No master files were edited (correct for a lane), and "Round 2 cross-review owed" is properly flagged. This review is one cross-lab pass; the gate still applies.
</code-review>