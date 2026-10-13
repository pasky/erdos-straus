# R176 — hostile review of O176 (DIFF_DEEP.md + BRAINSTORM/bsC_*.md)

Reviewer: side-agent/review-diff-deep. Merged `side-agent/spark-diff-parity` at start. From-scratch scripts:
`scripts/review_dd_*.{c,py}`. **ES is not solved anywhere; nothing below changes that.**

(in progress — sections are added claim by claim)

## Verdict per claim

| Claim | Verdict |
|---|---|
| DIFF_DEEP Thm 2.1 (algebraic bijection + `4h ∣ gcd(h,G)²`) | **SOUND** (re-derived; brute force exact for all odd n ≤ 2001) |
| Thm 2.1 geometric reading | SOUND-AFTER-REPAIRS (see D-list) |
| Prop 1.3 (∀E false; τ(e) maximal orders) | SOUND-AFTER-REPAIRS (τ(e) correct for all e; ET citation wrong) |

## Checks performed

### Thm 2.1 (algebra)
Re-derivation. ET Type II: a,b,c,d ≥ 1, `4abd = n + e`, `a + b = ce`; so `4abcd = cn + a + b` and
`(4acd−1)(4bcd−1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1`. Thus h := (ff'−1)/n = 4c²d = cM (M = 4cd), M | f+1, f'+1,
so M | G and h | cG. Conversely d = h/4c², M = h/c | G gives a, b ∈ ℤ_{>0}, and `abM − a − b = nc` is the ET
equation with e = (a+b)/c — but **e ∈ ℤ needs a separate line**: from `4abd = n + (a+b)/c` and 4abd, n ∈ ℤ,
(a+b)/c ∈ ℤ. (The author's ⇐ cites "(I)4's criterion", which contains this; fine.) Minimal c: h/g divides every
valid c, so 4c² | h is weakest at c = h/g; gives 4h | g². Edge h = 0 (f = f' = 1) is excluded by 0 ∤ cG. Correct.

Brute force (`scripts/review_dd_thm21.c`, C, 0.3 s): tuple side by the naive ET loop (a ≤ b, d, e = 4abd − n,
e | a+b); triple side by c, d with h = 4c²d ≤ (n+5)² (4× the analytic bound (n+5)²/4 that I derived on the triple
side), f ≡ −1 (M), f | 1 + nh, f' ≡ −1 (M). **All odd n ∈ [3, 2001] (1000 values, 21 odd squares): the two sets of
(f, f', c) coincide exactly, 16054 tuples, no duplicates, 0 solutions at odd squares.** (Author's enumerator gives
the same total 1120 for n ≤ 301.) The "iff 4h | gcd(h,G)²" part checked independently
(`scripts/review_dd_thm21_iff.c`): all 3 556 994 factor pairs f ≤ f' of 1 + nh, 1 ≤ h ≤ n², odd n ≤ 151 — predicate ⟺
existence of c, 0 disagreements, and no predicate-true pair beyond h ≤ (n+5)²/4.

### Prop 1.3 / bsC_supersingular_transfer Prop 3
* τ(e) count: the maximal orders of M₂(ℚ_ℓ) containing the Eichler order of level ℓⁿ are the n+1 vertices of the
  geodesic segment — true for every n, so the global count is ∏(v_ℓ(e)+1) = τ(e) for **non-squarefree e as well**.
  Checked by brute force on the Bruhat–Tits tree (`scripts/review_dd_tree.py`: ℓ = 3, 5, n ≤ 4, all vertices within
  radius n+2: exactly n+1 stable lattices). The local argument (−d a unit square mod ℓ^{v} since e | 4a²d + 1, ℓ ∤ 2d;
  Hensel; idempotents ⇒ [[ℤ_ℓ, ℓ^i],[ℓ^j, ℤ_ℓ]] ⇒ Eichler of level ℓ^{i+j}) is standard and correct.
