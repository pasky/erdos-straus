# AGENT REPORT O250 — bounded cap for every prime (CAP_BOUNDED.md), checkpoint 1

Branch side-agent/cap-bounded. Files: CAP_BOUNDED.md, BRAINSTORM/z22_{bounded_windows_dickson, uniform_certificates,
large_sieve_thin, primorial_windows}.md, scripts/z22_*.py, data/z22/*.txt (tiny). ES is not solved; no infinite case
of ES is claimed. One self-review (deep reviewer) was run on the branch; its FATAL (my Cor 2.2 "never
congruence-forced" was false: 3 | p + 4 for p ≡ 17 (24)) and all MAJOR/MINOR points were repaired, marked "R-O250 review fix".

SHARP: nothing of breakthrough grade. Mild candidates for a relay: (i) the Jacobi transfer (s/m) = (s/p) for every
prime s | K_m (Lemma 1.1) makes "bounded windows die at every cap" a two-line consequence of Dickson (Thm 1.3);
(ii) the odd-order witness (Prop 2.3): the cap at a forced window is ≤ (o−1)/2·max v_s(K) with o the odd order of p/4,
independent of the window size (windows can be prime factors of p^o + 4^o); (iii) spark 1 below (cap-C coverings of
the least-non-residue lines by huge S-unit-sum windows) is the most promising unexplored construction.

## Results (labels as in DISCOVERIES)
1. Lemma 1.1 / Cor 1.2 (PROVED): Jacobi transfer and the parity law of all Lemma-3.1 window certificates (δ_p incl.).
2. Thm 1.3 (CONDITIONAL on Dickson's prime k-tuples conjecture): for every M, infinitely many primes p ≡ 1 (8) have no
   window certificate with m ≤ M at ANY cap (e = ∞ included); i.e. every ES^{(y)} solution with p ∤ x has
   x > (p+M)/4. Explicit examples (M = 11: p = 807 330 585 601, …; M = 19: two BPSW-probable primes ≈ 10²²), control
   284/300 live. Scope: p ∤ x; says nothing about positive density.
3. Prop 2.1 / Cor 2.2 / Prop 2.3 (PROVED): uniform (self-generated) certificates classified — cap 0: classical
   p + 4, p + 1, 2^c p + 1, p + 2^c, p² + 2^c; cap ≥ 1: p^j + 4^j (K odd) or p^J + 2^c (K even, incl. j = 2 when K′ is
   a square); p mod 8 forces none; congruence forcing only via fixed small primes of N (classical classes). Odd-order
   witness as above; bounded cap would follow from a correlated Landau-type statement (U) — not a route.
4. Thm 3.2 (PROVED rel. Montgomery's large sieve, PNT in APs, Pollack JNT 2018): #{p ≤ X : e*(p) > (log X)^A/4}
   ≤ X^{2/A+o(1)} and #{p ≤ X : e*(p) > p^ε} ≪_ε (log X)^{⌈4/ε⌉}, exceptional sets explicit (𝒫(y): all q ≡ 3 (4) ≤ y
   are QRs mod p). Routine combination (Linnik-style); weaker in range than CAP_INTERPOLATION Rem 3.2(b)'s sketch.
5. §4 (Assessment): with many generators a deterministic cap needs cancellation of all characters χ² ≠ 1 over the box
   (resonances at χ(s) = ±1 since overflow steps by 2) — a Diophantine-genericity condition on discrete logs; no
   GRH/Chebotarev route seen.
6. §5 (EVIDENCE, Mordell-hard p ≡ 1 (8) ≤ 10⁷, 20 513 primes, exact caps, δ_p incl.): cap-0 rate at forced windows is
   ≈ 2× that at unforced windows within 100-wide q-bins (0.684/0.317, 0.396/0.166, 0.274/0.127); least forced window has
   cap 0 for 85.7 %; every such p has cap 0 at one of its first 20 forced windows (4 need > 10: 3361, 2 782 921,
   7 071 121, 8 925 841); the two explicit discrete-log-free witnesses reach max 10 (≤ 10⁶) and 17 (≤ 10⁷).
   Note: full-family sharpness of CAP_DOWN Prop 4.1(a) fails — p = 593, q = 11: δ_p = 0 slice needs cap 2, δ_p = −1
   gives cap 0 (reviewer's example, rechecked).

## Verdict
(A), (B), (C) not reached pointwise. Goal (A) via windows reduces (conditionally) to growing windows with non-residue
primes from the rough part of K — the B2 lottery; the uniform level reduces to Landau-type events; the forced level is
exactly (q − 3)/4 in the δ_p = 0 slice.

## Sparks (not pursued)
1. **Huge-window congruence coverings at cap C (most promising).** Fix S = primes ≤ y. Prime factors q ≡ 3 (4) of
   S-unit sums a + b (a/b in the cap-C box with b_s = 1) give windows that certify cap ≤ C for the whole class
   p ≡ −q (mod 4P(y)²) (K_q's S-part then fixed). Jacobi (Cor 1.2) forbids only the classes where all s ≤ y are QR mod
   p. A finite computation CovS(y, C) "all other classes are hit" would give e*(p) ≤ C for every p with n₂(p) ≤ y; for
   y = 17 this attacks the undecided lnr = 17 line at cap C ≥ 1 with windows far beyond s7's ≤ 800. Expected
   threshold C(y) ~ y^{2+ε} by counting; CAP_INTERPOLATION Prop 4.1 bounds what is possible (sterility at cap C for
   large r).
2. Extend Lemma 1.1/Thm 1.3 to Type I windows (p | x) to remove the scope gap.
3. Full-family (δ_p ≠ 0) forced worst case at a single window (Prop 4.1(a) fails there; p = 593).
4. Sharpen Thm 3.2(b): a density lower bound |𝒜(N, N^ε)| ≫ N/√log N would give a (log X)^{1/2}-type exceptional set.
5. Quantitative random-factorization model for the forced/unforced cap-0 ratio (§5) with Legendre conditioning.
