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
