# Z53_GENUSREDEI — joint factor-multiset realisation: what can data at p force about ALL prime factors? (z53, lane GENUSREDEI)

**ES is OPEN. Nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. All results are internal, internally reviewed only. Targets FRONTIER §7.6 (full-factor-multiset
realisation, `CLASS_FORCING.md` §6) and the "class beyond parity" part of §7.3.
Scripts `scripts/z53_genusredei_*`, data `data/z53/genusredei/`.

## 0. Status / iteration log
* **Checkpoint 1** (this version): precise statement (§1), why it is not closed (§2), first lemma (the law lemma, §3, PROVED)
  and first falsifier design (§4, run in progress).

## 1. The statement attacked (precise)

*Lines.* A **line** is an integer-valued linear form L(p) = (αp + β)/γ (α, γ ≥ 1, β ∈ ℤ∖{0}, gcd(α, β) = 1, on a residue
class of p) with a **level** t. The four ES lines of CLASS_FORCING §1: p + 4d (t = 4d), 4Cp + 1 (t = 4C), (p + e)/4 and
(pe + 1)/4 (t = e). A finite set Λ = {L_1, …, L_r} of pairwise non-proportional lines; R_{jj′} := α_{j′}β_j − α_jβ_{j′} ≠ 0.

*Decorated configuration.* Fix B (a smoothness bound), T (a B-smooth modulus, divisible by every level and by 4∏_{q≤B}q·∏|α_jβ_j|),
n ≥ 1 (a power-residue order; we restrict to p ≡ 1 (mod 4n)). For a prime p write L_j(p) = s_j · ∏_i ℓ_{j,i} with s_j the B-smooth part
and ℓ_{j,i} > B (with multiplicity). The *decorated configuration* of p is the list, for every j, of s_j and of the multiset of
triples
  (D1) a_{j,i} = ℓ_{j,i} mod T;  (D2) ζ_{j,i} = (ℓ_{j,i}/𝔭)_n ∈ μ_n (n-th power symbol at a prime 𝔭 | p of ℚ(ζ_n));
  (D3) the mutual Legendre symbols (ℓ/ℓ′) between distinct large factors (of any lines) — the joint Rédei matrix,
together with the **p-datum**: Frob_p in a fixed finite Galois Ω/ℚ (any governing field / Rédei field / Kummer field / ring
class field) and p mod M (M B-smooth, high exponents).

**Question (§7.6, made precise).** Which properties of the decorated configuration hold for *every* large prime p with a
given p-datum? Thm 5.2 of CLASS_FORCING: no single large factor has a forbidden class. Is anything *joint* forced beyond the
product of the classes and the quadratic (parity) links?

**Answer claimed (to be proved in §5):**
* (PROVED) Five laws hold identically: (L1) product law mod T per line; (L2) product law for the n-th power symbols per line;
  (L3) the parity link ζ^{n/2} = χ_{−αβ}(a) per large factor; (L4) the cross-line law ∏_{ℓ|L_j(p)}(ℓ/ℓ′) = (ρ_{jj′}/ℓ′) for
  every large ℓ′ | L_{j′}(p), j′ ≠ j, ρ_{jj′} = R_{jj′}/(γ_jα_{j′}); (L5) quadratic reciprocity for the mutual symbols.
* (CONDITIONAL on HC of CLASS_FORCING §6) **Joint Realisation Theorem (JRT):** every decorated configuration satisfying
  (L1)–(L5) and compatible with the p-datum is realised by infinitely many primes p. Hence the forced joint content of
  all-factor data is *exactly* (L1)–(L5): nothing beyond the product, the parities, and reciprocity.
* Corollary: a bounded-level divisor event (any finite set of lines/levels) is forced on a Chebotarev class iff the
  configuration "one large factor per line" already forces it — the B1 criterion of CLASS_FORCING Prop 3.2. This upgrades
  CLASS_FORCING Thm 6.1 (one-sided, only at C|_{Ω₀} = 1) to an exact criterion in every Chebotarev class.
* What JRT cannot be: unconditional (a single-configuration instance is a prime-pair statement, Prop D).

## 2. Why this is not already closed
* CLASS_FORCING Thm 5.2 is single-factor; Lemma 3.1's "realisability" is abstract (integers, not values of a line at primes);
  Thm 6.1 only exhibits *one* bad configuration (the p ≡ 1 (M) point, all cofactors prime) and only in Chebotarev classes whose
  abelian shadow is trivial. FRONTIER §3 "Does NOT rule out: joint restrictions on all varying prime factors". TWO_POWER_LADDER
  Thm 3.1 is explicitly scoped to one varying level prime ("says nothing about joint restrictions").
* Not covered: p-relative decorations of the factors ((ℓ/p)_n, i.e. spin/quartic data *of the factors at p*) and the joint
  Rédei matrix of all factors across lines (mutual symbols) — the "higher genus" data of the lane brief.
* Escapes the closed list: the "bounded-level reciprocity along forced progressions with one varying level prime gives only
  parity" item is the one-prime case; here all factors vary jointly and the decorations involve p.

## 3. First lemma (PROVED): the five laws hold identically
(See §5.1 for the full proof.)

## 4. First falsifier (design; EVIDENCE pending)
If a hidden joint law existed at a bounded level, the **event rate** E(p, C) := 1[−1 ∈ Σ(4Cp + 1) mod 4C] (and the
p + 4d analogue) would deviate from the *free model*: smooth part s with its actual classes, large factors' classes i.i.d.
uniform on (ℤ/T)^× conditioned only on (L1). Test: primes p ≡ 1 (4) up to ~10⁷, levels C ≤ 15, d ≤ 15, stratified by k = number
of large factors and by p-data (p mod 16, (2/p)₄, 8 | h(−4p), (ℓ/p)₄ of the factors); compare observed and model rates
(χ²). Also test independence of the factor-level decorations (D2), (D3) from (D1). Controls: odd squares m² (law (L3) becomes
χ = 1: all factors in ker χ, event rate 0), near-squares, and the FRONTIER §4 item-14 test primes.
