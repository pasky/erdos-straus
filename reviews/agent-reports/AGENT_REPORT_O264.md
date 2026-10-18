# AGENT_REPORT O264 — why 193/2521 are hardest in both worlds (cheap check)

Branch side-agent/hard-pair. Main file HARD_PAIR.md; memos BRAINSTORM/z34_slice_residue.md, z34_common_cause.md;
scripts scripts/z34_{dict.py, scores.c, check_scores.py, ranks.py, smooth_cell.py, smooth_matched.py}; logs logs/z34_*.
Self-review: one deep reviewer pass, with no FATAL and 5 MAJOR findings (a false reverse implication in Thm 1.2(e), smoothness ⇏ all small primes QR / ⇏ M_σ | p−1,
an unmatched control sample, Astra scope overstatements, correlation promoted to causation) plus minors; all repaired in place.

**Goal 1 (PROVED, elementary; exhaustive check ≤ 10⁵).** Astra's source pm² + 1 = qs and López's Type A cp + 1 = qa are one
equation qs = pc + 1 ("generalized source", point (sh/c, psh, ph)). Astra requires c = m², Type A requires c | h = (q+1)/4,
and per slice the only candidate is c_q = −p⁻¹ mod q (so N₁(p) = #{q : c_q | h}). Astra source integral on arrival ⟺ m² | h ⟺
Type A with square c. Hence Type A failure ⟹ no Astra source on any slice is integral on arrival, and (m = 1) the odd part of p + 1
has only primes ≡ 1 (4). The converse is false (314 primes ≤ 10⁵), and "Type A fails ⟺ no genuine source" is false (genuine sources
exist on every split slice). 29 % of Type A solutions lie on non-split slices (outside every Astra lattice).

**Goal 2 (EVIDENCE + Assessment, all 39 175 p ≡ 1 (4) ≤ 10⁶).** Six scores (N₁, f_II, m₀, S = lattice-ES slices, e₀ = least
Type I level, L_I). Spearman 0.02–0.80; count scores 0.43–0.80. The coarse profile (χ_p(3..13), p mod 8) accounts for
27–79 % of the variance (S most, 79 %). Residual correlation stays 0.14–0.72 for the count scores and is ≈ 0 for the least
scores. The size-matched smooth-(p−1) cell has 7–11× the joint-extremeness rate. Astra's 193 certificate ("no primitive Type II
target with a = 1") is literally N₁(193) = 0. Its 2521 certificates imply our m₀ = 23 and e₀ = 15 but are stronger and differently
scoped. 193 and 66529 are Type-I-easy (e₀ = 3); only 2521 is extreme in all six scores.

**Goal 3 (Assessment).** Mundane: local profile + shared B2 draws + partial definitional overlap. No extra structural coincidence
found and no new mechanism. The one-residue table (HARD_PAIR §1) is a dictionary, not an existence tool. ES is not solved.

Suggested ledger entry: (J)-level "HARD_PAIR: Type A = generalized Astra sources with c | h; 193/2521 overlap explained
(Assessment) by smooth p−1 + shared B2 + definitional overlap; no mechanism".
