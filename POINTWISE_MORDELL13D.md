# POINTWISE_MORDELL13D — closing exceptional root classes with a complete-witness hybrid DFS (task O103)

Status: work in progress (side agent O103, branch `side-agent/r13-hybrid-close`). Labels as in DISCOVERIES.md.
Continues POINTWISE_MORDELL13C (§6 Thm 6.1, §8 Comp 8.3 and plan).

## 1. The C complete-witness engine `scripts/m13d_wit.c`

Input: a node `x + Lℤ` (`4 | L`, `gcd(x,L)=1`, `L < 2¹²⁶`), optional `req` (a prime power exactly dividing L).
Output: all (or the first) ET classes (seven families, `mordell_lib` conventions) with modulus `M | L`
(and `req | M`) containing the node. Same mathematics as `m13c_witness.py` (13C §2), reorganised:

* **(A) II3 / I2 / I3** (`(a,d,f)` with `f` odd, `gcd(f,4ad)=1`, `M = 4adf | L`, `x ≡ −f (4ad)`): loop over odd
  `f | L`; then `m = 4ad` divides `G_f = gcd(L_f, x+f)`, `L_f` = part of L coprime to f; enumerate
  `a·d = Q | G_f/4` and test `f | x+4a²d` (II3), `f | ax+d` (I2), `f | x²+4a²d` (I3).
  Equivalent to 13C's loop (pairs (a,d), `f | gcd(K_c, ·)`, `f ≡ −x (4ad)`): both say `f·4ad | L`, `gcd(f,4ad)=1`.
* **(B) I1 / II1 / I4** (modulus `m = 4Q | L`): `f0 = −x mod m`, `g0 = −x⁻¹ mod m` (`x⁻¹` taken mod L).
  I1 `(a,d,f)`, `ad=Q`, `f | am+1`, `f ≡ −x (m)`: either `f = f0` or `g = (am+1)/f = g0` (13C §2); in both cases
  `h ∈ {f0,g0}` must divide `am+1`, i.e. `a ≡ −m⁻¹ (mod h)`, enumerated among divisors `a | Q`.
  II1 / I4 `(a,b,e)`, `ab = Q`, `e | a+b`, `e = f0` resp. `g0`: since `a+b ≥ e`, `min(a,b) ≤ 2Q/e` — scan the sorted
  divisors of `L/4` up to `2Q/e`.
* **(C) II2** `(a,d,f)`: `f | L`, `f ≡ 3 (4)`, `ad | A = (f+1)/4`, `x ≡ −4a²d (f)`. Per L, A is factored
  (trial division + Miller–Rabin + Pollard rho, 128-bit) and the residues `−4a²d mod f` are tabulated.
* 128-bit arithmetic, `mulmod` exact for moduli `< 2¹²⁷`. The Miller–Rabin test (20 prime bases) is used only
  to *factor* A in (C); a wrong "prime" verdict could only lose II2 witnesses (never create a false one —
  every witness is re-checked by the tree checkers).

**`req` (used inside the DFS).** If a node `x mod L` is known to lie in no class with `M | L`, a class covering
a child `y mod Lp` with `M | Lp` must have `v_p(M) = v_p(Lp)`; `req = p^{v_p(Lp)}` restricts the search accordingly.

**Validation.** (i) every unit `x` mod `L ∈ {9240, 10920, 65520, 720720}` (156288 nodes): full witness sets of
the C engine and `m13c_witness.witness_all(first=False)` agree — **0 mismatches**.
(ii) `m13d_validate.py /tmp/o100/t418_100.json 200 1 0 2 5` (logs/o103_val_trunc.log): 200 random open leaves
of the 13C §8.2 tree, each truncated to `x mod L'` (`L'` = L without its k largest prime powers, k ∈ [2,5] —
the Python engine costs ≈ ×3.5 per prime; `L'` ≈ 10¹⁰–10¹⁵): full sets agree, **0 mismatches** (90 nonempty).
(iii) `req` mode, `m13d_validate.py … 20 3 20 5 7`: all 583 children `y mod L'q` of 20 truncated leaves:
C set (req) = Python set restricted to `req | M`, and first-mode answers lie in it — **0 mismatches**
(only 2 nonempty; a heavier req check at k ∈ [3,4] and 30 untruncated / k ≤ 2 leaves: logs/o103_val_deep.log).

Speed (300 random open leaves of the 13C §8.2 tree, `L ≈ 10¹⁸–10²⁰`, 14–15 primes): ≈ 45 ms per node for the
full set, single core. 31 of the 300 leaves (10%) lie in no class with `M | L` (13C Comp 8.3 found 4%, sample of 52).

## 2. Hybrid DFS `scripts/m13d_dfs.py` — first runs on root 418321 (EVIDENCE)

**Run 2.1 (CK = 0: split chosen by tables `M ≤ 10⁶` as in 13C; C engine at every popped node).**
`m13d_dfs.py 418321:720720 1000000 100 3 5000 3600 …` (484 s): 5000 pops, 2313 covered by the C engine
(46%), open mass `5.2·10⁻⁹` of the root (13C Comp 8.2: `1.95·10⁻⁸` after 142088 nodes), but the queue still grows
(14874 open at stop; ≈ 7.4 children pushed per expansion, ≈ 4 of them open w.r.t. all `M | L`). Supercritical.

**Run 2.2 (CK = 6: the 6 candidate splits with fewest table survivors are scored by the C engine; split = min
(#children open w.r.t. all `M | L·q`, p)).** Same root, emax 3, 3600 s (logs/o103_dfs418_ck6.log): 6200 expansions,
open mass `5.1·10⁻⁹`, 16857 open leaves (depth 11–14). Open children per expansion by `log₂ L'`:
≈ 2.5 (bits 40–50), 3.2 (50–55), 3.6 (55–60), 3.0 (60–65) — not decreasing: supercritical.
*Shape of the open set:* every open leaf has `x ≡ 1` mod 16, 9, 25, 17; ≈ 85–90% have `x ≡ 1` mod 19, 23; 97–100% are
quadratic residues mod 19, 23, 29, 47 (cf. the non-square lemma, 13C §1: classes covering points that are
squares at all `q ∉ {11,13}` need the non-square witness 11 or 13). Most open leaves sit at the exponent caps
(`2⁶3⁴5³7²⁻³`), so the run cannot separate them from the 2-, 3-, 5-adic point `x = 1` → next: raise emax.

**Run 2.3 (emax 6, CK 6).** Minimising the open-child *count* now prefers raising 2- and 3-powers: after 9200 pops
open mass `4.6·10⁻⁶` (×900 worse than 2.2), open children per expansion still ≈ 2.85 (bits 45–55). Stopped.

**Run 2.4 (subtrees of single deep open leaves of run 2.2; emax 4, CK 6, 900 s each; logs/o103_sub6.log).**
`3466176103402110001 mod 14793247696034808000`: 71 expansions → 150 open leaves; `327585843065779201 mod
9127748578404456000`: 68 → 151. Deep nodes are as supercritical as shallow ones, and ≈ 13 s per expansion
(C engine at `L ≈ 10¹⁹–10²¹` and up to 6 candidate splits).

**Computation 2.5 (one node, all splits).** For the first node of 2.4, the complete engine counts the open children of
*every* split `q` (each prime `< 120`, or the next power of a prime of L): minimum **2** (at `2⁷`: 2/2 and `3⁵`: 2/3);
best non-trivial: `29` 4/28, `37` 5/36, `53` 6/52, `11²` 5/11; powers of primes where `x ≡ 1` (17, 23, 31, 43, 47, 5, 7)
leave ≈ all children open; new primes `> 60` leave 20–40% open. No split leaves ≤ 1 open child.

**Computation 2.6 (20 random open leaves of run 2.2, all splits, primes < 120; logs/o103_minopen20.log).**
Minimum number of open children over all splits: 0 (3 nodes), 1 (9), 2 (8); mean 1.25. The argmin is mostly
`2⁷` or `3⁵` — **beyond the exponent caps of runs 2.1–2.2** (2⁶, 3⁴), which is why those runs looked so
supercritical — or a new prime 29, 37, 53. Next: unbounded-ish 2-/3-adic refinement, always C-scored.
