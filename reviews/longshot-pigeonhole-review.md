# R135 — hostile review of O135 (LONGSHOT_PIGEONHOLE.md)

Reviewer: R135 side agent. Scope: §§1–2 lemmas, Theorem 2.2, §3 numerics (sample), §5 labels.
From-scratch scripts: `scripts/review_r135_*.py` (no author code reused).

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (e-slice) | SOUND (fibre-of-V statement); MINOR wording on "bijection" (D1) |
| Lemma 1.2 (genus incl. ℓ = 2) | (see below) |
| Lemma 1.3 (collisions → signed solutions) | (see below) |
| Prop 1.4 (Kneser criterion, sharpness) | (see below) |
| Lemma 2.1 (forcing cost) | (see below) |
| Theorem 2.2 | (see below) |
| Lemma 2.3 | (see below) |
| §3 numerics | (see below) |

## Lemma 1.1 — SOUND

Re-derived: (i) `4N^I ≡ 1`, `4N^II ≡ p (mod e)`, e odd ⇒ gcd(N,e) = 1 (p ∤ e). (ii)/(iii) immediate from the
defining equations; `e | a+b ⟺ ab⁻¹ ≡ −1`. (iv) exponent bookkeeping correct, every `t ∈ [−v, v]` realised.

From scratch (`scripts/review_r135_slices.py`):
* all primes 5 ≤ p < 2000: ES(p) by a direct `4/p = 1/x+1/y+1/z` solver ⟺ some e-slice (either type) has
  `−1 ∈ Σ_e(N)`: **0 mismatches**.
* all primes 5 ≤ p < 110 (both residues mod 4): complete enumeration of ordered solution triples, split by the
  number of coordinates divisible by p, versus `3·Σ_e #{(a,b): ab | N_e, e | a+b}`. No solution has 0 or 3
  coordinates divisible by p. **With the extra condition gcd(a,b) = 1 the counts agree exactly for every p;
  without it the fibre counts are strictly larger for 18 of 27 primes** (e.g. p = 71, Type I: 171 solutions vs
  210 fibre points; `(1,1,2,18;e=1)` and `(3,3,6,2;e=1)` both give (1278, 36, 36)). This is the dilation symmetry
  `(a,b,c,d) ↦ (λa, λb, λc, λ⁻²d)` of Elsholtz–Tao §2 (checked in sources/elsholtz-tao-1107.1010.pdf, Prop 2.2:
  uniqueness needs gcd(a,b,c) = 1).

Lemma 1.1 as stated is about the fibres of V_T(p), and there it is correct; ES(p) ⟺ V(p) ≠ ∅ is correct. See D1.

## Lemma 1.2 — SOUND

Re-derived. Useful remark the author leaves implicit: for e ≡ 3 (mod 4) and odd n, Jacobi reciprocity gives
`(−e/n) = (n/e)`, and at n = 2 `(−e/2) = (2/e)`; so `χ_{−e}` is just the Jacobi symbol `(·/e)`, a genuine
character mod e, non-trivial (e ≡ 3 (4) is not a square) with `χ(−1) = −1`. ℓ = 2 step: Type II `8 | p+e ⇒ −e ≡ p (8)`;
Type I `8 | pe+1 ⇒ −e ≡ p⁻¹ ≡ p (8)` (p² ≡ 1 mod 8); Kronecker at 2 depends on D mod 8 and `(p/2)_{Kr} = (2/p)` for
p ≡ 1 (4). ℓ = p never divides N (p ∤ e). (ii) via `(N/p)` with `4N^I ≡ 1`, `4N^II ≡ e (mod p)`: correct.
From scratch (`scripts/review_r135_genus_kneser.py`; Kronecker symbol computed from its definition, not via
reciprocity): periodicity mod e and `χ(−1) = −1` for all e ≡ 3 (4) < 400; (i) for all 96 524 (prime p ≡ 1 (4) < 4000,
e ≡ 3 (4) < 300, T, ℓ | N) instances, and (ii) for all (p, e, T): **0 failures**.

## Lemma 1.3 — SOUND

Unitary-divisor pigeonhole: u ≡ u' ⇒ a = u/g, b = u'/g coprime, `ab = uu'/g²` is a unitary divisor of N (product of
the prime powers in exactly one of u, u'), a ≢ b as integers since u ≠ u'. Both identities re-derived by hand and
verified exactly (Fractions) on every pair a > b, a ≡ b (e), ab | N for p < 300, e < 60, both types: 0 failures.
Note the lemma never uses the hypothesis on the sign coset; the conclusion "target 1 ∈ K_e" is correct.

## Prop 1.4 — SOUND (criterion); sharpness example SOUND but its reach is stated a bit broadly (D2)

Proof re-derived: H = Stab(Σ) ⊂ Σ since 1 ∈ Σ; Σ is a union of H-cosets missing t₀H; partial products of the
X_i in G/H have trivial stabiliser (a period of a partial product is a period of the full product — correct);
Kneser with trivial stabiliser gives `|AB| ≥ |A|+|B|−1`; `|{g^t H : |t| ≤ v}| = min(2v+1, o_H(g))`. Correct.
Brute force (all subgroups of (ℤ/e)* by closure, e < 64, ~12 000 random (g_i, v_i) configurations): whenever the
criterion holds for all H ∌ −1, indeed −1 ∈ Σ — **0 violations** (the criterion is silent on 5 280 covered
configurations, as expected of a sufficient condition). Check (a) (H = K_e ⟺ a factor outside K_e) correct.
Sharpness (c): in ℤ/2m with all g_i = 1, v_i = 1 one has Σ = [−k, k] and the H = 0 condition is exactly k ≥ m; so for
data consisting only of "orders of images in every quotient" no criterion can beat linear. Correct.
§5 explicit instances (e = 3: a factor ≡ 2 (3); e = 7: factor ≡ 3, 5, 6 (7) and ≥ 3 distinct factors ≢ ±1 (7))
re-derived from Prop 1.4 (subgroups of C_6 ∌ 6 are {1}, {1,2,4}; ord-3/6 elements with v ≥ 1 contribute 2 each,
so 3 of them give 6 ≥ 5) and checked directly for all p ≡ 1 (4) < 2·10⁵: 0 failures.
