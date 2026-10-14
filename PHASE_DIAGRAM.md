# PHASE_DIAGRAM — the (k, Q₁) phase diagram between ES^□ / ES^{(y)} and ES (task O204, wave Y-a)

Status: checkpoint 1 reviewed by R209 (reviews/phase-diagram-review.md) and R210 (reviews/phase-diagram-review-2.md):
no FATAL; all repairs applied, marked (R209 repair)/(R210 repair). (O204.) **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP.md (O200: Prop 1.2, Prop 1.3 duality D·g = 4k²n + Q₁², Thm 2.1, Prop 3.1, Thm 3.2; R200 M1),
GROWING_MUTE.md (O201: (A, B) form, V_n), MARKOFF_ES.md (O202), COMPOSITION_ES.md (O203), FROBENIUS_FIRING §4,
UNIT_ORBIT_ES §2, SYNTHESIS_SPARKS2 §2 (ES^□). Scripts `scripts/pd_*`.

Notation (as in GROWING_MUTE, widened shot family): n > 1 odd; shot datum (Q, g): Q ≥ 1, gcd(Q, n) = 1, g ≡ 3 (mod 4),
g | n + 4Q²; K := (g+1)/4, Q₀ := gcd(Q, K), overflow Q₁ := Q/Q₀, k := K/Q₀; den(z) = Q₁², y = n(g+1)/4 = nQ₀k.
Only shot data with Q₁ ODD are used (the variants require odd den z; Q₁ is odd iff v₂(Q) ≤ v₂(K), e.g.
n = 5, Q = 2, g = 3 has Q₁ = 2) (R210 repair m1). den z = Q₁² holds for every such shot, Q₀ of either parity: the
proof of EXPONENT_CAP Prop 1.2 is prime-by-prime over ℓ | Q₁ and never uses the parity of Q₀ (R209 repair m2).
Variants: ES ⇒ ES^{(y,1)} ⇒ ES^{[2]} (Q₁ | Q₀, "den z | y²") ⇒ ES^{(y)} (rad Q₁ | Q₀k); ES^□: no mute condition.

## 0. Iteration log

(Y1) Construction attempt as briefed (sieve r ≡ −1 mod 4P, P ≈ r^{1/4}, Q₁ | P). Screen: for each r the admissible
set {Q : Q | K·rad K} has size ≤ τ(K)2^{ω(K)} = r^{o(1)}, so a single-n statement needs a *hit*; switching the
order of summation turns the hit count into Σ_Q #{r | n + 4Q² : r ≡ −1 (mod 4Q₀)}, i.e. divisors of n + 4Q² in a
class of modulus 4Q₀ ≥ 4√Q ≈ (n + 4Q²)^{1/4} — the Lenstra/Coppersmith threshold (EXPONENT_CAP Prop 4.1).
Hypothesis to violate: "the per-r box is r^{o(1)}". Bounded cap cannot violate it (Prop 3.1), so look for
(a) a deterministic mechanism (Pell / genus / units: T1-exact facts that hold exactly at non-squares), or
(b) a different slicing in which the modulus is fixed.
(Y2) Exact re-slicing (§1): ES^{[2]} ⟺ ∃ (t, j): n t² + 4 j² has a divisor ≡ −n (mod 4tj) (t ⊇ overflow; side
conditions in §1), the "D-face" of the duality; ES is t = 1. The λ = 1 sub-family is the quartic family "n + 4t⁴ has a divisor ≡ −1
(mod 4t)", and its j = 1 member is the FIXED-modulus test "64 + n³ has a divisor m ≡ −n (mod 4) with t = (m + n)/4 odd
and the gcd side conditions of §1" (≡ 3 (mod 4) when n ≡ 1 (mod 4)) (R209 repair m1) (e.g. n = 13:
64 + 13³ = 7·17·19, m = 7 (the cofactor (n + 4Q²)/g of §1, not the duality cofactor D = 47 of Prop 1.3), t = 5, g = 359 | 13 + 4·25² → an ES^{(y,1)} solution of 4/13 with overflow 5). Fixed modulus only for one number per j: no infinite fixed-modulus family.
(Y3) Screen of (Y2): every slicing is one number per fixed parameter; the infinite directions all have moving
modulus. But the slicing exposes a structural fact that is new: with the self-mute cap Q₁ | Q₀ BOTH coordinate
directions of the duality plane are walled (§2), while every weaker variant has an unwalled direction. The phase
diagram is therefore organised by walls, and ES^{[2]} is the unique doubly-walled cell above ES (§3–§4).

## 1. Normal form: the overflow is a Q₁²-weight in the Type II equation

**Proposition 1.1 (PROVED; a re-expression of EXPONENT_CAP Prop 1.3 / Cor 1.4).** Let n > 1 be odd. Shot data
(Q, g) correspond bijectively to quadruples (a, b, k, Q₁) of positive integers with Q₁ odd, gcd(Q₁, k) = 1 and
`  k·(4ab − n) = b + a·Q₁²,    (1.1)`
via a = Q₀, b = (m + n)/(4Q₀) (m := (n + 4Q²)/g), k = (g+1)/(4Q₀), Q = aQ₁, g = 4ak − 1, m = 4ab − n
(plus gcd(aQ₁, n) = 1 for the shot convention). The overflow is Q₁, den z = Q₁², y = nak. In these coordinates
* ES (shot family = the d = 1 slice of ET's Type II 4abcd = a + b + nc): Q₁ = 1, i.e. k(4ab − n) = a + b;
* ES^{(y,1)}: Q₁ squarefree and Q₁ | a;  ES^{[2]}: Q₁ | a;  ES^{(y)}: rad Q₁ | a;  ES^□: no condition.
*Proof.* Prop 1.3: j' := (m + n)/Q₀ ∈ 4ℤ, so b = j'/4 ∈ ℤ_{>0}; D := kj' − Q₁² = 4kb − Q₁² and (a) reads
4Q₀D = 4kn + j', i.e. aD = kn + b, i.e. a(4kb − Q₁²) = kn + b, which is (1.1). Conversely (1.1) gives
m := 4ab − n > 0 with k m = b + aQ₁²; put g := 4ak − 1; then g·m = 16a²bk − 4akn − 4ab + n = 4a(b + aQ₁²) − 4ab + n
= n + 4a²Q₁², so g | n + 4Q² with Q = aQ₁, and gcd(Q, (g+1)/4) = a·gcd(Q₁, k) = a. ∎
*D-face (ES^{[2]}).* Writing a = λt, Q₁ = t: k(4λtb − n) = b + λt³; equivalently (eliminating k)
**ES^{[2]} shots with overflow exactly t (odd) ⟺ (λ, t, b) with m := 4λtb − n > 0, gcd(λtb, n) = 1,
m | b + λt³ and gcd(t, k) = 1 for k := (b + λt³)/m.** Under gcd(m, 2bn) = 1 (equivalently gcd(λtb, n) = 1, since
m is odd, gcd(m, n) = gcd(4λtb, n) and gcd(m, b) = gcd(n, b)), m | b + λt³ ⟺ m | nt² + 4b² (as
4b(b + λt³) ≡ nt² + 4b² mod m). Without these side conditions both equivalences fail (R-self-review: n = 9,
λ = t = 1, b = 3: m = 3 | 45 but m ∤ 4; n = 61, λ = 1, t = 3, b = 6: m = 11, k = 3, true overflow 1, not 3).
ES is t = 1: 4λb − n | λ + b. The quartic family of (Y2) is λ = 1.

## 2. The double wall of ES^{[2]}

**Theorem 2.1 (PROVED).** Let (Q, g) be an ES^{[2]} shot of odd n > 1 (overflow Q₁ odd, Q₁ | Q₀), k = (g+1)/(4Q₀).
(a) (**k-wall, new**) Q₁ ≤ W(k) := (16k³n + 1)/(4k − 1) = 4k²n + kn + (kn + 1)/(4k − 1) ≤ 6k²n.
(b) (Q₁-wall) g ≤ 2nQ₁²(n + Q₁²) (EXPONENT_CAP Thm 2.1); moreover if Q₁ > (n+1)/2 then k < Q₁²/2.
Hence every ES^{[2]} shot with Q₁ > (n+1)/2 lies in the band **√(Q₁/(6n)) ≤ k < Q₁²/2**: both
coordinates must grow together, every horizontal (fixed Q₁) and every vertical (fixed k) slice is a finite search.
**Thm 2.1 does NOT make ES^{[2]} or ES^{(y,1)} a finite search (R210 repair m2; R209 repair m3).** It gives no bound on
g, k or Q₁ in terms of n alone: the band is unbounded, and (GROWING_MUTE, R201 m3) every ES^{[2]} point with μ² − n
non-square lies on an infinite Pell orbit inside it (fixed-n examples with growing (Q₁, k): n = 3 has (55, 2), (101, 232),
(289, 2984), R210 `review_pd2_brute.py`). So the cell is an infinite union of finite slices; **R200 M1 (bounded e,
growing S: OPEN, not a finite search) stands for e = 1**, narrowed only in that k and Q₁ must grow together
(for Q₁ > (n+1)/2; equivalently the growing-S case needs Q₀ > (g+1)/(2Q₁²)).
*Proof.* (a) Prop 1.3(b): Dg = 4k²n + Q₁² with D ≥ 1. As Q₁ | Q₀, g = 4kQ₀ − 1 ≡ −1 (mod 4kQ₁), so g ≥ 4kQ₁ − 1
and, reducing Dg mod Q₁, D + 4k²n ≡ 0 (mod Q₁); hence D ≥ Q₁ − 4k²n. If Q₁ ≤ 4k²n, (a) holds because
(16k³n + 1) − 4k²n(4k − 1) = 4k²n + 1 > 0. Otherwise 4k²n + Q₁² = Dg ≥ (Q₁ − 4k²n)(4kQ₁ − 1), which expands to
(4k − 1)Q₁² ≤ (16k³n + 1)Q₁. (b) In the proof of EXPONENT_CAP Thm 2.1, the case kj' ≥ 2Q₁² gives Q₀ ≤ (n+1)/2, and
Q₁ | Q₀ then gives Q₁ ≤ (n+1)/2; so Q₁ > (n+1)/2 forces the case kj' < 2Q₁² with j' ≥ 4, i.e. k < Q₁²/2. ∎
*Sharpness.* (a) is attained exactly: (n, k, Q₁) = (3, 2, 55), g = 439 (W(2) = 385/7 = 55), and for EVERY
n ≡ 2 (mod 3) at k = 1 by the family Q₁ = W(1) = (16n + 1)/3, g = 4Q₁ − 1 = (64n + 1)/3, D = (4n + 1)/3, Q = Q₁²
(check: Dg = (4n+1)(64n+1)/9 = 4n + Q₁²; D ≡ 3 (mod 4) iff n ≡ 2 (mod 3); gcd(Q₁, n) = 1), an ES^{[2]} shot
(even ES^{(y,1)} when 16n + 1 is squarefree) with overflow ≈ 5.3n. (Also Q₁ = 4n + 3, D = 3 for n ≡ 2 (mod 3).) (b): k/Q₁² up to 0.436 is observed ((n, k, Q₁) = (29, 126, 17), g = 8567).
*Check (`scripts/pd_band.py 101 6 1.3`, `scripts/pd_band2.py 41 41`; exact rationals):* all 348 shots (gcd(Q, n) = 1; 12 further
solutions with gcd(Q, n) > 1 skipped) with odd n ≤ 101, k ≤ 6, Q₁ ≤ 1.3·W(k), and all 36 shots with n ≤ 41, (n+1)/2 < Q₁ ≤ 41, k ≤ 2Q₁²: identity (1.1), solution,
den z = Q₁², walls (a), (b) hold; max Q₁/W(k) = 1.000, max k/Q₁² = 0.436.
*Reading.* Without the self-mute cap the k = 1 slice is infinite and elementary (ES^□: "4n + Q₁² has a divisor
≡ 3 (mod 4)", Dirichlet). The cap Q₁ | Q₀ converts the modulus 4 into 4Q₁ and the k = 1 slice (each fixed-k slice) into a finite
search — not the cell (see above): the k-wall is created exactly by the self-mute cap, as the Q₁-wall of EXPONENT_CAP is created by fixing Q₁.

## 3. One slice, the whole ladder: k = 1

The k = 1 slice is where the duality plane meets ES^□. By Prop 1.3's converse with k = 1, k = 1 shots of overflow
Q₁ (odd, prime to n) are exactly the divisors g ≡ 3 (mod 4) of **4n + Q₁²** (cofactor D ≡ 3 (mod 4) automatically;
Q₀ = (g+1)/4, Q = Q₀Q₁; we also need gcd(Q₀, n) = 1). The mute rungs become congruences on g alone:
`  rung      condition on (Q₁, g)                                    modulus      status (k = 1 slice)`
`  ES^□      none                                                     4            PROVED‡ (one Dirichlet prime; Cor 3.2)`
`  ES^{(y)}  Q₁ ∈ ⟨S⟩ (S fixed, |S| ≥ 4), g ≡ −1 (mod 4·rad Q₁)      4·∏S fixed   PROVED† (FROBENIUS_FIRING Thm 4.2 sieve)`
`  ES^{(y,2)} v_ℓ(Q₁) ≤ 2, g ≡ −1 (mod 4·rad Q₁)                     ≥ 4√Q₁       OPEN; no wall (EVIDENCE below)`
`  ES^{(y,1)}, ES^{[2]}  g ≡ −1 (mod 4Q₁)                             4Q₁          FINITE: Q₁ ≤ (16n+1)/3 (Thm 2.1(a))`
`  ES        Q₁ = 1                                                  4            one number, 4n + 1`
(‡ n odd non-square; † n odd non-square with 3 ∤ n, ineffective — R210 repair m3, R209 repair m4/m5. R210 m3 also
notes that the convention gcd(Q₀, n) = 1 is not needed for the solution itself (den z stays prime to n); dropping it
from the k = 1 slice would remove the 3 ∤ n condition. Not pursued here.)
**Proposition 3.1 (PROVED; (a) ineffective, R209 repair m5).** (a) For every odd non-square n > 1 with 3 ∤ n
(R209 repair m4; first version: gcd(n, 15) = 1), the k = 1 slice of ES^{(y)} is non-empty: there are Q₁ ∈ ⟨S⟩ (S any four odd primes prime to n) and a prime g ≡ −1 (mod 4∏S) with g | 4n + Q₁².
(b) For ES^{(y,1)} and ES^{[2]} the k = 1 slice is contained in Q₁ ≤ (16n + 1)/3; for n ≡ 2 (mod 3) this bound is
attained in ES^{[2]}, and in ES^{(y,1)} when (16n + 1)/3 is squarefree (not always: n = 59, W(1) = 315 = 3²·5·7).
*Proof.* (a) Follow FROBENIUS_FIRING Thm 4.2(a) / UNIT_ORBIT Thm 2.4(a): M := 4 rad(n)∏S, a ≡ 3 (mod 4),
a ≡ −1 (mod s) for s ∈ S, and for ℓ | n residues a_ℓ chosen so that every prime r ≡ a (mod M) has (n/r) = −1
(by reciprocity this is a condition on the Jacobi symbol (r/n), adjusted at one prime ℓ₀ | n of odd exponent; such
ℓ₀ exists since n is not a square, n ≡ 3 (mod 4) included). Additionally take a_ℓ ∉ {0, 1, −1} (mod ℓ): possible for
every ℓ ≥ 7 with either prescribed quadratic character (outside {0, ±1} there remain (ℓ − 5)/2 ≥ 4 residues and
(ℓ − 1)/2 non-residues if ℓ ≡ 1 (mod 4), and (ℓ − 3)/2 ≥ 2 of each if ℓ ≡ 3 (mod 4)); at ℓ = 3 nothing remains and
at ℓ = 5 only non-residues {2, 3}. (R209 repair m4:) ℓ = 5 is harmless: if v₅(n) is even it does not enter the
Jacobi symbol; otherwise adjust at another odd-exponent prime ℓ₀ ≥ 7 if one exists, and if 5 is the only one then
n = 5m² ≡ 1 (mod 4) and the required (r/n) = (r/5) = −1 is exactly a₅ ∈ {2, 3}. Only ℓ = 3 | n is a genuine
obstruction (it forces r ≡ 1 (mod 3), outside Lemma 2.2); hence 3 ∤ n. Lemma 2.2 of UNIT_ORBIT only needs a ≢ 1 (mod ℓ), so the sieve of Thm 4.2
applies verbatim and gives a prime r ≡ a (mod M) with Γ_r := ⟨S mod r⟩ = (F_r^*)². Then
(−4n/r) = (−1/r)(n/r) = 1, so −4n ≡ Q₁² (mod r) with Q₁ ∈ ⟨S⟩ (squaring is bijective on the odd-order group
(F_r^*)²); put g := r. Q₀ = (r+1)/4 is prime to n (r ≢ −1 mod ℓ), and rad Q₁ | ∏S | Q₀. (b) is Thm 2.1(a) at
k = 1 together with its sharpness family. ∎
(R-note for the reviewer: (a) is a re-run of a reviewed sieve with one more excluded residue per ℓ | n; the
proof of Thm 4.2 uses Lemma 2.2, which allows any class a with a ≢ 1 (mod ℓ), so excluding −1 as well is free.)
**EVIDENCE (`scripts/pd_k1.py 200000 13 17 29 37 97 101 9 25`, every shot verified with exact rationals,
den z = Q₁², rad Q₁ | y).** k = 1 shots with Q₁ ≤ 2·10⁵:
* e ≤ 1 (squarefree Q₁): n = 13: 0; 17: 5 (max Q₁ = 91 = W(1)); 29: 6 (max 155 = W(1)); 37: 0; 97: 2 (max 79);
  101: 13 (max 431 < W = 539). All below the wall, as proved.
* e = 2, non-squarefree Q₁ (beyond ES^{(y,1)}): occupied bit-lengths of Q₁ — n = 13: {6, 11, 12, 15, 16, 18};
  17: {5, 6, 9, 12–17}; 29: {5, 6, 8–11, 14–16, 18}; 37: {9, 12, 13, 18}; 97: {7, 11, 13, 14, 17, 18};
  101: {6, 7, 9–18} (1–7 hits per occupied octave; sparse, with gaps of up to 4 octaves); max Q₁ = 185 761,
  120 409, 152 881, 194 271, 165 649, 192 721, i.e. hits up to the search limit 2·10⁵ ≫ W(1) — no wall seen, and
  n = 13, 37 (no e ≤ 1 shot at k = 1) have e = 2 shots. Whether there are infinitely many is open. T1: n = 9, 25: no shot on any rung.
**EVIDENCE for Prop 3.1(a) with ONE mute prime (`scripts/pd_k1s.py 1000000 40`, GNU factor with return-code and
output-count checks, exact rationals; re-run after the self-review, identical).**
For every prime 5 ≤ p < 10⁶ there is a ≤ 21 such that 4p + 9^a has a divisor g ≡ −1 (mod 12) (a = 0: g ≡ 3 mod 4),
i.e. a k = 1 ES^{(y)} shot with Q₁ = 3^a, den z = 9^a, 3 | y (a ≥ 1; a = 0 is an ES shot). Least-a histogram: 0: 59 504, 1: 6 911, 2: 4 726,
3: 2 548, 4: 2 040, 5: 799, 6: 524, 7: 426, 8: 339, 9: 236, 10: 183, 11: 91, 12: 66, 13: 43, 14: 25, 15: 17, 16: 10,
17: 4, 18: 1, 19: 2, 21: 1. T1 control: none of the 332 odd squares m² < 10⁶ (3 ∤ m) has one (sum of two coprime
squares). On the k = 1 slice the overflow exponent is exactly a, so this is the least cap within the family Q₁ = 3^a (not
within the whole k = 1 slice: n = 13 needs a = 3 here, but Q₁ = 49, g = 223 is a k = 1 cap-2 shot).
*Reading (Assessment).* Inside the single slice k = 1 the cap ladder shows every phase: fixed modulus (proved,
Dirichlet/sieve), moving modulus ≥ 4√Q₁ ≈ (4n + Q₁²)^{1/4} with no archimedean bound (e = 2: an infinite lottery
near the N^{1/4} threshold of Lenstra (1984) / CHN (2008); sparse hits up to the search limit, infinitude heuristic only), moving
modulus 4Q₁ ≈ (4n + Q₁²)^{1/2} (e ≤ 1: finite search ON THE k = 1 SLICE, the k-wall; the e ≤ 1 cell as a whole is an
infinite union of finite slices, R200 M1 stands — R210 repair m2), and the single number of ES. So, on the k = 1
slice, the transition "infinite lottery → finite search" happens between e = 2 and e = 1, and the transition "proved → lottery" between
e = ∞ (fixed S) and every bounded e.
*Corollary 3.2 (k-direction dichotomy; PROVED).* Every fixed-Q₁ slice of every variant is finite (EXPONENT_CAP
Thm 2.1). Every fixed-k slice of ES^{[2]} ⊇ ES^{(y,1)} ⊇ ES is finite (Thm 2.1(a)). For every odd NON-SQUARE n the k = 1 slice of ES^□ and,
if also 3 ∤ n, of ES^{(y)} (fixed S, |S| ≥ 4; ineffective) is INFINITE (at odd squares every shot slice is empty, T1;
scaling produces general solutions there, not shots): the sieve of Prop 3.1(a) gives infinitely many distinct primes
g, and g ≤ 2nQ₁²(n + Q₁²) forces Q₁ → ∞.
*Proof for ES^□ (R209 repair M1).* Choose, by Dirichlet, infinitely many primes g ≡ 3 (mod 4) in a class mod 4 rad(n)
with g ≢ 0, −1 (mod ℓ) for every ℓ | n and (n/g) = −1. This is possible for every odd non-square n: at ℓ = 3 the only
allowed class is g ≡ 1 (a residue); at ℓ = 5 both characters remain; at ℓ ≥ 7 both remain (Prop 3.1); so adjust the
character at an odd-exponent prime ℓ₀ ≥ 5 if one exists, and if 3 is the only odd-exponent prime then n = 3m² ≡ 3
(mod 4) and the needed (g/n) = (g/3) = +1 is exactly g ≡ 1 (mod 3) (by reciprocity (n/g) = −(g/n) for n ≡ g ≡ 3
mod 4; for n ≡ 1 (mod 4), (n/g) = (g/n)). Then (−4n/g) = 1, so −4n ≡ Q₁² (mod g) has a root, which can be taken odd
and prime to n (shift by multiples of g, CRT); Q₀ = (g+1)/4 is prime to n, and Prop 1.3's converse with k = 1 gives
a k = 1 shot of overflow Q₁. Distinct g give distinct shots, and Q₁ → ∞ as above. ∎ So the k-wall exists exactly at relative
cap ≤ 1 among these variants (each fixed-k slice finite; the cell itself is not a finite search, §2); for bounded absolute cap e ≥ 2 its absence is EVIDENCE only (§3 table).

## 4. One family for all caps: "nX² + 1 has a divisor ≡ −1 (mod M)", M ≈ N^{1/(2e+2)}

**Proposition 4.1 (PROVED).** Let n be odd, e ≥ 0, k, λ, R ≥ 1 with R odd, gcd(R, 2kn) = 1, M := 4kλ, g := MR − 1,
X_e := 2k·M^e, N_e := nX_e² + 1. Then g | 4k²n + R^{2e} ⟺ g | N_e, and in that case (Q, g) with Q = λR^{e+1} is a
shot with Q₀ = λR, overflow exactly R^e, den z = R^{2e} (if gcd(λR, n) = 1). Consequently
`  ES^{(y,e)}(n) ⟸ ∃ k, λ ≥ 1, gcd(λ, n) = 1: N_e = n(2k(4kλ)^e)² + 1 has a divisor g ≡ −1 (mod 4kλ) with`
`                   R = (g+1)/(4kλ) odd, squarefree, prime to kn   (gcd(λ, n) = 1: R209 repair m7),`
and for e = 0 this is exactly ES's shot family (λ = 1: "4k²n + 1 has a divisor ≡ −1 (mod 4k)"); for e = 1 it is
the general ES^{[2]} shot (GROWING_MUTE (A, B) form with A = 2k, B = R, Q₀ = λB) with X₁ = 8k²λ.
*Proof.* MR ≡ 1 (mod g) and gcd(M, g) = 1, so multiplying 4k²n + R^{2e} by M^{2e} gives 4k²nM^{2e} + 1 = N_e
(mod g). Then D := (4k²n + R^{2e})/g ≡ −R^{2e} (mod 4k) (as g ≡ −1), and Prop 1.3's converse with (k, Q₁ = R^e)
gives Q₀ = (g+1)/(4k) = λR and Q = Q₀Q₁ = λR^{e+1}; gcd(Q, Q₀k) = λR·gcd(R^e, k) = λR, so the overflow is R^e. ∎
*Check (`scripts/pd_theta.py 201 8 300`):* for odd n ≤ 201, k, λ ≤ 8, e ≤ 2: 349 / 670 / 1172 shots (e = 0/1/2; plus 19 / 40 / 104
exact solutions with gcd(Q, n) > 1, not shots) found via N_e, each exact with den z = R^{2e}; the equivalence g | 4k²n + R^{2e} ⟺ g | N_e checked on
2 802 432 (n, e, k, λ, R) with e ≤ 3, R ≤ 300.
*The modulus exponent (R209 repair m7, R210 repair m6: θ belongs to a parametrisation, not to a cell).* Define
θ_e := inf log M/log N_e over the Prop 4.1 face; it is approached along bounded λ, where log M/log N_e → 1/(2e+2)
(exactly M^{e+1} = 2λX_e, so M = (2λX_e)^{1/(e+1)} ≈ (2λ)^{1/(e+1)}(N_e/n)^{1/(2e+2)}); with k fixed and λ → ∞ the same
family has log M/log N_e → 1/(2e) (e ≥ 1; for e = 1 the face ranges over [1/4, 1/2), R210 measured 0.486 at k = 1,
λ = 10³⁰), and for e = 0, M = 4kλ ranges up to g, θ ∈ [½, 1). ES ⊂ ES^{[2]} (R = 1) sits at θ ≥ 1/2 on the e = 1 face.
For the proved rows below, θ refers to the prime-face modulus 4∏S (a different face), consistent with θ_e → 0.
`  e = 0 (ES):            θ_0 = 1/2  — Lenstra's regime (≤ 11 divisors in a class mod > N^{1/3}; bounded count)`
`  e = 1 (ES^{(y,1)}, ES^{[2]}): θ_1 = 1/4 — the N^{1/4} threshold of Lenstra (1984: O((α−¼)^{−2}) divisors in a class`
`                         mod s ≥ N^α, α > ¼) and CHN (2008: O((α−¼)^{−3/2}), constructive) (R209 m6, R210 m5 repairs);`
`                         on the e = 1 line M ≍ (2λ)^{1/2}n^{−1/4}N_1^{1/4}: no margin α > 0, neither theorem applies`
`  e = 2:                 θ_2 = 1/6  — below the threshold: no bound on divisors in one class is known (Lenstra's question)`
`  e = ∞, S fixed (ES^{(y)}): M fixed (θ → 0) — Kummer/Chebotarev firing, sieve-provable (Thm 4.2)`
`  no mute (ES^□):        M = 4                 — Dirichlet`
*Scope (R-self-review).* For e ≥ 2 Prop 4.1 is a SUFFICIENT sub-family (pure-power overflow R^e); general
ES^{(y,e)} shots have mixed exponents (e.g. n = 113, k = 1, Q₀ = 15, Q₁ = 75, g = 59 is ES^{(y,2)} with Q₁ not a
square). θ = 1/(2e+2) holds for bounded λ; with k fixed and λ → ∞ the same family has θ → 1/(2e).
*Reading (Assessment).* On this axis ES is θ_0 = 1/2, the e = 1 face reaches down to θ = 1/4 (the Lenstra/CHN
threshold; at θ = 1/4 itself no uniform bound follows), and the
proved cells are at θ → 0. The k-wall of Thm 2.1 is an elementary consequence of the duality cofactor
D = (4k²n + Q₁²)/g being < Q₁ (it is NOT the cofactor N_e/g of this face, which can be large: n = 13, e = 1, k = 5,
λ = 2, R = 3 gives N_e/g = 17 479 while D = 11); I do not claim a derivation of the wall from CHN. The brief's hook
(R200 M1: P ≈ r^{1/4}) is the e = 1 line read from the prime-g side.

## 5. Pushing the proved side down: ES^{(y)} with a sub-polynomial exponent cap

EXPONENT_CAP Thm 3.2 gives cap e ≤ y^δ with a FIXED set S of k ≥ 2/δ + 1 primes; its Remark (2) (Assessment) says
letting k grow is limited by the sieve modulus. Making that remark a theorem:

**Theorem 5.1 (ES^{(y,e)} with sub-polynomial cap; PROVED relative to Bombieri–Vinogradov and Iwaniec's linear
sieve, as UNIT_ORBIT Lemma 2.2; ineffective).** (R209 repair M2, R210 repair m7: family form, not an o(1) on one
solution.) For every A ≥ 1, η > 0 and odd non-square n ≡ 1 (mod 4) there is x₀ = x₀(n, A, η) (ineffective) such that
for every x ≥ x₀ there is a solution of ES^{(y,e)}(n) with x/8 ≤ y ≤ nx and
`  e ≤ y^{(2 + η)·log₃y / (A·log₂y)}`   (log₂ = log log, log₃ = log log log),
of Type II shape at every prime of n. For n ≡ 3 (mod 4) there is an ES solution (e = 0); for odd squares and the
remaining n the same family bound holds with y-window scaled by the cofactor (scaling, see proof). In particular
for every ε > 0 and odd n > 1 there is a solution with e ≤ y^{ε·log₃ y/log₂ y} (take A > 3/ε).
(R209 m8: the onset is astronomically late — A = 1 needs log x ≳ 10⁴ merely to have k ≥ 4, R209
`review_pd_thm51.py`; the theorem concerns enormous certifying primes.)
*Proof.* n ≡ 3 (mod 4) is ES with Q = 1; squares (and other n ≡ 1 mod 4 via a divisor) follow from a non-square
divisor p | n by scaling (FROBENIUS_FIRING Thm 4.2(c); the bound is monotone in y), running the argument for p with
S the first k odd primes not dividing the ORIGINAL n, so that no mute prime divides n (R210 repair m8). Let n ≡ 1 (mod 4) be a non-square, x large, and S = {s₁ < … < s_k} the
first k odd primes not dividing n with P := ∏S ≤ (log x)^A maximal; by the prime number theorem k log k ~ A log₂x,
so k ~ A log₂x/log₃x. M := 4 rad(n)P ≤ 4n(log x)^A; the class a mod M is that of Thm 4.2(a).
*Step 1 (sieve, uniform in M).* Fix ε = 1/100. Sift 𝒜 = {(r−1)/2 : x/2 < r ≤ x, r ≡ a (M)} by primes ℓ ∤ M, ℓ < z = x^{1/4−ε},
level D = x^{1/2}/(M log^{β}x) with β = β(A) the Bombieri–Vinogradov exponent for saving log^{2A+10}. Remainders:
distinct d give distinct moduli Md ≤ x^{1/2}/log^{β}x, so Σ_d |r_d| ≤ Σ_{q ≤ x^{1/2}/log^{β}x} max_a |E(x; q, a)|
≪_A x/log^{2A+10}x (Bombieri–Vinogradov, max form, for π(x) − π(x/2); uniform in M). Main term X·V(z)·(f(s) − o(1)) with X ≍ x/(φ(M) log x), V(z) ≫ 1/log z (the density 1/(ℓ−1) on
ℓ ∤ M, dimension 1, constants absolute; ∏_{ℓ|M}(1 − 1/(ℓ−1))^{−1} only helps), s = log D/log z → 2/(1 − 4ε) > 2.
So ≫ x/(φ(M) log²x) ≥ x/log^{A+3}x primes r ∈ (x/2, x] in the class with every prime factor of (r−1)/2 ≥ z.
*Step 2 (index).* As in Thm 4.2, Γ_r := ⟨S mod r⟩ ⊆ (F_r^*)², and a nontrivial index is ≥ z, so |Γ_r| ≤ x^{3/4+ε}.
Lemma 2.3's count made explicit: if |Γ_r| ≤ Y, the (B'+1)^k > Y products ∏ s_i^{a_i} (0 ≤ a_i ≤ B' := ⌈Y^{1/k}⌉)
collide, so r | N_c := ∏_{c_i>0} s_i^{c_i} − ∏_{c_i<0} s_i^{−c_i} ≠ 0 for some 0 < |c|_∞ ≤ B'; N_c has
≤ B' log P/log(x/2) + 1 prime factors > x/2. Hence #{r ∈ (x/2, x] : |Γ_r| ≤ Y} ≤ (2B'+1)^k(B' log P + 1)
≤ 6^k·Y^{1+1/k}·3 log P (R210 m9), which for Y = x^{3/4+ε}, k ≥ 4 is ≤ x^{15/16+2ε}(log x)^{O(A)} = o(x/log^{A+3}x).
*Step 3 (short relations).* Λ_r := {c ∈ ℤ^k : ∏ s_i^{2c_i} ≡ 1 (mod r)}; for the surviving r, ℤ^k/Λ_r ≅ (F_r^*)²,
det Λ_r = (r−1)/2. If λ₁(Λ_r) ≤ B (sup-norm) then r | N_{2c} for some 0 < |c|_∞ ≤ B, and as above
#{r : λ₁ ≤ B} ≤ (2B+1)^k(2B log P + 1) ≤ (3B)^{k+1} log P. Take B := ⌊x^{1/(k+1)}/(3 log^{(A+5)/(k+1)}x)⌋ (≥ 1 for
large x, since log x/(k+1) → ∞): this is ≤ x log P/log^{A+5}x = o(x/log^{A+3}x). So some sieved r has
Γ_r = (F_r^*)² and λ₁(Λ_r) > B.
*Step 4 (covering, Minkowski II).* λ₁⋯λ_k ≤ det Λ_r < x gives λ_k < x/B^{k−1}, and every class of ℤ^k/Λ_r has a
representative of sup-norm ≤ Σλ_i ≤ kλ_k =: L (EXPONENT_CAP Thm 3.2, step "Covering"). As there (R209 repair m9, R210 repair m9), let a ∈ ℤ^k with |a|_∞ ≤ L
represent the class of (−n/4)·∏ s_i^{−2L} in ℤ^k/Λ_r ≅ (F_r^*)² (i.e. ∏ s_i^{2a_i} ≡ (−n/4)∏ s_i^{−2L} mod r); then
Q := ∏ s_i^{a_i+L} has exponents in [0, 2L] and satisfies Q² ≡ −n/4 (mod r); UNIT_ORBIT Prop 2.1 gives an ES^{(y)} solution
(s_i | (r+1)/4 | y, Type II shape at every prime of n) with overflow exponents ≤ v_s(Q) ≤ 2L. Finally
2L ≤ 2k·x/B^{k−1} ≤ 2k·6^{k}·log^{A+5}x·x^{2/(k+1)} (using B ≥ x^{1/(k+1)}/(6 log^{(A+5)/(k+1)}x)) =
x^{(2+o(1))log₃x/(A log₂x)}, because 6^k log^{A+5}x =
exp(O(A log₂x)) is of lower order; and x/8 ≤ y = n(r+1)/4 ≤ nx, so log₃y/log₂y = (1 + o(1))log₃x/log₂x and for
x ≥ x₀(n, A, η) the bound is ≤ y^{(2+η)log₃y/(A log₂y)}. ∎
*Remarks.* (1) The only change from Thm 3.2 is that S grows with x, which Bombieri–Vinogradov tolerates up to
P = (log x)^A because its error term saves an arbitrary power of log (not more: Siegel–Walfisz range). (2) Allowing
P up to exp(c√log x) (Gallagher's prime number theorem for moduli without exceptional zero, provided the exceptional
modulus, if any, does not divide 4 rad(n) — the choice of S cannot avoid that case, R210 repair m13) should give e = exp(O(√(log y)·log₂y)); not carried out (Assessment). (3) The
covering lower bound (EXPONENT_CAP Prop 3.1(c)) is e ≥ (log y)^{1−o(1)} for any covering argument; the gap
(log y)^{1−o(1)} ↔ y^{o(1)} is the Dictionary 3.3(c) discrete-log problem, and below it every bounded cap is a
pure hitting problem for the arguments analysed (§4: θ_e = 1/(2e+2) > 0).

## 6. The phase diagram (cells, status, the wall that bounds each)

Columns: k-direction (fixed k: finite? — a statement about SLICES, not about the cell), Q₁-direction (fixed Q₁:
finite? — always yes, EXPONENT_CAP Thm 2.1), θ_min = the infimum of log M/log N over the Prop 4.1 face (bounded λ)
for capped rows, the prime-face modulus for the proved rows (R209 m7, R210 m6), and the status.
`  variant (mute condition on den z = Q₁²)      k-slices     θ_min        status`
`  ES^□       none                              k=1 infinite‡ 0 (mod 4)    PROVED (Dirichlet; SYNTHESIS_SPARKS2 2.2; Cor 3.2)`
`  ES^{(S)}   rad Q₁ ⊆ S fixed, |S| ≥ 4          k=1 infinite† 0            PROVED (UNIT_ORBIT 2.4; k = 1: Prop 3.1)`
`  ES^{(y)}   rad Q₁ | y                         k=1 infinite† 0 (S fixed)  PROVED (sieve; FROBENIUS 4.2, Prop 3.1)`
`  ES^{(y,e(y))} e ≤ y^{(2+η)log₃y/(A log₂y)}      —            → 0          PROVED, family form (Thm 5.1; was y^δ)`
`  ES^{(y,polylog)}  cap (log y)^C                —            → 0          OPEN: covering threshold; Dictionary 3.3(c)`
`  ES^{(y,e)}, e ≥ 2 fixed                        no wall seen ≤1/(2e)*     OPEN: hitting below θ = 1/4 (§3 EVIDENCE)`
`  ES^{[2]} = den z | y²; ES^{(y,1)} (e = 1)     each FINITE  1/4          OPEN: doubly walled (Thm 2.1) but NOT a finite`
`                                                                         search: infinite union of finite slices, Pell-`
`                                                                         orbit lottery (GROWING_MUTE, MARKOFF 6.1); R200 M1 stands`
`  ES         Q₁ = 1                             finite       1/2          OPEN (finite search, g ≤ 2n(n+1), B2/B3)`
(† for odd non-square n with 3 ∤ n, ineffective (R209 m4/m12, R210 m4); ‡ odd non-square n. * θ of the pure-power sub-family of Prop 4.1, 1/(2e+2) for bounded λ.) Reading of the table (Assessment, every
entry referenced): every PROVED cell has θ → 0 (certifying modulus fixed, or ≤ polylog of the number it divides),
which is what lets a Kummer/Dirichlet field fixed in advance decide firing in the arguments analysed; θ → 0 is not
sufficient (the polylog-cap row is open). For the arguments analysed here (fixed-field firing, covering of the
per-certificate box) every bounded cap is a hitting problem at θ > 0 — this is a limitation of those arguments, not
a classification theorem. The self-mute cap e ≤ 1 adds the k-wall (both slicings finite, the cell still unbounded — R209 m3, R210 m2), ES adds
Q₁ = 1 (one slice, hence a genuinely finite search).

**T1 (the brief's question: is ES^{(y,1)} T1-bearing?).** Yes, in the same sense as ES: (a) no ES^{(y,e)} solution
for any e ≤ ∞ at n = m² has Type I/II shape at every prime of m (FROBENIUS_FIRING Thm 4.2(b): an ES^{(y,e)} solution
is an ES^{(S′)} solution with S′ its mute primes; UNIT_ORBIT Cor 1.2), in particular no shot solution (sum of two
coprime squares, §1 of GROWING_MUTE); (b) as a statement it nevertheless holds at m² whenever it holds at a prime
p | m with mute primes prime to m (scaling 4/(pt) = 1/(tx) + 1/(ty) + 1/(tz)). So every cell of the table has the
T1 of ES (checked: all T1 controls in §2–§3 and pd_k1s are empty), and (Assessment, R210 repair m12) any proof of a
bounded-cap cell is expected to use a non-square input such as (n/r) = −1. Covering by finitely many SHOT
IDENTITIES is excluded for every cell (B1; PROVED, elementary; R209 m10, R210 m10/m11 repairs — this mirrors the
classical Mordell obstruction to identities on quadratic-residue classes, and the restriction to non-residues in
the first version was unused): let r ≡ 1 (mod 4) be prime, u ANY unit class mod r, and x(u) ∈ Ẑ the point with x_ℓ = 1 (ℓ ≠ r), x_r = u. A shot class {n : g | n + 4Q²} (g ≡ 3 mod 4) of ANY
variant down to ES^□ cannot contain x(u): writing g = r^a g′, g′ | 1 + 4Q² forces g′ ≡ 1 (mod 4), and r^a ≡ 1, so
g ≡ 1 (mod 4). Finitely many classes therefore miss a whole neighbourhood {n ≡ x(u) mod M} of x(u), which contains
infinitely many primes (Dirichlet): **for every prime r ≡ 1 (mod 4) and every class u ≢ 0 mod r, no finite set of shot
identities of any of these variants covers the primes p ≡ u (mod r)** (more generally, the same holds for every
reduced class modulo any modulus all of whose prime factors are ≡ 1 (mod 4); R210 `review_pd2_b1.py` found
uncovered primes in all classes mod 5 and 13 for the shot classes with g ≤ 60). The proved cells escape this only by using
arbitrarily large primes (non-covering proofs).

**Where the single-n requirement bites (the brief's sieve question; Assessment — R209 repair m12).** Not at B6: n is fixed and r (or (k, λ)) is
the summation variable, exactly as in the proved ES^{(y)}. It bites at the per-certificate box: after switching
(sum over the shot first) the count is Σ_{k,λ} #{g | N_e(k, λ) : g ≡ −1 (mod 4kλ)} with N_e = n(2k(4kλ)^e)² + 1
(Prop 4.1): divisors of ONE number per parameter in a class whose modulus is a parameter of that number. BFI /
Fouvry / Drappeau-type estimates (Titchmarsh divisor problem, primes in a fixed class −1 mod q averaged over
well-factorable q ≤ x^{1/2+δ}) equidistribute MANY primes r in classes of a modulus q chosen independently of r; here,
for the modulus q = 4Q₀ of a shot, at most ω(n + 4Q²) primes r ≡ −1 (mod q) qualify — the joint condition
"r ≡ −1 (mod 4Q₀) and r | n + 4Q₀²Q₁²" has the shot parameter on both sides, so its expected count per q is
≍ τ(N)/q, invisible to any level-of-distribution statement (whose main terms are ≍ x/φ(q)). Chen-type switching
only moves between the three faces (prime g, cofactor D, nX² + 1) — each a one-number-per-parameter divisor problem
with θ = 1/(2e+2). The Pell-orbit freedom of S_{n,D} (no archimedean wall once B = Q₁ is free, (J)36) multiplies
ONE point into infinitely many but does not create the first (MARKOFF 6.1(c): class-group layer) and does not keep
Q₁ squarefree (R201 M3), so it serves ES^{[2]} only, and only after existence.
**Exact conditional form of the class layer (PROVED, from MARKOFF Thm 4.1 + Gauss's genus theory).** If for some
(λ, D) with D admissible in the sense of MARKOFF Lemma 3.1 (D ≡ 3 (mod 4), gcd(D, n) = 1, (−n/p) = 1 for p | D),
λ²D² − n > 0 and not a square, and genus-admissible (MARKOFF §6 local layer: −D primitively represented by the
principal genus of discriminant 16(λ²D² − n)), the form class group of that discriminant (primitive forms, proper
equivalence) has one class per genus, then ES^{[2]}(n) holds (R209 repair m11). (One class per genus makes "represented by the principal genus" equal "represented by the principal form".)
This trades the problem for a Gauss/Cohen–Lenstra statement about the family 16(λ²D² − n): open, not a standard
hypothesis.

## 7. Verdict (O204 checkpoint 1, after R209/R210 repairs)

1. **Normal form (Prop 1.1, PROVED).** Shots ⟺ k(4ab − n) = b + aQ₁²: the overflow is a Q₁²-weight on a in ES's
   Type II equation (d = 1 slice); ES: Q₁ = 1; ES^{[2]}: Q₁ | a; ES^{(y)}: rad Q₁ | a. D-face: ES^{[2]} ⟺
   4λtb − n | b + λt³.
2. **Double wall (Thm 2.1, PROVED, sharp).** Under the self-mute cap Q₁ | Q₀ (ES^{[2]} ⊇ ES^{(y,1)}): Q₁ ≤
   (16k³n + 1)/(4k − 1), attained exactly (all n ≡ 2 mod 3 at k = 1). With Q₁ > (n+1)/2: √(Q₁/6n) ≤ k < Q₁²/2. Every
   fixed-k and fixed-Q₁ slice is finite; solutions with Q₁ > (n+1)/2 live in a band of slopes ½…2 in log coordinates.
   **This does NOT make ES^{(y,1)} or ES^{[2]} a finite search**: the band is unbounded and carries infinite Pell
   orbits; R200 M1 (bounded e, growing S: open) stands for e = 1 (R209 repair m3, R210 repair m2).
3. **k-direction dichotomy (Cor 3.2, Prop 3.1, PROVED).** The k = 1 slice is infinite for ES^□ and ES^{(y)}
   (non-square n; for ES^{(y)} also 3 ∤ n, ineffective; ES^□ proof R209 M1), finite for ES^{[2]}/ES^{(y,1)}/ES. EVIDENCE: e = 2 has no visible
   wall at k = 1 (sparse hits up to Q₁ = 2·10⁵); one mute prime (S = {3}) gives k = 1 shots for all primes < 10⁶.
4. **One axis for all caps (Prop 4.1, PROVED).** ES^{(y,e)} ⟸ n(2k(4kλ)^e)² + 1 has a divisor ≡ −1 (mod 4kλ) with
   (g+1)/(4kλ) squarefree (exact for e ≤ 1; a sufficient pure-power sub-family for e ≥ 2): modulus exponent
   θ_min = 1/(2e+2) (infimum over the face, along bounded λ; parametrisation-dependent). ES: θ_0 = ½ (Lenstra); the
   e = 1 face reaches down to θ = ¼, the N^{1/4} threshold of Lenstra (1984) / CHN (2008), with no margin; e ≥ 2
   below it; every proved cell has θ → 0 on its own (prime) face (R209 m6/m7, R210 m5/m6 repairs).
5. **Proved side pushed (Thm 5.1, PROVED rel. BV + linear sieve; ineffective, astronomically late onset).** For every
   A, η > 0 and n, for all x ≥ x₀(n, A, η) there is an ES^{(y,e)}(n) solution with x/8 ≤ y ≤ nx and
   e ≤ y^{(2+η)log₃y/(A log₂y)} (previously y^δ) (R209 repair M2, R210 repair m7).
6. **Boundary (Assessment with PROVED pieces).** For the arguments analysed (firing decided in a field or
   progression fixed in advance; covering of the per-certificate box), bounded e is out of reach: the per-certificate
   box is g^{o(1)} (EXPONENT_CAP Prop 3.1) and the pure-power sub-family has θ > 0; this does not exclude other
   (deterministic) methods. The k-wall makes e ≤ 1 an (infinite) union of finite slices in both directions — not a finite
   search; finitely many fixed shot classes never cover any reduced class mod a prime r ≡ 1 (mod 4) (§6, B1). The polylog cap is the covering threshold (Dictionary 3.3(c)); between y^{o(1)} (proved) and
   (log y)^{1−o(1)} (necessary for covering) nothing is known.
Not a proof of ES or of any bounded-cap variant; no infinite case of ES is claimed.
