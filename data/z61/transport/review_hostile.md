# z61 TRANSPORT — hostile review

Reviewer: independent deep-mode review subagent (`openai-codex/gpt-6-astra`).
Reviewed range: `347514c6^..c898f950`. No files edited or merged by reviewer.
ES remains OPEN.

## Reviewer report

**Recommendation: retain DEAD for this construction and DORMANT for broader astra-1, with two documentation corrections.** No fatal error in the mathematical kill under the implementation’s destination guards; no ES/U₇ theorem or general transport no-go follows.

### Findings

1. **P2 — Clarify when attempted destinations receive factor tests.** `Z61_TRANSPORT.md:19` says to test gcds at an “attempted destination,” but `scripts/z61_transport_rule.py:109–114` rejects invalid translations before those tests. This matters concretely: the n=105 token produces f′=17223, and **gcd(105,17223)=3**. It is STUCK only when out-of-range proposals are excluded *before* factor testing. Section 5.4’s statement that the arithmetic moves “do not produce” a factor is therefore too broad. Explicitly document the legal-destination-only interpretation, without silently rewriting the preregistration. The n=193 kill survives either interpretation.

2. **P3 — The n=193 hit listing omits f=39.** `Z61_TRANSPORT.md:51,117` names f=15 and 103 as the actual hits; the complete list is **15,39,103**. At f=39, r=2 and the word is (2,20,5). This third hit has (k,g)=(5,2), so it cannot rescue the token. Correct the apparently exhaustive wording, not the verdict.

### Mathematical assessment

- **Conservation/capacity:** sound for the implemented rule. Slots `(f,ℓ,e)` have unit capacity; neither signed carries nor reservoir moves are falsely assumed jointly injective.
- **Termination:** the potential proves finite exhaustion, including STUCK—not legal termination. The memo correctly identifies that distinction.
- **Interior arithmetic:** normalization, valid-range guards and invertibility check out, including ℓ=2. The n=53 trap genuinely demonstrates why raw-remainder congruences are insufficient.
- **Reservoir:** complete for admissible k=1 numerator slots/hits. The progression-skipping optimization preserves that set.
- **Factors:** foreign-label absorption is legitimate as an explicit compositeness exit, including square preflight; it is not numerator cancellation.
- **Large-layer lemma:** the stated inequalities and gcd argument hold.
- **Logical scope:** n=193 has hits, so it cannot refute an absence-of-hits conditional theorem. The memo explicitly acknowledges this. Under the guarded interpretation, n=105 supplies the separate genuine no-hit failure.

### Independent verification

The bounded checker passes. I additionally verified:
- All category memberships, summary aggregates, factorizations and scopes: **502 inputs; 190 complete, 308 sampled, 4 square preflights**.
- All **2,507 stored positive routes’ legality**, beyond merely checking endpoint arithmetic.
- Independent routing replay on **184 complete inputs ≤2000**, matching every ledger; **2,163 nonfactor ℓ=2 tokens** checked.
- Both empty-capacity obstructions, all square ledgers/restricted-exit overlaps, and 131’s **34-token U₇ routing with no U⁽⁸⁾ hit**.
- The U⁽⁸⁾/R₈ distinction and inherited status of the twelve large R₈ zeros are correctly qualified.

The archived checker is not an independent replay of all 301 failed inputs; the memo discloses that limitation. This is a genuine, narrowly scoped failed construction—not an overclaimed impossibility result.

No files edited or merged; no dense enumeration of large fixtures.

## Author disposition

Both findings accepted and checked directly. The original preregistration text is retained. The memo explicitly records its ambiguity, documents the implemented guard order, and demotes the 105 example to a guard-dependent diagnostic. The raw-proposal factor is now archived and checked independently. The prime 193 kill survives even factor-testing every raw proposal. Added the third hit f=39 and checked the complete hit list. No transport move changed; no extension was fitted after the kill. Verdict remains DEAD for this candidate / DORMANT for broader astra-1. Final bounded rerun and independent checker pass.
