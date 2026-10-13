# R164 — hostile review of O164 `WINDMILL_REDUCTION.md` (§1–§10)

Reviewer branch `side-agent/review-windmill-reduction`; merged `side-agent/windmill-reduction` at review start.
From-scratch scripts: `scripts/review_wr_*.py` (none of the author's `wr_*` code reused).
**ES is not solved; nothing in O164 claims otherwise.**

## Summary verdicts

| item | verdict |
|---|---|
| §1 Computation 1.2 + dictionary | SOUND (re-certified independently to 20000; see D1, D2 minor) |
| §2 Lemma 2.1, Cor 2.2 | SOUND |
| §2 Computation 2.3 (15 / 267; 78 no reduced) | SOUND (reproduced exactly, independent code) |
| §2 Lemma 2.4 | SOUND-AFTER-REPAIRS (D3: positivity hypothesis missing; statement false as written) |

(table extended below as the review proceeds)

## §1 — Zagier windmill ↔ rivers

**Independent check** (`scripts/review_wr_zagier.py lo hi`). h⁺(p) is computed *without* the river map R: Gauss-reduced
indefinite forms of disc p, cycles of the standard ρ-operator (Buchmann normalisation), canonical cycle representative.
Then: ζσ-cycles on X(p) are enumerated, each cycle's forms `[y,x,−z]` are reduced to a class; checked that (a) each cycle is
contained in one class, (b) cycles ↔ classes is a bijection, (c) `#cycles = h⁺(p)`, (d) `2·|cycle| = ` R-period of the river
(R as defined in the doc, implemented separately), (e) ζ maps the cycle of C onto the cycle of `[a,−b,c]` = C⁻¹ and is
self-paired iff C is principal; ζ is verified to be an involution of X(p).
Result: **0 failures for all 1125 primes p ≡ 1 (4), p < 20000** (author: p ≤ 1300). p = 1297 reproduces
h⁺ = 11 and cycle lengths `[11,11,11,11,13,13,17,17,21,21,37]` (doc writes `[11,…,37]`, consistent). Class numbers
h(229)=3, h(257)=3, h(401)=5, h(577)=7 agree with tables.

The "Reading" paragraph: `σρσ = σζ = ρ⁻¹` and `ζρζ = σζ = ρ⁻¹` verified by hand. Fixed points: ζ fixes exactly
`x = y` (middle piece), giving `(1,1,(p−1)/4)` ↦ principal form; σ fixes `y = z` ↦ `[a,b,−a]`. Correct.
Genus theory: disc p prime ⇒ one genus, 2-rank 0, h⁺ odd, principal class the only ambiguous one. Correct.

Verdict: **SOUND**, with two minor presentation defects (D1, D2).

## §2 — class-group form of Type II

**Re-derivation of Lemma 2.4.** `B = 4gb`, `B² − 4kc = −4gp` ⇒ `kc = g(p + 4gb²)`. `4gb | k+1` ⇒ `gcd(k,g) = 1` ⇒ `g | c`,
so `c = ge`, `ke = p + 4gb²` (the doc asserts `c = ge` without this one-line reason; fine). `ke ≡ p`, `k ≡ −1 (mod 4gb)`
⇒ `4gb | p + e`. `N = (p+e)/4`, `bg | N`, `α = N/(bg)`, `β = b`. `4N ≡ p ≡ −4gb² (mod e)` ⇒ `4gb(α+β) ≡ 0 (mod e)`;
`e ≡ −p (mod 4)` is odd and a common prime of e and bg divides `ke − 4gb² = p`, so `e | α+β` once `p ∤ bg`.
The bound `bg < p`: with `X = 4gb`, if `bg ≥ p` then `X ≥ 4p`, `e ≥ X − p ≥ 3X/4`, `k ≥ X−1`, so
`(3X/4)(X−1) ≤ ke = p + Xb ≤ X/4 + X²/4`, i.e. `X ≤ 2`, contradiction. Correct. Integrality of y, z and the identity
are then immediate. **But all of this uses `k > 0` (hence `c, e, N > 0`)**, which Lemma 2.4 does not state — see D3.

**Bound `b ≤ (p+1)/3` (Comp. 2.3, g = 1).** `k ≥ 4b−1`; if `4b > p` then `e ≥ 4b − p`; `(4b−1)(4b−p) ≤ p + 4b²` ⇔
`12b² ≤ 4b(p+1)`. For `4b ≤ p` the bound is automatic. So the search range is exhaustive. Correct.

**Independent computation** (`scripts/review_wr_esforms.py 20000`, enumerates for each b the smaller of the two cofactors
in its residue class): 267 primes; **no ES-form for exactly 15** = {97, 193, 673, 1033, 1297, 1777, 2473, 3361, 6481, 7681,
7753, 8017, 9433, 12433, 15313}; **78 with no reduced ES-form** — both match the doc. Lemma 2.4's explicit formula
verified exactly (Fractions) on 11575 positive ES-forms, p < 3000, g ≤ 5 (doc: 4360 instances; different enumeration).

Cor 2.2's equivalence `4b | p+e ⇔ 4b | k+1` (for `p ∤ b`): both directions force e odd and `gcd(e,b) | p`; correct.

## Defects (numbered; FATAL / MAJOR / MINOR)

**D1 (MINOR, §1 "Reading", line "The principal cycle has odd length L_1/2 (because |X(p)| = Σ_C L_C/2 …)").**
The oddness of `|X(p)|` is itself obtained from ζ having a unique fixed point — i.e. Zagier's argument. So the sentence
"Zagier's proof is the statement *the principal river has odd half-period*" is a *reformulation*, not an independent
proof route: in the doc the odd half-period is derived from Zagier, not vice versa. Repair: say explicitly that the
odd half-period is equivalent to (and here deduced from) the ζ-fixed-point count; an independent proof is Smith's /
Legendre's continuant-palindrome argument (cite where it shows the principal period is odd for p prime ≡ 1 (4)).

**D2 (MINOR, §1 Computation 1.2 / "Reading" label).** The Reading is "PROVED given 1.2's structure", but 1.2 (i)–(iii) is
only CERTIFIED for p ≤ 1300 (now p < 20000 by R164). As written, the general dictionary is CONDITIONAL on a statement
proved nowhere in the doc. It is in fact a known theorem (folklore; e.g. the literature on "Zagier's one-sentence proof
and reduction of binary quadratic forms"); either give a reference or a proof sketch (each ζσ step is a composite of
R-steps, by Observation 1.1, and covers exactly two R-steps), or relabel the general statement CONDITIONAL/folklore.

**D3 (MAJOR — false as stated, trivial repair; §2 Lemma 2.4 statement, and AGENT_REPORT_O164 Results item 2).**
Lemma 2.4 says "a form `[k,B,c]` of discriminant −4gp"; it omits *positive definite* (Cor 2.2 has it). Without it the
statement is false — it would prove ES for every p: `[−1, 4g, −g(p+4g)]` has disc `16g² − 4g(p+4g) = −4gp`, `4g | B`,
`B | k+1 = 0` (script part (c)). The proof silently uses `k > 0` (positivity of e, N, y, z). Repair: insert
"**positive definite** (i.e. k > 0)" in Lemma 2.4 and in the report's restatement; add the one-line reason
`gcd(k, g) = 1 ⇒ g | c` for `c = ge`.
