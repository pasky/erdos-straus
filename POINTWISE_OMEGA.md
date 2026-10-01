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
   and `log p ≪ K·max(log(Q·max d_i), K)`, where `K=1+log(M_1/μ)`. The
   Siegel-zero problem
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
     A polylogarithmic H_MIN (budgets `≤(log T)^A`) gives
     `W(p) > exp(c(log p)^{1/(2A)})`.
   * **(c) PROVED / EVIDENCE.** The natural candidate fails: event-level
     Bonferroni of degree J in the range `4.2θ²(log T)²(1+o(1)) ≤ J ≤ T^θ`
     has negative mean on the raw atom list for `θ<1/2` (Prop 6.3). The cause is "hub" classes (`−4d²`, …) at which many
     two-prime atoms fire together. This is notes §33's correlation wall in
     exact form. EVIDENCE: hubs survive the deletion of atoms implied by
     single-prime atoms (51–65% of the multi-prime atoms are irredundant at
     `T=10^4, 10^5`).

5. **Checkpoint 2 additions (§§8–9).**
   * **Type-I frame (§8).**
     * `ck_min(p) ≥ n_p` (Lemma 8.1, PROVED).
     * Jointly, `W ≥ (log p)^{2−o(1)}` and `ck_min ≥ (log p)^{1−o(1)}` hold
       i.o. (Cor. 8.2, PROVED modulo Thm 3.1).
     * Complete Type-I certificates force quadratic residuosity at every
       `5≤ℓ≤T` (Prop. 8.3, PROVED).
     * Hence any congruence method certifies exactly `ck_min>n_p`
       (Cor. 8.4, PROVED). Exponent `1+δ` for `ck_min` by congruences would
       beat every known Ω-result for the least quadratic non-residue.
   * **Haar side (§9; Haar only, says nothing about primes).**
     * Structural lemma: surviving atoms have smooth part `m≤r²+1`
       (Lemma 9.1, PROVED).
     * The global surviving mass is `≪(log T)^4 log log T` for every
       class-of-one quarantine (Lemma 9.2, PROVED modulo Elsholtz–Tao
       Prop. 1.4).
     * **`log(1/δ*(T)) ≤ T^{1/3+o(1)}` unconditionally** (Theorem 9.3,
       PROVED). This improves POINTWISE_SIZE Lemma 11.7's `1/2`.
     * The polylogarithmic bound `δ*(T) ≥ exp(−(log T)^{O(1)})` follows
       from the per-prime Hypothesis H_PP (Theorem 9.4, PROVED
       implication). H_PP itself is open, with EVIDENCE.

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
μ_ψ = (−1)^r ∏_{ℓ∈P_f} h(ℓ) · Σ_{P'⊆U∖P_f, |P'|≤J−1−r} (−1)^{|P'|} ∏_{P'} g,
```

and this is 0 if `r≥J`. The inner sum is `V'+ε'`, with:

* `V'=V/∏_{P_f}(1−g) ≤ (16/15)^r V`;
* `|ε'| ≤ S^{J−r}/(J−r)!`.

So `|μ_ψ| ≤ (16g_max/15)^r V + g_max^r S^{J−r}/(J−r)!`. The first term is
`≤V/15`. The second term:

* if `r≤J/2`, it is `≤(2eS/J)^{J/2} ≤ (e/11)^{J/2} ≤ e^{−0.69J} ≤ e^{−15S−6}`.
  Here `½ log(11/e) = 0.6989…`.
* if `r>J/2`, it is `≤16^{−J/2}e^S ≤ e^{−29S}`.

Hence `|μ_ψ| ≤ μ/4`.

**Moduli.** `log Z ≤ log Q + J𝓛 ≤ 2y + (22S+12)𝓛 ≤ 3y`, because
`S=T^{o(1)}` (Lemma 2.3) and `y ≥ √T`.

**Conclusion.** Theorem 4.1 gives `p≤x`, `p≡1 (Q)`, `W(p)>T`, with
`log x = C_1(3S+2)·3y`. Here `K≤3S+2≤log Z` for large T.

* With `y=√T exp(3𝓛/log 𝓛)` and Lemma 2.3,
  `log p ≤ √T exp((3+log 2+o(1))𝓛/log 𝓛)`.
* Inverting gives `𝓛 ≥ 2 log log p − O(log log p/log log log p)`.
* Infinitely many distinct p arise, because `p>Q>T` (Fact 1.2). Note that
  `W(p)>T` alone would not suffice for this, since finiteness of `W(p)` is
  not known.

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
`log(M_1/μ)` are all `≤(log T)^A`. Then `W(p) > exp(c(log p)^{1/(2A)})`
infinitely often.

*Proof.* First make Q exceed T. Let `ℓ_0` be a prime in
`(R,2R]`, where `R=max(T, max_i d_i)`, and replace Q by `Qℓ_0`. The minorant
inequality still holds on the smaller class `1 mod Qℓ_0`. The moduli `d_i`
stay coprime to `Qℓ_0`, and `μ`, `M_1` and every `μ_ψ` are unchanged.
Finally `log Z` grows by at most `log 2R`.

Now Theorem 4.1 gives a prime `p≡1 (mod Qℓ_0)`, so `p>T`, with

```
log p ≤ C_1 K max(log Z, K),   K ≤ 1+T^ε,   log Z ≤ 3T^{θ+ε} + log 2T.
```

Hence `log p ≤ T^{θ+2ε+o(1)}`, and distinct T give infinitely many distinct
p. In the polylogarithmic case the same computation gives
`log p ≪ (log T)^{2A}`. ∎

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
large, every even J with `(4.2θ²+o(1))(log T)² ≤ J ≤ y` gives `E[B_J]<0`.
Some upper limit on J is necessary. At most one atom per modulus fires, so
`N ≤ (T+1)/4`, and for `J>(T+1)/4` the truncation is exact,
`B_J=1[N=0]`, with positive mean. The method itself needs only `J≍S`.

*Proof.* Take r primes `≡1 (4)` and r primes `≡3 (4)` in `(y,2y]`, where
`r=⌈√(2J−1)⌉`. Since `J≤y`, we have `r≤√(2y)+1`, which is far below the
`≍y/(2 log y)` primes of each class in `(y,2y]`. Let `n≡−4` modulo all of them.
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

The proof of Prop 6.3 applies verbatim to any hub class whose
bipartite two-prime graph of irredundant atoms contains `K_{r,r}` with
`r≈√(2J)`. There are hub classes `−4d²` for every d (they fire when `d|A`).
We have **not** shown that the reduced hub graphs contain such complete
bipartite subgraphs asymptotically. The surviving edges counted above are
EVIDENCE that the clustering persists after deduplication. They are not a
proof that deduplicated Bonferroni fails.

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

## 8. The Type-I frame (`ck_min`): the congruence route is the least-quadratic-non-residue problem

Checkpoint 2, task (c). Notation as in notes §§44, 48, 50. A slice is a
pair `(c,k)∈𝓑_p` (notes (36.1)), with `h=4ck`, `N_{c,k}=p²+4ck²`, core
`s=sf(c)`, and genus character `χ_s=(Δ_s/·)`, where `Δ_s<0` is the
fundamental discriminant of `ℚ(√−s)`. `M_{c,k}(p)` is the number of divisors
of `N_{c,k}` that are `≡−p (mod h)` (notes (44.2)). Finally
`ck_min(p)=min{ck : (c,k)∈𝓑_p, sf(c)∉{1,2,3,6}, M_{c,k}(p)>0}`
(notes (48.9)).

The question was whether the prime-local analysis gives `(log p)^{2−o(1)}`
for `ck_min` too, alone or jointly with W.

**Answer.** Only `(log p)^{1−o(1)}` jointly with Theorem 5.1. Every congruence
method for `ck_min` is exactly the least-quadratic-non-residue Ω-problem. A
congruence proof of `ck_min(p)>(log p)^{1+δ}` i.o. would beat every known
Ω-result for the least non-residue.

The structural reason is a contrast between the two frames.

* `W(p)>T` is a pure congruence condition on p (notes (58.3)).
* `M_{c,k}(p)=0` is a congruence condition only through the genus character
  (Theorem 48.1). On an unforced class it is a factorisation event for
  `p²+4ck²`, and no congruence class forces it (notes Cor. 52.2).

**Lemma 8.1 (genus depth ≥ least non-residue; PROVED from notes Thm 48.1).**
Let `p≡1 (mod 24)` be prime, `B≥1`, and suppose `(ℓ/p)=1` for every prime
`5≤ℓ≤B`. Then `ck_min(p)>B`. In particular, if `n_p` denotes the least
quadratic non-residue mod p, then `ck_min(p) ≥ n_p` for every prime
`p≡1 (24)`.

*Proof.* Take `(c,k)∈𝓑_p` with `ck≤B`, and put `s=sf(c)≤B`. Since
`Δ_s∈{−s,−4s}`, we have `χ_s(p)=(−s/p)=(−1/p)∏_{q|s}(q/p)`. Each factor is
1:

* `(−1/p)=(2/p)=(3/p)=1` because `p≡1 (24)`;
* `(q/p)=1` for `5≤q≤B` by hypothesis.

Theorem 48.1 then gives `M_{c,k}(p)=0`. For the second sentence: `n_p` is
prime, and 2 and 3 are residues, so `n_p≥5` and every prime `5≤ℓ<n_p` is a
residue. ∎

*EVIDENCE* (`pointwise_omega_check.py typeI 30000 200`). Among the 385
primes `p≡1 (24)` below 30000, every one has `ck_min(p)≥n_p`, and 238 of
them have equality. The engine reproduces the notes (48.12) records
(`ck_min=7, 10, 11, 13, 21, 26, 38, 67, 77` at `p=73, …, 12289`). So the genus
depth is often the exact depth at small p. The large records, e.g.
`ck_min(12289)=77` against `n_p=11`, are factorisation conspiracies.

**Corollary 8.2 (joint Ω-result; PROVED modulo Theorem 3.1).** There are
infinitely many hard primes with both:

```
W(p) ≥ (log p)^2·exp(−C log log p/log log log p),
ck_min(p) ≥ log p · exp(−C log log p/log log log p).
```

*Proof.* The primes of Theorem 5.1 satisfy `p≡1 (mod ℓ)` for every
`ℓ≤y`, hence `(ℓ/p)=1`. Lemma 8.1 gives `ck_min(p)>y`. From §5,
`y=√T e^{3𝓛/log 𝓛}` and `log p ≤ √T e^{(3+log 2+o(1))𝓛/log 𝓛}`. Hence
`y ≥ log p·e^{−(log 2+o(1))𝓛/log 𝓛}`, with `𝓛∼2 log log p`. ∎

For `ck_min` alone, POINTWISE_SIZE Thm 11.2′ gives `(5/12−ε)log p`, which is
linear. Corollary 8.2 trades a factor `(log p)^{o(1)}` in `ck_min` for
exponent 2 in W. It does not improve `ck_min` alone.

**Proposition 8.3 (complete Type-I certificates force quadratic residuosity; PROVED).**
Let `24 | L`, and let `a mod L` be a reduced class with `a≡1 (24)`. Suppose
every sufficiently large prime `p≡a (mod L)` has `ck_min(p)>T`. Then every
prime `5≤ℓ≤T` divides L, and `(a/ℓ)=1`.

The divisibility statement is notes Thm 56.2; the residuosity statement is
new.

*Proof.* Suppose a prime `5≤ℓ≤T` has `ℓ∤L` or `(a/ℓ)=−1`. We produce
primes in the class with `M_{ℓ,1}(p)>0`.

1. **A class mod 4ℓ.** Choose `c_0 mod 4ℓ` with `c_0≡a (mod gcd(L,4ℓ))`,
   `c_0≡1 (4)`, and `(c_0/ℓ)=−1`. This is possible: if `ℓ∤L` the residue mod
   ℓ is free, and otherwise take `c_0≡a`.
2. **The genus value.** For `n≡1 (4)`, reciprocity gives
   `χ_ℓ(n)=(−ℓ/n)=(n/ℓ)`, so `χ_ℓ(c_0)=−1`.
3. **An auxiliary prime q.** By Dirichlet choose a prime `q≡−c_0 (mod 4ℓ)`
   with `q∤L`. Then `χ_ℓ(q)=χ_ℓ(−1)χ_ℓ(c_0)=1`, i.e. `(−ℓ/q)=1`, so there
   is an ρ with `ρ²≡−4ℓ (mod q)`.
4. **The primes p.** By CRT and Dirichlet there are infinitely many primes
   p with `p≡a (L)`, `p≡c_0 (4ℓ)` and `p≡ρ (q)`. These conditions are
   compatible because `c_0≡a` on `gcd(L,4ℓ)` and `q∤4ℓL`.
5. **Conclusion.** For each such p, `q | p²+4ℓ=N_{ℓ,1}` and
   `q≡−c_0≡−p (mod 4ℓ=h)`. So q is a divisor in the target grade and
   `M_{ℓ,1}(p)≥1` (notes Thm 50.1). Also `(ℓ,1)∈𝓑_p` for large p, and
   `sf(ℓ)=ℓ∉{1,2,3,6}`. Hence `ck_min(p)≤ℓ≤T`, a contradiction. ∎

**Corollary 8.4 (the Type-I congruence route certifies exactly `n_p`; PROVED).**
Let `24 | Q`. Let `B(n)=Σ_i c_i 1[n≡b_i (d_i)]` be any finite congruence
combination with `B(p) ≤ 1[ck_min(p)>T]` for all sufficiently large primes
`p≡1 (mod Q)`, e.g. a minorant as in Theorem 4.1 with `ck_min` in place of
W. Then every sufficiently large prime p with `p≡1 (Q)` and `B(p)>0` has
`n_p>T`.

*Proof.* B is periodic mod `L=lcm(Q,d_i)`. If `B(p)>0`, then B is the same
positive value on the whole class `a=p mod L`. So every large prime in that
class has `ck_min>T`. Proposition 8.3 gives `(a/ℓ)=1` for `5≤ℓ≤T`, hence
`(ℓ/p)=(p/ℓ)=1` by reciprocity (`p≡1 (4)`). Also `(2/p)=(3/p)=1`, so
`n_p>T`. ∎

So Lemma 8.1 and Corollary 8.4 together say: **the `ck_min` depth that any
congruence method can certify at p is exactly `n_p`** (for `p≡1 (24)`). The
consequences follow.

* **Known Ω-results for `n_p` transfer only in part.** These are stated in
  the archived secondary source `sources/lit2026/lau-wu-least-quadratic-nonresidue.pdf`,
  Lau–Wu §1; the primary sources were not obtained:
  * unconditionally, Graham–Ringrose (1990): `n_p=Ω(log p·log log log p)`;
  * under GRH, Montgomery: `Ω(log p·log log p)`;
  * under GRH, Ankeny: `n_p ≪ (log p)²`.

  If the Graham–Ringrose primes can be taken `≡1 (mod 24)`, Lemma 8.1 gives
  `ck_min(p) ≫ log p·log log log p` infinitely often, which would be the
  first superlinear `ck_min` result. **Not claimed.** We have not checked
  that their construction allows this congruence condition; `p≡1 (4)` is the
  issue, since `(2/p)=(3/p)=1` is automatic once `n_p>3`.
* **The ceiling.** Corollary 8.4 shows that a congruence proof of
  `ck_min(p)>(log p)^{1+δ}` i.o. would prove `n_p>(log p)^{1+δ}` i.o. That
  exceeds every known Ω-result above, unconditional or under GRH. It also
  exceeds the standard random-model prediction
  `max_{p≤x} n_p ≍ log x·log log x`, where
  `#{p≤x}·2^{−π(T)} ≈ 1` gives `π(T)≈log x/log 2` (Assessment). Even under
  GRH, Ankeny's bound caps the congruence-certified `ck_min` at
  `O((log p)²)`.
* **Comparison with W.** For W, the prime-local construction reaches
  exponent 2 because a single quarantine `p≡1 (mod ℓ)` kills every atom of
  every y-smooth modulus. For `ck_min`, the only congruence-killable slices
  are those with `χ_s(p)=1`. Killing all slices with `ck≤T` forces `(ℓ/p)=1`
  at every `ℓ≤T`. As a sieve condition this has local density `1/2` at every
  free prime: mass `≍T/log T`, not `T^{o(1)}`. So no quarantine-plus-sieve
  design helps.
* **The true size of `ck_min`.** Beyond `n_p`, slice vanishing is a
  factorisation event: there is no good prime-power factor of
  `p²+4ck²` in a single ray class. Making all unforced slices with `ck≤T`
  vanish is a lower-bound sieve problem of growing dimension
  `≍Σ_{ck≤T}1/φ(4ck)≍(log T)²` on polynomial values sifted to `√N`. This is
  the dimension barrier of POINTWISE_SIZE Assessment 11.5, now for slices
  (Assessment).

## 9. The Haar side: a structural lemma, the global mass, `δ*(T) ≥ exp(−T^{1/3+o(1)})`, and the polylog bound under a per-prime hypothesis

Checkpoint 2, task (a). **Everything in this section is about the Haar
(CRT) measure only.** It says nothing about primes: the local lemma is not
a pointwise minorant (notes §33), and the transfer to primes still needs
H_MIN (§6.2). Recall POINTWISE_SIZE §7.1:

* `δ*(T)` is the Haar measure of `{n∈Ẑ^× : n≡1 (24), n mod M∉𝓡(M) ∀M≤T}`,
  normalised within the class `1 (24)`;
* Lemma 11.7 proves `log(1/δ*) ≤ T^{1/2+o(1)}`;
* the measured value is `log(1/δ*) ≍ (log T)^{2.3…2.6}`.

**Setting.** Quarantine the class of one at all primes `≤z`:
`n≡1 (mod Q_z)`, `Q_z=lcm(24, ℓ^{e_ℓ}: ℓ≤z, ℓ^{e_ℓ}≤T maximal)`. For
`M≤T`, `M≡3 (4)`, write `M=m·r`, with m the z-smooth part and r the
z-rough part. If `r=1`, M is killed by the class of one (Fact 1.1).
Otherwise the atoms of M that survive the conditioning are the `D | A_M²`
with `m | 4D+1`. Each gives the event `n≡−4D (mod r)`, of conditional Haar
probability `1/φ(r)`.

**Lemma 9.1 (structural lemma: the smooth part is at most quadratic in the rough part; PROVED).**
Let `M≡3 (4)`, `D | A_M²`, and `M=m·r` with `m | 4D+1`. Then `m ≤ r²+1`, so
`M ≤ r³+r`. Moreover, for a prime ℓ the single-prime atoms with `r=ℓ` and
`D≤A` correspond bijectively to triples `(s,r',v)` with:

* s squarefree, `n:=sr' ≤ ℓ/2`;
* `v | 4nr'+1` and `4n | ℓ+v`;
* `k := m(ℓ+v)/(4n) − r' ≥ r'`, where `m=(4nr'+1)/v`, and `mℓ≡3 (4)`.

The atom is `D=sr'²`, `A=sr'k`. Its class is `−4D mod ℓ`, and the partner
`A²/D` has class `−(4D)^{−1} mod ℓ`.

*Proof.* By the involution of Lemma 2.3, which preserves `m | 4D+1`
because `m | M`, we may take `D≤A`. Write `D=sr'²` and `A=sr'k` with
`k≥r'`. As in Lemma 2.3, `m | r'+k`, so `m ≤ r'+k ≤ 2k`. Then

```
r = (4sr'k−1)/m ≥ 2sr' − 1/(2k)   ⇒   r ≥ 2sr'.
```

Hence `m ≤ 4sr'²+1 ≤ 4(sr')²+1 ≤ r²+1`.

For the parametrisation, put `v=(4sr'²+1)/m`. Then

```
m(vk−ℓr') = (4sr'²+1)k − (4sr'k−1)r' = r'+k,
```

so `vk−ℓr'=(r'+k)/m =: e`. Substituting `k=me−r'` gives
`e(mv−1)=r'(ℓ+v)`, i.e. `e=(ℓ+v)/(4sr')`. This yields the stated
conditions. The converse is direct. The partner class follows from
`4A≡1 (mod ℓ)`. ∎

*Consequence.* The single-prime forbidden set
`F_ℓ^{(z)}⊆F_ℓ^{full}` (the set over all m) is a T-independent object. It
is determined by atoms with `M≤ℓ³+ℓ`. In particular the `F_ℓ` of §2 satisfy
`F_ℓ⊆F_ℓ^{full}`.

EVIDENCE:

* `pointwise_omega_haar.py`: 0 violations of `m≤r²+1` over all 3.8·10⁶
  surviving atoms at `T=10^6` and 0.3–0.8·10⁶ at `T=10^5`.
* The parametrisation agrees with direct enumeration for all primes
  `ℓ<200` (0 mismatches).
* `|F_ℓ^{full}|` grows polylogarithmically: `|F_ℓ^{full}|/(log ℓ)²` lies
  between 0.4 and 4.8 for sampled primes `10²<ℓ<4·10⁴`, and
  `g=|F|/(ℓ−1)` falls from about 0.16 to 0.004
  (`data/pointwise_omega/Ffull.txt`).

**Lemma 9.2 (global mass after any class-of-one quarantine; PROVED, the polylog form modulo a cited bound).**
For every `2≤z≤T`,

```
S_tot(T,z) := Σ_{surviving atoms} 1/φ(r) ≤ C (log log T)(3+log T) Σ_{sr'²≤T} τ(4sr'²+1)/(sr').
```

The right-hand side is `≤ exp(O(log T/log log T))` by the divisor bound
alone. It is `≪ (log T)^4 log log T` by Elsholtz–Tao (arXiv:1107.1010,
Prop. 1.4, archived as `sources/elsholtz-tao-1107.1010.pdf`; cited):
`Σ_{a≤A,b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)` for `k≪(AB)^{O(1)}`.

*Proof.* Since r has all prime factors `>z≥2`,
`1/φ(r) ≤ C log log T/r = C log log T·m/M`. From here the proof is that of
Lemma 2.3, with `m=m_M` and the prime ℓ replaced by `r=M/m`. The only
change is the weight: `m/M ≤ m/(3A)` replaces `2m/(3A)`. Every surviving
atom has `m | gcd(4D+1, M)`, so `m | r'+k` as before, and the k-sum gives
`(3+log X)/m`. For the polylog form, split s and r′ dyadically and apply
Prop. 1.4 with `k=4` on each block. Each of the `O((log T)²)` blocks
contributes `O(log T)`. ∎

The bound is uniform in z. For `z≥√T` it is Lemma 2.3. EVIDENCE: at
`T=10^5`, `S_tot=49.7, 39.2, 29.8, 24.2, 17.9` for
`z=5, 20, 100, 300, 1000`; at `T=10^6`, `S_tot=38.5` and `30.6` for
`z=10³` and `3·10³`.

**Theorem 9.3 (unconditional: `log(1/δ*(T)) ≤ T^{1/3+o(1)}`; PROVED, Haar only).**
This improves POINTWISE_SIZE Lemma 11.7 (`T^{1/2+o(1)}`).

*Proof.* Fix `ε>0` and put `y=T^{1/3+ε}`, quarantining as above with
`z=y`.

1. **The events.** Every z-rough part `r≤T` has at most two prime factors
   with multiplicity, so `r∈{ℓ, ℓ², ℓ_1ℓ_2}`. Use the independent
   coordinates `X_ℓ = n mod ℓ^{e_ℓ}`, with `e_ℓ∈{1,2}`.
   * Single atoms (`r=ℓ` or `ℓ²`) form a forbidden set `G_ℓ` with
     `g_ℓ ≤ Σ 1/φ(r)` over these atoms.
   * `1∉G_ℓ` by Fact 1.1.
   * Pair atoms are classes mod `ℓ_1ℓ_2`.
2. **Bad primes.** Let `B={ℓ : g_ℓ>1/4}`. Then
   `|B| ≤ 4S_tot ≤ T^{o(1)}` (Lemma 9.2). Quarantine B as well, with
   `n≡1 (mod ℓ^{e_ℓ})` for `ℓ∈B`. This costs `|B| log T = T^{o(1)}`.
   * Pair atoms with both primes in B become impossible, by Fact 1.1.
   * A pair atom `(ℓb, a)` with `b∈B` becomes the residue `a mod ℓ` at ℓ if
     `a≡1 (b)`, and is impossible otherwise.
   * The enlarged forbidden set `G'_ℓ` at a good prime satisfies
     `g'_ℓ ≤ 1/4 + |B|·τ(·)²_{max}·T/(ℓ y(ℓ−1)) ≤ 1/4 + T^{−3ε+o(1)} ≤ 1/2`.
   * The added mass is
     `Σ_ℓ (g'_ℓ−g_ℓ) ≤ |B| τ²_{max} T/y² = T^{1/3−2ε+o(1)}`.
3. **Good pairs by the local lemma.** Under the product measure μ′
   (uniform on the allowed residues at each good prime), a good pair event
   `E=(ℓ_1ℓ_2,a)` has `μ'(E) ≤ 4/((ℓ_1−1)(ℓ_2−1))`. Its per-prime weight is

   ```
   w'_ℓ ≤ Σ_{ℓ'>y} (T/(ℓℓ'))τ²_max · 4/((ℓ−1)(ℓ'−1)) ≤ 16 τ²_max T/(ℓ² y) ≤ T^{1−3(1/3+ε)+o(1)} = T^{−3ε+o(1)},
   ```

   where `τ²_max=max_{A≤T}τ(A²)=T^{o(1)}`. Every event has at most two
   primes. The asymmetric local lemma (Erdős–Lovász; Alon–Spencer
   Lemma 5.1.1; classical) with `x_E=2μ'(E)` therefore applies for large T.
   It gives
   `μ'(no good pair event) ≥ ∏(1−2μ'(E)) ≥ exp(−16 S_tot)`.
4. **Collecting.**

   ```
   δ*(T) ≥ (8/φ(Q')) · ∏_{good}(1−g'_ℓ) · exp(−16S_tot)
         ≥ exp(−π(y) log T − |B| log T − 2(S_tot + T^{1/3−2ε+o(1)}) − 16 S_tot)
         = exp(−T^{1/3+ε+o(1)}).  ∎
   ```

Where the exponent `1/3` comes from: it is the crude per-prime bound for
multi-prime events, `N(M)≤τ(A²)` with no congruence saving at fixed ℓ.
That bound gives `w_ℓ^{multi} ≲ T/(ℓ²y)` regardless of the number of rough
primes. So with the quarantine at y, the local lemma closes iff `y³>T`.

**Hypothesis H_PP(z) (per-prime mass).** For all primes `z<ℓ≤T`:

```
w_ℓ(T,z) := Σ_{surviving events E : ℓ | r_E} 1/φ(r_E) ≤ log z/(8 log T).
```

**Theorem 9.4 (PROVED implication; Haar only).**

* If H_PP(z) holds, then
  `δ*(T) ≥ (8/φ(Q_z))·exp(−4S_tot(T,z)) ≥ exp(−(1+o(1))π(z)log T − O((log T)^4 log log T))`.
* If H_PP(`(log T)^C`) holds for all large T, then
  `log(1/δ*(T)) ≪ (log T)^{max(C+1,4)+o(1)}`. This is the polylogarithmic
  Haar bound of the brief's step (i).

*Proof.*

* **The space and the graph.** Take the product space of the coordinates
  `X_ℓ` (`ℓ>z`), uniform on units, and the distinct events `E=(r,a)`.
  Join two events when their rough parts share a prime.
* **Local lemma.** Use `x_E=2/φ(r_E) ≤ 1/2`. Each E has at most
  `ω(r_E) ≤ log T/log z` primes, so
  `∏_{E'∼E}(1−x_{E'}) ≥ exp(−4Σ_{ℓ|r_E}w_ℓ) ≥ e^{−1/2}`. This verifies
  the asymmetric condition, and
  `P(no event) ≥ ∏(1−x_E) ≥ exp(−4S_tot)`.
* **Quarantine cost.** It is `φ(24)/φ(Q_z)`, with
  `log φ(Q_z) ≤ π(z) log T`. ∎

**What H_PP needs, and the evidence.** `w_ℓ` splits into two parts.

* **The single-prime part `|F_ℓ^{(z)}|/(ℓ−1)`.** It is at most
  `|F_ℓ^{full}|/(ℓ−1)`, a T-independent quantity, with
  `|F^{full}_ℓ| ≈ (log ℓ)^{2+}` (Lemma 9.1 evidence). So at
  `ℓ>z=(log T)^C` it is about `(C log log T)^{2+}/(log T)^C`.
* **The multi-prime part.** EVIDENCE: `max_ℓ ℓ·w^{multi}_ℓ` is 13 at
  `z=100` and 0.68 at `z=300` (`T=10^5`).

The full ratio `max_ℓ w_ℓ·8 log T/log z` at `T=10^5` is:

| z | 100 | 300 | 1000 |
|---|---|---|---|
| ratio | 5.7 | 2.6 | 0.96 |

At `T=10^6` it is 0.81 for `z=3000`
(`data/pointwise_omega/haar_1e5.txt`, `haar_1e6.txt`). At accessible T the
ratio reaches 1 only near `z≈T^{0.6}`, where `log T/log z` is small. So
this evidence is consistent with H_PP for polylogarithmic z, but it does
not test that regime. The obstacle to a proof is the following.

* For a fixed prime ℓ, `ℓw_ℓ ≈ Σ_{j≤T/ℓ} m_j N(ℓj)/j`. This is the sum
  of Lemma 2.3 with ℓ fixed instead of averaged.
* The congruence saving `m | r'+k` then leaves a "first term"
  `ℓ/k_0`. Here `k_0` is the least solution of `k≡−r' (m)` and
  `4sr'k≡1 (ℓ)`.
* Bounding the first term needs the equidistribution of `(4sr')^{−1} mod ℓ`
  against the weights `τ(4sr'²+1)/(sr')`, uniformly in ℓ. This is a
  Kloosterman/Henriot-type input, cf. notes Thm 31.3, where the integer
  analogue needed Henriot's uniform Nair–Tenenbaum bound and still yielded
  only a softened charge.
* `ℓw_ℓ` is genuinely not polylogarithmic for all ℓ. At `ℓ=87359`,
  `(ℓ+1)/4=2^4·3·5·7·13`, so `|𝓡(ℓ)|` alone gives `ℓw_ℓ≈681` (EVIDENCE).
  So the hypothesis must be the relative form stated, not
  `ℓw_ℓ≤(log T)^C` for all ℓ.

**Consequences (Assessment).**

* Under RA (POINTWISE_SIZE §7.3), Theorem 9.3 predicts
  `W(p)>(log p)^{3−ε}` i.o. Previously Lemma 11.7 gave `2−ε`, which is now
  proved without RA by Theorem 5.1.
* Under RA and H_PP, the prediction is `W(p)>(log p)^A` for every A.
* On the prime side, Theorem 9.3's construction is a quarantine at
  `T^{1/3+ε}` plus pair events. Its prime analogue is exactly H_MIN(1/3),
  which would give exponent `3−ε` by Theorem 6.2. The local lemma does not
  supply the needed pointwise minorant, and §6.3's hub obstruction applies
  verbatim to pair events.

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
$C typeI 30000 200                 # §8: ck_min >= n_p for p=1 (24) < 30000, ~2 min
H="uv run python scripts/pointwise_omega_haar.py"
$H 100000 100 300 1000             # §9 (Lemma 9.1 check, S_tot, w_l, H_PP ratio), ~3 min -> data/pointwise_omega/haar_1e5.txt
(ulimit -v 12000000; $H 1000000 1000 3000)   # ~20 min -> data/pointwise_omega/haar_1e6.txt
# F_l^full sample (Lemma 9.1 parametrisation): see data/pointwise_omega/Ffull.txt (F_full() in pointwise_omega_haar.py)
```
