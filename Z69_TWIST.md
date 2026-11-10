# Z69_TWIST — pushing the surviving twists of the z69 ideation lanes (WORK IN PROGRESS)

**ES is OPEN. Nothing here proves or disproves it.** Status: in progress (checkpoint 1).
Sources: `Z69_IDEAB.md` §1 (branch `side-agent/z69-ideab`), `data/z69/xreview/REVIEW_IDEAB.md` table A
(branch `side-agent/z69-xrev-ideab`), `Z69_IDEAA.md` + `data/z69/xreview/REVIEW_IDEAA.md` "Possibly-premature
dismissals". Scripts `scripts/z69_twist_*`, data `data/z69/twist/`. Labels: PROVED / CONDITIONAL / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment.

Notation (IDEAB §1.0, p ≡ 1 (4) prime, all letters positive integers):
* **Type II**: 4abd = p + e, ce = a + b (⟺ pc = 4abcd − a − b). **Type I**: 4abd = pe + 1, ce = a + b.
  In both, e ≡ 3 (mod 4).
* **K3 form of Type I**: f := 4acd − p > 0 divides 4a²d + 1 (cofactor e).
* **(★)** = Type II with c = 1: p = 4uBC − u − B. **Words**: (x, y, z) with xyz − x − z = n; U₇(n) ⟺ a word with
  8 | xy; (★) ⟺ a word with 4 | y.

## 0. Mandatory falsifier table (checkpoint-1 version; restated at the end)

Checkpoint 1 holds only *triage* objects (kill lemmas and census tests); the table for the pushed survivors is in §4.

| screen | behaviour of the triage results | label |
|---|---|---|
| **F1 odd squares** | Lemma V (§2.1) and Lemma T10 (§2.2) are sterility statements valid for every n ≡ 1 (4) (V) / every prime p ≡ 1 (4) (T10; the Jacobi-symbol version holds for all odd n); they assert *absence* of solutions, so they cannot contradict R(m²) = 0. No positivity claim is made at checkpoint 1. | PROVED |
| **F2 numerator 8 / C-even** | No positivity claim. The word census (§3, I5) separates 4 ∣ y, 8 ∣ y, 8 ∣ xy; it reproduces zeros of the 8 ∣ y line and none of the 8 ∣ xy line at primes ≤ 10⁶. | CERTIFIED (census) |
| **F3 composites** | Lemma V needs no primality (it holds for all odd M = (n+1)/2). The parity lemma P (§3, I5: total word count odd) holds at primes *and* at 105 and at 9, where U₇ fails — this is exactly why it cannot force anything (§3). | PROVED |
| **F4 known zeros** | No positivity claim at checkpoint 1. | — |

**Pre-registered kill tests (fixed before the corresponding computation):**
* K-I9: on the hard sets (14 (★)-zero primes, 38 𝔊*-zero primes, 231 prime-witness-free primes ≤ 10⁹, restricted to
  the six Mordell classes mod 840 where p = X² + 840Y²), the indicator Q(p) := [∃ prime q ∣ X with (840/q) = −1]
  has frequency within 3σ of matched random primes of the same classes and size ⟹ classifier dead.
* K-I17: the set G(p) ⊂ Cl(−4p) of classes containing a good form is not stable (beyond chance overlap) under
  multiplication by the ambiguous class or any fixed small-norm class ⟹ dead. (Inversion stability is trivial, §3.)
* K-I23: some prime p ≡ 1 (4), p < 2000, has ES solutions but none with a twisted lift ⟹ dead as a universal mechanism.
* K-#11: a counterexample (M odd, coprime a, b ∣ M², (2M+1) ∣ a + b) for M ≤ 3·10⁶ ⟹ the slice is not sterile.
  (Not triggered; replaced by a proof, Lemma V.)

## 1. Triage table (10 items; details §2–§3)

| item | precise lemma tested | ≤ 30-min falsifier and outcome | verdict |
|---|---|---|---|
| **IDEAA #11** e = p + 2 | M odd ⟹ no a, b with ab ∣ M², (2M+1) ∣ a + b | search M ≤ 3·10⁶: 0 hits; then **proved** (Lemma V, Vieta descent) | **closed: sterile, PROVED** (all n ≡ 1 (4)); extended to all gaps e − n (Prop R, §4) |
| **I10** Pell d > 1 | a Type I point with p ∣ 4a²d + 1 | **proved impossible** for every d (Cor T10); 6 718 points checked | **dead, PROVED** |
| **IDEAA #10** nonsquare d | Type I at (a, d) forces (d/p) = −1 | Lemma T10; the fixture (1033, 1, 132) has (132/1033) = −1 | sharpened necessary condition (PROVED); no forcing lemma |
| **I9** X of p = X² + 840Y² | Q(p) = [∃ q ∣ X, (840/q) = −1] separates hard primes | K-I9 fired: 4 hard sets vs 200 matched controls each, all \|z\| < 2 (§3) | **dead as classifier, EVIDENCE** |
| **I17** class-set stability | G(p) ⊂ Cl(−4p) stable under J or a fixed class | K-I17 fired: J-overlap 72 vs chance 276 (anti-stable), explained by a small-norm null model (§3) | **dead (d = 1), EVIDENCE** |
| **I23** twisted trace at √p | every ES-solvable p has a triple with a twisted lift | K-I23 fired: no lift for 36 of the 37 primes p ≡ 1 (4) below 400 (only p = 5 has one) (§3) | **dead as mechanism, EVIDENCE** |
| **I24** cross-d transport | the d ↦ d + 1 lattice map carries solutions | **proved** to be the K1 t-form: (★) ⟺ ∃ t, a ∣ t: a + t/a ≡ −p (mod 4t) (§3) | **reduces (PROVED)**; no transport |
| **I5** non-affine involution | a cross-slice involution with controllable fixed points | Lemma P + census: no parity law (§3); the Vieta map ι of §4 *is* a non-affine cross-n involution for Type I, but it never fixes n | **open in general; the one specified map gives sterility only** |
| **I6** mock completion | G(q) = Σ q^{4abd−a−b} has a GL₂ (mock) modular completion | not testable in 30 min; G(e^{−t}) ~ (8t)⁻¹ log²(1/t) (three free divisor variables) — a ζ³-type object (§3) | **untested; Assessment: low** |
| **I12** target-only forcing | CRT-forced smooth part of p + u hits −1 (mod 4u) | algebra: the forced part is exactly the C-form covering class (§3) | **reduces (PROVED)** to covering |

**Blunt summary of the triage.** None of the ten items yields a mechanism that forces a tied divisor event. Two
items became theorems of the *opposite* kind (sterility of Type I slices); three died on their pre-registered tests;
two reduce by a short proof to the known covering form; I5 and I6 stay open only in the unspecific sense in which
they were open before.

## 2. Two kills that are now theorems

### 2.1 Lemma V — the Type I slice e = n + 2 is empty (IDEAA #11). PROVED.

**Lemma V.** Let M ≥ 1 be odd. There are no positive integers a, b with ab ∣ M² and (2M + 1) ∣ (a + b).

*Proof.* Suppose not, and take a counterexample (M, a, b) with M minimal. Write a + b = c(2M + 1), M² = abd with
c, d ≥ 1.
(0) a ≠ b: if a = b then a² ∣ M², so a ∣ M and gcd(a, 2M + 1) = 1; from a ∣ 2a = c(2M + 1) we get a ∣ c, hence
2a = c(2M + 1) ≥ 3a, absurd. By symmetry assume a > b.
(1) Let F(T) := T² − 2bcd·T + bd(b − c). Then F(M) = abd − bcd(2M + 1) + b²d = bd(a + b − c(2M + 1)) = 0. The
other root is M′ := 2bcd − M ∈ ℤ, with M·M′ = bd(b − c). M′ ≡ M (mod 2), so M′ is odd; in particular M′ ≠ 0.
(2) Put a′ := M′²/(bd) = (2bcd − M)²/(bd) = 4bc²d − 4cM + a ∈ ℤ, and a′ > 0 because M′ ≠ 0. Dividing F(M′) = 0 by
bd gives a′ + b = c(2M′ + 1). The left side is positive, so 2M′ + 1 > 0, i.e. M′ ≥ 0, hence M′ ≥ 1 (odd).
Also a′·b·d = M′², so a′b ∣ M′².
(3) M·M′ = bd(b − c) < b²d < abd = M², so M′ < M.
Thus (M′, a′, b) is a counterexample with odd 1 ≤ M′ < M, contradicting minimality. ∎

*Remarks.* (i) No coprimality and no primality is used. (ii) For even M the descent ends at M′ = 0 (b = c, a′ = 0)
and solutions exist: (a, b, M) = (4c³d, c, 2c²d). The only use of "M odd" is M′ ≠ 0. (iii) CERTIFIED independently:
exhaustive search, all odd M ≤ 3·10⁶ (1 499 999 values, 103 090 of them with 2M − 1 a prime ≡ 1 (8)), coprime
pairs: 0 hits (`scripts/z69_twist_slice11.c`, `data/z69/twist/slice11_3e6.txt` empty).

**Corollary V.** For every n ≡ 1 (mod 4) (prime or not) there is no Type I solution with e = n + 2: there
4abd = n(n+2) + 1 = (n+1)², so abd = M² with M = (n+1)/2 odd and (2M + 1) = e ∣ a + b. This closes the item
"e = p + 2: empirically empty, unproved" of `Z69_IDEAA.md` idea 11 / `REVIEW_IDEAA.md` next-step 3.
Together with the e = p − 2 slice (sterile for p ≡ 1 (8), IDEAA) both "(pe+1)/4 a perfect square" slices are sterile.

### 2.2 Lemma T10 — Type I needs (d/p) = −1; the negative-Pell substitution is dead for every d (I10, IDEAA #10). PROVED.

**Lemma T10.** Let p ≡ 1 (4) be prime and (a, d, f) a Type I point: f > 0, f ∣ 4a²d + 1, f ≡ −p (mod 4ad). Then the
Legendre symbol (d/p) = −1.

*Proof.* Every prime q ∣ 4a²d + 1 is odd, prime to d, and has −d ≡ (2a)⁻² (mod q), so the Jacobi symbol
(−d/f) = ∏ (−d/q) = 1. On the other hand f ≡ −p ≡ 3 (mod 4) gives (−1/f) = −1, and f ↦ (d/f) (Kronecker symbol
of the positive integer d; f odd and prime to d) is periodic mod 4d and even, so (d/f) = (d/p) [as f ≡ −p mod 4d].
Hence 1 = (−d/f) = −(d/p). ∎

**Corollary T10 (I10 for all d).** No Type I point has p ∣ 4a²d + 1. Indeed p ∣ 4a²d + 1 gives (d/p) = (−1/p) = +1.
So the substitution "4a²d + 1 = pY² from dX² + 1 = pY²" (I10) is sterile for **every** d ≥ 1, not only d = 1; the
orbit-sparsity heuristic of IDEAB is not needed. Square d (IDEAA #10's PROVED part) is the special case (d/p) = +1,
and the review's fixture (p, a, d) = (1033, 1, 132) has (132/1033) = (3/1033)(11/1033) = (+1)(−1) = −1 as required.
CERTIFIED check: 6 718 Type I points for all primes p ≡ 1 (4) below 3000 with ad ≤ 400: all have (d/p) = −1, none
has p ∣ 4a²d + 1 (`scripts/z69_twist_typeI_check.py 3000 400`).
*Assessment:* Lemma T10 is the Type I form of the campaign's Jacobi obstruction (IDEAB R5, `JOINT_BUDGET.md`
Rem. 4.4); new here is only the remark that it kills the Pell substitution uniformly in d.

## 3. Triage tests

### I5 (parity / involutions) — first census. EVIDENCE + one PROVED lemma.

**Lemma P (PROVED).** For n ≥ 3 let T_n := {(x, y, z) ∈ ℕ³ : xyz − x − z = n}. The swap (x, y, z) ↦ (z, y, x) has
fixed points x(xy − 2) = n; for n prime the only one is (1, n + 2, 1). Hence |T_p| is odd for every odd prime p.
The same holds at n = 9 and n = 105 (only x = 1), where U₇ fails: so **no involution of T_n that is defined
uniformly in n can have all its fixed points among the U₇ words** (cf. `INVOLUTION_ES.md` Prop 2.3 for the
analogous statement on its set X).

Census (`scripts/z69_twist_words.c 1000000`, `data/z69/twist/words_parity_1e6.txt`): for n ≡ 1 (8), n ≤ 10⁶, counts
of words by 2-adic pattern modulo 4. "all" and "OOO" (x, y, z all odd) are odd at every prime (Lemma P); every other
tested sub-count (x even; 8 ∣ xy; x even with xy ≡ 4 (8); x even with xy ≡ 2 (4); x ≤ z; x < z with 4 ∣ y;
16 ∣ xy; …) is equidistributed mod 4 (each class 24.3–25.7 % of the 19 552 primes). No parity law beyond Lemma P.

**Lemma P′ (all-odd words; PROVED).** Let n ≡ 1 (mod 8) and let O_n ⊂ T_n be the words with x, y, z all odd.
(a) Every word of O_n has y ≡ 3 (mod 4). (b) Split O_n = A_n ⊔ B_n with A_n := {x ≡ z ≡ 1 (4)},
B_n := {x ≡ 3 or z ≡ 3 (4)}. Then a word of O_n is in A_n iff y ≡ 3 (mod 8) and in B_n iff y ≡ 7 (mod 8).
(c) Every word of B_n with x ≡ 3 (4) is the Type I solution (a, b, c, d, e) = (1, yz − 1, z, (xy − 1)/4, y) of n
(f = x in K3 form); so B_p ≠ ∅ ⟹ ES(p). (d) For p prime, |A_p| is odd and |B_p| is even.
*Proof.* (a) y ≡ 1 (4) would give xz − x − z ≡ 1, i.e. (x − 1)(z − 1) ≡ 2 (mod 4), impossible for x, z odd.
(b) With f = xy − 1, f′ = zy − 1 we have ff′ = ny + 1 ≡ y + 1 (mod 8), and for y ≡ 3 (4): f ≡ 2 (4) iff x ≡ 1 (4),
f ≡ 0 (4) iff x ≡ 3 (4). So x ≡ z ≡ 1 (4) iff ff′ ≡ 4 (8) iff y ≡ 3 (8). (c) 4·1·(yz − 1)·(xy − 1)/4 =
(xy − 1)(yz − 1) = ny + 1 (from xyz − x − z = n: (xy − 1)(yz − 1) = y(xyz − x − z) + 1), and a + b = yz = ce.
(d) the swap preserves A_p and B_p; its only fixed point (1, p + 2, 1) lies in A_p (Lemma P). ∎
Census (`scripts/z69_twist_ooo.c 20000000`, `data/z69/twist/ooo_2e7.txt`; all primes p ≡ 1 (4), where the roles of
3 and 7 (mod 8) are exchanged for p ≡ 5 (8)): |A_p| odd and |B_p| even at all 635 170 primes; B_p = ∅ at 154 primes
(all ≡ 1 (24), last 17 662 681); B_p = ∅ and no (★) word only at p = 409; B_{m²} = ∅ at all 2 235 odd squares.
**Consequence for I5 (PROVED).** The odd set O_p has odd cardinality, its certificates are exactly the fibres
y ≡ 7 (8), and its forced element (1, p + 2, 1) sits in a fibre y ≡ 3 (8). A Zagier-type second involution on O_p
with all fixed points certificates must therefore move y between the classes 3 and 7 (mod 8) — it must be
cross-slice in y — and it cannot be defined uniformly in n: O₉ = A₉ = {(1, 11, 1), (1, 3, 5), (5, 3, 1)} has odd
cardinality and no certificate (this is the T1 constraint of `INVOLUTION_ES.md` Prop 2.3 in word coordinates).

*Assessment.* The cross-review asked for a specified non-affine cross-slice involution rather than a raw parity
count. One exists for Type I — the Vieta map ι of §4 — and it is tested there; it moves n, so it cannot serve as
the second involution of a Zagier-type argument at a fixed prime.

### I9 (X-coordinate of p = X² + 840Y²). EVIDENCE; pre-registered kill K-I9 fired.

For p in the six Mordell classes write p = X² + 840Y² (Cornacchia; gcd(X, 840Y) = 1). Any prime q ∣ X has
(p/q) = (840/q). Q(p) := [∃ prime q ∣ X with (840/q) = −1]. `scripts/z69_twist_i9.py 200`,
`data/z69/twist/i9_classifier.txt`; controls = the next 200 primes of the six classes above each hard prime.

| hard set (members in the six classes) | Q hard | Q control | z | Q with q < 100: hard / control (z) |
|---|---|---|---|---|
| 14 (★)-zero primes (9) | 0.444 | 0.562 | −0.71 | 0.111 / 0.196 (−0.64) |
| 38 𝔊*-zero primes (20) | 0.450 | 0.557 | −0.96 | 0.150 / 0.200 (−0.56) |
| 231 prime-witness-free primes ≤ 10⁹ (145) | 0.559 | 0.593 | −0.85 | 0.145 / 0.210 (−1.92) |
| U⁽⁸⁾-zero primes ≤ 10⁸ (11) | 0.636 | 0.539 | +0.65 | 0.182 / 0.196 (−0.12) |

No separation at 3σ. The only value near 2σ (fewer q < 100 on the witness-free set) has the trivial sign: hard
primes have few small non-residues of any origin. The "half law" of IDEAB is not a law: the control frequency of Q
is 0.54–0.59 at these sizes and tends to 1 slowly (X has all its prime factors in a density-½ set with probability
≍ (log X)^{−1/2}); nothing was proved or needed. *Verdict:* dead as a classifier; as a forcing rule it would be a
"divisor of a nonlinear expression" rule, covered conditionally by `Z69_NL7.md` Thm NL.

### I17 (existential class-set stability). EVIDENCE; pre-registered kill K-I17 fired.

**Dictionary (PROVED, elementary).** Type II with d = 1: 4ab = p + e, ce = a + b. The form
[4ac − 1, 4a, 4ab − p] has discriminant −4p and is equivalent to [e, 2(b − a), ·]; with s = b − a, t = a + b:
s² + p = t² − e = e(c²e − 1). So the class is that of the ideal 𝔢 = (e, s + √−p), and

  **Type II (d = 1) ⟺ ∃ t > s ≥ 0, t ≡ s (2): e := t² − s² − p > 0 and e ∣ t.**

G(p) := {classes [𝔢]} is closed under inversion (a ↔ b gives s ↦ −s); this is the only stability found.
Test (`scripts/z69_twist_i17.py`, `data/z69/twist/i17_classsets.txt`): all primes p ≡ 1 (8) in [20000, 24000)
(99 primes, Σ|G| = 1232, Σ|non-principal genus| = 6034). Members g ∈ G with J·g ∈ G (J = [2, 2, (p+1)/2] the
ambiguous class): 72, against 276 expected for a random subset of the genus; with ℓ·g ∈ G (ℓ the class of a prime
ideal over the least split prime ≡ 1 (4)): 378 against 276. So G is not J-stable — it is *anti*-stable — and not
ℓ-stable. Null model (`scripts/z69_twist_i17null.py`): the |G(p)| classes of ideals of smallest norm e ≡ 3 (4) have
J-overlap 0 and contain 740 of the 1232 good classes. The anti-stability is the small-norm bias of good classes (a
class with an ideal of small odd norm e has J-translate with reduced form [2e, ·, ·], whose odd values are ≳ p/2e),
not a hidden character. Only d = 1 was tested. *Verdict:* dead as a coset-like structure.

### I23 (twisted trace at √p). EVIDENCE; pre-registered kill K-I23 fired.

**Lemma (PROVED).** Let αᵢ = xᵢ + yᵢ√p ∈ ℤ[√p], yᵢ ≠ 0, Dᵢ = pyᵢ² − xᵢ². Then 4/√p = Σ 1/αᵢ ⟺ (4/p = Σ yᵢ/Dᵢ
and 0 = Σ xᵢ/Dᵢ). Writing wᵢ = xᵢ/yᵢ = gᵢ/hᵢ in lowest terms and nᵢ = Dᵢ/yᵢ: yᵢ/Dᵢ = 1/nᵢ with a prescribed
positive integer nᵢ and integral αᵢ iff mᵢ := phᵢ² − gᵢ² ≠ 0 divides nᵢ (then yᵢ = nᵢhᵢ²/mᵢ, xᵢ = nᵢgᵢhᵢ/mᵢ;
mᵢ < 0, i.e. |wᵢ| > √p, is allowed and gives yᵢ < 0), and the second equation is the **twist equation
Σ wᵢ/nᵢ = 0**. (Proof: 1/(√p·α) = y/D − (x/(pD))√p; n = y(p − w²) = ym/h²; gcd(m, h) = 1.)
So a twisted lift is an ES triple (n₁, n₂, n₃) plus three rationals wᵢ with (phᵢ² − gᵢ²) ∣ nᵢ and Σ wᵢ/nᵢ = 0;
w = 0 is allowed iff p ∣ nᵢ. IDEAB's "the descent condition is the original problem verbatim" dropped the twist
equation; the review was right that this was a gap.
Test (`scripts/z69_twist_i23.py 400 40`, `data/z69/twist/i23_lifts_400_h40.txt`): for every prime p ≡ 1 (4) below
400 and every ES triple (all triples, both types), lifts of two of the nᵢ with h ≤ 40 (both signs of m) were
enumerated and the forced third w tested exactly. **Lifts exist at p = 5 only**:
4/√5 = 1/(4 + 2√5) + 1/(3 − √5) + 1/(5 − √5), the lift (w₁, w₂, w₃) = (2, −3, −5) of 4/5 = 1/2 + 1/4 + 1/20 (all
three αᵢ are 2 or √5 times a unit; ℚ(√5) has the smallest fundamental unit). **None of the other 36 primes has a
twisted lift in the search range.** (A first run that wrongly required m > 0 found none at all; corrected.)
Reason (Assessment): lifts with |m| small relative to ph² have |w| close to √p, and three such cannot satisfy
Σ ±√p/nᵢ ≈ 0 together with Σ 1/nᵢ = 4/p; the remaining lifts need a large divisor m of nᵢ of the special shape
±(ph² − g²) *and* an exact linear relation. The bound h ≤ 40 on two of the three terms is a search limit, not a
proof of non-existence.
*Verdict:* the lift is an extra constraint, not a relaxation; dead as a mechanism.

### I24 (cross-d lattice transport). PROVED reduction.

For c = 1 put s = a + b, t = ab. Then p = 4dt − s, so for fixed t the admissible d are exactly those with
s ≡ −p (mod 4t) and s ∈ Σ(t) := {a + t/a : a ∣ t}; since 2 ≤ s ≤ t + 1 < 4t, s is the least positive residue:

  **(★) ⟺ ∃ t ≥ 1, a ∣ t : a + t/a ≡ −p (mod 4t) and p + a + t/a ≥ 4t.**

In Lenstra's regime 4d > √p there is at most one candidate (s, t) per d, namely t = ⌈p/4d⌉, s = 4dt − p. The
map d ↦ d + 1 at fixed t adds 4t to s and leaves the residue class, so every t meets at most one d per a; changing
t changes the lattice with no relation between Σ(t) and Σ(t + 1). The "lattice" is the IDEAB class K1 (e = a + b,
c = 1) in the coordinates (s, t). *Verdict:* re-encoding of the covering form; no transport.

### I6 (mock / harmonic completion) and I12 (target-only forcing). Statements only.

* **I6.** #{(a, b, d) : 4abd − a − b ≤ x} ~ (x/8) log²x (three free divisor variables), so G(e^{−t}) ~ (8t)⁻¹ log²(1/t)
  as t → 0⁺ (PROVED, elementary Abelian theorem). The d-fibres are weight-1 Eisenstein-type series of level growing
  with d (`METAPLECTIC_ES.md` Thm K); the full sum is a triple Lambert series with a cubic exponent, of the type of
  Σ d₃(n)qⁿ. No completion or transformation law was derived here and none was tested. *Assessment:* even a
  completion would give an identity for the generating function, and positivity of one coefficient would still
  need a pointwise bound for the non-Eisenstein part at a single prime.
* **I12.** Let D be any integer ≡ 3 (4) and k ∣ (D + 1)/4, u := (D + 1)/(4k). Then D ∣ p + u ⟺ D ∣ 4kp + 1
  (PROVED: 4k(p + u) = 4kp + 1 + D). So "choose u by CRT so that a prescribed D divides p + u and D ≡ −1 (4u)" is
  the condition p ≡ −(4k)⁻¹ (mod D) with k ∣ (D + 1)/4 — a class of the covering system (C-form), τ((D+1)/4)
  classes out of φ(D). Tracking the uncontrolled cofactor separately changes nothing: the cofactor's divisors are
  exactly what is not controlled. No target-specific subset-product statement with deterministic hypotheses was
  found. *Verdict:* reduces to covering.

## 4. Push 1 — the Vieta structure of Type I and the complete classification of the gaps e − n > 0. PROVED.

Lemma V is the first instance of a general structure. Throughout this section n ≡ 1 (mod 4) is any integer (no
primality), and a **Type I solution of n** is (a, b, c, d, e) ∈ ℕ⁵ with 4abd = ne + 1, ce = a + b. Then ne ≡ 3 (4),
so e ≡ 3 (4), and the **gap** j := (e − n)/2 is an odd integer. Also a ≠ b (a = b gives e ∣ 2a, e ∣ a,
e ∣ 4a²d = ne + 1, e = 1, contradicting e ≡ 3 (4)).

**Lemma ι (the cross-n Vieta involution).** Let (a, b, c, d, e) be a Type I solution of n. Put
  n′ := 4bcd − e,  e′ := 4bcd − n,  a′ := ce′ − b.
Then (1) e·e′ = 4b²d + 1, so e′ is a positive integer ≡ 3 (4) and n′ ≡ 1 (4); (2) n′e′ + 1 = 4a′bd and
a′ + b = ce′; (3) e′ − n′ = e − n; (4) applying the same map to (n′; a′, b, c, d, e′) returns (n; a, b, c, d, e).
*Proof.* (1) e(4bcd − n) = 4bd(a + b) − (4abd − 1) = 4b²d + 1. (2) (4bcd − e)(4bcd − n) + 1
= 16b²c²d² − 4bcd(n + e) + 4abd = 4bd(4bc²d − c(n + e) + a) = 4bd(4bc²d − cn − b) = 4bd·a′, using a − ce = −b.
(3), (4) are immediate. ∎
So ι_b : (n, e, a) ↦ (n′, e′, a′) fixes (b, c, d) and the gap; for fixed (b, c, d, j) the two values n, n′ are the
two roots of one monic quadratic (for j = 1 this is F of Lemma V with n = 2M − 1). In K3 language e′ = f_b is the
K3 divisor attached to b. ι_b is polynomial, not affine with a bounded menu, and it moves n: it is a "non-affine
cross-slice involution" in the sense asked for under I5. n′ may be ≤ 0, in which case a′ < 0.

**Lemma D (strict descent when e > n).** If n ≥ 1, j ≥ 1 and a > b, then n′ < n.
*Proof.* n′ < n ⟺ 4bcd < n + e ⟺ (multiply by a, use 4abd = ne + 1) c(ne + 1) < a(n + e) = cne + ce² − b(n + e)
⟺ c + b(n + e) < ce². Now a > b gives 2b ≤ ce − 1, and n ≤ e − 2 gives n + e ≤ 2e − 2, so
c + b(n + e) ≤ c + (ce − 1)(e − 1) = ce² − (c + 1)(e − 1) < ce². ∎

**Proposition R (gap classification).** Let j ≥ 1 be odd. The following are equivalent.
 (i) Some integer n ≥ 1, n ≡ 1 (mod 4), has a Type I solution with e = n + 2j.
 (ii) (**root at level j**) There are positive integers ν, ε, α, b, c, d with ν ≡ ε ≡ 3 (mod 4), ν + ε = 2j,
   4αbd = νε − 1 and b − α = cε.
*Proof.* (i) ⟹ (ii). Among all Type I solutions with gap j of integers n ≥ 1 take one with n minimal, and let
a > b. By Lemmas ι and D, (n′; a′, b, c, d, e′) satisfies the Type I equations with the same gap, e′ ≥ 3 and
n′ < n. If n′ ≥ 1 then 4a′bd = n′e′ + 1 > 0 gives a′ > 0, a Type I solution of a smaller positive integer with
gap j: contradiction. So n′ ≤ 0, and n′ ≡ 1 (4) gives n′ ≤ −3. Put ν := −n′ ≥ 3, ε := e′, α := −a′. Then
ν ≡ ε ≡ 3 (4), ν + ε = e′ − n′ = 2j, 4αbd = −(n′e′ + 1) = νε − 1 > 0 (so α ≥ 1) and b − α = b + a′ = cε.
(ii) ⟹ (i). Put n := 4bcd − ε, e := 4bcd + ν, a := ce − b. Then e − n = 2j, n ≡ −ε ≡ 1 (4),
ne + 1 = 16b²c²d² + 4bcd(ν − ε) − 4αbd = 4bd(4bc²d + cν − cε − α) = 4bd(4bc²d + cν − b) = 4abd, and a + b = ce.
Positivity: b = α + cε ≥ 1 + ε, so n = 4bcd − ε ≥ 4b − ε ≥ 4 + 3ε > 0, and a = 4bc²d + cν − b ≥ 3b > 0. ∎

**Corollaries (PROVED).**
* j = 1: ν + ε = 2 is impossible with ν, ε ≥ 3. This re-proves Corollary V.
* j = 3 and j = 5 are sterile: (ν, ε) = (3, 3) needs αbd = 2 with 3 ∣ b − α > 0; (3, 7), (7, 3) need αbd = 5 with
  7 ∣ b − α or 3 ∣ b − α > 0. So **no n ≡ 1 (4) has a Type I solution with e ∈ {n + 2, n + 6, n + 10}.**
* Every j ≡ 3 (mod 4), j ≥ 7, is non-sterile: j = 4m + 3 has the root (ν, ε, α, b, c, d) = (8m + 3, 3, 1, 3m + 1, m, 2),
  i.e. n = 24m² + 8m − 3 has the Type I solution e = n + 2j (m = 1: n = 29, e = 43, (a, b, c, d) = (39, 4, 1, 2)).
* **Square slices.** For a prime p, pe + 1 is a perfect square iff e = k(kp + 2) or e = k(kp − 2). For
  e = k(kp + 2) with k ≡ 1 (4): M = (kp + 1)/2 is odd, abd = M² and (2M + 1) = kp + 2 divides e ∣ a + b, so
  Lemma V applies: **no Type I solution has e = k(kp + 2), k ≡ 1 (mod 4)** (k = 1 is Corollary V).
* Every Type I solution with e > n lies on a finite ι-chain n > n′ > n″ > … ending at a root (iterate Lemmas ι, D,
  always moving the larger of the two letters). For fixed (c, d, j) the solutions are integer points of the conic
  a² + b² − (4c²d − 2)ab − 2jc(a + b) + c² = 0 with c ∣ a + b, and ι_a, ι_b are its Vieta involutions.

**CERTIFIED cross-check** (`scripts/z69_twist_gaps.py 301 3000`, `data/z69/twist/gaps_301_3000.txt`): roots
enumerated for all odd j ≤ 301 — 38 sterile gaps: 1, 3, 5, 9, 13, 17, 21, 29, 33, 37, 41, 49, 57, 61, 69, 73, 77,
89, 93, 113, 117, 121, 129, 133, 153, 157, 169, 173, 189, 197, 209, 213, 233, 241, 257, 261, 281, 297 (all ≡ 1 (4)
except 3). Brute force over all n ≡ 1 (4), n ≤ 3000, all odd j ≤ 301: no solution on a sterile gap; every gap with
a root whose first chain element is ≤ 3000 has a brute-force solution, and the minimal n per gap equals that
first chain element in all eight printed cases (29, 109, 37, 101, 125, 277, 909, 173 for j = 7, 11, 15, 19, 23, 25, 27, 31).

**What this is and is not (Assessment).** Proposition R is a complete, primality-free description of the Type I
solutions with e > n: they are the ι-descendants of finitely many roots per gap, and the first chain element
n = 4bcd − ε is the K3 point (b, d, f = ε) with cf < b — so for a *given* prime the statement "p has a Type I
solution with e > p" is again a divisor-in-a-class statement (ε ∣ 4b²d + 1, ε ≡ −p mod 4bd), not a forced event.
What is new is the method: Vieta descent proves universal statements about tied divisors on slices where the
modulus and the factored number are algebraically tied (e − n fixed), which the campaign had only as "empirically
empty, unproved". It yields sterility, never existence: the descent needs a solution to start from. Type II has
no analogue — for fixed (b, c, d) its solutions satisfy the *linear* relation e(4bcd − 1) = p + 4b²d (the K2
congruence class), so its transport (p, e) ↦ (p + t(4bcd − 1), e + t) is unipotent, not hyperbolic.
