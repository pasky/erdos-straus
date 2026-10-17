# s8_numerator_size_screen — where is the 4-specific step? (O258 item (vi), relay from O257 Thm 2.6)

**Idea.** O257 (NONCONG_LIFTS §5 Thm 2.6, read-only on side-agent/noncong-lifts) separates k = 4 from every 4 | k ≥ 8 at the
point x_{ℓ,2} by the size inequality b₀(k − 4/g) ≤ 3, not by reciprocity. Screen the other 4-specific arguments, and ask
whether an ES proof could be "k-uniform machinery + one numerator-size inequality".
**Literature.** NONCONG_LIFTS Thm 2.6, §2.3–2.4; (J)57 FOUR_ADIC_INPUT Thm 1.3, Prop 1.4; (J)41 □-relaxation and its
Pomerance–Weingartner thresholds; Mordell's identities (Mordell 1969, ET §1); Schinzel 2000.
**Key observation (PROVED, trivial, surely classical).** For 4 | k: k/n = 1/x + 1/y + 1/z ⟺ 4/n = 1/((k/4)x) + 1/((k/4)y) +
1/((k/4)z). So **the numerator-k model is ES restricted to solutions with (k/4) | gcd(x, y, z)**. In ET coordinates
(N_θ = k·abd): k-witnesses are exactly the 4-witnesses with (k/4) | d. At a fixed slice (a, b, c), the k-condition differs
from the 4-condition only at the primes of k/4 (and the extra power of 2). The size bound e = (a + b)/c ≤ a + b is k-free.
**Screen.**
* Thm 2.6 (x_{ℓ,2}): the inequality is the conjunction of a LOCAL condition at the primes of k (x ≡ 1 there forces
  e ≡ −1 (mod kab₀)) with the k-free size bound e ≤ a + b. Read 2-adically: at x_{ℓ,2} the Mordell witness (1, 6, e = 7) has
  d = (x + 7)/24, a 2-adic unit, so d is odd and the witness never lifts to k = 8. "Archimedean" and "2-adic parity of d" are
  two readings of one step; neither is reciprocity (agreeing with O257).
  Generalisation (`s8_xlr_points.py 60`): at x_{ℓ,r} the covered non-residues are mostly r ≡ −(small) (e.g. k = 4, ℓ = 17:
  covered r = 10, 11, 12, 14 ≡ −7, −6, −5, −3; uncovered 3, 5, 6, 7). The inequality concerns the least residue e of the CRT
  lift, not the size of r. Coverage thins quickly with k (k = 16: for ℓ ≤ 37, ℓ ∤ k, only ℓ = 29 has covered non-residues,
  r = 14 and 27).
* (J)57 Fano pigeonhole: the 4-specific step is 2-adic ("4 costs no bit, each further power of 2 costs one"). Its EVIDENCE
  "at 131 and 241 every entry divisible by 4 has v₂ exactly 2" is the same statement as "every solution of 4/131, 4/241 has an
  odd denominator" (`s8_even_denominators.py`: 32 resp. 8 solutions, 0 all-even; at non-exceptions, e.g. 233: 9 of 19).
* Mordell's identities: fixed slices; for k they cover the refined classes (k/4 | d), a 1/(k/4) share. The 4-specific
  resource is *completeness* (O257 §2.4), a covering count — size in the density sense, not in Thm 2.6's sense.
* (J)41 □-relaxation: no 4-specific step at all (a theorem for every M ≡ 0 (4)). Its thresholds p ≳ M² are archimedean,
  but they separate p from M, not 4 from 8.
**Can a proof be "k-uniform + one size inequality"? (Assessment.)** Two readings.
(a) Threshold form "k/p solvable for p > P₀(k)" (Schinzel-type). For k = 8 this implies ES above P₀(8) ≥ 241, because 8/p
⟹ 4/p. So the k-uniform statement is strictly STRONGER than ES and buys nothing.
(b) Step form: the k-dependence of any witness-producing argument enters exactly as the extra condition (k/4) | d. A proof
"spends" its 4-specific step by producing a witness while asserting nothing about d mod 2 (or about gcd(x, y, z)). The model
exceptions locate where this is unavoidable: at 131, 241, 17, 11, … every ES solution has an odd denominator. At 2-adically
square primes near the T1 point, this coincides with my §1 2-adic reading on MP(p) (b = 1 ∪ c = 1 fails only where all
v₂ ≤ 1). So the inequality must be spent on the **2-adic valuation of the cofactor d** (equivalently v₂(p + e) = v₂(4ab)
exactly). A k-uniform argument whose only 4-specific input is a size inequality must therefore be one where size controls
v₂(d) — as at x_{ℓ,2}, where the size inequality leaves only witnesses with d a 2-adic unit.
**Cheap numerics.** `s8_xlr_points.py 60` (k ≤ 24, ℓ < 40, a ≤ b ≤ 60): reproduces Thm 2.6(b) (k = 4 covers r = 2 exactly at
ℓ = 3, 5; no k ≥ 8 covers r = 2 at any ℓ ∤ k). `s8_even_denominators.py`: #(8/n solutions) = #(all-even 4/n solutions) at
9 test n.
**Assessment.** PROVED dictionary (numerator model = ES with (k/4) | gcd) + Assessment. Not sharp: it relocates O257's
inequality to 2-adic information on d, which (J)57 already treats as the 4-specific resource. No new lever.
