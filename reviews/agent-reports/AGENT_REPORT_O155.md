# AGENT REPORT O155: breakthrough-technique transfer audit (brainstorm)

Branch `side-agent/bs-technique-transfer`. There are 3 memos and 2 scripts, and nothing LIVE. ES is not
solved, and no case of it is.

**`BRAINSTORM/technique_transfer_list.md`: all COLLAPSE.** It screens 18 techniques:
* Maynard–Tao; Zhang/BFI; entropy decrement; Matomäki–Radziwiłł; Green–Tao; Helfgott-style tail;
  Guth–Maynard; restricted digits.
* Hooley/DFI; square sieve; Friedlander–Iwaniec/Heath-Brown; Kahn–Kalai/Park–Pham; GHS pretentious;
  expansion/AQUE/Pila–Zannier/DGH; slice rank/Kelley–Meka/sensitivity; Bhargava; motivic; Iwaniec P₂.

Each one fails at a named step. The unifying reason is the **1/|θ| law**: at fixed p, every dyadic block of
any slice parameter holds O(polylog p) expected winners. A technique transfers only if it can lower-bound a
sum whose main term is polylog(p) at one p.
* Every averaging technique either averages over p (B6/T7) or needs the target set to have density
  (log)^{−O(1)} in its variable (B3).
* The closest one remains Friedlander–Iwaniec bilinear input (H-B), still with no technology.
* Square-sieve aside: the avoider set contains the square classes but is not known to be contained in
  them (B1).

**`BRAINSTORM/tech_maynard_theta.md`: COLLAPSES (B3 at "error ≤ main"; reduced form = H-A).** Strongest
reason (Remark 1.2): ES needs m = 1 success. For m = 1, Maynard–Tao's multidimensional weights are
irrelevant, because they improve the ratio S₁/S₀, which matters only for m ≥ 2. The transfer therefore
reduces to a plain first moment over θ at fixed p, which is H-A.
* Maynard's density hypothesis fails: the success density is X^{−1+o(1)}.
* Weights are congruence conditions on θ. They cost a factor M and gain only 1.5–2.6 (measured, M = 5, 15,
  105).
* T1: the genus-blind asymptotic is the step that is false at odd squares.
* By-products:
  * Lemma 1.1 (PROVED, elementary, essentially folklore): R(p) = #{4AB | p+A+B} = #{(A,C): 4AC−1 | p+A} =
    #{(A,C): 4AC−1 | 4Cp+1}.
  * EVIDENCE: flat per-dyadic-block counts (6 primes near 10⁹), consistent with (log 2/4)·log(p/H²).

**`BRAINSTORM/tech_smooth_level.md`: COLLAPSES (B6 pointwise; (D)24 cap for exceptional sets).** Strongest
reason: a level of distribution beyond 1/2 enters a CRT majorant only via its level λ ≤ A·log N. The (D)24 cap
log(1/Eν) ≤ Cλ^{3/4} then changes only the constant, never the 3/4 exponent. Smoothness is irrelevant to the cap.
* EVIDENCE: the (A)3 subsystem restricted to N^{0.4}-smooth moduli leaves 25 of 9732 primes p ≡ 1 (24)
  ≤ 10⁶ uncovered, against 9 with all moduli.
* No new partial theorem.

*Not done:* no extra exotic sub-memo. No candidate survived long enough to warrant one.
