# Z52D_FOURIER — cluster C9 (rank_O) = A02 (rank_A): bounded-exponent Fourier/character obstruction of the window event

**ES is OPEN; nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED (computer) /
EVIDENCE / CONJECTURE / Assessment. Internal results, internally reviewed only (§8).
Members: Z3003 Z2940 Z2941 Z2512 Z3002 Z2964 Z1787 (rank_O C9); Z0648 Z0674 Z2926 (rank_A A02 extras).
Scripts `scripts/z52d_fourier_*.py`; data `data/z52d/fourier/` (15 MB).

## 0. Bottom line

The cluster's hope was: (a) every obstructed window is explained by *one bounded-order character* carrying a fixed share of
the Fourier mass; (b) at hard primes *one character is shared across windows*; (c) this character is "exceptional" and
repels failure elsewhere (Linnik/Deuring–Heilbronn). Results:

* **(a) is false.** Thm B (PROVED + CERTIFIED): at a forced prime window q, if (q−1)/2 has no prime factor ≤ B, then no
  character χ ≠ 1 of order ≤ B carries positive obstruction mass. 2,115 obstructed windows with full generated subgroup
  certify this for all B ≤ 952. Under Dickson's conjecture it holds for every B (Prop B′). Two certified examples have
  boxes 2.2 and 2.5 times the group, so poverty is not the reason. Thm C gives the same in abstract cyclic groups with boxes
  much larger than the group; there the obstruction sits on characters of order |G|. Census (EVIDENCE, 56,678 windows):
  L(12, 0.1) fails at about 40 % of forced obstructed windows with full subgroup (about 48 % if χ must be odd). It fails at 67 % when the box is at least
  the group's size. Hard primes and controls do not differ.
* **(c) Only half reduces to (I)7.** By the Jacobi transfer ((J)83 Lemma 1.1), the window's BM character χ_{−e} = (·/e)
  equals χ_p = (·/p) on every prime factor of N_e. Prop 1 (PROVED): its normalised obstruction mass is exactly
  **c(χ_{−e}) = (e/p)·∏_{s|N_e, (s/p)=−1}(2b_s+1)⁻¹**. So it supports the obstruction only at unforced windows, and never at
  forced ones. Every other real character is χ_{−e}·ψ with ψ an even genus character of the window. That is the window form
  of §7.3's "other genus characters", not (I)7. Prop 2 (PROVED): a subgroup obstruction always has a witness of 2-power
  order. Real is order 2; the rest has order 4, 8, 16, 32, a 2-primary layer, and is small.
* **(b) Only χ_p is shared.** The only character shared by all windows is χ_p, i.e. the BM layer. Hard primes do have more
  χ_p kills: +20 per prime at unforced windows (t = 5.5 after covariates). This is rank_O's "real-layer excess", now
  located exactly. Forced windows are where χ_p is silent. There, hard primes show *no* excess character obstruction. Their
  genus-twist kills are fewer (−3.1 per prime), their order-≥4 kills equal the controls', and their extra failures are
  poverty (B2/B4). No fixed Dirichlet character covers more than 16 % of the forced obstructed windows of any prime, and
  hard primes are not more coherent than controls. Repulsion test: the forced-window success rate does not rise with χ_p's
  exceptionality. Partial correlation is −0.04 [−0.14, +0.06] on 400 random primes and −0.18 on the hard/control set,
  i.e. no repulsion.

**Verdict: narrowed to the point of collapse.** The bounded-order inverse sub-route is **dead** (theorem + certificate).
The single exceptional character / Deuring–Heilbronn sub-route is **dead as stated**: the only window-uniform character is
χ_p (BM, already pointwise free, FRONTIER §2.4), and no repulsion is seen (EVIDENCE). What survives is exactly §7.3
(genus twists at composite windows), §7.4, and the B2 poverty core at forced windows. That poverty core is 84 % of forced
obstructions at hard primes. C9 should be folded into §7.3; it is not a separate avenue.

## 1. Statements attacked

Setting (FORCED_WINDOW; CAP_BOUNDED §1). p ≡ 1 (mod 4) prime; window e ≡ 3 (mod 4), 3 ≤ e < 3p, p ∤ e; N = N_e = (p+e)/4;
b_s = v_s(N); G = (ℤ/e)^*. The window *succeeds* iff −1 ∈ {a·b⁻¹ mod e : a, b coprime, ab | N}, which is equivalent to an
honest Type II solution with x = N (cap 0). Equivalently, some δ ∈ ∏_s [−b_s, b_s] has ∏ s^{δ_s} ≡ −1. Note gcd(N, e) = 1,
since a common prime would divide 4N − e = p. *Forced* means (e/p) = −1 (Jacobi). *Hard* primes are the 14 (★)-zeros
≤ 10¹⁰ together with the 16 primes ≤ 10⁷ with the largest m_II (least window hitting −1; z45 census).

* **(a) Inverse lemma L(B, η)** (rank_A A02 lane): every obstructed window with ⟨prime factors of N⟩ = G has a character
  χ ≠ 1 of order ≤ B with c(χ) ≥ η (normalised mass, §2). Variant L_odd: χ is also required to be odd. — **refuted** (§3.4–3.6, §4.1).
* **(b) Shared character** (Z2940 (c), Z3003 "next", Z1787 "next"): at hard primes the obstructed windows are explained by
  ONE character, more than at controls. — **only χ_p (BM)**; no non-BM sharing (§4.2).
* **(c) Real layer = (I)7?** — **half**: the χ_{−e} part is (I)7/(J)83 exactly (Prop 1). The rest consists of genus twists,
  i.e. §7.3 (§3.2–3.3).
* **(c′) Deuring–Heilbronn analogue** (Z2941, Z2940 (c)): if χ_p is exceptional, the windows χ_p cannot touch get easier. —
  **not seen** (§4.3).

## 2. The exact identity and its bookkeeping (PROVED, elementary)

For χ ∈ Ĝ put D_b(z) = Σ_{|j|≤b} z^j, which is real on |z| = 1 (D_b(e(θ)) = 1 + 2Σ_{j≤b} cos 2πjθ). Put
F(χ) = ∏_{s | N} D_{b_s}(χ(s)), M = F(1) = ∏(2b_s+1) (the box size), and **c(χ) := −χ(−1)F(χ)/M**. The map
(a, b) ↦ δ (δ_s = v_s(a) − v_s(b)) is a bijection between coprime pairs with ab | N and the box. Since
F(χ) = Σ_{δ} χ(∏ s^{δ_s}), orthogonality gives

  r(−1) := #{δ : ∏ s^{δ_s} ≡ −1} = φ(e)⁻¹ Σ_χ χ(−1) F(χ),  r(1) = φ(e)⁻¹ Σ_χ F(χ).  (2.1)

For squarefree N this is Z3003's formula. The rank_A remark that prime powers need the signed kernel D_b is built in.
Checked against direct counts on all 173,000 windows of §4 (|difference| < 10⁻⁶·M; `z52d_fourier_scan.py` asserts it).

**Corollary 2.2 (even/odd split).** Summing (2.1) over even and odd χ separately:
Σ_{χ odd} c(χ) = φ(e)(r(1) − r(−1))/(2M) and Σ_{χ even, ≠1} c(χ) = 1 − φ(e)(r(1)+r(−1))/(2M).
*Proof.* Σ_odd F = (φ/2)(r(1) − r(−1)) and Σ_even F = (φ/2)(r(1) + r(−1)), from (2.1). Then divide by M with the signs of c. ∎

So at an obstructed window, Σ_{χ≠1} c = 1, and how the mass splits between even and odd characters depends only on
φ r(1)/M. In the poverty regime φ > 2M r(1)⁻¹, the even part is negative. At (p, q) = (31121, 43) the two largest masses
sit on **even** characters of order 7 (c = 0.200 each). The odd characters carry 0.467 in total, the largest single one
being 0.095 at order 42. A "share of the Fourier mass" is therefore a fragile notion. We test both L (all χ) and L_odd.

## 3. Proved statements

### 3.1 The transfer (known; CAP_BOUNDED (J)83 Lemma 1.1, reproduced for completeness)
**Lemma T.** For every prime s | N: (s/e) = (s/p). Hence (N/e) = (N/p) = (e/p).
*Proof.* Odd s: s ∤ e (§1). Jacobi reciprocity with e ≡ 3 (4) gives (s/e) = (−1/s)(e/s) = (−e/s). Since s | p + e, −e ≡ p
(mod s), so (−e/s) = (p/s) = (s/p) (p ≡ 1 (4)). s = 2: 8 | p + e, so e ≡ −p (mod 8), and (2/·) is invariant under
x ↦ −x mod 8. Finally 4N ≡ e (mod p), so (N/p) = (e/p). ∎
**Cor T′ (window form of (I)7; (J)83 Cor 1.2).** Every success (a, b) has (ab/p) = −1. Indeed (a/e) = (−b/e) = −(b/e) gives
(ab/e) = −1, and Lemma T converts this to (ab/p).

### 3.2 Prop 1 — the exact BM share of the Fourier mass (PROVED; new as a formula, elementary)
Let χ_{−e} := (·/e) (Jacobi). It is odd since e ≡ 3 (4). Then

  **c(χ_{−e}) = (e/p) · ∏_{s | N, (s/p) = −1} (2b_s + 1)⁻¹.**

*Proof.* By Lemma T, χ_{−e}(s) = (s/p). D_b(1) = 2b+1 and D_b(−1) = Σ_{|j|≤b}(−1)^j = (−1)^b. So
F(χ_{−e}) = ∏_{(s/p)=1}(2b_s+1) · ∏_{(s/p)=−1}(−1)^{b_s}. The sign is ∏_{(s/p)=−1}(−1)^{b_s} = (N/p) = (e/p) (Lemma T), and
c = −(−1)F/M = F/M. ∎
*Consequences.* (i) χ_{−e} *kills* the window (c = 1) iff every prime factor of N is a QR mod p. This forces (e/p) = 1:
**the BM character never obstructs a forced window.** At forced windows it always pushes towards success:
c(χ_{−e}) = −∏(2b_s+1)⁻¹ < 0. (ii) Across windows, χ_{−e} is one and the same character χ_p evaluated on the prime factors
of the consecutive integers N = (p+3)/4, (p+7)/4, … . It is the only window-uniform character family we know (Assessment,
§4.2). CAP_BOUNDED Thm 1.3 (CONDITIONAL, Dickson) is the extreme case: all windows ≤ M are unforced and all
are χ_p-killed.
*CERTIFIED check:* across all 173,000 scanned windows, kill by χ_{−e} at a forced window occurs 0 times, and sign c(χ_{−e}) ≠ (e/p)
occurs 0 times.

### 3.3 Real layer = BM twisted by even genus characters; subgroup obstructions are 2-primary (PROVED)
**Prop 2.** (i) Every odd real character of G is χ_{−e}·ψ with ψ even real, and on prime factors of N it equals
(·/p)·ψ. (ii) ψ(N) = ψ(p/4) depends only on p mod e (CLASS_FORCING Thm 2.1(a)). (iii) If an odd χ is trivial on
H = ⟨s | N⟩, then χ^u is too, where u is the odd part of ord χ; χ^u is odd and has 2-power order. Hence the least order of
a "killing" character is always a power of 2.
*Proof.* (i) Real characters form a group and χ·χ_{−e} is even; then apply Lemma T. (ii) 4N ≡ p (mod e). (iii) χ^u(−1) =
(−1)^u = −1, and χ^u is trivial wherever χ is. ∎
So the real layer is {BM} ∪ {BM twisted by an even genus character of e}. ψ = 1 is (I)7 (§3.2). The twists ψ ≠ 1 exist
only at composite e. They are the window form of FRONTIER §7.3's "other genus characters, which can obstruct" (the same
kind of object, not the same sum: §7.3 is in level coordinates). **Prop 3** (known, CAP_POINTWISE (J)64): at a forced
*prime* window q, −1 ∈ H. *Proof:* (N/q) = −1 gives a factor s with (s/q) = −1. Its order in the cyclic group is even, so
s^{ord(s)/2} = −1. ∎ Subgroup-type obstructions at forced windows therefore occur only at composite e, by genus twists or
2-power characters (CERTIFIED: 0 exceptions). The kills that use no real character have least orders 4, 8, 16, 32 only
(EVIDENCE: 855 such windows in the hard/control scan, 912 in the random scan, §4).

### 3.4 Thm B — the bounded-order inverse lemma is false at arithmetic windows (PROVED)
**Theorem B.** Let q be a forced prime window at p such that every prime factor of (q−1)/2 exceeds B. Then every χ ≠ 1 of
(ℤ/q)^* with ord χ ≤ B equals χ_{−q}, and c(χ_{−q}) < 0. Hence, if the window is obstructed, L(B, η) and L_odd(B, η) fail
there for every η > 0.
*Proof.* q ≡ 3 (4), so q − 1 = 2m with m odd. Orders of characters divide q − 1. A divisor d ≤ B of 2m has no odd prime
factor ≤ B, so d ∈ {1, 2}. The order-2 character is χ_{−q}, and Prop 1 at a forced window gives c < 0. ∎

**CERTIFIED (`z52d_fourier_scan.py`, then independently `z52d_fourier_certify.py` with sympy and no Fourier code).**
2,115 windows in the hard/control scan are forced prime windows with (q−1)/2 prime, obstructed, and ⟨factors⟩ = G. They
involve 35 distinct q, up to q = 1907 (p = 102001, N = 25977 = 3·7·1237). This refutes L(B, η) for every B ≤ 952. The
poverty objection fails on two examples. (p, q) = (5211721, 479): N = 2·3·5²·7·17·73, box M = 1215 = 2.54|G|, 449 of the
478 residues hit, −1 missed, H = G; refutes B ≤ 238. (1714441, 503): N = 2⁶·3·7·11·29, M = 1053 = 2.10|G|, H = G; refutes
B ≤ 250. (57 Thm B windows have M ≥ |G|.)

**Prop B′ (CONDITIONAL on Dickson's conjecture for two linear forms).** For every B there are infinitely many (p, q) as in
Thm B, with N prime and ⟨N⟩ = G.
*Proof.* Dirichlet gives a prime q > 3 with q ≡ 3 (mod 8) and q ≡ 2 (mod ℓ) for each odd prime ℓ ≤ B. Then ℓ ∤ q − 1, and
(q−1)/2 is odd, so all its prime factors exceed B. Let g be a primitive root mod q and N₀ an odd integer ≡ g (mod q). Put
p₀ = 4N₀ − q ≡ 1 (mod 8), f₁(t) = 8qt + p₀ and f₂(t) = 2qt + N₀. Then f₁ = 4f₂ − q. The pair is admissible: both forms
are odd at ℓ = 2; at ℓ = q they are ≡ 4g and g, both nonzero; at any other ℓ ≥ 3 each has a single root, so at most 2 of
the ℓ ≥ 3 classes are excluded. Dickson gives infinitely many t with p = f₁(t) and N = f₂(t) both prime. Then
p ≡ 1 (mod 8), (q/p) = (p/q) = (4g/q) = −1 (forced), N = (p+q)/4 ≡ g (so H = G), and the box {1, N, N⁻¹} misses −1, since
ord g = q − 1 > 2. ∎

### 3.5 Thm C — abstract groups, boxes larger than the group (PROVED)
**Theorem C.** Let G = ℤ/m, m even, with target τ = m/2. Take k < m/2 generators all equal to 1, each with budget 1 (a box
of size 3^k, which can be far larger than m). Then the box {−k, …, k} misses τ and H = G. Every character χ_r of order
d ∈ [2, B] has |c(χ_r)| ≤ (ρ_B/3)^k, where ρ_B = max(1, 1 + 2cos(2π/B)) < 3. Meanwhile the odd character χ_1 (order m) has
c(χ_1) ≥ 1 − 4π²k/(3m²).
*Proof.* F(χ_r) = (1 + 2cos 2πr/m)^k. For order d the angle is j/d with gcd(j, d) = 1. If d = 2, |1 + 2cos π| = 1. If
d ≥ 3, 1 + 2cos(2πj/d) ∈ [−1, 1 + 2cos(2π/B)]. For χ_1: χ_1(τ) = −1, so c = ((1 + 2cos(2π/m))/3)^k. Now
1 + 2cos x ≥ 3 − x², and Bernoulli gives (1 − x²/3)^k ≥ 1 − kx²/3. ∎
So for k > log(1/η)/log(3/ρ_B) and m > 2k, L(B, η) fails, and the obstruction sits on characters of order ≍ |G| (Bohr /
low-frequency structure, not bounded order). Numerically confirmed for (m, k) = (40, 19), (100, 49), (400, 60).

### 3.6 What *is* true, and why it is empty (Assessment)
The any-order version, "some χ ≠ 1 has c(χ) ≥ η", holds at 98–100 % of obstructed windows for η = 0.2 (§4.1). The median
of the maximal c is 0.5–1.0, and it grows as the box shrinks. The reason is pigeonhole. Dirichlet simultaneous
approximation on Ĝ gives χ ≠ 1 with every phase θ_s(χ) of size ≤ |G|^{−1/k}, so |F(χ)| ≈ M. This happens whatever the
target, so it carries no information about −1. (The positive-sign version is not provable this way, because the parity of
the pigeonholed χ is not controlled. The z45 counterexample 31121/43 shows that no odd χ even clears the half-turn
separation threshold there.)

## 4. Computations (EVIDENCE unless marked CERTIFIED)

Hard set: 30 primes. Controls: 116 primes, the nearest 2 below and 2 above each hard p in the same class mod 840
(`z52d_fourier_primes.py`; matching mod 840 fixes (ℓ/p) for ℓ ≤ 7). Windows 3 ≤ e ≤ 2000, e ≡ 3 (4): 500 per prime,
73,000 in total (`scan_hardctrl_E2000.jsonl.gz`). Random set: 400 primes p ≡ 1 (24) in [10⁶, 10⁷] (seed 52041), e ≤ 1000,
100,000 windows (`scan_random400_E1000.jsonl.gz`).

Per-prime window classes (F = forced, U = unforced; sub = −1 ∉ H; pov = −1 ∈ H but missed by the box):

| | F-ok | F-sub | F-pov | U-ok | U-sub | U-pov |
|---|---|---|---|---|---|---|
| hard (30) | 13.7 | 36.5 | 186.6 | 3.2 | 207.7 | 52.3 |
| control (116) | 17.3 | 39.6 | 184.8 | 5.9 | 187.4 | 64.9 |

Subgroup kills per prime: U by χ_{−e} 195.4 vs 175.4; U by genus twist only 10.7 vs 10.5; F by genus twist 32.8 vs 35.1;
kills by non-real characters only 3.7 + 1.6 vs 4.5 + 1.5 (F + U).

### 4.1 Inverse lemma (a)
Share of obstructed **forced** windows with H = G at which L(B, η) holds (all χ | odd χ):

| set (n) | B=2, η=.1 | B=6, η=.1 | B=12, η=.1 | B=12, η=.2 | B=24, η=.2 |
|---|---|---|---|---|---|
| hard (5,124) | .33 \| .32 | .51 \| .45 | .61 \| .52 | .47 \| .36 | .57 \| .48 |
| control (19,437) | .33 \| .31 | .52 \| .45 | .62 \| .52 | .48 \| .37 | .58 \| .49 |
| random (32,117) | .34 \| .32 | .51 \| .45 | .63 \| .52 | .48 \| .36 | .59 \| .50 |

In the non-poverty regime (hard + control, forced, H = G): with M ≥ φ(e), 265 of 1,190 windows are obstructed, and L(12, .1)
holds at only .33 | .25. With M ≥ 2φ(e), 23 of 512 are obstructed, holding at .22 | .17. With M ≥ 4φ(e), none of 172 is
obstructed. At unforced windows L(2, .1) holds at 97–100 %, but that is χ_{−e}, whose share is fixed by Prop 1.

Small groups (`smallgroups.jsonl`: ℤ/m, m ≤ 46 even, k ≤ 4 generators with budget 1, every multiset with full subgroup;
**CERTIFIED** exhaustive). At m = 46 (q = 47, safe prime), L(12, .1) holds for .37/.46/.44 of the obstructed configurations
for k = 2/3/4, and L(12, .2) for 0. At m = 42, k = 4 (42,924 obstructed configurations) the figures are .72 and .16.

### 4.2 Cross-window sharing (b) (`z52d_fourier_xwin.py`)
For a primitive ψ of conductor f ≤ 200, induced to every window f | e, count the obstructed windows where c(ψ) ≥ η.
* Forced obstructed windows, η = 0.15: the best single ψ covers on average 10.0 % (hard) and 10.7 % (control); the maxima
  are 16.0 % and 14.8 %. The mean rank of hard primes is 56.6 against 72.5 expected, so hard primes are slightly *less*
  coherent. The best ψ is (·/3), a genus character, at 29 of the 30 hard primes; at 329617 it is (·/5). At η = 0.3: 7.4 % vs 8.1 %.
* Structural reason (Assessment): a fixed Dirichlet ψ exists only at windows f | e (relative density ≤ 1/3). χ_{−e} is the
  one family defined at every window, and the reason is the reciprocity transfer to χ_p. By CLASS_FORCING Thm 2.1, no
  higher reciprocity law supplies another such family.
* Where the hard-prime excess sits (`z52d_fourier_excess.py`, OLS with covariates qr = share of ℓ ∈ [11, 97] with
  (ℓ/p) = 1 and the mean ω(N_e)). U-sub by χ_{−e}: +20.0 per prime raw, +18.8 adjusted (t = 5.5). U-pov: −12.6 (t = −4.3).
  F-pov: +1.7 raw, +1.0 adjusted (t = 0.6). F-sub by genus twist: −3.1 (t = −3.2). F-ok: −3.6 raw, −2.9 adjusted
  (t = −3.5; a selection effect). **The shared-character excess is entirely χ_p at unforced windows**: the window-level face of a small BM
  main term. Forced windows carry no character excess.

### 4.3 Repulsion (c′) (`z52d_fourier_repulsion.py`)
Let x = the share of unforced windows killed by χ_p (χ_p's "exceptionality" on the window integers), and y = the forced-window
success rate.
* Random 400: corr(x, y) = +0.040 [−0.059, +0.137]. Partial correlation given the forced mean log M and qr: −0.039
  [−0.136, +0.060].
* Hard + control (146 primes, e ≤ 2000): corr = −0.388. Partial: −0.180 [−0.333, −0.016]. Exceptional χ_p goes with
  *harder* forced windows, if anything. This matches z45's "pretence makes primes harder on average".

No Deuring–Heilbronn-type repulsion is visible.

## 5. Verdict for C9 / A02
**Narrowed to collapse.** Killed: (a) as a bounded-order statement (Thm B, PROVED + CERTIFIED to B ≤ 952; CONDITIONAL for
all B; Thm C in abstract groups). Also killed: the any-order version as a source of information (§3.6). Killed at
EVIDENCE level: (b)/(c′) as a non-BM shared exceptional character (§4.2–4.3). Reduced: the real layer, to (I)7 (BM, exact
mass Prop 1, silent at forced windows) plus genus twists (Prop 2). The genus twists are §7.3's object. Surviving and
unchanged: §7.3, §7.4, and the B2 poverty core (forced windows: 186.6 of 223.1 obstructions per hard prime are poverty
type). Z3003's identity stays a correct *exact* certificate of failure. It is no handle on existence: any inverse theorem
would have to describe Bohr-type, order-≍|G| structure (Thm C) together with a target-aware sign (31121/43), i.e. B2 itself.

## 6. Proposed FRONTIER changes (not applied)
* §7.3, append: *(z52d, `Z52D_FOURIER.md`.)* In window coordinates (e ≡ 3 (4), N = (p+e)/4), the BM character χ_{−e}
  carries exactly c = (e/p)∏_{s|N,(s/p)=−1}(2b_s+1)⁻¹ of the normalised Fourier obstruction mass (PROVED). It obstructs only
  unforced windows. Every other real obstruction is χ_p twisted by an even genus character of the window (this item's
  object), and subgroup obstructions are 2-primary. A bounded-order character inverse lemma is false (Thm B: PROVED;
  CERTIFIED for B ≤ 952, including boxes 2.5|G|; Dickson for all B). No non-BM character is shared across the forced windows
  of hard primes, and no Deuring–Heilbronn repulsion appears (EVIDENCE, 30 hard / 116 matched / 400 random primes). The
  "regime split / exceptional character" cluster (C9/A02) therefore reduces to this item plus B2.
* §6 dead ends, add: "Fourier/character inverse for window obstructions (Z3003 route): bounded-order version false
  (`Z52D_FOURIER` Thm B, C); any-order version vacuous by pigeonhole; the only shared character is χ_p (BM), silent at
  forced windows; no repulsion (EVIDENCE)."

## 7. Reproduction
All commands are run from `scripts/` with `ulimit -v 8000000`:
`python z52d_fourier_primes.py` → `primes.json`;
`xargs -P8 -I{} sh -c 'python z52d_fourier_scan.py 2000 {} > /tmp/scan/{}.jsonl'` over hard ∪ control, and the same with
`1000` over `random400.txt` (≈ 3 + 9 min on 8 cores), concatenated, then compacted with `z52d_fourier_compact.py` (keeps the
top-character lists with conductor ≤ 200);
`python z52d_fourier_analyze.py <scan>` (→ `analyze_*.txt`), `z52d_fourier_xwin.py <scan> 0.15|0.3`,
`z52d_fourier_excess.py <scan>`, `z52d_fourier_repulsion.py <scan>`, `z52d_fourier_smallgroups.py 46` (6 s),
`uv run --with sympy python z52d_fourier_certify.py` (→ `certify_thmB.txt`).

## 8. Review
(§8 is filled in after the hostile review.)
