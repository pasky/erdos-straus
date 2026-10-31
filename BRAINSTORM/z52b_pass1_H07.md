# z52b pass 1 — batch H07 (16 items, Z2435–Z2882)

**Summary.** 16 items: covered 9, nothing 5, skipped 1, interesting 1, needs-compute 0.
**Interesting: Z2882** — the BM correction is a class-number square: T(p) = ¼·E(χ_p)·L(1,χ_p)² + o(1) (EVIDENCE: max error 0.07
over 40 random primes 10⁴–10⁶ with T ∈ [−3.33, 5.64]; proof sketch via hyperbola + Burgess). If made rigorous it gives M_BM(p) ≥ (21/(16π²) − o(1))(log p)²
(≈ 0.133 L², vs 0.019 L² in BM_CORRECTED_COUNT Thm 2.2), and under GRH M_BM = M₀ − O((log log p)²).
Nothing-with-data: Z2461 (energy Σ R² ≍ N log⁴N, at the Cauchy–Schwarz floor), Z2582 (smooth-C fractions), Z2771 (restricted-class ES ≤ 3·10⁵).
Outcomes: `data/z52b/pass1/outcome_H07.jsonl`; scripts `scripts/z52b_p1_H07_*`; data `data/z52b/pass1/H07/`.

ES is OPEN. Nothing here proves ES or any infinite case of it.

---

## Z2882 — the BM correction T(p) is ¼·E(χ)·L(1,χ)² (EVIDENCE + proof sketch; not reviewed)

**Setting** (`BM_CORRECTED_COUNT.md` Prop 2.1(d), Thm 2.2, Prop 2.3). For p ≡ 1 (mod 4), χ = (·/p) (even, so (−uB/p) = χ(uB)):
M_BM(p) = M₀(p) − T(p), T(p) = Σ_{(u,B) ∈ 𝒫(p)} χ(uB)/φ(4uB), with 𝒫(p) = {gcd(u,B) = 1, u + B odd, 4uB − u − B ≤ p}.
The repo bounds T only through g(p) = sup_t |Σ_{k≤t} χ(k)/k|: unconditionally |T| ≤ C·L² ("C not small"), under GRH T = o(L²);
Thm 2.2 then gets M_BM ≥ (3/(16π²) − o(1))L² ≈ 0.019 L² from a positive subfamily.

**Observation (EVIDENCE).** With
  E(χ) := 2χ(2)(1 − χ(2)/2) · ∏_{ℓ odd, ℓ ≠ p} [ (1 − χ(ℓ)/ℓ)² + 2χ(ℓ)(1 − χ(ℓ)/ℓ)/(ℓ − 1) ],
we have **T(p) ≈ ¼·E(χ)·L(1,χ)²**. Data (`scripts/z52b_p1_H07_Tp.c`; L(1,χ) computed exactly from
L(1,χ) = −p^{−1/2} Σ_{a<p} χ(a) log(2 sin(πa/p)); Euler product truncated at 2·10⁵):
* 40 random primes p ≡ 1 (4) in [10⁴, 10⁶] (`data/z52b/pass1/H07/Tp_random40.txt`): T ranges −3.33 … +5.64;
  max |T − pred| = 0.072, mean 0.013.
* The 9 (★)-failure primes ≤ 10⁶ (`Tp_selected.txt`): T − pred = 0.49, 0.27, 0.36, 0.31, 0.13, 0.16, 0.17, 0.015, 0.093 for
  p = 409 … 712321 (error decreasing with p); near 10⁶ and 2·10⁶ the error is ≤ 0.04.
* Sign law: E₂ = 2χ(2)(1 − χ(2)/2) is +1 for p ≡ 1 (8) and −3 for p ≡ 5 (8). So for p ≡ 5 (8), T < 0 and M_BM > M₀
  (observed: all 22 random p ≡ 5 (8) have T ∈ [−3.33, −0.02]); the deficit M₀ − M_BM lives only at p ≡ 1 (8).

**Proof sketch (not checked by a reviewer; this is the depth-lane task).**
1. Bulk uB ≤ p/4: by BM_CORRECTED Prop 2.1(e), T_bulk = ¼ Σ_{m ≤ p/4, 2|m} χ(m)2^{ω(m)}/φ(m) = ¼ Σ_{m≤x} χ(m) f(m)/m with
   f(m) = 1[2|m]·2^{ω(m)}·m/φ(m). Its Dirichlet series is L(s,χ)²·H(s,χ), H = Σ h(d)χ(d)d^{−s} absolutely convergent near
   s = 1 (h(ℓ) = 2/(ℓ − 1) at odd ℓ), with H(1,χ) = E(χ) (local factors computed above).
2. Write the partial sum as Σ_d h(d)χ(d)/d · Σ_{ab ≤ x/d} χ(ab)/(ab); truncate d ≤ p^ε (tail ≪ p^{−ε+o(1)}·L²). For y = x/d ≥ p^{1−2ε},
   the hyperbola method gives Σ_{ab≤y} χ(a)χ(b)/(ab) = 2G(√y)L(1,χ) − G(√y)² + O(p^{−η}L) = L(1,χ)² + O(p^{−η}L), using
   G(t) := Σ_{k≤t} χ(k)/k = L(1,χ) + O(p^{−η}) for t ≥ p^{1/4+ε} (Burgess, as in Thm 2.2's proof; beyond p use periodicity).
3. Boundary p/4 < uB ≤ (p + u + B)/4: for u ≤ p^{3/8−ε} the B-interval has length ≍ p/(16u²) ≥ p^{1/4+2ε}, so Burgess
   (after Möbius for gcd(B, u) = 1 and the 1/φ(B) weight, as in Prop 2.3's proof) makes it O(p^{−η}); u > p^{3/8−ε}
   contributes ≪ Σ_{u > p^{3/8−ε}} u^{−2} = o(1).
Hence (claim) **T(p) = ¼·E(χ_p)·L(1,χ_p)² + o(1)**, i.e. by the class-number formula
T(p) = E(χ_p)·(h(p) log ε_p)²/p + o(1).

**Consequences, if the sketch holds.**
* Unconditional: L(1,χ) ≤ g(p) ≤ (¼ + ε)L (Burgess, BM_CORRECTED Thm 2.2 proof) and E(χ) ≤ ∏_{ℓ odd}(1 + ℓ^{−2}) = 12/π²
  (attained only in the limit χ(ℓ) = 1 for all small ℓ; E ≤ 0 when χ(2) = −1), so T(p) ≤ (3/(16π²) + o(1))L², and
  **M_BM(p) ≥ (3/(2π²) − 3/(16π²) − o(1))L² = (21/(16π²) − o(1))L² ≈ 0.133 L²**. This is 7× Thm 2.2's 0.019 L² and close to the
  empirical minimum (0.062 L² for p ≤ 10⁶, where L(1,χ) is still small relative to the O(L) terms).
* GRH: L(1,χ) ≤ (2e^γ + o(1)) log log p (Littlewood) gives T = O((log log p)²), so M_BM = M₀ − O((log log p)²), much sharper than Prop 2.3's o(L²).
* Structure: the BM deficit at p is exactly a class-number quantity, (h(p) log ε_p)²/p times an Euler product. It is large
  precisely when p is a QR mod 2 and many small primes, i.e. at Mordell-hard p. (The (★)-failure primes have L(1,χ) = 2.3–5.1,
  well above the typical size; EVIDENCE only, and partly forced by the Mordell classes.)

**Why it matters for ES / what it does not do.** It sharpens the *main-term side* of H⁻_BM (FRONTIER §2.4) to
M_BM = M₀ − ¼E·L(1,χ)², and identifies the p-dependence of the main term as one L-value. It does **not** touch the lower-tail
problem (B2/B3: one integer, polylog main term); H⁻_BM stays open.

**Next step (depth lane).** (1) Write the proof rigorously, especially the error terms in steps 2–3, and decide whether
"T(p) = ¼E L(1,χ)² + O(p^{−η}L)" or only "+ o(L)" is provable. Then update BM_CORRECTED_COUNT Thm 2.2 and FRONTIER §2.2 after a review.
(2) Check numerically whether R(p) − M₀(p) regresses on −¼E·L(1,χ)² beyond what the genus layer already explains (SINGLE_P_COUNT
variance table), i.e. whether the class-number term predicts (★)-hardness.
Related TODO items with the same guess (now tested): Z1809, and the T(p)/L(1,·) items listed near ES_CONNECTIONS_TODO.md:613, 4796, 5099.

Reproduce: `gcc -O2 -o Tp scripts/z52b_p1_H07_Tp.c -lm && ./Tp <primes ≡ 1 mod 4 …> <max p>` (the last argument is the sieve bound;
about 1 s per prime at 10⁶).
