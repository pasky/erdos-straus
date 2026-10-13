# DETERMINISTIC_EXISTENCE — deterministic existence mechanisms in number theory, mapped onto ES (O168, SPARK)

Labels as in DISCOVERIES.md. **ES is not solved here.** Notation: ES(n) = positive solution of 4/n = 1/x+1/y+1/z;
Type I / II and the e-slice form as in the brief: −1 ∈ Σ_e(N) = {ab⁻¹ mod e : ab | N}, N = (p+e)/4 (II) or
(pe+1)/4 (I); divisor form tp+1 = m·m'', m ≡ m'' ≡ −1 (t), 4 | m. Barriers B1–B6, T1 as in STATUS.md.

Status of this file: §1 catalogue (Assessment); §2 selection; §3– attacks (labels per item).

## 1. Catalogue

Columns: **shape** = what the mechanism proves; **ES-shape** = the closest ES-shaped statement it could prove;
**fails at** = the exact step and the barrier it maps to; **evade?** = whether the failing step is a proved
barrier (✗), an unproved technical obstacle (?), or open (○). All entries are Assessment unless a theorem is cited.

| # | mechanism | shape | ES-shape | fails at | evade? |
|---|---|---|---|---|---|
| 1 | Thue's lemma / Dirichlet pigeonhole | x ≡ ay (mod q) has 0<\|x\|,\|y\|≤√q; with a = √−1 mod p and the *definite* form x²+y², "small and ≡ 0 (p) ⇒ = p" | small (a,b) with a ≡ −b·r (mod e) inside an e-slice | the *definite-form* step: ES's quadratic pieces are split (TERNARY Comp 6.1; notes §77), small values of split forms carry no information; collisions give *signed* solutions (LONGSHOT_PIGEONHOLE) — B2/B4 | ✗ for split targets; ? if a definite form whose small values are ES certificates existed (none known; §3) |
| 2 | Minkowski convex body / 2nd theorem, LLL | short vectors in lattices of covolume V in boxes of volume 2ⁿV | lattice {(a,b): a ≡ −b (e)} meets a box; or lattices from √−d mod f | "ab \| N" is not a convex/lattice condition; the lattice depends on the unknown divisor (prob_lll_fixed_p, gon_lll) — B2 | ✗ |
| 3 | Lagrange/Euler/Fermat descent | compose relaxed solutions mp = N(α), lower m | relaxed ES at mp, or quaternion norms (2ai+j)(2bi−j) = −e(1+2ck) | no composition law preserving the ES *shape* (noncounting_shapes §3c); toric composition = units — B2 | ✗ |
| 4 | **Legendre's theorem + Holzer** (rank-3 local–global for isotropy; small zero \|z\| ≤ √\|ab\|) | aX²+bY² = cZ² solvable ⇔ three QR conditions; a zero with \|Z\| ≤ √\|ab\| | ES as isotropy of F_{p,θ} with integrality forced by size | §3: ES's ternary pieces are isotropic (trivial zeros); the anisotropic conics attached to ES are the *obstruction* conics (Type I level d needs X²+dY²−pZ² anisotropic at p); Holzer-forced integrality yields only norm/genus statements — B1/B5 | §3 (precise theorem) |
| 5 | Hasse–Minkowski (all ranks) | rational zeros from local zeros | rational ES points | rational ES points are trivial (S_p is Q-rational); the content is integrality = integral HP = ES itself (GEOMETRY_ES §1) | ✗ (tautological) |
| 6 | Davenport–Cassels / Aubry rounding | Euclidean quadric: rational rep ⇒ integral rep | rational point of a quadric piece ⇒ integral ES point | side conditions with point-dependent moduli (4ad \| f+p) are destroyed by the rounding move; q(error) = 0 on isotropic pieces (rational_to_integral M3 + errata) | ○ (errata: positivity-preserving descent not excluded; §5) |
| 7 | Gauss genus theory; ambiguous classes ⇔ factorisations of Δ | genus of p ⇔ characters; 2^{t−1} ambiguous classes | "p (or N_θ(p)) represented by the right genus" | genus = congruence data on p (B1, Thm 2.2(ii) of redteam-2); square classes pass every genus test (B5); ambiguous forms factor Δ, not N_θ(p) | ✗ for fixed Δ; § 4 for Δ = Δ(N_θ) |
| 8 | Rédei 4-rank / Rédei symbols | existence of D = D₁D₂ "of the second kind" from a Legendre-symbol matrix | e-slice at e \| 24 is a quadratic-character condition on the divisors of N | e \| 24 slices are the Mordell coverings: lottery on whether N has a prime factor in a class — B2; needs factorisation of N | ✗ |
| 9 | **Legendre's Pell-factor argument** (negative Pell for prime p ≡ 1 (4); x²−py² = ±2 for p ≡ 3 (8)/7 (8)) | the fundamental unit factors Dy² = (x−1)(x+1); primality of D leaves only trivial splittings, minimality kills them | a unit of Q(√θ(p)) factors some N_θ(p) into an ES pair | §4: uses primality (T1-safe); the factorisation produced is of the *discriminant*, not of N_θ(p) | ? (§4) |
| 10 | Dirichlet unit theorem / CF periodicity | units exist | units as "universal divisors" (other_rings Prop 3.3) | ℤ^× = {±1}: only (1,1), i.e. p ≡ 3 (4); units of auxiliary rings act on the wrong integers | ? (§4) |
| 11 | Zagier/Heath-Brown involutions, parity | \|X\| odd ⇒ a fixed point of a second involution exists | X(p) = {(t,u,v): (tu−1)(tv−1) = tp+1} odd (O152) | T1 kills on square classes; finite affine menus barred conditionally (INVOLUTION_ES2 Thm 5.1/6.1) — B5 | ○ infinite/non-affine menus |
| 12 | Brouwer / Lefschetz / Sperner / Borsuk–Ulam | fixed points from degree/parity | (invol_topological) | discrete analogues are parity counts (#11) — B5 | ✗ |
| 13 | Chevalley–Warning, Ax–Katz, Combinatorial Nullstellensatz | zeros mod p of low-degree systems | zero-sums in (ℤ/e)^× ⇒ ab⁻¹ ≡ +1 | certifies the identity (signed ES); −1 needs full ratio-set coverage (polynomial_method) — B1/B4 | ✗ |
| 14 | EGZ / Davenport constant / Cauchy–Davenport / Kneser | long sequences have zero-sum subsequences; sumsets grow | products of the prime factors of N cover (ℤ/e)^× ∋ −1 | needs ω(N) ≫ log e prime factors in (ℤ/e)^×; covering by small prime factors fails for a positive proportion of p in every slice (LONGSHOT_PIGEONHOLE Thm 2.2) — B4 | ✗ |
| 15 | Hall marriage / Kőnig / max-flow | SDR exists if \|N(S)\| ≥ \|S\| | matching between slices and divisor pairs | ES needs *one* edge; Hall's condition already presupposes neighbourhood lower bounds (counting) — B3/B6 | ✗ (adds nothing) |
| 16 | CFT existence / Chebotarev; "p represented by some form of disc D ⇔ (D/p) = 1" | representation by the genus/some class (deterministic), by a given class (density) | p = Q(u,v) families | fixed families miss i.o. every square class (POINTWISE_BINARYFORM Thm 3.2); "some form" is congruence data; given class is an Artin symbol (lottery) — B1/B5 | ○ growing D (H-A) |
| 17 | Linnik/Duke equidistribution, Heegner points, Kloosterman / Kuznetsov | power-saving counts on homogeneous spaces | Type I/II as Heegner points on tubes of width 1/p | scale constraint: targets ≍ p^{−1}, main term ≤ p^{o(1)} (CONDITIONAL_ES Prop 2.3, Cor 4.1) — B3 | ✗ (pointwise) |
| 18 | Strong approximation (Spin, explicit ranges) | integral points in all congruence classes, for norms ≥ explicit bound | X_d : ef − 4da² = 1 with 4ad \| f+1 (GEOMETRY_ES) | side condition not mild; ranges power-size — B3/H5 | ○ H5 |
| 19 | Siegel's lemma | small solutions of underdetermined linear systems | linear constraints on (a,b,c,…) | ES constraint is multiplicative (divisibility) — B2 | ✗ |
| 20 | Thue–Siegel–Roth, Baker, Schmidt subspace, S-unit equations, Faltings, Hilbert irreducibility | finiteness / upper bounds / generic irreducibility | a+b = ec with ab \| N (S-unit-shaped) | wrong direction: these bound or exclude, never produce, solutions | ✗ |
| 21 | Burgess / Vinogradov / Pólya–Vinogradov | pointwise small non-residues via character sums | "some small slice works" | ES is not a statement about one character; the character expansion uses each χ once (CONDITIONAL_ES §3.2) — B3 | ✗ |
| 22 | Linnik's least prime in AP | prime ≡ a (q) below q^L | prime divisor b ≡ −1 (e) of (p+e)/4 | primes in [1,X] ≠ divisors of a specific N; reduces to a congruence covering — B1 | ✗ |
| 23 | Croot / Bloom unit-fraction density & colouring | dense or monochromatic sets contain S with Σ 1/x = 1 | 3-term 4/p | number of terms unbounded (Fourier on smooth numbers); 3 terms is the lottery (addcomb_unit_fraction_density) | ✗ |
| 24 | Greedy / Fibonacci–Sylvester, Erdős–Graham | Egyptian fractions exist deterministically | 3 terms | unbounded length (greedy_algorithm_dynamics) | ✗ |
| 25 | Euclid-type proofs of Dirichlet (Schur, M. R. Murty) | if N ≡ a (k) with a² ≡ 1, some prime factor of N lies in a non-trivial class | divisor ≡ −1 (e) of N from N's residue | "congruence-forced divisors" = B1 (other_rings, LONGSHOT_PIGEONHOLE) | ✗ |
| 26 | Weil / Lang–Weil / Deligne | F_q-points of varieties | ES mod q | local solubility is trivial; integrality needed — B1 | ✗ |
| 27 | Polynomial method (Dvir, Croot–Lev–Pach) | sets avoiding a pattern are small | Σ_e(N) ∌ −1 ⇒ τ(N) small | divisor sets already have polylog size, far below any CLP bound — B4 | ✗ |
| 28 | Compactness / overspill / minimal counterexample | — | p ∉ K ⊂ Ẑ | primes accumulate on (Ẑ^×)² ⊆ K (noncounting_shapes Props 1–3) — B1/B5 | ✗ (as displayed) |
| 29 | Gauss's 3-squares / class-number-one ternary genera | n = Q(x) for genus with one class | p-linear quantity represented by a ternary form | fixed recipes reduce to finite Mordell coverings (TERNARY Thm 4.1) — B1 | ○ growing parameters |

Remarks on the table.
* Rows 1, 4, 6, 9, 10 are the only rows whose failing step is not a proved barrier theorem *as stated*. Rows 1
  and 6 fail at a concrete structural fact (ES has no definite/anisotropic quadratic piece; side conditions with
  moving moduli); rows 4 and 9–10 are attacked below. Row 11 is open but was studied in depth (INVOLUTION_ES2).
* Every mechanism that *uses primality of p in an essential way* is automatically T1-safe at the first step:
  rows 1 (p | x²+y², 0 < x²+y² < 2p), 4 (Legendre condition at p), 9 (D = p prime has only trivial splittings).
  Everything else on the list sees p only through congruences or sizes, and B1/B5 apply.

## 2. Selection

The failing step of rows 4 (Legendre/Holzer), 9–10 (Pell/units) and 6 (Davenport–Cassels/Aubry) is not a proved
barrier theorem as stated, and rows 4 and 9 use primality of p in an essential way (T1-safe first step). These
three are attacked in §3 (row 4), §4 (rows 9–10), §5 (row 6).

## 3. Legendre / Holzer: is ES an isotropy problem?

### 3.1 The Fermat–Holzer template (classical)
Legendre: for squarefree, pairwise coprime a, b, c > 0, aX² + bY² = cZ² has a non-trivial integer zero iff −ab is a
square mod c, bc... (the three QR conditions). Holzer (Mordell's form): then there is a zero with
|X| ≤ √(bc), |Y| ≤ √(ac), |Z| ≤ √(ab). If ab ≤ 3 this forces |Z| = 1 (Z = 0 is impossible by definiteness), so
c = aX² + bY²: with (a,b) = (1,1), (1,2), (1,3) this is Fermat's two-squares theorem and its x²+2y², x²+3y²
analogues. In general Holzer only gives cZ² = aX² + bY² with Z² ≤ ab, i.e. *representation by the genus*.
**Two ingredients make the template work: a definite (anisotropic) form, and a size bound small enough to force
the "denominator" Z to be 1.** We now check both against ES.

### 3.2 What isotropy can know (PROVED; Legendre restated)
**Prop 3.1.** Let F_θ = a X² + b Y² − c Z² with a, b, c ∈ ℤ depending on p and a parameter θ (reduce to the
squarefree, pairwise coprime case in the standard way). Then "F_θ is isotropic" is equivalent to finitely many
quadratic-residue conditions: at primes ℓ dividing p-free coefficients they are congruence conditions on p mod ℓ
(B1 data); at primes ℓ | c(p,θ) they say "−ab is a square mod ℓ for every ℓ | c(p,θ)", i.e. a Hasse-norm
condition on the **factorisation** of the specific integer c(p,θ). ∎
So isotropy carries exactly two kinds of information: congruences of p, and a *splitting condition on all prime
factors* of a p-dependent integer. The second is strictly stronger than the ES-type condition "has one divisor
in a class" (B2), and of the opposite logical shape (∀ prime factors vs ∃ divisor). §3.3 shows the shapes match
exactly — but on the **failure** side.

### 3.3 Anisotropic conics in ES sit on the obstruction side (PROVED, elementary)
**Prop 3.2 (Type I needs an anisotropic conic).** If p ∤ 2cd and f | p² + 4c²d with f ≡ −p (mod 4cd), then
χ_{−4d}(p) = −1; equivalently the conic C_{d,p}: X² + dY² = pZ² is anisotropic over ℚ_p (hence over ℚ).
*Proof.* f is odd and coprime to dp. For every prime ℓ | f, −d ≡ (p/(2c))² (mod ℓ), so χ_{−4d}(ℓ) = 1; hence
χ_{−4d}(f) = 1. As f ≡ −p (mod 4d) and χ_{−4d} is odd, χ_{−4d}(p) = −χ_{−4d}(f) = −1. Then −d is a non-residue
mod p, and X² + dY² ≡ 0 (p) forces p | X, Y, then p | Z: no primitive ℚ_p-zero. ∎
(This is the Bright–Loughran/genus statement (I)7 in conic language.) **So every Type I solution of level d lives
on a conic X² + dY² = pZ² that has no rational point.** Legendre's theorem — whose content is "local ⇒ a point
exists" — is used by ES in the contrapositive direction only.

**Prop 3.3 (slice failure is a norm/isotropy condition; PROVED, elementary).** Fix e and N coprime to e; let
H_e(N) = ⟨ℓ mod e : ℓ | N prime⟩ ≤ (ℤ/e)^×. Then Σ_e(N) ⊆ H_e(N), and
(a) −1 ∉ H_e(N) ⇔ there is an odd character χ mod e with χ(ℓ) = 1 for all primes ℓ | N ⇔ every prime factor of N
splits completely in some imaginary cyclic subfield K_χ ⊂ ℚ(ζ_e);
(b) if (ℤ/e)^× is an elementary 2-group (e | 24), then Σ_e(N) = H_e(N), so the e-slice fails ⇔ (a) holds. For the
only such slice available at p ≡ 1 (4), e = 3: the slice fails ⇔ every prime factor of N is ≡ 1 (mod 3) ⇔ N is
primitively represented by X² + XY + Y² (class number 1).
*Proof.* (a) is duality for finite abelian groups. (b): in an elementary 2-group ab⁻¹ = ab, and H_e(N) is the set
of classes of divisors of N (squares are trivial), so a·1 with a | N realises every element. ∎
Thus the e | 24 Mordell slices fail **exactly** when a quadratic norm-form representation exists (an isotropy
statement, decidable by Legendre/Holzer); for general e the *group-level* part of the failure is an
"all primes split in K_χ" condition (Hasse norm theorem for cyclic K_χ).

### 3.4 The T1-safe deterministic residue: Jacobi forcing (PROVED + EVIDENCE)
**Prop 3.4.** Let p be prime and e ≡ 3 (mod 4) prime with (p/e) = −1, N_e = (p+e)/4. Then −1 ∈ H_e(N_e): N_e has
a prime factor ℓ with (ℓ/e) = −1, and −1 is a power of ℓ mod e.
*Proof.* (N_e/e) = (4⁻¹p/e) = (p/e) = −1, so some ℓ | N_e has (ℓ/e) = −1; ℓ has even order in the cyclic group
(ℤ/e)^× of order 2·odd, so −1 ∈ ⟨ℓ⟩. ∎
*T1:* for n = m², (N_e/e) = (m²/e) = +1 — Prop 3.4 never fires, consistent with ET Prop 1.6. For Type I slices,
(N'_e/e) = ((pe+1)/4 / e) = +1 always: Jacobi gives nothing there.
EVIDENCE (`scripts/de_jacobi_slices.py 200000 200`; p ≡ 1 (24), p < 2·10⁵, primes e ≡ 3 (4), e < 200):

| (p/e) | slices | −1 ∈ H_e(N_e) | −1 ∈ Σ_e(N_e) (slice solves) |
|---|---|---|---|
| +1 | 27127 | 0.4145 | 0.1688 |
| −1 | 25961 | 1.0000 (forced) | 0.3728 |

So Jacobi forcing removes the whole group-level obstruction and doubles the slice success rate — but 63% of forced
slices still fail: the residue is "−1 ∈ ⟨ℓ⟩ but ℓ^{ord(ℓ)/2} ∤ N and no other combination of N's prime factors
lands on −1", the multiplicity lottery (B4; LONGSHOT_PIGEONHOLE Thm 2.2 covers covering-by-prime-factors
certificates).
