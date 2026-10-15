# R235 — hostile review #1 of O232 (SIGN_FIELDS.md, BRAINSTORM/z8_*.md, data/z8/)

Reviewer: R235 (side-agent/review-sign-fields). Merged side-agent/sign-fields at 069d5e83 (README conflict resolved by
keeping both sides). From-scratch scripts: `scripts/review_r235_cert.py` (certificate checker, sympy, no ec_cert/z8
imports), `scripts/review_r235_brute.py` (independent ES solver via (ay − d)(az − d) = d²), further `scripts/review_r235_*.py`.

## Summary verdicts
(filled in progressively; see sections below)

| claim | verdict |
|---|---|
| Thm 1.3 (ES for all 4^s + k, nine k) | SOUND (label PROVED, computer-assisted, justified) |
| Lemma 1.1 (non-trivial k ≡ 9 mod 24 for c₀ = 1) | SOUND |
| Lemma 1.2 (no integer unit-square points, c₀ = 1) | SOUND |
| §1.4 OPEN list, k = 105 hardness, Λ₁₀₅ ∩ Sq^× = ∅ at L = 360 | SOUND-AFTER-REPAIRS (D3, D4 minor) |
| §1.4 mixed point μ* for k = 105 (EVIDENCE) | SOUND as EVIDENCE |

## 1. Theorem 1.3 — headline

**Independent checker** (`scripts/review_r235_cert.py 300`). Semantics re-derived from the JSON: n_s = 4^s + c,
class (M, r), x, y, z ∈ ℚ[n] given low-degree-first. For every class of all nine certificates:
1. 4xyz − n(xy + yz + zx) = 0 in ℚ[n] (sympy expansion): all 30 classes pass.
2. Integrality: with D = lcm of coefficient denominators, D·p ∈ ℤ[n] and D·p(n) mod D is D-periodic in n, so
   checking n = r + Mt for t < D/gcd(D, M) is exhaustive (different method from ec_cert's finite differences): pass.
3. Positivity: largest real root R of each coordinate (sympy real_roots), positive leading coefficients; class used only
   when n > R, else falls back to brute force: pass.
4. Periodicity (re-derived): write M = 2^e M′. For s ≥ ⌈e/2⌉, 4^s ≡ 0 (mod 2^e) so n_s ≡ c (mod 2^e); and
   n_{s+L} − n_s = 4^s(4^L − 1) ≡ 0 (mod M′) iff M′ | 4^L − 1 (checked: pow(4, L, M′) = 1). Hence n_s mod M depends only
   on s mod L for s ≥ S₀ = max⌈e/2⌉ (S₀ = 1 for k = 225 because of M = 2716 = 4·679, else 0). Coverage of the L residues
   from S₀ on: pass; redundant direct check n_s ≡ n_{s+L} ≡ n_{s+7L} (mod M): pass.
5. Exact integer verification of a class solution for every s ≤ 300: pass. Only s = 0, k = 225 (n = 226, even) needed
   brute force: (57, 6442, 41492922).
6. Independent brute force (no certificate) for s ≤ 20 for all 13 offsets k ≡ 9 (mod 24), k ≤ 297
   (`review_r235_brute.py 20`): all solvable.
The author's checker `ec_cert.py` (run with MMAX = 600) also passes all nine — consistent with the claim.

**T1 / square control.** Squares in the families come from (a − 2^s)(a + 2^s) = k. Complete list (s ≥ 0):
k = 9: s = 2, 25 = 5²; k = 57: s = 3, 121 = 11²; k = 129: s = 6, 4225 = 65²; k = 153: s = 2, 169 = 13²;
k = 201: s = 5, 1225 = 35²; k = 225: s = 3, 289 = 17²; none for k = 81, 177, 249. My checker confirms each of these is
covered by a **divisor class** D_q with q | a (D₅, D₁₁, D₅, D₁₃, D₅, D₁₇ respectively) — real solutions obtained by
scaling ES(q), not a polynomial ET family "solving" a square (which would contradict Mordell/Schinzel). No non-D class
contains a square member (the ec_cert T1 test to s < 20000 also passes). Note that k = 81 is a square but 4^s + 81 is never
a square (factor pairs (1,81), (3,27) give 2^{s+1} ∈ {80, 24}).

**Mordell-hard members.** Recomputed residues mod 840 for s ≥ 2: k = 57: s ≡ 3 (6) → 121; 153: s ≡ 2 (6) → 169;
177: s ≡ 5 (6) → 361; 225: s ≡ 3 (6) → 289, s ≡ 0 (6) → 121; k = 9, 81, 129, 201, 249: no hard members. Matches §1.3.
**Survey list.** k ≡ 9 (mod 24), k ≤ 300: 9, 33, …, 297 = 13 offsets; 9 certified + 4 OPEN — consistent.

Verdict Thm 1.3: **SOUND**. Defects are presentational only (see D1, D2 below).

## 2. Lemma 1.1, Lemma 1.2

**Lemma 1.1.** For s ≥ 2, c₀4^s ≡ 0 (mod 16), so n_s ≡ k (mod 8); 4 ≡ 1 (mod 3) gives n_s ≡ c₀ + k (mod 3). Mordell's six
classes 1, 121, 169, 289, 361, 529 (mod 840) are all ≡ 1 (mod 24), and every odd n outside them is ES-solvable by
Mordell's identities. For c₀ = 1: k ≡ 1 (8), k ≡ 0 (3) ⟺ k ≡ 9 (24). Correct. (Implicitly k odd; s ∈ {0, 1} are finitely
many members and are irrelevant to "non-trivial".) **SOUND.** Note "non-trivial" only means "not killed by Lemma 1.1";
five of the nine certified k are nevertheless Mordell-trivial for all s (D1).

**Lemma 1.2.** Re-derived: with EXPONENT_COVERING's conventions (2-component of ν(μ) is the constant k, odd components
4^μ + k), for ℓ ≥ 0 the odd components are the odd integer N = 4^ℓ + k ≥ 4, which has an odd prime factor q, so ν(ℓ)_q is
not a unit — squareness is not even needed (the author's "N = s² with s a power of 2" detour is correct but redundant). For
ℓ = −a < 0, (1 + k4^a)/4^a is a q-adic unit for all odd q iff the odd integer 1 + k4^a is 1, impossible for k ≥ 1. **SOUND.**
It only excludes *integer* ℓ; non-integer μ ∈ Ẑ can still be unit-square points — the doc says so ("(EH)" is checked
separately by the screen). Fine.

## 3. §1.4 OPEN offsets and k = 105 (`scripts/review_r235_k105.py`)

* Integer square points (search ℓ ∈ [−79, 79]): k = 33: ℓ = 2 (7²), 4 (17²), −2 (23²/16) ✓. k = 105: 2, 3, 4, −2 ✓.
  **k = 273: ℓ = 2 (17²) AND ℓ = 4 (4⁴ + 273 = 529 = 23²) — the doc omits ℓ = 4 (D3).** k = 297: ℓ = 3 (19²) ✓.
* k = 105: every member s ≥ 2 lies in Mordell's hard set, all six residues occur (checked s < 400) ✓; n_s ≡ (2^s)² (mod 105) ✓.
* Unit-square screen, L = 360 (own code, same logic: survivor ⟺ for every prime q < 3·10⁶ with q | 4³⁶⁰ − 1, n_s mod q is a
  non-zero QR). **0 survivors**; in fact primes ≤ 181 already suffice. The deduction Λ₁₀₅ ∩ Sq^× = ∅ is valid: for any
  μ ∈ Ẑ, ν(μ)_q mod q = 4^{μ mod ord_q 4} + 105, so the residue s = μ mod 360 transfers the kill. **CERTIFIED, SOUND.**
* k = 33 screen: for L = 180, 360, 720 the only survivor is s ≡ −2 ✓, and ord₂₃(4) = 11 so D₂₃ needs 11 | L ✓. But for
  L = 60 and 120 there is a second survivor (s ≡ 34 mod 60, s ≡ 94 mod 120) — a mixed point (≡ 4 at 3, 5; ≡ 2 mod 4),
  killed once 9 | L. "At every L tested" is therefore true only if no L with 9 ∤ L ≥ 60 was tested (D4). (It actually
  supports the author's mixed-point picture.)
* Mixed point μ* for k = 105: 124 ≡ (4 mod 8, −2 mod 9, 4 mod 5) ✓; 844 ≡ (4, −2, 4, 4) mod (8, 9, 5, 7) ✓.
  ord₁₈₁(4) = 90 = 2·3²·5, μ* ≡ 34 (mod 90), n ≡ 85 (mod 181), (85/181) = −1 ✓. ord₉₁₉(4) = 153, μ* ≡ 106 (mod 153),
  n ≡ 551 ≡ −4·2²·23 (mod 919), and 4·2·23 | 920: μ* lies in the ET family II2 (a, d, f) = (2, 23, 919) ✓.
  The reading "q with ord_q(4) a 2·3-power ⇒ n ≡ (41/4)²" is right only for ord = 3^b or 2·3^b (needs 4 ≡ −2 mod 2^a, a ≤ 1);
  "2·3-power" should be spelled "of the form 3^b or 2·3^b" (part of D4). The adaptive-covering Haar measures are EVIDENCE
  produced by author code; not replayed (scope: EVIDENCE only, claim is explicitly weak and not a certificate).

## Defects
**D1 (MINOR, presentation/novelty; SIGN_FIELDS §1 Thm 1.3 and AGENT_REPORT headline).** Five of the nine offsets
(k = 9, 81, 129, 201, 249) have **no** member in Mordell's six classes mod 840 for s ≥ 2, so ES for them is an immediate
corollary of Mordell's classical mod-840 theorem (plus s = 0, 1 by hand); the certificates just re-encode that. Of the
other four, the hard-class members are for k = 153 *all* multiples of 13 (4² + 153 = 13², ord₁₃4 = 6) and for k = 225 the
s ≡ 3 (6) ones are multiples of 17 — divisor classes. The genuinely non-classical content is: k = 57 (s ≡ 9 mod 30, class
mod 2015), k = 177 (s ≡ 5 mod 6, class mod 39), k = 225 (s ≡ 0 mod 6 via mod 39, s ≡ 9, 21 mod 24 via mod 2019, 2716).
Repair: state in Thm 1.3 that for k ∈ {9, 81, 129, 201, 249} the result is Mordell's theorem, and headline the four
offsets with hard-class members.

**D2 (MINOR, label hygiene; SIGN_FIELDS Thm 1.3 statement).** "certificates checked by ec_cert.py" — ec_cert's T1 test
is a sanity check, not a proof step; the proof is identity + integrality + positivity + periodicity + coverage + small
cases. Also ec_cert uses m₀ = v₂(M) (= 2 for k = 225) where ⌈v₂(M)/2⌉ = 1 suffices — harmless (conservative). No repair
needed beyond optionally noting that the k = 225 class mod 2716 is an I1 class whose 2-part needs s ≥ 1.

**D3 (MINOR; SIGN_FIELDS §1.4 first bullet list).** k = 273 has a second integer square point 4⁴ + 273 = 23² (factor pair
(7, 39) of 273). Repair: "k = 273: 4² + 273 = 17², 4⁴ + 273 = 23²".

**D4 (MINOR; SIGN_FIELDS §1.4, k = 33 parenthesis and mixed-point bullet).** (a) "the screen leaves exactly s ≡ −2 (mod L)
at every L tested" — false at L = 60, 120 (extra survivor s ≡ 34 mod 60, a mixed point); state the tested L list, or say
"for every L divisible by 9 tested (180, 360, …)". (b) "ord_q(4) a 2·3-power" → "ord_q(4) ∈ {3^b, 2·3^b}".
