# Z69_TWIST — pushing the surviving twists of the z69 ideation lanes: no forcing mechanism found (tested proposals killed, reduced, or left unresolved); by-product = fixed-gap Vieta-descent sterility theorems for Type I; not a HOT LEAD

**ES is OPEN. Nothing here proves or disproves it.** Status: final; internal hostile review ×3 applied (§7); waiting for
the cross-model review; not merged (verdict §6: **narrowed / dead on the triaged twists**; no forcing mechanism).
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

Checkpoint 1 holds only *triage* objects (kill lemmas and census tests); the final table is in §5.

| screen | behaviour of the triage results | label |
|---|---|---|
| **F1 odd squares** | Lemma V (§2.1) and Lemma T10 (§2.2) are sterility statements valid for every n ≡ 1 (4) (V) / every prime p ≡ 1 (4) (T10; the Jacobi-symbol version (d/n) = −1 holds for all n ≡ 1 (4)); they assert *absence* of solutions, so they cannot contradict R(m²) = 0. No positivity claim is made at checkpoint 1. | PROVED |
| **F2 numerator 8 / C-even** | No positivity claim. The word census (§3, I5) separates 4 ∣ y, 8 ∣ y, 8 ∣ xy; it reproduces zeros of the 8 ∣ y line and none of the 8 ∣ xy line at primes ≤ 10⁶. | CERTIFIED (census) |
| **F3 composites** | Lemma V needs no primality (it holds for all odd M = (n+1)/2). The parity lemma P (§3, I5: total word count odd) holds at primes *and* at 105 and at 9, where U₇ fails — this is exactly why it cannot force anything (§3). | PROVED |
| **F4 known zeros** | No positivity claim at checkpoint 1. | — |

**Pre-registered kill tests** (K-I9, K-I17, K-I23 were fixed before their computations; K-#11 was written down
only after its search had returned 0 hits and Lemma V had been found — listed for completeness, not as a
pre-registration; the I5 word census also preceded this list):
* K-I9: on the hard sets (14 (★)-zero primes, 38 𝔊*-zero primes, 231 prime-witness-free primes ≤ 10⁹, restricted to
  the six Mordell classes mod 840 where p = X² + 840Y²), the indicator Q(p) := [∃ prime q ∣ X with (840/q) = −1]
  has frequency within 3σ of matched random primes of the same classes and size ⟹ classifier dead.
* K-I17: the set G(p) ⊂ Cl(−4p) of classes containing a good form is not stable (beyond chance overlap) under
  multiplication by the ambiguous class or any fixed small-norm class ⟹ dead. (Inversion stability is trivial, §3.)
* K-I23: some prime p ≡ 1 (4), p < 2000, has ES solutions but none with a twisted lift ⟹ dead as a universal mechanism.
* K-#11: a counterexample (M odd, coprime a, b ∣ M², (2M+1) ∣ a + b) for M ≤ 3·10⁶ ⟹ the slice is not sterile.
  (Not triggered; replaced by a proof, Lemma V.)

*Honest record of how the kills were evaluated (added after the internal review).* K-I9: the first run did not
implement the registered matched design; a class-matched rerun was added (§3); the outcome is "no difference
detected", which is weaker than "classifier refuted". K-I17: fired for J; for ℓ the overlap is above chance but
reproduced by a null model (§3). K-I23: the bounded search alone did not meet the registered criterion; with the
truncation Lemma T it does, at 36 primes (§3).

## 1. Triage table (10 items; details §2–§3)

| item | precise lemma tested | ≤ 30-min falsifier and outcome | verdict |
|---|---|---|---|
| **IDEAA #11** e = p + 2 | M odd ⟹ no a, b with ab ∣ M², (2M+1) ∣ a + b | search M ≤ 3·10⁶: 0 hits; then **proved** (Lemma V, Vieta descent) | **closed: sterile, PROVED** (all n ≡ 1 (4)); extended to all gaps e − n (Prop R, §4) |
| **I10** Pell d > 1 | a Type I point with p ∣ 4a²d + 1 | **proved impossible** for every d (Cor T10); 6 718 points checked | **dead, PROVED** |
| **IDEAA #10** nonsquare d | Type I at (a, d) forces (d/p) = −1 | Lemma T10; the fixture (1033, 1, 132) has (132/1033) = −1 | sharpened necessary condition (PROVED); no forcing lemma |
| **I9** X of p = X² + 840Y² | Q(p) = [∃ q ∣ X, (840/q) = −1] separates hard primes | no difference detected: exploratory pooled run all \|z\| < 2; class-matched rerun all \|z\| < 1 (§3) | **no support (EVIDENCE)**; low power on the small sets |
| **I17** class-set stability | G(p) ⊂ Cl(−4p) stable under J or a fixed class | exact invariance fails: J-overlap 72 (chance 260), ℓ-overlap 378 (chance 260); a small-norm null set gives 0 and 339 (§3) | **no evidence of coset structure (d = 1, two translations; EVIDENCE)** |
| **I23** twisted trace at √p | every ES-solvable p has a triple with a twisted lift | K-I23 fired: 36 of the 37 primes p ≡ 1 (4) below 400 provably have no twisted lift (Lemma T + finite search); p = 5 has one (§3) | **dead as universal mechanism (PROVED at those primes)** |
| **I24** cross-d transport | the d ↦ d + 1 lattice map carries solutions | **proved** to be the K1 t-form: (★) ⟺ ∃ t, a ∣ t: a + t/a ≡ −p (mod 4t) (§3) | **reduces (PROVED)**; no transport found |
| **I5** non-affine involution | a cross-slice involution with controllable fixed points | Lemmas P, P′, Remark C + census (§3): no prime-forcing parity law; on the odd set O_p the idea fails at 154 primes; the Vieta map ι of §4 is a cross-n involution for Type I but it moves n | **open in general; nothing found** |
| **I6** mock completion | G(q) = Σ q^{4abd−a−b} has a GL₂ (mock) modular completion | no numerical test; PROVED character / divisor-sum decomposition r_d = ½(E_d − O_d) (§3); no completion or transformation law established, fibrewise or after summing over d | **unresolved; Assessment: low priority** |
| **I12** target-only forcing | CRT-forced smooth part of p + u hits −1 (mod 4u) | algebra: the forced part is exactly the C-form covering class (§3) | **reduces (PROVED)** to covering |

**Blunt summary of the triage.** None of the ten items yields a mechanism that forces a tied divisor event. Two
items became theorems of the *opposite* kind (sterility of Type I slices: #11, I10); I23 is refuted as a universal
mechanism at 36 explicit primes; I9 detects no separation; I17 rejects exact invariance under the two tested
translations, and its overlap pattern is qualitatively reproduced by small-norm selection (EVIDENCE; other
translations and d > 1 untested);
I24 and I12 reduce by short proofs to the known covering form; I5 and I6 stay open in the unspecific sense in
which they were open before.

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
exhaustive search, all odd M ≤ 3·10⁶ (1 500 000 values, 103 090 of them with 2M − 1 a prime ≡ 1 (8)), pairs a, b
supported on disjoint sets of primes of M: 0 hits (`scripts/z69_twist_slice11.c`; completion line in
`data/z69/twist/slice11_3e6.txt`). The internal reviewer independently checked all 12 547 unrestricted pairs for odd M ≤ 500.

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
fixed points x(xy − 2) = n; for a prime n = p ≥ 5 the only one is (1, p + 2, 1) (x = p would need py = 3). Hence
|T_p| is odd for every prime p ≥ 5 (at p = 3 there is a second fixed point (3, 1, 3) and |T₃| = 8).
The same holds at n = 9 and n = 105 (only x = 1; |T₉| = |T₁₀₅| = 11), where U₇ fails: so **no family of
involutions of T_n can have all its fixed points among the U₇ words at every n of a domain containing 9 or 105**
(cf. `INVOLUTION_ES.md` Prop 2.3 for the analogous statement on its set X; as there, a uniformly *described* map
whose certificate property is proved only at primes is not excluded by this).

Census (`scripts/z69_twist_words.c 1000000`, `data/z69/twist/words_parity_1e6.txt`): for n ≡ 1 (8), n ≤ 10⁶, counts
of words by 2-adic pattern modulo 4. "all" and "OOO" (x, y, z all odd) are odd at every prime (Lemma P); the
swap-symmetric sub-counts 4 ∣ y and 8 ∣ y are even at every prime (swap without fixed point). The other tested,
non-symmetric sub-counts (x even; 8 ∣ xy; x even with xy ≡ 4 (8); x even with xy ≡ 2 (4); x ≤ z; x < z with 4 ∣ y;
x even, 8 ∣ xy, y odd; 16 ∣ xy) are roughly balanced mod 4 (each class 24.2–25.7 % of the 19 552 primes). No
prime-forcing parity law was found beyond these swap-forced ones.

**Lemma P′ (all-odd words; PROVED).** Let n ≡ 1 (mod 8) and let O_n ⊂ T_n be the words with x, y, z all odd.
(a) Every word of O_n has y ≡ 3 (mod 4). (b) Split O_n = A_n ⊔ B_n with A_n := {x ≡ z ≡ 1 (4)},
B_n := {x ≡ 3 or z ≡ 3 (4)}. Then a word of O_n is in A_n iff y ≡ 3 (mod 8) and in B_n iff y ≡ 7 (mod 8).
(c) Every word of B_n with x ≡ 3 (4) is the Type I solution (a, b, c, d, e) = (1, yz − 1, z, (xy − 1)/4, y) of n
(f = x in K3 form); so B_p ≠ ∅ ⟹ ES(p). Conversely the Type I solutions with a = 1 are the words with
x ≡ y ≡ 3 (4) (z = c of either parity). So with B_n^L := {words of O_n with x ≡ 3 (4)}: B_n^L ↔ Type I solutions
with a = 1 **and c odd** (a bijection), and B_n = B_n^L ∪ swap(B_n^L) — not all a = 1 solutions are reached
(p = 73: (a, b, c, d, e) = (1, 11, 4, 5, 3) is the word (7, 3, 4); found by the internal review). (d) For p prime, |A_p| is odd and |B_p| is even.
*Proof.* (a) y ≡ 1 (4) would give xz − x − z ≡ 1, i.e. (x − 1)(z − 1) ≡ 2 (mod 4), impossible for x, z odd.
(b) With f = xy − 1, f′ = zy − 1 we have ff′ = ny + 1 ≡ y + 1 (mod 8), and for y ≡ 3 (4): f ≡ 2 (4) iff x ≡ 1 (4),
f ≡ 0 (4) iff x ≡ 3 (4). So x ≡ z ≡ 1 (4) iff ff′ ≡ 4 (8) iff y ≡ 3 (8). (c) 4·1·(yz − 1)·(xy − 1)/4 =
(xy − 1)(yz − 1) = ny + 1 (from xyz − x − z = n: (xy − 1)(yz − 1) = y(xyz − x − z) + 1), and a + b = yz = ce.
(d) the swap preserves A_p and B_p; its only fixed point (1, p + 2, 1) lies in A_p (Lemma P). ∎
Census (`scripts/z69_twist_ooo.c 20000000`, `data/z69/twist/ooo_2e7.txt`; all primes p ≡ 1 (4), where the roles of
3 and 7 (mod 8) are exchanged for p ≡ 5 (8)): |A_p| odd and |B_p| even at all 635 170 primes; B_p = ∅ at 154 primes
(all ≡ 1 (24), last 17 662 681); B_p = ∅ and no (★) word only at p = 409; B_{m²} = ∅ at all 2 235 odd squares.
**Remark C (certificate words; PROVED identities).** A word (x, y, z) of n ≡ 1 (4) yields an ES-type solution if
(i) 4 ∣ y: Type II with c = 1, (a, b, d) = (x, z, y/4) [(★)]; (ii) 4 ∣ x: Type II (a, b, c, d) = (1, yz − 1, y, x/4),
because xy(yz − 1) − yz = y(xyz − x − z) (mirror: 4 ∣ z); (iii) x ≡ y ≡ 3 (4): Type I as in P′(c), for z of either
parity (mirror: z ≡ y ≡ 3 (4)). Let C_n ⊂ T_n be the words of types (i)–(iii). Every U₇ word (8 ∣ xy) is of type
(i) or (ii); B_n is the all-odd part of (iii). C_n is swap-invariant, and for a prime p ≥ 5 the only swap-fixed
word (1, p + 2, 1) is not in C_p; so |C_p| is even and |T_p ∖ C_p| is odd.

**Census of C_n (CERTIFIED, one engine; added after the second review round; third round in §7).**
`scripts/z69_twist_cert.c 1000000000`, `data/z69/twist/cert_1e9.txt` (64-bit `long` required): among all
n ≡ 1 (mod 4), 5 ≤ n ≤ 10⁹, **C_n = ∅ exactly for the 15 810 odd squares m² ≥ 9 and for n = 105** — no prime and no other non-square composite.
(Engine cross-checks in the same run: the non-square n ≡ 1 (8) without a U₇ word number 8 composites and 0
primes, matching the campaign's Z₇; C_{m²} = ∅ is forced by T1.) Relation to known targets: the types (i) ∪ (ii)
are the campaign's U_II = (c = 1) ∪ (a = 1) ⊂ Type II (`Z60_SUMMARY.md`), whose non-square zeros in the certified
range n ≤ 10¹⁰ are 105 and 4545 (`Z60_LOPEZ.md` §0 F3 row and §1; that there are no others is CONJECTURE U_II); type (iii) adds the a = 1 line of Type I and removes 4545, which has the type-(iii)
word (47, 7, 14), i.e. the Type I solution (a, b, c, d, e) = (1, 97, 14, 82, 7). So the single word equation
carries the statement

  **(W) for every non-square n ≡ 1 (mod 4), n ≠ 105, there are x, y, z ≥ 1 with xyz − x − z = n and
  (4 ∣ x or 4 ∣ y or x ≡ y ≡ 3 (mod 4))** — CONJECTURE; verified for n ≤ 10⁹ (one engine; independently to 10⁶
  by the reviewer); (W) ⟹ ES for those n.

(W) is weaker than U₇ on n ≡ 1 (8) (every U₇ word is in C_n). Unlike (MS⁺₁₀₅) it has no threshold and no
coprimality condition, and it has one known non-square exception where U₇ has eight. It is a statement about all
non-squares: a proof may of course treat primes and composites separately, but any argument for it must fail at
105 and at every odd square. *Assessment:*
this is a cleaner bookkeeping target, not a mechanism — it is the union of three known one-parameter lines and
asks for the same kind of tied divisor event (a divisor of ny + 1 in the class −1 mod y with a 2-adic side
condition); nothing here makes it easier to force.
*Tail calibration (EVIDENCE; one engine; added after the third review round, not reviewed).*
`scripts/z69_twist_certcount.c 1000000000`, `data/z69/twist/certcount_1e9.txt`: number of certificate words
(ordered) per non-square n ≡ 1 (4), n ≤ 10⁹. At most 2 words: 4 values of n, the largest 111 969; at most 6: 52
values, the largest 4 808 265. Minimum over the blocks (4^k, 4^{k+1}] from 4⁵ to 10⁹ — all non-squares:
4, 2, 4, 2, 6, 8, 6, 14, 19, 18; primes only: 4, 8, 14, 14, 18, 18, 24, 30, 36, 46 (minimisers 2521, 9601, 21841,
76441, 351289, 4149601, 5516281, 17287201, 111664081, 278893729 — the campaign's familiar hard primes). The
minimum grows steadily; no sign of a late exception to (W) below 10⁹.

**Consequences for I5 (PROVED / CERTIFIED as marked).**
* On the odd set O_p alone a Zagier-type argument is impossible **already at primes**: |O_p| is odd while B_p = ∅
  at 154 primes ≤ 2·10⁷ (CERTIFIED), the first being 73, where O₇₃ = {(1, 75, 1), (1, 3, 37), (37, 3, 1)}. So no
  involution of O_p has all its fixed points in B_p at those primes.
* On the full word set T_p with certificate set C_p there is no prime obstruction in the data (C_p ⊇ U₇ words,
  and U₇ holds at every prime tested by the campaign), but there is the square obstruction: |T₉| = 11 is odd and
  C₉ = ∅. Hence no family of involutions of T_n has all fixed points in C_n at every n ≡ 1 (8) — the T1 constraint
  of `INVOLUTION_ES.md` Prop 2.3 in word coordinates. A map that is certificate-fixed only at primes is not
  excluded; none was found.
* Within O_p the certificate type is decided by the middle letter (y ≡ 7 versus 3 mod 8), so any such involution
  would have to move y.

*Assessment.* The cross-review asked for a specified non-affine cross-slice involution rather than a raw parity
count. One exists for Type I — the Vieta map ι of §4 — and it is tested there; it moves n, so it cannot serve as
the second involution of a Zagier-type argument at a fixed prime.

### I9 (X-coordinate of p = X² + 840Y²). EVIDENCE: no difference detected.

For p in the six Mordell classes write p = X² + 840Y² (Cornacchia; gcd(X, 840Y) = 1). Any prime q ∣ X has
(p/q) = (840/q). Q(p) := [∃ prime q ∣ X with (840/q) = −1].

*First run (exploratory; deviates from the registration).* `scripts/z69_twist_i9.py 200`,
`data/z69/twist/i9_classifier.txt`: controls = the next 200 primes of the *union* of the six classes above each
hard prime (not random, not class-matched, overlapping between hard primes, and for small p far larger than p);
pooled-binomial z. A fourth hard set (U⁽⁸⁾-zeros) and the feature "q < 100" were added beyond the registration.

| hard set (members in the six classes) | Q hard | Q control | z | Q with q < 100: hard / control (z) |
|---|---|---|---|---|
| 14 (★)-zero primes (9) | 0.444 | 0.562 | −0.71 | 0.111 / 0.196 (−0.64) |
| 38 𝔊*-zero primes (20) | 0.450 | 0.557 | −0.96 | 0.150 / 0.200 (−0.56) |
| 231 prime-witness-free primes ≤ 10⁹ (145) | 0.559 | 0.593 | −0.85 | 0.145 / 0.210 (−1.92) |
| U⁽⁸⁾-zero primes ≤ 10⁸ (11) | 0.636 | 0.539 | +0.65 | 0.182 / 0.196 (−0.12) |

*Second run (after the internal review; class-matched).* `scripts/z69_twist_i9m.py 50`,
`data/z69/twist/i9_matched.txt`: deterministic controls = up to 50 nearest primes below and the 50 nearest above in the
*same* residue class mod 840 (fewer below for small p — none for 2521; controls are reused across strata and hard
primes can occur as controls; for the smallest hard primes the upper controls are far larger than p);
approximate stratified z = Σ(Qᵢ − c̄ᵢ)/√Σ c̄ᵢ(1 − c̄ᵢ)(1 + 1/mᵢ), ignoring the covariance from reuse. Results: (★)-zeros z = −0.55 (control
mean 0.546); 𝔊*-zeros −0.73 (0.538); witness-free −0.65 (0.587; 14 220 control occurrences; median largest
control/p = 1.00, worst 43); U⁽⁸⁾-zeros +0.47 (0.582; poorly size-matched, ratio 4.5).

**Reading.** No difference between hard primes and controls was detected in either design (all |z| < 2; < 1 in the
matched design; the reviewer's covariance-aware recalculation also gave |z| < 1). With 9–20 members three of the four hard sets have little power; for the 145-member set the nominal
3σ scale is a frequency difference of about 0.12. This is absence of a detected signal, not a proof that X carries no
information. The "half law" of IDEAB is not a law: the control frequency of Q is 0.54–0.59 at these sizes
(heuristically it tends to 1 like 1 − c(log X)^{−1/2}); nothing was proved. *Verdict:* no support for the
classifier (EVIDENCE); as a forcing rule it would be a "divisor of a nonlinear expression" rule, conditionally
covered by `Z69_NL7.md` Thm NL.

### I17 (existential class-set stability). EVIDENCE: exact stability fails for the tested translations (d = 1).

**Dictionary (PROVED, elementary).** Type II with d = 1: 4ab = p + e, ce = a + b. The form
[4ac − 1, 4a, 4ab − p] has discriminant −4p and is equivalent to [e, 2(b − a), ·]; with s = b − a, t = a + b:
s² + p = t² − e = e(c²e − 1). So the class is that of the ideal 𝔢 = (e, s + √−p), and

  **Type II (d = 1) ⟺ ∃ t > s ≥ 0, t ≡ s (2): e := t² − s² − p > 0 and e ∣ t.**

G(p) := {classes [𝔢]} is closed under inversion (a ↔ b gives s ↦ −s); this is the only stability found.
Test (`scripts/z69_twist_i17.py`, `scripts/z69_twist_i17null.py`, `data/z69/twist/i17_classsets.txt`): all primes
p ≡ 1 (8) in [20000, 24000) (99 primes, Σ|G| = 1232, Σ|non-principal genus| = 6034).

| translation | members g ∈ G with (translate of g) ∈ G | chance for a random k-subset, Σ k(k−1)/(m−1) (Σ k²/m) | same for the null set N |
|---|---|---|---|
| J = [2, 2, (p+1)/2] (ambiguous class) | 72 | 260 (276) | 0 |
| ℓ = class of a prime ideal over the least split prime ≡ 1 (4) | 378 | 260 (276) | 339 |

Null set N(p): the |G(p)| classes of ideals of smallest norm e ≡ 3 (4) (exactly |G(p)| classes; |G ∩ N| = 730 of
1232). So G is far from invariant under either translation (6 % resp. 31 % of its members stay in G); relative to a
random subset it avoids its J-translate and is enriched on its ℓ-translate, and the small-norm null set does both,
more strongly for J (0) and comparably for ℓ (339). (The random-subset figures ignore the inversion symmetry of G.)
*Assessment:* both deviations are of the kind produced by the small-norm bias of good classes (a class with an
ideal of small odd norm e has J-translate with reduced form [2e, ·, ·], whose odd values are ≳ p/2e; its
ℓ-translate has an ideal of norm ℓe); no sign of a hidden character or coset structure. **Scope:** exact
invariance is refuted only for these two translations, d = 1, this range. The registered kill K-I17 asked for "no
stability beyond chance overlap": it fired for J; for ℓ the overlap is *above* chance but matched by the null
model. Other fixed classes and d > 1 were not tested. *Verdict:* no evidence for a coset-like structure.

### I23 (twisted trace at √p). Kill K-I23 fired — rigorously at 36 primes (PROVED truncation + CERTIFIED search).

**Lemma (PROVED).** Let αᵢ = xᵢ + yᵢ√p ∈ ℤ[√p], yᵢ ≠ 0, Dᵢ = pyᵢ² − xᵢ². Then 4/√p = Σ 1/αᵢ ⟺ (4/p = Σ yᵢ/Dᵢ
and 0 = Σ xᵢ/Dᵢ). Writing wᵢ = xᵢ/yᵢ = gᵢ/hᵢ in lowest terms and nᵢ = Dᵢ/yᵢ: yᵢ/Dᵢ = 1/nᵢ with a prescribed
positive integer nᵢ and integral αᵢ iff mᵢ := phᵢ² − gᵢ² ≠ 0 divides nᵢ (then yᵢ = nᵢhᵢ²/mᵢ, xᵢ = nᵢgᵢhᵢ/mᵢ;
mᵢ < 0, i.e. |wᵢ| > √p, is allowed and gives yᵢ < 0), and the second equation is the **twist equation
Σ wᵢ/nᵢ = 0**. (Proof: 1/(√p·α) = y/D − (x/(pD))√p; n = y(p − w²) = ym/h²; gcd(m, h) = 1.)
So a twisted lift is an ES triple (n₁, n₂, n₃) plus three rationals wᵢ with (phᵢ² − gᵢ²) ∣ nᵢ and Σ wᵢ/nᵢ = 0;
w = 0 is allowed iff p ∣ nᵢ. IDEAB's "the descent condition is the original problem verbatim" dropped the twist
equation; the review was right that this was a gap.
**Lemma T (truncation; PROVED).** Call a lift w = g/h of n *large* if h > H. A large lift has w ≠ 0 and, with
σ = sign w, |w − σ√p| = |m|/(h²(|w| + √p)) < n/(H²√p). Hence for a twisted lift of (n₁, n₂, n₃):
(a) three large lifts force |Σ σᵢ/nᵢ| < 3/(H²p); (b) exactly one small lift wᵢ forces
|wᵢ/nᵢ + √p(σⱼ/nⱼ + σₖ/nₖ)| < 2/(H²√p). So if μ₁ := min over signs of |Σ σᵢ/nᵢ| ≥ 3/(H²p) and μ₂ := the minimum of
the quantity in (b) over the finite list of small lifts and signs is ≥ 2/(H²√p), every twisted lift has at least
two small lifts, and those are found by a finite search (two small lifts enumerated, the third w forced).
Test (`scripts/z69_twist_i23.py 400 40`, `scripts/z69_twist_i23cert.py`, `data/z69/twist/i23_lifts_400_h40.txt`,
`data/z69/twist/i23_cert_400_h40.txt`): all 37 primes p ≡ 1 (4) below 400, every ES triple (both types), H = 40
(both signs of m; exact rational arithmetic). The conditions on μ₁, μ₂ hold for every triple of
every prime (tested exactly in rational arithmetic, by sign-aware squaring for the irrational comparison); the
smallest margins are ≈ 99× for (a) and ≈ 63× for (b) (p = 109, triple (50, 60, 32700)). **Result: p = 5 has twisted lifts, e.g.
4/√5 = 1/(4 + 2√5) + 1/(3 − √5) + 1/(5 − √5)** (the lift (w₁, w₂, w₃) = (2, −3, −5) of 4/5 = 1/2 + 1/4 + 1/20;
here 4 + 2√5 = 2(2 + √5), 3 − √5 = 2·((3 − √5)/2) and 5 − √5 = 2√5·((√5 − 1)/2) with units of the maximal order of
ℚ(√5)); **each of the other 36 primes has ES triples and provably no twisted lift.** So the registered kill K-I23
fired, at 36 primes and without a search-range caveat. (History: a first run wrongly required m > 0; the bounded
search alone, as first reported, did not prove non-existence — internal review finding — which is why Lemma T
was added.)
*Verdict:* the lift is an extra constraint, not a relaxation, and it is unsatisfiable at 36 of the 37 primes
tested: dead as a universal mechanism (PROVED for those primes; nothing is claimed for p ≥ 400).

### I24 (cross-d lattice transport). PROVED reduction.

For c = 1 put s = a + b, t = ab. Then p = 4dt − s, so for fixed t the admissible d are exactly those with
s ≡ −p (mod 4t) and s ∈ Σ(t) := {a + t/a : a ∣ t}; since 2 ≤ s ≤ t + 1 < 4t, s is the least positive residue:

  **(★) ⟺ ∃ t ≥ 1, a ∣ t : a + t/a ≡ −p (mod 4t)**  (then d = (p + a + t/a)/(4t) ≥ 1 automatically).

In Lenstra's regime 4d > √p there is at most one candidate (s, t) per d, namely t = ⌈p/4d⌉, s = 4dt − p. The
map d ↦ d + 1 at fixed t adds 4t to s and leaves the residue class, so every t meets at most one d per a; changing
t changes the lattice with no relation between Σ(t) and Σ(t + 1). The "lattice" is the IDEAB class K1 (e = a + b,
c = 1) in the coordinates (s, t). *Verdict:* re-encoding of the covering form; no transport.

### I6 (mock / harmonic completion) and I12 (target-only forcing). Statements only.

* **I6.** (a) #{(a, b, d) : 4abd − a − b ≤ x} ~ (x/8) log²x (three free divisor variables), so
  G(e^{−t}) ~ (8t)⁻¹ log²(1/t) as t → 0⁺ (PROVED, elementary Abelian theorem). (b) Fibre decomposition (PROVED,
  orthogonality of characters): R(n) = Σ_d r_d(4dn + 1), r_d(N) := #{A ∣ N : A ≡ −1 (4d)}, and for N ≡ 1 (4d)
    r_d(N) = ½(E_d(N) − O_d(N)),  E_d := #{A ∣ N : A ≡ ±1 (4d)} = (2/φ(4d)) Σ_{χ even} Σ_{A∣N} χ(A),
    O_d := #{A ≡ 1} − #{A ≡ −1} = (2/φ(4d)) Σ_{χ odd} Σ_{A∣N} χ(A).
  For odd χ, Σ_{A∣N} χ(A) are the coefficients of Hecke's holomorphic weight-1 Eisenstein series; for even χ the
  same divisor sums occur as the arithmetic factors in the Fourier–Whittaker expansion of the weight-0
  real-analytic Eisenstein series at s = ½ — which is not a q-series (standard facts quoted from memory;
  normalisations, imprimitive characters and the regularisation at s = ½ were not checked here). So fibrewise the
  count is half a difference of an "even" and an "odd" divisor sum of different automorphic origin (this is the
  E/O decomposition of `Z69_IDEAA.md` §3.1). No completion or transformation law — fibrewise or for the sum over d
  — was derived or tested, and the decomposition does not decide whether one exists. *Assessment (not a
  mathematical dismissal):* low priority; a completion would have to handle growing levels and the tied argument
  4dn + 1, and positivity of one coefficient would still need a pointwise statement at a single prime.
* **I12.** Let D be any integer ≡ 3 (4) and k ∣ (D + 1)/4, u := (D + 1)/(4k). Then D ∣ p + u ⟺ D ∣ 4kp + 1
  (PROVED: 4k(p + u) = 4kp + 1 + D and gcd(4k, D) = 1). So "choose u by CRT so that a prescribed D divides p + u and D ≡ −1 (4u)" is
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

**Prior art (found by the internal review; `git grep -i vieta`).** Vieta descent on Type I is not new in the
campaign: `POINTWISE_TYPEI3.md` §5 Lemma 5.1 (descent on Fe = 1 + 4ck², e − F = 4ckδ, giving F ≡ e ≡ 1 (mod 4cδ),
with explicit chains, and sterility of low 2-levels of certificates as applications; also
`paper/es-coverings-note.tex`), and `BRAINSTORM/cayley_markoff_cm.md` P5 (Markoff/Vieta moves mapping ES points of
4/n to ES points of 4/n′). The condition (d/p) = −1 is in `JOINT_BUDGET.md` Rem. 4.4 and
`BRAINSTORM/s8_signed_genus_wall.md`. What is new here is specific: Lemma V (the slice e = n + 2, left
"empirically empty, unproved" by `Z69_IDEAA.md` idea 11 and its review), the fixed-gap formulation (Lemmas ι, D)
and the root classification Prop R with its corollaries.

**What this is and is not (Assessment).** Proposition R is a complete, primality-free description of the Type I
solutions with e > n: they are the ι-descendants of finitely many roots per gap, and the first chain element
n = 4bcd − ε is the K3 point (b, d, f = ε) with cf < b — so for a *given* prime the statement "p has a Type I
solution with e > p" is again a divisor-in-a-class statement (ε ∣ 4b²d + 1, ε ≡ −p mod 4bd), not a forced event.
The descent proves universal *non-existence* statements on slices where the modulus and the factored number are
algebraically tied (e − n fixed), and it produces existence only along the sparse chains above a root (e.g.
n = 24m² + 8m − 3), never at an arbitrary prescribed prime: it needs a solution to start from. For Type II the
same construction gives nothing: for fixed (b, c, d) its solutions satisfy the *linear* relation
e(4bcd − 1) = p + 4b²d (the K2 congruence class), so this particular fixed-(b, c, d) exchange is a translation
(p, e) ↦ (p + t(4bcd − 1), e + t), not a two-root exchange. More precisely (PROVED, by substitution a = ce − b):
the Type II solutions of all n are the image of the free parameters (b, c, d, e) ∈ ℕ⁴, ce > b, under the
polynomial n = 4bd(ce − b) − e, whereas Type I needs the divisibility e ∣ 4b²d + 1 (n = 4bcd − (4b²d + 1)/e), and
it is this divisibility whose solutions the Vieta chains organise. So for Type II any "transport" is a change of
free parameters; no hidden two-root structure of this kind exists there. (After the third review round; a
one-line substitution, not reviewed.)

## 5. Mandatory falsifier table — final

The lane ends with no positivity mechanism, so the table is for the objects actually produced.

| screen | Lemma V / Prop R / Cor T10 (sterility of Type I slices) | Lemmas P, P′ (parity of word sets) | the triaged twists as would-be mechanisms |
|---|---|---|---|
| **F1 odd squares** | V, ι, D, R hold for every n ≡ 1 (4), squares included (T10 in the Jacobi form (d/n) = −1 likewise); they assert absence of solutions on slices, compatible with R(m²) = 0. No step uses non-squareness and none is needed. | \|T_n\| and \|O_n\| are odd whenever x(xy − 2) = n forces x = 1 — e.g. at n = 9 — while B₉ = ∅ and U₇(9) fails. So parity alone forces nothing; an involution argument must break at squares, and no candidate was found. | I17 would use "χ₋₄ is a non-trivial genus character of disc −4dn" (fails for n = m²) — but exact invariance fails for the two translations tested (d = 1). I9: Y = 0. I23: ℤ[√n] degenerates. None reached a stage where the screen bites. |
| **F2 numerator 8 / C-even** | Type I only; says nothing about the C-even line of (★). | Lemma P′ separates the fibres y ≡ 0 (4), y ≡ 7 (8), y ≡ 3 (8); 8 ∣ y is the C-even line and has 286 zeros among primes ≡ 1 (8) below 10⁶ (census §3), consistent with F2. No positivity claim. | n/a (no mechanism survived). |
| **F3 composites** | V, ι, D, R, T10 (Jacobi form) are primality-free (valid for all n ≡ 1 (4)). The square-slice parametrisation e = k(kp ± 2) does use primality (n = 21, e = 3: ne + 1 = 64, and (1, 8, 3, 2, 3) is a Type I solution). | \|T₁₀₅\| = 11 is odd and 105 ∈ Z₇: parity cannot be the whole argument at composites either. Even at primes, \|O_p\| is odd with B_p = ∅ at 154 primes ≤ 2·10⁷. | n/a. |
| **F4 known zeros** | Compatible: sterility of the gaps e − n ∈ {2, 6, 10, 18, …} removes candidate solutions, it never adds one. The census finds B_p = ∅ at 154 primes ≤ 2·10⁷ and (★) ∪ B empty only at 409, which has the Type II c = 2 solution (1, 117, 2, 1, 59) (REVIEW_IDEAA). | No positivity claim at the 14 (★)-zeros or the 38 𝔊*-zeros. | n/a. |

Where primality enters: in Lemma P / P′(d) / Remark C (uniqueness of the swap-fixed word needs
"x ∣ n ⟹ x ∈ {1, n}", and holds at some composites and squares too), in the square-slice parametrisation, and in
Corollary T10 as stated (Legendre symbol); nowhere else. **No statement of this memo forces a tied divisor event
at a prime, and nothing here is progress toward a proof of ES beyond removing candidates.**

## 6. Verdict

**Narrowed / dead on the triaged twists; not a HOT LEAD. ES is OPEN.**
* Of the ten twists handed over by the two cross-reviews, **none** yields a mechanism. I23 is refuted as a
  universal mechanism (36 explicit primes provably without a twisted lift). I9 detects no separation (EVIDENCE;
  low power on the small hard sets). I17 rejects exact invariance under the two tested translations (d = 1); its
  J-avoidance and ℓ-enrichment relative to a random subset are qualitatively reproduced by small-norm selection
  (EVIDENCE; other translations and d > 1 untested). I24 and I12
  reduce by short proofs to the covering form (PROVED). I10 is dead for every d and IDEAA #11 is closed, both by
  proof (PROVED). IDEAA #10 gets the necessary condition (d/p) = −1 (PROVED, known in substance). I5 and I6 remain
  open in the generic sense; for I5 the odd-word version is excluded at 154 primes.
* **What is new here and PROVED** (specific statements; the method — Vieta descent on Type I — is prior art,
  `POINTWISE_TYPEI3.md` §5): (1) Lemma V: for odd M no a, b with ab ∣ M², (2M + 1) ∣ a + b; (2) Lemmas ι, D and
  Prop R: with the gap j = (e − n)/2 fixed, Type I carries a cross-n Vieta involution, and the solutions with e > n
  are exactly the descendants of finitely many explicit roots per gap; the gaps j = 1, 3, 5 (and 35 further
  j ≤ 301, by finite computation of roots) are empty for all n ≡ 1 (4), every j ≡ 3 (4), j ≥ 7 is not; no Type I
  solution of a prime p has e = k(kp + 2), k ≡ 1 (4); (3) Cor T10: no Type I point has p ∣ 4a²d + 1; (4) Lemma P′
  and Remark C: for n ≡ 1 (8) the all-odd words have y ≡ 3 (4); those with y ≡ 7 (8) give, after orienting x ≡ 3 (4),
  exactly the Type I solutions with a = 1 and c odd; those with y ≡ 3 (8) are not certificates of the types (i)–(iii); for
  primes the latter set has odd cardinality; (5) Lemma T and the certified absence of twisted lifts at 36 primes.
* **New CERTIFIED observation / CONJECTURE (W)** (§3): the certificate words C_n (U_II plus the a = 1 line of
  Type I, all inside the one equation xyz − x − z = n) are non-empty for every non-square n ≡ 1 (4), n ≤ 10⁹,
  except n = 105. A cleaner bookkeeping target than U₇ or (MS⁺₁₀₅); not a mechanism.
* **What the pushes say about a mechanism (Assessment).** On slices where modulus and factored number are
  algebraically tied (fixed gap), descent decides emptiness completely — but it proves non-existence, or existence
  along sparse chains, never existence at a prescribed prime. The two-root exchange exists for Type I (pe + 1 is
  symmetric in p and e); the same fixed-(b, c, d) construction for Type II is a translation (a congruence class).
  The parity structure of the word set is real (Lemmas P, P′, Remark C) and says what a Zagier-type argument on T_p
  would need — a second involution whose fixed points lie in C_p — but no such map was found, the odd-word
  restriction is impossible at 154 primes, and any family that is certificate-fixed at every n ≡ 1 (8) is excluded
  by n = 9 (as in `INVOLUTION_ES.md`).
* Not done: I6 has no test; I17 only d = 1, two translations, one range; I9 has little power on three of the four
  hard sets; the I23 certificate covers p < 400 only; Prop R's sterile list is computed only for j ≤ 301 and no
  closed description of the sterile j ≡ 1 (4) was found.

## 7. Review log

**Internal hostile review** (deep-mode reviewer subagent via the `review` tool on commits `e1b30ce5e..ff0dfd7f6`;
the tool reported the reviewer model as `openai/gpt-6-astra`; no provider / auth / quota error occurred in this
lane). Outcome: no FATAL finding; Lemma V, Lemma T10, Lemmas ι, D, Prop R and all its corollaries, Lemma P′(a)–(d),
the I24, I12, I17 and I23 identities survived line-by-line checking and independent recomputation (12 547
unrestricted pairs for Lemma V; all 6 718 T10 points; the exact 38-entry sterile list; 119 positive-gap solutions
for n ≤ 1500, j ≤ 99; the word census to 10⁶ with 87 B-empty primes; the I9, I17, I23 numbers). Findings and
fixes, all applied:
1. MAJOR — "B = Type I with a = 1" was false (p = 73: (1, 11, 4, 5, 3) ↔ word (7, 3, 4)). Fixed: B ↔ a = 1 and
   c odd (Lemma P′(c)); Remark C added (full certificate set C_n); the consequence for I5 now states the prime
   obstruction on O_p (154 primes, first 73), which the first version had missed.
2. MAJOR — K-I23 had not fired as registered (bounded search only). Fixed by proving the truncation Lemma T and
   certifying it (`scripts/z69_twist_i23cert.py`): 36 primes now provably have no twisted lift.
3. MAJOR — I9 did not use the registered matched design and over-read non-significance. Fixed: design deviation
   disclosed, class-matched rerun added (`scripts/z69_twist_i9m.py`), conclusion reduced to "no difference
   detected".
4. MAJOR — I17 conclusion exceeded the test (ℓ-overlap is above chance; chance formula; null set overshoot).
   Fixed: table with both chance formulas, exact-size null set with its ℓ-overlap (339), scoped conclusion.
5. MAJOR — the I6 coefficient identity does not settle the completion question. Fixed: automorphic statements
   marked as quoted and unchecked, conclusion marked Assessment.
6. MINOR — Lemma P false at p = 3: restricted to p ≥ 5. 7. MINOR — falsifier-table scope (T10 for n ≡ 1 (4);
   square slices use primality): corrected. 8. MINOR — census wording (4 ∣ y, 8 ∣ y forced even; bin range):
   corrected. 9. MINOR — novelty overstated: prior art paragraph added in §4, verdict reworded.
   10. MINOR — blanket wording ("never existence", Type II, uniform involutions): narrowed. 11. MINOR — the p = 5
   unit description: corrected (maximal order). 12. MINOR — artifacts: slice search now starts at M = 1 and
   records a completion line; checkers exit non-zero on violation; scripts import each other through
   `__main__` guards.
**Second review round** (same tool, commits `ff0dfd7f6..f10374845`, on the new material). Outcome: no FATAL
finding; Lemma T, its case analysis and the script's lift enumeration survived; the reviewer independently
re-enumerated all 647 ES triples of the 37 primes and all small lifts, redid every case-(a)/(b) comparison exactly,
and confirmed that only p = 5 has a twisted lift; verified the three readings of Remark C on all 7 589 words of
the 147 primes p ≡ 1 (4) below 2000 (6 422 certificate readings, explicit triples (xyz/4, nxy/4, nzy/4),
(x(yz−1)/4, nxy/4, nxy(yz−1)/4), (n(yz−1)(xy−1)/4, z(xy−1)/4, z(yz−1)(xy−1)/4)); reran both word censuses, I17,
the matched I9, T10, the gap classification and the slice search; confirmed the prior-art descriptions.
Findings, all applied: (1) MAJOR — the old I6 claim survived in the triage table: row rewritten. (2) MINOR — the
B-word correspondence needs the orientation x ≡ 3 (4): stated with B_n^L. (3) MINOR — the margin "≥ 99×" was
wrong for case (b) (63× at p = 109): corrected. (4) MINOR — the certificate compared an irrational quantity with
60-digit decimals: replaced by an exact rational test (sign-aware squaring); rerun, same result. (5) MINOR — I9
matched-design description and power statement: qualified. (6) MINOR — summaries contradicted the scoped I17
text, and the headline said "all ten die or reduce": reworded. (7) MINOR — this log claimed a second review
before it existed: now recorded. After the second round one item was added: the census of C_n and the statement (W) in §3.
**Third review round** (same tool, commit `58c70a4d9`, on that item only). Outcome: no FATAL finding; the
enumeration in `scripts/z69_twist_cert.c` is complete and its predicates match Remark C; an independent Python
enumeration to 10⁶ found exactly {105} as non-square C-zeros, {105, 4545} as U_II-zeros, and no certificate at
any odd square; the 4545 example is exact (4/4545 = 1/1148 + 1/111356 + 1/36150930). Findings, all applied:
(1) MAJOR — the U_II zero list was stated without its certified range (10¹⁰): range and CONJECTURE status added.
(2) MINOR — the census starts at n = 5 (the square 1 is not counted): stated. (3) MINOR — the text referred to a
third round before it was recorded: recorded here. (4) MINOR — "a proof could not use primality" and the
comparison with U₇ were overstated: reworded. After the third round only the tail-calibration paragraph for (W) (§3) was added;
it is a single-engine census and was not reviewed.
