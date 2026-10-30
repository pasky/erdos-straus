# Z52 lane B — banked board items and the slate's cheap tests

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only (not refereed).

Sources: boards `~/.pi/boards/20261030-es-generators` and `~/.pi/boards/20261030-es-weakpoints` (memo + items + rounds).
Scripts `scripts/z52_bank_*`, data `data/z52_bank/`.

## Summary

(to be written last)

## Part 1 — banked items

### 1(a) fable-7: the pencil S_{n,k}, Lemma A, and the class (−q, −d)

Sources: generators board, `items/fable.md` (fable-1, Lemma A/B/C), `rounds/01-argon.md` (argon's proof of Lemma A),
`rounds/03-astra.md` §1 (the repaired class and local evaluation), `rounds/04-argon.md` §2.1 (2-adic audit). Everything below
was re-derived here; the proof of Lemma A is a uniform Hilbert-reciprocity argument, not argon's Jacobi computation.

**Setting.** For odd n ≥ 1 and k ∈ ℤ let S_{n,k} : 4xyz − n(xy + yz + zx) = k ⊂ 𝔸³_ℚ (k = 0 is the Erdős–Straus surface U_n
of Bright–Loughran). Put q = 4y − n, d = qz − ny, d′ = qx − ny. On S_{n,k} (one-line expansions):

  (I1) x·d = k + nyz,  (I2) d·d′ = n²y² + kq,  (I3) 4d = q(4z − n) − n²  (identically, no equation needed),

and also q·xz = k + n(xy + yz). S_{n,k} is smooth unless k ∈ {0, −n³/4} (the gradient vanishes only at (0,0,0) and at
x = y = z = n/2). For k > 0 every positive point has q > 0 and d > 0 (by the last identity and (I1)).

**Theorem 1(a) (PROVED; generalises the board's Lemma A).** Let m ≥ 1, k = m², and n odd with
  n ≡ 1 (mod 8) if m is even,  n ≡ 5 (mod 8) if m is odd,  and (n/ℓ) = +1 for every odd prime ℓ | m.
Then S_{n,k}(ℕ) = ∅. In particular (board's Lemma A) S_{n,4}(ℕ) = ∅ for n ≡ 1 (8), and S_{n,1}(ℕ) = ∅ for n ≡ 5 (8).

*Proof.* Let (x,y,z) be a point with x,y,z ∈ ℤ_ℓ on S_{n,k} at a finite place ℓ, with q, d ≠ 0. We show (−q, −d)_ℓ = +1.
* ℓ odd, ℓ ∤ qd: both entries are units, symbol +1.
* ℓ odd, ℓ | q. If ℓ | n then ℓ | y, so the equation mod ℓ gives k ≡ 0; for ℓ ∤ m this is impossible, and for ℓ | m it is
  excluded by (n/ℓ) = +1. So ℓ ∤ n and (I3) gives −d ≡ (n/2)² ≢ 0 (mod ℓ): −d is a unit square, symbol +1.
* ℓ odd, ℓ | d, ℓ ∤ q. If ℓ ∤ m: by (I2) kq ≡ −n²y², so ℓ ∤ ny (else ℓ | kq) and −q ≡ (ny/m)² is a nonzero square mod ℓ.
  If ℓ | m: (I2) gives ℓ | n²y², ℓ ∤ n, so ℓ | y and −q = n − 4y ≡ n, a nonzero square mod ℓ by hypothesis. Symbol +1.
* ℓ = 2 (q = 4y − n is odd). If −q ≡ 1 (8) it is a 2-adic square. Otherwise −q ≡ 5 (8) and it suffices that d is odd, because
  (u, w)₂ = +1 for units u ≡ 1 (4). m even, n ≡ 1 (8): y even gives −q ≡ 1 (8); y odd gives −q ≡ 5 and
  dd′ = n²y² + kq ≡ 1 + kq ≡ 1 or 5 (mod 8) (as 4 | k), so d is odd. m odd (k ≡ 1 (8)), n ≡ 5 (8): y odd gives
  −q ≡ n − 4 ≡ 1 (8); y even gives −q ≡ 5 and dd′ ≡ kq (mod 4) odd.
For a point in ℕ³ we have q, d > 0, so (−q, −d)_∞ = −1, while all finite symbols are +1: this contradicts Hilbert
reciprocity ∏_v (−q, −d)_v = 1. ∎

**The class (PROVED).** 𝒜 := (−q, −d) ∈ Br S_{n,k} for every square k = m² ≠ 0 (n odd). Proof: S is smooth, so by purity
it suffices that all residues vanish; the only possible ramification is along {q = 0} ∪ {d = 0}. {q = 0} is the line
y = n/4, x + z = −4k/n², on which −d = (n/2)² is a square. On {d = 0}, (I2) gives −q = (ny/m)², a square in the residue
field (the components are lines over ℚ(√(k(4k + n³)))); so the residue (−q)^{v(−d)} is trivial. Under the hypotheses
of Theorem 1(a) the proof above says exactly: inv_ℓ 𝒜 = 0 on all of S(ℤ_ℓ) for every prime ℓ (points with qd = 0 by local
constancy), while inv_∞ 𝒜 = 1/2 on the positive real locus. The adelic set S(ℝ)_{>0} × ∏_ℓ S(ℤ_ℓ) is non-empty
(PROVED: positive real point x = z = n, y = (k + n³)/(2n²); for any ℓ choose y with q a unit, then z with d ≡ 1 mod ℓ —
z ≡ 1 + y (mod 2) when ℓ = 2 — and x = (k + nyz)/d ∈ ℤ_ℓ by (I1)). So Theorem 1(a) is a **Brauer–Manin obstruction to
positive integral points** on a locally soluble surface, for a positive-density set of n for each square k:
density (1/8)·∏_{ℓ | m odd} (ℓ − 1)/(2ℓ) among all n. 𝒜 is not constant (inv_∞ = 0 at (0, 1, −4/n) ∈ S_{n,4}(ℚ) for n > 4).
The board proved the k = 4 and k = 1 cases (astra R3, argon R4); the uniform statement for all squares k is new here.
The class is ramified for non-square k (residue k along {d = 0}), consistent with the data below.

**Where the obstruction fails (PROVED).** For k = 4, n ≡ 5 (8): the 2-adic point (2, 4, 2(2n+1)/(16 − 3n)) has v₂(d) = 1 and
−q ≡ 5 (8), so inv₂ 𝒜 = 1/2, and 𝒜 does not obstruct; n = 5 has the solution (2, 4, 22). The full Br S_{n,4}/Br ℚ is not
computed (open, as on the board).

**Numerical checks (CERTIFIED; `scripts/z52_bank_pencil.c`, cross-checked by the brute force `z52_bank_pencil_brute.py`
on all 9 ≤ n ≤ 300 for k = 4, −4, 1: identical counts).** The complete search uses: with x ≤ y ≤ z, n/4 < x ≤ 3n/4 (for
k > 0: 4/n > 1/x and 4x³ ≤ 3nx² + k; for k = −4: 4/n − 1/x = 1/y + (1/z)(1 − 4/(nxy)) > 0 and 4/n < 3/x), and for fixed x,
m = 4x − n, (my − nx)(mz − nx) = n²x² + km, so all (y, z) come from divisor pairs of one integer (both signs enumerated).
* k = 4: S_{n,4}(ℕ) = ∅ for all 1 249 values n ≡ 1 (8), 9 ≤ n ≤ 10⁴ (complete search). For n ≡ 5 (8), 13 ≤ n ≤ 10⁵, a
  solution exists for every n **except n = 3861 = 3³·11·13** (complete search): a failure that 𝒜 does not explain
  (the board's "≠ ∅ for every n ≡ 5 (8) ≤ 1200" is correct but does not extend).
* k = 1: S_{n,1}(ℕ) = ∅ for all n ≡ 5 (8), 13 ≤ n ≤ 10⁴. Among n ≡ 1 (8) ≤ 10⁵ the zeros are exactly 9, 33, 81, 345, 825,
  921, 1305, 3777, 3969, 4809, 5889, 7161, 8361, 11025, 14505, 16617, 26025, 26385, 55425, 99825 (all divisible by 3).
  The board's Lemma C list "{9, 81, 345}" (n ≤ 400) omits 33 (two independent codes agree that S_{33,1}(ℕ) = ∅).
* Other squares (n ≤ 3000, odd n, complete search; `data/z52_bank/pencil_square_k_zeros_le3000.txt`): the residue classes
  in which *every* n fails are exactly those of Theorem 1(a): k = 9: n ≡ 13 (24); k = 16, 64: n ≡ 1 (8); k = 25:
  n ≡ 21, 29 (40); k = 36, 144: n ≡ 1 (24); k = 49: n ≡ 29, 37, 53 (56); k = 100: n ≡ 1, 9 (40). Outside them only
  sporadic zeros (e.g. k = 16: 117; k = 25: 33, 57, 133, 417).
* Local invariants (`scripts/z52_bank_bm_check.py`): on 16 000 random rational points of S_{n,k} (k ∈ {1, 4}, 20 values of n)
  the product formula holds on every point; at every place ℓ where the point is ℓ-integral, (−q, −d)_ℓ = +1 in all
  86 217 odd-place tests and in all 2-adic tests with the theorem's congruence (k = 4, n ≡ 1 (8): 2878; k = 1, n ≡ 5 (8):
  2927), while the other residue class gives −1 in about 20 % of 2-adic tests.

**External novelty check (research subagent + own reading, accessed 2026-10-30; excerpts `sources/z52/bank_lit_*.txt`).**
* Bright–Loughran, *Brauer–Manin obstruction for Erdős–Straus surfaces*, arXiv:1908.02526v2 (12 May 2020), Bull. LMS 52
  (2020) 746–761, DOI 10.1112/blms.12359 (PDF read): Thm 1.1 "there is no Brauer–Manin obstruction to the existence of
  natural number solutions"; Thm 1.2: for odd n and u ∈ ℕ³ a solution, ∏_{p|n}(−u₁/u₃, −u₂/u₃)_p = −1; Thm 1.6:
  Br U_n/Br ℚ ≅ ℤ/2 generated by (−u₁/u₃, −u₂/u₃) (transcendental); Thm 1.8: (U_n(ℝ)⁺ × ∏_p U_n(ℤ_p))^Br ≠ ∅ but is not
  everything. Only k = 0; Remark 1.10 treats m/n, not a constant-term deformation.
* Citers of BL (Semantic Scholar API, 5 records): Mitankin–Uhlemann arXiv:2411.02629v3 (semi-integral points on Markoff
  orbifold pairs), González-Avilés arXiv:2209.06653 (pinched varieties), X. Xu arXiv:2609.29250v1 and Cao–Xu
  arXiv:2610.32302v1 (ES polynomial families, mod 24 primes), plus one unparsable record. Abstracts read: none treats
  k ≠ 0 fibres or positivity-constrained BM on the ES cubic. Full texts NOT ACCESSED.
* Markoff-type cubics x² + y² + z² − xyz = k: Ghosh–Sarnak arXiv:1706.06712v3 (Invent. Math. 229 (2022)), Loughran–Mitankin
  arXiv:1807.10223v3 (IMRN 2021), Colliot-Thélène–Wei–Xu arXiv:1808.01584v4, Dao arXiv:2202.07142v4: integral Hasse
  failures and BM obstructions for a *different* cubic family, no positivity constraint. Colliot-Thélène–Wittenberg
  arXiv:0911.3539v3 (sums of cubes) and Colliot-Thélène–Xu arXiv:0712.1957: different families.
* Verdict: no source found treating 4xyz − nσ₂ = k with k ≠ 0, or the positive-integral obstruction from (−q, −d).
  This is a search result, not a proof of novelty. Assessment: the mechanism is the standard one (Hilbert reciprocity
  with the archimedean sign, as in Yamamoto/BL for k = 0), so the novelty, if any, is the regime (k = m², positive
  density, locally soluble), not the method.

**Why nothing transfers to k = 0 (PROVED except where labelled).**
1. At k = 0 the fibre is singular (at the origin) and (I2) degenerates to dd′ = (ny)². The step "ℓ | d ⇒ −q is a square
   mod ℓ" used the term kq; at k = 0 it is gone, so primes dividing d carry arbitrary invariants. Data (CERTIFIED,
   `scripts/z52_bank_k0_places.py`, all positive ES solutions of all primes 5 ≤ p < 400, all 6 labellings): the
   compensating place where (−q, −d)_ℓ = −1 is always ℓ = 2 or a prime ℓ | d (4 386 times an odd ℓ ≠ p dividing d, 3 117
   times ℓ = p, 7 233 times ℓ = 2), never a prime ℓ ∤ 2d; BL's class always compensates at ℓ = p (13 302 of 13 302).
2. Limit as k → 0 (PROVED). 𝒜 lives on the base-changed pencil k = m² (the residue along {d = 0} is k mod squares, so it
   does not live on the k-pencil itself). Over the m-line, the residue computation goes through at m = 0 on the smooth
   locus: on U_n ∖ {0}, {q = 0} is the line y = n/4, x + z = 0 with −d = (n/2)², and {d = 0} is the line y = z = 0, along
   which v(d) = 2 (d = −y²(n/x)/(1 − cy), c = (4x − n)/(nx)). So 𝒜|_{U_n∖{0}} ∈ Br(U_n ∖ {0}).
3. That limit class does not come from Br U_n (CERTIFIED by explicit points, given BL Thm 1.6). On U_5, at the place 3 the
   symbol of 𝒜 differs from that of BL's generator at P = (30/29, −12, −12) and agrees at P′ = (120/121, −12, −8);
   since Br U_5/Br ℚ = ⟨BL⟩, any class of Br U_5 differs from 0 or from BL by a constant algebra, whose local
   evaluation is constant, and 𝒜's real evaluation is non-constant. So the limit is ramified at the singular point
   (along an exceptional curve of a resolution) and gives no obstruction to anything on U_n.
4. The k-scaling (x, y, z, n, k) ↦ (λx, λy, λz, λn, λ³k) moves away from k = 0; at fixed y, gcd(K_y(±4), K_y(0)) | 4
   (board). No transport. Assessment: the theorem is a calibration of (J)97's "shape of a failure" — a sibling where
   reciprocity kills a positive-density set of n — not progress on 4/p.

### 1(b) GT1: every non-square n ≡ 1 (4) has a genus-free level

Source: weakpoints board, fable-4 (definition, conjecture), astra R1 §3 (proof), argon R2 / fable R2 (audits).
**Definition (fable-4).** For t ≡ 0 (mod 4), n is *genus-obstructed at t* if some odd real character ψ mod t
(ψ² = 1, ψ(−1) = −1) has ψ(s) = +1 for every prime s | tn + 1 with s ∤ t. A level-t word needs a divisor
D ≡ −1 (mod t) of tn + 1 (D is prime to t), and ψ(D) = ψ(−1) = −1 forces some prime factor with ψ = −1; so
genus-obstructed ⟹ no level-t word. t_G(n) := least such t at which n is not genus-obstructed.

**Lemma GT1 (PROVED, relative to Dirichlet's theorem).** Every positive non-square n ≡ 1 (mod 4) has t_G(n) < ∞.
*Proof.* (1) The Jacobi symbol a ↦ (a/n) is a character mod n, non-trivial because n is not a square, and even because
n ≡ 1 (4); χ₋₄ is odd. So (χ₋₄, (·/n)) maps (ℤ/4n)^× onto {±1}², and Dirichlet gives a prime a ≡ 3 (4) with
(a/n) = −1; by reciprocity (n ≡ 1 (4)) also (n/a) = −1, so a ∤ n. (2) By CRT and Dirichlet pick a prime r ≡ 1 (4) with
r ≡ −(4n)⁻¹ (mod a); then a | 4rn + 1. Put t = 4r. (3) The real characters mod 4r are generated by χ₋₄ and (·/r); since
(−1/r) = +1 the odd ones are exactly χ₋₄ and ψ := χ₋₄·(·/r). Now χ₋₄(a) = −1, and (a/r) = (r/a) = (−(4n)⁻¹/a) =
(−1/a)(n/a) = (−1)(−1) = +1, so ψ(a) = −1. The single prime a | tn + 1 (a ∤ t) defeats both odd real characters. ∎
At odd squares n = m² every level is obstructed by ψ = χ₋t (s | tm² + 1 ⟹ −t ≡ m⁻² is a square mod s), which is T1's
genus form. Scope: finiteness only; the level 4r is Linnik-size, no bound t_G ≪ log n, nothing about the *class*
of a divisor (the ES₅ event), and no ES implication. Assessment: this retires fable-4's open target; the "genus layer
is pointwise free" sentence is correct with that scope.
**Check (CERTIFIED, `scripts/z52_bank_gt1.py`, F₂-linear-algebra test "v(−1) ∈ span{v(s)}" over a basis of real
characters mod t):** all 7 457 non-squares n ≡ 1 (4), n ≤ 3·10⁴: t_G(n) ≤ 116 (max at n = 12 369; 62 % have t_G = 4),
and for every n the planted level 4r (least a, least r) is genus-free (max planted level 6 388); every odd square
≤ 3·10⁴ is obstructed at all t ≤ 40. Consistent with fable's census (max t_G = 124 below 3·10⁵, not re-run).

### 1(c) Three-coset Kneser bound 1 ≤ Ω_out ≤ d − 2

Sources: weakpoints board astra-1 (items/astra.md), argon-1 Thm 1.3 (items/argon.md), astra R1 §1. Base:
`EXSET_CHAR_FORCING.md` Lemma 2.1 (window criterion), Lemma 2.2 (Kneser covering lemma), Cor 2.3.
Setting: p ≡ 1 (4) prime, q ≡ 3 (4) prime with (q/p) = −1 (forced window), x = (p+q)/4, G = 𝔽_q^× (cyclic of order
2u, u odd), U = G², R(x) = ∏_s {s^{−v_s}, …, s^{v_s}}, R(px) = R(x) ∪ pR(x) ∪ p⁻¹R(x). "Full window fails" means
−1 ∉ R(px) (no solution of 4/p with this x, Lemma 2.1). Note (p/q) = (q/p) = −1 (reciprocity, p ≡ 1 (4)) and
(x/q) = (p/q) = −1 since 4x ≡ p.

**Proposition 1(c) (PROVED relative to Lemma 2.2).** If the full window fails, then for H = Stab(R(x)) and also for
H = Stab(R(px)), with d = [U : H]: H ≤ U, d ≥ 3, no prime factor of x lies in −H, and
  1 ≤ Ω_out(x) := Σ_{s ∉ H} v_s(x) ≤ d − 2  (Cor 2.3 had d − 1, and only for −1 ∉ R(x)).
*Proof, H = Stab(R(px)) (argon).* Apply Lemma 2.2 to the multiset {prime factors of x with multiplicity} ∪ {p}: its box
is R(px). Lemma 2.2(i)–(iii) give H ≤ U, no factor (and not p) in −H, and n_out ≤ d − 1, where p ∉ U ⊇ H is one of the
out-factors; so Ω_out(x) = n_out − 1 ≤ d − 2. *Proof, H = Stab(R(x)) (astra).* B = R(x) misses −1, and also −p⁻¹
and −p (as −1 ∉ pB, p⁻¹B). The cosets −H, −pH, −p⁻¹H are distinct: −pH = −H would put p ∈ H ⊆ U; if −pH = −p⁻¹H then
p² ∈ H, so pH is the unique involution of the cyclic group G/H, i.e. pH = −H, and then −p ∈ H ⊆ B, contradiction.
So |B| ≤ (2d − 3)|H|, while Kneser (as in Lemma 2.2) gives |B| ≥ (1 + 2Ω_out)|H|. In both versions Ω_out ≥ 1 because
x is a non-residue, so some prime factor of x lies outside U ⊇ H; then d − 2 ≥ 1 gives d ≥ 3. ∎
(For H = Stab(R(px)) also x, p ∉ −H, as x, p ∈ R(px).) Consequence at q = 7 (u = 3 forces d = 3, H = {1}; argon):
a failing full window has exactly one prime factor of x, with multiplicity, ≢ 1 (mod 7), call it s₀; s₀ ∉ −H = {6} and
x ≡ s₀ is a non-residue, so s₀ ≡ 3 or 5; s₀ ≡ 5 would give p ≡ 4x ≡ 6 ∈ −H, excluded; hence p ≡ 5 (mod 7).
**Test (CERTIFIED, `scripts/z52_bank_kneser.py`):** all primes p ≡ 1 (4) < 2·10⁵ and forced q ≤ 59: 10 035 failing full
windows, 0 violations of any clause for either stabiliser (the 283 failures at q = 7 all have p ≡ 5 (mod 7) and exactly one
prime factor ≢ 1 (mod 7)); the bound Ω_out = d − 2 is attained in 713 cases (so it is
sharp in practice). Scope (board, sustained): a local inverse theorem for one window; fable's within-class test shows
no cross-window escape; nothing global follows.

### 1(d) Coprime-category corrections (SQ, ES ⇒ ES₅)

Source: weakpoints board argon-2, astra R1 §2. Definitions: ET call (x, y, z) Type I if n | x and gcd(n, yz) = 1,
Type II if n | y, z and gcd(n, x) = 1 (FRONTIER §1 adopts this, R290 repair). An *N-point* is an element of
V_I(n) = {4abd = ne + 1, a + b = ce} or V_II(n) = {4abd = n + e, a + b = ce} (all ≥ 1, no coprimality), giving the
solutions (abdn, acd, bcd), resp. (abd, acdn, bcdn).

**Facts (CERTIFIED; `scripts/z52_bank_types.c`, `scripts/z52_bank_coprime.py`).**
1. Coprime Type I ∪ Type II is empty for an odd non-square n ≤ 10⁶ exactly at n ∈ {105, 345, 561, 5985} (complete
   solution enumeration with early exit; squares skipped, they are zeros by ET Prop 1.6). Same four as argon.
2. V(n) ≠ ∅ at all four, e.g. 4/105 = 1/27 + 1/1260 + 1/3780 from (a,b,c,d,e) = (3,9,4,1,3) ∈ V_II(105) with
   gcd(abd, 105) = 3; similarly 345: (1,29,10,3,3), 561: (1,47,16,3,3), 5985: (5,100,7,3,15).
3. n = 3985 = 5·797: 206 solutions of 4/3985, of which exactly 5 coprime Type I (e.g. (91312290, 1026, 34371) from
   (2, 67, 3, 171, 23)) and 0 coprime Type II. Its five-slot words (u ≤ v, complete) are (4, 5, 210), (23, 5, 35),
   (80, 5, 10), all with gcd(uv, 3985) = 5 (astra's correction of argon's "25" stands).

**Which definition the repo used.** SQ was introduced in `BRAINSTORM/corr_joint_factorisation.md` (O146) and
DISCOVERIES (J)1 as "V_I(n) ∪ V_II(n) = ∅ ⟺ n square" — N-points, **no coprimality** (two enumerators, n ≤ 10⁶);
`STERILE_STEER.md` Prop 3.1(b) and `reviews/sterile-steer-review.md` D2 say so explicitly. With that definition the
four integers are not counterexamples (fact 2), and the repo's SQ claim is **not refuted**. FRONTIER §5.5, however,
writes "Type I ∪ Type II empty", and FRONTIER §1 defines Type I/II coprimally; read with its own definitions the §5.5
sentence is **false** at 105, 345, 561, 5985. So §5.5 is a mis-transcription, not a wrong conjecture; the fix is to
write "V_I(n) ∪ V_II(n) (ET N-points, no coprimality)". `scripts/spec_typecount.c` uses a third, mixed convention
(Type I without gcd(c, n) = 1 — argon is right that this filter is absent — but Type II with gcd(abd, n) = 1); its
only odd non-square zero ≤ 10⁴ is 105 (CERTIFIED by running it), so it is not the source of SQ's evidence, and argon's
"root cause of the census omission" story is not what happened.
**ES ⇒ ES₅ (FRONTIER §7.14).** At 3985 the coprime implication "coprime Type I/II solution ⟹ five-slot word with
gcd(uv, n) = 1" fails (fact 3). Plain ES₅(3985) holds (the five slot identities need no coprimality), and §7.14 asks about
primes, where gcd(uv, p) = 1 and the coprimality conditions are automatic. **Primes are untouched.**

### 1(e) argon-3: I3_𝒞 and Prop 3.2(b)

Source: weakpoints board argon-3, astra R1 §4 and R3, fable R3 Audit 2. 𝒞_n = 4ℤ ∪ (8ℤ − n). Words: (t, u, v) ∈ ℕ³ with
tuv − u − v = n; A = tu − 1, A* = tv − 1.
**Definition.** I3_𝒞(n) := #{(t, u, v) ∈ ℤ_{≥3}³ : tuv − u − v = n, {t, u, v} ∩ 𝒞_n ≠ ∅}.
**Relation to ES (PROVED).** I3_𝒞(p) ≥ 1 ⟹ ES₅(p) ⟹ ES(p): by LOWERTAIL_ROUND2_FABLE Thm 1 (second form, no coprimality,
n ≡ 1 (4)) a coordinate in 𝒞_n puts 4 into one of the five slots t, u, v, A, A*, and each slot is a 4/n identity:
4 | t = 4s: 4/n = 1/(suv) + 1/(nsu) + 1/(nsv); 4 | v = 4w: 1/(wA) + 1/(nwt) + 1/(nwtA); 4 | u: same with A*; 4 | A = 4a:
1/(av) + 1/(avA*) + 1/(naA*); 4 | A*: symmetric (each checked by expansion, and on 4 809 words below). The converse fails:
I3_𝒞(2521) = 0 but ES(2521) holds (free word (15, 2, 87)). Thm 3.1 ("ES₅ ⟺ FreeCert ∨ I3_𝒞 ≥ 1") is a definitional split
of words by min(t,u,v) ≤ 2; its content is the census.
**Prop 3.2(b) (PROVED; astra's equivalence form).** Let p be Mordell-hard (p mod 840 ∈ {1, 121, 169, 289, 361, 529}).
Then p has an interior word (t ≥ 3, v ≥ 3) with endpoint u = 3 ⟺ M = (p+3)/4 is composite.
*Proof.* p ≡ 1 (8), p ≡ 1 (3), p ≡ ±1 (5) give M odd, M ≡ 1 (3), 5 ∤ M; so every prime factor of M is ≥ 7. A u = 3 word is
(3t − 1)v = 4M with A = 3t − 1 ≡ 2 (3). (⇐) Let q be the least prime of M (q ≥ 7, M/q ≥ q). If q ≡ 2 (3): A = q,
t = (q+1)/3 ≥ 4 (q ≥ 11), v = 4M/q ≥ 28. If q ≡ 1 (3): A = 2q, t = (2q+1)/3 ≥ 5, v = 2M/q ≥ 14. (⇒) If M is prime, the
divisors of 4M that are ≡ 2 (3) are 2 and 2M, giving t = 1 or v = 2. ∎ (The original "iff M has a prime factor ≡ 2 (3)"
is false: p = 1201, M = 7·43, word (5, 3, 86) — non-certifying. The certifying direction "q ≡ 2 (3) gives 4 | v" is fine.)
**Checks (CERTIFIED).** Prop 3.2(b) holds on all 20 513 Mordell-hard primes ≤ 10⁷ (`scripts/z52_bank_prop32b.py`; 8 590 of
them have a *certifying* u = 3 interior word). The I3_𝒞 census is Part 2 T1.

### 1(f) argon-6.1: median-coordinate corollary of H4_NOT_POLYLOG

Source: generators board argon-6 (items/argon.md), astra R1 (hypothesis patch), fable R1/R3; base
`H4_NOT_POLYLOG.md` Lemma 2 (events E_(a,v): p ≡ −a−v (mod av), 1 ≤ a < v ≤ H coprime, minus (1,2), (2,3);
C_(A,d): p ≡ −d (mod A), 2 ≤ A ≤ H, d | A+1, d < A, minus (2,1), (3,2)) and Theorem 1 / §§6–7 (the construction
yields primes p > H², p ≡ 1 (mod 840), **avoiding every event of both families**, with log p ≪ L¹²(log L)², L = log 3H;
≪ L⁶ log L relative to Gallagher's (G) or GRH).
**Patch.** Theorem 1's two *stated* conclusions (forest edges, p mod A ∉ G_A) are weaker than what the proof uses (G_A
carries a colour condition); the corollary must assume avoidance of all E and C events, which the construction supplies
(H4_NOT_POLYLOG "there is a prime avoiding the original events", proof of Thm 1).
**Corollary 1(f) (PROVED relative to H4_NOT_POLYLOG Thm 1).** Let p ≡ 1 (mod 24) be prime, p > H² ≥ 4, avoiding all
E_(a,v) and C_(A,d) at scale H. Then every word (t, u, v), u ≤ v, with a coordinate in 𝒞_p has
min(A, A*, v) > H and med(t, u, v) > √(H+1). Hence for every κ < 1/12 (κ < 1/6 relative to (G) or GRH) there are
infinitely many primes p ≡ 1 (mod 840) all of whose certificate words have med(t, u, v) > exp(½(log p)^κ).
*Proof.* vA = p + u, u | A + 1 = tu. A = 0 is impossible; A = 1 gives (2, 1, p+1), (1, 2, p+2), non-certifying (p ≡ 1
(24): coordinates ≡ 2, 1, 2 / 1, 2, 3 mod 8, and 𝒞_p = 4ℤ ∪ (8ℤ + 7)). If 2 ≤ A ≤ H and u < A: p ≡ −u (mod A) with
u | A+1 is the event C_(A,u), so (A, u) ∈ {(2,1), (3,2)}: words (3, 1, (p+1)/2), (2, 2, (p+2)/3), with (p+1)/2 ≡ 1, 5
and (p+2)/3 ≡ 1 (mod 8): non-certifying. If 2 ≤ A ≤ H and u ≥ A: u | A+1 forces u = A+1, t = 1, p ≡ −1 (mod A), the
event C_(A,1) for A ≥ 3; A = 2 gives (1, 3, (p+3)/2), (p+3)/2 ≡ 2 (mod 4), non-certifying. So A > H, and A* = tv − 1 ≥ A.
If v ≤ H: u = v forces u = v = 1 (u | p), the non-certifying word (p+2, 1, 1); otherwise u < v ≤ H, gcd(u, v) | p so
coprime, and uv | p + u + v is E_(u,v), leaving (1,2), (2,3), i.e. ((p+3)/2, 1, 2) and ((p+5)/6, 2, 3), with
(p+3)/2 ≡ 2 (mod 4) and (p+5)/6 ≡ 1 (mod 4): non-certifying. So v > H. Finally tu = A + 1 > H + 1 gives
max(t, u) > √(H+1), and med(t, u, v) ≥ min(max(t, u), v) > √(H+1). With H = exp((log p)^κ) and the size bound of
Thm 1 the asymptotic statement follows. ∎
Scope (board): this excludes only bottom-up enumeration of a small coordinate followed by trial division; it says
nothing about existence or about other algorithms; the Lenstra/Bernstein half is prior art (`BRAINSTORM/s3_lll_lenstra.md`).
**Check (CERTIFIED, `scripts/z52_bank_median.py`):** for all 2 212 primes p ≡ 1 (24) < 2·10⁵, with H_av(p) the largest H
(H² < p) at which p avoids all E and C events (max H_av = 28, at p = 196 561), every certifying word satisfies
min(A, A*, v) > H_av and med > √(H_av + 1): 0 violations. M₂(p) := least median over certifying words is 3, 3, 4, 3, 15, 7,
7, 9, 8 at p = 73, 193, 409, 577, 2521, 3361, 5569, 9601, 66529 (first six as astra reproduced; argon's 8813281 value not
rechecked).

## Part 2 — cheap tests

### T1 I3_𝒞 census on 4·10⁷ < p ≤ 10⁸

TODO

### T2 S_{n,−4} census, n ≤ 10⁵

TODO

### T3 ES_Q1 over ℤ[i], Gaussian primes 10⁴ < N ≤ 10⁶

TODO

### T4 Shared invariants of T2/T3 failures

TODO

## Review log

TODO
