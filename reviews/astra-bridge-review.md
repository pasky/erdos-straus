# R260 — hostile review of O249 (ASTRA_BRIDGE.md), round 1

Reviewer: R260 side agent (branch side-agent/review-astra-bridge), merged side-agent/astra-bridge at c467ce3f.
Astra (../erdos-straus-astra, d7300f8) read only; no Astra script run. From-scratch scripts: scripts/review_r260_*.py.

(work in progress — sections are filled one claim at a time)

## Thm 2.1 / Cor 2.2 (certified states ⟷ twisted Type I points) — **SOUND** (minor wording only)

Astra's definitions, quoted [STR §11.2 (28)–(30), §11.4]: "For a positive n satisfying `e | n²+4r`, define
`U=(n²H+r)/e, V=n²HU/r, Z=pn²H` … the exact closure gate … is `gcd(n,r)=1`"; "Every accepted cross output carries
an explicit certificate (e,H,r): `eU−n²H=r, gcd(e,n)=1, r | H²`." [SATURATION §2] uses the same certificate
(`eA=m²H+r₀, r₀ | H², gcd(m,e)=gcd(m,r₀)=1`). The bridge quotes these faithfully; (U/n², v, pH) with v = V/n² = HU/r
is the point (U,V,Z)/n² at p.

Re-derivation (mine). (a)⇒(b): 4(n²H+r) ≡ n²+4r ≡ 0 (mod e); r | H², gcd(H,e)=1 ⇒ gcd(r,e)=1; eHU = n²H²+rH ⇒ r | HU;
n²/U + r/(HU) = e/H = 4/p − 1/(pH). (b)⇒(a): r := eU − n²H = HU/v > 0, r | HU, 4r ≡ −n² (mod e); prime ℓ | n: ℓ | U ⟺ ℓ | r;
r | n²H² with gcd(r,n)=1 ⇒ r | H². All steps check. **Extra (not a defect):** the hypothesis gcd(n,e)=1 is automatic on
side (b) (if ℓ | gcd(n,e) then ℓ | 4r, but r | H² is prime to e), so (b) is empty for gcd(n,e) > 1 — confirmed numerically.
Cor 2.2: ⇒ (r/e) = (−1/e) = −1 so a prime s | r | H² has (s/e) = −1; ⇐ r = s, n₀² ≡ −4s, one of n₀, e−n₀ prime to s
(s ∤ e); reciprocity (s/e) = (−1/s)(e/s) = (p/s) = (s/p) for odd s | H; s = 2: 2 | H ⟺ pe ≡ 7 (8), and then
(2/e) = (2/p) (e ≡ 3 (8) ⟺ p ≡ 5 (8)). Parity: (H/p) = (4⁻¹/p) = 1. The "Reading" inclusion Claude-alive ⊆ Astra-alive is
right: Cor 2.2's dead condition is literally CAP_POINTWISE Prop 4.1(b)'s hypothesis (2 | H with (2/p) = 1 ⟺ e ≡ 7 (8)),
and Prop 4.1(b) (with its R238 arbitrary-y remark) kills every point with coordinate pH. Strictness (p=5, e=7, x = 45):
Prop 4.1's arbitrary-y remark applied to D = 7y − 9 gives D = 3^c, and the internal reviewer's c ≡ 5 (6) argument is right
(re-derived: y = (3^c + 9)/7 ∈ ℤ needs 3^c ≡ 5 (mod 7), i.e. c ≡ 5 (mod 6); then v₃(y) = 2, v₃(9y) = 4 and
den z = 3^{c−4} with c − 4 odd). SOUND.

From-scratch check `scripts/review_r260_typeI.py 3000 151 12` (2.7 s): side (b) enumerated **independently** of the
theorem (t = ev − H with t | n²H², which I derive from gcd(Hv, t) | H²; all v, not just those coming from r | H²) for
all p ≤ 3000, **all** e ≡ 3 (4) ≤ 151 including composite, n ≤ 12: side (a) = side (b) as sets of points in all 8018
pairs (40 202 states, 6982 at n = 1), every point exact. Cor 2.2 for prime e ≤ 151: brute-force aliveness over n ≤ 3e
(not assuming the "< e" claim) agrees with the Kronecker criterion (and with the (s/e) form) in all 4009 pairs; least
twist always < e (max 65); the even-multiplicity parity claim holds. Prop 3.3(b): 796 (a², e) pairs (e composite incl.,
gcd(e,a)=1), n ≤ 12: both sides empty.

Minor wording (see defects m1, m2 below): "carries an Astra state" / "Astra-alive" means *a certificate-satisfying state
exists*, not that Astra's genealogy reaches it; and the hypothesis gcd(n,e)=1 in Thm 2.1 can be dropped from (b).
