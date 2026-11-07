# Z62_PARITY — index / parity / fixed-point existence at a single prime (lane PARITY, wave z62)

**ES is OPEN; nothing here proves or disproves it, or (MS), (MS-U₇), U₇.** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results, internally reviewed only.
Scripts `scripts/z62_parity_*`, data `data/z62/parity/`. Brief: `z52bbriefs/z62_lanes.md` §PARITY.

*Status: CHECKPOINT 1 (skeleton; pre-registered kill test in §3).*

Notation as in FRONTIER §2 / `Z60_SUMMARY.md`: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} ((★)); 𝔐 = {1, 121, 169, 289,
361, 529} ⊂ (ℤ/840)^×; U₇(n): some f ≡ 7 (8) with (−n mod f) | f + 1; Z₇ = the eight composite U₇-zeros; "hard primes" =
primes p ≡ 1 (24) (and p mod 840 ∈ 𝔐 where stated).

## 0. Mandatory falsifier table (for the *framework* of §1 and the main line of §3; re-stated at the end)

| screen | behaviour of a parity/index mechanism (§1) | where primality / non-squareness must enter |
|---|---|---|
| **F1 odd squares** | Automatic *if* the forced set Fix τ (or the critical / terminal cells) lies in certificates ∪ K: then W(m²) = 0 and the identity only says I(m²) = 0. The mechanism must therefore have I(m²) ≡ 0 and I(p) ≢ 0. | In the evaluation of the "easy side" I(p) (Zagier: #Fix σ = #{p = x(x+4z)} = 1 uses primality). Any I that is a genus-character / Jacobi expression in p is T1-compatible by construction. |
| **F2 C-even / numerator 8** | An index whose terminal cells are certificates of a *sub-line* must not be stated uniformly in the numerator: R₈(p) = 0 at 12 primes in [10¹⁰, 1.1·10¹⁰]. An exact index with support in R₈ is refuted there (Lemma P1). | The index's support must contain the C-odd part, and the easy side must see 4 (not 8). |
| **F3 composites** | Uniform-in-n identities: at the 285 composite R-zeros the easy side must vanish too (it may: divisor-type terms). Prime-only identities: no constraint, but then primality is used in the identity itself. | Divisor-type easy side (has extra terms at composites) or prime-only identity. |
| **F4 known zeros** | **An exact index (no threshold) with support in (★) is refuted at the 14 (★)-zero primes** (Lemma P1). Support must be a family with no known prime zero: U₇, U_II, N_II (full Type II), full ES. | — |

## 1. The framework and its necessary condition

**Lemma P0 (index necessity; PROVED, elementary — generalises WINDMILL Lemma 1 and `BRAINSTORM/invol_topological.md`
Lemma T to the cochain/Stokes form).** Let K be a finite cell complex (built from p), Cert ⊂ cells(K) a set of
"certificate cells", each mapped to an ES certificate by Φ. Any of the following yields an integer (or F₂) weight
w: {certificates} → ℤ with Σ_c w(c) = I(p), where I(p) is the quantity the argument evaluates:
(a) two involutions σ, τ on a finite set S with Fix τ ⊂ Φ⁻¹(certificates) ∪ K_p (Zagier / Heath-Brown): I = |Fix σ| − |K_p| (mod 2);
(b) a graph of max degree 2 (PPA / handshake) whose odd-degree vertices are a known set ∪ certificates: I = #known (mod 2);
(c) a Morse matching on K whose critical cells are certificates ∪ known cells: I = χ(K) − χ_known (over ℤ, signed by dimension);
(d) Stokes: an acyclic K, a cochain ω with δω supported on Cert, and a cycle z with ⟨ω, z⟩ = I ≠ 0: for every filling
∂c = z, Σ_{e ∈ Cert} c(e)δω(e) = I (the weights c(e)δω(e) depend on the filling only through δω-cohomologous data);
(e) Lefschetz–Hopf for a cellular self-map with fixed cells ⊂ Cert ∪ known: I = L(f) − (known).
*Proof.* (a) |S| ≡ |Fix σ| ≡ |Fix τ|. (b) handshake. (c) the Morse complex has the same Euler characteristic.
(d) I = ⟨ω, ∂c⟩ = ⟨δω, c⟩ and δω vanishes off Cert. (e) Hopf trace formula. ∎
So **the entire content of any parity/index proof of ES at p is a weight w on certificates whose total is a computable,
non-zero function of p** ("deterministic weighted count"). The novelty can only be in *where w comes from* (it may be
non-local: in (b)–(d) w depends on neighbouring non-certificate cells).

**Lemma P1 (exact indices must avoid families with prime zeros; PROVED).** If an identity Σ_{c ∈ 𝒜(p)} w(c) = I(p)
holds for every prime p ≡ 1 (4) with no threshold, and I(p) ≠ 0 at every prime in a set 𝒫, then 𝒜(p) ≠ ∅ on 𝒫. Hence an
exact index with support in (★) cannot have I ≠ 0 at the 9 (★)-zero primes in 𝔐 (data: `data/z58/screens/`), nor one with
support in R₈ at the 4 R₈-zero primes in 𝔐 near 10¹⁰. An index argument for (MS) must either (i) carry a threshold in
its *easy side* (I(p) = 0 for the small zeros, I(p) ≠ 0 eventually — unusual for parity identities, not excluded), or
(ii) be supported on U₇ / U_II / full Type II / full ES. ∎ (Trivial, recorded because it fixes the admissible supports.)

## 2. Precise statements attacked

* **(PAR)** Find (K_p, Cert, w-source) as in Lemma P0 with I(p) ≠ 0 for all primes p ∈ 𝔐 (beyond a stated threshold)
  and I(m²) = 0 for odd squares, with a proof of the evaluation of I. Open; this lane tests concrete new objects.
* **Why not already closed.** Closed: finite-menu affine involutions on X(p) ((J)2 Thm 6.1, CONDITIONAL on BH); finite
  affine group menus (Z52D_PARITY Thms C, D); fixed-feature weight dictionaries (WINDMILL §3, invol_windmill_signature
  E1–E3, board astra-3 LP certificates); cheap signs on U₇ words (board, fable). Not closed: weights coming from
  *non-affine geometric structure* (topograph / river / Farey complex), cochain (Stokes) forms (d), and indices supported
  on U₇ or full Type II. These are what §3 tests.

## 3. Main line and PRE-REGISTERED kill test (checkpoint 1)

**Observation A (PROVED, one line; checked numerically in §4).** For (u,B,C) a (★) triple, the matrix
γ = [[4Cu−1, p],[4C, 4CB−1]] ∈ SL₂(ℤ) is an automorph (U = 1) of the binary form F = [4C, 4C(B−u), −p], which is
**ambiguous** (first coefficient divides the middle one), primitive, of discriminant Δ = t² − 4, t = tr γ = 4C(u+B) − 2
(Δ = 16C²(B−u)² + 16Cp = 16C(C(u+B)² − (u+B)) because 4CuB − u − B = p). So (★) certificates are ambiguous forms of
Richaud–Degert discriminant t² − 4 representing −p, i.e. **fixed points of Gauss's class inversion** on the topograph —
exactly the role Zagier's τ-fixed points play. A Zagier/Legendre-type proof would need the *other* half: a finite set of
forms/rivers on which this inversion acts, plus a second involution σ with a computable fixed set.

**Main line.** Topograph/river structures attached to the certificate forms (cycle of F, its second ambiguous centre,
principal-class membership, period parity) are the natural source of a non-local weight w in Lemma P0. If such a
structure supported an index, some *river-weighted* certificate count would have a parity that is a function of p's
coarse data.

**KILL TEST KT1 (pre-registered before any computation).** For all primes p ≡ 1 (24), p ≤ 2·10⁵ (≈ 2 230 primes), compute
for every unordered (★) certificate and every unordered U₇ word a battery of river weights (≥ 8 bits: cycle length of F
mod 2, [F ~ principal], [second ambiguous centre of F's cycle has leading coefficient ≡ −1 mod 4C], [−F ~ F], period
of the regular CF of the fixed point mod 2, and their products), giving count vectors W_w(p) mod 2. **The main line is
DEAD if no GF(2) combination of the W_w(p), fitted on the primes ≤ 10⁵, predicts W(p) mod 2 = a function of
p mod 840 on the held-out primes in (10⁵, 2·10⁵] with agreement > 60 %, and no single W_w is constant on the primes
of any fixed class mod 840.** It is also DEAD if the only always-odd combinations are explained by a non-certificate
central point (the WINDMILL §3.5 pattern).

**KT2 (Legendre forced divisor; secondary).** For N_C = 4Cp + 1 (C ≤ 40), the reflection of the principal cycle of
discriminant N_C has a second centre which (when N(ε) = +1) is an ambiguous form giving a parity-forced divisor a_C | N_C.
Dead if the rate of a_C ≡ −1 (mod 4C) is within 3σ of the random-divisor baseline (no enrichment ⟹ the river forces a
divisor but not its class: B2 in river coordinates).

**Escape hatch to examine if KT1/KT2 kill:** (i) indices supported on U₇ / full Type II whose easy side carries the
quadratic character (fable-2 / astra-2 remnants); (ii) the Stokes form (d) with a p-dependent acyclic complex (HJ trie /
Farey complex), where the weights are filling-dependent and are not a fixed dictionary.

## 4. Computations

### 4.1 KT1 — river weights on certificate forms: **DEAD (per pre-registration)**

Run: `python3 scripts/z62_parity_river.py 200000 <extras>` → `data/z62/parity/kt1_river_2e5.tsv` (all 2 224 primes
p ≡ 1 (24) ≤ 2·10⁵, plus the 12 (★)-zeros < 3·10⁶, Z₇, 68 odd squares; 3.5 s). Columns: for each family STAR ((★),
unordered), U7 (unordered U₇ words), ALLX (all unordered words of X(p) = {tuv − u − v = p}) and each of 8 river
weights and their 28 pairwise products, the count W_w(p). Checks: 2·STAR_one = R(p) against brute force (4 random
primes, and the zeros), ALLX_one = brute-force unordered |X(n)| (11 values), U7_one = 0 exactly at squares and Z₇,
> 0 at all 12 (★)-zeros.
Analysis: `scripts/z62_parity_gf2.py` (GF(2) nullspace of [counts | class indicators mod 840], train p ≤ 10⁵ (1 187
primes), test (10⁵, 2·10⁵] (1 037)); `scripts/z62_parity_quot.py` quotients by per-word identities (distinct per-word
patterns: 16; per-word identity space: dim 95). **Prime-level nullspace dim 98 = 95 trivial + 3.** The 3 excess
identities all generalise (held-out agreement 1.000) and all live on ALLX; restricted to interior words
(t, u, v ≥ 2) every one of them is ≡ 0, the constant sits on boundary words and is explained exactly: e.g.
Σ_ALLX (1 + [t = 1] + hj) ≡ #{u = 1 words} + #{HJ-length-1 words} = τ(p + 1) + 3 ≡ 1 (the three length-1 words
(2, 1, p+1), (p+2, 1, 1), (1, 2, p+2) are not certificates for p ≡ 1 (4)). No identity involves STAR or U7 non-trivially,
and no single STAR/U7 column is constant per class except per-word-constant ones. **KT1 fires: main line dead.**

**Why (Lemma R, PROVED).** For a word (t, u, v) of n with σ = u + v, ε = σ mod 2, the substitution x ↦ x − ky,
k = ⌊(v−u)/2⌋, carries F = [t, t(v−u), −n] to G(t, σ) := [t, tε, σ − t(σ² − ε)/4] (compute: with m = v − u = 2k + ε,
c′ = −t(m² − ε)/4 − n and n = t(σ² − m²)/4 − σ). So **the topograph/river of a certificate form depends only on
(t, σ) = (4C, u + B), not on p** (p enters only through which (t, σ) occur); the cycle is that of the cyclic HJ word
(t, σ), of Gauss length 2 or 4 (CERTIFIED for all 26 761 words of primes ≡ 1 (24) < 5·10⁴: STAR always 4).
Every river weight is therefore a fixed function w(C, u + B) of the certificate — a fixed-feature dictionary in new
coordinates, which is exactly what WINDMILL §3 / board astra-3 already found sterile. The river of a form *attached to a
certificate* carries no non-local information; any topograph route must use a discriminant attached to p alone.

### 4.1′ Theorem R (sharp form of Lemma R; PROVED) — the modular geodesic of a certificate is the length-2 word (t, u+v)

**Theorem R.** Let n ≥ 1 and (t, u, v) ∈ ℕ³ with tuv − u − v = n, σ := u + v, tσ ≥ 5. Then
γ_w := [[tu − 1, n],[t, tv − 1]] ∈ SL₂(ℤ) is SL₂(ℤ)-conjugate to S(t)S(σ) = [[tσ − 1, −t],[σ, −1]]
(S(b) := [[b, −1],[1, 0]], the Hirzebruch–Jung letter). In particular the (★) matrix of (u, B, C) is conjugate to
S(4C)S(u+B), and the U₇ matrix of a word (r, x, y) to S(x)S(r+y).
*Proof.* For any binary form f = [a, b, c] of discriminant T² − 4 put γ_f := [[(T−b)/2, −c],[a, (T+b)/2]] ∈ SL₂(ℤ)
(its U = 1 automorph). For g ∈ SL₂(ℤ), γ_{f∘g} = g⁻¹ γ_f g (standard; also checked on 2 000 random (f, g)). Here
T = tσ − 2, γ_w = γ_{F_w} with F_w = [t, t(v−u), −n], and S(t)S(σ) = γ_Q with Q = [σ, −tσ, t]; so it suffices that
F_w and Q are properly equivalent. Lemma R gives F_w ∘ (x ↦ x − ky) = G := [t, tε, σ − t(σ² − ε)/4], and
Q ∘ ((x, y) ↦ (y, −x)) = [t, tσ, σ], which the same substitution with k = (σ − ε)/2 (the Lemma R computation with
m := σ, n replaced by 0·… i.e. c′ = t(k² − σk) + σ = σ − t(σ² − ε)/4) also carries to G. ∎
CERTIFIED cross-check: the reduced cycles of F_w and Q coincide for all 15 208 words of primes p ≡ 1 (24) < 3·10⁴ and
of 121, 225, 105, 1465, 4545.

**Corollary R′ (scoped no-go; PROVED).** Every SL₂(ℤ)-conjugacy invariant of the certificate matrix — trace, the
proper class and the whole river/topograph of its form, the closed modular geodesic and its length, the Rademacher
function / linking number with the trefoil (Ghys), cycle lengths, ambiguous centres, orbital integrals for SL₂(ℤ) —
is a fixed function of (t, u+v) = (4C, u+B), independent of p. Weights built from them are fixed-feature dictionaries
in (C, u+B) coordinates; the only p-dependence is *which* pairs (C, u+B) occur, i.e. (★) itself:
p = tuv − u − v ⟺ Q_{t,σ}(1, u) = −p, the value of the fixed form Q_{t,σ} at the vector (1, u) on the row of the
region of value t. **Not covered:** the conjugating element itself (the position of the certificate in the fixed
topograph), conjugacy in Γ(N) / Γ₁(N) for N depending on the certificate (the TRACE lane's Γ(4C) structure), and
relations *between* different certificates.

### 4.2 KT2 — Legendre's parity-forced divisor of N_C = 4Cp + 1: **DEAD (per pre-registration)**

`python3 scripts/z62_parity_legendre.py 30000 30` → `data/z62/parity/kt2_legendre_3e4_C30.txt` (385 primes p ≡ 1 (24)
≤ 3·10⁴, C ≤ 30). The principal cycle of discriminant N_C is reflection-symmetric; its second centre is an ambiguous form
(a parity-forced nontrivial divisor of N_C; 8 317 pairs (p, C)) or a symmetric form (N(ε) = −1; 3 233 pairs). The forced
divisor lies in the (★) class −1 (mod 4C) **483 times against a random-divisor baseline of 483.8 ± 21.3 (z = −0.04)**.
The parity mechanism forces *a* divisor, never its class: B2 in river coordinates (CERTIFIED for the stated range;
"never" = Assessment). 287/385 primes get a forced certificate at some C ≤ 30 — a lottery with one ticket per C, sparser
than (★) itself (377/385 have some (★) certificate with C ≤ 30).

## 5. Verdict
(to be filled)
