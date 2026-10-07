# AGENT REPORT O88 — exceptional sets in short intervals and progressions

Branch `side-agent/short-intervals`; deliverable `EXCEPTIONAL_SHORT.md`.
All PROVED items are relative to the 3/4 note (thm:assembly, lem:identity),
so they inherit its INTERNALLY PROVED (unrefereed) status.

Results
1. **Theorem 1 (PROVED rel. note).** For every interval I of length H ≥ 2,
   `E(I) ≪ H exp(−c(log H)^{3/4})`, uniformly in position, for **all** integers.
   Hence `E((x,x+H]) ≪_θ H exp(−c θ^{3/4}(log x)^{3/4})` for `H ≥ x^θ`: the brief's
   target holds exactly in the range `H ≥ x^ε`. Proof: the note's majorant
   ν_X is shift-uniform (eq:transfer works on any interval; choose X by H,
   `log H ≍ (log X)^4`), and a new local smooth-part decomposition
   (n = d·m, d y-smooth, m exceptional coprime to P_y ⇒ ν_X(m) = 1 since
   lem:identity applies to all n) replaces the note's global Rankin step.
2. **Theorem 2 (PROVED rel. note).** `E(I;q,b) ≪ q_1 (H/q) exp(−c(log(H/q))^{3/4})`,
   q_1 = X-smooth part of q, X = exp(α(log(H/q))^{1/4}); so uniform in b for
   `q ≤ exp(c'(log(H/q))^{3/4})` (covers q ≤ (log x)^A), and for q with all primes
   > X (e.g. prime q up to H^{1−δ}). Large smooth q blocked by fibre-adversarial
   conditioning of the void lemma (Remark 2.2, OPEN).
3. **Primes (Cor 3.1, PROVED rel. note).** No primes-in-short-intervals input
   is needed: `E_pr((x,x+H]) ≪ (H/log x)e^{−c(log H)^{3/4}}` once
   `H ≥ exp(C(log log x)^{4/3})`. Prime input (BHP H ≥ 2x^{0.525}; Huxley x^{1/6+ε}
   for almost all x) only for relative densities (Cor 3.2; (b),(c) ranges quoted,
   not re-verified).
4. **Lower end (Prop 4.1, PROVED, trivial).** The target form for any
   H with `C·H < e^{c(log x)^{3/4}}` (strict; in particular polylog H) implies ES for all large n.
   For `e^{c(log x)^{3/4}} ≲ H ≤ x^{o(1)}` Theorem 1 gives only `(log H)^{3/4}`;
   beating it needs either θ_win > 3/4 (⇒ global θ > 3/4) or position-dependent
   input. For shift-uniform methods the threshold question is exactly (W) of
   EXCEPTIONAL_WEIGHTS; no Jacobsthal/Maier-type windows at the 3/4 scale are
   known (OPEN).
5. **Literature/novelty (Assessment).** Nothing found; but shift-uniformity is
   routine (Vaughan's 2/3 presumably transfers; campaign's EXCEPTIONAL_WEIGHTS
   Prop 5.1(a) already notes it for primes/avoiders). Novelty is modest: all-integer
   local transfer, progression version, no-prime-input observation, Prop 4.1 framing.
   Li Delang / Yang / Jia not checked directly.

No numerics (pure deduction); replay = audit points in §6.
Suggested ledger entries: Theorem 1, Theorem 2, Cor 3.1 (PROVED rel. note).
