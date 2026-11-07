# Z62_INVERSE — structure vs randomness at one prime: does R(p) = 0 force an explicit structure? (checkpoint 1)

**ES is OPEN; nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED (computer) /
EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Lane INVERSE of wave z62 (brief `z52bbriefs/z62_lanes.md`;
board item fable-5). Scripts `scripts/z62_inverse_*`, data `data/z62/inverse/`.

Notation. R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}. Two exact slicings (PROVED, FRONTIER §2.1):
R(n) = Σ_{u≥1} D(n+u; 4u) = Σ_{C≥1} D(4Cn+1; 4C), with D(N; m) := #{d | N : d ≡ −1 (mod m)}.
For a slice (N, m) let P = prime factors of N coprime to m, H = ⟨P⟩ ≤ G_m = (ℤ/m)^×, Div = divisor residues.
**Slice types**: h (hit, −1 ∈ Div); B (BM-kill: χ_{−m}(ℓ) = +1 ∀ ℓ ∈ P); T (other real odd character kills H);
Q (only non-real odd characters kill H); S (starved: −1 ∈ H \ Div). B, T, Q = *structured* failure (−1 ∉ H),
S = *random* failure.

## 0. Falsifier table (committed at checkpoint 1; restated at the end)

| | behaviour of the INVERSE idea |
|---|---|
| F1 odd squares | every slice of m² is a B-kill (T1 is the extreme structured case: χ_{−4u} trivial on all ℓ \| m²+u). An inverse theorem "R = 0 ⟹ S" is *true* at squares; step 2 "S ⟹ another family fires" must fail at squares, so it must use non-squareness at an identified step (only candidate so far: χ_p ≠ 1, via Burgess / n_p). |
| F2 C-even / R₈ | the 12 R₈-zeros have R ≥ 12; their C-slices fail on all even C. Any inverse statement read off C-slices must say which parity it uses. Census included (tag E). |
| F3 composites | the 285 composite zeros (265 divisible by 3, 5 or 7) have slice-type profiles indistinguishable from the prime zeros in the first census (tag K, §2). An inverse theorem with no primality input therefore also "holds" there; step 2 must use primality. |
| F4 known zeros | the 14 (★)-zeros and the 24 𝔊*-zeros with R > 0 are in the census (tags Z, G). |

## 1. Precise statements attacked

* **(INV-main), the inverse half.** For primes p ≡ 1 (24) (in particular p ∈ 𝔐), R(p) = 0 — or R(p) ≤ ε·M_BM(p) — forces
  an *atypical* structure in the slice data at a scale K(p) → ∞, i.e. one that an ordinary prime of the same class mod 840
  whose slices fail does not have. "Atypical" is measured by the conditional law of failure types (B/T/Q/S) among failing
  slices in bands of the modulus, compared with class-matched controls.
* **(STEP2).** Such a structure S forces another certificate family (Type I, the a = 1 / López line, …) to fire.
* Proposed concrete S from the brief: "p + k is χ_{−4k}-split for most small k". By the Jacobi transfer
  (ℓ | p + k ⟹ χ_{−4k}(ℓ) = (−k/ℓ) = (p/ℓ) = χ_p(ℓ) for p ≡ 1 (4)) this is: *every prime factor of p + k is a quadratic
  residue mod p*, i.e. the u-slice k is a B-kill. (PROVED one-line lemma; it also forces χ_p(k) = +1, since
  ((p+k)/p) = (k/p).)

**Why not closed.** Z52D_FOURIER killed the *signed bounded-order character* inverse lemma for individual window
obstructions and found no shared character other than χ_p; Z57_COMPLEMENT found positive (not complementary) association
of families. Neither asked whether a *zero* has an atypical *distribution* of obstruction types across scales, i.e. the
Gowers-type question "is maximal cancellation X = −M_gen achieved by structure or by randomness?". That is (INV-main).

## 2. First falsifier (exploratory census; EVIDENCE) — run before the kill test was written, reported as such

`scripts/z62_inverse_sets.py` (sets, exact R by `scripts/z62_inverse_rsieve.c` to 1.2·10⁷) and
`scripts/z62_inverse_slices.py 256` (slice types for u, C ≤ 256), `scripts/z62_inverse_bands.py` (band table), data
`data/z62/inverse/{sets.txt,slices_U256.txt}`. Integers ≥ 2·10⁴: Z (10 of the 14 (★)-zeros), c (319 class-matched
controls, same class mod 840, 15 primes on each side of each Z), n (all 125 primes p ≡ 1 (24) in (10⁵, 1.2·10⁷] with
1 ≤ R ≤ 4), t (400 random primes ≡ 1 (24), not class-matched), K (237 composites).

Structured share among *failing* slices, st|f = (B+T+Q)/(B+T+Q+S), u-slices, bands [1–4] [5–16] [17–64] [65–256]:
Z 0.93 0.78 0.62 0.64 · c 0.94 0.75 0.63 0.63 · n 0.93 0.73 0.63 0.64 · t 0.89 0.68 0.57 0.59 · K 0.91 0.73 0.68 0.72.
C-slices: Z 0.95 0.82 0.71 0.78 · c 0.95 0.79 0.75 0.75 · n 0.93 0.76 0.74 0.75 · t 0.94 0.77 0.70 0.71.
B-share among failing u-slices, [5–16]: Z 0.66, c 0.52/0.81 = 0.64, n 0.62.

Reading (EVIDENCE): the brief's observation (B-kills at most k ≤ 8 at the zeros) is real — the raw B rate at u ≤ 16
is 0.64–0.85 at zeros versus 0.52–0.58 at class-matched controls — but it is **entirely the selection "the slice
failed"**: *conditional on failing*, the zeros' slices have the same type mix as ordinary failing slices of the same
class (|Δ| ≤ 0.05 everywhere beyond u = 4). The class mod 840 matters (t vs c: 0.57 vs 0.63), so matching is essential.

## 3. Pre-registered kill test (written before running it on fresh data)

Fresh data: exact R by sieve to 10⁸; **near-zeros** = all primes p ≡ 1 (24) in (1.2·10⁷, 10⁸] with R(p) ≤ 2 (none has
R = 0 there, CERTIFIED by the census of FRONTIER §2.1); **controls** = for each near-zero the 3 nearest primes of the same
class mod 840 with R ≥ the median R of its ±50-prime class window. Slice types for u, C ≤ 256.
* **KILL (INV-main)** if, for both families (u and C) and both bands [17–64], [65–256], the near-zeros' conditional
  shares among failing slices satisfy |Δ st|f| ≤ 0.05 and |Δ B|f| ≤ 0.05 versus controls. Meaning: failing slices at
  near-zeros are distributed like ordinary failing slices — the deficit is carried by "randomness", not by a structure
  visible slice by slice. If killed, the main line (a slice-visible inverse theorem with growing scale) is abandoned.
* **Escape hatch pre-registered:** structure could still be *joint* (cross-slice coupling beyond the shared class
  mod 840 and the χ_p-pattern on small primes). Test 2: observed vs product-of-marginals frequency of "all slices
  u ≤ U fail" (U = 8, 16, 32) among primes ≡ 1 (24) in [10⁶, 1.2·10⁷], marginals estimated within cells
  (class mod 840) × (χ_p(11), χ_p(13)). O/E within [1/3, 3] at U = 16 and 32 ⟹ no joint structure detectable at that
  scale.

*(sections 4ff to be written)*
