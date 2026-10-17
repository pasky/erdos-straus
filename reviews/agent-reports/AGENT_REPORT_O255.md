# AGENT_REPORT_O255 — hatch H-B: parity-breaking literature audit + single-prime feasibility

Branch `side-agent/parity-audit`. Main file `PARITY_AUDIT.md`; excerpts in `sources/lit2026f/` (≈ 40 small .txt
files, ~150 KB total, no PDFs); scripts `scripts/pa_*.py`; logs `logs/pa_*`. **ES is not solved.**

## What was done
* Fixed the exact single-p events (§0): (a) ES-five on the u-side, E_a(p;U): ∃ u ≤ U, A | p+u, A ≡ −1 (mod u),
  (A/p) = −1; its sign-free 4-normalisation (a⁴) = (J)6's (★) (Type II (A)3); (b) windows q (QNR, q ≡ 4 − p (8)),
  sub-event d | (p+q)/4, d ≡ −1 (mod q). Lemma 0.1: min(u,v) ≤ √p + 2, so θ = 1/2 is the whole of ES-five.
* Literature table (§1, 33 rows): divisors in classes / intervals (Lenstra, CHN, Erdős–Hall, Ford, Koukoulopoulos);
  fixed-modulus Kloosterman and modular hyperbola (Weil via Shparlinski, KMS 2017/2020, Blomer–Pascadi 2026, KSWX,
  Bourgain–Garaev, Selberg–Hooley/FKM, DFI, Bettin–Chandee); pointwise short-interval results (Huxley/Li–Yang,
  Matomäki, Younis); parity-breaking and large moduli (FI, BFI, Maynard I–III and digits, Lichtman, Pascadi,
  Merikoski, Drappeau, Fouvry–Radziwiłł, Assing–Blomer–Li); Borwein–Choi xy+yz+zx; Elsholtz–Tao; Pollack/GRH
  windows; Dyachenko; Ventas v3; arXiv/#242 sweep to 2026-10-17 (nothing new since 2026-09-24).
* Quantitative gap (§2): Lemma 2.1 (PROVED, checked numerically) gives R(p) = M(p) + E(p) over a trial region
  |𝓡| ≍ p log p with M(p) = (log p)²/8 + O(log p). Restricting u ≤ (log p)^A does not shrink 𝓡. Ledger of the best
  pointwise inputs by category.
* Verdict (§3), SHARP flags (§4), census (§5).

## Main findings
1. **SHARP flags: none.** No known theorem reaches a single-p statement of type (a) or (b): not for all p, not for
   a thin set of non-B1 primes, not under GRH/RH. Every existence result found is averaged (over n, p, moduli or
   residues). Every pointwise-in-p result is an upper bound (Lenstra), class-blind (Li–Yang, Selberg–Hooley,
   Assing–Blomer–Li with f = p), needs intervals of length ≥ p^{1/2} (Matomäki; Younis even under RH), or stops at
   the window/sign layer (Pollack, GRH).
2. **Closest pointwise class-aware estimate:** Weil in modular-hyperbola form (Shparlinski Thm 13). Its error scale
   p^{1/2+o(1)} exceeds the (log p)² main term by ≍ p^{1/2}, which is the (J)6 number; no log-power refinement is
   known. Going below box area p^{3/2} for one residue is "out of reach" per the literature, tied to Selberg–Hooley.
   Area p^{1+o(1)} is reached only on average over residues (Garaev; KSWX §3.3). This is a statement about the cited
   methods, not a proved lower bound for (★) (review repair).
3. **Tied averaging (Remark 3.1):** every beyond-Weil result averages over a variable independent of the modulus.
   At one p the only free variables (u, C, q) are themselves the moduli. This is B2 from the literature side.
4. **Closest structural precedent:** Borwein–Choi (every N, up to one possible exception, is xy+yz+zx). It works
   via an exact class-number identity, i.e. a divisor of N + z² in an *interval*. For ES, finite fixed-level
   σ_k-identities are excluded by T1 ((J)7 Thm 9.1), and class groups see only the χ-shadow ((J)5 Prop 10.3). Not
   SHARP.
5. **Dyachenko 2511.07465:** the abstract's "Theorem 10.21" does not exist. Thm 9.21(III) builds its lattice from
   a presupposed solution, and the step from a lattice point to a solution is the B2 divisor event. The author's
   §11 concedes the general case is not proven.
6. **New refinements (PROVED, elementary):**
   * Lemma 3.2: (a⁴) never holds at odd squares. At a prime p ≡ 1 (8) the χ-shadow of the class is free when
     (u/p) = −1. This fails for p ≡ 5 (8) (p = 13, u = 5).
   * §3 item 2: length-based zero-sum forcing for windows needs q ≤ 2 log₂ p + 1, which fails infinitely often
     (least QNR, Graham–Ringrose; cited from memory).
7. **Census (EVIDENCE, primes ≤ 10⁶):**
   * (a⁴)/(★) is *not* an all-p target: R(p) = 0 at 9 primes (409, 577, 5569, …).
   * ES-five on the u-side never fails for p ≡ 1 (8). The least u is ≤ 17, and ≤ 2 for 89.9 % of these primes
     (60.3 % of p ≡ 1 (840)). At u ≤ 2 the class condition is vacuous and the event is a pure spin event at
     p + 1, p + 2. This refines (J)6: at one integer the sign layer is a factorisation fact too.
   * The window sub-event (b) fails at 8272 primes p ≡ 1 (4).
   * T1: no hits at the 499 odd squares.

## Verdict (Assessment)
H-B is **not feasible with known inputs**. Parity is not the binding constraint. For the cited methods the
constraint is the square-root error scale of complete sums at fixed modulus, together with tied averaging. The
restricted events are no easier for complete-sum methods (Lemma 2.1). The combinatorial (subset-product) route needs
factorisation statistics in every polylog-length interval, and pointwise results stop at length p^{1/2}, also under
RH. This confirms (J)6: H-B collapses into H-A. The six candidate input combinations, each with its missing piece,
are in §3.

## Review status
* Self-review via the review tool (deep reviewer): no FATAL. The MAJOR items were all repaired and are marked in
  the text:
  * the square-root "barrier" is restated as the error scale of the cited methods;
  * the box benchmark is separated from (★);
  * the spin extension is restricted to p ≡ 1 (8);
  * the zero-sum scope is narrowed;
  * the Elsholtz–Tao mean is corrected to log³ per prime for full Type II;
  * Blomer–Pascadi c^{1/32} is added;
  * the Borwein–Choi conditionality and the scope of the class-number exclusion are corrected;
  * the census population is fixed (60.3 % for p ≡ 1 (840)), with conjectural labelling.
* Minor items were repaired too, including the Li–Yang coefficient, the E6 date, the "iff" in B6, the U-range in
  Lemma 2.1, and composite windows.
* Not accessed: Hall–Tenenbaum *Divisors*; Hall (Acta Arith. 1976); BFI 1986, Heath-Brown on d₃, Garaev's p^{3/4}
  and Shkredov (secondary sources only, marked *sec.*); some journal references are given from memory and are
  marked so.

## Suggestions for the parent
* A ledger entry (J)-item for O255 (no headline theorem; Assessment + EVIDENCE + small PROVED lemmas).
* LITERATURE_2026 "Wave Z′ additions": Lenstra 1984, Erdős–Hall 1976, Shparlinski 2012, KMS 2017, Blomer–Pascadi 2026,
  KSWX, Matomäki 2016, Younis 2024, Borwein–Choi 2000, Li–Yang 2023, Assing–Blomer–Li.
* If H-B is pursued further, the only non-dead lead is a theorem with **untied** averaging at one p, i.e. a family
  in which the residue varies while the modulus stays fixed. The Garaev-type almost-all-residue results would then
  apply. None of the parametrisations (u, C, q) has this property.
