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
EVIDENCE (`logs/pf_mass_h1.txt`, complete b-range, p ≡ 1 (840) and generic): R = 44, 52 at p ≈ 10⁸, 10⁹
(p ≡ 1 mod 840); 62, 70 generic. Dyadic profiles: 0–6 successes per block across all 25–30 blocks, except
the top block at p = 10⁹+7 (16; small (B,C), i.e. forced classes of p modulo small 4BC−1). **No block's
count grows with p.** Requirement on a Type I estimate over a block of length B: error ≤ 1/2 against trivial
size B (or B log B counting divisor pairs) — a saving of B^{1−o(1)}.

**3.4 The modular-hyperbola form and the pointwise ceiling (PROVED dictionary + Assessment).** Write
m = 4BC − 1 (m ∤ 4p). From (4AC−1)(4BC−1) = 4Cp + 1: 4pC ≡ −1 (mod m), so with t := (4pC + 1)/m we get
mt ≡ 1 (mod 4p), and success ⟺ (m, t) is a point of the modular hyperbola 𝓗 = {xy ≡ 1 (mod 4p)} lying
on one of the curves Γ_A : x(tA... ) — explicitly t = 4AC − 1 with C = (mt−1)/(4p) dividing (m+1)/4. The
distribution of 𝓗 in boxes is controlled **pointwise in p** by Weil's bound for Kloosterman sums (error
O(p^{1/2+ε}) per box). The target is a union of thin curves with O(1) expected 𝓗-points per curve-block
(density of 𝓗 ≈ 1/(8p), strip area ≈ block length). So the strongest pointwise-in-p equidistribution tool
falls short by p^{1/2}: B3 in Kloosterman form. Assessment: an FI/Kloosterman-type theorem would need
**beyond-square-root** cancellation on a union of algebraic curves — not a parity statement.
