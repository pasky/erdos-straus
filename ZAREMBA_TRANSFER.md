# ZAREMBA_TRANSFER — the 2026 pointwise Zaremba method, tested on ES in continued-fraction coordinates (O266)

Status: working file (spark relay on O261). **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md.
The two 2026 preprints (Shkredov arXiv:2603.14116v2; X. Zhang arXiv:2605.02518v2) are **unrefereed**; anything that uses
them is CONDITIONAL on their correctness. Scripts `scripts/z36_*`; memos `BRAINSTORM/z36_*.md`.

Notation (DEDEKIND_ES): for a prime p and 0 < A < p, `r(p/A)` = Hirzebruch–Jung (HJ) length of p/A = 1 + Σ_{i odd} a_i
where p/A = [a₀; a₁, a₂, …] is the regular CF. `λ(p) = min{ r(p/A) : (A/p) = −1 }`. ES-five(p) ⟺ λ(p) ≤ 3 for p ≡ 1 (8)
(DEDEKIND_ES Cor 4.6, PROVED). `S_L(p) = {A ∈ (ℤ/p)^* : r(p/A) ≤ L}`.

## 0. Iteration log
* cp0: merged O261; read Shkredov §§2, 4, 5.1 (arXiv PDF, pdftotext in /tmp, not committed) and Zhang §3 (Thm 3.6, (3.1)–(3.8)).

## 1. The method, extracted (read in the sources; page refs to the arXiv PDFs)

**1.1 Objects.** Fix q and t = q^{1/2−ε}, N = q^{2ε} (so t²N = q) [Shk §5.1]. `Z_M(t) ⊆ ℤ/q` = numerators a whose CF
digits are ≤ M for all convergents with denominator < t [Shk (24)]. By Lemma 13 [Shk p. 8] Z_M(t) is a disjoint union of
T ≍ t^{2w_M} intervals of length between N and 16MN, i.e. `A = Λ ∔ [N]`, with |A| ≍ q^{w_M} N^{1−w_M} [Shk §5.1]. The
interval J_{u/v} is indexed by the prefix u/v (Shk (28)–(30)): **the prefix fixes the interval, the unresolved tail is the
position inside it.**

**1.2 The gluing.** By CF reversal (Shk (134)–(135)) a ∈ Z_M(t) ∩ Z_M(t)^{−1} has bounded digits at both ends (convergent
denominators < t and > q/t); only the *critical* middle window [t, q/t] = [q^{1/2−ε}, q^{1/2+ε}] is uncontrolled.
* Counting step (Shk Cor 16, via Lemma 14/15 = Bourgain–Gamburd + Helfgott; Zhang Thm 3.6 for all q):
  `|A ∩ B^{−1}| = |A||B|/q + O(√(|A||B|)·N^{−κ})` for A = Λ₁ ∔ [N], B = Λ₂ ∔ [N]; Zhang's form counts
  `(a + 2j)(b + 2j) ≡ 1 (mod q)`, j ≤ N, i.e. `g_j a = −b` with `g_j = [[2j, 1−4j²],[−1, 2j]]`, the generating set
  S = {g_j : j ≤ N} of size q^{2τ} (Zhang (3.1)–(3.5), Remark 1.4). Note g_j = ±T^{2j}ST^{2j}: **the expander alphabet is a
  set of HJ letter pairs with large letters 2j ≤ 2N** — the same kind of letters ES certificates are made of (§3).
* Main term beats error iff `|A|·N^{κ} ≫ q` [Shk (132)]: q^{2ε(1+κ−w_M)} ≫ q^{1−w_M}, i.e. **ε ≳ (1−w_M)/(2(κ+1−w_M))**,
  i.e. ε ≫ 1/M (Shk (133)); Zhang's version τη > 1/M (Zhang (3.8)). κ, η are tiny absolute constants.
* Middle step (Shk §4, Assumption 22, Lemmas 25–33, Prop 35): most a ∈ Z_M(t) ∩ Z_M(t)^{−1} have no M̃-critical
  denominator in the window; this needs ε ≤ ε₀ (an absolute constant; Shk §4 first paragraph: "(61), (99), (119) give an
  upper bound for ε").
* Coprimality / composite q: Lemma 20; Zhang §2 growth for arbitrary q.

**1.3 The threshold, stated exactly (Assessment from the sources).** The method needs a window ε with
`(1−w)/(2(κ+1−w)) ≲ ε ≤ ε₀`, i.e. **1 − w ≤ 2κε₀/(1 − 2ε₀) = κ/8** — a *near-full-dimension* condition on the digit set, not merely
w > 1/2. Equivalently: each half set must have density ≥ N^{−κ} = q^{−2κε} in ℤ/q (condition (40) of Shk:
|A|N^{κ/2} ≫ q^{1+o(1)}). The gluing count |A|²/q = q^{2w−1}·N^{2−2w} is then a power, but **a power-size count is not
sufficient**: Zaremba with M = 5 (w₅ ≈ 0.837, count ≈ q^{0.67}) is out of reach of the method (Zhang Remark 1.3: "Lowering
this bound to 5 … requires a new idea"). The brief's "M1 power-size main term" should be sharpened to
**M1⁺: half sets of density q^{−o_κ(1)} at the gluing scale.**

**1.4 Explicit constants (Shk §5, Appendix, prime q).** ε < 1/18 is forced by the critical-denominator step (Shk (151),
(156)); so the gluing intervals have length N = q^{2ε} < q^{1/9} (Shk p. 6: "intervals of length q^{1/9−o_M(1)}").
κ ≥ 2^{−1656}, M = 22000 suffices for large primes (Shk (158)); Zhang: M large, τη > 1/M.

## 2. The ES ladder in CF coordinates, and the first rung that is a theorem

**2.1 Rungs.** Rung L: **λ(p) ≤ L**, i.e. *some quadratic non-residue A mod p has HJ length r(p/A) ≤ L*. L = 3 is ES-five
(DEDEKIND_ES Cor 4.6, p ≡ 1 (8)). Every rung is T1-compatible: at n = m² (Jacobi symbol in place of Legendre) there is no
non-residue at all, so every rung fails at squares, for the trivial reason that the target set is empty.

**2.2 Sizes (EVIDENCE, `scripts/z36_ladder.py`, full enumeration at single n).**

| n | |S₃| | |S₄| | |S₆| | |S₈| | QNR share in S₃ / S₄ / S₈ | |S_L| at L = ⌊log n⌋ (= n^θ) | median r | λ |
|---|---|---|---|---|---|---|---|---|
| 10009 | 63 | 229 | 685 | 1594 | 0.70 / 0.75 / 0.54 | 2108 (θ = 0.83) | 16 | 2 |
| 100049 | 97 | 327 | 2138 | 6033 | 0.64 / 0.75 / 0.52 | 16393 (θ = 0.84) | 20 | 2 |
| 1000033 | 121 | 654 | 4518 | 19037 | 0.73 / 0.78 / 0.53 | 126657 (θ = 0.85) | 26 | 2 |
| 994009 = 997² | 97 | 406 | 4470 | 18435 | 0 / 0 / 0 | 124848 (θ = 0.85) | 26 | — |

Readings: (i) fixed-L rungs have polylog size (|S_L| ≈ (log p)^{L−1}·c_L); ES-five (L = 3) has ≈ 10² certificates at
p ≈ 10⁶, the QNR share ≈ 3/4 (the genus cells of DEDEKIND_ES Thm 4.5 favour −1 at primes). (ii) The size becomes a power
only at L ≍ log p: |S_{c log p}| = p^{θ(c)}, θ(1) ≈ 0.85, θ(1/2) ≈ 0.61 (numerics at 10⁶). (iii) The median of r is
≈ 1.9 log p at 10⁶ (slowly increasing ratio: 1.6, 1.74, 1.74, 1.88 at 10³ … 10⁶, consistent with log p·log log p).
(iv) T1 control: at 997² the ladder sets have the same sizes as at a prime, but contain no Jacobi −1 element.

**Theorem A (PROVED, elementary; KNOWN in substance: it follows from M.-C. Chang, "Partial quotients and equidistribution", Thm 5 — most primitive roots x mod p have Σ a_i(x/p) ≪ log p log log p, and primitive roots are non-residues; the log p log log p level for some numerator is Larcher's (1.1) there. Read in Chang's preprint, math.ucr.edu/~mcc/paper/141; Chang notes that removing the log log factor "is still open and would follow from … Zaremba's conjecture").** For every prime p > 5,
`λ(p) ≤ 1 + 10(1 + log p)(1 + log T)`, `T = ⌈10(1 + log p)⌉`. In particular λ(p) ≪ log p · log log p: *in the Farey/HJ
metric the least quadratic non-residue is O(log p log log p) unconditionally* (the archimedean least non-residue is only
known to be ≪ p^{0.152}, and ≪ log² p under GRH; note r(p/n_p) ≤ n_p, so GRH gives only λ ≤ 2 log² p).

*Proof.* Let a/p = [0; c₁, …, c_s], Euclid remainders ρ_{−1} = p, ρ₀ = a, ρ_i = ρ_{i−2} − c_iρ_{i−1} (ρ_s = 0), convergent
denominators q_{−1} = 0, q₀ = 1, q_i = c_iq_{i−1} + q_{i−2}. Standard identities: q_iρ_{i−1} + q_{i−1}ρ_i = p and
a·q_i ≡ (−1)^i ρ_i (mod p). For 1 ≤ i ≤ s put x = q_{i−1} ≥ 1, y = ρ_{i−1} ≥ 1, σ = (−1)^{i−1}: then ax ≡ σy (mod p) and
c_i ≤ ρ_{i−2}/ρ_{i−1} ≤ p/(q_{i−1}ρ_{i−1}) = p/(xy). The map (a, i) ↦ (x, y, σ) is injective: x < p is invertible, so
a ≡ σ y x̄; and q₀ ≤ q₁ < q₂ < ⋯ with q₀ = q₁ only when c₁ = 1, where σ separates i = 1, 2. Hence for k ≥ 1
`#{(a, i) : c_i ≥ k} ≤ 2·#{x, y ≥ 1 : xy ≤ p/k} ≤ 2(p/k)(1 + log p)`.
Summing over k ≤ T: Σ_a Σ_i min(c_i, T) ≤ 2p(1 + log p)H_T ≤ 2p(1 + log p)(1 + log T), and #{a : max_i c_i > T} ≤
2p(1 + log p)/(T + 1) < p/5. By Markov, #{a : Σ_i min(c_i, T) > 10(1 + log p)(1 + log T)} ≤ p/5. So at least
(p − 1) − 2p/5 > (p − 1)/2 residues a (p > 5) have Σ_i c_i ≤ 10(1 + log p)(1 + log T); there are only (p − 1)/2 residues,
so one of them is a non-residue A. Finally r(p/A) = 1 + Σ_{i odd} a_i(p/A) ≤ 1 + Σ_i c_i(A/p), since A/p = [0; a₀, a₁, …]. ∎

*Barrier reading.* Theorem A is a counting/pigeonhole proof whose main term is a positive proportion of ℤ/p: it is the
rung where the certificate set has density ≫ 1 (M1⁺ trivially). The step false at m² is "#non-residues = (p−1)/2".
Gap to ES: from L ≍ log p log log p (density 1/2) to L = 3 (count ≍ log² p) — the full B3 scale gap, now in one metric.

## 3. ES-five in the gluing language; the "alphabet knob" is vacuous

**Lemma C (PROVED, elementary).** Let p be prime and t, u, v ≥ 2. Then `tuv − u − v = p` ⟺
`t ≡ ū + v̄ (mod p)` and `tuv − u − v < 2p` (ū, v̄ inverses mod p).
*Proof.* If tuv − u − v = p then p ∤ uv (else p | u and p | v, and tuv ≥ 2p² > p + u + v). For p ∤ uv,
tuv − u − v ≡ 0 ⟺ t ≡ ū + v̄; and tuv − u − v ≥ 2uv − u − v > 0, so it equals kp with k ≥ 1, and k = 1 ⟺ < 2p. ∎
So the length-3 certificates are the solutions of the **reciprocal-sum congruence** ū + v̄ ≡ t with (t, u, v) in the
hyperbolic region tuv ≲ 2p. In Möbius form v = h_t(u), h_t(x) = x/(tx − 1) (matrix [[1, 0], [t, −1]], a conjugate of ST^tS):
ES-five(p) asks whether **some h_t, t ≤ T, maps the origin interval [U] into the origin interval [V]**, UVT ≍ p. This is
the shape of Shk Lemma 15 / Zhang (3.4) — a family of Möbius maps (g_j there, h_t here; both one-parameter families of
"two-letter" HJ words with one large letter) gluing two sets — but with A = B = {0} and S = [U] × [V] a box at the origin
of the modular hyperbola: expected count UVT/p ≍ 1 per dyadic box, ≍ log² p boxes. The asymptotic regime of every known
estimate for such counts needs a power more (Shparlinski's modular-hyperbola Thm 13: UV ≫ p^{3/2}; Shk Lemma 15: dense
A, B; Bourgain–Garaev reciprocal sums: energies, not existence). (Assessment.)

**Lemma D (PROVED; the region knob produces nothing).** Enlarging the region to tuv − u − v < (K + 1)p produces
exactly the length-3 HJ certificates of the multiples kp, k ≤ K (Lemma C with k free). Every ES statement they certify is
about kp, and ES(kp) already follows from ES(k) by scaling, so no information about p results. Hence the only nontrivial
knobs in CF coordinates are the **length L** (§2) and the **character condition** (§4). (Without χ, the L = 3 rung is
"t/p = 1/(ab) + 1/(an) + 1/(bn) for some t ≥ 2" — memo z36_numerator_free_rung — still a B2 lottery.)

## 4. The χ-twist: what the 2026 method would buy, and where it stops

**Hypothesis ZQ_M.** Every sufficiently large prime p has a quadratic non-residue a whose CF digits are all ≤ M.
EVIDENCE (`scripts/z36_zq.py`): ZQ₄ holds for all primes 7 ≤ p < 2·10⁴, and ZQ₃ for all of them except p = 277; ZQ₃ for all
primes in [10⁵, 1.02·10⁵) and [10⁶, 1.001·10⁶). In every case except 277 the QNR restriction costs nothing (min over
non-residues of the max digit = Zaremba's min).

**Theorem B (CONDITIONAL on ZQ_M; elementary).** λ(p) ≤ 1 + M·⌊s/2⌋ ≤ 1 + M(log p/(2 log φ) + 1) ≈ 1.04 M log p.
*Proof.* As in Thm A, r(p/A) = 1 + Σ_{j even} c_j(A/p) ≤ 1 + M⌊s/2⌋, and q_s = p ≥ φ^{s−1}. ∎
**Reading (Assessment, the main quantitative finding).** Theorem A (Chang/Larcher, unconditional) already gives
λ(p) ≪ log p log log p. So the full 2026 Zaremba machinery, *even if extended to non-residues*, would improve the ES ladder
only by the factor log log p (exactly Chang's "remove the log log" question), with constant M ≥ 22000 (Shk (158)).
ES-five needs λ(p) ≤ 3. The method's contribution to the ES gap is therefore asymptotically negligible.

**Why Shkredov/Zhang do not give ZQ (Assessment; precise obstruction to the naive twist).**
1. *Window conflict.* The only place the method sees individual residues is the gluing intervals A = Λ ∔ [N], N = q^{2ε}
   with ε < 1/18 (Shk (151)). A character-sum input on those intervals needs N ≥ q^{1/4+δ} (Burgess), i.e. ε > 1/8.
   1/8 > 1/18: the two requirements are incompatible. (A QNR in every interval of length q^{1/9} would give n_p ≪ p^{1/9},
   beyond Burgess's exponent 1/(4√e) ≈ 0.152.)
2. *T1 location.* Zhang's Zaremba holds for every q, squares included; ZQ fails at every q = m² (no non-residue). So no
   proof of ZQ can consist of growth/expansion statements in SL₂(ℤ/q) alone: it needs an input that is false at squares
   (a Burgess/Weil-type cancellation of the Jacobi symbol). The glued numerator's χ-value is not a function of its two
   half-set classes (the middle window carries the χ information), so the missing input must control χ on
   A ∩ B^{−1} itself — an incomplete-character-sum-on-a-glued-Cantor-set problem not addressed in either preprint.
3. *Multiplier escape (PROVED reduction, CONDITIONAL on the preprints).* By Shk Lemma 10, c·Z_M(q) ⊆ Z_{O(cM)}(q) for
   1 ≤ c < q: if ax ≡ y (mod q) has solutions with x|y| ≥ q/M only, then (ca)x ≡ y gives a(cx) ≡ y, so cx|y| ≥ q/(4M)
   (constants as in Lemma 10). Taking c = n_p (least non-residue) and a a Zaremba numerator: if a is a residue, ca is a
   non-residue. Hence Zaremba(M) ⟹ ZQ_{O(M n_p)} — useless pointwise (n_p ≪ p^{0.152}), and under GRH gives only
   λ ≪ M log³ p, worse than Theorem A.
