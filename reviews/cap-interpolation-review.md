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

**D2 (MINOR — scope).** Cor 5.2(i) "within the shot form y = pA every ES^{(y,e)} certificate at every modulus is a class
of 𝒟_e(M)" and Prop 5.3 "every integral solution of this shape is in ℛ(M)" omit the hypothesis p ∤ xM: solutions with
y = pA and p | M = 4A − 1 (e.g. 4/5 = 1/2 + 1/20 + 1/4) or p | x are genuine and not classes of 𝒟_e(M). *Repair:* add
"(with p ∤ x and p ∤ 4A − 1; then D = xM − pA, so this is all solutions with p ∥… p | y, p ∤ x, p ∤ 4y/p − 1)". The
converse derivation above (D = xM − pA) should be added to Prop 5.1's proof — it is what makes "every certificate" true
and is currently missing (the proof only goes from D to the solution).
