# R159 — hostile review of POINTWISE_BINARYFORM.md (O159, branch side-agent/binaryform-identities)

Reviewer: R159. Reviewed commit: merge of `side-agent/binaryform-identities` into
`side-agent/review-binaryform`. From-scratch scripts: `scripts/review_bf_*.py`.
ES is not solved; nothing below changes that.

## Verdict table (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 | SOUND (MINOR framing defect D1) |

## Claim-by-claim

### Lemma 1.1 (square vanishing for N-points)

Re-derived. ψ(k) = (−d/k) is a real character mod 4d, odd (ψ(4d−k) = −ψ(k)). Type I: (2.7)
`ef = 4a²d+1` ⇒ f odd, coprime to 2ad, −d ≡ (2a)^{−2} mod f ⇒ ψ(f) = 1; (2.1) ⇒ gcd(n,d)=1; (2.6)
f ≡ −n mod 4d ⇒ (−d/n) = −1 for n odd. Type II: (2.18) f ≡ −1 mod 4d ⇒ ψ(f) = −1; (2.21) ⇒
(−dn/f) = 1 ⇒ (n/f) = −1, which is impossible for any square n coprime to f (and n is, by
(2.21)). Sign reduction (§1): abd, acd, bcd > 0 ⇒ d > 0 and a, b, c of one sign; e = (a+b)/c > 0;
f > 0 from f = (4a²d+1)/e (I) resp. f = 4acd − 1 (II). Correct.

From scratch: `scripts/review_bf_lemma11.py` enumerates all N-points with a,b,c,d < 40
(38 827 Type I, 250 770 Type II; no gcd restriction) and verifies the ET equations, `(−d/n) = −1`
(Type I, odd n > 1), `(n/f) = −1` (Type II), no square n (Type II, either parity) and no odd square
(Type I, including n = 1); plus the periodicity/oddness of ψ for d < 200. 0 violations.

Framing (D1, MINOR): ET define Σ^I_n, Σ^II_n as *all* nonzero sextuples satisfying (2.1)–(2.9)
resp. (2.13)–(2.21) (ET p. 11), with no gcd(c, n) condition, and ET §4's proof of Prop 1.6 uses only
(2.1), (2.2) and n ≡ 1 (8) for an arbitrary N-point of Σ^I_n. So "ET Prop 1.6 without coprimality"
is not a strengthening; ET §4 already is the N-point statement. The genuinely extra bits are the
Jacobi-symbol refinements `(−d/n) = −1`, `(n/f) = −1` and the Type II case for even squares.

