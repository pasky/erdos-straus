# Referee report R33: `paper/es-subexp-note.tex` (branch side-agent/omega-paper-v4)

Referee: hostile side agent `side-agent/referee-subexp`. Merged author branch at
`ae9204b` (normal merge, since ff-only was impossible: main had moved).

Status: IN PROGRESS (written incrementally).

## Per-claim verdicts

| Item | Verdict | Notes |
|---|---|---|
| Lemma 2.1 (atoms) | SOUND | re-derived: u_q=max(0,d−a), w_q=d−2u_q, v_q=a−u_q−w_q ≥ 0 checked; brute force below |
| Lemma 2.2 (class of one) | SOUND | re-derived |
| Lemma 2.3 (mass bound) | SOUND | re-derived every step; g-symmetry and inner-sum bound brute-forced (`scripts/review_r33_atoms.py`, ratio ≤ 0.65); ET Prop 1.4 checked in source (see minor point 1) |
| Lemma 2.4 (iterated quarantine) | SOUND | #prime factors > z of M ≤ T is ≤ ⌊Λ/log z⌋ = k; pairs → atoms injection |
| Def 2.5 / Lemma 2.6 (pairs + lifts) | SOUND (see minor points) | |

## Numbered defects

1. MINOR (Lemma 2.3(b) proof, and intro). ET Prop 1.4 as stated in the source
   (arXiv 1107.1010, p. 6) is `Σ_{a≤A}Σ_{b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)`
   for A,B>1 and k ≪ (AB)^{O(1)}. The paper's use (k=4, so log(1+k)=log 5
   is absorbed) is correct, but the paper never states the result. Repair:
   quote the statement, including the `log(1+k)` factor, in a cited-result
   box like Theorem 3.1, so that “proved modulo [ET, Prop 1.4]” refers to
   something visible. Also: the paper's own k (the event-support size) clashes
   with ET's k; rename one of them in the proof.

(further points below)
