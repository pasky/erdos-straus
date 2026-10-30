# Hostile referee report: EXSET_CHAR_FORCING (Astra, round 4)

Reviewed snapshot: `55c1a52c`; entire document read. **Verdict: minor revisions remain; the main analytic conclusions survive.** ES remains OPEN.

R3's substantive analytic and hypothesis-status repairs pass; residual consistency issues are below. The new Observation 1.1(b) sentence also passes: use dyadic ranges and, if necessary, a smaller interval parameter ≤ min(C, 1) to absorb Proposition 5.2's second term.

## Verdict register — non-SOUND items only

| Location | Verdict | Finding |
|---|---|---|
| §6.4, final sentence (line 608) | MINOR — residual overclaim | “Above (log p)³ reach provably disappears” still reads as a cutoff theorem. Corollary 6.4 proves average/Markov statements in a fixed polylogarithmic q-range, not disappearance of every larger reached modulus. The repaired §§0 and 9 do not cure this surviving sentence. |
| §3.2, random-box paragraph (lines 214–215) | MINOR — internal inconsistency | “Typically about 3^{ω(x)} elements” still counts unreduced choices as distinct residues. For β < log 3 this exceeds the group order. §9 correctly distinguishes choices from elements; propagate that distinction here. The model's later truncation does not make this cardinality sentence true. |
| §5 status paragraph and §9 first bullet (lines 427, 710–711) | MINOR — residue dictionary | At a specified cell r, Type II requires e ≡ −r, but Type I requires e ≡ −r⁻¹ (mod q), since its cell is −e⁻¹. The shared “e ≡ −r … p + e (or ep + 1)” wording is wrong for Type I. Inversion permutes nonresidues, so the all-cell coverage discussion survives. |
| Propositions 5.1 and 5.1′ proofs (lines 345, 357) | MINOR — unrepaired proof detail | The bound m ≥ y/log y for odd primes is false over the stated finite range: at y = 17, m = 6 < 17/log 17 = 6.000254…. R3 already flagged this. The asymptotic exponents survive, but the finite-range proof needs correction. |
| §0 numerical row/bottom line; §6.3 majority-reach bullet (lines 25, 30, 587–588) | MINOR — scope/quantifier shorthand | “MR₁(1) at all p ≥ 10⁶” must say **sampled** p and specify the certified η = 0.2 margin; the §6.3 shorthand should use the same parameter. “No proof of any forcing reach” should mean no proved growing pointwise reach at the scales needed here, not denial of the certified finite reaches or classical fixed-q forcing. |

## Remaining required repairs

1. Replace §6.4's disappearance claim by the prescribed-q average/Markov statement, retaining q ≤ (log X)^C and the two-subfamily/height scope.
2. In §3.2 distinguish divisor-ratio choices from distinct residues, whose number is at most q − 1.
3. Separate the Type-II and Type-I congruences for e in §§5 and 9.
4. Repair the odd-prime lower bound in both moment proofs; justify the advertised finite-range bounds separately or restrict/restate them. Using m = (1 + o(1))y/log y suffices for the asymptotic applications, not the exact finite-range display by itself.
5. Make the summary's sampling, η and growing-reach qualifications explicit.

No source modification or commit is made. The numerical check used the requested memory limit and timeout; no empirical datasets were re-audited this round.
