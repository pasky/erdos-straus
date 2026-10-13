# R180 — hostile review of LORENZINI_W.md (O180), reviewer 1 of 2 (full document)

Reviewer worktree branch `side-agent/review-lorenzini-1`, merged `side-agent/lorenzini-w` at b71427be.
From-scratch scripts: `scripts/review_lw_*.py` (none of the author's `bsG_*` scripts reused).
Sources read: `sources/lorenzini/CriticalPolynomialOfAGraph.txt` (Lorenzini JNT 2024, Ex. 6.2, Prop 6.3, Rem 6.4).
NOT accessible: T. Wang, EJC 33(3) #P80 (2026). The "open problem" and "new as far as I can tell" claims about it are unchecked.

## Verdict summary (filled in claim by claim)

| claim | verdict |
|---|---|
| Thm 9.1 (even half) | **SOUND** |
| Prop 8.1, Cor 8.2 | **SOUND** |
| Lemma 3.1, Remark 3.2 | **SOUND** |
| Prop 3.3 | **SOUND** |
| Forms F0, F1, F3, F4 | **SOUND** |
| Form F2 | **GAP (mis-stated; false at n = 3, 15, 35)**, D1 |

## Claim-by-claim

### Thm 9.1 — SOUND
* **Reduction to 2^m − 2, m odd.** Checked against the source text. Lorenzini Prop 6.3(a) gives every even n > 0 except 2^m − 2 with m odd or
  m = 2, 4. His proof covers n + 2 not a 2-power by z = 2 (x(2y−1) = n + 2 with an odd divisor 2y − 1 ≥ 3 and x even ≥ 2), and even m > 4 by
  (4, (2^{m−3}+1)/3, 6). m = 2, 4 give n = 2, 14, which are exceptions. So the reduction is exactly as stated.
* **Congruences.** `scripts/review_lw_orders.py` recomputes every "⟺" in the table: ord₉2 = 6, ord₁₃2 = 12, ord₂₇2 = 18, ord₃₇2 = ord₁₀₉2 = 36, and
  the residues 2 − c (mod d) are 5, 2, 8, 17, 101 ≡ −8, 31, each hit by exactly one class of m mod the order, namely 5, 1, 3, 15, 21, 9. The 2-parts
  are also right: 8 | 2^m + 16 for m ≥ 3 and 16 | 2^m + 80 for m ≥ 4.
* **Covering.** For each odd r mod 36, `scripts/review_lw_pow2.py` tests every family on m = 36 + r + 36k (k < 60) with exact integers. All 18
  classes are covered. Only class 15 is covered twice ((7,2) and (3,9)). By hand: classes ≡ 5 (6) and ≡ 1 (6) are covered by the mod-9 families. The
  classes ≡ 3 (6) are 3, 9, 15, 21, 27, 33, and the remaining families cover {3, 15, 27} ∪ {15, 33} ∪ {21} ∪ {9}.
* **Identities.** Checked symbolically (sympy residual 0 for all six families).
* **Size.** The smallest third letter is y = (2^m + 80)/592 for (8,74). It is ≥ 2 iff 2^m ≥ 1104, i.e. m ≥ 11. Explicit solutions with
  min(x,y,z) ≥ 2 exist for every odd m ≤ 3001 except m = 1, 3, 9 (n = 0, 6, 510).
* **Brute force.** Every even n < 3·10⁵ was enumerated. The even non-values are exactly {0, 2, 6, 14, 510}, so the "equivalently" clause is
  right. All non-values < 3·10⁵ are exactly L_{A₃} minus {}; that is, {0,1,2,3,5,6,9,11,14,15,35,105,510}.
* **Novelty.** Lorenzini's own text says "We have not been able to answer this question beyond the following remarks", and Rem 6.4 lists
  2^{2m+1} − 2 as open. Nothing in the 2024 source anticipates the covering. I could not check Wang 2026.
* Cosmetic: the table's "covers odd m (mod 36)" for (3,9) lists 15, 33. That is right; 15 is a double cover.

### Prop 8.1 and Cor 8.2 — SOUND
* For n ≡ 1 (3) we have (2,2,z) with 3z − 2 = n, and z ≥ 2 iff n ≥ 4. For n ≡ 5 (12) we have 12y − 7 = n, and y ≥ 2 iff n ≥ 17. Every n ≡ 5 (12)
  with n ≥ 13 is ≥ 17. ✓ The hypothesis n ≡ 1 (4) is used only to land in 5 (12).
* Remark: the first family alone shows that *every* n ≡ 1 (3), n ≥ 4, is a value. That is not in Lorenzini Prop 6.3, which is stated weaker
  (6.3(c)). The author does use it in §8 "Where (W) is still open". It could be stated as a separate one-line Prop (cosmetic).
* Cor 8.2 follows from HJ_DEEP §3, "interior-SQ₅(n) ⟺ (W)(n) ∧ (S)(n) for n ≡ 1 (4)", and (S)(p) has the hypothesis L₃(p) ≠ ∅, which is now
  automatic. ✓
* Signs, re-derived. Word (3, t, 4) with t = (p+7)/12: A = 3t − 1 = (p+3)/4 ≡ 3·4⁻¹, so (A/p) = (3/p) = (p/3) = −1 for p ≡ 2 (3). Word (2, 2, (p+2)/3):
  A = 3 and A* = (2p+1)/3 ≡ 3⁻¹, so the sign is (3/p) = +1 for p ≡ 1 (12). ✓
* The residue list "n ≡ 3, 9, 11 (12) with n + 2 prime; n ≡ 2, 6 (12) with n + 2 = 2^m" was re-derived. The odd classes mod 12 are 1, 7 (≡ 1 mod 3), 5, and the rest.
  Lorenzini (b) handles odd n with n + 2 composite. All of E_W's odd members {3, 9, 11, 15, 35, 105} indeed have n + 2 prime and lie in 3, 9, 11 (12). ✓

### Lemma 3.1, Remark 3.2 (square shadow) — SOUND
Re-derived by hand.
* (−t/q) = 1 for odd q | tm² + 1 (q ∤ tm). Hence (−t/X₁) = 1.
* (i) 4 | t: X ≡ 3 (4) is odd. (−1/X) = −1. (2/X)^s = 1, since s is even, or s ≥ 3 and X ≡ 7 (8). (t₁/X) = (X/t₁)(−1)^{(t₁−1)/2} = 1. Hence the
  contradiction.
* (ii) t ≡ 3 (4): (−t/X₁) = (−1/X₁)(X₁/t)(−1)^{(X₁−1)/2} = (X₁/t). From 2^a X₁ ≡ −1 (t) we get (X₁/t) = −(2/t)^a, which forces a odd and
  t ≡ 3 (8). For m even, tn + 1 is odd, so a = 0. For m odd, v₂(t + 1) = 2 (t ≡ 3 mod 8), so a_X = a_Z = 1. ✓
* Remark 3.2: for t = 4ks we have tn + 1 = s(2km)² + 1, so (−s/q) = 1. Apply (i) with modulus 4s: (−4s/X) = (−s/X) = −1. ✓ (Not re-run numerically;
  the hand proof is complete.)

### Prop 3.3 — SOUND
* m even: (2, m²/4 + 1, 2).
* 3 ∤ m: (2, 2, (m²+2)/3).
* m = 3k with k odd ≥ 3: (3, (k²+1)/2, 6), where 18·(k²+1)/2 − 9 = 9k². The remaining case m = 3k with k even has m even.
All the size constraints hold for m ≥ 2, m ≠ 3. ✓ The aside "(t = 2, (x,z) = (3,6))" is consistent with the shadow: the middle letters
(m/2)² + 1 ≡ 1, 2 (4) and (k²+1)/2 ≡ 1 (4).

### §1 forms — F0, F1, F3, F4 SOUND; F2 GAP (D1)
`scripts/review_lw_forms.py 1500` implements each form *literally as written* and compares it with brute force for 2 ≤ n < 1500 (F1 for n < 400).
F1, F3 and F4: 0 mismatches. Hand checks:
* F3: ρ = x needs x < d = xy − 1, which is true.
* F4: a = xy − 1 and ā = yz − 1 lie in [1, n − 1], because xy ≤ n ⟺ x + z ≤ xy(z−1), true for x, y, z ≥ 2. Then b = y, since
  (bx−1)(bz−1) − 1 = b(bxz − x − z).
F2 as literally stated is **false at n = 3, 15, 35** (D1).

## Defects

**D1 (MINOR, §1 F2).** The diagonal alternative "x = z (x | n, x | n/x + 2)" omits y = (n/x + 2)/x ≥ 2. It then accepts n = x(x − 2) with y = 1,
including the exceptions 3 = 3·1, 15 = 5·3 and 35 = 7·5. *Repair:* write "x | n, x | n/x + 2 and n/x + 2 ≥ 2x". With this repair, 0 mismatches
for n < 1500 (`review_lw_forms.py`, function `F2_fixed`). Presumably `bsG_forms.py` implements the correct condition, since it reports 0
mismatches; the text should match the script.

### Prop 4.1, Thm 4.2 (sterile set) — SOUND (re-derived by hand; numeric check below)
Re-derivation notes (all steps of the author's proof verified; no gaps):
* Prop 4.1: ν ≤ −2 → x = −ν; ν = 0 → (2,2) (x,z)-kind; ν ≥ 1 → (ν+1, 2). Compactness statement fine (Ẑ∖V compact).
* Thm 4.2, (x,y)-kind: j = 0 gives d = e ≤ x−1 < 2x−1. j ≥ 1 ⇒ ℓ | x−1, x ≥ ℓ+1; ℓ^j ≡ f (mod x) with 0 < ℓ^j ≤ x+ℓ−1 < f+2x ⇒ ℓ^j ∈ {f, f+x}.
  f = ℓ^j ⇒ ℓ^j | ℓ ⇒ d = x−1. f + x = ℓ^j ⇒ x + ℓ − 1 = ℓ^j (as x+ℓ−1 < 2ℓ^j) ⇒ e = (ℓ^j−ℓ)/(ℓ−1), ℓ | e for j ≥ 2, x = 1 for j = 1. ✓ The mirrored (y,z)-kind is identical.
* (x,z)-kind: identity v(km−u) = (ℓ−1)u − m checked by expansion; 0 ≤ s ≤ ℓ−2 needs m < v, which holds since v ≥ 2 (I add: s ≥ 0 because vs > −m > −v).
  s(v−1) = (ℓ−1)u − m − s ✓ (expanded), so u | m+s and (k−1)m ≤ 2s. For a ≥ 2, k−1 = (sℓ^a − ℓ + 2)/(ℓ−1) > 2s already, so even m = 1 is impossible
  (the author's route via u ≤ s+1 gives the same inequality s(ℓ^a−2ℓ+2) ≤ ℓ−2, false for ℓ ≥ 3). For a = 1, ℓ−1 | s+1 ⇒ s = ℓ−2, k = ℓ−1, m ≤ 2;
  m = 1 ⇒ v = 1, m = 2 ⇒ u = ℓ, contradicting ℓ ∤ u. ✓ (ℓ ≥ 3 is used at s = 0 and in the last inequality; at ℓ = 2 the point ν(2,1) is in fact covered.)
* ν(ℓ, ℓ−1) → −1 in Ẑ: for every M, ν ≡ −1 (mod M) once ℓ ∤ M. ✓
* Numerics (`scripts/review_lw_sterile.py 30000`). ν(ℓ, ℓ−1) is covered by no fixed-pair family of modulus ≤ 3·10⁴ for ℓ = 3, 5, 7, 11, 13, 17, 101.
  ν(2,1) *is* covered, e.g. by (x,z) = (3,4). The controls ν(3,0) and ν(5,1) are covered. This is consistent with the theorem and its hypothesis ℓ ≥ 3.

### Cor 4.4 — SOUND; the label can be UPGRADED (no dependence on the 10⁹ enumeration needed)
`scripts/review_lw_cor44.c` is from scratch: 16 s, one core, 0.6 GB. It enumerates all 68 683 fixed-pair families whose modulus d divides
M = 151 351 200 = 2⁵3³5²7²·11·13. It marks every n ∈ [0, 3M) that lies in a family class *and* is above that family's size threshold. The thresholds
are 2d − x and 2xz − x − z, both < 2M. Results:
* |U_M| = **11 550** (density 7.631·10⁻⁵). Its projection mod 12 is {3, 6, 9, 11}. Both match the text.
* The unmarked n < 2M whose class lies *outside* U_M were each tested for (W) by direct search. The only non-values are
  2, 3, 5, 6, 9, 11, 14, 15, 35. The other two members of E_W, 105 and 510, lie in U_M classes.
So Cor 4.4 holds as stated, and its proof needs only the range n < 2M ≈ 3.03·10⁸ (not 10⁹). That range is closed by the same 16-second
computation. See D2.

### Prop 6.1 (rate N exp(−c√log N)) — SOUND-AFTER-REPAIRS (minor; label should be plain PROVED with citation)
Every step was re-derived.
* **Avoided classes.** For p ≤ Q = √N and x | p + 1 with 2 ≤ x ≤ (p+1)/2, the word (x, (p+1)/x, (n+x)/p) needs n + x ≥ 2p, which holds since
  n > N = Q² ≥ 2p. ω(p) = τ(p+1) − 2 counts distinct classes −x mod p (x < p), and ω(p) < p. ✓
* **Large sieve.** Montgomery's form |S| ≤ (N + Q²)/L, with L ≥ e_k(g; I) obtained by restricting to m = products of k distinct primes of
  I = (Q^{1/2k}, Q^{1/k}] (so m ≤ Q). The bound ω/(p−ω) ≥ ω/p is fine. ✓
* **G.** Σ_{p ≤ y} τ(p+1) = Cy + o(y) with C = ζ(2)ζ(3)/ζ(6). The shift +1 has no local correction factor, so the constant is right. Partial summation over
  I is uniform because the lower end a = Q^{1/2k} = exp(√log Q/(2ε)) → ∞. This gives G = (C/2 + o(1)) log Q / k − 2 log 2 + o(1). ✓
* **e_k step.** Inclusion–exclusion gives exactly k!·e_k ≥ G^k − C(k,2)·T·G^{k−2} with T = Σ_{p∈I} g(p)². (Sanity-checked in exact rationals:
  `scripts/review_lw_ek.py`.) With k = ε√log Q, k/G → 2ε²/C is a *constant*, not o(1). So "1 − O(k²/G²)" is only harmless because T → 0
  (T ≤ Σ_{p>a} p^{−2+o(1)}) or because ε is small. The text's justification "Σ g² < ∞" is enough only with that remark. See D3.
* **Conclusion.** e_k ≥ ½ G^k/k! ≥ ½ (eG/k)^k / (e√k), and eG/k ≈ eC/(2ε²) > e for small ε. So L ≥ exp(c′√log Q). With dyadic summation
  the result is ≪ N exp(−c√log N), c absolute. ✓
* **Label.** The input (Titchmarsh divisor problem for p + 1) is a theorem: Linnik 1963 (dispersion), and Rodriquez 1965 / Halberstam 1967 via
  Bombieri–Vinogradov. "PROVED relative to the Titchmarsh divisor asymptotic" is over-cautious. It should be **PROVED** with that citation (D3).
  The lower bound Σ_{p∈I} τ(p+1)/p ≫ log Q/k actually needs only BV, not the full asymptotic.
* **Context.** Lorenzini's Prop 6.3(b) already trivially gives #E ≤ π(N+2) + O(log N) ≪ N/log N, and Lorenzini 6.3's z = 4 condition gives
  N/(log N)^{3/2}. "Lorenzini/Wang give density 1 only" is literally true for Lorenzini's statement, but his (b) gives N/log N at once. The note
  should say so, so that the improvement is stated against the right baseline (D4).

### Prop 7.1 (Stern coding) — SOUND
Re-derived. Under N ↦ 2N the pair (u, w) = (s(N), s(N+1)) becomes (u, u+w). Under N ↦ 2N+1 it becomes (u+w, w). So the block 0^{a−2}1 gives
((a−1)u + w, (a−2)u + w). With (p, q) = (u, u − w) this is (p, q) ↦ (ap − q, p). The start N = 1 has (p, q) = (1, 0). Conversely, every N with
popcount k + 1 is, after stripping trailing zeros, of the stated shape with a_i = (gap) + 2 ≥ 2. ✓
`scripts/review_lw_stern.py` finds 0 mismatches for k ≤ 4 (letters < 12, or < 8 for k = 4). It also checks that {s(N) : popcount 4} ∩ [0, 300) equals
the A₃ value set there. The complement is {0,1,2,3,5,6,9,11,14,15,35,105}. ✓
Minor: the phrase "positions of popcount k+1 … of size ≍ (log)^k up to height N" does not say whether "height" means the position or the value.
Positions with N < X number ≍ (log X)^k. The value s(N) is not monotone in N, so this does not count anything about values (cosmetic).
