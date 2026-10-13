# R176 — hostile review of O176 (DIFF_DEEP.md + BRAINSTORM/bsC_*.md)

Reviewer: side-agent/review-diff-deep. Merged `side-agent/spark-diff-parity` at start. From-scratch scripts:
`scripts/review_dd_*.{c,py}`. **ES is not solved anywhere; nothing below changes that.**

(in progress — sections are added claim by claim)

## Verdict per claim

| Claim | Verdict |
|---|---|
| DIFF_DEEP Thm 2.1 (algebraic bijection + `4h ∣ gcd(h,G)²`) | **SOUND** (re-derived; brute force exact for all odd n ≤ 2001) |
| Thm 2.1 geometric reading | SOUND-AFTER-REPAIRS (see D-list) |
| Thm 1.1 / Cor 1.2 (supersingular transfer; ∃E vacuous) | SOUND (Diff(T') = {p} re-checked from scratch) |
| Prop 1.3 (∀E false; τ(e) maximal orders) | SOUND-AFTER-REPAIRS (τ(e) correct for all e; ET citation wrong) |
| Prop 2.2 (Gram form, involutions, k² = −4c²dp) | SOUND; last sentence (commutative identity with *this* k) FALSE as written — notation clash (D3) |
| Prop 2.3 (level free on one endomorphism, nrd x ≪ M²p) | **SOUND** (absolute constant; notation O⁰ clash, D5) |
| Prop 2.4 (exactness gap) | identity SOUND; f^{3/2} gap and lottery sum are Assessment, with a bookkeeping slip (D6) |
| §4 / report gloss "level G ≥ 2√h" as the content of (LD_p) | **GAP (MAJOR)**: the relaxed condition is vacuous |

## Checks performed

### Thm 2.1 (algebra)
Re-derivation. ET Type II: a,b,c,d ≥ 1, `4abd = n + e`, `a + b = ce`; so `4abcd = cn + a + b` and
`(4acd−1)(4bcd−1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1`. Thus h := (ff'−1)/n = 4c²d = cM (M = 4cd), M | f+1, f'+1,
so M | G and h | cG. Conversely d = h/4c², M = h/c | G gives a, b ∈ ℤ_{>0}, and `abM − a − b = nc` is the ET
equation with e = (a+b)/c — but **e ∈ ℤ needs a separate line**: from `4abd = n + (a+b)/c` and 4abd, n ∈ ℤ,
(a+b)/c ∈ ℤ. (The author's ⇐ cites "(I)4's criterion", which contains this; fine.) Minimal c: h/g divides every
valid c, so 4c² | h is weakest at c = h/g; gives 4h | g². Edge h = 0 (f = f' = 1) is excluded by 0 ∤ cG. Correct.

Brute force (`scripts/review_dd_thm21.c`, C, 0.3 s): tuple side by the naive ET loop (a ≤ b, d, e = 4abd − n,
e | a+b); triple side by c, d with h = 4c²d ≤ (n+5)² (4× the analytic bound (n+5)²/4 that I derived on the triple
side), f ≡ −1 (M), f | 1 + nh, f' ≡ −1 (M). **All odd n ∈ [3, 2001] (1000 values, 21 odd squares): the two sets of
(f, f', c) coincide exactly, 16054 tuples, no duplicates, 0 solutions at odd squares.** (Author's enumerator gives
the same total 1120 for n ≤ 301.) The "iff 4h | gcd(h,G)²" part checked independently
(`scripts/review_dd_thm21_iff.c`): all 3 556 994 factor pairs f ≤ f' of 1 + nh, 1 ≤ h ≤ n², odd n ≤ 151 — predicate ⟺
existence of c, 0 disagreements, and no predicate-true pair beyond h ≤ (n+5)²/4.

### Prop 1.3 / bsC_supersingular_transfer Prop 3
* τ(e) count: the maximal orders of M₂(ℚ_ℓ) containing the Eichler order of level ℓⁿ are the n+1 vertices of the
  geodesic segment — true for every n, so the global count is ∏(v_ℓ(e)+1) = τ(e) for **non-squarefree e as well**.
  Checked by brute force on the Bruhat–Tits tree (`scripts/review_dd_tree.py`: ℓ = 3, 5, n ≤ 4, all vertices within
  radius n+2: exactly n+1 stable lattices). The local argument (−d a unit square mod ℓ^{v} since e | 4a²d + 1, ℓ ∤ 2d;
  Hensel; idempotents ⇒ [[ℤ_ℓ, ℓ^i],[ℓ^j, ℤ_ℓ]] ⇒ Eichler of level ℓ^{i+j}) is standard and correct.

### Thm 1.1 / Cor 1.2 and the geometric reading of Thm 2.1
* Thm 1.1: ℤ⟨x,y⟩ with x² = −f, y² = −f', xy + yx = −2 is an order (yx = −2 − xy); it lies in a maximal order of
  B_T; Deuring realises every maximal order type of B_{p,∞}. ⇒: positive-definite T ⇒ x, y do not commute ⇒ they
  generate End⁰E. Correct. Its reduced discriminant is 4·det T, so p | det T is automatic on a curve (needed for the
  "h = det/p" phrasing). Correct.
* Diff(T') = {p} for every Type II pair: re-checked with my own Hilbert-symbol code on B_{T'} = (−f, −f·det T')
  (`scripts/review_dd_hilbert.py 1500`): **4025 Type II pairs of primes p < 1500, finite ramification exactly {p} in
  every case.**
* **The relaxed reading "level G ≥ 2√h" is NOT equivalent and is in fact vacuous** (`scripts/review_dd_vacuous.py
  3000 200`): for 437 of the 438 primes 5 < p < 3000 (all residues mod 24; the only miss is p = 5 at h ≤ 200) there is a
  pair (f, f') with ff' = 1 + ph, B_{T} ramified exactly at p (so it lives on a supersingular curve by Thm 1.1),
  G ≥ 2√h, and 4h ∤ gcd(h,G)², i.e. **not** a certificate. Examples: p = 73: (21, 153), h = 44, G = 22;
  p = 97: (20, 34), h = 7, G = 7; p = 1201: (39, 154), h = 5, G = 5. Per-pair counterexamples with small p:
  (f,f') = (4,9) at p = 7 (h = 5, G = 5). Thm 2.1's displayed condition is the correct one; the glosses are wrong
  (see D1).

### Prop 2.2 (`scripts/review_dd_identities.py 3001`, 27 788 Type II tuples of odd n ≤ 3001, own enumerator)
* Gram form: f = aM − 1, f' = bM − 1 ⇒ fX² + 2XY + f'Y² = M(aX² + bY²) − (X − Y)². ✓ (0 failures).
* x² = −f ≡ 1, (x + y)² = −(f + f' + 2) = −M(a + b) = −Mce ✓; trd(xy) = −2 so k = xy + 1 is trace-zero and
  nrd k = ff' − 2 + 1 = 4c²dp, k² = −4c²dp ✓ — verified in an explicit model x = i, y = i/f + j/f of (−f, −f·det T)
  (0 failures).
* bsC_typeII_commutative Lemma 1 `(2ad + k)(2bd + k) = de(1 + 2ck)` with **k² = −dn** ✓ (0 failures; re-derived:
  LHS = d(4abd − n) + 2(a+b)d·k, coefficient comparison gives exactly 4abd = n + e, a + b = ce; norms ✓ since
  ef = 4a²d + n). But DIFF_DEEP Prop 2.2 states the identity right after defining k := xy + 1 with k² = −4c²dp: **with
  that k the identity fails for all 27 788 tuples** (it forces 4abd − 4c²n = e). The memo's k is
  (xy + 1)/(2c). See D3.

### Prop 2.3 (re-derived)
O/MO ≅ M₂(ℤ/M) (p ∤ M); trd(O) = ℤ (contains 2, and O ⊗ ℤ₂ ≅ M₂(ℤ₂) has odd traces); x = x' + Mz is trace-zero
and ≡ x₀; MO ∩ B⁰ = M(O ∩ B⁰); the coset contains y with nrd y ≤ M²ρ²; y² = −nrd y ≡ 1 in O/MO and ℤ ∩ MO = Mℤ give
nrd y ≡ −1 (M); y ≠ 0 since x₀ ≢ 0. Constants: with λ_i the successive minima (squared, nrd) of O ∩ B⁰,
λ₁λ₂λ₃ ≪ det ≍ p² (Minkowski II), Kaneko (two non-commuting trace-zero elements: (−4λ₁)(−4λ₂) ≥ 4p) gives
λ₁λ₂ ≥ p/4, so λ₃ ≪ p and ρ² ≤ ¼Σλ_i ≪ p (in dimension 3 minimal vectors form a basis). **The implied constant is
absolute** (no dependence on M, x₀ or the order). SOUND. Remark: the statement is weak by design (one vector in a
coset of covolume ≍ M³p); it does not touch the second congruence or the exact-norm condition.

### Prop 2.4
y_⊥ = y − x/f, nrd y = 1/f + nrd y_⊥, det T = f·nrd y_⊥ ✓. {y ≡ y₀ (M), ⟨x,y⟩ = 1} is an affine coset of
x^⊥ ∩ MO⁰ ✓; det(x^⊥ ∩ L) = nrd(x)·det L/[L : ℤx ⊕ (x^⊥ ∩ L)]² (so "up to an index factor" is right, but the
index can be as large as ≍ f for special x, which would cut the gap to ≍ f^{1/2}; this is why it must stay an
Assessment). Thm 2.1 ⇒ h ≤ g²/4 ≤ G²/4 ⇒ nrd y_⊥ ≤ pM²/(4f) ✓; ratio f^{3/2} ✓; f ≥ M − 1 ✓.
