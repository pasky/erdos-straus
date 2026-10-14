# PHASE_DIAGRAM — the (k, Q₁) phase diagram between ES^□ / ES^{(y)} and ES (task O204, wave Y-a)

Status: in progress (O204). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP.md (O200: Prop 1.2, Prop 1.3 duality D·g = 4k²n + Q₁², Thm 2.1, Prop 3.1, Thm 3.2; R200 M1),
GROWING_MUTE.md (O201: (A, B) form, V_n), MARKOFF_ES.md (O202), COMPOSITION_ES.md (O203), FROBENIUS_FIRING §4,
UNIT_ORBIT_ES §2, SYNTHESIS_SPARKS2 §2 (ES^□). Scripts `scripts/pd_*`.

Notation (as in GROWING_MUTE, widened shot family): n > 1 odd; shot datum (Q, g): Q ≥ 1, gcd(Q, n) = 1, g ≡ 3 (mod 4),
g | n + 4Q²; K := (g+1)/4, Q₀ := gcd(Q, K), overflow Q₁ := Q/Q₀ (odd), k := K/Q₀; den(z) = Q₁², y = n(g+1)/4 = nQ₀k.
Variants: ES ⇒ ES^{(y,1)} ⇒ ES^{[2]} (Q₁ | Q₀, "den z | y²") ⇒ ES^{(y)} (rad Q₁ | Q₀k); ES^□: no mute condition.

## 0. Iteration log

(Y1) Construction attempt as briefed (sieve r ≡ −1 mod 4P, P ≈ r^{1/4}, Q₁ | P). Screen: for each r the admissible
set {Q : Q | K·rad K} has size ≤ τ(K)2^{ω(K)} = r^{o(1)}, so a single-n statement needs a *hit*; switching the
order of summation turns the hit count into Σ_Q #{r | n + 4Q² : r ≡ −1 (mod 4Q₀)}, i.e. divisors of n + 4Q² in a
class of modulus 4Q₀ ≥ 4√Q ≈ (n + 4Q²)^{1/4} — the Lenstra/Coppersmith threshold (EXPONENT_CAP Prop 4.1).
Hypothesis to violate: "the per-r box is r^{o(1)}". Bounded cap cannot violate it (Prop 3.1), so look for
(a) a deterministic mechanism (Pell / genus / units: T1-exact facts that hold exactly at non-squares), or
(b) a different slicing in which the modulus is fixed.
(Y2) Exact re-slicing (§1): ES^{[2]} ⟺ ∃ (t, j): n t² + 4 j² has a divisor ≡ −n (mod 4tj) (t = overflow), the
"D-face" of the duality; ES is t = 1. The λ = 1 sub-family is the quartic family "n + 4t⁴ has a divisor ≡ −1
(mod 4t)", and its j = 1 member is the FIXED-modulus test "64 + n³ has a divisor ≡ 3 (mod 4)" (e.g. n = 13:
64 + 13³ = 7·17·19, D = 7, t = 5, g = 359 | 13 + 4·25² → an ES^{(y,1)} solution of 4/13 with overflow 5). Fixed modulus only for one number per j: no infinite fixed-modulus family.
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
**ES^{[2]} shot ⟺ m := 4λtb − n > 0 divides b + λt³** ⟺ m | nt² + 4b² (as 4b(b + λt³) ≡ nt² + 4b² mod m and
gcd(m, 2bn) = 1). ES is t = 1: 4λb − n | λ + b. The quartic family of (Y2) is λ = 1.

## 2. The double wall of ES^{[2]}

**Theorem 2.1 (PROVED).** Let (Q, g) be an ES^{[2]} shot of odd n > 1 (overflow Q₁ odd, Q₁ | Q₀), k = (g+1)/(4Q₀).
(a) (**k-wall, new**) Q₁ ≤ W(k) := (16k³n + 1)/(4k − 1) = 4k²n + kn + (kn + 1)/(4k − 1) ≤ 6k²n.
(b) (Q₁-wall) g ≤ 2nQ₁²(n + Q₁²) (EXPONENT_CAP Thm 2.1); moreover if Q₁ > (n+1)/2 then k < Q₁²/2.
Hence every ES^{[2]} shot with Q₁ > (n+1)/2 lies in the band **√(Q₁/(6n)) ≤ k < Q₁²/2**: both
coordinates must grow together, every horizontal (fixed Q₁) and every vertical (fixed k) slice is a finite search.
*Proof.* (a) Prop 1.3(b): Dg = 4k²n + Q₁² with D ≥ 1. As Q₁ | Q₀, g = 4kQ₀ − 1 ≡ −1 (mod 4kQ₁), so g ≥ 4kQ₁ − 1
and, reducing Dg mod Q₁, D + 4k²n ≡ 0 (mod Q₁); hence D ≥ Q₁ − 4k²n. If Q₁ ≤ 4k²n, (a) holds because
(16k³n + 1) − 4k²n(4k − 1) = 4k²n + 1 > 0. Otherwise 4k²n + Q₁² = Dg ≥ (Q₁ − 4k²n)(4kQ₁ − 1), which expands to
(4k − 1)Q₁² ≤ (16k³n + 1)Q₁. (b) In the proof of EXPONENT_CAP Thm 2.1, the case kj' ≥ 2Q₁² gives Q₀ ≤ (n+1)/2, and
Q₁ | Q₀ then gives Q₁ ≤ (n+1)/2; so Q₁ > (n+1)/2 forces the case kj' < 2Q₁² with j' ≥ 4, i.e. k < Q₁²/2. ∎
*Sharpness.* (a) is attained exactly: (n, k, Q₁) = (3, 2, 55), g = 439 (W(2) = 385/7 = 55), and for EVERY
n ≡ 2 (mod 3) at k = 1 by the family Q₁ = W(1) = (16n + 1)/3, g = 4Q₁ − 1 = (64n + 1)/3, D = (4n + 1)/3, Q = Q₁²
(check: Dg = (4n+1)(64n+1)/9 = 4n + Q₁²; D ≡ 3 (mod 4) iff n ≡ 2 (mod 3); gcd(Q₁, n) = 1), an ES^{[2]} shot
(even ES^{(y,1)} when 16n + 1 is squarefree) with overflow ≈ 5.3n. (Also Q₁ = 4n + 3, D = 3 for n ≡ 2 (mod 3).) (b): k/Q₁² up to 0.436 is observed ((n, k, Q₁) = (29, 126, 17), g = 8567).
*Check (`scripts/pd_band.py 101 6 1.3`, `scripts/pd_band2.py 41 41`; exact rationals):* all 360 shots with odd
n ≤ 101, k ≤ 6, Q₁ ≤ 1.3·W(k), and all 36 shots with n ≤ 41, (n+1)/2 < Q₁ ≤ 41, k ≤ 2Q₁²: identity (1.1), solution,
den z = Q₁² (when gcd(Q₀, n) = 1), walls (a), (b) hold; max Q₁/W(k) = 1.000, max k/Q₁² = 0.436.
*Reading.* Without the self-mute cap the k = 1 slice is infinite and elementary (ES^□: "4n + Q₁² has a divisor
≡ 3 (mod 4)", Dirichlet). The cap Q₁ | Q₀ converts the modulus 4 into 4Q₁ and the slice into a finite search: the
k-wall is created exactly by the self-mute cap, as the Q₁-wall of EXPONENT_CAP is created by fixing Q₁.

## 3. One slice, the whole ladder: k = 1

The k = 1 slice is where the duality plane meets ES^□. By Prop 1.3's converse with k = 1, k = 1 shots of overflow
Q₁ (odd, prime to n) are exactly the divisors g ≡ 3 (mod 4) of **4n + Q₁²** (cofactor D ≡ 3 (mod 4) automatically;
Q₀ = (g+1)/4, Q = Q₀Q₁; we also need gcd(Q₀, n) = 1). The mute rungs become congruences on g alone:
`  rung      condition on (Q₁, g)                                    modulus      status (k = 1 slice)`
`  ES^□      none                                                     4            PROVED (one Dirichlet prime)`
`  ES^{(y)}  Q₁ ∈ ⟨S⟩ (S fixed, |S| ≥ 4), g ≡ −1 (mod 4·rad Q₁)      4·∏S fixed   PROVED (FROBENIUS_FIRING Thm 4.2 sieve)`
`  ES^{(y,2)} v_ℓ(Q₁) ≤ 2, g ≡ −1 (mod 4·rad Q₁)                     ≥ 4√Q₁       OPEN; no wall (EVIDENCE below)`
`  ES^{(y,1)}, ES^{[2]}  g ≡ −1 (mod 4Q₁)                             4Q₁          FINITE: Q₁ ≤ (16n+1)/3 (Thm 2.1(a))`
`  ES        Q₁ = 1                                                  4            one number, 4n + 1`
**Proposition 3.1 (PROVED).** (a) For every odd non-square n > 1 with gcd(n, 15) = 1, the k = 1 slice of ES^{(y)}
is non-empty: there are Q₁ ∈ ⟨S⟩ (S any four odd primes prime to n) and a prime g ≡ −1 (mod 4∏S) with g | 4n + Q₁².
(b) For ES^{(y,1)} and ES^{[2]} the k = 1 slice is contained in Q₁ ≤ (16n + 1)/3, and for n ≡ 2 (mod 3) this
bound is attained.
*Proof.* (a) Follow FROBENIUS_FIRING Thm 4.2(a) / UNIT_ORBIT Thm 2.4(a): M := 4 rad(n)∏S, a ≡ 3 (mod 4),
a ≡ −1 (mod s) for s ∈ S, and for ℓ | n residues a_ℓ chosen so that every prime r ≡ a (mod M) has (n/r) = −1
(by reciprocity this is a condition on the Jacobi symbol (r/n), adjusted at one prime ℓ₀ | n of odd exponent; such
ℓ₀ exists since n is not a square, n ≡ 3 (mod 4) included). Additionally take a_ℓ ∉ {0, 1, −1} (mod ℓ): possible for
every ℓ ≥ 7 with either prescribed quadratic character ((ℓ − 3)/2 ≥ 2 residues and non-residues ∉ {0, ±1}); at
ℓ = 3, 5 it is not, hence gcd(n, 15) = 1. Lemma 2.2 of UNIT_ORBIT only needs a ≢ 1 (mod ℓ), so the sieve of Thm 4.2
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
* e = 2, non-squarefree Q₁ (beyond ES^{(y,1)}): hits in every dyadic range up to the search limit, 1–7 per octave,
  max Q₁ = 185 761, 120 409, 152 881, 194 271, 165 649, 192 721 for n = 13, 17, 29, 37, 97, 101 — no sign of a wall,
  and n = 13, 37 (no e ≤ 1 shot at k = 1) have e = 2 shots. T1: n = 9, 25: no shot on any rung.
*Reading (Assessment).* Inside the single slice k = 1 the cap ladder shows every phase: fixed modulus (proved,
Dirichlet/sieve), moving modulus ≥ 4√Q₁ ≈ (4n + Q₁²)^{1/4} with no archimedean bound (e = 2: an infinite lottery
at the Lenstra–Coppersmith threshold, roughly constant hit-rate per octave, i.e. a log-divergent lottery), moving
modulus 4Q₁ ≈ (4n + Q₁²)^{1/2} (e ≤ 1: finite search, the k-wall), and the single number of ES. So the transition
"infinite lottery → finite search" happens between e = 2 and e = 1, and the transition "proved → lottery" between
e = ∞ (fixed S) and every bounded e.
*Corollary 3.2 (k-direction dichotomy; PROVED).* Every fixed-Q₁ slice of every variant is finite (EXPONENT_CAP
Thm 2.1). Every fixed-k slice of ES^{[2]} ⊇ ES^{(y,1)} ⊇ ES is finite (Thm 2.1(a)). The k = 1 slice of ES^□ and,
for gcd(n, 15) = 1, of ES^{(y)} (fixed S, |S| ≥ 4) is INFINITE: the sieve of Prop 3.1(a) (resp. Dirichlet) gives
infinitely many distinct primes g, and g ≤ 2nQ₁²(n + Q₁²) forces Q₁ → ∞. So the k-wall exists exactly at relative
cap ≤ 1 among these variants; for bounded absolute cap e ≥ 2 its absence is EVIDENCE only (§3 table).

## 4. One family for all caps: "nX² + 1 has a divisor ≡ −1 (mod M)", M ≈ N^{1/(2e+2)}

**Proposition 4.1 (PROVED).** Let n be odd, e ≥ 0, k, λ, R ≥ 1 with R odd, gcd(R, 2kn) = 1, M := 4kλ, g := MR − 1,
X_e := 2k·M^e, N_e := nX_e² + 1. Then g | 4k²n + R^{2e} ⟺ g | N_e, and in that case (Q, g) with Q = λR^{e+1} is a
shot with Q₀ = λR, overflow exactly R^e, den z = R^{2e} (if gcd(λR, n) = 1). Consequently
`  ES^{(y,e)}(n) ⟸ ∃ k, λ ≥ 1: N_e = n(2k(4kλ)^e)² + 1 has a divisor g ≡ −1 (mod 4kλ) with R = (g+1)/(4kλ)`
`                   odd, squarefree, prime to kn,`
and for e = 0 this is exactly ES's shot family (λ = 1: "4k²n + 1 has a divisor ≡ −1 (mod 4k)"); for e = 1 it is
the general ES^{[2]} shot (GROWING_MUTE (A, B) form with A = 2k, B = R, Q₀ = λB) with X₁ = 8k²λ.
*Proof.* MR ≡ 1 (mod g) and gcd(M, g) = 1, so multiplying 4k²n + R^{2e} by M^{2e} gives 4k²nM^{2e} + 1 = N_e
(mod g). Then D := (4k²n + R^{2e})/g ≡ −R^{2e} (mod 4k) (as g ≡ −1), and Prop 1.3's converse with (k, Q₁ = R^e)
gives Q₀ = (g+1)/(4k) = λR and Q = Q₀Q₁ = λR^{e+1}; gcd(Q, Q₀k) = λR·gcd(R^e, k) = λR, so the overflow is R^e. ∎
*Check (`scripts/pd_theta.py 201 8 300`):* for odd n ≤ 201, k, λ ≤ 8, e ≤ 2: 368 / 710 / 1276 shots (e = 0/1/2) found
via N_e, each an exact solution with den z = R^{2e}; the equivalence g | 4k²n + R^{2e} ⟺ g | N_e checked on
2 802 432 (n, e, k, λ, R) with e ≤ 3, R ≤ 300.
*The modulus exponent.* log M/log N_e → θ_e := 1/(2e + 2) for bounded λ (exactly:
M^{e+1} = 2λX_e, so M = (2λX_e)^{1/(e+1)} ≈ (2λ)^{1/(e+1)}(N_e/n)^{1/(2e+2)}):
`  e = 0 (ES):            θ = 1/2   — Lenstra's regime (≤ 11 divisors in a class mod > N^{1/3}; bounded count)`
`  e = 1 (ES^{(y,1)}, ES^{[2]}): θ = 1/4 — exactly the Coppersmith–Howgrave-Graham–Nagaraj threshold`
`  e = 2:                 θ = 1/6   — below CHN's range: no O(1) bound on divisors of N in one class`
`  e = ∞, S fixed (ES^{(y)}): M fixed (θ → 0) — Kummer/Chebotarev firing, sieve-provable (Thm 4.2)`
`  no mute (ES^□):        M = 4                 — Dirichlet`
*Reading.* This is the brief's phase diagram on one axis. The two archimedean facts of §2–§3 are its shadows:
θ ≥ 1/4 (e ≤ 1) is where the cofactor D = N/g is smaller than the modulus, which is what powers the k-wall
(proof of Thm 2.1(a): D < Q₁ forces D = Q₁ − 4k²n) — exactly CHN's "at most O(1) divisors in a class above N^{1/4}";
θ < 1/4 is where the k = 1 slice becomes an infinite lottery (§3 EVIDENCE). And θ → 0 is the only regime with a
proof. The brief's hook (R200 M1: P ≈ r^{1/4}) is the e = 1 line read from the prime-g side.

## 5. Pushing the proved side down: ES^{(y)} with a sub-polynomial exponent cap

EXPONENT_CAP Thm 3.2 gives cap e ≤ y^δ with a FIXED set S of k ≥ 2/δ + 1 primes; its Remark (2) (Assessment) says
letting k grow is limited by the sieve modulus. Making that remark a theorem:

**Theorem 5.1 (ES^{(y,e)} with e = y^{o(1)}; PROVED relative to Bombieri–Vinogradov and Iwaniec's linear sieve, as
UNIT_ORBIT Lemma 2.2; ineffective).** For every A ≥ 1 and every odd n > 1, ES^{(y,e)}(n) has a solution with
`  e ≤ y^{(2 + o(1))·log₃y / (A·log₂y)}`   (log₂ = log log, log₃ = log log log; o(1) as y → ∞ for fixed n, A),
of Type II shape at every prime of n when n is not a square. In particular for every ε > 0 there is a solution with
e ≤ y^{ε·log₃ y/log₂ y}.
*Proof.* n ≡ 3 (mod 4) is ES with Q = 1; squares follow from a non-square divisor by scaling (FROBENIUS_FIRING
Thm 4.2(c); the bound is monotone in y). Let n ≡ 1 (mod 4) be a non-square, x large, and S = {s₁ < … < s_k} the
first k odd primes not dividing n with P := ∏S ≤ (log x)^A maximal; by the prime number theorem k log k ~ A log₂x,
so k ~ A log₂x/log₃x. M := 4 rad(n)P ≤ 4n(log x)^A; the class a mod M is that of Thm 4.2(a).
*Step 1 (sieve, uniform in M).* Sift 𝒜 = {(r−1)/2 : x/2 < r ≤ x, r ≡ a (M)} by primes ℓ ∤ M, ℓ < z = x^{1/4−ε},
level D = x^{1/2}/(M log^{β}x) with β = β(A) the Bombieri–Vinogradov exponent for saving log^{2A+10}. Remainders:
distinct d give distinct moduli Md ≤ x^{1/2}/log^{β}x, so Σ_d |r_d| ≤ Σ_{q ≤ x^{1/2}/log^{β}x} max_a |E(x; q, a)|
≪_A x/log^{2A+10}x (Bombieri–Vinogradov, max form, for π(x) − π(x/2); uniform in M). Main term X·V(z)·(f(s) − o(1)) with X ≍ x/(φ(M) log x), V(z) ≫ 1/log z (the density 1/(ℓ−1) on
ℓ ∤ M, dimension 1, constants absolute; ∏_{ℓ|M}(1 − 1/(ℓ−1))^{−1} only helps), s = log D/log z → 2/(1 − 4ε) > 2.
So ≫ x/(φ(M) log²x) ≥ x/log^{A+3}x primes r ∈ (x/2, x] in the class with every prime factor of (r−1)/2 ≥ z.
*Step 2 (index).* As in Thm 4.2, Γ_r := ⟨S mod r⟩ ⊆ (F_r^*)², and a nontrivial index is ≥ z, so |Γ_r| ≤ x^{3/4+ε}.
Lemma 2.3's count made explicit: if |Γ_r| ≤ Y, the (B'+1)^k > Y products ∏ s_i^{a_i} (0 ≤ a_i ≤ B' := ⌈Y^{1/k}⌉)
collide, so r | N_c := ∏_{c_i>0} s_i^{c_i} − ∏_{c_i<0} s_i^{−c_i} ≠ 0 for some 0 < |c|_∞ ≤ B'; N_c has
≤ B' log P/log(x/2) + 1 prime factors > x/2. Hence #{r ∈ (x/2, x] : |Γ_r| ≤ Y} ≤ (2B'+1)^k(B' log P + 1)
≤ 6^k·Y^{1+1/k}·2 log P, which for Y = x^{3/4+ε}, k ≥ 4 is ≤ x^{15/16+2ε}(log x)^{O(A)} = o(x/log^{A+3}x).
*Step 3 (short relations).* Λ_r := {c ∈ ℤ^k : ∏ s_i^{2c_i} ≡ 1 (mod r)}; for the surviving r, ℤ^k/Λ_r ≅ (F_r^*)²,
det Λ_r = (r−1)/2. If λ₁(Λ_r) ≤ B (sup-norm) then r | N_{2c} for some 0 < |c|_∞ ≤ B, and as above
#{r : λ₁ ≤ B} ≤ (2B+1)^k(2B log P + 1) ≤ (3B)^{k+1} log P. Take B := ⌊x^{1/(k+1)}/(3 log^{(A+5)/(k+1)}x)⌋ (≥ 1 for
large x, since log x/(k+1) → ∞): this is ≤ x log P/log^{A+5}x = o(x/log^{A+3}x). So some sieved r has
Γ_r = (F_r^*)² and λ₁(Λ_r) > B.
*Step 4 (covering, Minkowski II).* λ₁⋯λ_k ≤ det Λ_r < x gives λ_k < x/B^{k−1}, and every class of ℤ^k/Λ_r has a
representative of sup-norm ≤ Σλ_i ≤ kλ_k =: L (EXPONENT_CAP Thm 3.2, step "Covering"). As there, Q := ∏ s_i^{a_i+L}
with exponents in [0, 2L] satisfies Q² ≡ −n/4 (mod r); UNIT_ORBIT Prop 2.1 gives an ES^{(y)} solution
(s_i | (r+1)/4 | y, Type II shape at every prime of n) with overflow exponents ≤ v_s(Q) ≤ 2L. Finally
2L ≤ 2k·x/B^{k−1} ≤ 2k·6^{k}·log^{A+5}x·x^{2/(k+1)} (using B ≥ x^{1/(k+1)}/(6 log^{(A+5)/(k+1)}x)) =
x^{(2+o(1))log₃x/(A log₂x)}, because 6^k log^{A+5}x =
exp(O(A log₂x)) is of lower order; and y = n(r+1)/4 ≥ x/8. ∎
*Remarks.* (1) The only change from Thm 3.2 is that S grows with x, which Bombieri–Vinogradov tolerates up to
P = (log x)^A because its error term saves an arbitrary power of log (not more: Siegel–Walfisz range). (2) Allowing
P up to exp(c√log x) (Gallagher's prime number theorem for moduli without exceptional zero, the exceptional
conductor avoided by the choice of S) should give e = exp(O(√(log y)·log₂y)); not carried out (Assessment). (3) The
covering lower bound (EXPONENT_CAP Prop 3.1(c)) is e ≥ (log y)^{1−o(1)} for any covering argument; the gap
(log y)^{1−o(1)} ↔ y^{o(1)} is the Dictionary 3.3(c) discrete-log problem, and below it every bounded cap is a
pure hitting problem (§4: θ = 1/(2e+2) > 0).
