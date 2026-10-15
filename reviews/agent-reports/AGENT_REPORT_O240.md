# AGENT_REPORT_O240 — spark relay Z9: menu-relative sterility (checkpoint 1)

Branch side-agent/menu-sterility (merged side-agent/synthesis-six first, README conflict resolved). Deep file
MENU_STERILITY.md; memos BRAINSTORM/z15_*.md (7, indexed); scripts scripts/z15_*; certificate data/z15_cert_proth3_et.json (4 KB).

**SHARP:** **ES holds for every n = 3·2^s + 1** (PROVED, computer-assisted; MENU_STERILITY Theorem C). This family is
PROVED to have no finite covering by ET/divisor classes (EXPONENT_COVERING Cor 1.5: μ = 0 is a profinite unit-square
point) — so, unlike O238's 4^s + 105 (R246 D2: no sterile point was ever established there), this is a *genuine* ET-sterile
point dissolving under a richer menu. The dissolving class is ONE Lemma-1.1 window, m = 11, whose budget is forced by the
Sophie Germain factorisation 4X⁴ + 1 = (2X² + 2X + 1)(2X² − 2X + 1), X = 2^{(s−4)/4}:
  for X ≡ 4, 6 (mod 11), n = 48X⁴ + 1:  4/n = 1/(3(4X⁴+1)) + 11/(6n(2X²−2X+1)(X²+X+2)) + 11/(2n(4X⁴+1)(X²+X+2))
(Theorem B: s ≡ 0, 12 (mod 40)). Other divisor exponents of the same window cover all s ≡ 0 (4) except s ≡ 4, 24 (40) —
exactly the neighbourhoods of the integer T1 points X = ±1 (n = 49 = 7²) — and 6 ET/divisor classes (moduli 5, 7, 15, 61)
cover the rest. Second sharp item: **Theorem A (witness reciprocity)**: the sterile set of the menu "identities polynomial
in u on n = φ(u)" contains the 2-descent set {u* : γ(u* − θ) locally square everywhere, γ ∈ ℚ[u]/(φ) totally positive};
it unifies Schinzel/Mordell and NEAR_SQUARE Thm 3.4 (integer T1 points with φ(u₀) > 1 stay with Thm 3.3 — R-O240 repair), and identifies one-parameter sterility with a Brauer/2-cover-
descent pairing on w² = φ(u).

## Results
* Theorem A (PROVED): witness reciprocity for M₁[φ], any φ (MENU_STERILITY §1).
* Theorem B (PROVED, symbolic) and Theorem C (PROVED, computer-assisted): ES for all 3·2^s + 1. Checker
  `scripts/z15_cert_proth_check.py data/z15_cert_proth3_et.json 1500` (sympy; re-derives the SG rules, checks identities,
  integer-valuedness, positivity, ET classes incl. no odd squares in non-divisor classes, coverage of all s mod 360, exact
  solutions s ≤ 1500; ~2 s). Builder `z15_cert_proth_make.py 3 360 3000 OUT 0,8,12,16,20,28,32,36`.
* Prop 4.1 (PROVED): constant windows m ≡ 7 (mod 8) never fire at μ = 0 of c·2^s + 1, c + 1 = 4^i (Jacobi); this kills all
  cyclotomic windows there and is why O238-style windows fail. Prop 4.3 (PROVED): the Sophie-Germain menu at μ = 0 is
  finite (resultant bound; m ∤ N identically since m has a positive real root where N > 0 — R-O240 repair). EVIDENCE: no SG window found at μ = 0 for c = 15, 63 (t ≤ 301), 255 (t ≤ 15).
* Prop 3.1 (PROVED): NEAR_SQUARE Thm 2.2 does not extend to families polynomial in an algebraic function of m
  (O238's class as m = 16v³ meets Z_105^□) — answers O238 spark 5 negatively for the naive extension.
* Prop 5.1 (PROVED, elementary): finitely many thin (root/exponential/window) items cannot cover all primes near the (J)54
  sterile Mordell points. Assessment (R-O240 narrowed): norm-form parametrisations keep T1 on square-compatible classes ((J)3,
  d = 2, under its hypotheses); remaining parameters at every prime are divisors (B2).
* §6 (Assessment): F_q[T] — Frobenius kills the Aurifeuillean divisor supply; Carlitz-cyclotomic divisors are the analogue.
* §4.1 EVIDENCE: 7·4^s + 9 ((J)68 sterile at μ = 0): μ = 0 covered by SG window m = 19; 2 of 1785 lifts left at L* = 128520, and they reproduce (1 lift each) at L* = 1413720 — self-similar stuck nodes, not decided.
* Menu ladder table: MENU_STERILITY §7.

## Self-review (codex deep, R-O240) — repairs applied
No FATAL; Theorems B/C re-run and confirmed (coverage of all s: ET periods divide 360, SG residues depend on s mod 40;
Cor 1.5 + Thm 1.4 indeed exclude ET/divisor coverings). MAJOR repaired: Theorem A does not contain integer T1 points with
φ(u₀) > 1 (not units; Thm 3.3 handles them; §4.3 attribution fixed, "Type I/II" qualifier added); Prop 4.3's general
finiteness now proved (real-root argument); density conclusions of §5 narrowed. Minors: ℤ[θ] → ℤ[1/lc][θ]; squares
s = 0, 3, 4; 27 vectors; Prop 4.1 proof expanded (e | j, odd-prime support); checker always covers s < 10.

## Honest caveats for the reviewer
* Theorem C's ET part uses the z8/ec_cover machinery (`ec_cover.certificate`); my checker re-verifies the JSON
  independently, but a from-scratch reviewer checker is advisable (as for O238).
* Positivity in Theorem C: SG rule coordinates are products of f± = 2X² ± 2X + 1 > 0, K + d > 0, n > 0 — checked by
  leading coefficients plus this remark, and exactly for s ≤ 1500.
* "Primes to 10⁶" triple-check is not applicable to a family theorem; exact symbolic identities + exact solutions to
  s ≤ 1500 (rules) / s ≤ 4000 (Theorem B) replace it. T1: 48X⁴ + 1 is square only at X = ±1 (< 10⁵ checked; X ≡ 4, 6 (11)
  none < 2·10⁶), and the rules are provably dead there.
* Novelty of "ES for all 3·2^s + 1" not literature-checked.
* Prop 4.3 for c = 15, 63 was not run to completion (resultant bounds ~10⁸ in t) — EVIDENCE only.
* Theorem A gives only ⊇ for the sterile set; equality (analogue of CONJECTURE Y10-S) is open.

## Sparks (not pursued)
1. 7·4^s + 9: identify the profinite point behind the self-reproducing residues 104960 (128520) → 233480 (1413720) and test it against Theorem A (is it a descent-sterile point for every root menu?).
2. μ = 0 of 15·2^s + 1: SG menu fails; try Type I root families and polynomial windows of degree ≥ 2, or prove sterility
   for all M₁[240X⁴ + 1] families via a refinement of Theorem A at the 2-adic places.
3. Genus ladder: for deg φ ≥ 5, Bruin–Stoll fake 2-Selmer sets are often empty — predict that M₁[φ] has no T1-type sterile
   points; test on c·2^s + 1 via quintic roots X = 2^{s/5} (needs m ≡ 3 (8) windows, i.e. new shapes).
4. Z_K⁺ (k < 0) analogue of Prop 3.1.
5. F_q[T]: Carlitz-cyclotomic divisors for thin families T^{q^s} + A.
6. Exponential analogue of Thm 1.4: "covering by ET + root-window classes exists iff Λ avoids ∩_e (descent sets)"
   (O238 spark 2), with Prop 4.3-type finiteness as the extra ingredient.
