# R191 — hostile review of FIXED_MODULUS_SHOTS.md (O191)

Reviewer: R191 side agent. Documents: FIXED_MODULUS_SHOTS.md, BRAINSTORM/bsN_divisor_box.md, reviews/agent-reports/AGENT_REPORT_O191.md
(as merged from side-agent/fixed-modulus-shots). All checks below use from-scratch code `scripts/review_fms_*.py`; the
author's `scripts/fms_*` were not used.

## Summary verdicts

(filled in progressively; see §§ below)

## A. Lemma 1.1 (Type II certificate cube) — SOUND

Re-derivation. 4cdj ≡ 1 (mod h) makes 4cd, 4dj units; 4cd(pj + c) ≡ p + 4c²d and 4dj(pj + c) ≡ 4dj²p + 1, so the three
divisibilities are equivalent. e·h = p + 4c²d with h ≡ −1 (mod 4cd) gives p + e ≡ 0 (mod 4cd); x + c²d = cdj·e from
4(x + c²d) = e(h + 1); then 1/y + 1/z = (x + c²d)/(p·cdj·x) = e/(px) = 4/p − 1/x. The bound: h ≤ pj + c gives
4cd ≤ p + (c + 1)/j ≤ p + c + 1, hence 3cd ≤ p + 1; so p ∤ c, d, p ∤ e, p ∤ x. Converse as written is correct (I
re-did it with D = ey′ − x, DD′ = x²). The map cube → solutions is **not injective** (points (bs, D/(b²s²), as) for every
s with s² | D/b² give the same solution); the text's "from at least one cube point" is accurate.

From-scratch check (`scripts/review_fms_cube.py 3000 1500`, 5 s): independent divisor-method Type II solver (ordered
(y, z)), itself validated against a fully naive triple loop for p ≤ 70. For **all 428 primes 5 ≤ p ≤ 3000** the set of
cube solutions equals the brute-force Type II set exactly; at every cube point the three divisibilities hold, p ∤ x,
3cd ≤ p + 1, and the triple is an exact solution. For p ≤ 300 a **wide** scan (all cd ≤ 2p, ignoring the 3cd ≤ p + 1
cut) finds no further cube point.

## B. Lemma 4.1 (Type I cube) — SOUND-AFTER-REPAIRS (minor)

Algebra re-derived: 1/y + 1/z = 4/p − 1/x ⟺ u(4vwf − p) = pv + f. Converse correct. Brute force (independent solver
enumerating the smaller of y, z in (p/4, 2p/3]) vs cube along (w, f), wf ≤ 2p/3: **identical ordered Type I sets for
all 237 primes 5 ≤ p ≤ 1500**; at every enumerated point with gcd(g, p) = 1 the divisibilities g | pv + f and
g | 4v²w + 1 agree. Non-Type-I cube points (p | uvwf) give genuine (Type II) solutions, as claimed.
Defect m1 below (hidden hypothesis in the three-way equivalence).

## C. Prop 6.1 (finiteness, O(p²)) — SOUND

Type II: x ≤ p/2 (else 1/y′ + 1/z′ > 2 — the text's route via y′ = 1 is also fine). The text's "both y′, z′ ≤
x(x + D)/(eD)" is not literally true for the chosen order (if D > x then y′ = (x + D)/e > x(x + D)/(eD)); the correct
statement is max(y′, z′) = x(x + D_min)/(e·D_min) with D_min = min(D, D′) ≤ x (DD′ = x²), ≤ x(x + 1)/e — same bound
(defect m2). f(e) = (p + e)(p + e + 4)/(4e) is convex on (0, p], f(1) = (p+1)(p+5)/4 > f(p) = p + 2, so
h ≤ (p+1)(p+5)/4 − 1. Type I: wf ≤ 2p/3, g ≤ p² + 4wf² ≤ 25p²/9 < 3p². Numerics: max h/((p+1)(p+5)/4) → 1, the
bound (p+1)(p+5)/4 − 1 is **attained** at 217 of 428 primes ≤ 3000 (all p ≡ 3 mod 4: e = 1, D = 1); max g/p² = 1.33
(p = 7), so the Type I constant 3 is loose but correct.

## D. Thm 2.1 (affine shots) — SOUND; Cor 2.2 — SOUND; Cor 2.4 — SOUND

Re-derived line by line. (a): the three cube points are correct (gcd(h, αβ) = 1 is what lets h pass from αp + β to
the primitive line form). (b): from h | pj + c, h | αp + β: h | αc − βj; c, j ≤ (h+1)/4 ≤ h/3 (h ≥ 3) gives |m| ≤ μ/3.
I re-expanded jX = m − αc (⟺ βj − αc = m(4cjt − 1)) and XY = 4m²t − αβ — both correct. Case 4m²t ≠ αβ: |X|, |Y| ≤
4m²t + αβ, |Y| ≥ 4|m|tj − α, |X| ≥ 4|m|ct − β give c ≤ |m| + β(α+1)/4 ≤ μ/3 + μ(μ+1)/4 ≤ μ² (true for μ ≥ 1) and the
same for j; |X| ≤ |m| + αc gives t ≤ (α + β + |m|)/4 ≤ 7μ/12 < μ; hence h < 4μ⁵. Cases X = 0 / Y = 0 (forced when
4m²t = αβ) give exactly the D- and E-members of 𝓜. Quantifiers: the sporadic bound depends only on μ = max(α, β), so
for each FIXED (α, β) there are finitely many sporadic h; nothing is uniform in α, β beyond that, and the text does not
claim more (C2 caveat is correct). Note the D- and E-alternatives are mutually exclusive (16DE = 1), so |𝓜| ≤ 1 + τ(H)
(the stated 1 + 2τ(H) is a harmless over-count).
Numerics (`scripts/review_fms_affine.py 40 60000`, own 𝓜, certification computed from the definition αc ≡ βj (mod h),
cj | (h+1)/4): 979 coprime pairs, all h ≡ 3 (mod 4) ≤ 6·10⁴ coprime to 2αβ: (a) never fails; 5766 (b)-exceptions,
all < 4μ⁵, max h/μ² = 8.50 at (α, β, h) = (37, 38, 12275); none on the three lines (trivially: for 1 ∈ 𝓜 every
h ≡ 3 mod 4 is covered by (a)). Pairs with 1 ∈ 𝓜: exactly (1,1), (1,4), (4,1). M ≥ √H/2 holds for all pairs.
Cor 2.4: δ ≤ Σ_{M∈𝓜} 1/φ(4M) is legitimate (upper density of 𝒞 ∩ {r ≡ −1 mod 4M} ≤ 1/φ(4M); finitely many sporadic
r and r | αβ discarded); H₀ depends on δ only (absolute constants in τ ≪ H^ε, φ(n) ≫ n/log log n). Sound.

## E. Cor 2.3 (three modulus-4 shots) and its EVIDENCE — SOUND (scope wording: m4, m5)

The Dirichlet construction (h prime, ≡ 3 mod 8, ≡ 1 mod every odd q | M, h > 4μ⁵) is correct, and 1 ∈ 𝓜 ⟺
β/α ∈ {1, 4, ¼} (c²|D = c forces c = D = 1). Recount (`scripts/review_fms_three.py 1000000`, own sieve; each firing
turned into an explicit cube solution and verified by 4xyz = p(xy + yz + zx)): 78 496 primes 5 ≤ p < 10⁶; failures
p+1 / p+4 / 4p+1 = **10 438 / 9 841 / 18 992**; joint **942** (first 193, 673, 2377, 2473, 2521, 3217), all ≡ 1 (mod 4);
all 499 odd squares 9 ≤ m² < 10⁶ fail all three. **Every figure reproduced exactly.**

## F. Remark 2.5 (p/h) = −1 — SOUND

Re-derived: h ≡ −1 (mod 4n) ⇒ (n/h) = 1 (for odd n′ | n, (n′/h) = (h/n′)(−1)^{(n′−1)/2} = (−1/n′)(−1)^{(n′−1)/2} = 1;
(2/h) = 1 for even n as h ≡ 7 mod 8) and (−1/h) = −1. gcd(c, h) = gcd(j, h) = 1 since cj | (h+1)/4. Numerically
every Box((r+1)/4), r < 10⁶ prime, consists of quadratic residues (`review_fms_box.py`: 0 exceptions).

## G. Thm 3.1, Thm 4.2 — SOUND (Thm 4.2 Type I bullet: m3); Cor 3.2 — GAP (MAJOR M1: false incomparability claim)

Thm 3.1 is an immediate rewrite of Lemma 1.1 (h | pj + c ⟺ −p ≡ c/j, j a unit since j | k). Statistics recomputed
(`scripts/review_fms_box.py 1000000`): for primes r ≡ 3 (mod 4), 7 ≤ r < 10⁶ (39 321 primes; the text's 39 319
presumably starts at r = 19 — m6), mean |A_r| = 77.4, max 1977 at r = 942 479, max density 0.0646 (r > 10³),
0.0081 (r > 10⁵): reproduced. The "14 to (median) 1092 times larger … on a sample" figure is not reproducible from the
text (sample unspecified — m6).

**Cor 3.2 / bsN / report SHARP 2 — the ES box is always INSIDE the ES^{(S)} residue set.** The first and third bullets
are correct as statements about exponent vectors. But the text then claims "Neither set contains the other in general
(R-O191: r = 11, S = {3}, … p = 43 has −p ≡ 1 certified by ES only)", bsN says "incomparable sets", and the report's
SHARP 2 says "the sets are incomparable". As **residue sets** (which is what certification depends on) this is false:

*Claim (PROVED here).* Let r ≡ 3 (mod 4) be prime, k = (r+1)/4 an S-unit, G = ⟨S⟩ mod r. Then Box(k) ⊆ 4G² (the
ES^{(S)} set of O186 Prop 2.1), i.e. every p certified by ES at r is certified by ES^{(S)} at r.
*Proof.* For cjt = k: c/j ≡ 4cjt·c/j = 4c²t (mod r). By Remark 2.5's computation (r ≡ −1 mod 4t) (t/r) = 1. Since
r − 1 = 2·odd, G ∩ (F_r^*)² = G² (G² ⊆ G ∩ squares, and [G : G²] = 2 iff |G| even iff −1 ∈ G iff G ⊄ squares). t ∈ G
(S-unit), so t = s², s ∈ G, and c/j ≡ 4(cs)² ∈ 4G². ∎ (Per certificate: ES point (c, t, j) ↦ ES^{(S)} Q ≡ cs.)
This is also just O186's own remark "every ES solution is an ES^{(S)} solution", read at one prime.
The document's own example refutes itself: at r = 11, S = {3}, G = ⟨3⟩ = {1, 3, 9, 5, 4} (odd order), 4G² =
{1, 3, 4, 5, 9} ⊇ Box(3) = {1, 3, 4}; and p = 43 IS certified by ES^{(S)} at r = 11: Q = 27 ∈ ⟨3⟩, 43 + 4·27² =
2959 = 11·269. The "only {3, 4}" in the text comes from imposing |e| ≤ 1 on the ES^{(S)} exponent — an artefact of the
chosen representation (1 = 3⁰ ≡ 3⁵ has an odd-exponent representative), not a property of the residue set.
Numerics: for all 1135 primes r ≡ 3 (mod 4), r < 2·10⁴, with S = primes of k, Box(k) ⊆ 4G² — 0 exceptions.
Also: O186's ⟨S⟩ is the *monoid* (Q ∈ ℤ_{>0}), so the per-certificate ES^{(S)} vector satisfies e_q = 2s_q − κ_q ≥ −κ_q,
not "no bound" (harmless at the residue level, where monoid and group images coincide).
Consequence: the corrected dictionary is *strict inclusion* A_r ⊆ −4G², with |A_r| ≤ τ₃(k) vs |4G²| ≍ |G| —
the size contrast (the actual point of §3) survives and is strengthened; only the "incomparable" sentences are wrong.

Thm 4.2 (Type I bullet): the ⟸ direction produces an ES solution which is Type I only if p ∤ uvwf (otherwise it is a
Type II solution); the text says so only in a parenthetical after "⟺" (m3).

## H. Thm 6.2 (scope), §5 labels, Remark 2.5/Cor 2.3 wording — SOUND-AFTER-REPAIRS (minor)

(i) is exactly Thm 2.1 + Cors 2.2–2.4 for Type II divisors of a fixed-coefficient affine form; (ii) Thm 3.1/4.2; (iii)
Prop 6.1. The scope paragraph is accurate and honest (p-dependent coefficients, degree ≥ 2, Type I affine shots,
multi-prime conditions excluded; (ii)–(iii) flagged as size statements, not impossibility). The "Reading" is labelled
Assessment. §5 outcomes are declared Assessments unless citing a theorem; C1/C3/C4/C7 cite Thm 2.1/Cor 2.2/Cor 3.2/
Prop 6.1 correctly; C2/C6 are honestly left open. C3's "needs ord_r(q) ≤ 2v_q + 1" holds for |S| = 1 (with more primes
the box could contain ⟨q⟩ via mixed vectors; still O(polylog)), fine as an Assessment.
