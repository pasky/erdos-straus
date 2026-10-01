# A superlinear Ω-result for the multiplier witness: `W(p) > (log p)^{2−o(1)}` infinitely often

Task c2. Labels follow the house rules (PROVED / PROVED modulo a cited
theorem / CONDITIONAL / Assessment / EVIDENCE). **Cited** marks an external
theorem whose statement we read in the archived source but whose proof we did
not check. ES is not solved here or anywhere; nothing below bears on whether
`W(p)<∞`.

## 0. Results at a glance

Notation (notes (51.1), (58.3); POINTWISE_SIZE §7): for `M≡3 (mod 4)` put
`A_M=(M+1)/4` and `𝓡(M)={−4D mod M : D | A_M²}`, and

```
W(n) = min{ M≡3 (4) : n mod M ∈ 𝓡(M) },   so   W(n)>T  ⟺  n mod M ∉ 𝓡(M) for all M≤T, M≡3 (4).
```

"Hard" means Mordell-hard (one of Mordell's six classes mod 840); every
`p≡1 (mod 840)` is hard.

1. **Theorem 5.1 (PROVED modulo one cited theorem; effective).** There is an
   absolute constant `C` such that for infinitely many hard primes p,

   ```
   W(p) ≥ (log p)^2 · exp(−C log log p / log log log p).
   ```

   In particular `W(p) > (log p)^{2−ε}` infinitely often for every `ε>0`,
   `limsup log W(p)/log log p ≥ 2`, and `W(p)/log p → ∞` along a sequence of
   hard primes. More precisely, for **every** large T there is a prime
   `p≡1 (mod 840)` with `W(p)>T` and `log p ≤ T^{1/2}·exp(O(log T/log log T))`;
   so the least hard prime with `W>T` satisfies
   `log L_h(T) ≤ T^{1/2+o(1)}` (notes (58.2)). The previous records were
   `W ≥ (5/8−ε) log p` and `log L_h(T) ≤ (8/5+o(1))T` (POINTWISE_SIZE
   Thm 11.2, via Chang), and `1/5.2` (notes Thm 54.1, effective).

   The cited theorem is Thorner–Zaman, *Refinements to the prime number
   theorem for arithmetic progressions*, Math. Z. 306 (2024), Corollary 1.4
   (arXiv:2108.10878v2, archived). It is a PNT in progressions in the Linnik
   range `x≥q^{12}`, with the Deuring–Heilbronn repulsion built into the
   error term. It has effective constants. There is no Siegel caveat and no
   use of Chang's theorem.

2. **The new arithmetic input: Lemma 2.3 (PROVED).** Impose the class of one at
   every prime `≤y`, with `y≥√T`. What remains of the witness system is
   *prime-local*: a single forbidden set `F_ℓ` at each prime `ℓ∈(y,T]`. Its
   sieve mass is

   ```
   S := Σ_ℓ |F_ℓ|/(ℓ−1) ≤ exp(O(log T / log log T)) = T^{o(1)}.
   ```

   The congruence `m | 4D+1` saves a factor m, via the identity `m | r+k` in
   the parametrisation `D=sr²`, `A=srk`. This is exactly the "mean value for
   divisors of `((M+1)/4)²` in the class `−(M+1)/4 mod m`" that POINTWISE_SIZE
   §7.3(i) lists as missing. The crude bound behind Lemma 11.7 is
   `T^{1/2−η+o(1)}`, and with it the same transfer gives only a linear range
   (Assessment 11.6). EVIDENCE: `S(10^3..10^6)=6.5, 13.6, 23.9, 38.5`, about
   `0.054(log T)^{2.5}`.

3. **Transfer Theorem 4.1 (PROVED modulo the same citation).** This is a
   general criterion. Suppose a congruence minorant
   `B=Σc_i 1[n≡b_i (d_i)] ≤ 1[W(n)>T]` exists on the class `1 mod Q`. It
   must have positive mean μ, ℓ¹-mass `M_1`, and a twist condition for one
   possible real character. Then there is a prime `p≡1 (Q)` with `W(p)>T`
   and `log p ≪ log(Q·max d_i)·(1+log(M_1/μ))`. The Siegel-zero problem
   (step (iii) of the brief) is solved inside this theorem:
   * a uniqueness lemma for one "severe" exceptional character across the
     whole family of moduli (Lemma 3.2, from McCurley's region as quoted by
     Thorner–Zaman);
   * a two-case analysis.

4. **Obstruction above exponent 2 (§6).**
   * **(a) PROVED.** Exponent 2 is the ceiling of every *prime-local* design:
     a class-of-one quarantine in which no `M≤T` has two unquarantined prime
     factors. Any such design forces `log p ≥ (1/√3−o(1))√T`.
   * **(b) PROVED implication; the hypothesis is open.** The precise missing
     input is **Hypothesis H_MIN(θ)**: a congruence minorant for the
     non-prime-local residual system with quarantine `log Q ≤ T^{θ+o(1)}`,
     moduli `log d ≤ T^{θ+o(1)}`, and mean/mass ratio `e^{T^{o(1)}}`.
     H_MIN(θ) implies `W(p) > (log p)^{1/θ−ε}` infinitely often (Theorem 6.2).
     A polylogarithmic H_MIN gives `W(p) > exp((log p)^c)`.
   * **(c) PROVED / EVIDENCE.** The natural candidate fails: event-level
     Bonferroni of degree `J ≳ 4.2θ²(log T)²` has negative mean for `θ<1/2`
     (Prop 6.3). The cause is "hub" classes (`−4d²`, …) at which many
     two-prime atoms fire together. This is notes §33's correlation wall in
     exact form. EVIDENCE: hubs survive the deletion of atoms implied by
     single-prime atoms (51–65% of the multi-prime atoms are irredundant at
     `T=10^4, 10^5`).

## 1. Setting

Fix `T` large and put `𝓛=log T`. Throughout,

```
y := √T · exp(3𝓛/log 𝓛)                    (so  y = T^{1/2+o(1)},  y ≥ √T),
Q := lcm(24, ℓ^{e_ℓ} : ℓ ≤ y prime, e_ℓ = max{e : ℓ^e ≤ T}),
U := {primes ℓ : y < ℓ ≤ T}.
```

**Fact 1.1 (class of one; notes Thm 17.3(c)).** `1∉𝓡(M)` for every
`M≡3 (4)`.

*Proof (repeated for completeness).* Suppose `−4D≡1 (mod M)`. Since
`4A_M≡1`, this says `D≡−A_M (mod M)`. Replacing D by `A_M²/D` if necessary
(this is still `≡ −A_M`, because `A_M²·D^{−1} ≡ A_M²·(−A_M)^{−1} = −A_M`), we
may assume `D≤A_M`. Then `0<D+A_M≤2A_M<4A_M−1=M`, yet `M | D+A_M`, a
contradiction. ∎

**Fact 1.2 (sizes).**
* `log Q ≤ θ(y) + π(√T)𝓛 + log 24 ≤ 2y` for large T. Indeed only primes
  `ℓ≤√T` have `e_ℓ≥2`, and `θ(y)<y log 4` (Chebyshev).
* `840 | Q` (since `y≥7`), so every `p≡1 (mod Q)` is ≡1 mod 840, hence
  Mordell-hard, and `p>Q>T`.

## 2. The prime-local residual system and its mass

For `ℓ∈U` define

```
F_ℓ := { −4D mod ℓ :  m ≤ T/ℓ,  mℓ ≡ 3 (4),  D | A_{mℓ}²,  m | 4D+1 },     g(ℓ) := |F_ℓ|/(ℓ−1),   S := Σ_{ℓ∈U} g(ℓ).
```

Every element of `F_ℓ` is a unit mod ℓ, because `gcd(A_{mℓ}, mℓ)=1`.

**Lemma 2.1 (prime-local reduction; PROVED).** Let `n≡1 (mod Q)`. If
`n mod ℓ ∉ F_ℓ` for every `ℓ∈U`, then `W(n)>T`. (The converse also holds, but
it is not needed.)

*Proof.* Let `M≤T` with `M≡3 (4)`. There are two cases.

* **All prime factors of M are `≤y`.** Each prime power `ℓ^e ‖ M` satisfies
  `ℓ^e≤T`, so `M | Q` and `n≡1 (mod M)`. By Fact 1.1, `n mod M∉𝓡(M)`.
* **Otherwise.** Let `ℓ>y` be a prime factor. Since `ℓ²>y²≥T≥M`, we have
  `ℓ ‖ M`. Put `m=M/ℓ`; then `m<T/y≤√T≤y`. So m has no prime factor `>y`,
  hence `m | Q` and `n≡1 (mod m)`.
  * If `n≡−4D (mod M)` with `D | A_M²`, then reducing mod m gives
    `−4D≡1 (mod m)`, i.e. `m | 4D+1`.
  * Reducing mod ℓ then gives `n mod ℓ ∈ F_ℓ`, which contradicts the
    hypothesis. ∎

**Lemma 2.2 (local sizes; PROVED).** Put `τ*(N)=max_{n≤N} τ(n)`. Then for
`ℓ∈U`:

* `|F_ℓ| ≤ (T/ℓ)·τ*(T)²`;
* `g(ℓ) ≤ 2Tτ*(T)²/y² ≤ 2 exp((2 log 2−6+o(1))𝓛/log 𝓛) → 0`.

In particular `max_ℓ g(ℓ) ≤ 1/16` for large T.

*Proof.* For each `m≤T/ℓ`, the number of D is at most `τ(A²)≤τ(A)²`, with
`A≤(T+1)/4`. Then `1/(ℓ−1)≤2/ℓ` and `ℓ>y`. For `τ*`, use Wigert's bound
`log τ(n) ≤ (log 2+o(1)) log n/log log n` (Hardy–Wright Thm 317; classical). ∎

**Lemma 2.3 (the mass with congruence saving; PROVED).** Let `X=(T+1)/4`.
Then

```
S ≤ (4/3)(3+log X) · Σ_{s r² ≤ X, s squarefree} τ(4sr²+1)/(s r)
  ≤ 2(3+𝓛)(1+𝓛)² τ*(T+2) = exp((log 2+o(1)) 𝓛/log 𝓛).
```

*Proof.* `S ≤ Σ_{(m,ℓ,D)} 1/(ℓ−1)`. The sum runs over triples with:

* `ℓ∈U` prime, `mℓ≤T`, `mℓ≡3 (4)`;
* `A:=(mℓ+1)/4`, `D | A²`, `m | 4D+1`.

1. **Halving.** The map `D ↦ A²/D` preserves the condition `m|4D+1`.
   * Indeed `4A≡1 (mod m)` and `4D≡−1`. Hence `D^{−1}≡−4` and
     `4A²D^{−1} ≡ 4·4^{−2}·(−4) = −1`.
   * The map exchanges `D>A` with `D<A`.

   So the number of admissible D is at most `2#{D≤A admissible}`.
2. **Parametrisation.** Write `D=sr²` with s squarefree. Then
   `D|A² ⟺ D*:=sr | A`. Writing `A=srk`, the condition `D≤A` becomes `r≤k`.
   * The map `(m,ℓ,D) ↦ (m,s,r,k)` is injective.
   * `1/(ℓ−1) ≤ 2/ℓ = 2m/(4A−1) ≤ 2m/(3A)`.
3. **The key congruence.** From `m | 4sr²+1` and `m | mℓ = 4srk−1` we get
   `m | 4sr(r+k)`. Also `gcd(m,4sr)=1`, since `m | 4sr²+1`. Hence

   ```
   m | r + k.
   ```

   Since `k≥r≥1` and `r+k>0`, the smallest admissible k is
   `k_0 ≥ max(r, m−r) ≥ m/2`. Therefore

   ```
   Σ_{k≡−r (m), k_0≤k≤X} 1/k ≤ 2/m + (1/m)Σ_{i≤X} 1/i ≤ (3+log X)/m.
   ```

   This is the saving: without step 3 the k-sum would be `≍log X`, with no
   factor `1/m`.
4. **Collecting.** Steps 1–2 give `S ≤ Σ_{(m,s,r,k)} 2·2m/(3srk)`. Step 3
   bounds the k-sum, so
   `S ≤ (4/3)Σ_{s,r} Σ_{m | 4sr²+1} m·(3+log X)/(m·sr)`, which is the first
   display. Here `4sr²+1≤T+2`.
5. **The second display.** It follows from
   `Σ_{s≤X}1/s · Σ_{r≤√X}1/r ≤ (1+log X)(1+½log X)` and Wigert. ∎

**Remarks.**

* *What was missing.* The bound in POINTWISE_SIZE Lemma 11.7 (the same system,
  `y=T^{1/2+η}`) is `f_ℓ ≤ (T/ℓ)T^{o(1)}`, i.e. `S≤T^{1/2−η+o(1)}`. In the
  error budget of Assessment 11.6 that bound exactly cancels the gain of the
  quarantine. Lemma 2.3 removes the `T/ℓ` by the congruence `m | r+k`.
* *EVIDENCE* (`pointwise_omega_S.py`, with `y=√T`):

| T | `#U` | S | `max g` | crude mass (no `m\|4D+1`) | Lemma 2.3 majorant |
|---|---|---|---|---|---|
| 10³ | 157 | 6.48 | 0.326 | 25.2 | 440 |
| 10⁴ | 1204 | 13.56 | 0.211 | 129.6 | 1066 |
| 10⁵ | 9527 | 23.94 | 0.159 | 495.1 | 2195 |
| 10⁶ | 78330 | 38.49 | 0.083 | 1951.7 | 4044 |

  `S/(log T)^{2.5}` takes the values 0.052, 0.053, 0.053, 0.054, so S is
  polylogarithmic in practice. The crude mass grows like `√T`. The majorant
  is far from sharp, but it is `T^{o(1)}`, which is all that is used.
* *Machine check of the algebra* (`pointwise_omega_check.py lemma 3000`).
  It covered 18756 triples `(M,m,D)` with `m|M`, `D|A²` and `m|4D+1`. There
  were 0 failures of the involution and 0 failures of
  `A=srk, k≥r, m|r+k`.
* *Machine check of Lemma 2.1* (`… local`). At `T=1000` it drew 20000 random
  `n≡1 (Q)`, of which 25 survived. At `T=4095` it drew 5000. In both cases
  `W(n)>T ⟺ avoidance` with 0 mismatches. In addition, 2000 forced
  survivors (CRT-sampled from the allowed residues) all have `W(n)>T`
  directly.

## 3. The analytic input

**Theorem 3.1 (Cited: Thorner–Zaman, Math. Z. 306 (2024), arXiv:2108.10878v2, Corollary 1.4 and Remark 1.5; statement read in `sources/lit2026/arxiv-2108.10878-thorner-zaman-pntap.{pdf,txt}`).**
There are absolute, effectively computable constants `c_4>0` and `C_0` with
the following property. Let `q≥2`, let `gcd(a,q)=1`, and let `x≥q^{12}`.
Then

```
Σ_{p≤x, p≡a (q)} log p = (λx/φ(q)) · [1 + ε],
|ε| ≤ C_0 ( exp(−c_4 log x/log q) + exp(−c_4 (log x)^{3/5}/(log log x)^{1/5}) ),
```

where:

* `λ=1−χ_1(a)x^{β_1−1}/β_1` if `β_1` exists, and `λ=1` otherwise;
* `β_1` is the possible exceptional zero for the modulus q. The source (p. 1,
  attributed to McCurley, J. Number Theory 19 (1984)) says that
  `∏_{χ mod q} L(s,χ) ≠ 0` for `Re s ≥ 1 − 1/(13 log(q(|Im s|+3)))`, apart
  from at most one real zero `β_1`. If `β_1` exists it is simple, and
  `L(β_1,χ_1)=0` for a unique nontrivial real character `χ_1 mod q`.

The source also states `0<λ<2` (its (1.7)).

The Deuring–Heilbronn phenomenon enters through the source's log-free density
bound (its Thm 2.1, (2.2), via Jutila). That is what makes the error relative
to λ. McCurley's paper itself was not obtained; we use its statement as
quoted by Thorner–Zaman.

**Lemma 3.2 (one severe character per family; PROVED from the McCurley statement).**
Let `𝒬` be a finite set of moduli, all `≤Z`. Call a pair `(χ*,β)` *severe*
when:

* `χ*` is a real primitive character whose conductor `q*` divides some
  `q∈𝒬`;
* `L(β,χ*)=0` and `β ≥ 1−1/(13 log(3Z²))`.

Then at most one severe pair exists. Moreover, if `(χ*,β*)` is severe and
`q* | q∈𝒬`, then the exceptional pair of Theorem 3.1 for q is `β_1=β*`, with
`χ_1` induced by `χ*`. If no severe pair has `q* | q`, then any exceptional
`β_1` of q satisfies `x^{β_1−1}/β_1 ≤ 2 exp(−log x/(13 log 3Z²))`.

*Proof.*

* **At most one.** Let `(χ_a,β_a)` and `(χ_b,β_b)` be severe, with
  conductors dividing `q_a, q_b ∈ 𝒬`. Put `q'=lcm(q_a,q_b) ≤ Z²`. Both
  characters induce characters mod q′, with the same zeros in `Re s>0`. Both
  β's lie in `[1−1/(13 log 3q'),1)`. By the McCurley statement for q′ there
  is at most one such real zero, it is simple, and its character is unique.
  Hence `β_a=β_b` and `χ_a=χ_b`.
* **Severe, `q* | q`.** Since `q≤Z`, `β*` lies in McCurley's region for q,
  so it is q's exceptional zero.
* **No severe pair with `q* | q`.** An exceptional `β_1` of q that was
  `≥1−1/(13 log 3Z²)` would be severe with conductor dividing q. So
  `x^{β_1−1} ≤ exp(−log x/(13 log 3Z²))`, and `β_1 ≥ 1−1/(13 log 6) > 1/2`. ∎

## 4. A general transfer theorem

**Theorem 4.1 (PROVED modulo Theorem 3.1).** Let `T≥1` and `Q≥2`. Let
`B(n)=Σ_{i∈I} c_i 1[n≡b_i (mod d_i)]` be a finite real combination such that:

* `gcd(d_i,Q)=1` and `gcd(b_i,d_i)=1` for every i;
* `B(n) ≤ 1[W(n)>T]` for every integer `n≡1 (mod Q)`.

Put `Z=Q·max_i d_i`, `μ=Σ_i c_i/φ(d_i)` and `M_1=Σ_i |c_i|/φ(d_i)`. Assume
`μ>0`, and assume the **twist condition**: for every real primitive character
ψ with conductor `f>1`, `gcd(f,Q)=1`, `f | d_i` for some i,

```
|μ_ψ| ≤ μ/4,   μ_ψ := Σ_{i : f | d_i} c_i ψ(b_i)/φ(d_i).
```

Then there is an absolute effective constant `C_1` with the following
property. Let `K=1+log(M_1/μ)`. If
`log x ≥ C_1·K·max(log Z, K)`, then some prime `p≤x` with `p≡1 (mod Q)` has
`W(p)>T`.

*Proof.*

**Setup.** For each i let `q_i=Qd_i` and let `a_i mod q_i` be the CRT class
`≡1 (Q)`, `≡b_i (d_i)`. Then

```
Σ_{p≤x, p≡1 (Q)} log p · B(p) = Σ_i c_i θ(x; q_i, a_i).
```

Here `x≥Z^{12}≥q_i^{12}`. Put

```
E_1 := exp(−c_4 log x/log Z) + exp(−c_4(log x)^{3/5}/(log log x)^{1/5}),
E_2 := exp(−log x/(13 log 3Z²)).
```

Apply Lemma 3.2 to `𝒬={q_i}`. Decompose the conductor of a severe χ* as
`q* = q*_Q q*'`, where `q*_Q` is supported on the primes of Q and
`gcd(q*',Q)=1`. Write `χ*=χ*_Q χ*'` accordingly.

**Case A: a severe χ* exists with `q* | Q`.** Then for every i, Lemma 3.2
gives `λ_i = 1−χ*(a_i)x^{β*−1}/β* = 1−x^{β*−1}/β* =: λ_*`, because
`a_i≡1 (mod q*)`. Also `λ_*>0` once `log x>2`. Theorem 3.1 gives

```
Σ_i c_i θ = (xλ_*/φ(Q)) [μ + Σ_i c_i ε_i/φ(d_i)] ≥ (xλ_*/φ(Q)) [μ − C_0E_1M_1].
```

**Case B: otherwise.** For each i, one of the following holds.

* `q* | q_i` (equivalently `q*_Q | Q` and `q*' | d_i`, with `q*'>1`). Then
  `λ_i = 1−ψ(b_i)x^{β*−1}/β*`, where `ψ:=χ*'`.
* Otherwise `|λ_i−1| ≤ 2E_2`.

Every `λ_i<2`. Hence

```
Σ_i c_i θ ≥ (x/φ(Q)) [ μ − 2|μ_ψ| − M_1(2C_0E_1+2E_2) ] ≥ (x/φ(Q)) [ μ/2 − M_1(2C_0E_1+2E_2) ].
```

Here `x^{β*−1}/β* ≤ 2`, and `μ_ψ` is absent if there is no severe pair or
if `q*_Q ∤ Q`.

**Conclusion.** Both brackets are positive once
`E_1,E_2 ≤ μ/(8(C_0+1)M_1)`. This holds for `log x ≥ C_1 K max(log Z,K)`,
since `u^{3/5}/(log u)^{1/5} ≥ u^{1/2}`. Then
`Σ_p log p·1[W(p)>T] ≥ Σ_p log p·B(p) > 0`. ∎

*Remarks.*

* (i) The theorem never needs a lower bound for `1−β*`. In Case A the
  exceptional factor `λ_*` multiplies main term and error alike (relative
  error with Deuring–Heilbronn). In Case B the exceptional term is a twisted
  mean.
* (ii) The brief's suggested range, PNT uniformly for `q≤exp(c√log x)`,
  would force `log x ≥ (log Z)²/c²`. With `log Z ≥ log Q ≈ y ≥ √T` this is
  linear in T, so the Linnik-range uniformity of Theorem 3.1 is essential.

## 5. The theorem

**Theorem 5.1 (PROVED modulo Theorem 3.1; effective).** For all large T
there is a prime `p≡1 (mod Q)`, hence Mordell-hard, with

```
W(p) > T    and    log p ≤ C_2 · y · (S+1) ≤ T^{1/2}·exp(O(log T/log log T)),
```

where `C_2` is absolute. Consequently, for infinitely many hard primes,
`W(p) ≥ (log p)² exp(−C log log p/log log log p)`. Equivalently
`log L_h(T) ≤ T^{1/2+o(1)}` for all large T.

*Proof.*

**The minorant.** Let J be the least even integer `≥ 22S+10`. Put

```
B(n) := Σ_{P⊆U, |P|≤J−1} (−1)^{|P|} ∏_{ℓ∈P} 1[n mod ℓ ∈ F_ℓ]
      = Σ_{j=0}^{J−1} (−1)^j binom(N(n), j),
N(n) := #{ℓ∈U : n mod ℓ ∈ F_ℓ}.
```

**Pointwise bound.** For `N≥1`, the identity
`Σ_{j≤J−1}(−1)^j binom(N,j) = (−1)^{J−1} binom(N−1,J−1) ≤ 0` holds, since
`J−1` is odd. So `B(n) ≤ 1[N(n)=0] ≤ 1[W(n)>T]` for `n≡1 (Q)`, by
Lemma 2.1. Expanding `1[n mod ℓ∈F_ℓ]=Σ_{a∈F_ℓ}1[n≡a (ℓ)]` writes B in the
shape of Theorem 4.1. The moduli are `d_P=∏_{ℓ∈P}ℓ`, coprime to Q, with
`d_P ≤ T^{J}`; the classes are units.

**Mean and mass.** Let `e_j` be the elementary symmetric functions of the
`g(ℓ)`. Then `μ = Σ_{j<J}(−1)^j e_j(g)` and `M_1 = Σ_{j<J} e_j(g) ≤ e^S`.

* Let N be a sum of independent Bernoulli(`g(ℓ)`) variables. The same
  identity gives `|μ−V| ≤ E binom(N,J) = e_J(g) ≤ S^J/J! ≤ (eS/J)^J ≤ e^{−2J}`,
  where `V=∏(1−g(ℓ)) ≥ e^{−2S}` because `g≤1/16`. (We used
  `binom(N−1,J−1) ≤ binom(N,J)`, which is trivial when `N<J`.)
* Hence `μ ≥ V − e^{−44S−20} ≥ 0.99V`, and `log(M_1/μ) ≤ 3S+1`.

**Twist.** A real primitive ψ with conductor `f>1`, `gcd(f,Q)=1` and `f|d_P`
has `f=∏_{ℓ∈P_f}ℓ` with `P_f⊆U` and `r:=|P_f|≥1`, and `ψ=(·/f)`. Put
`h(ℓ)=Σ_{a∈F_ℓ}(a/ℓ)/(ℓ−1)`, so `|h(ℓ)|≤g(ℓ)≤1/16`. Then

```
μ_ψ = ∏_{ℓ∈P_f} h(ℓ) · Σ_{P'⊆U∖P_f, |P'|≤J−1−r} (−1)^{|P'|} ∏_{P'} g,
```

and this is 0 if `r≥J`. The inner sum is `V'+ε'`, with:

* `V'=V/∏_{P_f}(1−g) ≤ (16/15)^r V`;
* `|ε'| ≤ S^{J−r}/(J−r)!`.

So `|μ_ψ| ≤ (16g_max/15)^r V + g_max^r S^{J−r}/(J−r)!`. The first term is
`≤V/15`. The second term:

* if `r≤J/2`, it is `≤(2eS/J)^{J/2} ≤ e^{−0.7J} ≤ e^{−15S}`;
* if `r>J/2`, it is `≤16^{−J/2}e^S ≤ e^{−29S}`.

Hence `|μ_ψ| ≤ μ/4`.

**Moduli.** `log Z ≤ log Q + J𝓛 ≤ 2y + (22S+12)𝓛 ≤ 3y`, because
`S=T^{o(1)}` (Lemma 2.3) and `y ≥ √T`.

**Conclusion.** Theorem 4.1 gives `p≤x`, `p≡1 (Q)`, `W(p)>T`, with
`log x = C_1(3S+2)·3y`. Here `K≤3S+2≤log Z` for large T.

* With `y=√T exp(3𝓛/log 𝓛)` and Lemma 2.3,
  `log p ≤ √T exp((3+log 2+o(1))𝓛/log 𝓛)`.
* Inverting gives `𝓛 ≥ 2 log log p − O(log log p/log log log p)`.
* Distinct T give infinitely many distinct p, because `W(p)>T`.

Effectivity: Theorem 3.1, McCurley's region, Chebyshev and Wigert are all
effective. ∎

**Corollaries.**

* **Lemma 58.5 (notes).** `liminf log L_p(T)/T = 0`, indeed
  `log L_h(T)/T→0`. So the superlinear question of POINTWISE_SIZE §12 is
  settled in the affirmative.
* **Assessment 7.2, last bullet.** It predicted `W(p)>(log p)^{2−ε}` i.o.
  from RA plus the Haar bound of Lemma 11.7. Theorem 5.1 proves exactly
  this, without RA. Up to `T^{o(1)}` factors, the prime-local construction
  realises the proved Haar scale `log(1/δ*(T)) ≤ T^{1/2+o(1)}`.
* **Theorem 11.2(d).** Its "ceiling of the certified coefficient" applies
  only to the class-of-one certificate, and it is exceeded here.

**EVIDENCE (illustration only).** We take `T=1000` and `y=31`, so
`log Q=66.5`; the class of one would need `log L*≈667`. The first primes
`p=1+kQ` that pass the prime-local sieve have `log p≈75.6–77.4`, with
actual `W(p)=1007, 1151, 1199, 1759, 1475`, i.e. `W/log p≈13–23`
(`pointwise_omega_check.py primes 1000 5`). At such small T,
`log Q_y≈2y` is dominated by the prime powers.

## 6. Above exponent 2: the precise obstruction

### 6.1 Exponent 2 is the ceiling of prime-local designs

Call a design *prime-local* if it consists of the following:

* a set Π of quarantined primes, with `n≡1 (mod ℓ^{e_ℓ})` imposed for
  `ℓ∈Π`;
* the requirement that every `M≤T`, `M≡3 (4)`, has at most one prime factor
  outside Π.

Theorem 5.1 uses such a design.

**Proposition 6.1 (PROVED).** In a prime-local design, Π contains every odd
prime `≤√(T/3)` with at most one exception. Hence
`log ∏_{ℓ∈Π}ℓ ≥ (1/√3−o(1))√T`. Every prime the design produces satisfies
`p≡1 (mod ∏_{Π}ℓ)`, so `log p ≥ (1/√3−o(1))√T`: the certified exponent is
at most `2+o(1)`.

*Proof.* Suppose two odd primes `ℓ_1<ℓ_2≤√(T/3)` lie outside Π. One of
`ℓ_1ℓ_2` and `3ℓ_1ℓ_2` is `≡3 (4)` and `≤T`, and it has two prime factors
outside Π. ∎

If the quarantine class is some `c≠1` modulo `∏_Π ℓ^{e_ℓ}`, the counting
part of the proof still applies. The bound `p>∏_Πℓ` is then replaced by the
requirement `log x≥12 log Z≥12 log∏_Πℓ` of every transfer through Theorem
3.1 or Linnik-range PNT.

*Caveat (as in notes Prop 33.2).* This is a statement about the design, not
about every atom. A two-prime modulus whose atoms are all implied by
single-prime atoms would be harmless. §6.3 shows this does not happen in
general.

### 6.2 What would suffice: H_MIN

**Hypothesis H_MIN(θ)** (0<θ≤1/2; open for `θ<1/2`). For every `ε>0` and
all large T there are `Q` with `840 | Q` and `log Q ≤ T^{θ+ε}`, and a
minorant B as in Theorem 4.1 for the threshold T, such that:

* `log max_i d_i ≤ T^{θ+ε}`;
* `μ>0` and `log(M_1/μ) ≤ T^ε`;
* the twist condition holds.

Since this is a statement about congruence combinatorics on `ℤ/Q·∏d_i`, it
is falsifiable. Primes do not enter it.

**Theorem 6.2 (PROVED modulo Theorem 3.1).** H_MIN(θ) implies
`W(p) > (log p)^{1/θ−ε}` for infinitely many hard primes, for every `ε>0`.
Suppose the polylogarithmic version holds: `log Q`, `log max d_i` and
`log(M_1/μ)` are all `≤(log T)^A`. Then `W(p) > exp(c(log p)^{1/A})`
infinitely often.

*Proof.* Theorem 4.1 gives `log p ≤ C_1(1+T^ε)·2T^{θ+ε}`. ∎

Theorem 5.1 is H_MIN(1/2) (Lemma 2.3 plus Bonferroni). On the Haar side the
corresponding statement is easy: the local lemma, as in notes Thm 31.4 and
POINTWISE_SIZE Lemma 11.7, gives void probabilities. What is missing is a
**pointwise** minorant of bounded modulus and ℓ¹-mass (notes Lemma 33.3, now
for units and primes). The prime side (moduli, Siegel zeros, ℓ¹-mass) is
completely handled by Theorem 4.1.

### 6.3 Why event-level Bonferroni does not give H_MIN(θ) for θ<1/2

Let `y=T^θ` with `θ<1/2`, quarantine the primes `≤y` as in §1, and take as
events the atoms `(M,c)`, `c∈𝓡(M)`, compatible with the quarantine. The
degree-`(J−1)` Bonferroni minorant `B_J=Σ_{j<J}(−1)^j binom(N,j)` (J even)
has mean `P(N=0) − E[binom(N−1,J−1)1_{N≥1}]`, in the CRT measure on the
class `1 (Q)`.

**Proposition 6.3 (PROVED for the raw atom list).** For `θ<1/2` fixed and T
large, every even `J ≥ (4.2θ²+o(1))(log T)²` gives `E[B_J]<0`.

*Proof.* Take r primes `≡1 (4)` and r primes `≡3 (4)` in `(y,2y]`, where
`r=⌈√(2J−1)⌉` (there are enough of them). Let `n≡−4` modulo all of them.
For every cross pair the modulus `M=ℓℓ'` is `≤4y²≤T` and `≡3 (4)`. The atom
`D=1` gives the class `−4 mod M`, so `N(n) ≥ r² ≥ 2J−1`. The CRT probability
of this configuration is at least `(2y)^{−2r}`. Hence

```
E binom(N−1,J−1) ≥ (2y)^{−2r}·binom(2J−2,J−1) ≥ exp((J−1)log 4 − log(2J−1) − 2r(θ𝓛+log 2)).
```

This exceeds `1>P(N=0)` once `J log 4 > 2√(2J)θ𝓛(1+o(1))`, i.e. for
`J>(2√2θ/log 4)²𝓛²(1+o(1)) = 4.16θ²𝓛²(1+o(1))`. ∎

**Deleting implied atoms does not remove the phenomenon (EVIDENCE;
`pointwise_omega_check.py pairs`).**

* The D=1 hubs above are implied by the single-prime atom
  `(ℓ', −4)` for `ℓ'≡3 (4)`. So we tested the reduced system, in which an
  atom is deleted if its residue at some of its free primes is already in
  the single-prime set `F_ℓ`.
* At `T=10^4` and `T=10^5`, for `θ=0.3, 0.4, 0.45`, between 51% and 65% of
  all multi-prime atoms are irredundant.
* Hub classes persist. At `T=10^5`, `θ=0.4`, the classes `−16, −36, −12`
  (`D=4, 9, 3`, firing when `2|A` resp. `3|A`) carry 331, 320 and 299
  irredundant two-prime atoms on about 72 primes each.

The proof of Prop 6.3 applies verbatim to any hub class whose bipartite
two-prime graph contains `K_{r,r}` with `r≈√(2J)`. There are hub classes
`−4d²` for every d (they fire when `d|A`).

Quarantining hub residues voluntarily does not help. Forbidding hub classes
`−4d²` for `d≤d_0` costs about `e^{−O(d_0)}` in density. But hubs with
`d≤e^{c√J}` still contribute `≳4^J e^{−O(√J log(dJ))}` to the truncation
error, so `d_0` would have to be `e^{c√J}` (Assessment).

The plain truncation also needs `J≳e²S`. With `S≈0.054(log T)^{2.5}`
(EVIDENCE, §2), this exceeds the threshold of Prop 6.3 at every T of
interest (Assessment).

**Assessment 6.4 (what a proof above exponent 2 needs).** A proof above
exponent 2 needs a hypergraph sieve minorant. It must be pointwise, with the
modulus and ℓ¹-mass budgets of H_MIN, and its truncation must be adapted to
hubs, for instance:

* per-vertex degree truncation (Brun–Hooley grouping by the largest free
  prime, with conditional forbidden sets `F_ℓ(history)`);
* a cluster expansion whose polymers are the hub stars.

This is the "convergent hypergraph-sieve or event-cluster minorant" of
notes Lemma 33.3, now in the unit/prime setting, where the transfer side is
proved (Theorem 4.1). The sibling ingredients of the brief have been
handled: (ii) the transfer with moduli `exp(T^{θ})` in the Linnik range, and
(iii) Siegel zeros. Only (iv) remains, in the exact form H_MIN.

## 7. Position relative to the campaign documents

* **POINTWISE_SIZE.**
  * §11.3, Assessment 11.6. Its error budget `log x ≳ log Q·log(1/V)` is
    right. The crude `log(1/V)≤T^{1/2−η}` was the bottleneck, and Lemma 2.3
    replaces it by `T^{o(1)}`.
  * §11.3's "possible route" (polylogarithmic quarantine) is H_MIN with
    `θ→0`. It remains open, for the reason located in §6.3.
  * §7.3(i)'s missing mean value is Lemma 2.3, in the prime-local setting.
* **Notes.**
  * §54: `H_MOD(A)` (notes (51.19): `W(p)≤(log p)^A` for every sufficiently
    large prime p) is now refuted unconditionally for every `A<2`. Notes
    Cor. 54.2 refuted only `A<1`, and POINTWISE_SIZE Thm 11.2 did not reach
    `A=1`. The open pointwise range becomes `A≥2`; heuristically it is empty
    (Assessment 7.2).
  * Thm 56.1 and Prop 11.2'' (complete certificates cost `(2/3)T`) are
    untouched. Our certificate is not complete: it is a sieve over many
    classes.
  * §58: `log L_h(T)≤T^{1/2+o(1)}` replaces (58.18)/Thm 11.2(b) as the
    upper end.
* **Upper side** (notes §51, Thm 51.2(1)): `#{p≤N : W(p)>T} ≪ N exp{−c(log T)² log log T}`
  when `log N ≳ (log T)^3 log log T`. At `T=(log N)^{2−o(1)}` this bound
  is `N exp{−c'(log log N)² log log log N}`. That is compatible with
  Theorem 5.1, which supplies at least one such prime for infinitely many N.
  The two results bracket the exceptional set at this threshold: it is
  non-empty i.o., and it has density `≤ exp{−c'(log log N)^{2+o(1)}}`.
* **Type I frame** (`ck_min`, Thm 11.2′). Not treated. A prime-local
  analysis of the genus-forcing atoms would be needed (open).

## Replay

```
export PYTHONPATH=scripts
for T in 1000 10000 100000; do uv run python scripts/pointwise_omega_S.py $T 0.5; done      # < 1 min
(ulimit -v 12000000; uv run python scripts/pointwise_omega_S.py 1000000 0.5)                # ~25 min -> data/pointwise_omega/S_1e6.txt
C="uv run python scripts/pointwise_omega_check.py"
$C lemma 3000                      # Lemma 2.3 algebra, ~10 s
$C local 1000 20000 1              # Lemma 2.1, ~1 min
$C local 4095 5000 2               # ~3 min
$C primes 1000 5                   # example primes, ~1 min
$C pairs 10000 0.3; $C pairs 10000 0.4; $C pairs 10000 0.45     # §6.3, ~1 min each
$C pairs 100000 0.4                # ~5 min -> data/pointwise_omega/pairs_1e5_0.4.txt
```
