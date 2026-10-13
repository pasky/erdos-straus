# Review R201 of GROWING_MUTE.md (O201, checkpoint 1) — hostile review

Reviewer: R201 (side agent). Document reviewed at merge of `side-agent/growing-mute`.
From-scratch scripts: `scripts/review_gm_*.py` (no reuse of `scripts/gm_*`).

(in progress)

## Claim-by-claim

### Def 1.0 + Prop 1.1 (cap hierarchy, (A, B) form, T1) — SOUND-AFTER-REPAIRS (M1, m1)

Re-derivation. Def 1.0 agrees with EXPONENT_CAP Def 1.1 at e = 1 (v_ℓ(q) ≤ 1 and rad q | y ⇔ q squarefree, q | y);
the hierarchy q = 1 ⇒ (q | y, q sqfree) ⇒ q | y ⇒ rad q | y is trivial and holds for all solutions.
(a) With c = v_ℓ(Q), s = v_ℓ(K): "c ≤ s + 1 and s ≥ 1 for all ℓ | Q" ⇔ Q | K·rad K — correct.
(b) v(Q₀) = min(c, s), v(Q₁) = max(0, c − s); Q₁ | Q₀ ⇔ c ≤ 2s ⇔ Q | K² — correct; gcd(Q₁, k) = 1 since ℓ | Q₁ ⇒ c > s
⇒ v_ℓ(Q₀) = s ⇒ ℓ ∤ k — correct. Moreover in the shot family ES^{(y,1)} ⇔ (Q₁ squarefree and Q₁ | Q₀) (c > s forces
c = s + 1 with s ≥ 1) — this is the "B squarefree" claim of (c); correct.
(c) Forward: A = 2k, B = Q₁, g·D = nA² + B² (EXPONENT_CAP Prop 1.3(b)), g + 1 = 2AQ₀ with B | Q₀ — correct.
Converse: D ≡ −B² (mod 2A) is forced (A even ⇒ 2A | A²), so Prop 1.3's converse applies; correct, but the
written proof is garbled ("with Q₁ ≡ …") — m1.
T1: (mA)² + B² with gcd(mA, B) = 1, odd ⇒ all divisors ≡ 1 (mod 4), while 4 | 2AB ⇒ g ≡ 3 (mod 4). Correct.

From-scratch check (`scripts/review_gm_dict.py 201 301 60`, exact rationals, solutions classified DIRECTLY from
(x, y, z) per Def 1.0, not via the paper's criteria):
* Part A: all 30 443 shot data (odd n ≤ 201, odd Q ≤ 301, gcd(Q, n) = 1, every g ≡ 3 (4) dividing n + 4Q²):
  den z = Q₁² always; ES ⇔ Q | K; ES^{(y,1)} ⇔ Q | K rad K; ES^{[2]} ⇔ Q | K² ⇔ Q₁ | Q₀; ES^{(y)} ⇔ rad Q | K — no
  exception. 497 have Q | K² (matches the author), all map to valid (A, B, g).
* Part B: all 816 triples (odd n ≤ 201, even A ≤ 60, odd B ≤ 60) (matches the author): every one yields a valid
  solution with den z = B², B | y; B squarefree (782) ⇒ ES^{(y,1)}. Odd squares n ≤ 201: zero triples (T1).
* **But 370 of the 816 triples have λ = (g+1)/(2AB) EVEN, and 35 have gcd(λ, n) > 1.** Since Q₀ = λB and
  Q = λB², these give Q even or gcd(Q, n) > 1 — NOT shot data in the paper's Notation (Q odd, gcd(Q, n) = 1).
  The solutions are nevertheless valid (den z = B², odd, prime to n). See M1.

### Prop 1.2 (Markov-type equation, Pell automorphs, "no Markov tree") — (a), (b) SOUND; (c) SOUND but under-stated, reading mis-worded (m2–m5)

(a) g·D = nA² + B² with g = 2ABλ − 1 ⇔ nA² + B² + D = 2λD·AB; (B − μA)² − (μ² − n)A² = B² − 2μAB + nA² = −D. Correct.
(b) For the form [n, −2μ, 1] (disc 4(μ² − n)) the automorph attached to T² − (μ² − n)u² = 1 is
[[T + μu, −u], [nu, T − μu]] — exactly the paper's matrix. u even ⇒ T odd ⇒ A' even, B' ≡ TB odd;
(T − μu)(T + μu) = 1 − nu² ≡ 1 (mod n) ⇒ gcd(B', n) = 1; unimodular ⇒ gcd(A', B') = 1. Positivity: f < 0 forces
μ² > n and B/A between the two positive roots; T > 0 ⇒ both eigenvalues positive ⇒ each half-cone preserved.
Correct. B-involution B ↦ 2μA − B: root product nA² + D > 0, so B' > 0; gcd(B', n) = 1 because gcd(D, n) = 1 (a
common prime would divide B); the paper asserts "always available" without this one-line check (fine).
(c) A ↦ 2μB/n − A integral ⇔ n | 2μB ⇔ n | λ (gcd(B, n) = gcd(D, n) = 1). Reciprocity argument re-derived and
correct. **Stronger and simpler (m2):** n | λ gives g ≡ −1 (mod 4n), and every prime q | g has (−n/q) = 1, so the
Kronecker character χ_{−4n} (odd, χ(−1) = −1) gives χ_{−4n}(g) = χ_{−4n}(−1) = −1 vs +1: n | λ is impossible for
EVERY odd n > 1, not only n ≡ 1 (mod 4). (For n ≡ 3 (mod 4): (n/g) = −(g/n) = −(−1/n) = 1, (−n/g) = −1.)
Check `scripts/review_gm_orbits.py nlam 401 60`: 1912 points over all odd n ≤ 401 (both classes mod 4), n | λ in 0.

From-scratch numerics (`review_gm_orbits.py 300 …`, data/review_gm/orbits_300.txt): n = 13: 4 points
[(10,3,2,11), (16,5,3,7), (36,5,1,47), (184,19,9,7)] — matches; 17: 19 (4 with B = 1); 29: 20; 73: 6; 9, 25, 49: 0 —
all match. Every point: D ≡ 3 (mod 4); 3 automorph images forward and 3 backward each re-verified as V_n points
(366 images in all) and the B-involution image re-verified. Two deviations:
* **"Every (λ, D) pair carries ≤ 3 points in the box" is false**: n = 29, (λ, D) = (2, 3) has 4 points
  (2,7), (2,17), (14,47), (14,121) (m4). (B = 121 is not squarefree; the claim may have meant squarefree B.)
* **Squarefreeness is NOT preserved** by automorphs: of the images of squarefree-B points, many have r² | B
  (e.g. 14 of 114 at n = 17, 16 of 120 at n = 29, all 3 at n = 37 — counting only r < 1000). So Prop 1.2(b)'s
  infinite orbits live in ES^{[2]}, not in ES^{(y,1)}. See M3.
* μ² − n IS sometimes a square (15 points with A, B ≤ 60, n ≤ 401, e.g. n = 35, (A,B,λ,D) = (2,11,2,3), μ = 6);
  then the (λ, D)-fibre is finite. Prop 2.2 states the "μ² − n non-square" hypothesis, but §5 item 2 ("Every
  solution with B > 1 lies on an infinite Pell orbit") drops it (m3).

Reading of (c) (Assessment) — wording misleading, substance partly right (m5): on S_{n,D} both Vieta moves (in A
and in B) fix C = 2μ, and their composite is a Pell automorph of the same conic f_μ = −D; C enters linearly, there
is no third involution, so there is never a Markoff-type *tree* across different C, whatever (c) says. What the
missing A-involution really costs is classical Vieta jumping: with both involutions integral, a minimal point of
the conic satisfies A ≤ μB/n and B ≤ μA, which bounds μ in terms of D (finitely many C per D, as for
x² + y² + D = Cxy); with only the B-involution, reduction theory still gives finitely many orbits per (μ, D) but no
bound on μ. Rephrase (c)'s reading as "no Vieta-jumping bound on C = 2λD in terms of D", for every odd n.

### Prop 2.1 (firing set for fixed P is a finite divisor set) — statement SOUND (modulo M1); "Consequence" OVERCLAIMED (M2)

Statement: for fixed squarefree P, overflow Q₁ | P is bounded, so Thm 2.1 gives g ≤ 2nQ₁²(n + Q₁²) ≤ 2nP²(n + P²);
the A-range bound (A = 2k ≤ (n+1)/2 + (n+1)Q₁² from both cases of the Thm 2.1 proof) is ≤ (n+1)(1 + 2Q₁²). Correct.
I also checked the bound g ≤ 2nB²(n + B²) directly on all (A, B, g) with odd n ≤ 301, A, B ≤ 80, INCLUDING the
λ-even triples outside the shot convention: max ratio 0.292 (n = 3, A = 4, B = 1, g = 7); λ even: 0.205.
The "Consequence (Assessment)" and §5 item 2 ("for each fixed P the sieve's progression meets the firing set only
in an explicit finite divisor set — BV/BDH and Chebotarev contribute nothing") do not follow: the construction in
(V4) has P ≈ g^{1/4} GROWING with g, and then the proposition's bound reads g ≲ 2nP⁴ ≈ 2n·g — vacuous. This is
precisely the regime R200 M1 identified as NOT excluded by the wall. Finiteness "for each fixed P" is the fixed-S
case already in EXPONENT_CAP Cor 2.2. See M2.

### Prop 2.2 (equivalence with V_n / S_{n,D}) — SOUND-AFTER-REPAIRS (M1, M3, m6)

(i) ⇔ (ii) ⇔ (iii) re-derived (C := 2λD; D ≡ 3 (mod 4) from 1 + D ≡ 0 (mod 4)). Caveats: (ii) contains points with
λ even / gcd(λ, n) > 1, which are not shot data in the Notation (M1); and Q = λB² so (i) needs "λ odd, gcd(λ, n) = 1"
or the shot convention must be widened. "On V_n with B free, every point with μ² − n non-square lies on an infinite
Pell orbit" is correct but V_n was DEFINED in (ii) with B squarefree, which the orbit does not preserve (M3).
"On the curve B = 1, A ≤ 3(n+1)/2" — correct (even A ≤ (n+5)/2: with D = 2Aκ − 1 the B = 1 slice is
A(4λκ − n) = 2(λ + κ)); brute-force check `scripts/review_gm_b1check.py 1201`: max A/(3(n+1)/2) = 0.667,
max g/(2n(n+1)) = 0.292 over all odd n ≤ 1201.
Reading: the heuristic Σ τ(nA²+B²)/(2AB) ≍ log³X is a fair Assessment. "For each D the solution set is O(log X)
Pell/Vieta orbits" is unsupported: for fixed D, μ = λD ranges over multiples of D up to ≍ nX, each with its own
orbits (m6). **The Ghosh–Sarnak claim is WRONG** (M4): their abstract (arXiv:1706.06712, checked) says "for almost
all k the Hasse Principle holds … and there are infinitely many k's for which it fails" — failures have density 0
(their Thm 1.2(i): at least √K (log K)^{−1/2} failures in 0 < k ≤ K; full text checked), NOT "a positive proportion of k".

### Prop 3.1 (e-ladder) and "Smooth representatives" — factual parts SOUND; label mixing (m7); one wrong heuristic (m8)

Factual content re-derived: box sizes τ(K), ≤ τ(K)·2^{ω(K)} (#{Q | K rad K} = ∏(v_ℓ(K) + 2)), τ(K²) — correct;
#{Q ≤ g^C : rad Q | K} ≤ (C log g/log 2 + 1)^{ω(K)} — correct; A ≤ 3(n+1)/2, g ≤ 2n(n+1) on B = 1 — correct (checked,
see Prop 2.2). But the PROVED label covers sentences that are Assessments ("NOTHING changes at a single modulus",
"the entire difference is archimedean": the e = 1 box is larger by a factor up to 2^{ω(K)} — still g^{o(1)}, but not
"nothing"; and "B free does not [cap A]" is only "no cap is proved", see M3). The ES^{(y)} line "all of (F_g^*)² for
sieved g" is FROBENIUS_FIRING's mechanism stated loosely (true for the g the sieve produces, not "box = everything").
**"For e = 0 … expected count ≍ log³ n" is wrong** (m8): the B = 1 slice is the d = 1 slice, not all of Type II;
its heuristic count is Σ_{A ≲ n} τ(nA² + 1)/(2A) ≍ log² n, and my exact counts agree: mean number of B = 1 triples
over 400 primes p ≡ 1 (4) near 10³, 10⁴, 10⁵, 10⁶ is 11.6, 20.5, 30.1, 43.0, i.e. /log²p = 0.243, 0.242, 0.227,
0.225 (flat) vs /log³p = 0.035 → 0.016 (decaying). (Elsholtz–Tao's log³ is for all Type II solutions.)
GHS/Harman: unverified citations, honestly labelled as such; the argument does not depend on them (the point is
only that the admissible set is a divisor-type set of size g^{o(1)}), so no defect beyond m9.

### §4 Numerics (EVIDENCE) — SOUND; reproduced exactly and strengthened

From-scratch `scripts/review_gm_least.py 1000000 300 51` (data/review_gm/least_1e6.txt; 2·10⁵ run in
least_2e5.txt) uses a COMPLETE test for the B = 1 slice (no k-bound): with D = 2Aκ − 1 the slice is
A(4λκ − p) = 2(λ + κ), equivalently p + 4t² has a divisor d ≡ −p (mod 4t) for some t ≤ (1 + √(1+4p))/4
(cross-checked against brute force over all odd n ≤ 1201, `review_gm_b1check.py`). Results to 10⁶:
* 39 175 primes; B = 1 with k ≤ 20: 38 705; least-k histogram identical to the author's (1: 29 666, 2: 4 223, …,
  20: 21) — data/review_gm/least_k_hist_1e6.txt.
* **Exactly 99 primes < 10⁶ have no B = 1 triple at all** (provably, complete test); the author's 116 is a superset
  (the other 17 have B = 1 only at k > 300, e.g. 90313: k = 324; 187417: k = 1674). So the author's "exact only for
  p < 400: p = 13, 37, 97" is too weak AND incomplete: 181 and 193 (< 400, also covered by k ≤ 300 ≥ 3(p+1)/4) also
  have no B = 1 solution, and with the complete test all 99 are exact (m10).
* All 99 have ES^{(y,1)} (A, B) solutions with k ≤ 300: B = 3 (89), 5 (5), 7 (3), 11 (p = 2293), 23 (p = 12433);
  each verified with exact rationals AND classified directly per Def 1.0 (den z = B², B odd, prime to p, B | y).
* **4/13 = 1/6 + 1/390 + 9/65**: 1/6 + 1/390 = 11/65, + 9/65 = 4/13 ✓; den z = 9 = 3², 3 odd, 3 ∤ 13, 3 squarefree,
  3 | 390 ✓ — a genuine ES^{(y,1)} solution per Def 1.0 (and EXPONENT_CAP Def 1.1, e = 1). BUT it has λ = 2,
  Q = 18 (the doc itself prints Q = 18): not a shot datum in the Notation (Q odd). Same for p = 12433 (λ = 28).
* Under the strict shot convention (λ odd, gcd(λ, p) = 1): 204 primes < 10⁶ lack a λ-odd B = 1 triple; within
  k ≤ 300, B ≤ 51 all but 4 have a λ-odd ES^{(y,1)} triple; the 4 (541, 1297, 12433, 19273) have one with a larger
  window: (B, k, g, λ) = (73, 304, 266303, 3), (51, 343, 4268291, 61), (51, 1442, 32652647, 111),
  (15, 1637, 7955819, 81). So the EVIDENCE claim survives under either convention, but "B ≤ 23" holds only for the
  widened family (M1).
* §4.2 orbit numbers reproduced (see Prop 1.2), except "≤ 3 points per (λ, D)" (m4).

