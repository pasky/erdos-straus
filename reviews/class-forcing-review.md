# R272 — hostile review of O263 (CLASS_FORCING.md, branch side-agent/class-forcing @ ec15ff50)

Reviewer scripts: `scripts/review_r272_*.py` (from scratch; author's z33 scripts not reused). ES is not solved.

## Summary verdicts (filled in progressively)
| claim | verdict |
|---|---|
| Thm 6.1 + Hypothesis HC | **FATAL as stated** (HC is false; Thm 6.1's conclusion is false) — SOUND-AFTER-REPAIRS with the D1 repair |

## Defects

**D1 (FATAL) — §6, Hypothesis HC and Theorem 6.1: the compatibility condition only controls Ω ∩ ℚ(ζ_M); the abelian
part of Ω can force a congruence p ≡ a (mod q) at a prime q > B that kills admissibility / creates a certificate.**
Counterexample (checked in `scripts/review_r272_thm61_cex.py`): D = 1, B = 6 (≥ 4D + 2), q = 7 > B, Ω = ℚ(ζ₇),
C = Frob class of p ≡ −4 ≡ 3 (mod 7). Since 7 ∤ M, Ω ∩ ℚ(ζ_M) = ℚ, so C is "compatible with p ≡ 1 (mod M)" in the
sense of Thm 6.1 (and primes p ≡ 1 (M), p ∈ C exist: 15552001, 33696001, …). But for every p ∈ C, 7 | p + 4 and
7 ≡ −1 (mod 4): w = 7 is a certificate at d = 1 (exact ES solution (x,y,z) = (a, 2ap, 2p), a = (2p+1)/7, verified for
all 1497 such primes p < 2·10⁵). So (i) the conclusion "infinitely many p ∈ C with no certificate at levels ≤ D" is false,
and the "Consequently no theorem of the form 'every prime with Frob_p|Ω ∈ C has a certificate at level ≤ D' exists for
such C" is false (here it does exist, trivially). (ii) HC itself is false as stated: take f₀ = 1 + Mk, f₁ = (f₀ + 4)/s₁,
Ω = ℚ(ζ₇), C as above; the system is admissible and C is compatible with f₀ in HC's sense, yet 7 | f₁(k) whenever
Frob_{f₀(k)} ∈ C. The proof of Thm 6.1 hides this: "admissibility" is checked for the forms alone, never for the forms
restricted to the k-classes selected by C|_{Ω ∩ ℚ^{ab}} (conductor primes > B).
*Repair.* (a) Restate HC with the correct local condition: let Ω₀ = Ω ∩ ℚ^{ab}, of conductor m; C|_{Ω₀} selects a set
A ⊂ (ℤ/m)^×; require some k₀ with f₀(k₀) mod m ∈ A such that the system {f_i(k₀ + m j)}_j is admissible. (b) In Thm 6.1
require B ≥ every prime dividing the conductor m of Ω₀ and e_q ≥ v_q(m), and "C compatible with p ≡ 1 (M)" to mean
C|_{Ω₀} = {1} (Ω₀ ⊂ ℚ(ζ_M)). Then the proof goes through (k-classes selected by C are k ≡ anything mod primes > B), and
the honest reading is: *Frobenius data = its abelian (congruence) shadow + a non-abelian part; the congruence part is B1
and may well cover whole classes (as above); only the non-abelian part is (conditionally) useless.* §9's verdict bullet
and AGENT_REPORT ("for every finite Galois Ω and class C compatible with p ≡ 1 (M)") must be amended accordingly.
