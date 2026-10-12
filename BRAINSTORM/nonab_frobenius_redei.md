# Brainstorm O147(a): non-abelian Frobenius, Rédei symbols, arithmetic topology

Status labels as in DISCOVERIES.md. ES is not solved; nothing here proves any case of it.
Script: `scripts/bs_nonab_frob.py`; log: `logs/bs_nonab_frob_4e6.txt`.

## 1. Idea

Hatch H-D asks for data that congruences do not determine. For a prime p, the natural such data are:
* Frob_p in a fixed non-abelian Galois K/ℚ: dihedral ring class fields (p = x² + 32y², i.e. 8 | h(−4p)
  by Barrucand–Cohn), Kummer fields (2 a quartic residue: Frob in ℚ(i, 2^{1/4}); 2 a cubic residue:
  Frob in ℚ(ζ₃, 2^{1/3}));
* Rédei symbols [a, b, p] and the 4-/8-ranks of Cl(ℚ(√−p)), Cl(ℚ(√−dp)), the FIMR "spin" of prime ideals.
  In Morishita's dictionary these are the triple (Milnor) linking numbers of the knot p with two fixed knots.

What would have to be true. Some ES-relevant event at p (non-emptiness of a slice, the genus/divisor
conditions of Type I/II, square-class hardness) would have to depend on such a symbol, *beyond* its
abelian shadow. Then either (i) a "non-abelian covering" (finitely many Chebotarev classes, each with its
own witness recipe) proves ES, or (ii) higher linking explains the square-class hardness.

## 2. Literature anchor

* Morishita, *Knots and Primes* (Springer Universitext 2012). Legendre symbol = linking number mod 2;
  Rédei triple symbol = mod-2 Milnor μ(123). From memory, unverified page refs.
* Rédei 1939 (J. reine angew. Math. 180), the triple symbol. Stevenhagen, "Rédei reciprocity, governing
  fields and negative Pell" (Math. Proc. Camb. Phil. Soc. 2022, arXiv:1806.06250). Koymans–Pagano,
  "On the distribution of Cl(K)[ℓ^∞] for degree ℓ cyclic fields" (JEMS 2022) and related 16-rank work.
  A. Smith, "2^∞-Selmer groups, 2^∞-class groups, and Goldfeld's conjecture" (arXiv:1702.02325).
  FIMR: Friedlander–Iwaniec–Mazur–Rubin, "The spin of prime ideals" (Invent. Math. 193 (2013) 697–749).
  All from memory, unverified in this session.
* What these theorems give: the *distribution* of 4-/8-/16-ranks or spins **over families** (fields
  ℚ(√−p) with p ≤ X; prime ideals in a fixed field). FIMR proves that spin is equidistributed, i.e.
  cancellation in a sum over prime ideals. No statement fixes p and decides a property of p beyond its
  Frobenius.
* POINTWISE_SIZE §4.2 (E3) lists fixed non-abelian Frobenius data as open. A Frobenius-decorated Theorem M/C
  is proposed there but not developed.

## 3. Dictionary (PROVED, elementary)

**D1 (the slice event is abelian Frobenius data).** By the e-slice form (LONGSHOT_PIGEONHOLE Lemma 1.1),
ES(p) ⟺ ∃ e ≡ −p (4) and a, b with ab | N_e, where N_e = (p+e)/4 (II) or (pe+1)/4 (I), such that
`a·b⁻¹ ≡ −1 (mod e)`. Under Artin reciprocity for ℚ(ζ_e)/ℚ, the class of an integer coprime to e is its
Frobenius, and −1 corresponds to complex conjugation c_∞. So the slice event says: *the ideal (a)(b)⁻¹,
built from prime divisors of N_e, has Artin symbol c_∞ in ℚ(ζ_e)/ℚ.* Every slice event is therefore a
statement about **abelian** Frobenius classes of the prime factors of N_e. The data of p itself enter
only through the congruence p ≡ −e (mod ℓ) for ℓ | N_e. In knot language, the condition is a linking
relation between the knots ℓ | N_e and the "cyclotomic knot" e. No triple-linking (Rédei) term occurs:
the condition is linear in the classes of the ℓ in (ℤ/e)^×.

**D2 (non-abelian Frobenius conditions pass the odd-square test T1).** Odd squares satisfy the obvious
analogue of every fixed non-abelian Frobenius condition:
* *Ring class fields.* Let Q be a primitive positive definite form of discriminant D in the principal
  genus, so Q = g² in Cl(D). If a prime ℓ ∤ D is represented by g (infinitely many are, by Chebotarev),
  then composition gives a primitive representation of ℓ² by Q. The ideal 𝔩² is not divisible by (ℓ),
  because ℓ splits. Forms outside the principal genus represent no square coprime to D (genus characters).
* *Power-residue symbols.* (a/m²)_k = (a/m)_k², so with m = ℓ ≡ 1 (mod 2k) and (a/ℓ)_k = 1, every
  k-th power residue condition holds at m².
* *Rédei symbols and spin* are defined from the same ingredients (quadratic and quartic symbols of the
  prime factors), so by the same composition they can be made trivial at ℓ².

Hence a route of the form "Frob_p ∈ C (non-abelian) ⇒ Type I/II(p)" must still contain a step that is
false at n = ℓ². The Frobenius condition cannot be that step. The step must be the same divisor event
as before.

**D3 (the non-abelian covering mechanism is Theorem C again).** A *Frobenius-gated identity covering*
is a finite list of rules (C_i, r_i mod M, W_i). Here C_i is a conjugacy class of Gal(K/ℚ), and W_i is
a witness polynomial in p, valid when Frob_p ∈ C_i and p ≡ r_i (M). It cannot cover all large primes.

*Proof (PROVED relative to Chebotarev and Mordell's theorem, as quoted in ET p. 8).* Let L = K·ℚ(ζ_M).
For each σ ∈ Gal(L/ℚ) restricting to the identity on ℚ(ζ_M), Chebotarev gives infinitely many p ≡ 1 (M)
with Frob_p|_L = σ. Choose σ with σ|_K ∈ C_i for some rule i applicable at p ≡ 1 (M). (If no rule applies
to the class r = 1, the covering already fails on infinitely many primes.) Then W_i is valid at
infinitely many p, so W_i is a polynomial identity in p, valid on the whole class p ≡ 1 (M). That class
is a square class. Mordell's theorem says no polynomial identity covers it.

Scope: witnesses polynomial in p. Witnesses computed by procedures that also factor auxiliary values
r_h(p) need the Schinzel–Chebotarev hypothesis H_K of POINTWISE_SIZE §4.2(E3). The step "FROB queries
are constant along the admissible set" is then immediate, and Theorem C's character computation applies
unchanged (it uses only Legendre symbols). So, CONDITIONAL on H_K, E3 at the witness-procedure level adds
nothing to Theorem C. The only remaining non-congruence channel is E2: e.g. "find x, y with
p = Q(x, y) (Cornacchia), then use a polynomial identity in (x, y)". By D2, that channel meets T1 exactly
as the one-variable identities do whenever its integrality class contains composition-square points.
A full proof needs a two-variable Theorem M at a "Q-square-mimicking" profinite point; not done here.

## 4. Experiment (EVIDENCE; `scripts/bs_nonab_frob.py 4000000 400`)

Statistic: W(p) = # ordered Type II triples (e, a, b) with e ≤ 400, e ≡ −p (4), ab | (p+e)/4 and
e | a+b. Population: all primes 1000 < p < 4·10⁶ with p ≡ 1 (24) (35265 primes). The table shows the mean
of W/log³p by stratum. The SE is ≈ 0.0001 (0.0002 in the square-class subpopulation).

| stratum (Frob type) | all p≡1(24): T / F | square classes mod 840: T / F |
|---|---|---|
| 2 quartic residue (D₄, non-abelian) | 0.0409 / 0.0409 | 0.0322 / 0.0319 |
| p = x²+32y² (D₄ ring class, 8 ∣ h(−4p)) | 0.0411 / 0.0408 | 0.0321 / 0.0320 |
| 2 cubic residue (S₃) | 0.0411 / 0.0408 | 0.0323 / 0.0320 |
| 3 quartic residue (D₄) | 0.0410 / 0.0409 | 0.0320 / 0.0321 |
| **control: p ≡ 1 (16) (abelian)** | **0.0382 / 0.0437** | **0.0311 / 0.0331** |

The abelian control separates the strata at ≈ 40σ (≈ 7σ inside the square classes). The four non-abelian
splits differ by ≤ 2σ. The square-class penalty (0.032 vs 0.041) is abelian, as known. The minima of W
show no non-abelian pattern either.

Explanation (heuristic; the density-level statement is PROVED by Chebotarev): K ∩ ℚ(ζ_q) ⊆ K^ab, so for
any fixed modulus q the joint density of {p ≡ r (q), Frob_p ∈ C} factorises over the abelian shadow.
Every truncation of W(p) is a congruence statistic, so its mean is blind to the non-abelian part of the
Frobenius. This is a T7 statement: it holds on average only, and it says nothing at a single p.

## 5. Barrier screen

* **B1.** D3: Frobenius gating does not rescue identity coverings (PROVED for polynomial witnesses;
  CONDITIONAL on H_K for procedures).
* **B2.** D1: the slice condition is literally abelian Frobenius data of the factors of N_e. Non-abelian
  data of p could at most *choose* θ (as H-D already notes). Choosing θ by a Chebotarev class is a fixed
  finite set of rules, so Thm 2.2(iii) applies.
* **B3/B4.** These are not engaged; no counting main term is proposed.
* **B5/T1.** D2: the non-abelian conditions hold at suitable odd squares ℓ². The false-at-squares step
  remains the divisor event.
* **B6/T7.** Smith, Koymans–Pagano and FIMR are distributional over families of fields or primes, so
  they are pure averages. At a single p, Rédei symbols are just bits of p, of the kind D3 and the table
  show to be irrelevant.

## 6. Viability Assessment

**COLLAPSES to B2 (at D1) and to B1/B5 (at D3/D2).** The decisive reason is D1. Every ES slice event is
an abelian (cyclotomic) Frobenius condition on the prime factors of N_e, so no non-abelian invariant of
p has a slot in which to enter. Fixed non-abelian invariants of p only gate θ-choices. They pass T1
(D2), they are statistically invisible (§4), and a gated identity covering fails by Chebotarev plus
Mordell (D3).

By-products:
* D3 (PROVED, polynomial-witness scope; CONDITIONAL on H_K for procedures). This settles the
  identity-level case of E3 in POINTWISE_SIZE §4.2.
* D2 (PROVED, elementary): the T1 dictionary for non-abelian conditions.
* EVIDENCE §4: no non-abelian Frobenius effect on Type II abundance at the 2σ level.

Novelty: modest. D3 is a straightforward combination of known tools.
