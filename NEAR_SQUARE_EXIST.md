# NEAR_SQUARE_EXIST — near-square primes: from the hardness explanation towards existence (task O225, wave Z-b)

Status: in progress (O225). **ES is not solved here, nor any infinite case of it unless explicitly stated with a complete
proof.** Labels as in DISCOVERIES.md. Builds on NEAR_SQUARE.md ((J)55, R225), THREE_SQUARES.md ((J)53), DEDEKIND_ES.md
Thm 4.5 (the sign table). Memos BRAINSTORM/z2_*.md, scripts `scripts/z2_*`.

Notation. p ≡ 1 (mod 4) prime (p ≡ 3 (4) is trivial). A *word* is (t, u, v) ∈ ℕ³ with tuv − u − v = p;
A = tu − 1, A* = tv − 1, AA* = tp + 1, p + u = vA, p + v = uA*; χ(w) = (A/p) (= (A*/p)). Words are the same objects
seen from two sides:
* *t-side (level t):* divisors A | tp + 1 with A ≡ −1 (mod t) (then A* ≡ −1 (mod t) automatically);
* *u-side (u-level u):* divisors A | p + u with A ≡ −1 (mod u) (t = (A + 1)/u, v = (p + u)/A).

**Sign table (DEDEKIND_ES Thm 4.5, PROVED + CERTIFIED there).** For n ≡ 1 (mod 4): χ(w) = −1 ⟺ 4 divides one of
t, u, v, A, A*. (Re-checked: `scripts/z2_words.c` mode 1, all 34 913 178 words with u ≤ v of all 332 180 primes
p ≡ 1 (4) below 10⁷: 0 mismatches between (A/p) and the table.)

## 1. The u-side mechanism for every u (goal 1; PROVED)

**Prop 1.1 (u-side T1, all u).** Let p ≡ 1 (mod 4) be prime and u ≥ 1 with p + u = x² + y², gcd(x, y) = 1. Then every
word with this u (or with v = u) has χ = +1. If u is even there is no word with this u at all.
*Proof.* N := p + u = vA. Since gcd(x, y) = 1, every odd prime factor of N is ≡ 1 (mod 4) and 4 ∤ N.
*u even.* N is odd, so N ≡ 1 (mod 4) and u ≡ 0 (mod 4). Then A = tu − 1 ≡ 3 (mod 4), but A | N forces A ≡ 1 (mod 4):
no word. (Equivalently: by the table every word with 4 | u has χ = −1, so the u-level is "clean" only vacuously.)
*u odd.* N even ⇒ x, y odd ⇒ N ≡ 2 (mod 8) ⇒ u ≡ 2 − p ≡ 1 (mod 4).
– A odd: A ≡ 1 (4) (product of primes ≡ 1 mod 4), v = N/A ≡ 2 (4); tu = A + 1 ≡ 2 (4) ⇒ t ≡ 2 (4); A* = tv − 1 is odd.
  So none of t, u, v, A, A* is ≡ 0 (4).
– A even: A = 2A′, A′ ≡ 1 (4), so A ≡ 2 (4); v = N/A is odd with v ≡ 1 (4); tu = A + 1 ≡ 3 (4) ⇒ t ≡ 3 (4) (u ≡ 1);
  A* = tv − 1 ≡ 2 (4). Again none of the five is ≡ 0 (4).
By the sign table χ = +1. The v-side statement is the same argument with (u, A) ↔ (v, A*). ∎
CERTIFIED-style check (`scripts/z2_words.c` mode 1): all primes p ≡ 1 (4) below 10⁷: 1 358 527 words have p + u or
p + v a sum of two coprime squares; 0 have χ = −1; none of them has the flagged u (or v) even. Control: all odd squares
below 10⁶: 6 434 flagged words, all χ = +1 (as every word at a square).
So R225's "even u" gap closes trivially: for even u the hypothesis forces u ≡ 0 (4), and 4 | u is exactly the u-level
on which *every* word has χ = −1 — the hypothesis then says there are no words. This is the cleanest form of the
u-side mechanism: **at 4 | u, χ = −1 is free and the whole content is "p + u has a divisor ≡ −1 (mod u)"; p + u a sum of
two coprime squares kills that divisor (T1: p = m², u = 4 gives m² + 4).**

## 2. Sign fields: the complete classification of sign-clean levels (goal 2)

Both sides are instances of one situation: a *level quantity* N(m) = a·m² + b (a, b ∈ ℤ, a > 0) and a *level modulus* M,
words = divisors A | N(m) with A ≡ −1 (mod M), and for every odd prime r | A (r ∤ M automatically)
(r/p) = (−M/r)   [t-side: THREE_SQUARES Lemma 1.1; u-side: p ≡ −u (mod r) and p ≡ 1 (4)].
* t-side (n = m² + k): N = tn + 1 = t·m² + c₀, c₀ = tk + 1, M = t.  * u-side: N = n + u = m² + K, K = k + u, M = u.
(General Q(m) = Am² + Bm + C: multiply by 4A and use X = 2Am + B; the t-side has a·b = t·E/… with E = 4A − tΔ.)
Define the **family field** F := ℚ(√−ab) (odd primes r ∤ 2ab divide some N(m) iff they split in F) and the **sign field**
  Σ_M := ℚ(ζ_M, √−M).
For an odd A coprime to M let σ_A ∈ Gal(Σ_M/ℚ) be its Artin symbol (ζ_M ↦ ζ_M^A, √−M ↦ (−M/A)√−M). Then
(i) A ≡ −1 (mod M) ⟺ σ_A|ℚ(ζ_M) = complex conjugation c_∞; (ii) χ(A) = ∏_{r|A}(r/p) = (−M/A) = σ_A(√−M)/√−M.
So **an admissible odd A has χ(A) = −1 ⟺ σ_A = c_∞|Σ_M** — the "Frob = c_∞" of (J)50, now with the level field attached.
Call m *generic* if gcd(N(m), 2ab) = 1 is not needed but gcd(m, b) = 1 (u-side) resp. gcd(m, c₀) = 1 (t-side), i.e. every
odd prime of N(m) prime to 2ab... precisely: every odd prime r | N(m) splits in F or divides 2ab only to the extent forced
by r | gcd(N(m), ab); we take m with gcd(N(m), ab) | 2^∞.

**Theorem 2.1 (sign-field criterion; PROVED).** Let n(m) = m² + k with k ≥ 1 (so F is imaginary), level (side, M) as above.
(a) If F ⊄ Σ_M, there is a set of primes r of positive density with σ_r = c_∞ on Σ_M and r split in F; for each such r
and every m in one of the two residue classes mod r with r | N(m) (all large m in those classes), the level carries the
word with A = r (resp. A* = r) and χ = −1. In particular the level is NOT sign-clean on a positive density of m-classes,
and these classes can be chosen inside any m-class C (CRT, r ∤ modulus of C).
(b) If F ⊂ Σ_M, then for every generic m, every word at this level with A odd has χ = +1.
*Proof.* (a) F and Σ_M are abelian; F ⊄ Σ_M ⇒ Gal(FΣ_M/ℚ) = Gal(F/ℚ) × Gal(Σ_M/ℚ) restricted appropriately, so
(1, c_∞|Σ_M) is an element; Chebotarev. Then r ≡ −1 (mod M), r | N(m) on two classes mod r, χ(r) = (−M/r) = −1;
u = (r + 1)/M (t-side) or t = (r + 1)/u (u-side), and the cofactor ≥ 1 for large m.
(b) Every odd prime r | A divides N(m), is prime to M (A ≡ −1 mod M) and, m generic, splits in F; so
σ_A = ∏σ_r^{e} ∈ Gal(Σ_M/F). If χ(A) = −1, then by (i)–(ii) σ_A = c_∞|Σ_M (Σ_M = ℚ(ζ_M)(√−M)), so c_∞ fixes F —
impossible for F imaginary. ∎
*Reading.* T1 (k = 0): F = ℚ(√−M) ⊂ Σ_M at every level, so c_∞ is forbidden everywhere. The deformation k ≠ 0 moves F;
a level stays sign-clean exactly when the moved family field still sits inside the level's sign field. The obstruction
is always the same: an admissible χ = −1 divisor is "Frobenius = complex conjugation", and an imaginary F refuses it —
positivity once more ((J)52).
