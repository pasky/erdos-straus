# Hostile review R49 of POINTWISE_OMEGA14.md (task O49, branch side-agent/junta-third)

Reviewer branch: side-agent/review-omega14. Reviewed state: junta-third @ 12df24b.
Status: ROUND 1 COMPLETE.

## Verdicts (summary; filled in as the review proceeds)

| claim | verdict |
|---|---|
| Lemma 1.1 (planting) | SOUND |
| Thm 1.3 (abstract level barrier) | SOUND (minor: integrability/a.e. remark) |
| Setting 2.0 reduction level ≤D ⇒ 𝒱_k | SOUND |
| §1 numerics (2), toy LP | SOUND-AFTER-REPAIRS (wording: grid values, not thresholds) |
| Lemma 2.1 | SOUND |
| Lemma 2.2 | SOUND (modulo BV + fundamental lemma, as labelled) |
| Lemma 2.3 (m-copy Janson) | SOUND (minor: w_ℓ citation) |
| Thm 2.4 | SOUND |
| Cor 2.5 | SOUND-AFTER-REPAIRS (wording: Selberg/β-sieve "need" only when used densely) |
| Thm 2.6 | SOUND (minor: blocks only fibres with log(1/δ)≪𝓛^4/(log𝓛)²) |
| Prop 2.7 + scope | SOUND; labels honest |
| Cor 3.1 | SOUND |

## Claim-by-claim

### Lemma 1.1 (planting) — SOUND

Re-derived independently.
* Marginals: for |K|≤k, z⊆K, the σ_J-mass of {x_K=1_z} is [z⊆J]·Σ_{y'⊆J∖K}(−1)^{|z|+|y'|+1};
  J∖K≠∅ since |J|=k+1>|K|, so the alternating sum vanishes. ✔ (K=∅ gives total mass 1.)
* ν(0)=P_0−P_0Σw_J=0 ✔.
* Positivity: negative atoms are exactly 1_y with |y|=j even, 2≤j≤k+1, receiving
  P_0∏_y r·e_{k+1−j}(s)/e_{k+1}(r). Needs e_{k+1−j}(s)≤e_{k+1}(r). The counting identity
  Σ_{|I|=n−1}∏_I s·Σ_{i∉I}s_i = n·e_n(s) and Σ_{i∉I}s_i ≥ Σs−(n−1)r* give
  n e_n(s) ≥ e_{n−1}(s)(R−jr*−(n−1)r*) ≥ e_{n−1}(s)(R−(2k+1)r*) ≥ (k+1)e_{n−1}(s) ≥ n e_{n−1}(s)
  for n≤k+1 (uses j≤k+1, n−1≤k). Chaining n=k+2−j..k+1 gives e_{k+1−j}(s)≤e_{k+1}(s)≤e_{k+1}(r). ✔
* Edge cases: zero p_i (w_J=0 for J∋i, harmless); k=0 (no even |y|≥2 atoms; only needs
  e_1>0); e_{k+1}(r)>0 argued correctly. p_i<1 required for r_i finite — stated.
* From-scratch check `scripts/review_o14_planting.py` (full 2^n enumeration, exact Fractions,
  n≤10, k≤3; random p incl. exact zeros and one large coordinate p_0∈[0.6,0.9]; plus 18
  *equality* instances R=(k+1)+(2k+1)r*): 97+18 instances satisfying (1.1), **0 failures**
  of ν≥0, ν(0)=0, mass 1, all ≤k-marginals. On 294 instances violating (1.1), the same
  construction has a negative atom in 77 — so the check is not vacuous (positivity is the
  only hypothesis-dependent part).
* Minor: the author's own numerics check only ρ on |y|≤k+1 for n≤22; mine enumerate the
  full cube for n≤10 — consistent.

### Theorem 1.3 — SOUND

Re-derived. Given x_s the bits 1[X_b∈Ω_b(x_s)] are independent with marginals p_b(x_s)
(big coordinates independent of each other and of X_s). In the planted case Lemma 1.1 gives
ν_{x_s}; drawing X_b | bit independently from the true conditionals makes (X_b)_{b∈K} have its
true product law for |K|≤k (bits on K: true product law by k-wise agreement; X_K | bits =
product of own conditionals). So E_νφ=Eφ for every φ(x_s,X_K), hence E B=E_νB≤E_νF, and a
planted bit =1 means X_b∈Γ_E for some E∈𝓕 with x_s∈Σ_E, so F=0. ✔
Points the author leaves implicit (MINOR, m1 below): (a) only finitely many b have p_b>0
(primes ≤T), so Lemma 1.1 is applied to a finite bit vector; bits with p_b=0 get w_J=0 and are
never planted; (b) ν≪P with dν/dP≤2 (from e_{k+1−j}(s)≤e_{k+1}(r), the positive extra charge on
1_y is ≤μ(1_y)), so "B≤F P-a.e." suffices and every integrable φ stays ν-integrable;
(c) measurability of x_s↦ν_{x_s} is trivial (Ω_b depends on x_s through a finite modulus).
Note (strength, not a defect): functions in 𝒱_k may read *all* small coordinates; only the
number of big primes in a modulus is constrained. So the barrier holds even for minorants with
arbitrary dependence on primes ≤T^{0.6}.

### Setting 2.0: level ≤D ⇒ 𝒱_k — SOUND

* O9 Thm 1.1's B is a combination of cells 1[n≡b_i (d_i)], Z=Q·max d_i; O13 Thm 5.1's B ≤ F ≤
  1[W>T] on r′H′ with cells of modulus ≤e^{2τ+3𝓛} (O11 Cor 1.2: products A_iA_{i'}u_ju_{j'}).
  On the fibre these are functions of n mod qQ with q≤max d_i, so O14's "level" matches O9's Z. ✔
* A modulus q≤D has fewer than log D/log(T^{0.6}) prime factors >T^{0.6} ⇒ k=⌊log D/(0.6𝓛)⌋. ✔
  Primes >T (incl. ℓ_aux, fixed by the fibre) are harmless: they carry no event (p_b=0).
* Integer vs Haar: ES events force n coprime to M (ℓ|M ⇒ ℓ∤D), B and F are periodic, so the
  integer statement "B(n)≤1[W(n)>T] for n≡r′(Q′), (n,d_i)=1" implies B≤F Haar-a.e. on the
  fibre; and E_{M,D} ⇒ W(n)≤M (D=u²w, A=uvw with u=t, w=κ, D=κt²) so 1[W>T]≤F. ✔

### §1 numerics (2) — SOUND-AFTER-REPAIRS

From-scratch exact-symmetrised LP `scripts/review_o14_toy_lp.py` (S_n-symmetrisation reduces
the k-junta span to polynomials of degree ≤k in |x|; bisection in p). Optimum E B/E F vanishes at
R≈1.11 (n=10,k=1), **1.25** (n=10,k=2), **2.51** (n=12,k=3); also 1.05/1.11/2.28 (n=20,
k=1/2/3), 2.26 (n=30,k=4). The author's "1.1, 1.8, 3.0" are the first grid points (p step 0.05)
with value 0, not thresholds; their grid values agree with mine (e.g. n=10,k=2,R=1.11: 0.258 vs
my 0.277 at R=1.10). Conclusion "(1.1) conservative by a constant factor" stands. Note the
parity effect: even k is barely stronger than k−1 (Bonferroni of odd order).

### Lemma 2.1 — SOUND
v=M/ℓ<T^{0.4}; for fixed ℓ ≤T^{0.4}·T^{0.1}(1+𝓛) (v,D) pairs (HAAR F3), one class mod ℓ each,
so p_ℓ≤T^{0.5}(1+𝓛)/(ℓ−1)≤T^{−0.09} for ℓ>T^{0.6}. Small primes (<T^{0.4}) and big primes
(>T^{0.6}) are disjoint sets — used silently later (Lemma 2.3 conflict structure). ✔

### Lemma 2.2 — SOUND (mod BV, FL)
Checked: vℓ≡−1 (4n), (v,2n)=1 ⇒ M≡3(4), n|A_M, squarefree (ℓ>v); P(E)=1/φ(M)≥1/(vℓ).
BV moduli 4n≤4T^{0.1}≤X^{1/5} for X≥T^{0.6} ✔; bad-q mass ≤𝓛·𝓛²·𝓛^{−A′} ✔; good q:
Σ_blocks (π(2X)−π(X))/(2Xφ(q)) ≈ log(7/6)/(2 log 2·φ(q)) ≥ c_2/φ(q) ✔ (edge block partial —
harmless). Cauchy–Schwarz for bad n ✔ (Σ4^{ω(n)}/φ(n)≪𝓛^4). 1/φ(4n)≥1/(2n) ✔ (both parities).
v-sum ≍𝓛/log y by FL, primes of n>y removed at cost ≤ω(n)/y·𝓛/log y ✔.

### Lemma 2.3 — SOUND
* HAAR Thm 1.4 is stated for arbitrary independent coordinates with atomic events, so the copy
  space (shared X_q, q|v; copies X_ℓ^{(i)} mod ℓ) is a legitimate instance; P(Av(𝓕^{(m)})|x_s)
  =∏_ℓ(1−p_ℓ)^m ✔; mass mμ ✔.
* Conflicts of E^{(i)}: same small q (any copy) or same ℓ in copy i (big ≠ small primes, Lemma 2.1).
  m·(𝓛/log y)·𝓛³/(2y) ≤ 1/(2log y) for m≤y/𝓛^4 ✔; P(E)≤2T^{−0.6} ✔; HAAR Rem 1.4(iii) ⇒ K≤e^{1/3} ✔.
  The "w_ℓ as in Lemma 2.1" is a mis-citation (Lemma 2.1 bounds the *conditional* p_ℓ(x_s), the
  local lemma needs the unconditional Σ_{ℓ(E)=ℓ}P(E)); the latter is ≤T^{0.1}(1+𝓛)(C𝓛/log y)/(ℓ−1)
  ≤T^{−0.49}, so harmless (m5).
* Pair sum: (α) same copy = bit-sharing pairs of 𝓕 (same ℓ ⇒ same residue ⇒ D=D′ as D<ℓ) ⇒ ≤mΔ(𝓕),
  Δ(𝓕)≤C𝓛² by HAAR Lemma 2.4 on the subfamily ✔. (β) cross copies share only primes of g=(v,v′),
  agreement ⇔ g|D−D′; P=1/(φ(g)φ(w)φ(w′)φ(ℓ)φ(ℓ′))≤32/(gww′ℓℓ′) ✔ ((w,w′)=1, (g,ww′)=1).
  Σ(g,n)≤C𝓛/(φ(4n)log y) via BT (q=4n≤t^{1/5}, partial summation ≈(2.5/φ(q))log(5/3)) and Mertens ✔.
  D=D′: Σ_g1/g≤C𝓛/log y, ×(C𝓛/log y)²Σ2^{ω}/φ(4n)² ≪𝓛³logN_0/(N_0 log³y)≪𝓛 ✔ — this case
  includes the diagonal E=E′ in different copies (w=w′=1), which must be counted; it is. D≠D′:
  F5 (ω(m)≤𝓛, y≥𝓛) ⇒ ≪𝓛^7/(y log²y)≪𝓛² ✔. Copy pairs ≤m² ✔. C_5 absolute ✔ (y≥𝓛^5 only helps).

### Theorem 2.4 — SOUND
Chain re-derived: E B≤E[F1{R<K′}]≤E[e^{−P}1{P<K′}] (R≥P, E[F|x_s]≤∏(1−p_ℓ)) ≤e^{θK′}E e^{−(1+θ)P},
1+θ=m(1+p*), e^{−m(1+p*)P}≤∏(1−p_ℓ)^m (log(1−p)≥−p(1+p), p≤1/2) ✔; K′≤(k+1)(1+4p*) (r*≤2p*) ✔;
m(1+p*)K′≤mμ/2 ✔; total exp(−mμ/2+mμ/8)=exp(−3mμ/8) ✔. With O13's Y=𝓛^{C_0+4}, C_0≈48.5,
y=Y: μ≫𝓛³/log𝓛, m≍𝓛/log𝓛 (binding constraint μ/(8C_5𝓛²)) ⇒ exp(−c′𝓛^4/(log𝓛)²) ✔.
O13 Thm 3.4's Q is Y-smooth (only ℓ≤Y eligible, 840|Q), ℓ_aux>T ⇒ Setting 2.0 applies ✔.
Contradiction with the transfer's need: O13 I1(a) gives δ=E_{rH}F≥exp(−(4/3)S_res) with
S_res≪𝓛³log𝓛, and BRW needs E B≥0.99δ; exp(−c′𝓛^4/(log𝓛)²) < 0.99δ for large 𝓛 ✔.

### Corollary 2.5 — SOUND-AFTER-REPAIRS
Implication correct; "optimal up to (log𝓛)²" ✔ (𝓛^4log𝓛 vs 𝓛^4/log𝓛). Wording (m3): "Selberg-type
quadratic minorants, β-sieve/Bonferroni truncations … all need level ≫𝓛^4/log𝓛" is true only when
they are required to be dense (E B ≥ δe^{−𝓛^{3.9}}); in O9 Thm 1.1 any of them could in principle be
used sparsely (Prop 2.7's loophole). The closing qualifier covers this, but the "In particular" list
should carry it too.

### Theorem 2.6 — SOUND
𝓕_Q inherits all upper bounds; lost mass ≤(𝓛^5/(6log𝓛))·𝓛³/(2𝓛^6)+negl. ≪𝓛²/log𝓛 ≪μ/2 ✔;
m≤y/𝓛^4=𝓛² not binding ✔. Primes of Q in (T^{0.4},T^{0.6}] carry no 𝓕 event ✔. MINOR (m4): the
bound is absolute, so it obstructs dense minorants only on fibres with log(1/δ_fibre) ≤
c″𝓛^4/(log𝓛)²; §0's "every dense minorant … share ≥exp(−𝓛^{3.9})" silently assumes such a fibre
(true for O13's, by I1(a)). State it.

### Prop 2.7 and scope — SOUND; labels honest
E_νB=E_ν[B1_{G^c}]+E[B1_G], ν(all bits 0 | x_s∈G^c)=0 ⇒ first term ≤0 ✔; P(G) bound same arithmetic ✔.
The sparse-minorant loophole is real and correctly stated: O9 Thm 1.1's cost (1+log A)log Z is
invariant under B↦εB, and even a *nonnegative* B (A=1) is not excluded — a nonnegative level-D
B≤F with tiny mean would beat 1/4. The "1/4 ceiling" is labelled Assessment and O49b open. ✔
Nothing in §4/§0 claims more than dense minorants, apart from m3/m4 wording.

### Corollary 3.1 — SOUND
O13 I1(a): EL_mod(τ) ⇒ E[F−B]≤e^{−3S_res}/100≤δ/100 ⇒ E B≥0.99δ, cells ≤e^{2τ+3𝓛}; Thm 2.4 forbids
for 2τ+3𝓛≤c𝓛^4/log𝓛 ✔. Tail form: 2^{−τ/ρ}≤e^{−3S}/(100m²(S+1)) at τ≍ρ(S_res+𝓛) (m≤T²) ✔;
ρ≤c𝓛/(log𝓛)² gives τ≪c𝓛^4/log𝓛 ✔. "ρ" here is O11's ρ𝓛 (=2𝓛), consistent. The claim is about the
*true* energy tail measured in log-modulus, hence method-independent ✔.

## Defects

No FATAL or MAJOR defects found.

* **m1 (MINOR, Thm 1.3 proof).** Add: finitely many b with p_b>0 (others never planted);
  dν/dP≤2, so B≤F a.e. suffices and integrability is preserved. Repair: one sentence.
* **m2 (MINOR, §2 Numerics (2)).** "vanishes already at R≈1.1/1.8/3.0" are grid points; actual
  thresholds 1.11/1.25/2.51 (n=10,10,12; `scripts/review_o14_toy_lp.py`). Repair: rephrase or bisect.
* **m3 (MINOR, Cor 2.5 'In particular' list).** Selberg/β-sieve/Bonferroni are blocked only when
  used as dense minorants. Repair: insert "used as dense minorants (share ≥e^{−𝓛^{3.9}})".
* **m4 (MINOR, §0, Thm 2.6).** Dense-minorant obstruction requires log(1/δ_fibre)≤c″𝓛^4/(log𝓛)²
  (true for O13's fibre by I1(a)); state it in §0 and after Thm 2.6.
* **m5 (MINOR, Lemma 2.3 local lemma).** "w_ℓ as in Lemma 2.1" — Lemma 2.1 bounds the conditional
  p_ℓ(x_s); the unconditional w_ℓ=Σ_{ℓ(E)=ℓ}P(E)≤T^{−0.49} needs its own line. Repair: add it.

## Overall verdict
SOUND-AFTER-MINOR-REPAIRS. Lemma 1.1 verified exactly (115 instances incl. equality cases, full
cube enumeration); Thm 1.3 and the conductor→k-big-coordinates reduction are correct; Lemma 2.3's
copy argument correctly instantiates HAAR Thm 1.4; Thm 2.4's constants close and contradict BRW's
E B≥0.99δ on O13's fibre. Labels are honest: only dense minorants are excluded; the sparse case
(O49b) and the "1/4 ceiling" are correctly left open / Assessment.

