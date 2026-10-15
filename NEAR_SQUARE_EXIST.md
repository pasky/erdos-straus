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
Call m *generic* if gcd(m, b) = 1 (u-side, b = K) resp. gcd(m, c₀) = 1 (t-side). Then every odd prime r | N(m) is prime
to ab (r | b, r | N ⇒ r | m; r | t ⇒ r ∤ tn + 1) and hence splits in F.

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

**Corollary 2.2 (t-side: Prop 4.1 is also the admissible classification; PROVED).** For n = m² + k, k ≥ 1: F = ℚ(√−tc₀)
⊂ Σ_t ⟺ c₀ = tk + 1 is a square. Hence every level t with tk + 1 ≠ □ carries an *admissible* χ = −1 word (A a prime
r ≡ −1 mod t) on a positive density of m-classes inside any class C; the levels with tk + 1 = □ are clean (Prop 4.1(a)).
*Proof.* ℚ(√−t) ⊂ Σ_t, so F ⊂ Σ_t ⟺ ℚ(√c₀) ⊂ Σ_t ⊂ ℚ(ζ_{4t}). Then sqfree(c₀) has no odd prime outside t; as
gcd(c₀, t) = 1, c₀ ∈ {s², 2s²}; c₀ = 2s² forces t odd and √2 ∈ ℚ(ζ_{4t}), impossible. ∎
(So on the t-side "clean" and "sign-clean" coincide; the novelty is (a): uncleanness is *admissible* on a full class.)

**Corollary 2.3 (u-side classification; PROVED for words with A odd).** For n = m² + k, k ≥ 1, u ≥ 1, write
K = k + u = f²K₀ (K₀ squarefree). The u-level is sign-clean at generic m (Thm 2.1(b)) iff
 (a) every odd prime of K₀ divides u, and
 (b) K₀ ≡ 3 (4): no condition; K₀ ≡ 1 (4): u ≡ 1 (4) or 4 | u; K₀ = 2K₁, K₁ ≡ 1 (4): u = 2u′ with u′ ≡ 1 (4), or 8 | u; K₀ = 2K₁, K₁ ≡ 3 (4): u = 2u′ with u′ ≡ 3 (4), or 8 | u;
otherwise it carries an admissible χ = −1 word on a positive density of m-classes (Thm 2.1(a)).
*Proof.* F ⊂ Σ_u ⟺ the character (D_F/·) is trivial on V := Gal(ℚ(ζ_{8uK})/Σ_u) = {c : c ≡ 1 (mod u), (−u/c) = 1}.
For c ≡ 1 (mod u) the value (−u/c) depends only on c mod 8, and the 2-adic image V₂ of V is {1, 5} (u ≡ 1 (4)),
(ℤ/8)^× (u ≡ 3 (4)), {1, 3} (u = 2u′, u′ ≡ 1 (4)), {1, 7} (u′ ≡ 3 (4)), {1, 5} (u ≡ 4 (8)), {1} (8 | u) [reciprocity:
(u/c) = (−1)^{(u−1)(c−1)/4} for odd u and c ≡ 1 (mod u)]. Write (D_F/·) = ∏_{q | K₀ odd}(·/q) × ψ₂ with ψ₂ = 1, (−4/·),
(−8/·), (8/·) according to K₀ ≡ 3 (4), K₀ ≡ 1 (4), K₀ = 2K₁ with K₁ ≡ 1, 3 (4). V is "≡ 1 mod u" at odd primes and V₂ at 2
(CRT), so triviality ⟺ (a) and ψ₂|V₂ = 1, which is (b). ∎
In field language: **u-level sign-clean ⟺ √−(k + u) ∈ ℚ(ζ_u, √−u)**; T1 is k = 0. Examples (k = 24, the hardest offset
of NEAR_SQUARE §5): u ∈ {1, 3, 8, 12, 24, 25, 26, 30, 40, 48, 51, 57, 72, 74, 76, …} — e.g. u = 3 (K = 27 = 3·3²),
u = 26 (K = 50, K₀ = 2, u′ = 13), u = 30 (K = 54, K₀ = 6, 3 | 30, u′ = 15 ≡ 3). Only u = 1, 25, 12, 40, 57, 76 (K a square)
are R225's "p + u a sum of two coprime squares"; the rest are new u-side sign-clean levels, and most of them are
*not clean* in the sense of THREE_SQUARES (primes r | p + u with (r/p) = −1 occur) — the admissibility A ≡ −1 (mod u)
is what makes them sign-clean. (t-side, k = 24: t ∈ {1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, …} = {(c² − 1)/24}.)

**Remark 2.4 (even A; M odd).** Thm 2.1(b) is about odd A; even A occur only for odd M. For the t-side the clean levels are
clean prime by prime (Prop 4.1(a) incl. the prime 2 when (2/p) = 1), so nothing changes. For the u-side with u ≡ 3 (4),
F ⊂ Σ_u ⊂ ℚ(ζ_u) and the argument extends (PROVED): A = 2^a·A₀ gives σ_{A₀}|ℚ(ζ_u) = σ_{−2^{−a}}, which must fix F; for
a even this contradicts c_∞|F ≠ 1, for a odd it forces 2 inert in F, and then N ≡ 4 (8) gives A = 2A₀ with v ≡ 2 (4),
t odd, A* odd, so χ = +1 by the sign table. For u ≡ 1 (4) (K odd, N ≡ 2 mod 4, a = 1) the even-A words are not covered by
the proof: EVIDENCE only (next paragraph).

EVIDENCE (`scripts/z2_classify.py SIDE k-list MAXL MMAX x`: Thm 2.1's group criterion vs brute force over all m ≤ 500
with n ≡ 1 (4), gcd(m, b) = 1, all words incl. even A, χ from the sign table; n need not be prime): k ∈ {1, 8, 9, 16, 24},
u ≤ 80 and t ≤ 60: predicted sign-clean = empirically sign-clean in every case; the 14 levels predicted dirty but not yet
dirty at m ≤ 500 all became dirty by m ≤ 3000 (the first suitable prime r is large). Without the gcd restriction the
predicted-clean levels show χ = −1 exactly at non-generic m (e.g. k = 24, u = 25, m = 63 = 7·9, 7 | K = 49).
