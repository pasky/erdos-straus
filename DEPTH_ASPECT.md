# DEPTH_ASPECT — prime-power moduli in ES, over ℤ and in F_q[T] (O178, spark relay E)

Status: in progress (O178). ES is not solved, here or anywhere, and nothing below proves a case of it.
Builds on FUNCTIONFIELD_ES3.md (O173, CLAIMED, under review R173), FUNCTIONFIELD_ES2.md, CONDITIONAL_ES.md Lemma 1.2.
Scripts `scripts/bsE_*`. Memos `BRAINSTORM/bsE_*.md`.

## 0. Iteration log

* (I1) Over ℤ, restrict ET's moduli to powers of one prime q (§1). There is a parity kill (q ≡ 1 mod 4 never
  helps p ≡ 1 mod 4) and a mass kill: slice q^s carries mass ≈ log²p/q^s, so the family is a fixed finite slice set
  plus a geometrically small tail (B2). Numerics: for q = 3 the family misses 1233 of the 78496 primes below 10⁶.
  The p-adic structure of s ↦ q^s p + 1 does not help (Lemma 1.3).
* (I2) Steering: which barrier hypothesis did (I1) satisfy? It satisfied "mass per modulus ≍ 1/M, so a thin set of
  moduli carries vanishing mass". The function-field sterile-point problem violates this. There the point is
  ≡ 1 at every prime ≠ T, so the *whole* problem is forced to the depth T^s (O173). Go there (§2).
* (I3) In F_q[T], O173's elementary count of the T^s-hyperbola families is q^{s/2} (square root). An ET-type
  divisor casework (four different "given two small things, the rest is a divisor of an explicit polynomial"
  bounds) beats it: q^{2s/5+o(s)} (§2, Lemma 2.2).

## 1. Over ℤ: prime-power moduli in the ET slices

Notation: CONDITIONAL_ES Lemma 1.2 (ET Props 2.3/2.7). Type I: 4abd = tn + 1, t | a + b. Type II: 4abd = n + e,
e | a + b. Equivalent slicings: Type I as f | n² + 4c²d, f ≡ −n (mod 4cd), with f = 4acd − n. Type II as ff' = 1 + 4c²dn,
f ≡ f' ≡ −1 (mod 4cd), with f = 4acd − 1, f' = 4bcd − 1 (direct expansion; c = (a+b)/t resp. (a+b)/e).

**1.1 Which moduli can be prime powers (PROVED, elementary).** Every one of the moduli t, e, c, d may be taken to
be a power of a fixed prime q, and the integer then moves with the modulus:
| slice | integer N | modulus | event |
|---|---|---|---|
| (I-t) t = q^s | (q^s n + 1)/4 | q^s | ab | N, a ≡ −b (mod q^s) |
| (II-e) e = q^s | (n + q^s)/4 | q^s | ab | N, a ≡ −b (mod q^s) |
| (I-cd) c = q^u, d = q^v | n² + 4q^{2u+v} | 4q^{u+v} | f | N, f ≡ −n |
| (II-cd) c = q^u, d = q^v | 4q^{2u+v} n + 1 | 4q^{u+v} | f | N, f ≡ −1 |
Parity: (I-t) needs q^s n ≡ 3 (mod 4) and (II-e) needs n + q^s ≡ 0 (mod 4). So q = 2 is impossible, and for
n ≡ 1 (mod 4) a prime q ≡ 1 (mod 4) never contributes. For q ≡ 3 (mod 4) only odd s contribute.
So for the hard primes the depth families are t, e ∈ {q, q³, q⁵, …} with q ≡ 3 (mod 4).

**1.2 Mass (heuristic, Assessment; numerics EVIDENCE).** For a fixed modulus M the expected number of (a,b) is
≍ log²n/M. ET's average log³n is Σ_{M ≤ n} log²n/M. Over the thin set M = q^s the sum is
≍ log²n·Σ_s q^{−s} = O_q(log²n), and it is concentrated on s = O(1). Measured (`scripts/bsE_qpow.c`, q = 3,
primes ≤ 10⁶, mean count per s, Type I / Type II): s=1: 13.9/13.3, s=3: 1.84/1.32, s=5: 0.20/0.11,
s=7: 0.028/0.007 (all primes; odd s are the p ≡ 1 mod 4 half). The decay is ≈ 1/3 per step, as predicted.

**1.3 Numerics (EVIDENCE; `scripts/bsE_qpow.c`, cross-checked by `scripts/bsE_qpow_check.py` to 7400, identical
failure lists, every counted solution rebuilt and checked exactly).** Prime-power ET families (I-t) ∪ (II-e),
s ≥ 0, primes 5 ≤ p ≤ 10⁶:
* q = 3: **1233 primes have no solution in the family** (first: 241, 409, 769, 1249, 1321, …). Up to 2·10⁴ there are
  42 (1.9 %), up to 10⁶ 1233 (1.6 %). The largest least-s needed is 7.
* q = 7: 3518 failures (first 1009, 1021, …); q = 11: 259 already below 2·10⁴.
* T1 control: all 499 odd squares ≤ 10⁶ have empty families (as they must, T1).
* q = 5: every p ≡ 1 (mod 4) fails (parity, §1.1).
So the depth family is far from sufficient. It behaves like the two slices t = 3, e = 3 plus a small tail.

**Lemma 1.3 (q-adic structure gives only bounded depth; PROVED, elementary).** Fix q and n. Let a, b be fixed
integers (independent of s). Then a ≡ −b (mod q^s) holds only for s ≤ v_q(a + b). More generally, let a_s, b_s, d_s be
exponential polynomials in s of the shape α·q^s + β with α, β ∈ ℚ (the only shapes compatible with
4a_s b_s d_s = q^s n + 1 identically). If two of them are constant, the third is (q^s n + 1)/(4·const). Then
a_s ≡ −b_s (mod q^s) holds identically only if v_q(1 + 4b²d) = ∞, which is impossible. So every "q-adically
analytic" choice of witnesses serves only boundedly many s. Witnesses for large s must contain prime factors of
q^s n + 1 that grow with s, and those are the lottery.
*Proof.* If a_s = (q^s n + 1)/(4bd) with b, d fixed, then a_s + b ≡ 1/(4bd) + b (mod q^s), and this is ≡ 0 only for
s ≤ v_q(1 + 4b²d) < ∞. The case where a or b is the only non-constant factor is symmetric (a_s + b with d fixed;
a fixed, b_s varying). If d_s is the non-constant factor, a, b are fixed and the first sentence applies. A product
of two non-constant factors would have degree 2 in q^s. ∎
For each prime ℓ ∤ qn, ℓ | q^s n + 1 iff s ≡ −log_q(n) (mod ord_ℓ q). So the small-prime factorisation of N_s is
periodic in s (Sierpiński/covering-congruence structure). Periodic data are congruence data, so this is B1.

**1.4 Barrier screen and verdict for the ℤ question.**
* B2: the family's mass sits on s ≤ S₀ = O(1). For each fixed S₀ the slices s ≤ S₀ are a fixed finite slice set,
  which fails i.o. under H (redteam-automorphic-2 Thm 2.2(iii)). The tail s > S₀ has mass ≪ log²p/q^{S₀}. A failing
  prime needs only ≈ 2 log_q log p simultaneous slice failures, so the family fails i.o. under a uniform
  Hardy–Littlewood heuristic (CONJECTURE). The 1233 failures below 10⁶ are this effect.
* B3/B6: depth-aspect equidistribution (Postnikov, Iwaniec, Milićević) controls character sums over *intervals*.
  Here the objects are the ≤ τ(N_s)² divisor pairs of one integer per s. No interval occurs and there is nothing to
  average, so depth tools have no entry point at fixed p (Assessment).
* T1: respected trivially (the family is a subfamily of Type I/II).
* **Verdict (Assessment): over ℤ, prime-power moduli give a thin H-A family, dominated by bounded moduli. Dead.**
  What the Z-side shows: the depth aspect can only matter where the problem is *forced* to a prime power, as in the
  function-field sterile point, where every non-T place is trivialised. That is §2.

## 2. F_q[T]: the depth-aspect count at slice points is *not* square-root

Setting (FUNCTIONFIELD_ES3 §§1–3): q odd, A = T^k, k ≥ 2, c ∈ F_q^*. The *c-slice* is the set of slice points x_u
(x ≡ 1 at every prime ≠ T, x ≡ u mod T^∞) with u ∈ 1 + cT + T²F_q[[T]], with Haar measure on u (total mass q^{−2}).
A linear family valid at some x_u is valid exactly on a cylinder u ≡ −E (mod T^{N+1}) (Lemma 1.1 there), of mass
q^{−(N+1)}. If the total mass of all cylinders is < q^{−2}, then some x_u lies in O(q, T^k). By the compactness
criterion (FUNCTIONFIELD_ES2 §0.1), ES_q(T^k, ·) then has **no finite linear covering**.
O173 bounded the Case B families at level N by q^{(N+1+γ)/2+o(N)}, i.e. square-root size ≈ q^N in the critical regime
γ ≈ j, which gives mass ≈ q^{−k/2} per level, with no decay. O173 called this "a Kloosterman-type problem mod T^s".

**2.1 Case B tuples.** By O173 Lemma 2.1 a Case B family with parameter s = N + 1 + γ is a tuple (m', g', w, C)
of monic polynomials with
  m'wC = T^s + v,  w + C = g'v,  T ∥ w, T ∥ C, T ∤ m'g', v ≠ 0,  (B)
and L' = g'm', E = L'w − 1, E' = L'C − 1, EE' = 1 + T^s L'g'. The family (up to the choice of types, ≤ 4 choices,
same cylinder) is determined by (N, γ, m', g', w, C). By O173 Lemma 3.1 the union of its cylinders over (N, γ) with
N + 1 + γ = s is the single cylinder with j − γ ∈ {0, 1}, i.e. **N = N(s) := ⌈(s + k − 2)/2⌉**. Write 𝓕(s) for the
set of tuples (B). Degrees: a = deg w, b = deg C, z = deg m', y = deg g', t = deg v; a, b ≥ 1, a + b + z = s,
y + t ≤ max(a, b) (because g'v = w + C).

**Lemma 2.1 (four reconstruction identities; PROVED).** For every tuple (B), with E = L'w − 1:
(R1) (m', w, C) is an ordered factorisation of T^s + v, and g' = (w + C)/v;
(R2) E is a monic divisor of D = 1 + T^s L'g', g' | L';
(R3) **E | g'T^s + w**, and C = (g'T^s + w)/E, L' = (E + 1)/w;
(R4) **E | T^s + m'w²**, and L' = (E + 1)/w, g' = L'/m', C = (g'T^s + w)/E.
The same holds with (w, E) replaced by (C, E'). The polynomials g'T^s + w and T^s + m'w² are nonzero.
*Proof.* (R1), (R2) are (B) and O173 Lemma 2.1. Multiply m'wC = T^s + v by g' and use g'v = w + C:
g'm'wC = g'T^s + w + C, i.e. C(L'w − 1) = g'T^s + w. This is (R3). Multiply it by m'w:
CEm'w = g'm'w·T^s + m'w² = (E + 1)T^s + m'w², so E | T^s + m'w². This is (R4). Nonvanishing: deg(g'T^s) > a = deg w,
and v_T(m'w²) = 2 < s (T ∤ m'; s ≥ 3 by O173 Lemma 2.1). ∎

**Lemma 2.2 (Case B count beats square root; PROVED).** Let δ(n) be the maximum number of monic divisors of a
nonzero polynomial of degree ≤ n over F_q, and δ₃(n) the maximum number of ordered monic triple factorisations.
For every degree pattern (a, b, z, y, t) with a ≤ b, the number of tuples in 𝓕(s) with that pattern is at most
  B·q^{min(t − 2, y + z, (a − 1) + y, (a − 1) + z)},  with B = max(2δ₃(s), δ(s)·δ(3s), δ(2s)),
and min(t − 2, y + z, a − 1 + y, a − 1 + z) ≤ **2(s − 3)/5**. Hence |𝓕(s)| ≤ (s + 1)^4·B·q^{⌊2(s−3)/5⌋}.
(For a > b, use the C-versions of (R3), (R4).)
*Proof.* Count the data that determine the tuple. A monic w with T ∥ w and deg w = a has ≤ q^{a−1} choices. v has
T² | v (O173 Lemma 2.1(b)) and lc(v) = lc(w + C) ∈ {1, 2}, so ≤ 2q^{t−2} choices. Then:
by (R1), ≤ 2q^{t−2}·δ₃(s) tuples; by (R2), given L' (≤ q^{y+z} choices), g' | L' and E | D give ≤ δ(s)·δ(3s);
by (R3), given (w, g'), E | g'T^s + w gives ≤ δ(2s); by (R4), given (m', w), E | T^s + m'w² gives ≤ δ(2s).
For the minimum put x' = a − 1, σ = x' + y + z. Since t + y ≤ b = s − a − z, we get t − 2 ≤ s − 3 − σ. The least of the
three pairwise sums of (x', y, z) is ≤ 2σ/3. So min ≤ min(s − 3 − σ, 2σ/3) ≤ 2(s − 3)/5. ∎
*Remark.* This is Elsholtz–Tao's divisor casework (their n^{3/5} bound) transplanted. The square-root count of O173
used only (R1) and the cylinder count; the two "small-variable" identities (R3), (R4) are what beat it. Over ℤ the same
identities give #{(c,f,g): cfg − c − f = n} ≪ n^{2/5+o(1)} for the a = 1 Type I slice (same proof).
