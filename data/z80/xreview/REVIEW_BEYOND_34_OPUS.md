# Hostile cross-lab review — `notes/z80/BEYOND_34.md` (commit 850a05506)

Reviewer: Claude Opus (Anthropic). Author: GPT-6.2 Astra lane. Scope: every change in `git log main..`
(`notes/z80/BEYOND_34.md`, `scripts/z80_beyond34.py`, `data/z80/beyond34.txt`). Sources checked: the untracked
`data/z80/lit/{hit,tz,stark*,}_scratch.txt` (Paredes–Sasyk arXiv:2202.10420v2; Thorner–Zaman arXiv:1803.02823v3;
Cho–Lemke Oliver–Zaman arXiv:2510.02309 **v2** (the note cites v1), which quotes Stark 1974 Lemma 8; Zykin's reprint of
Stark's Lemmas). The Stark 1974 scan in the scratch files is unreadable, so I checked Lemma 8 only through CLOZ's
literal use of it. Compared against `notes/z79/WILD_ES.md` (§§1–3, 6, 10), `notes/z78/ANALYTIC_WILD.md` (§§2–4, 9, 15),
`notes/z75/ANALYTIC_BREAK.md` §1, STATUS §1A/§1B and FRONTIER (the line near 1707 and the e* row).
Replay: `scripts/z80_beyond34.py` reproduced `data/z80/beyond34.txt` exactly (0.4 s). I also ran one independent
numerical spot check (below). No master files were edited and nothing was committed.

## Outcome

**ACCEPT both new results in substance, with required form/scope fixes (none mathematical-fatal).**

* **Theorem C (3/4 tail for every nonconstant fixed-degree polynomial): ACCEPT.** I re-derived every step and found
  no gap. The fixes needed are about labels and naming, plus one statement on effectivity.
* **Theorem B (Dirichlet-GRH cap coefficient 2√2 → 2): ACCEPT.** The exponent arithmetic, the packet identity, the
  mod-b synchronisation, the deletion and the diameter are all correct. One scope reconciliation is **required**: the
  result goes *below* the z78 §2 "optimistic certificate floor" (2 in u-units, i.e. 2√2 in t-units), which FRONTIER
  §6 lists as an "adaptive-window entropy floor". This is not a contradiction, because the window qb and the group
  order q are decoupled. But the note never says so, and at export the FRONTIER line has to be re-scoped.

Neither result touches ES, the unrestricted 3/4 exponent, or cap zero. The note says so correctly.

## 1. Theorem C: step-by-step audit

**Lemma 1 (Lüroth + effective HIT). Correct.**
* Generic calculation. T = −vF(Y). Infinity of Q(Y) is the only place above T = ∞ and it is totally ramified, so any
  intermediate Q(Z) has exactly one place above ∞, and that place is rational. After a Möbius change of variable,
  Z = G₁(Y) and T = P(Z) are both polynomials. Q(Z)/Q(T) Galois means its automorphisms fix ∞, so they are affine.
  A finite subgroup of Aff(Q) embeds into {±1}, so deg P ≤ 2. Completing the square gives F = aG² + b. This is
  correct. The intermediate field lies inside Q(Y), so constant-field extensions in the Galois closure are irrelevant.
  For F = Y³ the closure contains ζ₃, but Q(∛·) still has no abelian subfield. The note's "does not assert regularity
  of the normal closure" is the right caveat.
* PS Thm 1.3, checked literally. E_{F,K}(B) = #{t ∈ [B] : G_t ≠ G} ≲_{K,d_T,d_Y} (log H + 1)^{[6,10]} B^{1/2}. The
  non-monic case holds for the second inequality. **Form:** `[6,10]` is the paper's char-0/char-p notation, so the
  exponent over ℚ is **6**, not 10. Quoting 10 is harmless (it is an overestimate) but it is a misreading. With U = h^{1.1e}
  the count is h^{.55e+o(1)} ≤ h^{.56e}. ✓
* Specialisation. Away from branch values and with |G_t| = |G|, the decomposition group equals G and acts compatibly on
  the roots. So the maximal abelian subfield of K corresponds to G_α[G,G] on both sides. ✓

**Lemma 2 (disjointness). Correct.**
* Square class: (−u/v − B/C)/a ≡ −aCv(Cu+Bv). ✓ A prime p | Cu+Bv with p ∤ 2aBC is prime to u and v (by coprimality),
  hence to q (q = 4uv, or 16w with v = 1). Such a prime does not cancel against v either, because p | v and p | Cu+Bv
  would force p | C. The deletion count is h^{o(1)} squarefree parts × h^{.555e} square multiples, so O(h^{.58e}). ✓
* K ∩ M, for M = Q(ζ_q)E_* abelian, is abelian Galois over Q and lies in K, so it is Q or K₀. K₀ is ramified at a prime
  outside qD_*, so it equals Q. Then [KM:K] = [M:Q] = 2φ(q), since p_* ∤ q gives E_* ⊄ Q(ζ_q), and hence
  E_* ⊄ K(ζ_q). ✓
* p_* → ∞: the odd part of a real primitive conductor is squarefree, so if p_* stays bounded then D_* stays bounded,
  and any fixed real character's zeros stay away from 1. ✓ This step, together with Landau–Page, is *effective in
  principle but not explicit*. **Fix:** state "no effective onset asserted", as z79 §3 does.
* Numerical spot check (mine, `/tmp`, not committed). F = Y⁴+Y², u = 7, v = 1: the radicand class is −3, so
  K₀ = Q(√−3). At q = 28 = 4uv every reduced class mod 28 has a positive proportion (0.22–0.52) of primes ℓ < 2·10⁴
  at which vF+u has a root. The control at q = 12 (where K₀ ⊂ Q(ζ₁₂)) has the classes 5 and 11 identically 0. This
  confirms why the fresh ramified prime has to avoid q, and that it automatically does.

**Lemma 3 (TZ Thm 1.4 + Stark). Correct.**
* TZ Thm 1.4, checked literally. L/F Galois, H ⊆ G abelian with C ∩ H ≠ ∅, K = L^H, x ≥ (D_K Q n_K^{n_K})^{c₂}, and
  π_C = |C|/|G|·(Li x − θ₁ Li x^{β₁})(1 + O(e^{−c₃ log x/log Z} + e^{−(c₃ log x/n_K)^{1/2}})), with c₂, c₃ absolute.
  The note applies it with base = K, H = G = (Z/q)^* (valid by (1)) and C = {σ_s}. ✓ Q ≤ q^d holds because every
  character is χ∘N. ✓ Z ≤ h^{C′e}. ✓ The relative error e^{−c₃/(C′e)} is a small constant once e is small. ✓
* Exceptional zero. If β > 1 − η/log h, then β is a zero of ζ_E with E = K or E = K(√χ₁) ⊆ L, [E:Q] ≤ 2d and
  log D_E ≪ e log h. Stark's Lemma 8 holds with threshold 1/(4[E:Q]! log D_E); CLOZ use it in exactly this form, for an
  arbitrary F with no normality assumption. Once e ≤ 1/(4(2d)!ηC), it gives a quadratic k ⊆ E with |D_k| ≤ |D_E| < h
  and ζ_k(β) = 0. So k = E_* ⊆ L, which contradicts (1). ✓ When 1 − β ≥ η/log h, t^{β−1} ≤ e^{−η} on (h,2h], which
  gives the (1 − e^{−η}) lower bound. θ₁ = −1 only helps. ✓
* Degree ≥ 2 ideals cost O(d√h), which is far below h^{1−1.6e}/log h. Degree-1 ideals outside the index give roots,
  and their Frobenius is ℓ mod q. ✓ The result is a genuine per-class lower bound, uniform in (u,v). That is stronger
  than z79's BV + twist-pruning route, and **BV and the Montgomery density theorem are no longer needed** for C.

**§4 transfer. Correct, given z79.**
* Masses. Per block, Σ1/q ≍ t²h(k) (ratio) or t h(k) (word). Multiplying by 1/log h and summing over ≍ t blocks gives
  t^r h(k), the same normalisation as z79 (2). ✓
* The p_* | uv losses are a relative O(1/p_*). ✓ When p_* | k the case is vacuous, since u ≡ −c₀v is a unit mod p_*. ✓
* The Lemma 1–2 deletions cost K₁h^{−.4e}t, which is o(1). That is negligible even per k, since t²/k² ≥ t²h^{−e/250}. ✓
* Disjointness at one pivot: ℓ | uv′ − u′v is impossible, and q > K₁ pins k. ✓ At most d roots per ℓ, because ℓ ∤ va. ✓
* Repair / scaling / Taylor transfer: identical to z79 §3, with the three m values and the three t scalings. ✓
* Coefficient ceiling. ‖F‖ ≤ h^{e/C_d} for every h ≥ √X and the Lemma 2 height condition both follow from
  b_d ≤ αe/(2C_d·O_d(1)). ✓ Either leading sign is fine: with a negative leading coefficient the positive values lie in
  a window of length exp(O(b(log H)^{1/4})). ✓ Values of arbitrary size are fine, since nothing uses |F(j)| beyond
  discarding tiny values. ✓

**Scalar × square induction. Correct.**
* F = cG₀² with c = cont(F) a positive integer (Gauss). Any failure at F(j) > 0 is a failure at |G₀(j)|, by scaling by
  c|G₀(j)|. Degree halves. ‖G₀‖ ≤ (2+‖F‖)^{O_d(1)} (Mahler measure gives this too). So shrinking b_d finitely many
  times is enough. ✓
* The Δ = 0 quadratics excluded in z79 A are now covered, since 4A·F = (2Aj+B)². ✓
* Scoping the word tails *away* from cG₀² is necessary, not merely conservative: z79 Thm C shows that 8 | xy has **no**
  solution at 2j². ✓
* **Form:** the "proposed Jordan shortcut" paragraph answers a proposal that is not in the note. Delete it, or state
  the shortcut being refuted.

**Coverage relative to the current masters.** C subsumes z79 Thm A (now including Δ = 0 by scaling), the full-ES part of
Thm D (including even h with b = 0), and §10 CUB3. It extends the z79 Thm B word tails to all F that are not of the
form c·G². It is the quantitative form of `Z60_MS105.md` Thm 3 for full ES at all degrees. External priority is
unverified; the KRK caveat on 3/4 is inherited.

## 2. Theorem B: step-by-step audit

**Lemma 5 (BV friable cofactors). Correct.**
* Ψ(Y, √s) has a positive proportion at the fixed ratio 2θA. ✓ Smooth d′ ∤ L₀ need p^j > z with j ≥ 2, which costs
  ≤ 2π(z)/z. ✓
* BV at level 48y^θ with θ < 1/2. ✓ Each main term is ≫ y/(Y log y). There are ≤ 2y/Y values of t₀, so by pigeonhole
  some t₀ carries ≫ Y/log y distinct primes, chosen before any halving. ✓
* v₂(r−1) = 2 and d′ is odd, so (r−1)/4 divides L_o. ✓ log L = O(√s + log y) = o(s). ✓
* (2y)^m < D gives distinct units. ✓ log C(P,m) ≥ m log(P/m) ≈ (s/(A log s))(θA−1) log s = (θ − 1/A)s > ηs. ✓

**Lemma 6 (simultaneous packet). Correct.** I verified each identity by hand.
* qb ≡ 3 (8) with b ≡ 5^m (8) gives q ≡ 3 (4) and makes K′ odd. ✓ S | K′. ✓ K′ is coprime to qbR, because the primes
  of R are 1 (8), those of b are 5 (8), and q ≡ 3 (4). ✓
* K′ ≡ R/4 (mod r), and g ≡ 3^{2δ}·K′/w⁴. Hence g^{(r−1)/4} = (R/4)^{(r−1)/4}(3/r)^δ = −1, using (3/r) = −1 at
  r ≡ 5 (24). Since (r−1)/4 divides the odd number L_o, g^{L_o} ≡ −1 (mod r). ✓
* (g/q) = (K′/q) = (R/q) = (q/R) = −1, by Jacobi reciprocity with R ≡ 1 (4). ✓ So −g^{L_o} ∈ U, |U| is odd, and
  (−g^{L_o})^{−j} ∈ H₁. ✓
* d₁ ≡ −K′ holds modulo q (j odd) and modulo each r | b (v^{2L} ≡ 1 since r−1 | L, and g^{L_o j} ≡ −1). ✓
* 4/R identity: RA₀ + K′ + d₁ = A₀(R+qb) = 4K′A₀. ✓ Overflow is (w−2c)^+ with w − 2c = L_o j v_p(g) + 2La_p − c,
  which is even because v_p(g) ≡ c (mod 2), including the 3^{2δ} correction. Overflow primes divide y₁. The denominator
  is prime to R, so scaling by n/R is safe. ✓
* Planted branch ((R/r) = −1 for some r ∈ 𝒫). (r/q′) = (q′/r) = (−R/r) = (R/r) = −1, and r ∥ K. This is z75 §1, and
  its log-cap is O(log s). ✓
* The half-selection by quartic sign is covered by "any half" in Lemma 5. ✓

**§7 count, deletion, diameter. Correct.**
* Distinct b mod D/8 (at a factor-8 loss) give disjoint q-classes mod D. ✓ Under GRH, each class with (q/R) = −1 has
  ≫ X/(D log X) primes. The error √X log(RD) is smaller than X/D by a factor D(1+t)⁵. ✓ χ_R is primitive and
  nontrivial, and (R, D) = 1. ✓ So M ≫ XD^{η−1}/log X. ✓
* Relations among v^{2L}: there are (3B₀)^k vectors, each with log height ≤ 2LB₀ log D. The choice of B₀ leaves a
  survivor, and log B₀ ~ u/(k+1) → ∞. ✓
* Box injection gives j ≤ X/B₀^k. ✓ Minkowski II for the unit sup cube gives λ_k ≤ |H₁|/B₀^{k−1}, and the
  shift-then-round step gives 0 ≤ a_v ≤ 2⌈kX/B₀^{k−1}⌉. ✓
* log cap ≤ 2u/(k+1) + (1−η)·((k−1)/(k+1))·log D + O(k + log u + log L). With k = b√(u/log u) the normalised cost is
  2/b + (1−η)b/2, minimised at b = 2/√(1−η) with value 2√(1−η) in √(u log u) units. Since u ~ 2t, this is 2√2·√(1−η)
  in √(t log t) units, which tends to **2** as η ↑ 1/2 (limsup first, then η). ✓ This reproduces the old 2√2 at η = 0.
  The replay script confirms the packet algebra, not the asymptotics. The note says so. ✓

**Required reconciliation (substantive scope).**
* z78 §2 proves that the optimistic certificate, with window height = diameter height X and integer windows q ≤ X with
  k primes of K = (R+q)/4, has floor (2−o(1))√(u log u). That is 2√2 in t-units, and Theorem B gets below it.
* The escape is that the window is qb ≤ XD while the cyclic group is F_q^* of order ≤ X. So the supply loss
  log(X/M) ≈ (1−η)log D is paid against the group order, not against the window height. At window height X′ = XD the
  z78 supply bound is not violated: log(X′/M) ≈ (2−η)log D ≥ k log k.
* **Fix:** add one sentence to §§7/9 saying this. At export, re-scope FRONTIER §6 (z78 line, "adaptive-window entropy
  floor") to "prime windows whose cyclic group order equals the window height". Otherwise a reader of the masters sees
  a proved floor contradicted by a proved theorem.
* z78 §3's 2√2 square-divisibility floor is unaffected: it is a different certificate.

**Other checks.**
* The GRH-free parts (Lemmas 5, 6) are unconditional. The §0 label "CONDITIONAL … (§§5–7)" should be
  "CONDITIONAL on Dirichlet GRH (§7 prime supply only); Lemmas 5–6 PROVED rel. BV, Dickman, Linnik".
* BV level 1/2 is the only reason η < 1/2. The "next test" (D^{1−o(1)} unit residues) would indeed push the
  coefficient to 0, i.e. o(√(t log t)). That is correctly labelled as open.
* The §8 "Assessment (A)" Rankin argument (prime bound x^{1−δ} ⇒ integer bound N^{1−δ′}) is correct, since a failure
  has only failing prime factors. Its QR-bias sentence matches `EXSET_CHAR_FORCING.md` Prop 5.1′ (X^{1/A+o(1)}). ✓

## 3. Results legitimately covered

1. **PROVED** (rel. Paredes–Sasyk Thm 1.3, Thorner–Zaman Thm 1.4, Stark 1974 Lemma 8, Landau–Page, Lüroth, BT,
   Mertens, Vaughan's exceptional set, and the *internal, unrefereed* TQ/AP2 lattice and incidence estimates via
   z79 §§1–3):
   * For fixed d, uniformly over every nonconstant F ∈ ℤ[Y] with deg ≤ d and ‖F‖ ≤ exp(b_d(log H)^{1/4}), and over
     every interval of H consecutive parameters, #{j : F(j) > 0 and ES fails} ≪_d H exp(−c_d(log H)^{3/4}). The
     same holds for the union over the box.
   * For F not of the form c·G² (c ∈ ℚ), z79-B type word tails hold at V = (log H)^{2/3}/(log log H)^{1/3}, and at
     (log H)^{2/3} for prime values.
   * No effective onset.
2. **CONDITIONAL on Dirichlet GRH** (plus BV, Dickman, Linnik, Minkowski II): log(1 + e*(n)) ≤ (2+o(1))·√(log₂R·log₃R)
   for the capped relaxation. This is the method's constant, not a lower bound, and has no cap-zero consequence.
3. **CERTIFIED (finite):** 8266 packets, of which 2802 have composite b and 18 have exact rationals. Replayed.

## 4. Required fixes before promotion

1. **(Required, scope.)** Add the z78 §2 reconciliation (decoupled window/group height) and propose the FRONTIER §6
   re-scoping in §0's STATUS/FRONTIER delta.
2. **(Required, label.)**
   * §0 for C must name the internal unrefereed TQ/AP2 inputs. "Named unconditional inputs" reads as if everything
     were external.
   * Split B's label: Lemmas 5–6 PROVED; §7 CONDITIONAL on GRH.
   * Add "no effective onset" (p_* → ∞ and Landau–Page).
3. **(Required, naming.)** "Theorem B" and "Theorem C" collide with z79 Theorems B and C, and the note itself cites
   "Z79 Theorem B" inside Theorem C. Rename them (e.g. Theorem P for the pullback, Theorem Q for the cap) before any
   master file quotes them.
4. (Minor)
   * The PS height exponent over ℚ is 6. `[6,10]` is the char-0/char-p notation.
   * Cite the CLOZ version actually consulted (v2 in the scratch file).
   * Delete or explain the "Jordan shortcut" paragraph.
   * The heading "Detect the prime in the root field, not its permutation sign" is cryptic; replace it with a
     descriptive title.
5. (Export) The STATUS §1A delta should *replace* the z79 sub-bullet (quadratics, cubics, binomials), not add a row. It
   must keep "parameters with F(j) > 0", the coefficient ceiling, "word tails exclude c·G²", and "external priority
   unverified". The §1B change is just 2√2 → 2, with "cross-review owed" until a second review. Note that a claimed
   improvement of an internal record needs only one cross-lab review under AGENTS §3. It is not a published record.

## 5. Debate / challenge notes (non-blocking)

* *Could a non-square F kill all atoms on a positive proportion?* Only through a quadratic subfield K₀ ⊂ Q(ζ_q)E_*, and
  Lemma 2's fresh ramified prime rules that out. My q = 12 control shows what fails when it is not ruled out. Square
  values of aG²+b (Pell families) are thin and covered by the exceptional count.
* *Is TZ really uniform here?* Yes. c₂ and c₃ are absolute, n_K ≤ d, and the only F-dependence is through Z ≤ h^{C′e}.
  The novelty, compared with z79's route, is the per-class Linnik-range Chebotarev over the root field. That is what
  makes "all polynomials" possible without any Artin input.
* *Is the GRH gain "real" or certificate bookkeeping?* It is a genuine new certificate, a composite window with
  synchronised CRT signs, valid at every R. It is not an average over R or over classes, so the z78 §15 obstruction
  does not apply. It still leaves the √(t log t) order untouched.
