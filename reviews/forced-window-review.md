# R264 — hostile review of O252 (FORCED_WINDOW.md, BRAINSTORM/z24_*.md)

Reviewer: R264 side agent (branch side-agent/review-forced-window). Reviewed commit: merge of side-agent/forced-window
(O252 checkpoint 1, after self-review R-O252). From-scratch scripts: `scripts/review_r264_*.py` (no author code reused).
Status: COMPLETE (round 1).
**Repairs applied (author quiet since checkpoint 1):** D1–D5, D7–D12 applied to FORCED_WINDOW.md, each marked "(R264 repair)"
(D6 as an "R264 remark"); z24 memos and AGENT_REPORT_O252 not edited (z24_crt_shortfall still says "cap ≍ log log p", D4).

## Summary verdicts

**Lemma 1.1 (parity split) — SOUND.** Re-derived: p ≡ 1 (8), q ≡ 3 (8) ⇒ K odd; (K/q) = (p/q) = (q/p) = −1 ⇒ (c/q) = −1,
t = −c ∈ U_q; δ_s = −ε_s + 2j_s has δ_s ≡ b_s (2), δ_s ≥ −1 ≥ −b_s, and δ_s ≤ b_s + 2e exactly by the j-range, so δ_s ∈ D_s(e).
D_s(e) matches CAP_DOWN Lemma 1.1 via δ_s = c_s − b_s (c_s ≤ 2b_s, or c_s even with overflow (c_s − 2b_s)/2 = i). From scratch
(`review_r264_prop21.py 20000 300`): for every p ≡ 1 (8) ≤ 2·10⁴ and every forced q ≡ 3 (8), q ≤ 300 (4 580 pairs) the least
parity-box cap was found, δ checked in D_s(e), and the ES^{(y,e)} solution x = K, y = pA, z = pKA/d rebuilt with exact rationals
(den z = r², r odd, v_ℓ(r) ≤ e, rad r | y). "Sufficient only" confirmed: p = 241, q = 11 reproduced (W₀ = {1, 5, 9} ∌ 4); 133 of
the 4 580 pairs have parity-cap > 0 although cap(q) = 0.

**Prop 1.2 (Fourier criterion) — SOUND.** Standard; |Σ_{j≤L} e(jθ)| ≤ 1/|sin πθ| ≤ 1/(2‖θ‖) (sin πx ≥ 2x on [0, ½]).
Random test (3 000 boxes in ℤ/n, n odd ≤ 400): criterion fired 59 times, W = G every time. Note the hypothesis "odd order" is
not used. **Prop 1.3 — SOUND** (pigeonhole on the character torus; |W| ≤ ∏(L_i + 1)).

**Prop 2.1 (cap-0 certificates = least-residue events) — SOUND.** Re-derived: m ≤ u + v ≤ uv + 1 ((u−1)(v−1) ≥ 0) < 4uv and
uv ≥ max(u, v) ≥ (u+v)/2 ≥ m/2; converse: gcd(u, r) | gcd(u, u+v) = 1, r ≡ 3 (4), primes of K_r ∤ r unless = p. Exhaustive
from-scratch check (`review_r264_prop21.py`): for every prime p ≡ 1 (4) ≤ 2·10⁴ the three window sets (A) brute-force Type II
solutions 4/p = 1/x + 1/(py′) + 1/(pz′) with m = 4x − p, (B) windows with a cap-0 δ-box certificate, (C) residues
r = (−p mod 4uv) with r | u + v over ALL coprime (u, v), uv < p/2, coincide; all 50 958 certificates satisfy gcd(u,v) = 1,
uv | K, m | u+v, m = (−p mod 4uv), 4uv ≥ 2m. (A) also confirms "cap 0 = honest Type II": every Type II solution has window
m < p and is a box certificate. The "Reading" (no main term for least-residue events) is Assessment and correctly labelled.

**Prop 2.2 (decoupling at cap ≥ 1) — SOUND** (with a MINOR wording point, D2). δ_s = j = b_s + 2i at b_s = 1 gives
i = (j−1)/2; s ∥ K ⟺ 4s | p + q, s² ∤ p + q. The parenthetical "prime factors of Φ_{2j}(s) above 4s² occur" checked:
none for j = 3 (s < 400), and e.g. j = 5: s = 13, q = 2411 > 676; j = 7: s = 3, q = 547 > 36 (`review_r264_misc.py`).


**Thm 3.1 (covering needs a box of window size) — SOUND.** (a) the Jacobi coset of −1 has φ(m)/2 elements (m ≡ 3 (4) is never
a square); (b) 2b+1+e ≤ (2b+1)(e+1), ω(n) ≤ (1+o(1)) log n/log log n, limsup log τ(n²)·log log n/log n = log 3; the o(1)
depends on n only, so the bound is uniform in e as repaired; (c) re-derived: log φ(m) ≥ (θ − o(1)) log p and K ≤ p give
log(3(e+1)) ≥ (θ − o(1)) log log p. The cap-0 statement and "m = p^{2/log log p} is uncoverable" follow (log 3 < 2). Windows
m > 3p: correct but vacuous at cap 0 (Prop 2.1: cap-0 windows are < p).

**Thm 3.2 (CRT in a window interval) — SOUND-AFTER-REPAIRS** (D3). Main statement re-derived: P(y) ≤ h consecutive K contain a
multiple of P(y); gcd(m, p) = 1 as 0 < K < p; F_e ≥ 3(e+3)^{π(y)−1} (s = 2 has no overflow); threshold
log(e+3) ≥ (1+o(1)) log log h. Only the parenthetical about m ≥ h is wrong (D3).

**Cor 3.3 (CRT shortfall) — SOUND as labelled (PROVED inequality + Assessment).** Ratio (A/log 3)·LL : A·LL/log(A·LL)
= log(A log log p)/log 3 ≍ log₃p/log 3 ✓. Random-model count: f(A) = A − (α log α − α + 1) with α = A/log 3 is maximal at α = 3,
A = 3 log 3, f = 2 ✓ (Selberg–Sathe for ω is uniform for α ≤ any fixed constant). Caveat D3: the CRT window need not be ≍ h
(it can be ≍ h/log h); the shortfall factor is unchanged to leading order.

**Prop 4.1 (covering ⟺ balanced lattice up to 2; Minkowski floor) — SOUND.** (i) Λ + B_L is closed (Λ discrete, B_L compact),
so μ ≤ 1 gives Λ + B_L = ℝ^S; x − λ ∈ L/2 + B_L is an integer point of ∏[0, L_s] ✓. (ii) ⌊x⌋ ≡ j (mod Λ) with
j ∈ ∏[0, L_s], so x ∈ ∏[0, L_s + 1) + Λ, a translate of (max (L_s+1)/L_s)·B_L ✓ (needs integer L_s ≥ 1, as repaired).
(iii) |W_L| ≤ ∏(L_s+1); k ≤ (1+o(1)) log q/log log q for ∏S ≤ q; ((q−1)/2)^{1/k} ≥ (log q)^{1−o(1)} ✓.

**Prop 4.5 — SOUND.** Index 2: forcing gives some s | K with (s/q) = −1; a non-square g = −u (u ∈ U_q of odd order n′) has
g^{n′} = −1, so −1 ∈ ⟨S⟩ ✓. det Λ_± = |⟨S⟩|/2 ✓. "Probability ≈ τ(K²)/q" is Assessment (order of magnitude; the random-model
value is τ(K²)/|⟨S⟩|).

**Hypothesis W (as repaired) — not false as far as I can determine; not ES in disguise.** I tried to falsify the p-dependent
version: (1) the class a mod 8P (q ≡ 3 (8), q ≡ −p (P)) is reduced (p > y) and does not determine χ_p(q) (p ∤ 8P), so the
candidate set is non-empty under GRH (count re-derived, below). (2) The class can force structure: if p ≡ −1 (mod s) then every
candidate has q ≡ 1 (mod s), so s | |U_q| and an "all generators are s-th powers" obstruction becomes possible; but by Kummer
disjointness (ℚ(ζ_s, S^{1/s}) ∩ ℚ^{ab} = ℚ(ζ_s)) this has relative density ≈ s^{−k} inside the class, and the class contains
≫ φ(8P) log⁴p/log X candidates — no structural kill found (even for p ≡ −1 (mod P), where |U_q| is divisible by P for all
candidates). (3) Unlike the first version, no CRT choice of p empties the candidate set, since X(p) grows with p. W is
stronger than what Thm 4.3 needs (D6: discrete covering W_L = U_q suffices). W ⇒ only
e*(p) ≤ L − 1, never cap 0, so it is not ES in disguise. It is however NOT known to follow from GRH (the P-loss is real: the
unbalanced primes are not Chebotarev-controlled at the needed level) — the document says so.

**Thm 4.3 (CONDITIONAL on W) — SOUND.** Checked every step the brief asked for: p ≡ 1 (8), q ≡ 3 (8) ⇒ K_q odd ✓; P odd,
q ≡ −p (P) ⇒ P | 4K ⇒ P | K ✓; (q/p) = −1 ⇒ q forced, (K/q) = (p/q) = (q/p) = −1 ✓ (valid also for q > p; X(p) can exceed p
when y ≍ log p); q ∤ K (else q | p) ✓; q ∤ P automatic (q | P and P | p + q would give q | p) ✓; Lemma 1.1 with j_s = 0 off P:
δ_s = −ε_s admissible ✓; on P, ⌊(b_s + ε_s)/2⌋ ≥ 1 for b_s ≥ 1, so j_s ≤ L is within cap e = L − 1 ✓; target −c ∈ U_q includes
the odd-exponent primes of the uncontrolled cofactor, and Prop 4.1(i) covers ALL of U_q, so no control of the cofactor is
needed ✓; gcd(K, p) = 1 ✓, so CAP_DOWN Lemma 1.1 gives the ES^{(y,L−1)} solution. From scratch
(`review_r264_thm43.py 300000 20000 1`): 4 356 pairs (hard p ≤ 3·10⁵, every admissible q ≤ 2·10⁴, y = 7), certificate built from
generators 3, 5, 7 only with sides L_min(q), cap ≤ L_min − 1 in all cases, exact ES rebuild.
*GRH count paragraph* — SOUND: χχ_p is non-principal mod 8Pp; under GRH ψ(X, χχ_p) ≪ √X log²(8PpX) (imprimitivity costs
O(log X·ω(8Pp))); with y ≤ log p, log(8PpX) ≤ (5 + o(1)) log p, so √X = √C φ(8P) log²p beats φ(8P)·log²(8PpX) for C absolute ✓.
It is correctly NOT a hypothesis of the theorem.

**Cor 4.4 — SOUND as labelled (CONDITIONAL on W; exponent at random-lattice L is Assessment)**, with D7. Arithmetic re-derived:
y = LL·LLL, log P = (1+o(1))y, log X = 2y(1+o(1)) + 4LL + O(1) = 2y(1+o(1)) since LL = o(y); k = π(y) − 1 ~ y/log y;
exp(log X/k) = y^{2+o(1)} = (log log p)^{2+o(1)} ✓; (log k)^{O(1)} = y^{o(1)} ✓; y ≤ log p ✓. Optimality within the method:
exponent (2 + 4LL/y)·log y forces y/LL → ∞, so 2 + o(1) is the best this W gives; the "2" is the price of X ≈ φ(8P)² (a
Linnik-type X = φ(8P)^{1+ε} would give 1 + ε, matching the floor). The ℓ^∞ covering radius of a Haar-random lattice of
covolume D in dimension k is D^{1/k}·k^{o(1)} (lattice covering density k^{O(log log k)}, Rogers), so the stated
(log k)^{O(1)} is harmless; whether relation lattices of primes behave like random lattices is the Assessment content.
*Floor (log₂p)^{1−o(1)}*: CAP_INTERPOLATION Prop 4.1 checked on main — it is a statement about covering at a single prime window
with generator product ≤ r for p ≡ 1 (mod 8∏_{r≤R} r), matching the use here ✓.
*"GRH alone reaches only exp(O(√(log₂p log₃p)))"* — GAP in wording (D8): this is the best GRH-conditional bound in the campaign
(CAP_INTERPOLATION Thm 4.2(b), whose mechanism is a global count of short-relation primes (3B)^{k+1} log P against the class main
term x/φ(4P) — i.e. the P-loss, as stated), not a barrier theorem about GRH.

**Prop 5.1 (GRH ⇒ every element is ∏_{s ≤ C log⁴q} s^{δ_s}, δ ∈ {−1,0,1}) — SOUND (relative to GRH for Dirichlet L-functions
mod q).** Re-derived: Σ_{δ∈{−1,0,1}} χ(s)^δ = 1 + 2 Re χ(s) is real, and |1 + 2cos 2πθ| ≤ 2 for ‖θ‖ ≥ 1/6 (value 2 at 1/6,
0 at 1/3, −1 at 1/2) ✓; mass bound: ½(X − L_g) + 2L_g ≥ 0.98X ⇒ L_g ≥ 0.32X (stated 0.31X, fine) ✓;
(q − 2)(2/3)^{0.31X/log X} < 1 ⟸ X/log X > log q/(0.31 log 1.5) ≈ 7.96 log q ✓. The log⁴q comes only from needing
√X log²(qX) ≤ X/50, consistent. The input ψ(x, χ) ≪ √x log²(qx) under GRH is standard (Davenport, *Multiplicative Number
Theory*, Ch. 20); I could not check the MV §13.1 pointer against the book. Literature: consistent with (and quantitatively a
bounded-exponent strengthening of) Bach's GRH generation bound (least prime outside a proper subgroup < 2 log² q; recalled, not
re-checked) and with Erdős–Rényi (≈ log₂ q random generators suffice in the random model); I know of no published statement
that contradicts or supersedes it, but did not search exhaustively.

**Prop 5.2 (GRH for Dedekind zetas + Lagarias–Odlyzko: i.o. q ≡ 3 (4) with all primes ≤ c_ℓ log q log log q ℓ-th powers) —
SOUND-AFTER-REPAIRS (MINOR D9).** i ∉ M since [M : ℚ(ζ_ℓ)] is an ℓ-power and i ∉ ℚ(ζ_ℓ) ✓; Frobenius = generator of Gal(L/M)
gives q ≡ 3 (4), q ≡ 1 (ℓ), all s ∈ S ℓ-th powers ✓; such q is unramified, hence q > y ✓; ℓ | (q−1)/2 so ⟨s²⟩ ⊊ U_q ✓;
infinitely many q since for fixed q the property fails for large y ✓. The least-prime bound under GRH is
Lagarias–Montgomery–Odlyzko (1979) / Bach–Sorenson (explicit (4 log d_L + 2.5 n_L + 5)²), not "Lagarias–Odlyzko" (1977, the
density theorem) — citation precision only. The discriminant line is wrong as written (D9) but the conclusion survives. This is
the ℓ-th-power analogue of Montgomery's GRH result n₂(q) ≫ log q log log q i.o.; worth citing as such.

**"Forcing–generation gap" (PROVED pieces + Assessment) — SOUND-AFTER-REPAIRS (D10, wording).** "generation … holds for all q
only from y ≍ log² q on" should read "is known (GRH, Bach) from y ≍ log² q on"; failure is proved (under GRH) only at
c log q log log q.

**§5 literature screen — SOUND as Assessment, partially re-checked.** Re-checked: Lichtman arXiv 2211.09641 Thm 1.1 (read from
the arXiv PDF): "For fixed nonzero a ∈ ℤ and β > 15/(32√e) = 0.2843 … P⁺(p − a) ≤ x^β" — fixed shift, as the document says ✓;
the abstract confirms Baker–Harman's 0.2961 (secondary confirmation only). Elsholtz–Tao (sources/): Type II = p | y, z, p ∤ x,
as used ✓. NOT re-checked (no source access in this run): Soundararajan 2008, Harper 2012, Matomäki–Radziwiłł 2016,
Friedlander–Granville 1989, BGK, Shkredov, Burgess/Ankeny/Bach, Erdős–Rényi 1965, Montgomery–Vaughan. The "Konyagin–Shparlinski
type" bullet names no specific result (D11). The screen's conclusions are structural (scale mismatches) and do not depend on
fine constants, so these omissions do not affect any PROVED claim.

**§6 numerics (EVIDENCE) — SOUND (all headline figures reproduced from scratch).** `review_r264_leastwin.py 10000000 400 500`
(full rerun, 15 s, output data/review_r264_leastwin_1e7.txt; supersedes the ≥ 2 000-prime sample): all 332 180 primes
p ≡ 1 (4) ≤ 10⁷ have a cap-0 window ≤ 107; **record m₀ = 107 at p = 8 803 369** ✓ (K = 2 200 869 = 3²·11²·43·47,
9·43·47 = 18 189 ≡ −1 (mod 107) ✓); m₀ = 3 for 296 430 = 166 169 forced + 130 261 unforced ✓; hard-prime histogram identical to
the document's (20 513 primes) ✓; kinds U/F/C = 15 266/4 145/1 102 ✓; means Ω, ω, u, log τ(K²) at m₀ vs all scanned windows
(including m₀) = (3.61, 3.08, 1.93, 3.61) vs (3.12, 2.60, 1.65, 3.07) ✓; per-kind success rates reproduced bin by bin; forced
windows with τ(K²) ≥ 4m: 2 133 tries, 5 failures ✓; 665 exact Type II rebuilds. Certificate statistics depend on WHICH
certificate is recorded (D12): minimising over all certificates at m₀, max|δ| ≤ 1 holds for 99.9 % (all) / 98.5 % (hard)
and support ≤ 2 for 99.8 % / 96.9 % (support 1: 92.9 % / 62.8 %) — stronger than the stated 97 %/90 %, 99 %/91 %, 92 %/58 %, so
the qualitative claim stands. Balance (`review_r264_balance.py`): y = 7: 1 012 primes, 23 non-generating, ρ quantiles
1.079/1.241/1.449/2.037/3.462/6.432, all 48 classes hit, max over classes of min ρ = 1.3718 ✓; y = 11: 4 451 primes,
27 non-generating, quantiles 1.132/1.296/1.449/1.776/2.551/5.746, all 480 classes, max-min ρ = 1.4715 ✓ — exact agreement.
T1 control (`review_r264_t1.py`): 499 odd squares, windows ≤ 200, no cap-0 certificate ✓ (positive control p = 241 fires).

**Labels and §7 verdict — SOUND.** Every PROVED item re-derived; Thm 4.3 correctly CONDITIONAL on W (GRH only sizes the
candidate set, not a hypothesis); Cor 4.4 correctly "CONDITIONAL on W + Assessment for the exponent"; Prop 5.1/5.2 correctly
relative to GRH (Dirichlet / Dedekind); numerics EVIDENCE. §7(C) checked against CAP_BOUNDED Lemma 3.1 on main
(e*(p) ≤ (q₃(p) − 3)/4; relative density 1 − 2^{−π(4C+3;4,3)} among p ≡ 1 (8) by independence of the quadratic characters) ✓.
No claim of ES or of an infinite case of ES. Memos z24_*: consistent with the main file; the "ET family s | jp + 1,
s ≡ 3j − 1 (4j)" in z24_budget_not_mechanism checked (j = (s+1)/m) ✓; z24_crt_shortfall inherits D4.

**Overall: SOUND-AFTER-REPAIRS (12 MINOR defects, no FATAL/MAJOR).** The sharp headline (Thm 4.3 + Cor 4.4: W ⇒
e*(p) ≤ (log log p)^{2+o(1)}) is a correct conditional theorem; W as repaired is not refutable by the CRT trick that killed
the first version, I found no other falsification, and it is not ES in disguise (it only yields cap ≤ L − 1).

## Defects

No FATAL and no MAJOR defects found. All PROVED claims re-derived; all headline numerics reproduced from scratch.

**D1 (MINOR, notation; §0 Notation and Lemma 1.1).** Lemma 1.1 says "K odd (q ≡ 3 (8))"; this needs the standing p ≡ 1 (8).
*Repair:* "K odd (q ≡ 3 (8), p ≡ 1 (8))".

**D2 (MINOR, Prop 2.2 wording).** "needs only s ∥ K" — s ∥ K is *sufficient* (any odd b_s ≤ j also works, with smaller cap
(j − b_s)/2). *Repair:* "s ∥ K suffices".

**D3 (MINOR, Thm 3.2 last parenthetical; also Cor 3.3 "m ≍ h").** "smaller than the CRT window m itself whenever m ≥ h, which
happens for a positive proportion of residue classes of p mod 4P(y)": the least CRT window is (−p mod 4P(y)) < 4P(y), so when
h ≥ 4P(y) (which happens, since only P(y) ≤ h < P(y)·y⁺ is known) NO class has m ≥ h (`review_r264_misc.py` (3): proportion 0
at h = P(y)y⁺ − 1, 0.75 at h = P(y)). *Repair:* "m ≥ P(y) for ≈ 3/4 of the classes of p mod 4P(y) (m is the least positive
residue of −p mod 4P(y)); the cap-0 box 3^{π(y)} = h^{o(1)} is smaller than m whenever m ≥ h^ε, i.e. for 1 − o(1) of the
classes". In Cor 3.3 replace "m ≍ h" by "m ≥ h^{1−o(1)}"; the shortfall factor is unchanged.

**D4 (MINOR, §0 (F2), Reading after Cor 3.3, z24_crt_shortfall).** "the deterministic covering scale is cap ≍ log h" / "Cap ≍
log log p is exactly where box size meets window size": Thm 3.2 gives log(e + 3) ≥ (1 + o(1)) log log h, i.e.
e = (log h)^{1+o(1)}, not e ≍ log h. *Repair:* write "cap = (log h)^{1+o(1)}" (resp. "(log log p)^{1+o(1)}").

**D5 (MINOR, notation clash, Thm 4.3).** "ES^{(y,L−1)} solution" uses y in the EXPONENT_CAP sense (the solution variable,
rad r | y) while §4 uses y for the prime bound of S(y). *Repair:* "an ES^{(·,L−1)} solution (EXPONENT_CAP Def 1.1 normalisation)"
or rename the prime bound Y.

**D6 (MINOR, Def 4.2 / Hypothesis W is stronger than needed).** The proof of Thm 4.3 uses only the discrete covering
W_L = U_q (box ∏[0, L]); μ_L ≤ 1 is merely sufficient for it (Prop 4.1(i)) and by Prop 4.1(ii) loses up to a factor 2 in L.
*Repair (optional):* define (y, L)-balanced as "W_L = U_q" (this is exactly what §6's L_min tests), or note that W can be
weakened so.

**D7 (MINOR, Cor 4.4 quantifier).** "L ≍ ((q−1)/2)^{1/k}·(log k)^{O(1)}" makes L depend on q, but W(y, L) fixes L = L(p)
before q is chosen. *Repair:* "L(p) := ⌈(X(p)/2)^{1/k}(log k)^{A}⌉ for a fixed A" (since q ≤ X(p) this is at least the
random-lattice size for every candidate q).

**D8 (MINOR, overclaim in wording; §4 Reading after Cor 4.4).** "this is why GRH alone reaches only exp(O(√(log₂p log₃p)))
… and not (log₂p)^{2+o(1)}" reads as a barrier for GRH. *Repair:* "this is why the GRH method of CAP_INTERPOLATION Thm 4.2(b)
(global count of short-relation primes against the class main term) reaches only exp(O(√(log₂p log₃p))); no GRH barrier
below that is claimed."

**D9 (MINOR, Prop 5.2 proof, discriminant).** "log d_L ≤ [L:ℚ]·log(4ℓ∏S)·O(1)" is false as written: L/ℚ is wildly ramified
at ℓ (and 2) and the standard bound is log d_L ≤ n_L(Σ_{p ram} log p + log n_L) (Hensel/Serre), whose n_L log n_L term is
n_L·π(y) log ℓ ≫ n_L(y + log ℓ) for large ℓ. The conclusion survives with c_ℓ depending on ℓ: log log d_L = π(y) log ℓ +
O_ℓ(log y). Also cite the least-prime bound as Lagarias–Montgomery–Odlyzko 1979 (explicit: Bach–Sorenson 1996), and note the
ℓ = 2 analogue is Montgomery's GRH lower bound for n₂(q). *Repair:* replace the line accordingly.

**D10 (MINOR, wording; §5 "forcing–generation gap", (F5)).** "generation of U_q by primes ≤ y holds for all q only from
y ≍ log² q on" — generation is *known* (GRH, Bach) from ≍ log² q; that it fails between c log q log log q and log² q is not
shown. *Repair:* "is known for all q (GRH, Bach) from y ≍ log² q on".

**D11 (MINOR, §5 screen).** "Konyagin–Shparlinski type 'every residue is a short product of small primes'" cites no specific
result; and Soundararajan 2008, Harper 2012, Matomäki–Radziwiłł, Friedlander–Granville, BGK, Shkredov, Bach, Erdős–Rényi,
Montgomery–Vaughan are recalled, not checked (the AGENT_REPORT says so for some, not all). *Repair:* give exact references or
mark the bullet "(recalled; not re-checked)"; the conclusions are structural and unaffected.

**D12 (MINOR, §6 certificate statistics depend on the recorded certificate).** "max |δ_s| = 1 in 18 498/20 513", "support 1 in
11 807", "All primes: max|δ| = 1 in 97 %, support 1 in 92 %" are statistics of the certificate the script happens to record
(not specified). Minimising over all certificates at m₀ (from scratch): max|δ| ≤ 1 in 98.5 % (hard) / 99.9 % (all); support 1 in
62.8 % / 92.9 %; support ≤ 2 in 96.9 % / 99.8 %. *Repair:* state the selection rule, or quote the existence figures (which
strengthen the claim "the budget is not the mechanism").
