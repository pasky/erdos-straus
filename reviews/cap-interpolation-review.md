# Hostile review R237 of O234 — CAP_INTERPOLATION.md (+ BRAINSTORM/z10_*.md, AGENT_REPORT_O234)

Reviewer: R237 (side-agent/review-cap-interp). Status: round 1, in progress.
From-scratch scripts: `scripts/review_r237_*.py`; outputs `data/r237/`. Author scripts were NOT reused.

## Summary verdicts

| claim | verdict |
|---|---|
| Prop 5.1 (exact dictionary 𝒟_e(M)) | SOUND (both directions re-derived; exhaustive check M < 1500); scope sentences in Cor 5.2(i)/Prop 5.3 need repair (D2) |
| T1 for 𝒟_e(M) | SOUND |
| Cor 5.2 (dimension e + 3, no tower) | SOUND-AFTER-REPAIRS (D2 scope) |
| Prop 5.3 | SOUND-AFTER-REPAIRS (D2 scope) |
| Thm 3.1 (ceiling "at ANY cap, incl. e = ∞") | **GAP/FALSE as interpreted** (D1): the inequality is correct for the *truncated* family V < ℓ/4, but that family is not "the largest class family of this architecture"; with the full 𝒟_e(ℓ) the prime-modulus large sieve gives a POWER saving at e = ∞ (and at e ≥ (log N)^{1+ε}) |
| Input (G) (Gallagher Thm 7) | SOUND-AFTER-REPAIRS (D3: statement/range mis-quoted; the consequence used is valid) |
| Lemma 1.1 (Rankin lower bound) | SOUND |
| Prop 1.2 (uniform cube supply) | SOUND-AFTER-REPAIRS (D3: add log T ≥ √log x to the hypotheses) |
| Remark 1.3 (exactness unnecessary) | SOUND (special case of Prop 5.1) |
| Thm 2.1 (uniform in e ≤ log log N) | SOUND-AFTER-REPAIRS (D3, D4 minor); label "PROVED rel. (G) + BV + LS" correct |
| Thm 3.1 inequality itself (truncated family) | SOUND |
| Prop 4.1 (covering barrier, Linnik) | SOUND (method-scoped; D5 on the "same scale" Reading after D1) |
| Thm 4.2(a) (GRH, e*(p) ≤ C_ε(log p)^{2+ε}) | SOUND-AFTER-REPAIRS: re-derived; CONDITIONAL is the right label once the Lagarias–Odlyzko error term and the disjointness are written out (D6); no downgrade to Assessment needed |
| Thm 4.2(b) (GRH, exp(O(√(log₂p log₃p)))) | SOUND-AFTER-REPAIRS (parameters re-checked; relies on PHASE_DIAGRAM Thm 5.1 Steps 2–4 incl. the R209/R210 negative-exponent shift, which must be cited explicitly, D6) |
| KARY3 consistency | SOUND (no contradiction) |
| (further claims) | see below (to be filled) |

## Claim-by-claim

### Prop 5.1 — SOUND

Re-derivation (independent). Hypotheses M ≡ 3 (4), A = (M+1)/4, p prime, p ∤ DM, p ≡ −4D (M).
EM = p + 4D and M ≡ −1 (4) give E ≡ −p (4), so x = (p+E)/4 ∈ ℤ_{>0}; x + D = E(M+1)/4 = EA, whence
1/y + 1/z = (x+D)/(pxA) = E/(px) = (4x − p)/(px) = 4/p − 1/x. ✓
Valuations at s | D, t = v_s(D) ≥ 1, σ = v_s(A): s ≠ p; s ∤ M (else s | p); v_s(E) = 0 (s odd: s ∤ p + 4D; s = 2:
p + 4D odd). σ = 0: v_s(z) = −t, s ∤ y — forbidden. 1 ≤ σ < t: v_s(x) = σ, v_s(z) = 2σ − t. σ ≥ t: v_s(z) ≥ σ ≥ 0.
Primes s ∤ D: v_s(z) ≥ 0. Against Def 1.1 (ℓ ∤ 2n, ℓ | y, v even, ≥ −2e) this is exactly the stated predicate; s = 2 is
allowed only with t ≤ 2σ. ✓ e = 0: D | A², which is the 3/4 note's ℛ(M) (paper/es-threequarter-note.tex l. 1290–1300,
even D included, matching v₂(D) ≤ 2v₂(A)). ✓

Converse / scope (re-derived). Let (x, pA, z) be ANY ES^{(y,e)}(p) solution with y = pA. Put M := 4A − 1 and
D := pxA/z. From 1/z = 4/p − 1/x − 1/(pA): D = xM − pA ∈ ℤ, D > 0 ⟺ z > 0, and p + 4D = M(4x − p), so
p ≡ −4D (M), E = 4x − p and x = (p+E)/4. Hence **every** solution with p | y, written y = pA, is of the displayed form,
and Prop 5.1 applies iff p ∤ DM; p | D ⟺ p | xM, so the exact scope is "y = pA with **p ∤ x and p ∤ M = 4A − 1**".
Solutions with p | M do exist and are genuine ES solutions outside 𝒟_e (e.g. p = 5, A = 4, M = 15: 4/5 = 1/2 + 1/20 + 1/4,
D = 10; p = 3, A = 1: 4/3 = 1/2 + 1/3 + 1/2). See D2.

From-scratch check (`scripts/review_r237_dict.py 1500`, `data/r237/dict.txt`):
* Part A: all M ≡ 3 (4), M < 1500; all D < M coprime to M PLUS all D = ∏_{s|A} s^{t_s}·f^{t_f} with t_s ≤ 2σ+2e+2
  (e = 3) and one foreign prime f (D ≤ 10¹²); two primes p ≡ −4D (M) each; e = 0, 1, 2, 3; Def 1.1 tested with exact
  rationals and sympy factorisation of den z: **6 965 312 / 6 965 312 agreements** (51 990 in-family (D, e) pairs).
* Part B (converse): all primes p < 60, A < 40, all x ≤ 3pA, e ≤ 2: every ES^{(y,e)} solution with y = pA, p ∤ x,
  p ∤ M has D = xM − pA ∈ 𝒟_e(M) and reproduces (x, y, z): 336 pairs, 0 failures; 203 with p | x and 347 with p | M
  lie outside the hypothesis (as they must).

### T1 for 𝒟_e(M) — SOUND
Re-derived: D = f²d, d squarefree; odd t forces the branch t ≤ 2σ, so d | A; for odd q | d, (q/M) = (−1)^{(q−1)/2}(M/q)
= (−1)^{(q−1)/2}(−1/q) = 1; 2 | d ⇒ 2 | A ⇒ M ≡ 7 (8); so (−D/M) = (−1/M) = −1 and gcd(4D, M) = 1, hence −4D is a
non-residue mod some prime of M. Check: `review_r237_dict.py` t1(1500, 3): 3200 classes (D < M/4, e = 3), Jacobi and
brute-force square search, 0 failures.

### Cor 5.2, Prop 5.3 — SOUND-AFTER-REPAIRS (D2)
Local count N(σ, e) = 2σ + 1 + e at odd s (t ∈ [0, 2σ] ∪ {2σ+2, …, 2σ+2e}) and 2σ + 1 at s = 2 ✓; Dirichlet series
ζ^{e+3}H ✓; the lower bound via D = c₀²d₀R² (injective: d₀ = squarefree part, c₀ = rad of √(D/d₀)) and c₀d₀ | A ⇒
D ∈ 𝒟_e(M) ✓. Prop 5.3 (z ∈ ℤ ⟺ D | A² inside 𝒟_e) is immediate from the valuation table ✓. Only the scope wording is
wrong (D2).

### Input (G) — Gallagher's Theorem 7: checked against the source; SOUND-AFTER-REPAIRS (D3)
Source obtained: GDZ scan of Invent. Math. 11 (1970) 329–339 (LOG_0035), OCR excerpt in
`data/r237/gallagher1970_thm7_ocr.txt`; pp. 337 read as an image. **Actual statement (Thm 7, eq. (29)):**
Σ_{q≤Q} Σ*_χ |Σ_{x<p≤x+h} χ(p) log p| ≪ h·exp(−a log x/log Q), **provided x/Q ≤ h ≤ x and exp(log^{1/2} x) ≤ Q ≤ x^b**;
the q = 1 term is read as Σ log p − h; if there is an exceptional zero 1 − δ of L(s, χ′) (δ log Q ≤ d) the χ′-term is
read as Σ χ′(p) log p + hξ^{−δ} (the exceptional character is NOT omitted; its secondary main term is subtracted).
Differences from (G): (i) Gallagher has a lower bound Q ≥ exp(√log x) instead of the "+exp(−c₁√log x)" term with
1 ≤ T; (ii) short-interval form (x, x+h] instead of ψ(x, χ); (iii) the exceptional term is modified, not dropped.
The consequence actually used in Prop 1.2 is nevertheless VALID: with h = y, x = y (dyadic (y, 2y]), Q = T, for q ≤ T with
q₁ ∤ q every χ mod q is induced by a distinct non-exceptional primitive χ* of conductor ≤ T, and χ(p) = χ*(p) for
p > T, so |θ(2y; q, a) − θ(y; q, a) − y/φ(q)| ≤ φ(q)^{−1}·C y exp(−a log y/log T): relative error C e^{−a log y/log T},
the φ(q) cancelling (the author's key observation is right). Dropping one term of a sum of non-negative terms is fine.
The range condition T ≥ exp(√log x) holds in Prop 1.2 iff u/(10(e+1)) ≳ √u, i.e. u ≳ 100κ² — true in Thm 2.1 (u ≥ e^{C₄}κ²
log(κ+2)) but not stated in Prop 1.2's hypothesis u ≥ 40(C₂+1)κ² (D3). T ≤ x^b holds since log T/log x ≤ 1/(4κ).
Exceptional modulus: Gallagher's exception is relative to Q (region (26)/(27)); χ₋₄, χ_{±8} have a fixed zero-free
neighbourhood of 1, so for T ≥ T₀ the exceptional conductor has odd part > 1, and dropping one prime s₁ of it from 𝒫'
makes q₁ ∤ 4m for all admissible m ✓.

### Lemma 1.1 — SOUND
Re-derived line by line: F_Z ≥ F(σ) − Z^{−σ/2}F(σ/2); log(F(σ/2)/F(σ)) ≤ κΣ_p p^{−1−σ/2}(1 − p^{−σ/2}) ≤ κ(1 + O(σ) +
E₁(1) + O(1)) = C₂κ; σ = 2(C₂κ+1)/log Z gives F_Z ≥ (1 − e^{−1})F(σ); log(1 + w) ≥ w − w²/2, Σ_{p>κ} p^{−2} ≤ 1/κ, Mertens
for Σ_{p≤κ} 1/p and ≤ 1/3 for the excluded prime. All uniform in κ ≥ 1 and in σ ∈ (0, ½].

### Prop 1.2 / Remark 1.3 — SOUND (after D3)
Validity of each class: D = V = c₀²d₀R² with c₀d₀ | K, v(R) ≤ e satisfies Prop 5.1's predicate (s | d₀: t = 1 ≤ 2σ;
s | c₀: t = 2 + 2ρ even ≤ 2σ + 2e), so Remark 1.3 is a special case of Prop 5.1 and needs no separate proof; its
valuation table agrees with mine. Supply: ω_e(ℓ) ≥ Σ_{m ≤ Z, 4m | ℓ+1} κ^{ω(m)} (distinct since V < ℓ/4 and V injective);
swap; Σ_{ℓ ≡ −1 (4m), ℓ∈(X^{1/2},X]} 1/ℓ ≥ (1 − 3η)(log 2)/(2·φ(4m))·(1 − o(1)) ≥ 1/(5φ(4m)) for η ≤ 1/6 ✓; φ(4m) ≤ 2m ✓;
V ≤ m^{2+2e} ≤ Y ✓; log Z ≥ 4(C₂κ + 1) ⟸ u ≥ 40(C₂+1)κ² ✓; log x/log T ≥ (u/2)/(u/(10(e+1)) + log 4) ≥ 4κ for κ ≥ κ₀ ✓.

### Thm 2.1 — SOUND-AFTER-REPAIRS (minor)
Bookkeeping re-done independently: log S ≥ κ(log u − A_κ) = κ(1 + λ/(κ+1)) ≥ κ; log k ≤ λ − log 2u;
log(S/k) ≥ (κ+1)log u − κA_κ − λ = A_κ + κ + 1 ✓. k!e_k ≥ S^k − C(k,2)T S^{k−2} ✓ (standard). T ≤ X^{1/5−1/2}S ✓;
k² ≤ X^{3/10} ⟸ u ≥ (20/3)λ ✓ in both regimes. L ≥ ½(S/k)^k ✓, log L ≥ (κ+1)k − 1 ✓, k ≥ log N/(2u) − 1 ✓; small primes
≤ X: e^u ≤ e^{O(λ² log λ)} ✓. The sieved set: p ∈ (X, N] prime with no ES^{(y,e)} solution avoids −4V mod ℓ (p ∤ Vℓ since
p > X > ℓ, V) ✓. Monotonicity in e ✓. At e = ⌊λ⌋: saving ≥ c log N/(e·λ log λ) ✓. Finitely many small e via CAP_GROWING
Thm 1.4 (≪_e, c_e > 0) — uniform constant by taking min/max over finitely many e ✓. Label correct; "ineffective" correct
(BV/Siegel–Walfisz for the small e; the large-e part is effective).
Minor (D4): the statement has log(e+3), the proof gives log(κ+2) = log(e+4) — harmless; the "u ≤ ½log N − (saving)"
sentence is garbled (what is needed is e^u ≤ N exp(−c(log N)^{κ/(κ+1)}/(κ log κ)), true since u = O(λ² log λ ·
(log N)^{1/3})).

### Prop 4.1 — SOUND
Re-derived: a prime-modulus shot needs r ≡ 3 (4) and (−p/r) = 1, i.e. (p/r) = −1 (p ≡ 1 (4)); for p ≡ 1 (mod W),
W = 8∏_{3≤r≤R} r, (p/r) = (1/r) = 1 for all odd r ≤ R; Linnik gives such p with log p ≤ L log W = (L + o(1))R. Hence every
prime certifying modulus exceeds R ≫ log p. The cap consequence is EXPONENT_CAP Prop 3.1(c): with ω(K) ≤ (1+o(1))log r/
log log r, ∏(κ_i + e + 1) ≥ (r−1)/2 forces log(e + 1) ≥ (1 − o(1)) log log r. ✓ (It is a statement about covering
arguments only; e*(p) itself is 0 for all tested p — the author says so.)

### Thm 4.2 — label CONDITIONAL is acceptable; sketch adequate after D6
(a) Re-derivation. p ≡ 1 (4). Want a prime r ≡ 11 (12) with (p/r) = −1 and ⟨3⟩ = (F_r^*)². Then (3/r) = 1 automatically
(r ≡ 2 (3), r ≡ 3 (4)), (r−1)/2 is odd, so ⟨3⟩ = squares = ⟨9⟩, and (−p/r) = 1 gives −p/4 ≡ 9^a, a < (r−1)/2:
D = 9^a ∈ 𝒟_e(r) with e = max(0, a − v₃(K)) ≤ r/2, p ∤ Dr. ✓ Counting under GRH (Hooley): the fields
L_m = ℚ(ζ₁₂, √p, ζ_m, 3^{1/m}) (m | ∏_{5≤q≤ξ₁} q) have |C| = 1 class (r ≡ 11 (12), Frob nontrivial on √p, split in
ℚ(ζ_m, 3^{1/m})); linear disjointness: ℚ(ζ_m, 3^{1/m}) ∩ ℚ^{ab} = ℚ(ζ_m) for odd squarefree m, and √p ∈ ℚ(ζ_{12m}) only if
p | 12m, impossible as m ≤ e^{O(ξ₁)} ≤ x^{ε′} < p. Lagarias–Odlyzko (GRH): |π_C(x, L) − li(x)/[L:ℚ]| ≪ √x(log d_L/[L:ℚ] +
log x) ≪ √x log(pmx); x^{ε′} terms: error x^{1/2+ε′}log(px) vs main ≥ 0.3·x/(8 log x): needs x ≥ C_ε(log p)^{2+ε} ✓.
Medium/large q (Hooley; r ≡ 1 (q) and 3 a q-th power; BT; r | 3^t − 1) are p-free and O(x log₂x/log²x) ✓. Note q = 3 is
automatically harmless (r ≡ 2 (3)). So (a) is a correct GRH theorem; the sketch contains every ingredient.
(b) Parameter bookkeeping re-checked: ξ = √x/(P log³x) makes the medium range ≪ x/(φ(P) log²x); large range
6^k(√x P log³x)^{1+1/k}·3 log P ≪ x/(φ(P)log²x) ⟸ log x ≥ Ck log k ✓; (3B)^{k+1} log P = x log P/(P log³x) ✓;
λ_k ≤ 2^k x/B^{k−1}·(Minkowski II), x/B^{k−1} = x^{2/(k+1)}(P log³x)^{(k−1)/(k+1)}3^{k−1} ✓; with log x ≍ log₂p and
k ≍ √(log₂p/log₃p) every term is exp(O(√(log₂p log₃p))) ✓. Each s ∈ S is a QR mod r for r ≡ −1 (4P) ✓ (both s mod 4
cases). The covering step needs non-negative exponents: PHASE_DIAGRAM Thm 5.1 Step 4's shift by ∏ s^{−2L} (R209 m9,
R210 m9) doubles the exponent bound — fine, but must be cited (D6).

### KARY3 consistency — SOUND
EXCEPTIONAL_KARY3 Thm 4.1 is about families of ℛ(M)-, (a,D)-, Case-A and selector classes (ES certificates). For
e ≥ 1, 𝒟_e(M) ⊋ ℛ(M) (the even-excess exponents certify only the relaxation ES^{(y,e)}), so (e+2)/(e+3) > 3/4 at e ≥ 2 is a
statement about a weaker problem; at e = 1 it ties 3/4; at e = 0 it is 2/3 < 3/4. No contradiction ✓. The (e+3)/(e+4)
rows are correctly labelled Assessment.

### Thm 3.1 — the inequality is correct for V < ℓ/4; the "any cap, e = ∞ included" reading is FALSE (D1)
See D1.

## Defects

**D1 (MAJOR — wrong headline; Thm 3.1 / §0 Z4-2 / Remark 2.2 / §7 item 2 / AGENT_REPORT SHARP 2 / z10_uniform_cap).**
Thm 3.1 defines ω_∞(ℓ) as the classes −4V(τ) with **V(τ) < ℓ/4** and calls this "the largest class family of this
architecture". It is not: neither CAP_GROWING Prop 1.3 nor Prop 5.1 has any size condition on D; V < ℓ/4 only serves to
make the classes distinct for counting. The full certificate family at ℓ is {−4D mod ℓ : D ∈ 𝒟_e(ℓ)} (Prop 5.1), with
D arbitrarily large. Counterexample to the e = ∞ claim: for ℓ ≡ 11 (12), 3 | K = (ℓ+1)/4, so D = 9^j ∈ 𝒟_∞(ℓ) for all
j, and the classes −4·⟨9⟩ number ord_ℓ(9) ≥ ord_ℓ(3)/2. Elementarily (count prime factors of ∏_{j≤T}(3^j − 1)),
ord_ℓ(3) ≥ ℓ^{1/2}/log ℓ for all but O(y/log³y) primes ℓ ∈ (y, 2y]. Hence already the single-prime part of the large-
sieve sum gives L ≥ Σ_{ℓ≤N^{1/2}, ℓ≡11 (12)} ω(ℓ)/ℓ ≫ N^{1/4}/log²N, i.e. **exceptions to ES^{(y,∞)} ≪ N^{3/4+o(1)} from the
prime-modulus large sieve** — a power saving. Numerically ω(ℓ) = (ℓ−1)/2 (all non-residues) for most ℓ ≡ 11 (12), and
Σ_{ℓ<3·10⁵} ω/(ℓ−ω) = 5899 ≍ Q/log Q (so in fact ≪ N^{1/2+o(1)} heuristically/under Artin-type input)
(`scripts/review_r237_fullfamily.py 300000`, `data/r237/fullfamily.txt`; exact solution with D = 729 > ℓ = 11:
p = 43, (x, y, z) = (78, 129, 1118/81)). The same mechanism (classes −4·9^j, j ≤ e, distinct once ord_ℓ(9) > e)
gives ω(ℓ) ≥ e + 1 at almost all ℓ ≡ 11 (12) ≥ e³, and with q = products of k ≍ log N/(2 log e³) such primes,
log(S/k) ≍ log(e/log N): a power saving for every **e ≥ (log N)^{1+ε}**. So "no cap — not even e = ∞ — gives a power
saving", "the knob saturates at e ≍ log log N" and "matching Rankin ceiling at every cap (even e = ∞)" are false for
the architecture as defined by Prop 1.3/5.1.
*What survives:* Thm 3.1 is a correct bound for sieves using only classes with D < ℓ/4 (the truncation Thm 2.1 uses,
D ≤ X^{1/5}). Whether the ceiling log N/(λ log λ) holds for the full 𝒟_e(ℓ) when e ≤ C log log N (or up to log N) is
OPEN — it is plausible for e ≤ c log ℓ / log 9 at the relevant ℓ, since then D < ℓ automatically for one-prime powers,
but products of several s^{2σ+2e} need not be < ℓ.
*Repair:* restate Thm 3.1 for the truncated family ("classes −4D with D < ℓ/4", or more generally D ≤ ℓ^{O(1)}?—only
D < ℓ/4 is proved); delete "at ANY cap", "e = ∞ included", "the largest class family of this architecture" and the
B6-moral "not even for a true statement" (the opposite is true: at e = ∞ the large sieve does give a power saving, just
not "all p ≥ p₀" — the large sieve can never give that, which is the trivial part of B6); replace "saturates at
e ≍ log log N" by "saturates at e ≍ log log N *within the truncated family*"; add the full-family power saving at
e ≥ (log N)^{1+ε} as a Remark (PROVED, elementary as sketched) and leave log log N ≤ e ≤ (log N)^{1+ε} as OPEN.

**D3 (MINOR — citation).** §1 Input (G) misquotes Gallagher's Thm 7 (see the claim section above: range
exp(√log x) ≤ Q ≤ x^b, short intervals x/Q ≤ h ≤ x, exceptional term modified not omitted). *Repair:* quote eq. (29)
verbatim, state that (G) is used only in the form "for q ≤ T, q₁ ∤ q, y ≥ T^{4κ}, exp(√log 2y) ≤ T: relative error
≤ C exp(−a log y/log T) for θ(2y; q, a) − θ(y; q, a)", and add "u ≥ 100κ²" (or C₂ ≥ 2) to Prop 1.2's hypothesis so that
T ≥ exp(√log X).

**D4 (MINOR — bookkeeping wording).** Thm 2.1 proof: log(κ+2) vs log(e+3) mismatch; the sentence "u ≤ … ≤ ½ log N −
(saving)" should read "e^u ≤ N·exp(−c(log N)^{κ/(κ+1)}/(κ log κ))", which holds since u ≪ κ² log κ (log N)^{1/(κ+1)}
≤ (log N)^{1/3+o(1)} + O(λ² log λ).

**D5 (MINOR — consequence of D1).** §4 "Reading" after Prop 4.1 and §4 "The gap" ("the large sieve cannot do better at
any cap") inherit D1. *Repair:* qualify by "with the truncated class family D < ℓ/4".

**D6 (MINOR — Thm 4.2 write-up).** The proof is labelled "citation level, to be hostile-reviewed". I re-derived (a) and
the bookkeeping of (b) and found no error, so CONDITIONAL (GRH) may stand, but the text should (i) cite the effective
Chebotarev theorem precisely (Lagarias–Odlyzko 1977 / Serre 1981 Thm 4: error ≪ √x(log d_L + [L:ℚ] log x)/[L:ℚ] for
|C| = 1) and bound log d_L ≤ [L:ℚ] log(12·3·m·p·m) explicitly; (ii) state the disjointness argument (ℚ(ζ_m, 3^{1/m}) ∩ ℚ^{ab}
= ℚ(ζ_m), p ∤ 12m); (iii) in (b) cite the non-negative-exponent shift of PHASE_DIAGRAM Thm 5.1 Step 4 (exponents ≤ 2L);
(iv) drop "There is an absolute C" in front of (a) (the constant is C_ε). Then remove "to be hostile-reviewed".

**D2 (MINOR — scope).** Cor 5.2(i) "within the shot form y = pA every ES^{(y,e)} certificate at every modulus is a class
of 𝒟_e(M)" and Prop 5.3 "every integral solution of this shape is in ℛ(M)" omit the hypothesis p ∤ xM: solutions with
y = pA and p | M = 4A − 1 (e.g. 4/5 = 1/2 + 1/20 + 1/4) or p | x are genuine and not classes of 𝒟_e(M). *Repair:* add
"(with p ∤ x and p ∤ 4A − 1; then D = xM − pA, so this is all solutions with p ∥… p | y, p ∤ x, p ∤ 4y/p − 1)". The
converse derivation above (D = xM − pA) should be added to Prop 5.1's proof — it is what makes "every certificate" true
and is currently missing (the proof only goes from D to the solution).
