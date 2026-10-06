# Review R53 of EXCEPTIONAL_SPW2.md (O53, branch side-agent/weak-spw)

Reviewer: hostile side agent (branch side-agent/review-spw2). Reviewed
version: side-agent/weak-spw at ef0bfbd (merged into this branch).
Checked against EXCEPTIONAL_SPW.md (SPW1; Lemma 1.4, Thm 3.2, Lemma 3.1),
EXCEPTIONAL_INTERFREQ2.md (IF2; Def 1.2, Flat, Thm 5.2 + proof, Prop 9.1),
EXCEPTIONAL_KARY3.md §4.3. From-scratch scripts: scripts/review_spw2_*.py.

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| Lemma 1.1 (requirement) | (in progress) |
| Lemma 2.2 (near zone) | (pending) |
| Lemma 2.3 (interval support) | (pending) |
| Thm 3.1 (K-free edge bound) | (pending) |
| Lemma 4.1 (dual) | (pending) |
| EVIDENCE / Assessment labels | (pending) |

## Claim 1: Lemma 1.1

Re-derivation (independent).
1. SPW1 Lemma 1.4 mix R = (1 − 1/(2K))λ_N + R′/(2K) (needs only K ≥ 1/2 for
   R ≥ 0). Full class s (modulus e > CN ≥ N, one point of [1,N]):
   λ_N(s) = 1, so R(s) ≤ 1 − η/(2K). Sparse: R(s) ≤ 1/2 ≤ 1 − η/(2K) since
   η ≤ 1/2 ≤ K. Medium: λ_N(s) = c(s) so |R(s) − c(s)| = |R′(s) − c(s)|/(2K)
   ≤ Δ′/(2K). (P1) is convex. So SPW(C, σ = η/(2K), Δ₀ = Δ′/(2K)), σ ≤ 1/2.  ✔
   (The index sets (D, CN] and (N/2, CN] coincide for D = ⌊N/2⌋.)
2. IF2 Prop 9.1: θ = σ/(2(σ + τ + 1/(2C))), t = θ/2, s₀ = σ/2, Δ = 6θ + Δ₀.
   Since σ ≤ 1/2 and τ = O(1): 1/t = 4(σ + τ + 1/(2C))/σ ≤ c_C/σ, so
   log(1/t) ≤ log(K/η) + O_C(1). Δ ≤ 3 + Δ′/(2K), so
   log(1 + Δ(1+c)) ≤ log(1+c) + log 4 + log(1 + Δ′/K).  ✔ (bookkeeping right)
3. IF2 Thm 5.2 as *stated* assumes t ≥ e^{−S_A} and Δ ≤ e^{S_A}. Lemma 1.1
   applies it with no such hypothesis (its third bullet is precisely the
   regime t = N^{−c}). I re-read the proof of Thm 5.2: t enters only through
   the trivial case "KB ≥ tN" and the final line (1+Δ+Δc)B ≥ tNe^{−S′};
   the high-mass bound T_{>CN} < tN/s₀ + N needs only t ≤ 1, and the mean
   side (level λ ≤ (A + A₁ + 2)log N + S + λ₀) does not see t or Δ. So the
   hypotheses t, 1/Δ ≥ e^{−S_A} are cosmetic (they only make the conclusion
   "3/4-shaped") and the strengthened use is VALID — but it is an unstated
   extension of a cited theorem (defect m1).
4. s₀ = σ/2 = η/(4K), so the needed hypothesis is η/K ≥ 4N^{−A₁}, not
   η/K ≥ N^{−A₁} (absorb by A₁ → A₁ + 1). Trivial (m2).
5. The exponent "C′(log N)^{3/4}" without (log log N)^{3/4} relies on
   KARY3 Thm 4.1 replacing K2 Thm 5.1 inside IF Thm 2.5's mean side. KARY3
   §4.3 lists INTERFREQ Cor 2.3 at *pointer level, not re-reviewed*, and does
   not list IF2 Thm 5.2 at all. With level containing +S the self-consistent
   bound S ≤ C(c log N + S)^{3/4} ⇒ S = O((log N)^{3/4}) is fine, so I believe
   it, but the label should say "conditional on KARY3 §4.3 pointer" (m3).
6. "Exact requirement" / "polynomially small σ does *not* suffice for
   anything ES-relevant": Lemma 1.1 is a *sufficient* condition (an upper
   bound on the saving obtainable via this particular chain
   Lemma 1.4 → Prop 9.1 → Thm 5.2). Nothing is proved about necessity:
   a different mixing than Prop 9.1, or a sharper use of (5.1) than the
   final step, could lose less than log(1/t). The statement "σ = N^{−c} gives
   nothing" is true only as "this chain then yields only B ≥ N^{1−c−o(1)}".
   Overclaimed wording (defect M1).

Verdict Lemma 1.1: **SOUND-AFTER-REPAIRS** (bookkeeping correct; title and
third bullet overclaim necessity; relies on unstated hypothesis-free form of
Thm 5.2 and on the KARY3 pointer).
