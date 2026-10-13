# AGENT REPORT O181 — spark relay H: degree-k Diff-parity over F_q(T), odd-degree descent (checkpoint 1)

Branch side-agent/drinfeld-degree-k (merged side-agent/spark-higher-reciprocity and main incl. R177). Deep file
DRINFELD_ES.md; memos BRAINSTORM/bsH_*.md (11, indexed in BRAINSTORM/README.md); scripts scripts/bsH_*.py.
**ES is not solved; no infinite case of ES or ES_q is claimed.**

## SHARP:
1. **The ES_q surface over F_q(T) carries Bright–Loughran classes of order q − 1 over the base field (μ(F) = F_q^*;
   no corestriction, so LDP A.1 does not apply), and their odd part vanishes identically on every monic integral
   point** (DRINFELD_ES Thm 2.2, PROVED). Proof: a Steinberg identity valid over any field,
   α_ζ(u) = (−u₂/u₃, −1)_ζ + (λu₁ − 1, −u₂/u₃)_ζ, makes every finite local invariant away from P a power of −1
   (the residue of λu₁ − 1 is the ES target −1), sign normalisation does the same at ∞, and reciprocity
   handles P. Cor 2.3: on Type II points inv_P α_ζ = (−f/P)_m, i.e. the BL order-m class *is* the order-m
   Kudla symbol. Numerically 0 nonzero odd invariants on > 20 000 solutions (q = 7, 13, 19; m = 3, 9).
2. **Function-field anatomy of the "degree-2 accident" (Assessment resting on PROVED Lemmas 1.1 and 3.2):**
   F_∞^*/U₁ = F_q^* × ℤ (sign × degree). Order-k invariants at ∞ of sign-normalised data are degree characters.
   An order-k T1 needs a target of order k (ES has −1: order 2) *and* a pinned degree (no positivity can pin it).
   Twisted targets A/P = c₁/X + c₂/Y + c₃/Z do produce a genuine order-3 reciprocity, and at cubes confine all
   Type I/II solutions to the trivial degree class (Thm 3.3, PROVED; EVIDENCE on 4 074 points), but never
   sterilise. This also explains FUNCTIONFIELD_ES's "no odd-square obstruction" as the k = 2 case.
3. R177 D2c's Kottwitz form: over F_q(T), PGL₁(D) with inv_∞ D = 1/k has an incoherence group of order k (it is
   Br[k], ABHN) — the object exists; ES_q's coupling to it is exactly α_ζ, and Thm 2.2 says Diff_m(u) = {∞} for
   all ES_q points (odd m): the incoherence is never absorbed at a finite place.

## Results by goal
(1) Function fields. PROVED: k-th power law (P/f)_k = ε_k^{(1+deg f)(1+deg Ad)−1} (Prop 1.2); Kummer CM data
f^{1/k} of Type II moduli split completely at P for odd k, hence never embed in the rank-k supersingular algebra
D_{P,∞}^{(k)} (Thm 1.3); Thm 2.2; Thm 3.3. EVIDENCE: k-th powers are *enriched* ×≈k (T1 reversed). Forcing via
rank-k class sets: genus-vacuous (§5; Assessment with classical inputs, Wei–Yu mass formula cited from memory);
LSV complexes: B3. No obstruction and no forcing mechanism for ES_q.
(2) Number fields, odd-degree descent: closed with proof (§4): Prop 4.1 (parity over an odd-degree F' ⊂ ℚ(ζ_M)
sees f only as a coset H ∖ H'; equality with {−1} forces F' = ℚ(ζ_M)⁺, even degree; 81/81 pairs checked for
M ≤ 120); Prop 4.2 (odd-degree norm descent yields certificates for p·R_r(p), not p). FF remark: Carlitz real
subfields often have odd degree, but Prop 4.2 still kills descent.
(3) Other: x*_c = rec_T((1 + cT)^{−1}) is a wild-inertia element at T (PROVED, class field theory) and a profinite
square — the FF analogue of the T1-obstructed points rec_2(u), u ≡ 1 (8), over ℚ, with T1 removed (memo
bsH_lubin_tate_sterile). Yun–Zhang / Feng–Yun–Zhang higher theta series: still quadratic parity.

## Labels / caveats for the reviewer
* BL Props 2.5–2.6 are used over F_q(T) in odd characteristic for the prime-to-p part (Assessment that BL's proof
  transfers; only α_ζ ∈ Br of the function field and the symbol identities are actually used by Thm 2.2, and those
  are characteristic-free). Thm 2.2 needs P a prime power (else only the sum over v | P is controlled).
* Lemma 3.2 assumes some denominator has degree > n − deg A (true unless c₁ + c₂ + c₃ = 1).
* Literature citations from memory: Rosen Thm 3.5 numbering, Pierce §13 embedding criterion, Wei–Yu, FYZ.
* §6 Diff_m is my definition (Kudla-style), not a theorem from the literature.

## Sparks (not pursued)
* Profinite squares vs O(3, T²): is the closure of {Q²} more often obstructed than random slice points? (A test of
  "T1 point with T1 removed".)
* Twisted ES with c₁ + c₂ + c₃ = 1 (all three denominators of minimal degree): the degree character degenerates
  and the ∞-invariant might be pinned — the one place where a full order-m sterility could occur.
* Higher Siegel–Weil for PGL₁(D), inv_∞ = 1/k, over F_q(T): the genuine order-k Kudla theory (no ES coupling by
  Thm 2.2, but intrinsically new).
* Char 2/3 (where FF coverings are theorems): the wild (p-power) part of Br F_∞ — Artin–Schreier–Witt symbols —
  is untouched here; does the ES_q target interact with it?
