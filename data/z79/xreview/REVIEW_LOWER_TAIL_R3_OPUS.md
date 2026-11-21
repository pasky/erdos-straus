<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="e6d4de5db">
A separate reviewer subagent was asked to review the changes in `git log e6d4de5db..`. Its request and review follow.

Request: review changes since e6d4de5db carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-3 review of notes/z79/LOWER_TAIL.md and scripts/z79_lower_tail_r3.py at 4fbd377ce. Independently derive K's reciprocal I4 identity, uniform supply constant and multiplicity for both BV uses, concentration on Haar and primes, explicit c_A, L's growing order, including on a possible Siegel-small fibre. Attack M's improvement of R coefficient (uniform/completed local 2 factor including q=8 etc; k'=k/(4,k); splitting lemma; equal-sum same product; the new primitive conic count for ratios P/Q; power-small bad pin mass accounting, diagonals and double counting orientations). Check falsifiers and ordered convention. Please give clear verdict for each and all needed fixes. No edits, memory ≤1200000, timeout ≤1800, uv run --offline --no-project python; note previous rounds were reviewed, scope is §§9–11. This should be Claude Opus.

Commit log:
commit 4fbd377ce00a0d0e36b69680b0946a92941669c9
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 14:29:26 2026 +0100

    Concentrate Type I multiplier counts and add the third disjoint star chart

 data/z79/lower_tail_r3_checks.txt |  6 +++
 notes/z79/LOWER_TAIL.md           | 91 +++++++++++++++++++++++++++++++++++++--
 scripts/z79_lower_tail_r3.py      | 79 +++++++++++++++++++++++++++++++++
 3 files changed, 172 insertions(+), 4 deletions(-)

Review:
**Verdict: accept §§9–11 (Theorems K, K.1, L and M) with minor fixes. I found no fatal gap, and no change to any label or scope is forced.** I re-derived every listed item by hand. I ran `scripts/z79_lower_tail_r3.py` and its output is byte-identical to `data/z79/lower_tail_r3_checks.txt`. I also ran independent checks in `/tmp`, all under `ulimit -v 1200000` with `uv run --offline --no-project`.

## Theorem K: Type I chart (accept)
- **Identity:** with a=u, b=kℓ, c=(a+b)/e, d=(ep+1)/(4ab) you get 4abcd=(ep+1)c=p(a+b)+c, so the decomposition 4/p=1/(pabd)+1/(acd)+1/(bcd) holds. p divides only the first denominator (a, b, c<p, and 4abd≡1 mod p rules out p|d), so it is genuinely Type I.
- **Injectivity:** (u,kℓ)=1 because ℓ>K. The swap a↔b leaves the box because kℓ>K≥u. ℓ is the only prime factor of b above K, so the split b=kℓ is unique.
- **Distinct targets at fixed ℓ:** equal targets force e=e′ (both are below ℓ). Then e divides uk′−u′k, which is smaller than 2K²<H, so (u,k)=(u′,k′). Hence at most one hit per ℓ, and the ℓ-digits are independent Bernoullis. ✓
- **Uniform supply (K.1):** BV in ℓ applies because U≤x^{1/4}. BT gives E_x(e)≪x/φ(e). The second moment of R_z goes through lcm l≤16K⁴, a τ(l)⁴ multiplicity and a K⁴/H tail. Cauchy then gives a t^{−D} error uniformly in z. The e-sum equals ΔS(q)/q+O(t/H) by the e/φ(e) expansion. ✓
- **Constant C_I:** the local factor at odd h is 1−1/h³, and 1/4·∏_{h odd}(1−h⁻³)=2/(7ζ(3)). Numerically, the natural density over odd coprime u,k≤3000 is 0.237703 against 0.237688 predicted. With log K=t/50 and Δ=t/40 this gives exactly the stated C_I. ✓
- **Moments and transfer:**
  - The central moment bound O_m((1+M_I)^m) holds.
  - The level is (4Y^{26/25})^v.
  - The GRH coefficient sum Y^{(26/25)v+o(1)} comes from at most τ(u+kℓ) values of e per (u,k,ℓ).
  - The BV multiplicity ρ(l): the steps through Hölder, l=4abk′, and the bound Σ_{a+b=n}1/(ab)=2H_{n−1}/n are correct.
  - Markov gives O(t^{−3m}).
- **Explicit c_A:** C_Iλ³/2 is valid for large X.
- **Siegel-small fibre:** §4.2 needs only F≥0 and E_rF. On a fibre with cond ψ | Q, both F and F=1 have exceptional coefficient ψ(r)v/φ(Q). So the min(u,1) factor cancels in the relative proportion. ✓

## Theorem L: growing-degree Type I tail (accept)
- K.1 still applies at t=ηL^{1/4}: √Y≫B, 2K²<H and U≤x^{1/4} all still hold.
- With D≍t³ distinct-ℓ atoms, the conductor log is at most σL+O(η⁴L). The bounds E2^{−Z}≤e^{−μ/2} and e_j≤μ^j/j! carry over from Theorem J. The §4.2 (G) comparison is linear in the L¹ norm and does not depend on the degree, so it holds on a Siegel-small fibre. The GRH coefficient sum is exp(O(t⁴)). ✓

## Theorem M: R coefficient 9/(32π²) (accept)
- **Disjointness of the three charts:** (4ab)(4aC−1)=4a(p+a)>X^{2θ}, and ff′=4d²p+1 separates the two trial charts. ✓
- **Constant:** the local factor at odd h is 1+1/h², and at 2 it is (1/2)·2=1, giving 12/π². The numerical density is 1.215873 against 1.215854 predicted. Then (3/π²)·(1/32)+K₂/64 = 9/(32π²). This equals Z53 §9.2's stated ceiling (3/16 of M₀), which is a good consistency check.
- **2-adic factor, including q=8:** min(v₂q, v₂u)≥3. Given the even coordinate, the odd coordinate makes a+b uniform on odd residues mod 2^m. So the expected factor is 2^m/φ(2^m)=2, the same as unconditionally. At odd h|u, z is a unit because (a′,b′)=1, and the expected factor is h/(h−1). So the pinned and unpinned completed means agree. ✓
- **k′=k/(4,k) and the splitting lemma:** h′|ab and k′|h′ are correct. The split k_i=(k′,h_i) puts a in one class mod h₁k₂ and b in one class mod h₂k₁. The four terms of (8) follow from k≤4k₁k₂ and h′≥h/4. ✓
- **Large-h spike:**
  - A nonzero sum difference gives a bound of X^{w−g}.
  - For k>ABX^{−δ}, any nonzero-difference point is impossible, since 2(A+B)X^w<ABX^{−δ}. So on good rows those terms vanish outright.
  - Equal sum plus equal product forces {a,b}={c,d} (Vieta).
- **Conic count:** the derivation b(Pi−Q₁j)=GQ₁j(i−j) is correct, and the gcd bound PQ₁|P−Q₁| is correct and needs no coprimality of P and Q₁. The count A′LX^{5(δ+2w)} is correct, and 5δ+11w<0.61g, so it saves a power.
  - Brute force on (a,b)∈[200,400)²: 1,795,368 ordered equal-sum configurations, each determined uniquely by (i,j,P,Q₁), with the gcd and |Pi−Q₁j| bounds asserted.
- **Diagonals and orientations:**
  - The pin and its swap define the same congruence, giving the term 2EN.
  - Ordered (atom, pin) counting is only an overcount.
  - Each box J is handled by its own Chebyshev bound, so swaps landing in another box are harmless.
  - Var≤2EN+O(L²X^{−κ}); BV at level X^{2θ} then gives O(1/L²) exceptions.
- **Numerical caveat:** in a P-weighted exact Haar test on dyadic boxes with A=100, 200 and 400, the pinned-row excess is +11%, +11% and +8%. At these sizes τ(u)²/A is not small, so this neither confirms nor refutes the X^{−κ} claim.

## Falsifiers and ordering convention
- F1–F4 are compatible.
  - The odd-square Jacobi argument is correct (e≡3 mod 4, (ab/e)=+1 against (−1/e)=−1).
  - The 241 and 131 examples are exact in 4 but not in 8.
  - Almost-all bounds allow the known (★)-zeros.
- R counts ordered (u,B,C) (`Z53_PZ.md` §1), and the pair chart already contains both (a,b) and (b,a).

## Fixes needed (form and minor)
1. **§0 Result:** state 9/(32π²) directly rather than the stale 3/(16π²) clause.
2. **§0 Label:** add Brun–Titchmarsh, and Siegel–Walfisz for K on polylogarithmic bases.
3. **§0 Scope:** "only lower bounds on R and f_II" should add f_I.
4. **Theorem K, "factor 1/2 here is conservative":** this misattributes the 1/2, which is the ε-margin. Say instead: under ET's ordered convention f_I≥2Z_I, because y≠z.
5. **"e is automatically prime to all factors":** this fails for even e (u+kℓ is even). Say that even-e atoms are empty.
6. **Headings:** "### 10." should be "## 10.".
7. **§11 notation:** it clashes with the rest of the note (pairs (c,d), Q₁ against the base Q, M_J against §2's M_J, e reused). Rename.
8. **Label of L:** cite BV, BT and PNT through K.1.
9. **Script:**
   - The "pair" toy (b=kℓ) is not the §11 chart, and the distinctness it asserts is not claimed anywhere in the note. Either explain it or drop it.
   - Add finite checks of the conic lemma (uniqueness and gcd bound) and of the pinned local 2-adic and odd-prime factors. None of M's new lemmas is currently exercised.
10. **STATUS delta:** keep "Round 3 cross-review: pending". This review counts as one cross-lab review. Since 3/(16π²) is an internal result rather than a published record, one cross-lab review satisfies the AGENTS §3 gate.

No files were edited. The check scripts are `/tmp/r3check.py`, `/tmp/r3check2.py` and `/tmp/r3check3.py`.
</code-review>
