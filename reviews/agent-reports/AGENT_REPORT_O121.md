# AGENT REPORT O121 — (EFF) for DI Thm 7 / Drappeau Lemma 4.10; ET Type I ≪ N log²N

Branch `side-agent/eff-di7`. Main file `EXCEPTIONAL_TYPEI_LOGLOG3.md`; derivations `scripts/ttl3_*.md`.

## Claim
* **Thm 9.1.** (EFF) holds: TTL2's (DI7_ε) (DI Thm 7 and Drappeau Lemma 4.10 for interval/prefix coefficients,
  levels ≤ M₀ divisible by the modulus r of an even χ, uniformly in r, χ) holds with
  `C_ε ≤ exp(exp(A₀/ε))`, `A₀ = 24B_χ + 30`, `B_χ = 400 + 64·max(4,⌈B_W+1⌉) + 16 log(2+C_W)`
  (C_W, B_W = the absolute constants of the twisted Weil bound; A₀ < 2·10⁴ if B_W ≤ 3, C_W ≤ 10).
* **Thm 9.2.** `Σ_{p≤N} f_I(p) ≪ N log²N` (TTL2 Thm 4.1(ii) with Thm 9.1).
* Label: **PROVED relative to** (B1) the exact Petersson/Kuznetsov formulae (Γ₀(q); (Γ₀(L),χ) as in Dr Lemma 4.5;
  SL₂(ℤ)), (B2) Weil, (B3) twisted Weil with absolute constants, (B4) Selberg 3/16, (B5) λ₁(SL₂(ℤ)) > 1/4, and
  TTL's cited inputs — pending the parent's hostile review.

## Structure
* §1 toolkit: explicit divisor bound, log absorption, an explicit Gevrey-2 cutoff (`‖η^{(p)}‖ ≤ 8e¹⁶36^p(p!)²`).
* §2 DI's induction (8.19) made explicit from three inputs (P1) [(8.7)+Thm 14], (P2) [Lemma 8.1], (P3) [Thm 2]:
  `K₇ = max(2K₂Q₀, 10K₁, 6c)`, `Q₀ = max((90c)^{1/(10δ²)}, (2π)^{1/(2δ)})` ⇒ double-exponential class preserved.
* §§4–6 effective (P1)/(P2), Thm 2 (all three spectral parts, exceptional included), Thm 14 (U-form):
  `K_{T2} ≤ exp(exp(100/δ))`, `K₁₄ = 2^{1200}(1+K_{T2})(1+6/δ)³`, `K₁, c ≤ exp(exp(405/δ))`.
* §8 nebentypus: Drappeau's induction needs an **extra branch** — the switched parameter `C = πNY/(rQ)` can be `< N`
  (even `< 1`), where no induction hypothesis is available; handled directly by (P1χ). Uniform in r.

## Repairs to the literature found on the way (all minor; none affects DI/Dr's theorems)
DI p. 257: with DI's cutoff support (1/2,3) the derivative separation `|B/2√t| < |A−u|` fails (ratio up to 1.17);
a support in [3/4,9/4] fixes it. DI p. 272–273: pictured supports give only `16C/25 ≤ c ≤ 32C`, not `(C,16C]`;
narrower explicit cutoffs fix it. DI (8.3): lower bound not uniform near Y = 1 (fixed via Y ≥ 2³² + monotonicity);
(8.2) needs a `log Y` at κ = 0. DI p. 259 exponent 2s→3s; diagonal (5.2) asymptotic replaced by `≤ 2K²`;
Thm 13's separation uses six derivatives (beyond (7.7)); a cosh missing on p. 264; below (8.18) `Y₁ = Q+N`
(known from O116). Dr p. 17–18: modulus `S∞∞(m,n;qc)` should be `Sχ(m,n;rqc)`; single `g(q)` cannot majorise
`(Q,16Q]` (use DI's four enlargements); dx vs dx/x; N,Y interchanged; the C < N branch above.
Also: the twisting idea "even χ = ψ²" is **false** for globally-even χ with odd local components (e.g. χ₃χ₇ mod 21).

## Caveats / what to attack
The analytic derivations of §§4–6 and the twisted transfers were written by deep-mode subagents from the scan and
checked by me structurally (statements, ε-bookkeeping, key repairs against DI pp. 256–257, 270–278), then by three
independent deep-mode referees (`scripts/ttl3_review_R{A,B,C}.md`: no FATAL/MAJOR; MINORs logged/repaired in §9).
Numerical majorants such as `2^{1000}` were not re-derived by me. The numerical A₀ needs certified C_W, B_W.
Most attackable: `ttl3_thm2_effective.md` Steps 4, 7–9; `ttl3_thm14_effective.md` §2 (Lemma 7.1 replacement);
`ttl3_lemma81_effective.md` §2.2; the twisted resonance step and small-C branch.
