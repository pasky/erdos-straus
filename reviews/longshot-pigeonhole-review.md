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

## §3 numerics — SOUND (sample re-run, exact agreement)

Independent engine `scripts/review_r135_covers.py` (sympy factorisation, Σ as an iterated product set, −K_e from
Jacobi symbols, TP from the definition of §2.2 with θ = 0, H = K_e). Per-prime results vs `data/lsa/cen_*`:

| p | E | sol. slices | P | TP | P20 | TP20 | max covered φ(e)/2 (P / TP) | max ω | author |
|---|---|---|---|---|---|---|---|---|---|
| 3529 | 2000 | 12 | 5 | 4 | 0 | 0 | 12 / 12 | 5 | identical |
| 5569 | 2000 | 19 | 4 | 3 | 2 | 2 | 23 / 23 | 6 | identical |
| 21169 | 2000 | 24 | 9 | 9 | 4 | 4 | 300 / 300 | 6 | identical |
| 110881 | 2000 | 33 | 4 | 1 | 0 | 0 | 12 / 11 | 6 | identical |
| 100000609 | 5000 | 105 | 23 | 12 | 14 | 9 | 455 / 455 | 7 | identical |
| 100001329 | 5000 | 101 | 22 | 13 | 13 | 9 | 324 / 324 | 7 | identical |

So the two exceptions 3529, 110881 (no cover with |−K_e| ≥ 20 for e ≤ 2000) are confirmed. The labels in §3
(EVIDENCE) and §5 (Conjecture 5.1 = CONJECTURE) are appropriate. Item 3 (model-limit series) not re-run.

## Theorem 2.2 — SOUND-AFTER-REPAIRS (two MINOR slips, D3–D4; one wording defect D5; a strengthening, D6)

Every step re-derived. Checks of the points the author flagged:

* **Definition not rigged.** R = Σ_e(L)·{M⁻¹,1,M} ⊂ Σ_e(N) (aM·b | N), so a TCC is a genuine ES certificate
  (−1 ∈ −H ⊂ R). It is not vacuous: TP flags (H = K_e) occur ~10–16 times per prime in §3 (re-confirmed above).
  The definition is the natural "p-blind coset covering from small primes" notion; its real limitation is the
  coset size (θ < 1/2), see D5/D6. Slip: θ = 0 does **not** admit H = K_e (index 2 > e⁰) — D3.
* **(a) e ≤ Y.** p ≡ 1 (mod 8ℓ) for every ℓ ≤ Y ⇒ (ℓ/p) = 1 (ℓ = 2 via p ≡ 1 (8)); Lemma 1.2(i) ⇒ L ∈ K_e;
  (e/p) = 1 as all prime factors of e are ≤ Y; Lemma 1.2(ii) ⇒ χ(M) = 1; R ⊂ K_e ∌ −1. Correct, independent of θ.
* **(b1).** Walking up the prime factors (with multiplicity, each < e < x^{1/4}) produces u | N in (x^{1/4}, x^{1/2}];
  BT `π(x;4u,b) ≤ 2x/(φ(4u) log(x/4u))` with φ(4u) ≥ 2φ(u) gives ≤ 5x/(φ(u) log x) for large x; Rankin with
  σ = (log x)^{−1/3}: ℓ^σ ≤ e for ℓ < E_1, product `(log x)^{O(1)}`; times 2E_1 pairs it is
  `x(log x)^{O(1)} exp((log x)^{1/3} − (log x)^{2/3}/4)/log x = o(x/log x)`. Correct. Note this bounds pairs (p, e),
  so it is also a mass bound.
* **(b2) constants and compatibility with p ≡ 1 (q₀).** h(ℓ^v) = (2v+1)² − (2v−1)² = 8v ✓. Type II: m | N ⟺
  p ≡ −e (4m); Type I: p ≡ −e⁻¹ (4m) (gcd(m,e) = 1 since m | N). Compatibility with p ≡ 1 (q₀) at odd ℓ ≤ Y
  (ℓ | m) is ℓ | e+1 in both types ✓; at 2 it is automatic mod 4 and forces e ≡ 7 (8) if 2 | m (ignored — fine, upper
  bound). `φ(lcm)φ(gcd) = φ(4m)φ(q₀)` ✓; lcm ≤ 4x^{1/2}q₀ ≤ x^{2/3} for x ≥ x₀(Y), giving the factor 6 ✓.
  Local factors: 2-part `Σ_j h(2^j)·φ(gcd(2^{j+2},8))/φ(2^{j+2}) = 1 + 8 + 8Σ_{j≥2} j2^{1−j} = 33` ✓ (numerically
  33.0); odd ℓ ≤ Y, ℓ | e+1 (q₀ has ℓ¹): `1 + Σ_v 8v ℓ^{1−v} = 1 + 8/(1−1/ℓ)² ≤ 19` ✓; Y < ℓ < e:
  `1 + 8ℓ²/(ℓ−1)³` ✓; primes ℓ ≤ Y with ℓ ∤ e+1 contribute 1 ✓. `∏_{3≤ℓ<e}(1 + 8ℓ²/(ℓ−1)³) ≤ C₀(log e)⁸` with an
  absolute C₀ (ratio computed: 0.071, 0.065, 0.063, 0.0629, 0.0628, 0.0627 at e = 10²…10⁷;
  `scripts/review_r135_constants.py`). Dropping "L ≤ x^{1/2}" after restricting to m ≤ x^{1/2} is legitimate.
* **Uniformity of C in Y.** C collects 6·33·C₀·9·2 (types) and the constant in
  `Σ_{e>Y} 19^{ω(e+1)}(log e)⁸ e^{2θ−2}(log log e)² ≪_{θ,ε} Y^{−1+2θ+ε}`; none depends on Y (Y enters only through x₀(Y)
  and the o(1)). ✓ (For −1+2θ+ε ≥ 0 the statement is trivially true, so no restriction on ε is needed.)
* **(c) Shiu, Type I.** p ↦ N injective, N ≡ 4⁻¹ (mod e), N ≤ X := (xe+1)/4, f = τ(·²)² multiplicative,
  f(ℓ^v) = (2v+1)² ≤ 9^v, f(n) ≪_ε n^ε. Shiu Thm 1 (checked in sources/shiu-1980.pdf, p. 163, OCR: needs
  0 < α, β < 1/2, (a,k) = 1, `k < y^{1−α}`, `x^β < y ≤ x`) gives `≪ X/(φ(e) log X)·exp(Σ_{ℓ≤X} 9/ℓ) ≪ (xe/φ(e))(log x)⁸`
  — but the stated range check "modulus e ≤ (xe/4)^{1/2}" is false for x/4 < e ≤ x: D4 (harmless).
  Summation `Σ_{e>E₁} B_e^{−2} e/φ(e) ≪ E₁^{−1+2θ+ε}` (ε small) beats `(log x)⁹` ✓. Type II via `Σ_{n≤X} f ≪ X(log X)⁸` ✓.
* **(d) e > x.** N < e²/4; `τ(N²) ≤ τ(N)²`; Nicolas–Robin `log τ(n) ≤ 1.5379 log 2 · log n/log log n` (n ≥ 3; the
  standard constant, attained at n = 6 983 776 800) gives `τ(N²) ≤ exp((4.27+o(1)) log e/log log e) < B_e` for
  e ≥ e₀(θ) ✓ (uses that log n/log log n is increasing for n ≥ e^e; N small is trivial).
* **Quantifiers.** The theorem asserts one set of primes (relative lower density > 0) that has **no** TCC_θ in
  **any** (e, T) simultaneously — stronger than "for each slice, a positive proportion fails"; the proof supports
  exactly that (all e-ranges are unioned per prime). The density is ≈ (1 − O(Y^{−1+2θ+ε}))/φ(q₀) with Y
  ineffective-large: "positive proportion" is purely qualitative, as §3 item 3 already concedes. The factor 2C in
  the consequence is slack (C suffices once o(1) < C·Y^{…}); harmless.
* **Inputs/labels.** PNT in APs to a fixed modulus, Montgomery–Vaughan BT (`π(x;q,a) ≤ 2x/(φ(q) log(x/q))`),
  Shiu Thm 1, Nicolas–Robin: all used within their stated ranges (after D4). Label PROVED (relative to these
  classical theorems) is justified.
