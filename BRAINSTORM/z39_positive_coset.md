# z39_positive_coset — ES = a positive element of the coset −Γ₁(c) with upper-right entry n; the odd (weight-1) part is the ±I parity (O269)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
QUESTION_R Prop 1.1 writes ES words as self-levelled matrices γ = [[A, n],[c, A*]], A ≡ A* ≡ −1 (mod c). Read the
congruence group-theoretically and match it with Thm K's even/odd split.

## Dictionary (PROVED, elementary)
1. γ ≡ −[[1, −n],[0, 1]] (mod c), i.e. **γ ∈ −Γ₁(c)**, and every element of the Γ_∞-double coset
   Γ_∞γΓ_∞ satisfies the same congruence (translations change a, d by multiples of c). So, unlike the Type II
   normalisation of `bsB_salie_duality` (where the congruence modulus moved under Γ_∞), here the self-level
   condition is Γ_∞-bi-invariant: **level-t ES words = the positive elements with b = n of the single Bruhat cell
   Γ_∞[[−1, ∗],[t, −1]]Γ_∞** — one term of each Kloosterman sum S(·, ·; t), the term (a, d) ≡ (−1, −1).
   The non-invariant datum is b = n itself; summing q^b over the cell gives the split indefinite theta of
   z39_kronecker_levels.
2. The partner quadrant Q_t of Thm K is the cell of +I: positive γ ∈ Γ₁(t) with b = n. It is **never empty**:
   [[1, n],[t, 1 + nt]] = [[1,0],[t,1]]·[[1,n],[0,1]] (lower × upper unipotent). Its analogue in −Γ₁(t),
   [[−1, n],[t, −1 − nt]], is not positive. So ES(n) at level t asks whether **positivity can be restored in the
   −I coset** — the archimedean theme of (J)52 in group form.
3. The odd part O_t = D⁻ − D⁺ + 2 of Thm K is the signed count over the two cells ±Γ₁(t) (sign = the value of the
   weight-1 parity character at −I, (−1)^k with k = 1); the even part E_t is the unsigned count. So the **weight-1
   (holomorphic, Kronecker) part is exactly "−I-coset minus I-coset"**, and Cor K1.1 (T1 at 4 | t) says: at
   n = m² the −I cell has no positive element with b = m², i.e. the odd part equals minus the even part.
4. Metaplectic version (relating to QUESTION_R Prop 1.4, *classical/RS* input per R278): on positive self-levelled
   γ ∈ −Γ₁(4) one has (c/d) = 1, hence ν_θ(γ) = ε_d⁻¹(c/d) = −i constant (d ≡ 3 mod 4), while on positive
   γ ∈ Γ₁(4), ν_θ(γ) = (c/d) = (a/b). The theta multiplier refines the ±1 parity of item 3 to the 4th roots
   ±1, ±i: the −I coset is where ν_θ is *imaginary*. T1 = "ν_θ ≡ −i on positive self-levelled elements of −Γ₁(4) is
   incompatible with b being a square" (since then (a/b) = 1 forces (c/d) = −1 by Prop 1.4, contradicting
   self-levelling).

## Literature
Iwaniec, *Topics in classical automorphic forms* (GSM 17), Ch. 2–3 (Bruhat cells, Kloosterman sums, theta
multiplier); Rickards–Stange arXiv:2401.01860 §3, §7.3.

## Barrier screen
B2: item 1 locates B2 precisely — not in the congruence (which is cell-invariant) but in "b = n inside a cell indexed
by c": the cell index c is a solution coordinate. B6: a Poincaré/Kuznetsov sum would average over the full
Kloosterman sum at each c (all cells), ES keeps one cell per c and one b — a single-n, single-cell count (B3 scale
log²). T1: item 3/4. B1/B4/Thm 9.1/Prop 10.3: n/a.

## Cheap numerics
Covered by `scripts/z39_kronecker.py` (D⁺ count = Γ₁(t) cell count; 0 failures).

## Assessment
PROVED dictionary. New: the self-level congruence is Bruhat-cell invariant in this normalisation, so ES is "one
Kloosterman term per modulus, at a prescribed b"; positivity in the −I cell is the whole question. No mechanism.
Promise 1/5.
