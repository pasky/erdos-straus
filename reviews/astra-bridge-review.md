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

## Thm 3.1 (a)–(d) (surface Dg = pM² + Y²; ES-ready sources) — **SOUND**

Re-derived. (a) qs = pm² + 1 ⇔ (m, 1) ∈ L_ρ with ρ = m⁻¹ (ρ² ≡ −p); Astra's own source identity [CAMPAIGN "Source and proof
standard": `q | pm²+1, s=(N+1)/q, h=(q+1)/4, 4/N = 1/(sh)+1/(Nsh)+1/(Nh)`, genuine = gcd(m,h)=1, composite q allowed] is
quoted correctly; Astra-genuine gcd(A, m) = 1 ⇔ gcd(h, m) = 1 since qs ≡ 1 (mod m). (b) (1, 2Q) and the Prop 1.3 point
(2k, Q₁): Q₁ − 2kρ = Q₁(1 − 4Q₀k) = −gQ₁ ✓. (c) m even ⇒ 2m | m² ⇒ qs ≡ 1 (mod 2m) ⇒ [s ≡ −1 ⇔ q ≡ −1 (mod 2m) ⇔ m | 2h] ✓;
with k = m/2, Q₀ = h/k, 4Q₀k = g + 1 and 4Q₀² ≡ (2k)⁻² ≡ −p (mod g), so the shot is direct (Prop 1.3's converse is not even
needed); Q₁ = gcd-normalised overflow = 1 ⇒ ES with y = ph. Converse ✓. (d) ✓. Note: **every m = 2 source is ES-ready**
(2 | 2h always): the "m = 2 exception" is the whole classical "4p + 1 has a divisor ≡ 3 (4)" line, genuine iff h odd.

From-scratch `scripts/review_r260_lattice.py 3000 400 400 400` (4 s; /tmp output reproduced in §Numerics below): all primes
p ≡ 1 (4) ≤ 3000, **all** g ≡ 3 (4) ≤ 400 prime to p (composite incl.), m ≤ 400: 125 604 sources exact (matches the author's
count), 62 993 even-m; ES-ready ⇔ m | 2h ⇔ g ≡ −1 (2m) in all; 1193 ES-ready, each gives an exact ES point with y = ph, and
**Prop 1.3's D (= kj − Q₁², computed from the shot) equals Astra's s in every case**; 250 genuine ES-ready sources, all m = 2.
Independently, the set of ES shots (Q₁ = 1) equals the set of ES-ready sources under (Q, g) ↦ (g, 2h/Q) on the common range.

## Thm 3.4 (lattice meeting point) — **SOUND-AFTER-REPAIRS** (minor: m5, m6)

Re-derived both directions of (b) without Prop 1.3: for (2k, Y) ∈ L_ρ, k | h, gcd(Y, 2k) = 1, put Q = (h/k)Y. Then
gcd(2k, g) = 1 (k | h, gcd(h, g) = 1) and 2k·2Q = (g+1)Y ≡ Y ≡ 2kρ, so 2Q ≡ ρ and g | p + 4Q²; gcd(Q, h) = (h/k)gcd(Y, k) = h/k,
so Q₀ = h/k, Q₁ = Y, Prop 1.3's k equals k. Forward: gcd(Q₁, k) = gcd(Q/Q₀, h/Q₀) = 1. Denominator: z = p·x·h/Q² with
g·x = ph + Q² (ℓ ∤ pg for ℓ | Q) gives den exponent 2(a − b)⁺ at every ℓ including 2 (same as [FORCED_FOLD §2 "Exact
normalization, including the prime 2"]) — correct, and needed, because EXPONENT_CAP Prop 1.2 is stated only for Q odd while
here Q₀ = h/k may be even. Discriminant: basis (1, ρ), (0, g) gives ((p+ρ²)/g)u² + 2ρuv + gv², disc −4p ✓.

From-scratch check (same run): **all** shot data (Q, g), Q ≤ 400, enumerated directly from g | p + 4Q² (not from the lattice):
125 248 shots, all exact; for the 78 764 with odd overflow, (2k, Q₁) ∈ L_{2Q}, gcd(Q₁, 2k) = 1, den z = Q₁² exactly, Prop 1.3(b)
and D ≡ −Q₁² (4k) hold, and "ES^{(y,e)} ⇔ rad Q₁ | h" agrees with a direct test of EXPONENT_CAP Def 1.1 (odd square
denominator, prime to p, radical | y; cap = max v_ℓ(Q₁)); independently enumerated lattice points (2k, Y), all roots ρ,
Y ≤ 400, map **bijectively** onto exactly these shots (set equality, root branch preserved). Even overflow (46 484 shots):
den z = Q₁² exactly in every case (so the scope note's "(2, 2) not primitive" shots are Astra even-twist states, as stated).
1193 ES shots.

Conventions vs EXPONENT_CAP Prop 1.3 (brief's question): **Astra's q is Claude's slice g** (y = ph = p(g+1)/4) — yes;
**s = D** — yes, literally (above); **twist m = 2k** — only as a *coordinate*: on L_ρ an Astra source has denominator M² = m²
(the twist is the M-coordinate) whereas a Claude shot point has denominator Y² (the twist is the Y-coordinate; 2k is the
"growing modulus", not a twist). So the two programmes twist *different lattice coordinates*; see m3.
