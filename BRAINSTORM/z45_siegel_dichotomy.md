# z45_siegel_dichotomy — three different notions of pretence, and the missing target

## 0. Summary

**Assessment.** A two-world proof has to distinguish three objects: the quadratic character χ_p on freely chosen small primes, all characters of the window group on the primes actually dividing K_q=(p+q)/4, and an exceptional real Dirichlet character χ_D. They are not interchangeable. Non-pretence in the second sense gives existing positive-cap covering results, not cap 0; pretence in the first sense is genuinely realised and makes primes harder on average, not easier; a Siegel zero biases free primes towards χ_D=-1 and does not control a divisor class of a prescribed K_q. Fresh computations through 10⁷ confirm this orientation, including all 20,513 Mordell-class primes. A sharper target-aware inverse proposal also fails locally: at p=31121, q=43 the full divisor-ratio box misses −1 despite having 37 of 42 residues and despite **every odd character exceeding the natural half-turn separation threshold**. This is a small, exact obstruction to replacing target membership by a single pretentious character. It is not an ES failure.

**Verdict: PARTIAL — the missing implication is single-p, target-specific cap-0 membership beyond balance/zero repulsion; promise 1/5.** The displayed off-the-shelf dichotomy collapses at B2, not the entire possibility of a future structure/randomness theory.

**Assessment, prior coverage.** The general Siegel dichotomy and the anti-Siegel orientation are already in `BRAINSTORM/hardness_law.md` and `bsB_sterile_pretentious.md`; the dual dictionary and cap gap are in `FORCED_WINDOW.md`, `BALANCED_LATTICE.md`, and (J)85/(J)91. `POINTWISE_OMEGA15.md` §§3–4 already blocks exceptional-character reweighting of its specified minorant architecture. No novelty is claimed for these facts or ordinary Fourier duality. The additions here are the three-character separation, fresh joint window/cap/count data, and the explicit failed target-aware inverse test in §5. A repository search for pretentiousness and phase/separation formulations was performed before that test.

## 1. Precise dictionary and the sharpest honest two-world statement

### 1.1 What has to be hit

**PROVED (existing reduction, `FRONTIER.md` §2).**

    R(p) = Σ_{C≥1} #{d | 4Cp+1 : d ≡ −1 (mod 4C)}.

R(p)>0 suffices for ES, but R vanishes at 14 primes ≤10⁷. A proposed all-p theorem must either admit these exceptions or use a larger certificate family. The unconditional BM-corrected main term is ≫log²p; its positivity is not the missing step.

**PROVED (existing window dictionary).** For p≡1 (4), m≡3 (4), gcd(m,p)=1, K=(p+m)/4, and b_s=v_s(K), put

    B(K,m) = {∏_{s|K} s^{δ_s} mod m : −b_s ≤ δ_s ≤ b_s}.

Then −1∈B gives a Type II certificate, while −p∈B gives a Type I certificate. The least m hitting either target is `a_min`; the least m hitting −1 is denoted m_II here. These are different statistics: at p=2451289 they are 31 and 71. For a prime forced window q≡3 (8), p≡1 (8), χ_p(q)=-1, K is odd and (K/q)=-1. Allowing

    δ_s ∈ [−b_s,b_s] ∪ {b_s+2,...,b_s+2e}

defines cap(q)≤e. The global minimum e*(p) is zero whenever an honest Type II window exists. Positive cap is a relaxation, not a small numerical error in an ES certificate.

### 1.2 Three non-equivalent distances

**PROVED (definitions and elementary distinctions).**

1. The requested statistic is

       D_y(p) = Σ_{ℓ≤y} (1−χ_p(ℓ))/ℓ.

   This is the **square** of the usual Granville–Soundararajan distance; we retain the task's D notation. More generally replace χ_p(ℓ) by χ_p(ℓ)overline(ξ(ℓ))ℓ^{-it} and take the real part. Testing only ξ=1, t=0 is not testing all possible pretences.
2. Balance uses the odd-order group U_q=(F_q*)², N=(q−1)/2, and generators s² for a forced set S. Its distance is

       d_S(ψ)=Σ_{s∈S} ||arg ψ(s²)/(2π)||,   ψ∈Û_q.

   It has flat weights, linear angles, no averaging over free primes, and generally a **different modulus q**, not p. `BALANCED_LATTICE` Proposition 1.3 gives covering radius comparable to 1/min(1,min_{ψ≠1}d_S(ψ)), within a factor k^{3/2}, when S² generates U_q. Generation failure is the zero-distance case.
3. A Landau–Siegel zero concerns a **real** primitive χ_D and the global analytic function L(s,χ_D), not either of the preceding finite distance tests.

**PROVED.** Because U_q has odd order, all its nonprincipal characters are nonreal. Their even extensions to F_q* have conductor q (q is prime), regardless of their order. Thus “small conductor”, “small order”, and “small angle on S” are three different restrictions. In particular the characters deciding the balance problem are not themselves possible exceptional real characters. Repulsion could improve estimates involving them, but cannot identify them with χ_D.

### 1.3 World A: the actual sufficient premise

**CONDITIONAL (exact implication from existing theorems).** Fix p. Let S be the odd primes ≤y, P=∏S, k=|S|. Suppose a candidate q exists with

    q≡3 (8), q≡−p (P), χ_p(q)=-1,
    min_{ψ≠1}d_S(ψ) ≥ ε>0.

Then the cube side L=⌈k^{3/2}/min(1,ε)⌉ covers U_q; `FORCED_WINDOW` Theorem 4.3 gives e*(p)≤L−1. Hypothesis W supplies such a balanced q at its stated scale, giving the familiar conditional (log log p)^{2+o(1)} cap at random-lattice balance. This is **not a constant cap bound**, and still less cap 0.

**Assessment, two missing arrows.** “χ_p does not correlate with small-conductor ξ” does not supply this premise: one must find q in the p-dependent progression **and** exclude all bad window characters, including high-order ones. Even granting this stronger World A, the cap-0 box has its actual valuation side lengths, not the enlarged covering side L. For q≈P²log⁴p, the guaranteed parity sub-box has only 2^k=P^{o(1)} elements, far below (q−1)/2. A single target may still be hit, but the covering theorem says nothing about that hit. This is exactly (J)91 Proposition 5.1, not a new obstruction theorem for all cap-0 methods.

**PROVED (genuinely cap-0 sufficient World A).** For the *actual* factorisation of K and characters χ mod q define

    A_χ(K)=∏_{s^b||K} [(2b+1)^{-1} Σ_{δ=-b}^b χ(s)^δ],
    V(K)=∏_{s^b||K}(2b+1).

By orthogonality the number of admissible exponent vectors hitting −1 is

    Z_p(q)= V(K)/(q−1) · [1 + Σ_{χ≠1} χ(−1) A_χ(K)].                 (1)

The A_χ are real. Consequently Σ_{χ≠1}|A_χ(K)|<1 suffices. This keeps p fixed and detects the exact target. But no cited non-pretentiousness or zero-free theorem produces this inequality for some suitable K_q at **every** fixed p. Calling that assertion World A only names B2.

### 1.4 World B: what structure actually says

**PROVED.** At a forced q, if χ_p(s)=+1 for every s in a proposed supporting set S⊂{s:s|K}, no ratio supported on S can equal −1 mod q. Indeed window reciprocity gives (s/q)=(s/p)=+1, whereas (−1/q)=-1. If all these forced s have χ_p(s)=+1, the non-residue sign of K must be supplied by an uncontrolled prime factor outside S. Thus this form of pretence gives an obstruction to the proposed small-factor construction, not a certificate.

**PROVED.** A ψ nearly trivial on S² says the S-unit exponent box is squeezed in a character direction. If ψ is exactly trivial on S² and ψ(t)≠1, the target t is excluded at every cap using S alone; if ψ(t)=1, one only reduces to a kernel, retaining a membership problem. Approximate triviality likewise requires the **phase of the target**, not merely the distance from 1. Neither conclusion is an existence theorem.

**Assessment.** The most honest dichotomy is therefore “a sufficiently strong *target-specific* Fourier estimate gives a hit, otherwise a Fourier obstruction remains.” The complement does not automatically produce one small-conductor character, an exceptional zero, or a constructive alternative. Both horns of the proposed stronger ES dichotomy still require new arithmetic.

## 2. What the external theorems really provide

### 2.1 Halász: a pointwise character, but a mean over integers

**PROVED (published).** Granville–Harper–Soundararajan, *A new proof of Halász's theorem, and its consequences*, Compositio Math. 155 (2019), 126–163, arXiv:1706.03749, Corollary 1.2, gives for f∈C(1), where |Λ_f|≤Λ, the following explicit version. Define F(s)=Σf(n)n^{-s} and M by

    max_{|t|≤log x}|F(1+1/log x+it)/(1+1/log x+it)| = e^{-M} log x.

Then

    |Σ_{n≤x}f(n)| ≪ (1+M)e^{-M}x + x log log x/log x.

Statement and hypotheses checked in [the full text](https://arxiv.org/html/1706.03749v1), §1.1. Dirichlet characters and their completely multiplicative unit-modulus twists lie in this class. The Euler product relates M to pretentious prime data, with the necessary minimisation in t.

**Assessment.** Here x and the integers n≤x are averaged; p can remain a fixed character modulus, but the resulting sum is not the divisor-box sum of one K_q. Twisting by ξ handles progressions, not a single prescribed factorisation. Applying Halász to a family of weights over p, as in almost-all window results, reintroduces B6. “No Siegel zeros” is not GRH, nor does it imply this route's EQ/S/W hypotheses or the Fourier bound (1).

### 2.2 Exceptional-zero world and its orientation

**PROVED (elementary).** If

    L_y(1,χ_p)=∏_{ℓ≤y}(1−χ_p(ℓ)/ℓ)^{-1},

then log L_y=Σ_{ℓ≤y}1/ℓ−D_y(p)+O(1), uniformly in p,y. Expand −log(1−z)=z+O(z²); Σℓ^{-2}<∞ bounds the remainder. Thus low D means a large **truncated** L-product. It does not by itself bound the complete L(1,χ_p), whose tail remains uncontrolled.

**PROVED (published theorem, safe sufficient formulation).** Heath-Brown, *Prime twins and Siegel zeros*, Proc. London Math. Soc. (3) 47 (1983), 193–224, implies infinitely many twin primes if there is a sequence of real primitive characters with zeros β_D for which (1−β_D)log|D|→0. This deliberately stronger sufficient hypothesis avoids treating the informal phrase “a Siegel zero” as a uniform all-scales assumption. The statement and proof mechanism were verified against [Tao's exposition](https://terrytao.wordpress.com/2015/08/26/heath-browns-theorem-on-prime-twins-and-siegel-zeroes/) and the Heath-Brown theorem quoted in [arXiv:2111.14054v5 §2](https://arxiv.org/html/2111.14054v5). A lone zero supplies conclusions on associated ranges, not infinitely many pairs at arbitrary scales by itself.

**Assessment, with the verified mechanism.** The relevant pretence is μ(ℓ)≈χ_D(ℓ), hence χ_D(ℓ)≈−1 on a weighted prime range tied to D and the strength of the zero. It is not χ_D≈1, and it is not a theorem that every fixed tiny prime is a non-residue. Heath-Brown replaces a prime-detecting convolution in a long n-average by a character/divisor convolution; its error is controlled after averaging over n. Transplanting that substitution does not yield a pointwise estimate of (1). The earlier memo's slogan “most small primes are non-residues” must be read with these range and weighting qualifications.

**PROVED (published, quantitative repulsion).** Benli–Goel–Twiss–Zaman, *Explicit Deuring–Heilbronn phenomenon for Dirichlet L-functions*, arXiv:2410.06082v1, Corollary 1.1: for Q>400000, T≥4, if ∏_{χ mod Q}L(s,χ) has a real zero β₁>1−1/(10log Q), every other zero β+iγ with β>1/2, |γ|≤T satisfies

    β < 1 − log(1/[12(1−β₁)A])/A,   A=10log Q+log T+107.

Checked in [the full text](https://arxiv.org/html/2410.06082v1). Taking Q divisible by relevant conductors makes the dependence on the enlarged modulus explicit. This is a zero-location theorem, not a divisor-residue theorem; it is useful only when its logarithmic repulsion term is positive.

### 2.3 What changes for the fixed prime p?

**PROVED (orthogonality bookkeeping).** The Λ-weighted forced-window count in a class a mod M, gcd(p,M)=1, is

    (1/[2φ(M)]) Σ_{ξ mod M} overline(ξ(a))
        [Σ_{n≤X}Λ(n)ξ(n) − Σ_{n≤X}Λ(n)ξ(n)χ_p(n)].               (2)

This identity is exact for the weight (1−χ_p(n))/2; removing prime powers is a separate standard step. The usual explicit formula has an exceptional contribution −X^{β_D}/β_D in a character sum containing χ_D (primitive inductions understood).

**CONDITIONAL (on such a zero and an explicit-formula error small enough at the chosen X).**

* If χ_D=χ_p, its term occurs in the **subtracted** sum with ξ principal. It therefore **increases** the candidate forced-window count by X^{β_D}/(2φ(M)β_D). This helps supply the sign/window candidates, not the prime-factor residues of K_q.
* If the conductor of χ_D divides M, its correction instead has coefficient −χ_D(a). Depending on the class, it helps or hurts. There is no universal abundance conclusion for every prescribed class.
* More generally χ_D can be a twist ξχ_p. If it is not induced by any of the characters in (2), there is no direct exceptional main term there. Repulsion can still improve analytic error estimates, within its ranges.

**Assessment.** Even the most favourable χ_D=χ_p case leaves balance and cap-0 membership untouched. For D unrelated to p, one must prove a relation between χ_D and the entire factor multiset of K_q; asserting “orthogonality” is also too strong, since some arithmetic alignments can occur. No such useful relation is supplied by repulsion alone. Tiny L(1,χ_D) without a quantitatively specified zero/range is still less input. Conversely, a finite profile χ_p(ℓ)=+1 does not logically exclude a distant exceptional phenomenon; “anti-Siegel” is an orientation of the local Euler-product data, not an equivalence theorem.

**PROVED (existing scoped no-go).** `POINTWISE_OMEGA15.md` Theorem 3.1 transports its planted fake through the positive reweighting 1−εχ_D, doubling the atomwise error; its §4 supplies the matching integer-side obstruction for that minorant architecture. This directly rules out repairing *that architecture* by an exceptional term. It does not rule out every nonlinear two-world argument.

## 3. Computations at a single prime and across primes

### 3.1 Design and reproducibility

**EVIDENCE (fresh census; exact spot audits).** `scripts/z45_siegel_dichotomy_scan.c` computes a_min, m_II and a local cap for **all 332180 primes p≡1 (4), p≤10⁷**. For p≡1 (8), q_F is the least prime q≡3 (8) with χ_p(q)=-1; cap_F=cap(q_F) is computed exactly, without censoring. The q≡3 (8) convention makes K odd. It differs from earlier “first q≡3 (4)” censuses and must not be compared as if the populations were identical. For p≡5 (8) cap_F is undefined, not zero.

**EVIDENCE.** Fresh f_II counts use the already-reviewed `scripts/bs_prob_fII.c`, with its ordered ET-parameter convention. Counts are not claimed to be the number of distinct unordered denominator triples. The analysis normalises by log³p and correlates D_y with log(f_II/log³p), log a_min and log(1+cap_F). The full global cap e*(p) is identically zero in this census, so its correlation is **undefined**; substituting a varying local cap without saying so would be misleading.

**CERTIFIED (audit subset).** At 333 evenly spaced census primes, a separate SymPy divisor-ratio enumeration checks all windows through m_II, rebuilds the discovered fractions exactly, and recomputes cap_F. Every fixture in `hard_primes.csv` also has its window certificates checked, and f_II is checked by the separate split single-prime engine `bs_adv_count.c`. No discrepancy occurred. The full census statistics are labelled EVIDENCE rather than independently certified exhaustively.

**EVIDENCE, resource bounds.** The C census uses about 20 MB of static arrays; the existing full f_II counter uses about 210 MB. Shell limits were 1 GB for C and 2 GB for Python; each execution had a 240/300-second timeout. Python streams character contributions one small prime at a time, not a prime-by-prime Cartesian array. Compressed raw data and the complete JSON report are retained in `data/z45_siegel_dichotomy/`.

Reproduction (from the repository, with existing dependencies):

```sh
mkdir -p data/z45_siegel_dichotomy
gcc -O2 -Wall -Wextra -Werror scripts/z45_siegel_dichotomy_scan.c -o /tmp/z45_siegel_scan
gcc -O2 scripts/bs_prob_fII.c -o /tmp/z45_siegel_fii
gcc -O2 scripts/bs_adv_count.c -lm -o /tmp/z45_siegel_single
(ulimit -v 1000000; timeout 240 /tmp/z45_siegel_scan 10000000 > data/z45_siegel_dichotomy/windows.csv)
(ulimit -v 1000000; timeout 240 /tmp/z45_siegel_fii 10000000 data/z45_siegel_dichotomy/fII.bin)
# gzip the two new raw files; do not overwrite retained copies without comparing them.
gzip -n data/z45_siegel_dichotomy/windows.csv data/z45_siegel_dichotomy/fII.bin
(ulimit -v 2000000; OPENBLAS_NUM_THREADS=1 timeout 300 uv run python scripts/z45_siegel_dichotomy_analyze.py)
```

### 3.2 Correlations

**EVIDENCE.** Pearson correlations below; cap correlations use only the p≡1 (8) subpopulation where q_F is defined. All three columns use D_50.

| population | n | log(f_II/log³p) | log a_min | log(1+cap_F) |
|---|---:|---:|---:|---:|
| all p≡1 (4), p≤10⁷ | 332180 | +0.426 | −0.475 | −0.365 |
| p≡1 (24) | 82887 | +0.535 | −0.353 | −0.151 |
| Mordell square classes mod 840 | 20513 | +0.468 | −0.191 | −0.326 |
| Mordell, 5·10⁶≤p≤10⁷ | 9802 | +0.482 | −0.187 | −0.330 |
| 0<p−⌊√p⌋²≤64 | 7379 | +0.410 | −0.507 | −0.395 |
| repository hard list, deduplicated | 14 | −0.020 | −0.299 | −0.353 |

**EVIDENCE.** On Mordell primes, using D_300 instead gives +0.462, −0.188, −0.319: extending the small-prime range adds little to these correlations. D_7 is exactly zero throughout that population, so all its correlations there are undefined. Indeed, for primes coprime to 840 with p≡1 (4), being Mordell-hard is exactly χ_p(2)=χ_p(3)=χ_p(5)=χ_p(7)=+1; it does **not** mean all primes up to an arbitrary y are residues.

**EVIDENCE.** In the bottom/top D_50 deciles of Mordell primes:

| statistic | most pretentious decile | least pretentious decile |
|---|---:|---:|
| mean D_50 | 0.231 | 0.774 |
| mean f_II/log³p | 0.0323 | 0.0456 |
| mean a_min | 10.76 | 6.01 |
| mean cap_F | 1.93 | 0.080 |
| cap_F=0 fraction | 0.418 | 0.932 |

**Assessment.** This supports the old orientation: pretence to 1 tends to obstruct rather than force easy certificates. It is not a pointwise law, and the very small selected hard list has **no count correlation**. The near-square row is not a matched-cell causal analysis; it only verifies that the sign of the observed correlation persists in that explicitly defined subset. Selecting q_F also confounds cap statistics with window size, so no causal claim about D_50 alone is justified.

**EVIDENCE (old data reanalysed).** The 351 rows in `logs/bs_adv_*.jsonl` contain 349 distinct primes. Recomputing D_50 gives correlation +0.735 with log(f_II/log³p), −0.339 with log m_II, and 11 primes with D_50=0. Those counts are inherited, not recomputed at 10¹⁶, and the sample mixes selected designs and sizes; this is a stress-test summary, not an unbiased estimate. `adversarial.csv` preserves the design tags and deduplicated inputs.

### 3.3 Individual hard cases and the strongest local pretence

**EVIDENCE, with exact fixture checks.** All 14 known (★) failures, the three b=1 failures, p=3361, p=5101441, the 14 distinct primes of `data/lsa/hard.txt` (including 20322481 and 37117609), and the least-window record are included in `hard_primes.csv`. Selected rows:

| p | f_II | D_50 | a_min | m_II | q_F | cap_F |
|---:|---:|---:|---:|---:|---:|---:|
| 193 | 4 | 1.173 | 7 | 7 | 11 | 1 |
| 409 | 12 | 1.003 | 7 | 7 | 11 | 0 |
| 2521 | 6 | 0.704 | 23 | 23 | 11 | 1 |
| 3361 | 4 | 0.687 | 3 | 3 | 11 | 1 |
| 66529 | 20 | 0.488 | 19 | 31 | 19 | 1 |
| 2451289 | 80 | 0.167 | 31 | 71 | 67 | 1 |
| 5101441 | 78 | 0.254 | 19 | 19 | 43 | 2 |
| 8803369 | 92 | 0.095 | 107 | 107 | 43 | 1 |
| 8813281 | 92 | 0.328 | 3 | 3 | 59 | 0 |
| 9257329 | 168 | **0** | 7 | 7 | 59 | 0 |

**EVIDENCE.** p=9257329 is the unique p≡1 (4)≤10⁷ with D_50=0: all primes ≤47 are quadratic residues. It nevertheless has 168 ordered Type II parameters and a cap-0 window at 7. Thus genuine “World B” pretence occurs at a single prime, but it neither proves failure nor identifies a particularly large a_min. Conversely p=8803369 is much harder by a_min with positive D_50. The maximum measured cap_F is 40, while e*(p)=0 everywhere; this sharply illustrates why a local positive cap is not a measure of global failure.

## 4. FRONTIER §4 checklist — every line

**Assessment.** PASS here means the formulation respects that screen, not that a proof exists.

1. **PASS — T1.** The forced-window premise χ_p(q)=-1 is impossible for the principal quadratic datum of an odd square. The cap-0 reduction itself also has T1. The analytic absence of a Siegel zero alone would not supply this distinction.
2. **FAIL — numerator 8 controls.** The proposed analytic completion has no new 4-specific step excluding 8/131 or 8/241 and no explicit numerator-dependent threshold. Writing K=(p+q)/4 is not a proof of the needed distinction.
3. **FAIL — numerator-uniform laws.** Generic character cancellation and repulsion are numerator-blind; no admissible 4-specific transport or closure theorem is supplied.
4. **FAIL — tied modulus.** The class is −1 mod q for a divisor ratio of the one integer K_q; equivalently (−p mod 4uv) divides u+v. Neither horn controls that event.
5. **FAIL — prescribed p recovered from analytic estimates.** Algebraic identities and conditional W keep p fixed. Halász averages n, Heath-Brown averages n, and known almost-all window estimates average p. No theorem transfers those estimates to the required divisor support at every fixed p.
6. **PASS — scale honesty.** No power-size family of ES solutions is claimed. The BM main term is ≍log²p; enlarging an exponent box changes the problem. The prime-density normalisation for (★) is 3/(2π²), not 1/8.
7. **PASS — one-sided only.** Only positivity/lower bounds are sought. Correlations are not a uniform two-sided asymptotic, which the Linnik examples forbid.
8. **FAIL for the finite-profile shortcut — B1.** D_y with fixed y is finite congruence data. Growing y and actual factorisations are allowed escape hatches, but their missing control is precisely what the analytic shortcut does not provide.
9. **FAIL — class, not parity.** Exceptional bias can increase non-residue candidates. It does not select −1 inside the permitted coset; §5 exhibits an explicit residual class failure.
10. **N.A. — pooling large primes.** No cross-shift collision is used; a future coherence theorem cannot assume private large factors coincide.
11. **N.A. — signed reflection.** No signed-to-positive transformation is proposed.
12. **FAIL — cap transport.** W gives e*(p)≤L−1. No theorem lowers that cap to zero, and no continuity in the integer cap is available.
13. **PASS — no BM shortcut.** The memo treats the BM sign/main term as already available, not as global existence.
14. **PASS — fixtures.** All listed (★) exceptions and b=1 exceptions are explicitly included. At 3361 we make no claim of a prime-modulus Type II witness; the successful m=3 ratio window is not the different PM-II notion. f_II(5101441)=78 is not its a=1 Type I count.
15. **PASS — Mordell and near-squares checked.** D_7 vanishes on Mordell classes; the near-square subset is stated exactly, and no global structural conclusion is inferred from it.
16. **N.A. — thin families.** No algebraic budget from a special p=φ(u) is transported to arbitrary primes.
17. **FAIL — large-factor classes.** The forced small-prime box cannot cover the target coset at cap 0 in the relevant regime. Neither pretentiousness of χ_p on free small primes nor repulsion controls the residues of the unforced large factors of K_q.

## 5. New-theory sketch: target-weighted phase obstructions, not an exceptional character

### 5.1 A precise elementary starting point

**PROVED (phase-separation lemma; elementary duality, no novelty claim for the principle).** At a prime window q, write χ(s)=exp(2πiθ_s), choose θ_s∈[−1/2,1/2], and suppose χ is odd, χ(−1)=-1. Define the **budget-weighted phase cost**

    T_χ(K)=Σ_{s|K} b_s ||θ_s||.

If T_χ(K)<1/2, then −1∉B(K,q). For every allowed δ, the real lift Σδ_sθ_s has absolute value ≤T_χ<1/2, so cannot be congruent to 1/2 mod 1. If T_χ=1/2, any hit must lie on an extremal face: each nonzero θ_s fixes δ_s to one of the two simultaneous choices ±b_s sign(θ_s). Zero-angle coordinates remain free. The target's remaining class in ker χ must then be tested separately. This proves a target-aware obstruction, not existence.

**Assessment.** This suggests a *phase-flag* theory: retain valuation budgets, the target phase, and the residual kernel target; successively reduce only where a phase estimate has arithmetic content. It is closer to the actual inhomogeneous lattice problem than harmonic distance on all small primes. It must allow arbitrary conductor q and higher-order characters. A theory that merely computes all faces/characters is another exact solver for B2, not a new existence mechanism.

### 5.2 The first tempting inverse conjecture is false

**CONJECTURE tested and refuted.** “Every forced window with empty cap-0 box has an odd χ with T_χ(K)≤1/2.” If true, this would turn every failed target into a geometrically narrow character direction; a separate cross-window argument might then try to exclude coherent failure. It is already false locally.

**CERTIFIED (two exact enumerations; explicit counterexample).** Take

    p=31121, q=43, K=(p+q)/4=7791=3·7²·53.

Both p,q are prime, p≡1 (8), q≡3 (8), and 43^{15560}≡−1 mod 31121. A primitive root mod 43 is 3; the discrete logs of 3,7,53 are 1,35,10 modulo 42. For odd character indices j=1,3,...,41, the exact numerators 42T_χ are

    25,57,27,35,57,41,31,75,33,53,63,53,33,75,31,41,57,35,27,57,25.

Thus min T_χ=25/42>1/2. Nevertheless the exponent box δ₃∈[−1,1], δ₇∈[−2,2], δ₅₃∈[−1,1] has 45 vectors and only 37 distinct nonzero residues; its missing residues are

    {4,11,14,40,42}.

In particular −1 is missing. The computation checks both full exponent products and independent divisor ratios. Neither insufficient box cardinality (45>42) nor a single odd-character half-turn separator explains this failure. It is an actual arithmetic window, not a fabricated discrete-log vector. **ES(31121) is easy at another window, m=3; only the proposed local inverse theorem is refuted.**

**CERTIFIED (boundary example).** At p=9833, q=67, K=2475=3²5²11, use primitive root 2 and odd character index j=27. The lifted angle numerators over 66 are −3,9,9, so T=1/2 exactly. The two extremal vectors produce residues 30 and 38, not 66. Here χ has order 22 and kernel of size 3: the projected sign is attainable but the residual kernel class is wrong. This is a concrete parity/class distinction one layer beyond a phase estimate.

### 5.3 Toy census and what a real new theorem would need

**EVIDENCE (fully enumerated finite toy, not asymptotics).** For all p≡1 (8), p≤10⁵ and q≡3 (8) prime q<200 with χ_p(q)=-1, there are 14485 pairs: 3937 cap-0 hits and 10548 failures. Of the failures, 10468 have a strict separator T<1/2, 53 have min T=1/2, and **27 have no weak separator at all**. The much smaller p≤10⁴, q≤103 pilot had only one non-strict failure; stopping at that pilot would have suggested a false inverse theorem. The enlarged experiment is the retained output.

**Assessment, first necessary new input.** A surviving theory needs a *multicharacter, target-aware inverse statement* capable of encoding the 27 residual holes, followed by a genuinely arithmetic theorem forbidding such obstructions at **all** windows in a growing p-dependent family. One useful form would bound the negative part of the exact Fourier contribution in (1), aggregated over a chosen family, by less than its principal mass at every fixed p. That is a one-sided B2 statement; no implication from Halász, a zero-free region, or Deuring–Heilbronn is known here. Requiring this theorem only under “no coherent phase flags” is not enough unless the exceptional coherent flags themselves imply a contradiction or a certificate elsewhere. The toy says that single-character pretence is not a complete list of flags.

**Assessment.** This sketch is a diagnostic framework, not a new standard conjecture implying ES. It sharpens what the structure horn would have to describe while preserving the actual target and budget. It does not yet give plausible arithmetic input for the all-window step.

## 6. Verdict and next steps

**Assessment — PARTIAL, promise 1/5.** The useful distinction is exact: free-prime quadratic pretence, high-order window-lattice pretence, and a real exceptional zero occupy different roles. The first is realised at individual primes, the second can obstruct instead of construct, and the third can improve free-prime counts without solving either target membership or the cap gap. Even assuming the strongest existing balanced-lattice horn leaves cap 0 open. The simple inverse structural horn is explicitly false at (p,q)=(31121,43). Thus this two-world strategy currently **relocates B2**, with additional B6 and numerator-specificity gaps; no new case of ES is proved.

**Assessment, concrete next steps (low priority for proving ES).**

* Classify the 27 nonseparable toy holes using two-character phase data, and test whether any criterion is stronger than an exact subgroup/box membership algorithm. This is finite and falsifiable.
* If seeking a positive analytic result, first formulate a class-sensitive theorem on the actual factors of K_q; benchmark it against (1) and 31121/43 before invoking zero repulsion.
* For statistics, condition cap_F on q_F and the Mordell residue cell, rather than fitting a causal hardness law to D_y alone. Larger y alone has already saturated in the present data.

**Files.** One memo (this file); `scripts/z45_siegel_dichotomy_scan.c`; `scripts/z45_siegel_dichotomy_analyze.py`; data, summaries, audit fixtures and verified literature extracts under `data/z45_siegel_dichotomy/`. All scripts are memory-bounded when run as documented. No existing research file is edited.
