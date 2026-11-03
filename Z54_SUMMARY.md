# Z54_SUMMARY — wave z54 on the three best open gaps after z53

**ES is OPEN.** Every result here is internal. Each memo had an internal hostile review and a cross-model (GPT-6 Astra)
review; all seven were ACCEPT-WITH-FIXES and were merged after the fixes. Reviews: `data/z54/xreview/REVIEW_<LANE>.md`.
Briefs: `z52bbriefs/z53_depth.md`, `z54_lanes.md`, `xreview_z54.md`. This summary carries scopes only loosely; each
memo's own statement governs.

## 0. Bottom line

**None of the three gaps closed, and B2 did not move.** Each gap now has a sharper statement of what is missing, and there
are a few new conditional or small results.

## 1. Gap 1 — bilinear (ℓ, C) cancellation: square sieve at the balanced block

Lanes: BILINJAC (Jacobi-symbol tools) and BILINDIV (divisor and geometry tools).

**What was proved (BILINJAC).** Prop M / Cor M′ (PROVED; Cor M′ relative to the quoted tool statements) shows that two
classes of character-side input to the square sieve give no saving when used directly:
* inputs that see the weights only through their square-class ℓ² mass, as Heath-Brown's real-character large sieve
  does when used directly;
* inputs that see the weights only through sup-norm, support and range, as Heath-Brown's Cor 4 does.

After Poisson summation the (ℓ, C) coefficients are Kloosterman sums, not Jacobi symbols.

**Sufficient condition (BILINJAC Thm R, PROVED).** Power-saving equidistribution of the strip's lattice points modulo
small Q (TS) suffices for a balanced-block power saving, with a loss of only Q. TS is necessary only for twist-blind
bounds (Prop R′). This is a twisted short-interval divisor problem at length x^{1/4}; its square-root form is a twisted
analogue of Jutila's conjecture (Assessment). No checked reference gives a pointwise power saving even for the untwisted
strip count (search-limited).

**New sufficient condition (BILINDIV Theorem T, PROVED).**
* Theorem T bounds N₂ by the size of the strip plus phase sums T(h) over the lattice points of the thin hyperbolic
  strip. So a first-order hypothesis TD(η), uniform for primes p and U in the fourth-root range, gives
  N₂ ≪ U^{1−η+ε}, hence a balanced-block saving (CONDITIONAL on TD).
* TD stands alongside z53's second-order MIX. Neither is shown to imply the other.
* EVIDENCE: T(h) is of square-root size at 10¹²–10¹⁸, at primes, odd squares and near-squares.

The specified one-variable implementations are closed as scoped statements, each with its deficit.

**Status.** This gap is upper-bound only and cannot give positivity. Sufficient missing inputs are now named: TD, MIX,
or the twisted Jutila-type equidistribution TS. None is shown to be necessary.

## 2. Gap 2 — the exact-divisor layer R − G on the Thm U family (B2 in its cleanest form)

Lanes: EXACTSUM (exponential sums in the free variable w) and EXACTSPIN (spins, Rédei symbols, power residues).

**Scoped no-go (EXACTSUM Theorem N, PROVED).** On a fixed window with α₁ ≤ β, bounding the exponential sums frequency
by frequency, or conductor by conductor, with n-uniform estimates and the triangle inequality, costs at least
P^{α₁−o(1)}. Prime-sensitive, one-sided and grouped-block methods are not excluded.

**Small positive results (EXACTSUM).**
* Lemma 4.1 / Cor 4.2 (PROVED relative to an exponent pair with κ > 0) control the plain exact shell in progressions,
  with a power saving uniform in the modulus.
* There are windows where Thm U, Thm X (with (C4) relaxed to (C4′)) and this control coexist; they exist already with
  a classical van der Corput pair (Prop 4.3). For every tabulated non-conjectural pair they lie in the extreme corner
  C ≤ p^{0.025}.
* Transfer to the squarefree layers is Assessment.

**What survives (Assessment).** Cancellation across u within a dyadic slice: about U distinct integers p + u with moving
moduli 4u. That is B2 in tied form. In the data (EVIDENCE, non-reconciled windows) the variance-carrying blocks have conductor
comparable to u.

**Spin route (EXACTSPIN, PROVED identities).**
* At prime u = ℓ, the order-k part of the class of the level divisor is the Ramanujan sum c_k of a power-residue
  symbol. Its p-factor is a Frobenius in ℚ(ζ_k, p^{1/k}), a field that depends only on p.
* For k = 3 and k = 4 the symbol is written out explicitly: for k = 3 as an anticyclotomic character of the angle of the
  prime above u (with a ramified factor at 3); for k = 4 with anticyclotomic angle factors plus quadratic "Rédei-type"
  bits.
* R − G splits as S₂ + S_o; both parts vanish at odd squares (via the empty genus), but the individual order-k layers
  Δ_k with 4 ∤ k need not.

No bounded-degree identification of the full layer was found, and no bound on T_uw follows. The direct
complete-fibre averaging is excluded by the fibre sizes (Lemma 4.5).

**Status.** Narrowed. The remaining object is cross-u cancellation of tied events, i.e. B2.

## 3. Gap 3 — growing-window HC (target A > 2 log 2)

Lanes: HCKILL (the kill side, unconditional and conditional), HCWIN (the upper side) and UPPER2 (an unprimed "just prove
it" attempt).

**Exact reduction (HCKILL Lemma 1.1, PROVED).** For primes p ≡ 1 (mod 8), K(4) = K(5) = K(6), i.e. "HC(p) > 4 infinitely
often", is equivalent to P(4,15): infinitely many such p with p + 4 and 4p + 1 both composed only of primes ≡ 1 (4).
"HC unbounded" therefore needs at least two half-dimensional shift conditions on a prime.

**Theorem Q (PROVED, an explicit near-square kill family).** Every prime p = 5m² + 1 with 4 | m has HC(p) ≥ 7.
* The family is infinite under Bunyakovsky for the single polynomial 720k² + 1.
* CERTIFIED for all 5,719 such primes ≤ 10¹².
* I re-checked 628 of them independently (`scripts/z54_summary_thmQ_check.py`, `data/z54/summary/thmQ_check.txt`; one engine, EVIDENCE). Controls: about 7.5 % of random primes p ≡ 1 (8) near 10⁹ have HC > 4.

**Conditional kill (Theorem E, CONDITIONAL on EH(1 − η₀) for some absolute, uncomputed η₀ > 0; implied by the standard
Elliott–Halberstam conjecture).**
* #{p ≤ x : p ≡ 1 (8), HC(p) > 4} ≫ x/(log x)², the order of the known upper bound.
* With BV alone only the "shadow" Prop A is proved.
* Within this sieve implementation (Assessment), closing the gap needs either level θ₀ or prime detection in a
  switched sequence; unconditional K(4) is open.
* The direct confinement-sieve implementation gives no K(7) lower bound even at level 1 (Assessment, scoped).
* A two-variable quadratic confines at most one window integer on a full-rank coset (Prop F6). One-variable quadratic
  families can confine both line-4 integers (Theorem Q), but no single one certifies a growing window (Prop F5), and for
  the lines {4, 7, 8} only finitely many formal ratios exist (Prop F4, Faltings).

**Where 2 log 2 comes from (HCWIN Theorem B, PROVED rel. Henriot and BV).**
* 2 log 2 separates two proved regimes of the truncated divisor mass of the window integers, averaged over p. This is an
  average (B6) and only calibrates the threshold.
* At a single p, Turán–Kubilius over the window variable x is exact only for primes ≤ √X.

**HCWIN conditional theorems (PROVED implications, hypotheses open).**
* Theorem C (model statement): the conjunction "some line is K-big at every large p" and "every K-big line succeeds"
  has probability 0 in the model, for fixed K and for K(p) → ∞. That class hypotheses must be joint is Assessment.
* Theorem S: anatomy plus a conditioned lottery Lot(C) gives HC ≤ (log p)^A.
* Theorem D: the class-layer hypothesis Lot_Λ(C) (with window cap exp(3√(C log p))) *alone* gives
  HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)} for all large primes p ≡ 1 (8). This beats the open HC ≪ p^θ, but only
  under that hypothesis, which is ES-strength.

**UPPER2 (unprimed, PROVED).**
* HC(p) ≤ 8 for every prime p ≡ 1 (8), p > 7, that is a non-residue modulo 3, 5 or 7, i.e. outside Mordell's six classes
  mod 840, via six explicit words.
* No finite set of fixed-level congruence tests covers all p ≡ 1 (8) (Prop 6.3(a)); growing-level arguments are not
  excluded.
* The target itself is not proved. Any uniform finite bound already implies eventual ES.
* Per the cross-review, most of UPPER2 is an independent reproof of `Z53_UPPER.md` / `LOWERTAIL_ROUND2_FABLE.md`
  results, its sieve theorems weaker than Z53's. New: the census HC(p) ≤ 64 for all primes p ≡ 1 (4) up to 10⁹
  (CERTIFIED), and the μ data.

**Status.** Every kill K(X) implies P(4,15) = K(4). P(4,15) is open unconditionally and holds under EH(1 − η₀) or under
Bunyakovsky for 720k² + 1; for fixed X ≥ 7, K(X) still rests on Dickson. On the upper side there is a sufficient route
through pointwise anatomy plus an open single-p class lottery.

## 4. Honest assessment

Wave z54 converted each "best gap" into a sharper named missing statement:
* **Gap 1:** TD, MIX, or twisted Jutila-type equidistribution (each sufficient, none shown necessary).
* **Gap 2:** cross-u cancellation of tied events, which is B2.
* **Gap 3:** P(4,15) on the kill side, and Lot on the upper side.

The genuinely new mathematics is modest:
* an exact reduction of HC-unboundedness;
* a Bunyakovsky-conditional near-square kill family, Theorem Q;
* a kill conditional on EH (standard but unproved);
* a first-order sufficient condition TD;
* the explicit spin and Kummer description of the class layer, at prime u and per fixed order.

None of it touches positivity at a prescribed prime.
