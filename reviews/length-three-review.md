# R205 — hostile review of LENGTH_THREE.md (O206)

Reviewer: R205 side agent. Reviewed: LENGTH_THREE.md as merged from side-agent/length-three (report AGENT_REPORT_O206.md).
From-scratch scripts: `scripts/review_l3_*.py` (none import or copy scripts/l3_*).
**ES is not solved here; nothing below changes that.**

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Prop 1.1 (pentagon / A₂ frieze, (P), converse, formal vs interior) | SOUND |
| Cor 1.2 (five slices = five cluster variables ≡ 0 mod 4) | SOUND |

## Checks performed

**Prop 1.1 / Cor 1.2** (`scripts/review_l3_words.py 20000 3000`, 55 s). Own enumeration of all words (c, m, s) ≥ 1 with
0 < N ≤ 2·10⁴: 1 194 085 words, 610 533 interior. For every word: the ten |det(V_i, V_k)| equal the claimed λ's; the
five boundary points are in the cyclic order ∞ > c > h/m > N/h′ > 0 (so the pentagon is embedded and fans make sense);
all five Ptolemy relations computed generically from the λ-table; the generic Penner fan identity at each of the
five vertices; the five table identities of Thm 2.1 *as printed*; cs − r² = (c + s)/m. For interior words: h′ < N,
gcd(h′, N) = 1, and an independently computed HJ expansion of N/h′ is exactly [c, m, s]; and own-Jacobi check of Cor 1.2
on all 139 915 + (non-slice) interior words with N ≡ 1 (4). Set identity {h′ : interior words at N} = L₃(N) (L₃ computed
by HJ-expanding every A/N) for all N ≤ 3000. 0 failures. Controls: the set of N ≤ 2·10⁴ without an interior word is
exactly E_W = {2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510}; 105 has formal words but no interior word; (1, 4, 2) is a
formal word at N = 5 with L₃(5) = ∅; 69 of the 70 odd squares 9 ≤ N ≤ 2·10⁴ have interior words (9 does not), none has a
slice word.
By hand: V₄ = mV₃ − V₂, V₅ = sV₄ − V₃ = (N, h′); det(V₃, V₅) = c(ms − 1) − N = s; the five quadrilateral Ptolemy
relations (drop V₅, V₁, V₂, V₃, V₄) give exactly the five lines of (P); the converse identity
hh′ − mN − 1 = m(K − N) is correct. N > 0 forces h, h′ ≥ 1 (h = 0 or h′ = 0 forces N = −1), so V₅ ≠ ∞ and the
pentagon is non-degenerate on the whole domain. DK's (v, t, u) = (c, m, s), A = tu − 1 = h′, A* = tv − 1 = h, so DK Thm
4.5's five conditions are exactly 4 | h′, h, m, s, c as claimed.

## Defects

(numbered below as found)
