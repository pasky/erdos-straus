<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="420c1f9c9">
A separate reviewer subagent was asked to review the changes in `git log 420c1f9c9..`. Its request and review follow.

Request: review changes since 420c1f9c9 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-2 review of notes/z79/WILD_ES.md and scripts/z79_*: freshly scrutinize Theorems C,D,E,F in §§5–8 especially the ramified sign switch on small fibres, prime-parameter repair, permutation degree argument, primorial population error, clean-scale average of character prime sums WITHOUT Gallagher/DH, and least-good-denominator 1/3 via O13. Audit all bounds, degenerate controls and exact labels/scopes. Reproduce/independently check local finite data. Return full report as text; do not edit files. Python only via ulimit -v 6000000; timeout <=1800 uv run --offline --no-project python -B. No side agents.

Commit log:
commit eb56287b0dc6e56c0c314aee50937c89daacbce3
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:47:06 2026 +0100

    z79: ramified sign switch, permutation-prime pullbacks and clean-scale HJ gaps

 data/z79/wild_round2.txt   | 14 +++++++++++
 notes/z79/WILD_ES.md       | 60 ++++++++++++++++++++++++++++++++++++++++++++
 scripts/z79_wild_round2.py | 62 ++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 136 insertions(+)

Review:
# Hostile cross-lab Round-2 review: `eb56287b0` (`notes/z79/WILD_ES.md` §§5–8, `scripts/z79_wild_round2.py`, `data/z79/wild_round2.txt`)

**Verdict: ACCEPT with fixes.** I found no fatal mathematical error in Theorems C, D, E or F. Most of what needs fixing is about how the results are framed and labelled, plus several proof interfaces that are asserted rather than re-derived. The main substantive objection is that Theorem F's seven-chart part is not a record improvement.

Scope: I reviewed only `420c1f9c9..eb56287b0`, which touches three files and leaves the master files alone, as lane rules require. I am a Claude model (Anthropic), so this is the cross-lab review for this Astra-lane round.

## 1. Replay and my own checks
All runs used `ulimit -v 6000000` and `uv run --offline --no-project python -B`.

- **Replay:** `scripts/z79_wild_round2.py` reproduces `data/z79/wild_round2.txt` byte-for-byte.
- **Divisors of f+1:** for f ≡ 3 (4) up to 20 000, every odd divisor of f+1 is a Jacobi residue mod f, and every divisor is one when f ≡ 7 (8). 0 failures. This confirms the F1 reciprocity step behind (3).
- **The new zero claim for 2j²:** an exhaustive search over all x, y with 8 | xy for n = 2j², j ≤ 40, finds **0** solutions of n = xyz − x − z. The control n = 2j²+2 finds 258.
- **Sign identity in general form:** for words with 4 | xy and (x odd or f ≡ 7 (8)), n < 500, no hit has (n/f) = +1 (3198 hits checked).
  - Without that restriction the general form fails 664 times, because x is even when f ≡ 3 (8).
  - The note does not claim the general form, but it shows the row restriction is essential.
- **Root-count formula (3):** 3310 atoms built directly, with composite k ≤ 300, ℓ up to about 10⁵, u < 40, v < 15 and 15 squarefree s: 0 failures. This also confirms that every active residue is a unit mod k.
- **Theorem D:** I compared full fibre-size multisets (not just images, which is all the script checks) of a·j^h + b against a·j² + b (even h) or a·j + b (odd h). There were 400 random tests over 15 degrees h ≤ 30 on primes ℓ ≡ −1 (M): 0 failures.
- **Least good HJ denominator:** for all 1115 primes p ≡ 1 (840) below 3·10⁶, the least A found directly from interior words with (A/p) = −1 equals the least A found from the forbidden-atom description (u | A+1, sign (−u/A_odd) = −1). 0 mismatches; the maximum least A is 593. The terminal word (u = 2, A = f) is good for 74 primes f ≡ 7 (8).

## 2. Theorem C (ramified pencil s·j²)
- **(3) holds.** Activity gives −suv ≡ (sjv)² mod k, so (−suv/k) = 1. With (−uv/f) = −1 in each row, multiplicativity in the denominator gives a root count of 1 − (s/f) at ℓ.
  - When k shares a prime with sj, the pair is indeed never active: that prime would divide both u and f.
- **s = 2.** Both rows of Theorem B force f ≡ 7 (8) and are dead there.
  - The impossibility argument is correct for every x, not only 8 | xy. From 2j² ≡ −x mod each prime p | f we get (−2x/f) = +1, while f ≡ 7 (8) forces it to be −1.
  - The replacement row (x odd, f ≡ 4w' − 1 mod 8w') has two roots on every active atom, with q = 8w' > K.
- **Odd prime p | s.** The digit of f at p is free once the odd parts of u, v (or w') avoid the primes of s, so (s/f) = −1 is reachable.
  - Because the root count is exact, no zero-density input is needed: **"No zero-density input in C" is correct.**
- **Bookkeeping checks out.**
  - Rough J₀ gives h ≍ t/log t.
  - Deleting multipliers divisible by p costs at most h_{J₀}/p, since k = pk′ with k′ rough.
  - The gap between the ratio weight and the harmonic weight is at most (1 + log K)·Σ_{p>y} p⁻².
  - The resulting tail scale is L_r.
  - The prime-parameter repair leaves a prime j > K unchanged, so P_r follows.
- **Form:**
  - (C1) Equation (2) is never restated for the ramified rows. The weight 1 + (D/ℓ) is replaced by 1 − (s/f) on the refined class, and the Δ ≠ 0 pruning of §2 is bypassed. Write that modified (2) out explicitly.
  - (C2) The letter s is overloaded three ways: the kernel here, (nv+u)/f in §1, and the squarefree factor in §2.

## 3. Theorem D (permutation primes)
- **Core claim holds.** For ℓ ≡ −1 (M), gcd(h, ℓ−1) = gcd(h, 2), so odd h gives a bijection.
  - For even h, the squares form an odd-order subgroup, so j^h has the same image and fibre sizes as j². I verified this independently, as noted above.
- **AP compatibility at 4 and at primes of M dividing q is correct.** The fresh-prime pruning correctly widens to s | 2MAΔd.
- **The Bonferroni sieve in progressions is right.** The term (log log t)^{D+1}/(D+1)! is super-polynomially small, and y^{D+1} = exp(O(log² t)) is much smaller than Y = exp(√t). One point to make explicit: the lower bound uses the odd truncation order.
- **Square values are harmless.** j³ is a perfect square whenever j is (j = m² gives m⁶), and squares have zero hits by F1. That is O(√H) parameters, inside the O(H·e^{−cL}) exceptional allowance.
  - Worth one sentence in F1, because the supplement says "odd degree uses permutation primes, not a square polynomial".
- **Form:** the letter D clashes three ways: the Bonferroni order, the discriminant in (1) and the level in §8.

## 4. Theorem E (primorial fibres)
- **The argument holds.**
  - Primes p ≤ B₀ never divide F(j).
  - The exponential moment at B₀ gives Pr(W > δ) ≪ e^{−δB₀}, and B₀ ≫ t^{r+1}.
  - Cell intersections with the progression cost O(1) each; the boundary H^{O(α^{r+2})} is below N^{1/2} once α is chosen depending on σ.
- **The smooth-f remark is correct.** If n ≡ 1 at every prime of f, then (n/f) = +1, which contradicts (−uv/f) = −1.
- **The examples check out.** The empty-fibre example (1 − d a nonresidue at a pinned prime) and the nonvacuous examples j^h + 1 at j ≡ 0 and j² + 1 − a₀² are right.
- **(E1) Interface gap.** For the ratio row (r = 2), the coefficient ceiling must satisfy exp(b(log H)^{1/4}) ≤ X^{e/1000} = exp(eα(log H)^{1/4}/1000). So b ≤ eα/1000, and since α depends on 1 − σ, so does b.
  - The theorem says "the nondegenerate quadratic of A", which suggests A's fixed b.
  - Fix: state that the coefficient constant may depend on σ.

## 5. Theorem F
- **Clean scales: correct.**
  - On q ≤ U, |γ| ≤ U⁴, the standard zero-free region covers the box once c ≤ c₀/6. Only Landau exceptions remain.
  - A dirty character at U_i is a Landau–Page exception at U_{i+1} because 2c < c_P, so uniqueness chains the dirty scales and gives the contradiction.
  - Effectivity bonus: by the same chaining, the first scale after a dirty run must be clean. Clean scales can therefore be located effectively via Page (15), though with huge gaps. Worth stating, since H4 cares about effectivity.
- **Clean transfer (4): correct.** I checked every term:
  - The truncation term is x·U^{6−4N}.
  - The term for zeros with β ≤ 1/2 is √x·U⁶·log U = o(x), since x = U^{C log log U}.
  - I checked the density bound against the archived MV III draft, where Thm 28.6 (28.30) carries a log⁶ factor.
  - Partial summation gives roughly (log U)^{6−cC}, so cC > 6 already suffices.
  - (22) needs only Z³ ≪ x.
- **Lemma 6 is not needed on clean scales.** Every nonprincipal prime sum is collectively o(x), and |c(χ)| ≤ E|B|/φ(Q′) ≤ 1.03μ/φ(Q′) trivially. "Coefficient supremum, not total norm" is the right observation.
- **(F1) Main objection: significance.** Gallagher's theorem is a published theorem (Invent. Math. 1970), and STATUS §1D already lists κ < 1/4 rel. Gallagher as PROVED.
  - The new seven-chart result is an alternative route with a *weaker* quantifier (a subsequence instead of every prescribed f). It is not an improvement of any exponent.
  - "Improves the no-(G) 1/8 exponent" is technically true but suggests more than it delivers.
  - The provenance argument against (G) also cuts both ways. The replacement density theorem is cited in §2 from the *same* archived MV III draft (`sources/omega9/montgomery-mnt3.pdf`, Thm 28.6). Cite Montgomery, *Topics in Multiplicative Number Theory*, LNM 227 (1971), Thm 12.2, and adjust the explicit "Cc > 8" if its log exponent differs.
  - I recommend triage METHOD or ancillary, and no §1D STATUS line. A number theorist reading only STATUS is not misled without it.
- **HJ least good denominator (κ < 1/3).**
  - These steps are correct:
    - reciprocity with p ≡ 1 (840);
    - at most τ(A+1) atoms per A;
    - the sign filter makes the atoms miss unit squares;
    - Σ_{A<T} N_A/A ≪ L², and the higher moments are polylogarithmic;
    - the Hölder interpolation;
    - the budget log(Q′D) ≪ L^{3+ε}.
  - Both orientations are covered, because (tu−1)(tv−1) = tp + 1 ≡ 1 mod p.
  - The terminal word was verified.
  - It is consistent with the O14 ceiling: the HJ mass is quadratic, while II2 with general a is cubic. Only the a = 1 part of II2 lies inside HJ.
  - **(F2)** The step "z78 §6.2 quarantine/energy proof applies with cubic replaced by quadratic" is asserted, not re-derived. It runs through O13 Lemma 3.2(d), the late loads and free 2-adic digits. It is plausible, but the inherited interfaces need a dedicated review before any promotion.
- **(F3) Label gaps.**
  - The F label omits the published inputs inherited from z78 G: ET Thm 7.1, Shiu, Pólya–Vinogradov, and H4 Lemmas 5–6.
  - The "with (G)" HJ variant depends on H4 Lemma 7b, (G) and Lemma 6, but the label reads "Without Gallagher's (G)".
  - The HJ result is a new, scoped invariant. Its scope disclaimer is adequate.

## 6. Form, §0 and scripts
- **(G1) §0 block.** Round 2 is a free-text paragraph.
  - Result, Label, Scope and Triage are not updated for §§5–8.
  - The "Proposed §1D delta" gives no replacement text, which AGENTS §0 requires.
- **(G2) Letter clashes.**
  - Theorems C–F collide with the theorem letters of z78 `WILD_ES.md`, a file with the same name that §8 cites as "z78 Thm G".
  - The letters B, D, L and T are each reused with several meanings.
- **(G3) The CERTIFIED block overstates what the script checks.**
  - Images are compared only for ℓ < 500; above that only the gcd is checked, and the data file does not say so.
  - Fibre sizes are never checked.
  - The "238 HJ comparisons" only test a reciprocity tautology.
  - Nothing checks the s = 2 zero claim or the replacement row.
  - I suggest adding the cheap brute-force 2j² check and the fibre-multiset check from §1.
- **(G4) Falsifier supplement.** It mixes table rows F1–F4 with checklist items 1–19. Items 1, 2 and 14 are covered only implicitly.

## 7. Recommendation
- Accept C, D and E as PROVED relative to the stated inputs, after fixes C1 and E1.
- Accept F's analytic clean-scale lemma. Reframe the seven-chart part as a Gallagher-free alternative proof along a subsequence, not a RECORD.
- Keep the HJ κ < 1/3 as scoped, with "cross-review owed" on the inherited O13/z78 interfaces (F2).
- Before export, update the §0 fields (G1) and the labels (F3).
</code-review>
