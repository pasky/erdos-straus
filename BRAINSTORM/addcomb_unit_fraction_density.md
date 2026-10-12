# Brainstorm memo: Croot/Bloom density methods for unit fractions vs. three-term ES (O142(c))

Labels as in DISCOVERIES.md. ES is not solved, and nothing here proves any case of it.
Verdict up front: **COLLAPSES to B3 (scale)**, by three independent measures: number of terms,
size of the representation count, and multiplicative (not additive) structure. The only
by-product is an exact but **known** reformulation (§3.2).

## 1. Idea

Croot (coloring) and Bloom (density) prove the existence of a finite S ⊂ A with
`Σ_{n∈S} 1/n = 1` by a circle method over the lowest common multiple of the denominators,
combined with combinatorial pruning. Question: can any piece of this be adapted to numerator 4
with **three** terms at a single n? Or does it say anything about the campaign's m/n density
results (DISCOVERIES (D)31)?

## 2. Literature anchor (checked: arXiv abstracts and Bloom's PDF, read via the visit-webpage skill)

* Croot, *On a coloring conjecture about unit fractions*, Annals 157 (2003), arXiv:math/0311421.
  The abstract says: if [2, b^r] is r-coloured, some colour class contains S with Σ 1/n = 1.
  Bloom's summary of Croot's main theorem: it is a density statement for sets of
  `n^{1/4−o(1)}`-smooth numbers in [2, N] with Σ 1/n > 6.
* Bloom, *On a density conjecture about unit fractions*, arXiv:2112.03726 (v2 2023;
  Lean-verified with B. Mehta).
  * Thm 2: positive upper density ⇒ some finite S with Σ 1/n = 1.
  * Thm 3: `Σ_{n∈A} 1/n ≥ C (log log log N / log log N)·log N` with `A ⊂ [1,N]` suffices.
  * **Prop 1 (the engine):** `A ⊂ [N^{1−1/log log N}, N]`, with
    `R(A) ≥ 2/y + (log N)^{−1/200}`, two small divisors in [y, z], prime powers
    `q ≤ N^{1−6/log log N}`, and `ω(n) ≍ log log N`, ⇒ some S ⊂ A with `R(S) = 1/d`,
    `d ∈ [y,z]`.
  * Lower bound `λ(N) ≫ (log log N)²` (Pomerance: n with a prime factor ≫ n/log n).
* Bloom 2023, arXiv:2305.02689: every positive rational is a sum of distinct unit fractions
  with denominators in {p − 1}. Liu–Sawhney 2024 give quantitative improvements; this is from a
  search snippet only, and the precise statement is not verified.
* For k = 3: Elsholtz–Tao §2. The Type I/II parametrisation comes from the gcd structure of
  (x, y, z).

## 3. Analysis

**3.1 Number of terms (PROVED, immediate from Prop 1's hypotheses).** In Bloom's Prop 1 every
element of S is ≥ `N^{1−1/log log N}` and `R(S) = 1/d` with d ≤ z ≤ (log N)^{1/500}, so
`|S| ≥ N^{1−1/log log N}/z`. Croot's theorem works with Σ 1/n over [2, b^r]; Bloom's summary
puts the smoothness threshold at `n^{1/4−o(1)}`, so its solutions also have length ≥ N^{c}
(Assessment: from the summary, not re-derived). ES needs |S| = 3.
* *Why the method needs this.* The Fourier/circle step detects `Σ 1/n ≡ 1/d` modulo every prime
  power q | lcm(S). That requires, for each such q, many elements of S divisible by q, so that
  their q-adic residues equidistribute (Bloom's "minor arc" hypothesis on multiples in short
  intervals). With three terms there are at most three residues per prime: no equidistribution
  is available, and the q-adic constraints are rigid.

**3.2 The k = 3 shadow of the local-cancellation principle (PROVED, elementary; known).** Let
`4/p = 1/x + 1/y + 1/z` and let ℓ ≠ p be prime with `v = max v_ℓ(x,y,z) > 0`. Then at least two
of x, y, z have `v_ℓ = v`; otherwise `v_ℓ(Σ) = −v < 0 ≤ v_ℓ(4/p)`. This is Croot–Bloom's
"every prime power of the lcm must be cancelled", specialised to three terms. Carried through
the gcds, it is exactly the derivation of ET's Type I/II parametrisation (ET §2), and so it
leads back to the divisor-class form (B2). Nothing new; it confirms that the method's
local engine, at k = 3, *is* the known parametrisation.

**3.3 Representation-count scale (Assessment, standard).** Circle-method, dispersion and
additive-combinatorial counting (Linnik's dispersion for n = x² + ab, Hooley; the Croot/Bloom
circle method) prove existence through a main term of size ≥ n^{δ} with a power-saving error.
At a fixed p, Type II is the representation `p = e(4acd − 1) − 4a²d` in four positive variables,
and its count is `f_II(p) ≍ log³p` on average (ET Thm 1.7, from memory). The main term is
`p^{o(1)}`, so no power-saving method applies (B3; CONDITIONAL_ES Prop 2.3). Dropping the
congruence `f ≡ −1 (mod 4ad)` gives counts of size `p^{1+o(1)}` but loses ES.

**3.4 The additive structure is fake (PROVED, one line).** The e-slice condition (LONGSHOT_PIGEONHOLE
Lemma 1.1) reads `a + b ≡ 0 (mod e)` with `ab | N`. That looks like a sum-product question
(additive event on a multiplicatively structured set; Bourgain–Glibichuk–Konyagin-type sums of
multiplicative subgroups). But on the part with `gcd(a,e) = 1`, which is the part Lemma 1.1
writes as ratios, b ≡ −a forces b to be a unit too, and the condition is equivalent to
`a·b^{−1} ≡ −1` in `(ℤ/e)^×`. That is purely multiplicative: sum-product has no additive set to
act on. The multiplicative covering version (Kneser) is already LONGSHOT_PIGEONHOLE Prop 1.4
(needs a number of prime factors linear in the index).

**3.5 Relevance to the m/n density results ((D)31, EXCEPTIONAL_MN).** These concern three
terms at almost all n. Croot/Bloom concern many terms, at density scale. The one structural
overlap is the smoothness/roughness dichotomy: Pomerance's obstruction (a prime factor
≫ n/log n) is the analogue of a denominator prime that cannot be cancelled. For ES the prime p
plays that role and is allowed to appear in one denominator (Type I) or two (Type II).
Prop 2.5 of the red team (a denominator prime ℓ ≥ n_p with χ_p(ℓ) = −1) is the ES-side
"roughness" condition. Neither direction transfers a quantitative statement (Assessment).

## 4. Barrier screen

* **B1.** Not applicable; the methods are not congruence coverings, but they do not apply at k = 3.
* **B2.** At k = 3 the local engine reproduces the parametrisation, i.e. the divisor-class form (§3.2).
* **B3.** It fails decisively: the number of terms needed is `N^{1−o(1)}` against 3, and the
  representation count is `p^{o(1)}` against the power needed (§3.1, §3.3).
* **B5.** At `n = m²` the local cancellation of §3.2 is still satisfiable, since local
  solutions exist (B5). In a hypothetical k = 3 circle method, the step that is false at
  squares would be "major arcs positive": the genus pairing cancels the local densities
  exactly (O128 Props 9.1–9.2). But the method never reaches that step at k = 3.
* **B6/T7.** Not reached: Bloom/Croot are pointwise in the target (1 or 1/d), but at density
  scale in the set A, which is the wrong axis for ES.

## 5. Viability

**COLLAPSES to B3** at step "number of terms / size of the representation count" (§3.1, §3.3).
The sum-product variant collapses to LONGSHOT_PIGEONHOLE Prop 1.4 (§3.4).

By-product: §3.2/§3.4 are exact one-line reformulations (PROVED, elementary, known in
substance). No new theorem. No relevant piece was found for the m/n density results beyond a
qualitative "roughness" analogy (§3.5).
