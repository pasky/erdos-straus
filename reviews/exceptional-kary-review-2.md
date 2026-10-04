# Second hostile review: EXCEPTIONAL_KARY.md (headline Thm 4.5)

Reviewer: side-agent/review-kary-2. Subject: branch `side-agent/kary-comparison`
at `e35bf60` (includes Lemma 4.2′). First review:
`side-agent/review-kary:reviews/exceptional-kary-review.md` (all SOUND, ETw
inputs taken on trust). This review re-derives the ETw inputs from scratch,
re-derives KARY Thm 2.5 / Thm 4.1, and sanity-checks the headline.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered E1, E2, …
(E-prefix to avoid clashing with the first review's D-numbers.)

## Part 1 — ETw inputs, re-derived, and their use in KARY

### 1.1 ETw Lemma 1.3 (QR base) and Lemma 1.1 / Cor 1.2 — SOUND

* Lemma 1.1 re-derived: `A = (M+1)/4`, `gcd(A,M) = gcd(A,4A−1) = 1`; `D = sr²`,
  `D | A² ⇔ sr | A` (s squarefree), so `4s | M+1`. `(−4D|M) = (−1|M)(s|M) = −(s|M)`.
  For odd s, `M ≡ −1 (mod 4s)` gives `(M|s) = (−1|s)` and reciprocity with
  `(M−1)/2` odd gives `(s|M) = (−1|s)(−1)^{(s−1)/2} = 1`. For `s = 2s'`,
  `8 | M+1` ⇒ `(2|M) = 1`. Hence `(−4D|M) = −1`. Correct.
* Cor 1.2: n a nonzero QR at every `p | M` ⇒ `(n|M) = 1 ≠ (−4D|M)`. W-smooth
  Case-B moduli are odd, so only odd `p ≤ W` matter; `R_W` imposes exactly that.
* Lemma 1.3(2): the factor at odd `p^e ∥ Q₀` keeps `p^{e−1}(p−1)/2` of `p^e`
  residues; at `p = 2` nothing is imposed. `log(Q₀/|R_W|) = Σ_{3≤p≤W} log(2p/(p−1))`,
  independent of Q₀ and of the family. (3): a single class mod `p^e` has
  probability `≤ 2/(p^{e−1}(p−1)) = γ(p)/p^e`. CRT product ⇒ independence.
* Use in KARY: base term `O_B(1)` once `W = W₀(B)` is fixed; (R1) for the
  W-smooth classes; (R2) feeds Γ. Q₀ may be arbitrarily large (powers of small
  primes from the family's W-smooth parts) without affecting either. Within
  hypotheses.
