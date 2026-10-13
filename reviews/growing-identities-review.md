# R170 — hostile review of GROWING_IDENTITIES.md (O170, branch side-agent/growing-identities)

Reviewer: R170. Reviewed commit: merged `side-agent/growing-identities` at start of review.
From-scratch scripts: `scripts/review_gi_*.py` (no author code reused).
Status: IN PROGRESS.

## Verdict table
(filled in claim by claim below)

### Lemma 1.1 (continuant / HJ form) — SOUND-AFTER-REPAIRS (wording only)
Re-derived by hand: `S_cS_g = [[cg−1, −c],[g, −1]]`, `S_cS_gS_f = [[cgf−c−f, −(cg−1)],[gf−1, −g]]` ✓;
`c − 1/(g − 1/f) = (cgf−c−f)/(gf−1)` ✓; det = 1 ⇒ (m,n) = 1; c ≥ 2 ⇒ m = gf−1 < n; uniqueness of HJ
expansions (entries ≥ 2) gives injectivity in both directions ✓. `S_aS_1S_b = S_{a−1}S_{b−1}` ✓ (both equal
`[[ab−a−b, −(a−1)],[b−1, −1]]`). `K⁻(a,4cd,b) = 4abcd−a−b` ✓.
From scratch (`scripts/review_gi_identities.py 300`): brute-force enumeration of the cubic vs. the set
{m ∈ [1,n): 4|m, (m,n)=1, r(n/m) = 3} for all n ≤ 300 — identical as sets of words (entries ≥ 2), 0 failures.
The restriction "entries ≥ 2" is essential: for n ≡ 1 (4), n ≤ 300, the W-certificates at
**n = 5, 17, 41, 65, 209, 241, 265 all have an entry 1** and there is no HJ-length-3 m ≡ 0 (4) at all (this
matches DEDEKIND_ES §4.2–4.3, where 17, 241, … are "solved by the boundary case"). See defect m1.

### Lemma 1.2 (fibration swap) — SOUND
Both fibrations re-derived (`f(cg−1) = n+c`; `(cg−1)(fg−1) = gn+1`) and checked by brute force: R(n) and W(n)
from the cubic agree with the g-fibred and the c-fibred sums (with the stated mod-4 conditions) for all n ≤ 300,
0 failures. The "sum over m first" form re-derived: for 4 | m, (m,n) = 1, r_m := −n⁻¹ mod m ∈ [1,m), the t's
are t = r_m (if r_m | m+1) and t = m+1 (iff r_m = 1, i.e. n ≡ −1 (m)); so exactly
`W(n) = #{4|m, (m,n)=1 : r_m | m+1} + #{4|m : m | n+1}`; the second ("boundary") term is 0 for n ≡ 1 (4).
Checked for all n ≤ 120, 0 failures. (The bound "∈ {0,1,2}" ✓.) See m2 for the vague "(+ boundary)".

### Lemma 1.3 and Proposition 4.1 (sign = Jacobi symbol at n) — SOUND (statement); identity form SOUND-AFTER-REPAIRS
Re-derived independently: for odd prime ℓ | u, tn ≡ −1 (ℓ) ⇒ (n/ℓ) = (−t/ℓ); n ≡ 1 (4) ⇒ (u/n) = (n/u);
t ≡ 3 (4) ⇒ (−t/u) = (−1)^{ε(u)}(t/u) = (u/t); u ≡ ε·2^{−j} (t) ⇒ (u/t) = (ε/t)(2/t)^j = ε(2/t)^j; hence
(m''/n) = ε·(2/(tn))^j, and j ≥ 1 with 4 | m gives 8 | tn+1, (2/(tn)) = 1. All coprimality conditions needed for
the Jacobi symbols hold since u | tn+1. t ≡ 3 (4) is forced by 4 | tn+1, n ≡ 1 (4) ✓. Hypothesis "4 | m" is used
only to get 8 | tn+1 when j ≥ 1. ✓
From scratch: all n ≡ 1 (4) ≤ 300 with **all** t ≡ 3 (4) up to 3n+12 (both classes), and n ∈ [10⁶, 10⁶+1600),
t < 400 (54 081 pairs, sympy divisors): 0 failures.
Consistency with DEDEKIND_ES Thm 4.5 (O169): with t = g, A = m = gf−1, m'' = cg−1 one has A·m'' = gn+1 ≡ 1 (n),
so (m''/n) = (A/n); Prop 4.1 (ε = −1) is exactly the "4 | tu−1 ⇒ (A/n) = −1" direction of Thm 4.5 (with
O169's letters n/A = [[v,t,u]] ↔ O170's [[c,g,f]]). **No discrepancy.** O170 does not claim the converse
direction of Thm 4.5 (on L₃, (A/n) = −1 ⇒ one of five slices), nor does it need it.
The identity `W = Σ_{D(n)}(1 − (m''/n))/2` is correct (only finitely many non-zero terms), but D(n) is infinite,
so "S = #D(n)", "W = (S − O)/2" and "|Σ_{D(n)}(m''/n)| ≤ #D(n) with equality iff ES fails" are ill-defined as
written. See defect M1 (repair is easy and makes the truncation t ≤ n+2 automatic).
