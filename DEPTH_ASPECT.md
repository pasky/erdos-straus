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
| (I-t) t = q^s | (q^s n + 1)/4 | q^s | ab ∣ N, a ≡ −b (mod q^s) |
| (II-e) e = q^s | (n + q^s)/4 | q^s | ab ∣ N, a ≡ −b (mod q^s) |
| (I-cd) c = q^u, d = q^v | n² + 4q^{2u+v} | 4q^{u+v} | f ∣ N, f ≡ −n |
| (II-cd) c = q^u, d = q^v | 4q^{2u+v} n + 1 | 4q^{u+v} | f ∣ N, f ≡ −1 |
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
* q = 7: 3518 failures (first 5, 13, 29, 53, …); q = 11: 259 already below 2·10⁴.
* T1 control: all 499 odd squares ≤ 10⁶ have empty families (as they must, T1).
* q = 5: every p ≡ 1 (mod 4) fails (parity, §1.1).
*(Review repair: bsE_qpow.c truncated Type I at t ≤ n + 2, which is the a = 1 cutoff, not the general one. The
per-s means above are therefore truncated. `scripts/bsE_qpow_complete.py` re-checks every reported failure with t up to
the complete bound 9n²/4 + 1 (ET Lemma 2.8): 0 of the 1233 (q = 3) and 0 of the 3518 (q = 7) failures are rescued, so the
failure counts stand.)*
So the depth family is far from sufficient. It behaves like the two slices t = 3, e = 3 plus a small tail.

**Lemma 1.3 (affine-in-q^s witnesses give only bounded depth; PROVED, elementary; scope restricted by review).** Fix q and n. Let a, b be fixed
integers (independent of s). Then a ≡ −b (mod q^s) holds only for s ≤ v_q(a + b). More generally, let a_s, b_s, d_s be
exponential polynomials in s of the shape α·q^s + β with α, β ∈ ℚ (the only shapes compatible with
4a_s b_s d_s = q^s n + 1 identically). If two of them are constant, the third is (q^s n + 1)/(4·const). Then
a_s ≡ −b_s (mod q^s) holds identically only if v_q(1 + 4b²d) = ∞, which is impossible. So witnesses that are affine functions of q^s serve only boundedly many s. (Review repair: the proof is degree
counting, so it covers only witnesses polynomial in q^s, not arbitrary "q-adically analytic" choices. The earlier sentence
about large prime factors is withdrawn as a claim; a large divisor need not have a large prime factor.)
*Proof.* If a_s = (q^s n + 1)/(4bd) with b, d fixed, then a_s + b ≡ 1/(4bd) + b (mod q^s), and this is ≡ 0 only for
s ≤ v_q(1 + 4b²d) < ∞. The case where a or b is the only non-constant factor is symmetric (a_s + b with d fixed;
a fixed, b_s varying). If d_s is the non-constant factor, a, b are fixed and the first sentence applies. A product
of two non-constant factors would have degree 2 in q^s. ∎
For each prime ℓ ∤ qn, ℓ | q^s n + 1 iff s ≡ log_q(−n^{−1}) (mod ord_ℓ q), provided −n^{−1} ∈ ⟨q⟩ mod ℓ (otherwise never). So the small-prime factorisation of N_s is
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
and L' = g'm', E = L'w − 1, E' = L'C − 1, EE' = 1 + T^s L'g'. The cylinder (not necessarily the individual family: a0, b0 may split L·g differently) is determined by
(N, γ, m', g', w, C), and families with the same data have the same cylinder (review repair). By O173 Lemma 3.1 the union of its cylinders over (N, γ) with
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
identities bound the a = 1 Type I slice: #{(c,f,g) ∈ ℕ³: cfg − c − f = n} ≪ n^{1/3+o(1)}. *Proof:* for g ≤ n^{1/3},
(gc − 1)(gf − 1) = gn + 1 leaves ≤ τ(gn + 1) choices. For g > n^{1/3} and c ≤ f we have cf ≤ 2n^{2/3}, so c ≤ 2n^{1/3}, and
(gc − 1) | n + c leaves ≤ τ(n + c) choices of g. (PROVED, elementary; very likely folklore. Over ℤ there is no
depth, and this bound plays no role in ES.)

**2.2 Case A at generic slice points.** O173/O166 proved Case A impossible at the single point u = 1 + cT. At a general
u ∈ 1 + cT + T²F_q[[T]], Case A families occur and must be counted. Notation (R166's proof in FUNCTIONFIELD_ES2 §0.2,
step (1) and the degree estimate opening step (2); these use only E ≡ −u (mod T^{k+j}) with u ≡ 1 + cT mod T².
The rest of R166's step (2) uses the exact polynomial u = 1 + cT and does not generalise (review repair)): a0 = g·a1, b0 = g·b1, gcd(a1, b1) = 1,
E | a1 + b1, E ≡ −1 (mod L'), L' = g'a1'b1' (′ = prime-to-T part). WLOG deg a1 ≥ deg b1. Then T^α ∥ a1 with
α ≥ 1 + deg g' + deg b1', T ∤ b1, j = γ + α, and validity on the cylinder u ≡ −E (mod T^{k+γ+α}). The data (a1, b1, g, E)
with γ = 0 give the largest cylinder (lc(a0 + b0) and lc(L/a0 + L/b0) do not change when g is multiplied by T^γ), so it
suffices to count tuples with γ = 0, each covering mass q^{−(k+α)}.
Put λ = deg a1', β = deg b1, F := (a1 + b1)/E, f = deg F. Since gcd(a1', b1) = 1, a1'b1 | E + 1 and T | E + 1, so
**K := (E + 1)/(a1'b1) is a polynomial with T | K**; κ := deg K ≥ 1. Then deg E = λ + β + κ and f = α − β − κ ≥ 0.

**Lemma 2.3 (Case A identities; PROVED).** With z := (F + b1)/a1':
(A0) a1' | F + b1, so z is a polynomial, and z ≠ 0 for every valid family;
(A1) given (a1', b1): E | T^α a1' + b1;
(A2) given (b1, K): E | T^α + b1²K;
(A3) given z: b1·K·F = T^α + z, so (b1, K, F) is an ordered factorisation of T^α + z; then a1' = (F + b1)/z;
(A4) given (a1', K, F): b1 = (T^α a1' + F)/(a1'KF − 1) is determined.
*Proof.* EF = T^α a1' + b1 and E ≡ −1 (mod a1') give −F ≡ b1 (mod a1'), which is (A0). Substitute E = a1'b1K − 1:
a1'b1KF − F = T^α a1' + b1, i.e. **b1(a1'KF − 1) = T^α a1' + F** (A4; a1'KF − 1 ≠ 0 as T | K). Adding b1 to both sides of
a1'b1KF = T^α a1' + F + b1 = a1'(T^α + z) and dividing by a1' gives b1KF = T^α + z (A3). Substituting F = a1'z − b1 into (A3):
z(a1'b1K − 1) = T^α + b1²K, which is (A2). (A1) is EF = a1 + b1. If z = 0 then b1KF = T^α, so b1 = 1, F = −1 and K = −T^α. Then
E = −T^α a1' − 1, and E + 1 = T·L'·H with T ∤ H forces α = 1 and g' = 1. Then lc(E) = −1, while deg a0 > deg b0 gives
lc(a0 + b0) = lc(L/a0 + L/b0) = 1. Every Case A type combination has lc(s) = 1 ≠ −1 = lc(E) (q odd), so the family is not
valid. ∎

**Lemma 2.4 (Case A count; PROVED).** For each α, the number of Case A tuples (a1', b1, g', E) with γ = 0 and v_T(a1) = α
that are valid somewhere on the c-slice is at most (α + 1)^3·B_A·q^{⌊(α−1)/2⌋}, with B_A = 4·δ(α)·δ₃(α) (δ, δ₃ as in Lemma 2.2).
*Proof.* lc(E) ∈ {1, 2} (validity: lc(E) = lc(s) ∈ {1, lc(a0 + b0), lc(L/a0 + L/b0)} ⊂ {1, 2}), and so lc F, lc K take ≤ 2
values each. Monic K with T | K of degree κ: ≤ q^{κ−1} choices. Since a1 + b1 has degree α + λ ≥ β, f ≤ α − 1 and
deg z ≤ max(f, β) − λ ≤ α − 1. In particular T^α + z ≠ 0 (and T^α + b1²K ≠ 0, since z ≠ 0 by (A0)). Two cases.
* f ≥ β. Then deg z ≤ f − λ ≤ f, and by (A3) there are ≤ 2q^{f}·δ₃(α) tuples. By (A2), given (b1, K) there are
  ≤ 2q^{β+κ−1} choices, times δ(α + 2β + κ) ≤ δ(3α) for E; and β + κ − 1 = α − f − 1. min(f, α − f − 1) ≤ (α − 1)/2.
* f < β. Then deg z ≤ β − λ, and (A3) gives ≤ 2q^{β−λ}δ₃(α). (A4) gives ≤ 4q^{λ+κ−1+f} = 4q^{λ+α−β−1} with nothing
  further to choose. min(β − λ, λ + α − β − 1) ≤ (α − 1)/2.
g' is then a monic divisor of K/T: ≤ δ(α) choices. Patterns (λ, β, κ): ≤ (α + 1)^3. (Here δ(3α) ≤ δ(α)·… is absorbed
is not needed: in the case f ≥ β, deg(T^α + b1²K) ≤ α because 2β + κ = α + β − f ≤ α, so δ(α) suffices there (review repair).
Also α > β forces deg a1 > deg b1, so lc(s) = 1 and E, F, K are monic.) ∎

**Theorem 2.5 (large q in characteristic 3: no finite linear covering of ES_q(T^k); PROVED, given O173 Lemmas 1.1, 2.1,
3.1, R166's Case A steps (1)–(2) and the compactness criterion).** Let k ≥ 2 and let q be odd with q ≥ 1.3·10^16, or
q = 3^r with r ≥ 27. Then for every c ∈ F_q^* the set of u ∈ 1 + cT + T²F_q[[T]] such that x_u lies in no validity set
has positive Haar measure (relative measure ≥ 0.97 for q = 3^r, r ≥ 27). Hence O(q, T^k) ≠ ∅, and **ES_q(T^k, ·) has no finite linear covering**.
For char q ≥ 5 this was known (O140 Prop 4.1: 1 ∈ O). For q = 3^r it is new; there the class-1 obstruction is absent
(FUNCTIONFIELD_ES §6.1(a)).
*Proof.* Relative to the c-slice (mass q^{−2}), a Case B tuple of parameter s covers q^{1−N(s)} and a Case A tuple of
depth α covers q^{2−k−α}. N(s) and the Case A exponent only improve with k, so take k = 2. Lemma 2.2 gives
Case B mass ≤ Σ_s Σ_patterns min(four bounds)·q^{1−⌈s/2⌉}, and per s the exponent is
⌊2(s−3)/5⌋ + 1 − ⌈s/2⌉ ≤ −max(1, s/10 + 1/5). Lemma 2.4 gives Case A mass ≤ Σ_α (α+1)^3 B_A q^{⌊(α−1)/2⌋−α}, exponent
≤ −(α+1)/2. With δ(n) ≤ 2^n and δ₃(n) ≤ 3^n (a degree-n polynomial has ≤ n irreducible factors), the crude closed
form 4Σ_s(s+1)^4(16q^{−1/10})^s q^{−1/5} + 24Σ_α(α+1)^3(16q^{−1/2})^α q^{−1/2} is decreasing in q and is < 0.48 at
q = 3^{34}; it is < 1 for q ≥ 1.3·10^16. For 3^27 ≤ q ≤ 3^33, `scripts/bsE_largeq.py` evaluates (in floating point; the margin
is ≥ 38×, so rounding is irrelevant, but no outward-rounded certificate was made) the pattern-wise
minimum exactly for s, α ≤ 100 and adds the crude tail beyond 100. The totals are 2.6·10^{−2} (r = 27),
1.9·10^{−7} (r = 28), < 2·10^{−11} (r = 29..33). Any covered set has measure ≤ these sums, so the uncovered set has
positive measure. Points of the uncovered set are in O(q, T^k) by definition, and O ≠ ∅ excludes a finite covering
(FUNCTIONFIELD_ES2 §0.1). ∎
*What this does and does not say.* Every truly large-q statement known before (O140 Thm 2.1) was at *fixed degree*
n, with q → ∞. Theorem 2.5 is at *fixed q* and covers all degrees at once. It is the function-field analogue of
"a sterile point exists" (over ℤ open for every Mordell r; MORDELL13E, MORDELL17C). The constant 16 comes from crude
divisor bounds. **The exponents are not the obstacle; the constants are.** At q = 3 the same union bound is > 1
(§3), exactly as over ℤ, where MORDELL17B needs ET's exponent 2/5 *with an explicit constant C ≤ 1.40*.

## 3. Transfer to ℤ: large Mordell primes r have sterile points

The dictionary of §2 is exact on the ℤ side. A *T-generic point* (POINTWISE_MORDELL §2.1, MORDELL17 §1) is
x(u) ∈ Ẑ^× with x_q = 1 for all q ≠ r and x_r = u. It is the analogue of the slice point x_u, with T ↦ r. The
classes of the seven ET families meet the r-generic line in *boxes* u ≡ ρ (mod r^k). By MORDELL17 Lemmas 1.1,
2.1–2.3 (stated for r = 17; the proofs use only that r is an odd prime and the r-generic table of
POINTWISE_MORDELL §2.1, which is for general T), the boxes are as follows. Level-k boxes of types Q, Q⁻¹, U, U⁻¹,
√Q number ≤ 6·f(r^k), where f(n) is the number of ordered solutions of 4/n. P-boxes are N-points of Σ^II_{r^K}
at half level ⌈K/2⌉, ≤ 2 per point. MORDELL17 §2, "Consequence (measure)", with 17 ↦ r, gives
  μ(⋃ boxes) ≤ S(r) := Σ_{k≥1} 6 f(r^k) r^{−k} + Σ_{K≥1} 2 f_II^N(r^K) r^{−⌈K/2⌉},
where f_II^N counts N-points of Σ^II modulo dilation. The ET exponent of the P-family is 2/5, against the weight
N^{−1/2} (margin 1/10). This is the ℤ face of Lemma 2.2. At r = 17 the margin is eaten by constants (MORDELL17 §4:
even constant 1 gives a tail of 0.84 > 0.677).

**Theorem 3.1 (sterile points for all large Mordell primes r; PROVED relative to ET Prop 1.7's proof applied to
N-points (as in MORDELL17 §2, R83-reviewed), Browning–Elsholtz f(n) ≪_ε n^{2/3+ε} for all n (review repair: ET's f(n) ≪ n^{3/5+o(1)} is stated
for prime n only, the same point as MORDELL17 R83 repair m1), and MORDELL17 Lemmas 1.1, 2.1–2.3,
Cor 4.2 for general odd prime r).** There is an effectively computable r₀ such that for every prime r ≥ r₀ the
r-generic line contains a sterile point x(u) with u a quadratic non-residue mod r. That is, x(u) lies in no class
of any of the seven ET families. Consequently **no finite set of ET Prop 1.9 classes covers all sufficiently large
primes p ≡ 1 (mod 24) whose least quadratic non-residue is r.** In fact the sterile set has measure
≥ (r − 1)/(2r) − S(r) → 1/2 in ℤ_r.
*Proof.* Browning–Elsholtz bound f(r^k), and ET's proof of Prop 1.7 gives f_II^N(n) ≤ n^{2/5 + C/log log n} with an
absolute (effective) C (MORDELL17 §2 for the N-point version). With n = r^K ≥ r, the exponent loss is ≤ CK log r/log log r.
Hence the Q/U part of S(r) is ≤ 6C_εΣ_k r^{−k(1/3−ε)} = O(Σ_k r^{−k/4}) with ε = 1/12 (all five
non-P box types are ≤ f(r^k) by MORDELL17 Lemmas 2.1, 2.2). The P part is
≤ 2Σ_K r^{K(2/5 + C/log log r) − K/2} ≤ 2Σ_K r^{−K(1/10 − C/log log r)}. Once C/log log r < 1/20 every series is geometric with
ratio ≤ r^{−1/20}, so S(r) → 0 as r → ∞. The non-residue cells have total measure (r − 1)/(2r). So for r ≥ r₀,
S(r) < (r − 1)/(2r), and some u in a non-residue cell is in no box, i.e. x(u) is sterile. MORDELL17 Cor 4.2 (proof:
a finite union of classes is clopen and misses a neighbourhood {x ≡ u mod r^L, x ≡ 1 mod Q} with
840·∏_{q<r} q | Q, which contains infinitely many primes, all with p ≡ 1 (24) and least non-residue r) gives the
consequence. ∎
*Remarks.* (1) The averaging over the (r − 1)/2 non-residue cells is essential. Low-level P-boxes (K = 1: ≤ 2f_II(r) ≪ r^{2/5+o(1)}
of them) cover *whole* cells, but only r^{2/5+o(1)} of the r/2 cells. (2) r₀ is astronomically large (log log r₀ ≈ 20C), so
this says nothing about r = 13, 17, where the sterile-point question stays open (MORDELL13E, MORDELL17C). What is new is
the logical status: **sterile Mordell points exist**, for all large r. The campaign had none: the only proved sterile points were
the square points, and x* was refuted. (3) Function-field twin: Theorem 2.5 (q large ↔ r large). There the constants are explicit
(q ≥ 3^27), because the divisor bound 2^n is uniform in q; over ℤ the divisor bound n^{C/log log n} is what forces r₀ huge.
(4) It does not touch ES itself. Sterility excludes finite *covering certificates*. The primes near x(u) may still satisfy ES,
and heuristically they do (the lottery, B2).
(5) **Caveat for the reviewer:** this transfer was written in one pass at the end of the session. The steps to recheck
are: (i) MORDELL17 Lemmas 1.1, 2.1–2.3 for general r, including whether any parity or reciprocity step used 17 specifically.
Lemma 1.3 is used only as an emptiness statement, which is not needed for an upper bound. (ii) The uniformity of ET's
O(1/log log n) for N-points that are not Type I/II solutions (MORDELL17 R83 repair m1 asserts it from ET §3). (iii) That U-boxes ≤ f(r^k)
(MORDELL17 Lemma 2.2) holds for general r. *The O178 self-review (deep reviewer) re-checked (i)–(iii) and found that the
transfer passes after the Browning–Elsholtz repair. This is internal; a hostile R-review is still needed.*

## 4. Numerics for §2 (EVIDENCE; validation of the enumerations)

* `scripts/bsE_famcount.c p k SMAX [print]` enumerates **all** Case B tuples of parameter s by (w, C), with v = (−T^s) mod wC.
  It checks the identities of Lemma 2.1 on every tuple (0 failures: q = 3 to s = 15, q = 5 to s = 11, q = 7 to s = 9,
  q = 11 to s = 8). Counts at q = 3 for s = 4..15: 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104, 48 (logs `data/bsE/fc*.txt`). This is polynomial-looking
  and far below both q^{s/2} and q^{2(s−3)/5}. Mean union-bound mass of a c-slice through SMAX: q = 3: 1.74; q = 5: 0.110; q = 7: 0.015;
  q = 11: 0.031.
* Cross-check with O173's independent engine (`scripts/bsE_crosscheck.py`, 300 random points of the c-slices, q = 3, deg L' ≤ 4,
  j ≤ 5, s ≤ 12): every ff3_caseB hit is a famcount tuple, and every famcount tuple whose maximal cylinder contains the point is
  found by ff3_caseB. 1064 hits, 446 covering tuples, 0 mismatches.
* Case A (`scripts/bsE_caseA.py`): route (A4) (enumerate a1', K, F; Lemma 2.3) and route (A1) (sympy factorisation of
  T^α a1' + b1) give identical tuple sets. q = 3, α = 1..6: 0, 0, 2, 4, 10, 8 tuples (union-bound mass 0.088); q = 5, α ≤ 4: 0.
  Every identity of Lemma 2.3 was asserted on every tuple.
* Observation (CONJECTURE, bsE_caseAB_shift): #Case A(α) = #Case B(α + 1) on all computed data.
