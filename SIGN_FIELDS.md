# SIGN_FIELDS — exponential near-squares, sign fields of other numerators, the non-genus layer (task O232, spark relay Z2)

Status: checkpoint 1 (O232), awaiting review. **ES is not solved here, nor any infinite case of it unless stated with a
complete proof.** Labels as in DISCOVERIES.md. Builds on NEAR_SQUARE_EXIST.md (O225, sign fields Σ_M = ℚ(ζ_M, √−M)),
NEAR_SQUARE.md ((J)55), EXPONENT_COVERING.md ((J)22: Thm 1.4 compactness criterion, ec_cover / ec_cert), DEDEKIND_ES
Thm 4.5 (five-slice sign table), FOUR_SPECIFIC ((J)46). Memos BRAINSTORM/z8_*.md, scripts `scripts/z8_*`, certificates
`data/z8/`.

## 1. Exponential near-squares n_s = c₀·4^s + k (goal 1, O225 spark S4)

Setting. n_s = c₀m² + k with m = 2^s. EXPONENT_COVERING Thm 1.4 applies verbatim with base b = 4 and additive constant
k (its proof is family-agnostic): a finite covering of {n_s : s ≥ s₀} by ET classes and divisor classes exists iff the
limit set Λ = {ν(μ) : μ ∈ Ẑ}, ν(μ)_2 = k, ν(μ)_q = c₀·4^μ + k (q odd), avoids the sterile set S′.

**Lemma 1.1 (which families are non-trivial; PROVED, elementary).** For s ≥ 2, n_s ≡ k (mod 8) and n_s ≡ c₀ + k (mod 3).
Unless k ≡ 1 (mod 8) and c₀ + k ≡ 1 (mod 3), every n_s with s ≥ 2 lies outside Mordell's six classes mod 840 that are
≡ 1 (mod 24), hence is ES-solvable by a fixed congruence identity. (Odd n ≢ 1 mod 8 or ≢ 1 mod 3: classical.)
So the interesting offsets are k ≡ 1 (8) with c₀ + k ≡ 1 (3); for c₀ = 1: k ≡ 9 (mod 24). Note Lemma 2.3 of NEAR_SQUARE:
Z_k^□ ≠ ∅ for all these k (k ≡ 1 mod 8), so **no finite set of polynomial families in m covers n = m² + k for all m**
(NEAR_SQUARE Thm 2.2); the question is whether the exponential subfamily m = 2^s escapes.

**Lemma 1.2 (no integer unit-square points; PROVED).** Let c₀ = 1 and k ≥ 3 odd. For ℓ ∈ ℤ, ν(ℓ) is never a profinite
unit square. *Proof.* ℓ ≥ 0: the odd components are the odd integer N = 4^ℓ + k ≥ 4; a square in every ℤ_q (q odd) and a
unit at every odd q forces N = s² with s a power of 2, i.e. N = 1: impossible. ℓ = −a < 0: components (1 + k·4^a)/4^a;
as before 1 + k4^a = s² with s a unit at all odd primes, s odd ⇒ s = 1: impossible. ∎
So the Cor 1.5 obstruction of (J)22 never occurs here; what remains are *non-unit* square points
(4^ℓ + k = s² or 1 + k4^a = s², covered by D_q for q | s but making coverings expensive, cf. EXPONENT_COVERING §4.3) and
the non-square sterile part of S′.

**Theorem 1.3 (PROVED, computer-assisted; certificates checked by ec_cert.py).** ES holds for every n = 4^s + k, s ≥ 0, for
k ∈ {9, 57, 81, 129, 153, 177, 201, 225, 249}. Certificates `data/z8/cert_c1_k*.json` (L ∈ {6, 24, 30}; 2–8 classes),
produced by `scripts/z8_expnear_cert.py` and checked by `ec_cert.main` (polynomial identity, integrality on the class,
positivity bound, periodicity M′ | 4^L − 1, exact verification for all s ≤ 600, brute force below s₀, T1 control).
Of these, k = 57, 153, 177, 225 have members in Mordell's hard classes mod 840 (s ≡ 3 mod 6: n ≡ 121; s ≡ 2 mod 6:
n ≡ 169; s ≡ 5 mod 6: n ≡ 361; s ≡ 0 mod 3: n ≡ 121, 289), the others are covered by mod-840-type classes. (R235 repair) For k ∈ {9, 81, 129, 201, 249} no member with s ≥ 2 lies
in Mordell's six classes, so those five cases are already Mordell's theorem; for k = 153 (and k = 225, s ≡ 3 mod 6) the
hard members are multiples of 13 (17): divisor classes. The genuinely new coverings are k = 57 (s ≡ 9 mod 30), k = 177
(s ≡ 5 mod 6) and k = 225 (s ≡ 0 mod 6, s ≡ 9, 21 mod 24). These are
*near-square* infinite families n = m² + k on which polynomial families in m provably cannot cover (Z_k^□ ≠ ∅):
the exponential coupling of EXPONENT_COVERING Prop 2.2 is what makes them coverable.
Survey (`scripts/z8_expnear_survey.py 1 300 30000 6 12 18 30 36 60`; EVIDENCE): of the 13 non-trivial k ≤ 300, 9 are
covered (above; 225 needs L = 24), 4 are OPEN at the search limits: k = 33, 105, 273, 297.

**1.4 The OPEN offsets (EVIDENCE + PROVED pieces).** Integer *non-unit* square points: k = 33: 4² + 33 = 7², 4⁴ + 33 = 17²,
1 + 33·4² = 23²; k = 105: 4² + 105 = 11², 4³ + 105 = 13², 4⁴ + 105 = 19², 1 + 105·4² = 41²; k = 273: 4² + 273 = 17², 4⁴ + 273 = 23² (R235 repair);
k = 297: 4³ + 297 = 19². (Same pattern as (J)22 §4.2: every OPEN k has an integer square point.)
* **k = 105 is the "maximally hard" offset** (PROVED, trivial): 105 = 3·5·7 ≡ 1 (mod 8), so n_s ≡ (2^s)² (mod 105) and
  n_s ≡ 1 (mod 8): **every** member lies in one of Mordell's six hard classes mod 840 (all six occur), and n_s is a square
  modulo every prime of k — the near-square T1-mimicking at the primes of the offset.
* Unit-square screen (`scripts/z8_expnear_screen.py 1 105 3000000 … 360 …`, CERTIFIED finite computation): at L = 360
  every residue s mod 360 has n_s ≡ 0 or a non-residue modulo some prime q < 3·10⁶ with ord_q(4) | 360. Hence
  **Λ₁₀₅ ∩ Sq^× = ∅** (the square half (EH) of (J)22's criterion holds); only the non-square part of S′ can obstruct.
  (k = 33: the screen leaves exactly s ≡ −2 (mod L) for L = 180, 360, 720 (R235 repair: at L = 60, 120 also the mixed
point s ≡ 34 mod 60 survives, killed once 9 | L) — the point μ = −2, n = 23²/16, a non-unit square,
  killed by D₂₃ only when 11 | L.)
* The obstruction is the *class supply*, at **mixed points**: the general search leaves s ≡ 124 (mod 360), and refines
  to s ≡ 844 (mod 2520). These exponents are the CRT gluing μ* = "4 in every ℓ-adic component except ℓ = 3, where
  μ* = −2" (`scripts/z8_point.py`): at primes q with 3 ∤ ord_q(4), n ≡ 4⁴ + 105 = 19²; at q with ord_q(4) ∈ {3^b, 2·3^b} (R235 repair),
  n ≡ 4⁻² + 105 = (41/4)²; only at q whose order mixes 3 with another prime is n_q generic (non-residue at q = 181,
  ord 90, but no ET class of admissible modulus ≤ 2·10⁶ hits it). The point μ* itself lies in the II2 class
  (2, 23, 919) (ord_919(4) = 153), so μ* is NOT sterile; but its neighbours with other 17-adic components are again
  uncovered (L = 42840). An adaptive "lifting" covering (`scripts/z8_adaptive.py`, ordered class lists, independent
  replay checker `scripts/z8_cert_tree.py`) drives the uncovered Haar measure of the exponent space down
  monotonically — 8.3·10⁻³ (L = 360) → 1.2·10⁻³ (75 600) → 7·10⁻⁴ (982 800) → 8·10⁻⁵ (1.7·10⁷) → 3·10⁻⁶ (2.3·10⁸)
  → 8.5·10⁻⁸ (4.0·10¹², 89 classes, 342 114 uncovered residues) — after which the greedy stalled (no class with
  M ≤ 10⁵ within its period-growth caps). EVIDENCE (weak) that k = 105 is coverable at very large cost; not a certificate.
* Assessment. Mixed points are the exponential analogue of (J)22 §4.3's near-square points: an exponent that imitates
  *different* integer square points in different ℓ-adic components of Ẑ. They are where coverings get expensive;
  whether some mixed point is sterile (which would make "all 4^s + 105" uncoverable) is open. No mixed point found so far
  is sterile.

## 2. Sign fields for numerators ν (goal 2, O225 spark S2)

Words w = (t, u, v), tuv − u − v = n, A = tu − 1, A* = tv − 1 (NEAR_SQUARE_EXIST notation). A **ν-word** is a word with
ν dividing one of t, u, v, A, A*; each gives an explicit decomposition of ν/n (PROVED, direct expansion):
ν | u = νw: ν/n = 1/(wA*) + 1/(tnw) + 1/(tnwA*); ν | A = νw: ν/n = 1/(wv) + 1/(wvA*) + 1/(nwA*) (v, A* ↔ u, A for the
mirror slots; ν | t via (J)32). Exact check: `scripts/z8_numerators.py` (all words of primes < 2000 and odd squares < 3600,
ν ∈ {3, 4, 5, 7, 8, 11, 12}; every u/v/A/A* slot verified in exact rationals). For ν = 4 and n ≡ 1 (mod 4), DEDEKIND_ES
Thm 4.5 says: 4-word ⟺ χ(w) = (A/n) = −1.

Level u (u-side): A | n + u, A ≡ −1 (mod u); t = (A + 1)/u, v = (n + u)/A. Let σ_A ∈ Gal(ℚ(ζ_{νu})/ℚ) be the Artin symbol
(A coprime to νu), c the complex conjugation, and Σ_{ν,u} := ℚ(ζ_{νu}, √−u) (the *ν-sign field*; Σ_{4,u} ⊇ O225's Σ_u).

**Prop 2.1 (Frobenius form of the ν-slots; PROVED, elementary).** Let gcd(ν, u) = gcd(ν, n) = 1, ν ∤ n + u, and A coprime
to ν. Then w is a ν-word ⟺ σ_A|ℚ(ζ_{νu}) ∈ C_ν(n, u) := {σ : σ|ℚ(ζ_u) = c, σ|ℚ(ζ_ν) ∈ {−1, −(n + u)/n}}; the class −1
is the slot ν | t (σ_A = c on all of ℚ(ζ_{νu})), the class −(n + u)/n is the slot ν | A*.
*Proof.* ν | A and ν | u are excluded; ν | v ⟹ ν | Av = n + u, excluded. tu = A + 1 with u invertible mod ν gives
ν | t ⟺ A ≡ −1 (mod ν), i.e. (with A ≡ −1 mod u) A ≡ −1 (mod νu). ν | tv − 1 ⟺ (A + 1)(n + u) ≡ uA (mod ν) ⟺ An ≡ −(n + u). ∎
(The script asserts this classification on every coprime word of the test range: 0 failures.)

**Theorem 2.2 (T1 as a containment; PROVED).** Let n = m² be an odd square, gcd(m, u) = 1, so every odd prime r | m² + u
splits in ℚ(√−u) and every odd A at level u with gcd(A, ν) = 1 (R235 repair) has σ_A ∈ Gal(Σ_{ν,u}/ℚ(√−u)).
(For ν odd, √−u ∈ ℚ(ζ_{νu}) ⟺ √−u ∈ ℚ(ζ_u), and then the whole level is empty for odd A, not just the t-slot: χ_{−u}(A) =
χ_{−u}(−1) = −1 for A ≡ −1 mod u. R235.)
(a) If √−u ∈ ℚ(ζ_{νu}), no odd A at level u lies in the t-slot class (σ_A = c on ℚ(ζ_{νu}) would move √−u).
(b) √−u ∈ ℚ(ζ_{νu}) for every u ≥ 1 ⟺ 4 | ν. (⇐: disc ℚ(√−u) divides 4u. ⇒: u = 1 needs i ∈ ℚ(ζ_ν).)
(c) If √−u ∉ ℚ(ζ_{νu}) (e.g. ν odd, u = 1), Chebotarev in Σ_{ν,u} gives primes r ≡ −1 (mod νu) split in ℚ(√−u); for
every odd m with r | m² + u and m² + u ≥ r, A = r is a t-slot ν-word of m² (v = (m² + u)/r): T1 fails at this level.
So **"full T1 ⟺ 4 | ν" ((J)46 SHARP 2) is, on the t-slots (odd A coprime to ν; R235 repair: the other slots and even A
are not re-derived here), the statement ℚ(i) ⊂ ℚ(ζ_ν)**: for 4 | ν every sign field
Σ_{ν,u} collapses to the cyclotomic field ℚ(ζ_{νu}), and c is forbidden at squares.
(d) **Uniqueness of 4 (PROVED).** Let 4 | ν, u ≡ 1 (mod 4) prime to ν, n ≡ 1 (mod 4) (so √−u ∉ ℚ(ζ_u): the c-fibre is
split half/half by √−u). (R235 repair: the former parenthetical on u ≡ 3 (mod 4) was wrong. There 4 | n + u, Prop 2.1 does
not apply for ν = 4, and the v-slot opens: v₂(v) = v₂(n + u) ≥ 2 for odd A, so every odd-A word at level u ≡ 3 (4) is a
4-word, and by reciprocity has χ = −1; the whole c-fibre is both the 4-slot set and the forbidden set. So for ν = 4 the
coincidence holds at every odd u (= DEDEKIND Thm 4.5); for other 4 | ν at u ≡ 3 (4) it is not analysed.) The class
−(n + u)/n ≡ −(1 + u) ≡ 2 (mod 4) is not a unit, so the coprime part of C_ν is the single class σ = c on ℚ(ζ_{νu}), of relative size 1/φ(ν) in the c-fibre
over ℚ(ζ_u); the T1-forbidden part {σ(√−u) = −√−u} has relative size 1/2. They coincide iff φ(ν) = 2, i.e. ν = 4.
**For ν = 4 the word condition is exactly the sign condition σ_A = c on Σ_u = ℚ(ζ_u, √−u) (O225); for every other
T1-numerator (8, 12, 16, …) it is a proper Chebotarev subset of the forbidden half, cut out by the extra field
ℚ(ζ_{νu}) ⊋ Σ_u that no genus/T1 mechanism controls.**
Numerics (EVIDENCE, `scripts/z8_numerators.py 2000 60 3 4 5 7 8 11 12`): ν-words at odd squares 3² … 59²: 0 for
ν = 4, 8, 12; for ν = 3, 5, 7, 11 many, and every coprime odd-A violator has √−u ∉ ℚ(ζ_{νu}) as (a)/(c) predict (the
coprime violators with √−u ∈ ℚ(ζ_{νu}) all have A even — O225's Remark 2.4 caveat, (a) is for odd A).
**The failures.** 8/131: of the 21 words of 131, 14 carry a 4-slot (R235 repair: 131 ≡ 3 mod 4, so these are the words with (A/131) = +1,
i.e. (−A/131) = −1; (d) and DEDEKIND Thm 4.5 are for n ≡ 1 mod 4; R235 counts 22 words (t, u ≤ v) for 131 and 16 for 241 — the word convention behind 21 / 15 should be stated) and every such slot is ≡ 4 (mod 8) —
all forbidden-half Frobenii land in the complementary ℚ(ζ_{8u})-class; same at 8/241 (6 words with a 4-slot, all
≡ 4 mod 8). 11/37: none of the 9 words of 37 has an 11-slot (11 is odd: no containment, T1 fails, and 37 is a
lottery miss). Assessment: the sign-field picture makes 4's special status *visible* (it is the unique numerator whose
slot set is a full quadratic-character half, so genus theory — T1 — and the word condition are the same thing) but
does not make ES easier: the χ = −1 half is still reached by a Frobenius lottery (B2).

## 3. The non-genus layer (goal 3, O225 spark S1)

Layers at a level u for p (A odd): genus-clean (an imaginary quadratic F ⊂ Σ_u splits every odd r | p + u; O225)
⊂ *group-clean* (c ∉ ⟨σ_r : r | p + u⟩ ⊂ G = Gal(Σ_u/ℚ)) ⊂ clean (no divisor A of p + u with σ_A = c). Genus-clean ⟺
c ∉ ⟨σ_r⟩·G² (a quadratic character separates); S1 asked whether depletion sits in ⟨σ_r⟩G² \ ⟨σ_r⟩ ("Rédei layer").

**Prop 3.1 (PROVED, elementary).** Whether level u carries a χ = −1 word of p (A odd) is a function of the multiset of pairs
(σ_r, v_r(p + u)) over the odd primes r ∤ u of p + u, and σ_r depends only on r mod 4u. In particular it involves no
Frobenius in any non-abelian extension of ℚ: Rédei symbols / 4-rank data of F = ℚ(√−(k + u)) (Frobenii in dihedral
degree-8 fields) do not enter the decision function (R235 repair: they can constrain its *input* — which r divide
p + u in a family is governed by ring-class-field Frobenii — and that this adds nothing beyond genus is the Assessment below).
*Proof.* A = ∏ r^{a_r}, 0 ≤ a_r ≤ v_r; admissibility and χ are σ_A = ∏σ_r^{a_r} = c (O225 (i)–(ii)); Σ_u ⊂ ℚ(ζ_{4u}). ∎
**Consequence (Assessment, not a theorem).** On p = m² + k, the only constraints on that multiset that hold for *all*
m in a congruence class are (i) every σ_r lies in the image H_F of Gal(Σ_uF/F) (r splits in F; O225 genus layer) and
(ii) ∏σ_r^{v_r} = σ_{p+u}, a congruence function of m. By O225 Lemma 4.2 such constraints force "c absent from all
sub-products" only when c ∉ H_F, i.e. genus-cleanness. A *forced* Rédei layer would need a level field that is not
abelian over ℚ (H-D); sign fields are abelian, so the residual near-square depletion of R225/O225 §3 is not a forcing
statement at any single level — it can only be a statistical shading of the lottery (or a multi-level correlation).
NOT DONE: the numerical test of whether group-clean-not-genus levels are enriched at small K0 (the infrastructure is
`scripts/z2_hardness.c`; adding the group-clean flag is a ~30-line change; left as spark).

## 4. Chebotarev-in-a-family levels (goal 4)

Attempt (construction-first). Choose the level from p: u = u(p) with F_{K(p)} ⊄ Σ_{u(p)} (always possible: e.g. any u
with k + u having an odd prime factor ∤ u, Cor 2.3 of O225), so Chebotarev supplies a positive density of primes r with
σ_r = c and r split in F. To get a word we need such an r (or a product) **dividing p + u**. For a prime A = r:
r | p + u and r ≡ −1 (mod u) ⟺ u ≡ −p (mod r) and u | r + 1; with u < r this is u = r − (p mod r) and u | r + 1, i.e.
**p mod r ∈ {r − d : d | r + 1, (−d/r) = −1}** — a congruence condition on p per prime r. (Iteration log.)
(F1) bounded r ≤ R: a finite congruence covering — B1 (fails on Z_k^□ / T1-type classes; O225 §4.4 E4 is this sieve).
(F2) bounded A (composite): the same with A | p + u for A ≤ R: a fixed finite slice set — B2 Thm 2.2 (fails i.o. under H).
(F3) u(p) chosen *first*, then "some A | p + u(p) with σ_A = c": the divisor lottery at one integer — B2/B3; the
     disjointness F ⊄ Σ only guarantees the target class is non-empty, not hit.
(F4) violate "one level": run over all u ≤ U(p) and use the multiplicativity across levels (p + u for consecutive u are
     coprime-ish) — this is the averaged count Σ_u #{A}, main term ≍ log³p with no pointwise lower bound (B3/B6).
**Verdict (Assessment).** Every version stops at B2 (bounded divisors ⇒ fixed slice menu) or B3 (growing divisors ⇒
main-term certificate with uncontrolled error). Linear disjointness of Σ_{M(p)} and F(p) is cheap and never the issue; the
issue is that Chebotarev counts primes, while a word needs a *divisor of one specific integer*.
