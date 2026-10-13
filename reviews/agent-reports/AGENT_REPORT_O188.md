# AGENT_REPORT O188 — spark relay M: steering by sterile Mordell points (checkpoint 1)

(R188 review `reviews/sterile-steer-review.md`: no FATAL; MAJOR framing defects D3, D9 and minors repaired by the
reviewer in STERILE_STEER.md, the bsM memos and this report, marked "(R188 repair)".)

Main file: `STERILE_STEER.md` (§§0–6). Memos: `BRAINSTORM/bsM_boundary_escape.md`, `bsM_borel_cantelli_patterns.md`,
`bsM_shot_coverage.md` (indexed in BRAINSTORM/README.md). Scripts: `scripts/ss_escape.py`, `scripts/ss_sqclass.py`.
Branch merged first: side-agent/spark-depth-aspect (README conflict resolved by keeping both sections).
**ES is not solved; no infinite case of ES is claimed.** All new statements depend on O178 (CLAIMED, under R178/R187)
only where marked.

## SHARP:
1. **Borel–Cantelli dichotomy for non-square patterns (§3).** The sterile set S (complement of all ET classes) is a
   closed subset of Ẑ, and ES(p) ⟺ p ∉ S. SQ ⟺ S ∩ ℕ_odd = odd squares (Prop 3.1, PROVED rel. ET Props 2.2/2.6; R188 repair of the citation).
   On the T-generic non-square set G_T (1 off T, non-square on T) with product measure ν_T: if Σ_{q∈T, q≡3(4)} 1/q = ∞
   then ν_T-a.e. point is covered, already by the Mordell classes {n ≡ −4 (mod q)} (Prop 3.2, PROVED, second
   Borel–Cantelli). For T = {r}, r ≥ r₀, sterile points have positive measure (O178). Every non-square integer
   (in particular every prime) has a divergent pattern. Integers lie in no slice G_T, so measure and pattern
   arguments on G_T say "almost all covered" and nothing about the point (R188 repair: previously "So ES lives at
   ν-null points on the divergent side"; the dichotomy is proved only on the slices G_T). The sparse-T extension of O178
   is only sketched (Assessment): it needs a multi-prime box dictionary (mixed I2/I3/II3 splits), which has not been written.
2. **Sterile points are a profinite symptom of "finitely many shots per prime" (§5; R188 repair of "the signature").** Per-prime level-1 coverage on the
   q-generic line: ET classes cover ≪ q^{−2/5+o(1)} (PROVED rel. ET + MORDELL17 lemmas for general r); O183's V_φ
   unit shots cover 1/i_𝔮 of the non-squares (PROVED), and i_𝔮 = 1 for a positive proportion of 𝔮 under GRH. A
   ℤ-mechanism with infinitely many shots would need ≫ 1 coverage per prime, and ET classes cannot give it (at a given q only
   the τ₃((q+1)/4) shots with 4ad | q + 1 are usable; Mordell's p + 4 is the unique shot usable at every q ≡ 3 (mod 4);
   R188 repair of "unique bounded-modulus shot"). This makes O183 spark S4 precise.

## What was done (by goal)
* (1) Escape lemma (§1, PROVED): near x(u), every class of p has r-level > L or a prime power q^v ∥ M with
  q^v ∤ p − 1. The brief's routes (a) "moduli → ∞" and (b) "other primes not ≡ 1" coincide (H-A). Numerics (§2,
  EVIDENCE; r = 17, u = 5, B = 23/47/97, 4 × 30 primes per B, all classes of modulus ≤ 10⁵, witnesses re-solved):
  primes near the sterile point and primes near the square point 1 behave **identically**. In all 180 cases (≈ 150 distinct primes;
  reproduced independently by R188) they escape at a single prime just beyond B, with Mordell height of order B
  (1.5B–3B; R188 repair of "≈ 2.5B"). No r-depth and no large prime is needed. The
  sterile point is not where hardness sits.
* (2) Explicit r₀ (§6, Assessment): table of admissible ET constants C_adm(r, K₁) at θ = 2/5 (grows ≈ r^{0.1K₁+0.1}).
  Nicolas–Robin divisor bounds give r₀ ≈ exp(exp(30–60)). No computer-assisted proof along the O178 union-bound route
  (R188 repair: scope) at r = 101 (or 10⁹) is possible without a new explicit Type II count of 4/r^K with no τ-loss, the bottleneck already isolated at r = 17
  (MORDELL17B–D). I did not attempt it.
* (3) Exponential families (§4, PROVED, elementary): limit sets Λ_k never meet an r-generic line for odd r (Lemma 4.1; R188 repair: false for r = 2). ET classes
  have pushed-forward measure 1/ord_{M'}(2), not 1/M' (Lemma 4.2), so the O178 convergent-measure mechanism cannot
  transfer. This is consistent with O185's finite coverings (k = 9, 27).
* (4) Shots (§5): see SHARP 2.

## Caveats for the reviewer
* Prop 3.1(b) uses "a class gives an N-point at every n ≥ 1 in it" (POINTWISE_MORDELL §0) and the II2/I1 membership of
  Type II/I N-points; I checked the identities but not ET's Props 1.3/1.4 for composite n.
* Prop 5.1(a) reuses the single-prime box lemmas for general r (DEPTH_ASPECT §3 transfer, under review).
* Cor 3.3's density 1/4 assumes the Kronecker character of ℚ(√n) differs from χ_{−4} (true for n > 0 non-square).
* `ss_escape.py` uses its own seven-family enumeration; equality with `mordell_lib.residue_set` is asserted only for
  M ≤ 600. Every *reported* witness is re-solved at p.
* `ss_sqclass.py` gave only a trivial result (non-square classes mod 840 are Mordell-covered). It is kept as a tool for
  spark 2 below and not used in any claim.

## Sparks (not pursued)
1. **Pattern sterility conjecture.** Sterile points exist in G_T for every T ⊂ [q₀, ∞), divergent or not (greedy
   heuristic: the forbidden mass at prime q given the past is ≈ polylog(q)/q). Consequence: no finite ET covering of
   p·Sq^× for primes p with large least QNR. Test: for a prime p with least QNR 13 or 17, look for a finite covering of
   p·t² (mod L) with L ∋ 17, 19, 23 (needs a residue table for M | L only, not all M ≤ L).
2. **Multi-prime box dictionary.** Extend MORDELL17 Lemmas 1.1–2.3 to |T| ≥ 2 (mixed splits of the T-part between two
   moduli of I2/I3/II3). Mixed boxes are half-level at some primes and full-level at others, so the needed counts are
   mixed Type I/II bounds. This would turn the sparse side of §3 into a theorem: sterile points with infinitely many
   non-square coordinates.
3. **Mordell height of adversarial primes.** Near-square primes have h(p) ≈ 2.5 log p. A random-class model predicts
   that the worst primes ≤ X have h ≈ exp((log X)^{1/3}). Measure max h(p) on structured vs CRT-adversarial primes,
   and test whether "h(p) ≪ polylog p" is false.
4. In V_φ, are there sterile points at all beyond the squares (the convergent regime needs Σ 1/i_𝔮 < ∞ along T, so it
   lives on primes where φ has tiny order)? A clean profinite T1-only statement would support O183's template.
5. **(After O185's FYI) Sterile non-square points in Λ_k (e.g. k = 105).** A natural place to look is the
   ℓ-adic exponent line μ ∈ ℤ_ℓ ⊂ Ẑ (other components 0). There ν(μ)_q = k + 1 for every odd q with
   ℓ ∤ q(q − 1), so the point is the "integer" k + 1 (with 2-component 1) perturbed only at q = ℓ and q ≡ 1 (mod ℓ),
   all driven by the single parameter μ_ℓ. If the base point ν(0) lies in a class of modulus M, a neighbourhood
   of μ = 0 is covered, so candidates must sit away from 0. The perturbation set has density 1/(ℓ − 1), which is
   divergent in the sense of §3. The coordinates are coupled through one ℓ-adic exponent, though, so Prop 3.2's
   independence (and its conclusion) does not apply. This is the one-parameter analogue of the r-generic line inside
   Λ_k, and the right object for an O178-style measure argument (Haar on ℤ_ℓ, class measure =
   #{μ mod ℓ^j : …}/ℓ^j). Not pursued.
