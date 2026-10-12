# R158 — hostile review of INVOLUTION_ES.md (O158, branch side-agent/involution-depth)

Reviewer branch `side-agent/review-involution`. From-scratch scripts: `scripts/review_inv_*.py`.
ES is not solved here, and the document does not claim it is.

## Verdict table (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 2.1 | SOUND |
| Lemma 2.2 | SOUND |
| Prop 2.3 (parity) | SOUND |
| Prop 2.3(ii) / summary inference | SOUND-AFTER-REPAIRS (wording; see D1) |
| Prop 3.1 | pending |
| Lemma 4.1 / Prop 4.2 / Thm 4.4 | pending |
| Thm 5.1 / Lemma 5.2 | pending |
| Cor 5.3 | pending |
| novelty / §6 framing | pending |

## Claim-by-claim

### Lemma 2.1, Lemma 2.2, Prop 2.3

Re-derived. `(tu−1)(tv−1) = t(tuv−u−v)+1` gives the A,B form; X(n) is finite (`A,B ≥ t−1`, `A ≥ 1`).
Lemma 2.2: I redid every step. `A = 4δ ≥ 4` (A = 0 would need `0·B = tn+1`); `t | A+1` gives t odd and
`gcd(t,δ)=1`; `tm²+1 ≡ t+1 (mod 8)` gives `t ≡ 3 (4)`, and `t ≡ 7 (8)` if `8 | A`; so `t ≥ 3` and the Jacobi
symbol `(·/t)` is defined. Primes ℓ | δ₀ divide `tm²+1`, so ℓ ∤ tm and `−t ≡ m⁻² (mod ℓ)`: `(−t/δ₀) = 1`
(multiplicativity covers repeated primes). `(4δ/t) = (−1/t) = −1`, and `(2/t)^s = 1`, so `(δ₀/t) = −1`.
Reciprocity with `(t−1)/2` odd gives `(t/δ₀) = −(−1/δ₀)`, so `(−t/δ₀) = −1`. Contradiction. No coprimality
hypothesis is used. **SOUND.** The E→ES map (CONDITIONAL_ES Lemma 1.1 with (g,f,c)=(t,u,v)) was also checked.

Prop 2.3: the fixed points of ρ are `u(tu−2) = q²`. u = 1 gives t = q²+2; u = q needs `q | q+2`; u = q² needs
`q² | 3`. So exactly one, and |X(q²)| is odd. (iii) holds: for odd n, `gcd(u, n/u) | 2` is odd. **SOUND.**

EVIDENCE (`scripts/review_inv_xsets.py 1200 151`, 22 s, independent enumeration through `A | tn+1`):
* Lemma 2.1 parity and the unitary claim hold for all odd n ≤ 1200.
* Every E(n) element, n ≤ 1200, rebuilds to an exact solution of 4/n.
* E(m²) = ∅ for all odd m ≤ 151. |X(m²)| is odd for 69 of the 75 m, including every odd prime.
* Lemma 5.2: 213 E-elements at p ≡ 1 (8), p ≤ 1200; all have `(δ₀/p) = −1`.

Inference in Prop 2.3(ii) and §0 ("no involution family on X with ES-only fixed points, of any complexity,
exists on a square class"). What is actually excluded is **pointwise**: for each odd prime q, *no* involution
of X(q²) has all its fixed points in E(q²), because the set is odd and E(q²) is empty. "Family" and "any
complexity" add nothing. The statement excludes exactly:
* windmills on X that are required to work at some n = q²;
* by Lemma 1.1, windmills on any sets whose certificates do not exist at odd squares, if they are required
  to work at an odd square with `|X| odd`.

It does **not** exclude windmills on X that are defined only for primes, or only for non-squares. Those are
the only ones ES needs, and §5 handles them. The text after Prop 2.3 says this, so the result is correctly
scoped there. The §0 bullet "T1 kills the O152 odd set" overstates it, though: T1 kills only the extension of
the O152 set to square classes. See D1.
