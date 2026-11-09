# z69 MINE round 2 — PRE-REGISTRATION (committed before any round-2 run)

Context: cross-model review items 1, 2, 5 (`data/z69/xreview/REVIEW_MINE.md`). ES is OPEN.

## Samples (fixed now)
* **H split** (all 849 H primes, no exclusions): H_test = {p ∈ H : int(sha256(str(p)), 16) odd} (411 primes, incl. 3361,
  21841, 76441, 3613009), H_train = the rest (438, incl. 2521, 9601). Files `H_train.txt`, `H_test.txt`.
  Exploration (inspecting relation details, choosing follow-up statistics) uses H_train and the controls only.
  H_test is scored once, with the statistics/generators fixed below or fixed on H_train before H_test is opened.
* **Disjoint band B**: primes p ≡ 1 (8) in [5·10⁹, 5·10⁹ + 4·10⁷] (no H prime lies there), 10 000 drawn uniformly
  (random n ≡ 1 (8) in the band, accepted iff prime; seed 6969).
* Kill-test sets: odd squares m² ≤ 10⁶; Z₇; the 38 U⁽⁸⁾-zero primes ≡ 1 (8) ≤ 10⁸.

## Part A (item 1) — Q-set / CFpA letters, within-prime decoys
For every prime p and **all** its witnesses (no cap), letters ℓ ∈ {x, y} with ℓ ≥ 5. Full CF period of √p (no truncation):
the list (Q_1, …, Q_L), Q_L = 1. Statistics per (p, ℓ): D = 1[∃ i: ℓ | Q_i]; R = #{i: ℓ | Q_i}/L; E = 1[ℓ ∈ {Q_i}];
first index i₀ (relative position i₀/L) and its parity; G = 1[∃ i: gcd(ℓ, Q_i) > 1 and ℓ ∤ Q_i] is *not* used (too
dense). CFpA: D_A = 1[ℓ divides some convergent denominator of p/A, A ∈ {a, b, c, d, e, g}].
**Decoys** (same p, same Q list): for each letter ℓ = 2^k·∏ q_j^{e_j}, a decoy ℓ′ = 2^k·∏ q′_j^{e_j}, q′_j a random odd
prime with χ_p(q′_j) = χ_p(q_j) (0 only if q′_j = q_j = p, impossible here), q′_j ∈ [q_j/1.5, 1.5 q_j] (q′_j = q_j allowed
when the window has no other choice), 2 decoys per letter. Null: real and decoy letters have the same D, R, E, CFpA
rates (the Q-set "knows" only χ_p at the prime factors of ℓ and ℓ's size). Estimator: prime-weighted (each prime's
letters averaged, then primes averaged), cluster-by-prime z for real − decoy. A *signal* = |z| ≥ 4 on H_train
**and** the same sign with |z| ≥ 3 on H_test (and reported on controls).

## Part B (items 2, 5) — pre-registered bounded-complexity generators (no witness consulted)
Candidate letters from p's data only:
* GEN-G: a, b and |αa + βb| (0 ≤ α ≤ 3, |β| ≤ 3, gcd(α, β) = 1); GEN-N: the same for (c, d), (e, g), (u, v) [p ≡ 1 (3)],
  (s, t) [(p/7) = 1];
* GEN-J (joint): |X ± Y| and gcd(X, Y) for distinct X, Y ∈ {a, b, c, d, e, g, u, v, s, t} (available ones);
* GEN-Q: Q_i and partial quotients a_i for i ∈ {1..10} ∪ {⌊L/2⌋−3, …, ⌊L/2⌋+3} (full period), the 10 largest Q_i;
* GEN-A: convergent denominators of p/A, A ∈ {a, b, c, d, e, g};
* GEN-C: h(−4p), h(−8p), h(p) and their odd parts and quotients by 2, 4, 8;
* GEN-ALL: union.
**Only candidates c ≥ 65 are used** (K5: bounded letters are the Prop K / Cor K′ cascade, which alone covers every
prime ≤ 4·10⁹ by Z68_U7O). Each candidate c is tried in all three roles, exactly: x-role (p + c has a divisor
≡ −1 mod lcm(8, c)), y-role (cp + 1 has a divisor ≡ −1 mod lcm(8, c), proper), z-role (p + c has a divisor e ≡ −1 mod c
with 8 | ((p + c)/e)·((e + 1)/c)); every produced word is verified (xyz − x − z = p, 8 | xy).
**Decoy generator** for each GEN-*: each candidate c replaced by a random integer c′ with v₂(c′) = v₂(c) and
|log c′ − log c| ≤ 0.05 (c′ ≥ 65), same multiset size.

## Kill tests (fixed now)
* K1: on odd squares m² ≤ 10⁶ no word is produced (engine sanity; U₇(m²) = 0).
* K2: no word on Z₇.
* K3: on the 38 U⁽⁸⁾-zero primes, report coverage; produced words must be non-U⁽⁸⁾ (automatic).
* K4: coverage ≥ 99.9 % on band B AND every prime of H_test (p ≤ 10¹² handled; none excluded).
* K5: only candidates ≥ 65; report the share of successes whose successful letter divides p + c′ or c′p + 1 for some
  c′ ≤ 64 (Λ-type, Cor K′).
* K6: coverage(generator) − coverage(decoy) > 0 with paired McNemar z ≥ 3 on band B (else: indistinguishable from a
  size-matched blind search).
**HOT LEAD (user criterion):** some generator passes K4 — reported loudly regardless of K6, with K5/K6 status.
**Mechanism lead:** K1–K6 all pass.

## Part C (item 2, z-relations on H)
(x, z)-phantoms (p′ = p + 8j·xz, |p′ − p| ≤ p/2, canonical word) on H_train and H_test with **all** witnesses, plus a
χ-matched variant (χ_{p′}(ℓ) = χ_p(ℓ) for ℓ ∈ {3, 5, 7, 11, 13} not dividing xz; coverage reported where matching
fails). Relations: divz / vdivz / eqz of the round-1 dictionary. Signal criterion as in Part A.
