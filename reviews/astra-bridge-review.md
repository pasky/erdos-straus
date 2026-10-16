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

## §4 fixtures — numerics **SOUND**; extraction **incomplete**; the "Reading" is **near-tautological** (m7, m8)

From-scratch `scripts/review_r260_fixtures.py` does its *own* extraction: it regex-scans every Astra *.md for integer
triples (a, b, c), computes N = 4/(1/a+1/b+1/c) and keeps those with N = p·n², p ≡ 1 (4) prime (no use of the author's
data). Result: 94 exact triples overall (56 twist-1, 38 twisted). Comparison with the author's 51:
* all 51 author triples are exact (I confirm); 6 of them are written as equations "4/p = 1/a + …" and so escape my regex
  (I grep-confirmed each in Astra: SOURCE_SELECTION (9) at 2521, TYPEII_MOMENTS l.127 at 3361, SOURCE_SELECTION l.407 at
  233689, FORCED_FACTOR l.207 at 193·47², BIRATIONAL (11) at 1129, SOURCE_SELECTION at 3361);
* **21 exact triples inside the author's own 13 files are missing from the author's "verbatim extraction"**, e.g. 193·5²
  (1207, 2655400, 7218200) and (1224, 84150, 7218200) [STR], 193·2² (200, 5790, 115800) [STR], 193·3² (696, 1160, 251865)
  [TWIST_FLOOR_CERTIFICATE_GATEWAY], 2521·11² (94540, 394460, 2883857614) and the 2521 exit (652, 18908, 23833534)
  [GATEWAY_COMPATIBILITY], 5209·7² (63945, 30309930, 31576885074) [BIRATIONAL], and ES points at p = 13, 73, 281, 349,
  8353, 8737, 13633 [SOURCE_SELECTION, BIRATIONAL]. So "re-checks every numeric triple" is true of the extraction file only.
* Spot re-verification against Astra text: 5209 e = 31, H = 40370 = 2·5·11·367, r = 550 = 11·50, 4·550+1 = 31·71 [STR §19.2
  (70)–(71)] ✓; 15241 exit (3813, 5315322, 871084114): H = 57154, e = 15, r = 15·3813 − 57154 = 41 ✓; 193 e = 7 (H = 338)
  and Type II w = 7, 15 ✓; borrowing rule (67) quoted correctly in §5.3 ✓.
* "Only one twisted fixture is a Claude ES^{(y,e)} point (193·5², (1218, 152250, 699625))" — **survives** on my larger set
  (`scripts/review_r260_capcheck.py`: every other twisted point has an even root, a non-square denominator, two
  non-integral coordinates, or a radical dividing no integral coordinate).
* Levels/windows of the twist-1 points in the 13 files on my extraction additionally include Type I e = 11 (p = 13) and
  e = 23 (p = 73, 13633), and Type II w = 3 (p = 349): the "25 of 30 … e ∈ {3,…,143}, 5 … w ∈ {7,15,39}" census is of the
  incomplete list; the qualitative "small modulus" observation survives (max level 143 in scope).

**Tautology (m8).** For a prime p every ES solution has p dividing exactly one or two denominators, hence is Type I at
the level e = (4H − 1)/p (automatically ≡ 3 (4)) or Type II at the window w = 4x − p. So "every Astra exit is a
classical … ET certificate" is true of *every* ES solution of every prime and carries no information about Astra; only
the word "small" (an observation on ≈ 30 points) does. Thm 2.1's memorylessness is the real content and is proved.

## §1 slot dictionary (Def 1.1, Lemmas 1.2, 1.3, table) — **SOUND** after R-O249

Re-derived: {m : m²x, m²y, m²z ∈ ℤ} = τℤ, so W(pm²) = m²·{points with τ | m}; Lemma 1.2 (den x = den y = 1, den z = r² ⇒ τ = r;
anchor r²z prime to r for r > 1); the window-shot anchor pK(g+1)/(4Q₀²) = p·x·h/Q₀² is [FORCED_FOLD (5)] Z = p(U/c)(K/c)
with Astra's K = (G+1)/4 = Claude's h and c = Q₀ (notation clash: the bridge's K is the window x, Astra's K is the slice h —
harmless but worth a footnote). Lemma 1.3: source identity, C = s + 1, C = m²(4x − p) ✓; scalar-removal remark ✓ (m² | s and
4sh ≡ 1 + s (mod m²) force m = 1). The p = 5, q = 3, m = 5 caveat ✓ (s = 42, h = 1). The repaired scope (sources vs window
shots, not programmes) is correct; the 193·5² point is the unique Claude-capped twisted Astra fixture even on my larger
extraction (above). "[A:STR §11.4] reachable subclass": Astra calls m² | B₁, B₂ "a weaker closed arithmetic property" and
warns "Do not confuse arbitrary coprime-anchor states with either reachable subclass" — the bridge's gloss is acceptable
but should say "Astra's weaker closed class (m² | both non-anchor coordinates)" (m14).

## Prop 3.2, Prop 3.3 — **SOUND**

3.2: q/(ph) = 1/x + 1/z ⟺ x = (ph + d)/q, d | (ph)² (complete parametrisation); shot ⟺ d = Q₀² (q·x = ph + Q₀²) ✓;
−ph ≡ −p/4 ≡ (2m)⁻² (pm² ≡ −1) ✓, asserted for all 125 604 sources in my run; slice-ES brute force over divisors of (ph)²
for all 7697 (p, g) with composite g (1745 carry ES). 3.3(a): odd divisors of (aM)² + Y² with gcd = 1 are ≡ 1 (4) ✓;
(b) Jacobi argument ✓ (numerics above). Wording: "the ES Type II point" in (a) should read "the ES *shot* (surface point)";
it is not a statement about all Type II solutions of a² (m15).

## Prop 5.1 — **SOUND** (label nuance m9)
(K/q) = (p/q) = (q/p) = −1 and (h/q) = (4⁻¹/q) = 1 ✓ (asserted on 4377 admissible (p, q), q ≤ 400). (a) is a *group* statement
(−1 ∈ ⟨primes of K⟩, possibly via 2); the forced ES^{(y,e)} *state* needs CAP_DOWN's (E) — the Transfer paragraph states this
correctly, (a)'s word "forced" should point to it. (b)'s "nothing forces −1 ∈ ⟨primes of h⟩" is an Assessment (no
dead-slice theorem is proved; dead slices are frequent empirically: 5952 of 7697 in my run), not part of the PROVED label.

## Prop 5.2 — **SOUND**
(a) ✓ (gcd(m, s) = 1 automatic; m ∤ ph). (b) ✓: den z exponent 2(a − b)⁺ at all ℓ | Q incl. 2 when gcd(Q, pq) = 1; my run:
4370 least-root shots (p ≤ 3000, admissible prime q ≤ 400) exact with den z = Q₁², Q₁ ≤ (q−1)/2 (max 191); the 7 skipped had
gcd(Q, p) > 1, all with q ≥ 2p; p = 5, q = 103, Q = 30 gives den z = 20 ✓. Pollack IJNT 2014 Thm 1.4 (sources/ PDF read):
"the smallest prime q ∤ f for which ξ(q) ≠ 0 satisfies q ≪ W^{1/4} f^ε", ξ = (1 − χ₋₄)(1 − χ_p) has ξ(0) = 1, W = 4p, f = 4p:
gives p^{1/4+ε} ✓ (ineffective as stated in CAP_DOWN). Typo: the parenthesis "(O249 self-check: …" is never closed.
**Reading (m10, fidelity):** "Astra's 'strict twist decrease' is progress only through its final step" — Astra never presents
the decrease as progress; [STR §11.2] calls (m, C) "a terminating invariant. It is not a theorem that a transition always
exists." The real point (small-twist points are free, so only *availability of moves from every state* matters) should be
phrased as agreeing with Astra's own caveat, not as a correction of it.

## §5.3 macro table, §5.4 heights — **SOUND** (attribution m13)
Quotes checked: borrowing (67) ✓, first pivot (27) ✓, fold (1)–(3) ✓, FORCED_FACTOR "t | m, t² | (p+q)/4 … iff gcd(t,p(p−1))=1"
✓, TWIST_HEIGHT_COMPRESSION Thm 1 (H ≥ r²B(p,r), **p, r distinct odd primes** — the bridge drops "prime r") ✓, FIXED_DEFECT
F_p = ⌊9p⁴/8⌋ ✓, r^{32/11} ✓. §5.4's bound τ²·pUK ≤ τ²p(p+q)(p+q²+q)/(16q) ✓ (K ≤ (p+q²+q)/(4q) from 4Q² < q²).
**Attribution:** Astra [STR §21.2 (78)] already states the n = 1 case of Thm 2.1 ("such an endpoint exists if and only if
there is r | H² with e | 4r+1"), and §11.2 (28)–(30) is the (a)⇒(b) half with "the exact closure gate, necessary and
sufficient". Thm 2.1's genuinely new content is the converse (every point with x-twist n and coordinate pH is a certified
state) and the coset reading. Say so.

## §6 Props 6.1, 6.2, gate table — **SOUND** (labels m11, m12)
6.1 re-derived: for odd e, |ker(x ↦ x²)| = 2^{ω(e)}, so |K| = φ(e)/2^{ω(e)}; (2) gives |K| = ∏ d_i ≤ ∏ (J_{q_i} + 1) ≤
∏_{q | H} (2h_q + 1) = τ(H²) (w_q ≥ 1, v_q(c) ≥ 0); divisor bound + φ(e) ≫ e/log log e: if e ≥ p then e is absolutely bounded,
otherwise e ≤ p^{O(1/log log p)} ✓. From scratch (`scripts/review_r260_sec56.py`): I implemented [SATURATION §2–§3] literally
(w_q, c from v_q(r₀) parity, J_q, a_q = q^{w_q}, all orderings, relative indices) for 80 primes p, all e ≡ 3 (4) ≤ 199
(composite incl.), one certificate r₀ per level: 2243 cases, saturation holds in 156 (max e = 171), φ(e) ≤ 2^{ω(e)}τ(H²) in all.
**m11:** "So the only fully forced Astra exit applies at levels so small …" misdescribes Astra: saturation is *one* forced
mechanism; Astra also has the source-forced macro [STR §16], the prescribed borrowing rule for certificates (31, H, 11)
with 10 | H, i.e. p ≡ 9 (40) [STR §19.2], the forced-factor exit [STR §17.3] and the fold [FORCED_FOLD §2]. Replace by
"saturation, Astra's whole-subgroup forced exit, applies only at …".
6.2 ✓ (cyclic group of order 2·odd; non-residue ℓ has even order ⇒ −1 ∈ ⟨ℓ⟩; −H ≡ −4⁻¹): asserted for 546 (p, ℓ) pairs at
the least admissible prime e. The "Why it does not give a bounded cap" paragraph is correctly labelled Assessment and the
S ∩ G² = S² step (−H/ℓ is a square of an element of ⟨primes of H⟩) is right since G has 2-part of order 2.
**m12:** §6.1 "Each Astra gate is one B2 event" and verdict item 6 carry no label; they are an Assessment (a re-encoding;
the B2 statement of redteam-automorphic-2 Thm 2.2 is about the E1–E6 encodings, not Astra's). The fold-supply row (prime
R | r with R ≡ 3 (4), (C/R) = 1, R < 2 min(m, p)) is a prime-factor/quadratic-residue/size condition, not "a divisor in a
residue class whose modulus is part of the solution"; mark it as such or drop it from the B2 table.

## Summary verdict per claim

| claim | verdict |
|---|---|
| §1 slot dictionary (Def 1.1, L 1.2, L 1.3, table; R-O249 scope) | SOUND (m14) |
| Thm 2.1 | SOUND (m2, m13 attribution) |
| Cor 2.2 | SOUND (m1) |
| Thm 3.1(a),(b) | SOUND |
| Thm 3.1(c),(d) | SOUND (m4) |
| Prop 3.2 | SOUND |
| Prop 3.3 | SOUND (m15) |
| Thm 3.4 | SOUND-AFTER-REPAIRS (m5, m6) |
| conventions Astra q = slice g, s = D, m = 2k | SOUND as coordinates; m3 (twists sit in different coordinates) |
| §4 fixtures: 51 triples exact | SOUND |
| §4 "every exit is a classical small-modulus certificate" + census | GAP (M1: tautology + incomplete extraction) |
| Prop 5.1 | SOUND (m9) |
| Prop 5.2 | SOUND (m10, typo) |
| §5.3, §5.4 | SOUND (m13) |
| Prop 6.1 | SOUND (m11) |
| Prop 6.2 + Assessment | SOUND |
| §6.1 B2 table | Assessment, unlabelled (m12) |
| fidelity to Astra | mostly faithful; m10, m11, m13, m14 |

No FATAL defect. ES is not claimed and nothing in the document claims an infinite case.

## Defects

**MAJOR**
* **M1 (§4 Reading; §7 item 4; AGENT_REPORT item 4).** (i) "Every Astra exit is a *classical* small-modulus ET certificate"
  is a tautology: for prime p every ES solution is Type I at the level e = (4H−1)/p or Type II at w = 4x − p. (ii) The
  census "25 of the 30 twist-1 points … 5 Type II …" is over an extraction that misses ≥ 21 exact triples present in the same
  13 Astra files (list in §4 above; e.g. 193·5² (1207, 2655400, 7218200), 2521·11² (94540, 394460, 2883857614), the 2521 exit
  (652, 18908, 23833534)); with them the level set gains e = 11, 23 and the window set w = 3. *Repair:* replace the Reading by
  "Every ES solution of a prime is Type I or Type II; what Thm 2.1 adds is that the Type I exit at level e depends on the route
  only through one divisor r | H². Observed: all Astra twist-1 exits in these files have level ≤ 143 / window ≤ 39 (EVIDENCE,
  N points)", and either complete the extraction (e.g. a regex pass as in scripts/review_r260_fixtures.py, plus the
  equation-form triples) or say "a sample of 51 triples".

**MINOR**
* m1 (Cor 2.2, Reading, §7.3): "carries an Astra state"/"Astra-alive" = a certificate-satisfying state *exists* (Thm 2.1(b)),
  not that an Astra genealogy reaches it. Add one clause.
* m2 (Thm 2.1): gcd(n, e) = 1 is automatic on side (b) (ℓ | gcd(n,e) ⇒ ℓ | 4r, but r | H² is prime to e); state it, so (b)
  is "all points with x-twist n and coordinate pH".
* m3 (§7 items 1–2; AGENT_REPORT SHARP): "Astra twist = Claude overflow Q₁" and "Astra's twist m is Prop 1.3's 2k" read as
  contradictory. Clean statement: on L_ρ(g) an Astra source (m, 1) has denominator M² (twist in the M-coordinate), a Claude
  shot point (2k, Y) has denominator Y² (twist in the Y-coordinate; 2k is the growing modulus). Moreover a lattice point
  is a *parameter*, not a rational point: at the "meeting point" (2k, 1) the two readings give **different** rational points
  sharing only y = ph — e.g. p = 5, g = 3, (2, 1): Astra's source (7/4, 35, 5) (twist 2) and Claude's ES shot (2, 5, 10).
  Say "ES shots are the parameters where both readings exist", not that the Astra source *is* the ES point.
* m4 (Thm 3.1(d) title "excludes exactly"): the classical line m | 2h is a small part of the non-genuine set gcd(m, h) > 1;
  say "genuineness excludes this line (except m = 2, where every source is ES-ready)".
* m5 (Thm 3.4(c)): "2kρ ≡ 1, i.e. g | 4k²p + 1" — the converse only gives 2k⁻¹ ≡ *some* root; for composite g add "for some
  root branch".
* m6 (Thm 3.4 proof / Prop 1.2 use): note explicitly that EXPONENT_CAP Prop 1.2 is stated for Q odd and that Q = (h/k)Y may be
  even; the valuation argument given covers it (I confirm numerically), so this is a citation-hygiene point.
* m7 (§4 opening): "re-checks every numeric triple" → "every triple of the extraction file" (see M1).
* m8 = M1(i).
* m9 (Prop 5.1): "(a) forced" is a group statement; the forced *state* needs CAP_DOWN (E). "(b) nothing forces" is an
  Assessment inside a PROVED proposition — split the label.
* m10 (Prop 5.2 Reading; fidelity): rephrase "Astra's strict twist decrease is progress only through its final step" as
  agreeing with Astra's own statement that (m, C) is a terminating invariant without a transition-existence theorem
  [STR §11.2]. Also close the unbalanced parenthesis "(O249 self-check: …".
* m11 (after Prop 6.1; fidelity): "the only fully forced Astra exit" → "saturation (Astra's whole-subgroup forced exit)";
  Astra has other forced macros (STR §16, §17.3, §19.2; FORCED_FOLD).
* m12 (§6.1, §7 item 6): label the gate table Assessment; fix or drop the fold-supply row (not a residue-class event).
* m13 (Thm 2.1, attribution): credit [STR §21.2 (78)] (n = 1 case, verbatim the classical criterion) and [STR §11.2 (28)–(30)]
  ((a)⇒(b), "necessary and sufficient" gate); the new part is the converse/coset reading. §5.4: add "r prime" to the
  TWIST_HEIGHT_COMPRESSION hypothesis.
* m14 (Lemma 1.3): "the 'reachable subclass' [A:STR §11.4]" → Astra's "weaker closed arithmetic property" (m² | both
  non-anchor coordinates), which Astra distinguishes from arbitrary coprime-anchor states. Footnote the K-notation clash
  (bridge K = window x; Astra FORCED_FOLD K = slice h).
* m15 (Prop 3.3(a)): "the ES Type II point" → "the ES shot (surface point)".
