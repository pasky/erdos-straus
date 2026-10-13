# PARITY_FIXED_P — hatch H-B: parity-breaking / bilinear structure at a fixed prime (task O165)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.**
Labels as in DISCOVERIES.md. Scripts `scripts/pf_*`.

Goal (brief): a formulation of ES(p) as a sum over a long structured family (length a power of p) with a
non-tiny positive main term and Friedlander–Iwaniec (FI) Type I/Type II structure, where parity is the only
obstruction; say what an FI-type theorem would have to deliver.

## 1. Dictionaries at fixed p (PROVED, elementary; checked by `scripts/pf_dict_check.py`)

Notation: row II{a,d} target `f | N = p + 4a²d`, `f ≡ −1 (mod 4ad)` (count over *all* such f, no range cut);
Type I target `f | p² + 4c²d`, `f ≡ −p (mod 4cd)`.

**Lemma 1.1 (Type II as a three-parameter divisibility).** For every integer n ≥ 1 the map
`(h,k,d) ↦ (a,d,f) = ((hn+k)/(4dhk−1), d, 4adh−1)` is a bijection
`{(h,k,d) ∈ ℕ³ : (4dhk − 1) | hn + k}  →  {(a,d,f) : f | n + 4a²d, f ≡ −1 (mod 4ad)}`.
*Proof.* Given (a,d,f), put q = 4ad, g = N/f. Since f ≡ −1 and N ≡ n (mod q), g ≡ −n (mod q). So
f = qh − 1, g = qk − n with h,k ≥ 1. Expanding fg = n + qa gives `qhk − hn − k = a`, i.e.
`a(4dhk − 1) = hn + k`. Conversely, if m = 4dhk − 1 divides hn + k, put a = (hn+k)/m ≥ 1, f = 4adh − 1,
g = 4adk − n. Then 4adk = n + (k+a)/h > n, so g ≥ 1, and the same algebra gives fg = n + 4a²d. The two maps
are mutually inverse. ∎ (Brute-force bijection check: all n ≤ 119.)

h = 1 is the (A)3 subsystem `(4dk−1) | n + k` (BRAINSTORM/tech_maynard_theta Lemma 1.1). Reducing mod m:
`m | hn + k ⟺ m | 4dh²n + 1`, so the triple is also "4dh²n + 1 has a divisor ≡ −1 (mod 4dh)" (the
divisor form tp+1 = m·m″ with t = 4dh²).

**Lemma 1.2 (Type I is p-free up to one congruence).** For every prime p,
`(d,k,f) ↦ (c,d,f) = ((f+p)/(4dk), d, f)` is a bijection
`{(d,k,f) : f | 4dk² + 1, 4dk | f + p, p ∤ f}  →  {(c,d,f) : f | p² + 4c²d, f ≡ −p (mod 4cd), p ∤ f}`.
*Proof.* On either side, a prime r | gcd(f, cd) divides f + p (as 4cd | f+p, resp. as 4dk | f+p and
c = (f+p)/4dk... directly: r | f and r | 4cdk = f + p), hence r = p, excluded; so gcd(f, cd) = 1.
(←) f = 4cdk − p with k = (f+p)/(4cd). Mod f, p ≡ 4cdk, so p² + 4c²d ≡ 4c²d(4dk² + 1), hence f | 4dk² + 1.
(→) p ≡ 4cdk (mod f) gives p² + 4c²d ≡ 4c²d(4dk²+1) ≡ 0, and f = 4cdk − p ≡ −p (mod 4cd). ∎
(Solutions with p | f force p | cd; they are the non-primitive ones and are irrelevant here.)
(Direction (→) checked for n ≤ 39.) Writing m = dk: **Type I(p) ⟺ ∃ m ≥ 1, k | m, f | 4mk + 1 with
p ≡ −f (mod 4m).** The integers 4mk + 1 do not involve p; p enters only through its residue mod 4m. This is
the B1 frame made exact at fixed p: p must avoid the residue sets −D_m (mod 4m), D_m = {f : f | 4mk+1, k|m},
for *every* m — a sieve in which the single integer p is the sifted object.

**Lemma 1.3 (spin lemma; PROVED).** Let p ≡ 1 (mod 4) be prime.
(i) (Type II) If ℓ is a prime, ℓ | p + 4a²d, ℓ ∤ 2pad, then `χ_{−4d}(ℓ) = (ℓ/p)`.
(ii) (Type I) If ℓ | p² + 4c²d, ℓ ∤ 2pcd, then `χ_{−4d}(ℓ) = +1`.
*Proof.* (i) −4a²d ≡ p (mod ℓ), so (−d/ℓ) = (p/ℓ) = (ℓ/p) by reciprocity (p ≡ 1 mod 4). (ii) −4c²d ≡ p²
is a nonzero square mod ℓ. ∎ (18950 instances checked, 0 violations.)

*Consequence (the sign layer, made explicit).* The genus character χ = χ_{−4d} lifted to q = 4ad (resp. 4cd)
has χ(−1) = −1, so a hit f needs χ(f) = −1.
* Type I: every divisor f coprime to 2cd has χ(f) = +1, but the target class −p has χ(−p) = −χ(p): the
  χ-test is passed iff (−d/p) = −1 — pure congruence data on p (the BL/genus condition). No spin freedom.
* Type II: χ(f) = (f/p) (Jacobi symbol mod p) for f | N coprime to 2ad. So the χ_{−4d}-layer of slice II{a,d}
  is passed iff **N_θ = p + 4a²d has a divisor that is a quadratic non-residue mod p**, i.e. a prime factor
  ℓ ∤ 2ad with (ℓ/p) = −1. Since N_θ ≡ 4a²d (mod p), (N_θ/p) = (d/p): for (d/p) = −1 this is automatic; for
  (d/p) = +1 it is a genuine **spin event** (an even, nonzero number of QNR prime factors). At n = m² the
  symbol (ℓ/n) is replaced by +1 and the event never happens — the T1 mechanism at the level of a single
  character. This is the FI-type object of the problem: Legendre symbols modulo the fixed p evaluated on the
  prime factors of a polynomial family.

## 2. Where is parity in H-B? (the multiplicative-class layers need no parity breaking)

Recall the priority partition of slices (BRAINSTORM/corr_parity_layers §1 + errata): hit > prime > Q > Q′ > A.
The H-B premise (redteam-automorphic-2 §3) is that "bad" slices form a multiplicative/sign-pattern set that the
parity problem prevents a *lower-bound* sieve from detecting. But a fixed-p route needs a lower bound for
*good* slices, i.e. an **upper** bound for bad ones, and upper-bound sieves have no parity problem. Concretely:

**Proposition 2.1 (the χ_{−4d}-layer by Brun's pure sieve; PROVED relative to Burgess).** Let p ≡ 1 (mod 4)
be a large prime and 𝓑 = {d ≤ p/4 : (d/p) = +1} (slices II{1,d}, N_d = p + 4d, |𝓑| ~ p/8). Call d
*χ_{−4d}-obstructed* if every prime ℓ ∤ 2d dividing N_d has χ_{−4d}(ℓ) = +1. Then
#{obstructed d ∈ 𝓑} ≤ (5/8 + o(1))·|𝓑|. (Slices with (d/p) = −1 are never obstructed, since (N_d/p) = (d/p).)

*Proof.* An odd prime ℓ | N_d, ℓ ≠ p, never divides d. By Lemma 1.3(i), obstructed ⟹ no ℓ ∈ 𝒫 :=
{2 < ℓ ≤ z prime, (ℓ/p) = −1} divides N_d, z = p^{1/4+ε}. *Burgess input:* #{n ≤ z : (n/p) = −1} = z/2 + o(z),
each such n has a prime factor in 𝒫 ∪ {2}, so Σ_{ℓ∈𝒫} 1/ℓ ≥ 1/2 − 1/2·[(2/p) = −1] − o(1)… — to avoid the
prime 2, use odd n: #{n ≤ z odd : (n/p) = −1} = z/4 + o(z) (Burgess for the character n ↦ (n/p) on the
progression 1 mod 2), each with a prime factor in 𝒫, so Σ_{ℓ∈𝒫} 1/ℓ ≥ 1/2 − o(1). Pick 𝒫′ ⊂ 𝒫 greedily
with μ := Σ_{𝒫′} 1/ℓ ∈ [1/2 − o(1), 1]. With X(d) = #{ℓ ∈ 𝒫′ : ℓ | N_d}, 1[X = 0] ≤ 1 − X + X(X−1)/2.
For r = ℓ or ℓℓ′ (ℓ ≠ ℓ′ ∈ 𝒫′, r ≤ p^{1/2+2ε}), r | N_d fixes d ≡ c_r (mod r); Burgess for the incomplete sum
Σ_{t ≤ p/(4r)} ((c_r + rt)/p) (length ≥ p^{1/2−3ε} ≥ p^{1/4+ε}) gives #{d ∈ 𝓑 : r | N_d} = |𝓑|/r·(1 + o(1))
uniformly in r. Summing, #{obstructed}/|𝓑| ≤ 1 − μ + μ²/2 + o(1) ≤ 5/8 + o(1) for μ ∈ [1/2, 1]. ∎
(The same proof works for a ≤ p^ε with routine bookkeeping for ℓ | a; not needed here.)

EVIDENCE (`scripts/pf_spin.py`, `logs/pf_spin.txt`; 4000 random weighted slices each): pass rate among
(d/p) = +1 slices 0.39, 0.54, 0.45, 0.60 at p = 100004521, 1000002361, 10000003441, 1000000003801
(all ≡ 1 mod 840); 0.000 at the controls n = 10001², 100001² (T1).

Remarks. (1) T1 passes: at n = m², Lemma 1.3(i) has (ℓ/n) replaced by +1, the QNR primes have *no roots*
(ω(ℓ) = 0), and the sieve correctly certifies nothing. (2) The same argument works for any quadratic
character ψ of small conductor dividing 4a with ψ(−1) = −1 (sift by {ℓ : ψ(ℓ) = −1}, Dirichlet density 1/2,
proportion → 0 like (log p)^{−1/2}), and for the "prime" class (≤ (2+o(1))|𝓑|/log p). (3) What the
upper-bound sieve cannot do is the union over the 2^{ω(4ad)} characters for slices with many prime factors
in q; numerically (corr memo table) the full quadratic layer passes for ≈ 20 % of slices at p ≈ 10⁶.

**Assessment 2.2 (H-B collapses into H-A; parity is not the binding constraint).** The layers *prime, Q, Q′*
are multiplicative-class sets, bounded above by sieves without parity breaking. The remaining layer A
("−1 ∈ H_θ but no divisor of N_θ lands in −1 mod q_θ") concerns the divisors of one integer modulo a moving
modulus; its natural count Σ_θ #{f | N_θ : f ≡ −1 (q_θ)} = Σ_{fg = N_θ} 1[q_θ | f + 1] is a bilinear form
with **all coefficients equal to 1** — a Type I / dispersion (divisor-sum) object, not a Type II sum with
Möbius-like coefficients. No step of a fixed-p ES argument needs to distinguish λ(n) = +1 from −1. The triage's
"parity-breaking input coupled to divisor incidence" therefore reduces to: a level-of-distribution statement
for the divisor incidences at Planck scale — hatch H-A.

Supporting EVIDENCE (`scripts/pf_mass.py`, `logs/pf_mass_h1.txt`): over the (A)3 successes at fixed p the
Liouville sums Σ λ(b), Σ λ(p+A) are of size O(√R) (e.g. p = 100000007: R = 62, Σλ(b) = 8, Σλ(p+A) = 4;
p = 100004521: R = 44, 10, 0); no parity bias in the solutions themselves.

## 3. What an FI-type theorem would have to deliver (the size layer)

**3.1 The FI template** (FI 1998; *Opera de Cribro* ch. 16–22; schematic). Input: a sequence a_n ≥ 0 of total mass
X; Type I: Σ_{r | n} a_n = g(r)X + R_r with Σ_{r≤D}|R_r| ≪ X𝓛^{−A}; Type II: Σ_{m∼M}Σ_n α_mβ_n a_{mn} ≪ X𝓛^{−A}
for β Möbius-like. Output: Σ_ℓ a_ℓ ~ 𝔖X/𝓛. The target is a ≥ 𝓛^{−O(1)} fraction of the mass, and errors are
𝓛^{−A}-fractions of the mass.

**3.2 Mass conservation (trivial, PROVED).** If certificates map at most M-to-one onto ES solutions, their number
is ≤ M·f(p). Heuristically f(p) ≍ 𝓛³ (EVIDENCE); proved: f(p) ≪ p^{3/5+o(1)} (Elsholtz–Tao). So in any
parent sequence of mass X built from bounded-multiplicity certificates, the target fraction is ≤ f(p)/X, and
the FI template applies only if X ≤ f(p)𝓛^{O(1)} — a polylog-length family, with no power-length bilinear
ranges. A "positive main term ≥ p^δ" (brief) therefore needs either unbounded multiplicity (fibred encodings;
LONGSHOT_FIBRED) or a parent count of *non*-certificates plus a deterministic upgrade (§4).

**3.3 The canonical size-layer object.** By Lemma 1.1 (h = 1) and its symmetric forms,
(★) R(p) = #{(j, f) : f | p + j, f ≡ −1 (mod 4j)} = #{b ≥ 3 : 4·(−p mod b) | b + 1}
(Type I with k = 1 in Lemma 1.2 is the same shape with f ≡ −p (mod 4j)). So the size layer is: *divisors of
the shifted primes p + j in a class modulo 4j* — a Titchmarsh-type divisor problem with fixed prime and
varying shift whose modulus is tied to the shift. Swapping, j = (−p mod f) must divide (f+1)/4: one Planck-scale
event per b. Heuristic main term per dyadic block b ∼ B: M(B) ≈ Σ_{n∼B/4} τ(n)/(4n) ≈ (log 2/4)·log(B/4)
(≈ 2.2 at B = 2²⁰) times local factors at small primes.
EVIDENCE (`logs/pf_mass_h1.txt`, complete b-range, p ≡ 1 (840) and generic): R = 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰
(p ≡ 1 mod 840); 62, 70 generic (10⁸, 10⁹); at p = 1000000003801 (≡ 1 mod 840) the partial range b ≤ 2·10⁹ already
gives 56. Dyadic profiles: 0–8 successes per block across all 25–34 blocks, except
the top block at p = 10⁹+7 (16; small (B,C), i.e. forced classes of p modulo small 4BC−1). **No block's
count grows with p.** Requirement on a Type I estimate over a block of length B: error ≤ 1/2 against trivial
size B (or B log B counting divisor pairs) — a saving of B^{1−o(1)}.

**3.4 The modular-hyperbola form and the pointwise ceiling (PROVED dictionary + Assessment).** Solutions of
4ABC − A − B = p ⟺ (4AC−1)(4BC−1) = 4Cp + 1. Hence (A)3(p) ⟺ ∃ (x, y) ∈ ℕ² with xy ≡ 1 (mod 4p) such
that C := (xy − 1)/(4p) ≥ 1 satisfies 4C | x + 1 and 4C | y + 1 (then A = (x+1)/4C, B = (y+1)/4C). So the
success set is a sparse subset of the modular hyperbola 𝓗 = {xy ≡ 1 (mod 4p)}, cut out by a divisibility
condition coupling the point to its own "height" C. The
distribution of 𝓗 in boxes is controlled **pointwise in p** by Weil's bound for Kloosterman sums (error
O(p^{1/2+ε}) per box). The target is a union of thin curves with O(1) expected 𝓗-points per curve-block
(density of 𝓗 ≈ 1/(8p), strip area ≈ block length). So the strongest pointwise-in-p equidistribution tool
falls short by p^{1/2}: B3 in Kloosterman form. Assessment: an FI/Kloosterman-type theorem would need
**beyond-square-root** cancellation on a union of algebraic curves — not a parity statement.

## 4. Construction log (each attempt: which barrier hypothesis it violates, and the outcome)

* **I1 — weights q_θ** (violates "bounded weights" in B3): Σ_θ q_θ·#{f | N_θ : f ≡ −1 (q_θ)} has heuristic
  main term ≍ Σ_θ τ(N_θ) ≍ p𝓛. Fails: it is still a sum of O(1)-per-block events, now with weights up to p;
  relative fluctuation is unchanged and the L² mass grows by the factor Q, which every Cauchy–Schwarz Type II
  bound pays back. (Assessment.)
* **I2 — unbounded multiplicity via norm composition** (violates "bounded multiplicity"). In Q(√−d),
  (p + 2c√−d)(1 + 2cdt + pt√−d) = p + 2c′√−d with c′ = c + tN/2, N = p² + 4c²d, so Type I lines are closed under
  multiplication by these elements and N | N′. But the target class moves from −p mod 4cd to −p mod 4c′d, so
  solutions are not transported; no fibres form. Fails (PROVED identity; failure elementary).
* **I3 — partial certificates + deterministic upgrade by subset products** (violates "congruence-only data";
  the upgrade is an Olson/Davenport-type covering of −1 by subset products of the prime factors of N_θ). Needs
  ω(N_θ) ≳ log₂ q_θ, forcing q_θ ≤ exp(O(𝓛/log 𝓛)) and N_θ near-maximally composite; such θ are rarer
  (probability superpolynomially small in q) than the lottery itself. Fails quantitatively (cf. B4).
* **I4 — modular hyperbola mod 4p with Weil** (§3.4): the only fixed-p object found with power-length family,
  power-size main term and a *pointwise-in-p* asymptotic. The ES target is a curve-incidence inside it; short by
  p^{1/2}. Fails (Assessment); it is the precise form of "what FI/Kloosterman would need".
* **I5 — sign layer** (Prop 2.1): a genuine fixed-p, T1-passing, positive-proportion theorem — by an upper-bound
  sieve, no parity breaking. Insufficient for ES (corr memo §4; the size layer remains).
* **I6 — joint sign-and-divisor** (the triage's open sub-question): conditioning on sign-compatible slices
  raises the per-slice hit probability by a bounded factor (≈ 1/0.2 at p ≈ 10⁶ by the corr table; Prop 2.1 caps the
  gain from the χ_{−4d}-layer at 8/3); mass stays polylog. The joint count is the (★)-type divisor sum with
  coefficients 1 — Type I/dispersion, not Type II. Reduces to H-A.
* **I7 — Möbius/Liouville of N_θ** (brief lead (c)): "N_θ prime ⇒ empty" is ≤ (2+o(1))/𝓛 of slices by an
  upper-bound sieve; Σ λ over successes shows no bias (§2). The proposed second half ("structural lower bound on
  non-prime, non-obstructed slices") is exactly H-A.
* **I8 — short window of n around p with a dual detector** (brief lead (b)): thickening = interval averaging
  (POINTWISE_SPECTRAL Prop 5.4) — B6.

## 5. Verdict (Assessment) and exact scope

* **PROVED**: Lemmas 1.1–1.3 (dictionaries; the spin lemma χ_{−4d}(ℓ) = (ℓ/p) on Type II slices), Prop 2.1
  (relative to Burgess), the composition identity of I2, the (★) and modular-hyperbola forms.
* **Main finding (Assessment, mechanism-level).** H-B as posed is mis-targeted: every multiplicative-class
  ("parity/sign-pattern") obstruction in the slice partition — prime, Q, Q′ — enters a fixed-p argument only
  through an **upper** bound on bad slices, which sieves give without parity breaking (Prop 2.1 is the model case,
  and it passes T1). The irreducible part is the size layer: divisor incidences in a moving class at O(1) expected
  events per dyadic block, a Type I/dispersion object with unit coefficients (★), whose natural pointwise tool
  (Weil on the modular hyperbola mod 4p) is short by p^{1/2}. So H-B collapses into H-A; no Friedlander–Iwaniec
  Type II input is even *requested* by the problem. This sharpens corr_parity_layers §4 and answers the triage's
  "untested coupling" question negatively at the level of mechanisms (not a theorem: CONDITIONAL_ES Remark 2.4 still
  allows an exact-accuracy argument with small main term).
* **What a positive route would need** (stated precisely): a lower bound R(p) ≥ 1 for (★), i.e. an
  "exact-incidence" theorem for the curves {4C | x+1, 4C | y+1, xy = 4Cp+1} on 𝓗 mod 4p, or a Type I estimate
  for Σ_j Σ_{f | p+j} 1[f ≡ −1 (4j)] over a dyadic block with error < 1/2 — saving B^{1−o(1)} over trivial.
