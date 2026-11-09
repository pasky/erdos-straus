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

(to be completed)

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
