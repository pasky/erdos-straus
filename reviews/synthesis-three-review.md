# R207 — hostile review of O208 SYNTHESIS_SPARKS3.md (+ BRAINSTORM/s3_*.md)

Reviewer branch `side-agent/review-synthesis-three`, merged `side-agent/synthesis-three`. From-scratch scripts:
`scripts/review_s3_thm11.py` (Lemma 1.0, (∗), Thm 1.1(a)/(b)), `scripts/review_s3_exact.py` (independent exact
census of M/p failures), `scripts/review_s3_certs.py` (M^□ / M^{(S)} certificates, overflow profile), further
scripts named below. No author script was reused.

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.0 (M-shot identity, den(z) = (Q/gcd(Q,k))²) | SOUND |
| Thm 1.1(a) (M^□ at odd non-squares prime to M) | SOUND (minor notation/scope repairs) |
| Thm 1.1(b) (no M-shot at odd squares) | SOUND |
| (∗) (−M/g) = −1 for every odd g ≡ −1 (mod M), incl. M = 4·square | SOUND |
| EVIDENCE §1 (278 pairs, g ≤ 239, S-certificates Q ≤ 385, 8/131 example) | SOUND (independently reproduced) |
| overflow profile "Q₁ ≥ 3 at every failing pair, = 3 at 131, 241" | SOUND-AFTER-REPAIRS (m4) |
| Remark (ii): Gupta–Murty transfer "verbatim" | GAP (D3: fails as stated at n = 3k², 3 ∤ M; harmless for primes) |
| Cor 2.1 formal part (R_8(131) ∧ ¬8/131) | SOUND |
| Cor 2.1 "must use a 4-specific input" + label PROVED | SOUND-AFTER-REPAIRS (D1: meta-statement, Assessment; D2: novelty vs (J)31) |
| item-by-item numerator-uniform Assessment | (filled below) |
| memos | (filled below) |

## Claim-by-claim

### Lemma 1.0 — SOUND
Re-derived: m′g = n + MQ² ≡ n and g ≡ −1 (M) give m′ ≡ −n (M), x ∈ ℤ; y = nk ∈ ℤ. M/n − 1/x = m′/(nx);
m′/(nx) − M/(n(g+1)) = (m′g − n)/(nx(g+1)) = MQ²/(nx(g+1)) = 1/z. gMx = g(n + m′) = n(g+1) + MQ² ⇒ gx = nk + Q².
Valuations at ℓ | Q (ℓ ∤ n), c = v_ℓ(Q), σ = v_ℓ(k): σ = 0 ⇒ v_ℓ(x) = 0, v_ℓ(z) = −2c; 1 ≤ σ < 2c ⇒ v_ℓ(x) = σ,
v_ℓ(z) = 2σ − 2c; σ ≥ 2c ⇒ v_ℓ(z) ≥ σ. In each case the ℓ-part of den z is ℓ^{2max(0, c−σ)}; ℓ ∤ Q never
appears (z = nxk/Q²). ℓ = 2 is included (no parity of Q needed). Numerically: 172 591 random shots (M ≤ 60,
composite g allowed), 0 failures of the exact identity and of den(z) = (Q/gcd(Q,k))² (`review_s3_thm11.py`).

### (∗) and Thm 1.1 — SOUND
(∗) re-derived: (4/g) = 1; 8 | M ⇒ g ≡ 7 (8) ⇒ (2/g) = 1 (so every power 2^a ‖ M is fine); for odd ℓ | M, Jacobi
reciprocity (ℓ/g)(g/ℓ) = (−1)^{((ℓ−1)/2)((g−1)/2)} with (g/ℓ) = (−1/ℓ) and (g−1)/2 odd gives (ℓ/g) = 1; this holds
for any multiplicity, so M = 4·square is included (trivially). (−1/g) = −1. Brute force: all M ≡ 0 (4) ≤ 200,
all odd g ≡ −1 (M) < 2·10⁴ (22 480 pairs), 0 failures.
(a) (n/g) = (n₀/g) = (g/n₀)(−1/n₀) is correct (g ∤ k); a class a mod n₀ with (a/n₀) = −(−1/n₀) exists as n₀ > 1
is squarefree; CRT needs gcd(n₀, M) = 1 (hypothesis); s ≢ 0 (g ∤ n); Q by CRT mod 2g·rad n. Brute force: every
odd non-square n < 10⁵ prime to M, M ∈ {4, …, 24}, certified with a PRIME g ≡ −1 (M) and odd Q prime to n,
den z an odd square prime to n, exact Fractions (max g: 103, 263, 239, 751, 659, 719); every odd non-square
n < 3000 for every M ≡ 0 (4) ≤ 100 (incl. 36, 64, 100 = 4·square, and 60, 84 with two odd primes).
Hypothesis gcd(n, M) = 1 is necessary for the shot mechanism: M = 12, n = 3k² (k < 60): 0 shots of any g; M = 20,
n = 5k²: 0 shots (the theorem states the hypothesis; §4 drops it — m2).
(b) Correct: every prime ℓ | k² + MQ² has (−M/ℓ) = 1, so (−M/g) = 1 for every divisor g (Jacobi), contradicting
(∗). Brute force over ALL divisors g (composite included), k, Q < 150, M ∈ {4,…,24, 28, 36, 60, 100}: 0 shots.
Scope remark: (b) is about shots, not M^□ itself — M^□ ⊇ (M/n) holds at most odd squares (e.g. 8/9 =
1/2 + 1/3 + 1/18); the report states this correctly, SPARKS3 §1 should too (m3).

### EVIDENCE §1 and Cor 2.1 data — SOUND (independently reproduced)
`review_s3_exact.py` (own exact solver: x ∈ (p/M, 3p/M], then a/b = 1/y + 1/z ⟺ ∃ d | b², d ≤ b, d ≡ −b (mod a))
recomputed the failing primes p ∤ M for M ∈ {8, 12, 16, 20, 24}: up to 10⁶ the lists coincide EXACTLY with
`data/ms/prime_fail_1e8.txt` (5, 20, 37, 61, 154 primes), and M = 20 up to 3·10⁶ adds exactly 2763601. So 277 of the
278 pairs are reproduced from scratch; the census for p ∈ (10⁶, 10⁸] (only 2763601 lies there besides) is not
re-run (M = 8, 12 lists also agree with PW Table 1, `sources/pw.txt` l. 868–884).
`review_s3_certs.py`: every one of the 278 pairs has an exactly verified M^□ certificate with a prime g; the max of
the least prime g per M is 23, 59, 191, 199, 239 (claim "g ≤ 239" ✓). M^{(S)}, S = {3,5,7,11}: the 14 pairs with
p ∈ S (8:3,11; 12:5,7; 16:3,5,7,11; 20:3,7,11; 24:5,7,11) are excluded; all 264 others have a certificate, max least
Q = 385 ✓; none has den z = 1 (consistent with M/p failing). 8/131 = 1/20 + 1/131 + 9/2620 ✓ (g = 7, Q = 3).

### Overflow profile (§1 last paragraph) — SOUND-AFTER-REPAIRS (m4)
With Q restricted to ODD Q ≤ 60 (as the M^□ definition requires) the least Q₁ is ≥ 3 at every pair where a shot
exists and equals 3 at (8,131) (Q = 3, g = 7) and (8,241) (Q = 51, g = 679) ✓. But (a) 8 pairs have NO odd-Q shot with
Q ≤ 60 at all — (16,97), (16,1489), (20,761), (20,5641), (24,1657), (24,2281), (24,3433), (24,97777) — so "≥ 3 at every
failing pair" is vacuous there; (b) if even Q is allowed, Q₁ = 2 occurs (e.g. (8,241): Q = 2, g = 7; also (8,3),
(8,11), (8,17), (16,131), …), so the parenthetical "necessarily" only forces Q₁ ≠ 1, not Q₁ ≥ 3.

### Remark (ii): Gupta–Murty transfer to r ≡ −1 (mod M) — GAP (as an Assessment; harmless for primes ≥ 5)
Checked against UNIT_ORBIT_ES Lemma 2.2 / Thm 2.4. What transfers: Lemma 2.2's class condition (a ≡ 3 (4),
a ≢ 1 mod every odd ℓ | M′) holds for a ≡ −1 (mod M) (ℓ ≥ 3); (r−1)/2 is odd for r ≡ 7 (8) (indeed for every r ≡ 3 (4)),
so 2 is never sifted; for r ≡ 3 (4) index ≤ 2 ⇒ Γ_r ⊇ (F_r^*)² and Γ_r² = (F_r^*)² (squares = 4th powers, the square
group having odd order); |S| = 4 for S = {3,5,7,11}; the needed sign (n/r) = −1 comes from (∗) exactly as in Thm 1.1(a).
What does NOT transfer verbatim: Thm 2.4 needs a prime ℓ₀ ≥ 5 of odd valuation in n so that a residue a ≢ 0, 1 (mod ℓ₀)
with either character value exists; it handles the remaining case n ≡ 3 (4) by the Q = 1 shot (n + 4 has a prime
factor ≡ 3 (4)). For M ≠ 4 the Q = 1 shortcut is unavailable (n + M need not have a divisor ≡ −1 mod M), and when the
squarefree kernel is n₀ = 3 (n = 3k², 3 ∤ M, e.g. M = 8, 16, 20, 28) the two requirements collide: (n/r) = (3/r) = −1
with r ≡ 3 (4) forces r ≡ 1 (mod 3), so 3 | (r−1)/2 and the index-3 case cannot be sifted out. A Kummer/Chebotarev
condition (some q ∈ S a non-cube mod r) inside the sieve would be needed — not routine. EVIDENCE that the statement is
still true there: M ∈ {8,16,20,28}, n = 3k² (k < 80), S = {5,7,11,13}: a prime-g shot with Q ∈ ⟨S⟩ exists in every
case. For n = p prime ≥ 5 (all that Cor 2.1 uses) the transfer is routine. See D3.

### Cor 2.1 — formal part SOUND; "must use a 4-specific input" SOUND-AFTER-REPAIRS (D1, D2, D4)
Formal content (re-verified): 8^□(131), 8^□(241) hold (Thm 1.1(a); explicit certificates), 8^{(S)} holds at both
(explicit certificates), the M-shot family has T1 (Thm 1.1(b)), and 8/131, 8/241 are insoluble (PW Table 1 row m = 8,
`sources/pw.txt` l. 868; my own solver). So "∀ p ∤ 8: R_8(p) ⇒ 8/p" is false for R ∈ {□, (S)}. This is SOUND.
The inference "a proof of ES … must therefore use at least one input that is FALSE for M = 8 at p = 131 or 241 — an
input specific to the numerator 4" is not a theorem and is wrong as worded:
(1) *Thresholds.* Schinzel's conjecture is itself "M/n solvable for n > n₀(M)" (PW intro); the PW/Elsholtz–Tao
lottery heuristic (≈ log³p/M solutions) is numerator-uniform and predicts exactly the small failures 3, 11, 17, 131, 241.
An input "p > n₀(M)" (or any analytic estimate that is only effective beyond a threshold) is numerator-uniform yet
false at (8,131). A uniform mechanism "R_M(p) ∧ p > n₀(M) ⇒ M/p", combined with the existing computational
verification of ES far beyond any plausible n₀(4), is NOT excluded by Cor 2.1. What survives is the threshold-uniform
version, and that is (J)31's "meaningful form" (BL Rem 1.10 + PW): combined with Thm 1.1(a) one gets the honest
strengthening "for every M ≡ 0 (4), M ≥ 6.52·10⁹, there is a prime p ∈ (M², 2M²) with M^□(p) and ¬(M/p)" (PW Thm 1.2,
`sources/pw.txt` l. 65; p > M² so p ∤ M), i.e. any M-uniform transport needs a threshold n₀(M) > M² (and, via the
proof of PW Thm 1.1, > exp(M^{1/3−ε}) for large M). The document never mentions thresholds; §3.1 ("removing every
numerator-uniform tool from consideration") and §4 ("both need a numerator-4-specific input") overclaim. (D1)
(2) *Label.* "PROVED given Thm 1.1 and the CERTIFIED census" should attach only to the formal implication failure;
the "Consequently …" sentence is a relativisation-style Assessment that presupposes the argument is literally uniform
in M (a hidden hypothesis). The author's report says this correctly ("The formal content is the single implication
failure"); the deep file does not. (D1)
(3) *Novelty.* (J)31 (DISCOVERIES l. 845–853; TES_FINITE Cor 5.4 + B7) already states "An ES proof must use something
specific to the numerator 4 (Assessment; see (J)32)", and (J)32/MODEL_SPECIFIC already uses 8/131 to refute the
χ-fibre mechanism for m = 8 (S₈(131) = ∅) — i.e. as a mechanism test. Thm 1.1 is (J)28 Prop 2.2 with 4 → M (the only new
computation is (∗)). Genuinely new: (∗) and Thm 1.1 for general M; the observation that the relaxed shot mechanisms
(with exact T1) also cannot see the failures, which adds "□/mute relaxation + Dirichlet/sieve existence" to the list
"BM + T1" of (J)31's B7; and the explicit certificate data. §3.2's "8/131, 8/241 appeared before only as Brauer–Manin
controls …, not as a test for proof mechanisms" is false. (D2)
(4) *BM clause.* "No BM obstruction to 8/p at 131, 241: Bright–Loughran Rem 1.10": BL Rem 1.10 (checked, BL p. 4) only
states that BL's Thm 1.2/1.5/1.8/1.9 analogues hold for m/n; it computes nothing at 131, 241. The certificates are
TES_FINITE Thm 5.3 (relative to BL Thm 1.6 / Rem 1.10). For M = 12, 16, 20, 24 no BM computation exists in the campaign,
yet the "likewise" parenthesis and §3.2(i) ("every local, Brauer–Manin … input holds") extend the claim to them; and
several of those pairs are trivial archimedean failures (M/p > 3: (16,3), (16,5), (20,3), (24,5), (24,7)). (D4)

### Item-by-item "numerator-uniform" Assessment — fair as a list, overreaching as a conclusion
Each bullet is plausible and correctly labelled Assessment (shot identity, (J)34 duality, T1/BL local lemma at 2, box
finiteness = BL Lemma 3.10 for any numerator, Dirichlet/sieve, composition "uniform in form"). Two caveats: (a) the
list classifies tools by whether 4 enters, not by whether they carry M-dependent thresholds, so "hence cannot be that
input" fails for every threshold-bearing analytic tool (D1); (b) the FF / ℤ[ω] bullet is a different kind of
blindness — relaxation true where the exact problem at the SAME numerator fails (ES_q^{(s)} vs ES_q; TES^{□₃} vs TES)
— not numerator-blindness; it is in fact stronger than anything known over ℤ (ES has no known failure), so "the same
blindness" should read "the analogous relaxation-vs-exact blindness" (m5). Also the bullet says (J)28 covered N ≤ 6000
("15 of the 16") while the report and memo s3_order3_numerator say the recipe was run to 27000 (all 16); I re-ran
`scripts/syn2_tes_shots.py 27000 50` (campaign script, not independent): 5856/5856 solved, incl. N = 26893 (m6).
Nothing beyond the formal implication failure is claimed as PROVED in the list itself; the overreach is in §2's
"Consequently", §3.1 and §4.
