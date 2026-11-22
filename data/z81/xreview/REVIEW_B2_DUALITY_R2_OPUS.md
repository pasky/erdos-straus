<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="7d17b3bfd">
A separate reviewer subagent was asked to review the changes in `git log 7d17b3bfd..`. Its request and review follow.

Request: review changes since 7d17b3bfd carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus supplemental review z81 B2_DUALITY.md: audit H especially the smoothness/weighted 2-torsion, exact joint denominator, infinite order and finite-place integrality approximation, p-adic and odd-denominator Hilbert reciprocity necessity. Re-derive rigorously. Check the R1 fixes incl. explicit G constant and F restriction. Check labels, only scoped statements. Keep computational replay <= 10 minutes; no long census needed. Return a concise verdict and all necessary fixes.

Commit log:
commit 668858f7b76dd36b5ca2540eed96ab7e9b71f65a
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:08:42 2026 +0100

    z81: give rank-positive weighted jump with unavoidable denominator primes; fix Opus R1

 data/z81/duality/pencils.txt                  |  9 +++
 data/z81/xreview/REVIEW_B2_DUALITY_R1_OPUS.md | 94 +++++++++++++++++++++++++++
 notes/z81/B2_DUALITY.md                       | 64 ++++++++++++++----
 scripts/z81_dual_pencils.py                   | 47 ++++++++++++++
 4 files changed, 200 insertions(+), 14 deletions(-)

Review:
**Verdict: accept with minor fixes.** I re-derived every step of H by hand and found no mathematical gap. The R1 fixes are applied correctly, and the G constant is valid with plenty of room. No master files were touched, labels stay scoped, and nothing claims ES.

## H, re-derived

- **Seed and jump: correct.** P=(a,b,−pD) satisfies 4/p and x+y−z=s₀. I_w maps P to the positive class [1/a:1/b:1/(pD)], and Q=(ps₀/4)(…) is the normalized point.
  - The last entry of Q is p(1+D)/(4D) in lowest terms, because gcd(p,D)=gcd(1+D,D)=1 and 1+D=(p²+3)/4 is odd.
  - So the exact joint denominator is p²−1 (even).
- **Weierstrass model: correct.** I re-derived Y²=X(X²+(N²−2N+5)X−16N) from scratch.
  - P maps to (−p²N, pN(N+1)).
  - By X(2P)=(X²−B)²/(4Y²) and (p²+4)(p⁴−p²+4)=p⁶+3p⁴+16, I get X(2P)=(p⁴−p²+4)²/(4p²). Since p∤4, 2P is not integral, so P has infinite order.
  - The short-model shift is not needed: the generalized Nagell–Lutz theorem applies directly to y²=x³+ax²+bx+c with integer coefficients. It is harmless.
- **Smoothness: correct.** A Gröbner computation on (xy+yz+zx)(x+y−z)−Nxyz finds singular members only at N ∈ {0, −1, 3±4i}. N=p²+3 is never one of these.
- **Weighted 2-torsion: correct.**
  - A torus fixed point of I_w forces N=(±1±1∓i)² ∈ {−1, 3±4i}, so I_w has no fixed points and is translation by the rational point (0,0).
  - P has X<0, so it lies on the bounded component (egg). Q has X=16/p²>0, so it lies on the identity component.
  - ⟨2P⟩ is dense in the identity component, and positivity is an open condition near Q. This gives infinitely many positive rational points.
- **Finite-place integrality approximation: correct.** The Weierstrass identity maps to [0:0:1]. The plane normalization s₀(x,y,1)/(x+y−1) is regular there with value (0,0,−s₀), so it is ℓ-integral near O. Taking compact open subgroups of finite index, a multiple mP with m even, and density finishes the argument.
- **The no-positive-integral-point lemma (p∤Σwᵢxᵢ for weights whose ratios are quadratic residues): correct.**
  - v_p(z)=1 is forced when exactly two coordinates are p-units.
  - α_p=−1 follows from Bright–Loughran (BL) Lemmas 3.1, 3.5 and 3.8 plus reciprocity.
  - α is symmetric under permutation, since (−ab,−bc)=(−ac,−bc).
- **p-adic necessity: correct.** All three cases give α_p=+1 for *every* rational point on the plane.
- **Necessity at odd denominator primes: correct.**
  - At ℓ | K, exactly two coordinates have valuation −d and the third is an ℓ-unit.
  - The symbol is (w_j/w_i, ℓ^d·unit) = (±1/ℓ)^d.
- **Replay (about 3 minutes in total):**
  - `z81_dual_pencils.py` reproduces `pencils.txt` byte-identically.
  - A brute-force check over all primes p≡1 (mod 4) below 300 found no positive integral point with x+y−z≡0 (mod p), in any coordinate order.
  - Multiples kP, and kP+T for odd k (k≤60), at p=5, 13, 17, 29 gave 143 positive points, all on the identity component. Every point tested had α_p=+1, and every odd-K point had α₂=+1.
  - 57k random odd-denominator points on S_p had α₂=+1, consistent with BL Lemma 3.8.

## Fixes needed

1. **Sharpen the H conclusion.** For odd K, the obstructed primes are exactly those dividing den(z). Reciprocity then says (−1 | den z) = α_∞, so **positive points with odd K have den(z) ≡ 3 (mod 4)**. This is cleaner than the current "odd number of ℓ≡3 (mod 4) with odd exponent" and implies it. It held at all 40 odd-K positive points tested.
2. **Rephrase "puts a mandatory odd-exponent prime outside any prescribed finite set".** Suggested: "for each finite S∋2 there are infinitely many S-integral positive points; their K is odd and >1, so each has an odd-exponent ℓ≡3 (4) dividing den(z) outside S." As written, the quantifiers are ambiguous.
3. **Correct the F1 cell for H; it is misleading.** The example (7,70,350) at 4/25 says nothing about H; the lemma actually *holds* at 25 and 169. The real data:
   - The lemma fails at 9, 49, 81, 121, 45 and 4545. For example, at 4/49 the point (14,784,112) has 14+784−112=14·49.
   - Even so, the s₀ plane is empty at every square and composite tested.
   - So the emptiness of this plane is not by itself evidence of a prime-specific obstruction. Only the proof is prime-specific.
4. **G: fix one step.** "Lu≤2(V+W)+V/v=5V+2L" should read "≤4V+2L+V/v≤5V+2L". Everything else checks: u≤5H/2+2≤16H, |R|≤3072H⁵, V(u+1)≤17H³, and tv≤67652H⁸. That gives p<1.09·10⁶H⁹, inside the stated 3·10⁷H⁹.
5. **Script and data:**
   - `screen()` only tests positive weights from 1 to 5, so the H weight (1,1,−1) is never screened. Add it, or say so.
   - The `pencils.txt` columns are not documented in the note.
   - The p=17 row, with weight (1,4,4) and common sum 482, is a plane holding both a signed and a positive integral point. That is relevant scope data and should be mentioned.
   - Add `scripts/z81_dual_pencils.py` to the §6 command block.
   - Wording: "fitted directional character formula" should be "derived …", and "prime-weight exclusion" should be "QR-ratio weight exclusion".
6. **§0 block:**
   - The Scope line says "Three method tests"; it should say four.
   - The Label line should add Hilbert and quadratic reciprocity.
   - The Review line should cite this supplemental review once it is filed.
7. **Cut or reword one sentence.** "Even a nonintegral intermediate point … cannot be followed by a jump landing on a positive integral point on that plane" just restates that the plane is empty.

## On the substance

H is really an integral Brauer–Manin obstruction on one curve. Its most useful content is that α_p is trivial for *every* rational point on the plane, while every positive integral point has α_p=−1. The positive rank and the sign change are genuine but standard. So the BARRIER-SCOPED/METHOD-CX triage and STATUS delta none are right, and the routing merge C/H in FRONTIER §6 is appropriate.

The Bremner–Guy–Nowakowski priority check for E is still owed. I did not verify the DOI.

My check scripts are in `/tmp` (`h_check.py`, `h2.py`, `h3.py`) and are not committed.
</code-review>
