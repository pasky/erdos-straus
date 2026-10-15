# Hostile review R231 of STERILE_LOWER.md (O228, checkpoint 1) — round 1

Reviewer: R231 (independent hostile review #1). Branch `side-agent/review-sterile-lower-2`, merged `side-agent/sterile-lower`.
Scripts (from scratch): `scripts/review_zl_*.py`. Status: IN PROGRESS.

## Summary verdicts
(filled in at the end)

## Claim-by-claim

### Lemma 3.1 (joint parametrisation of level-1 data)
Re-derived (i): with f = 4acd − 1 and f | N + 4a²d, Nc + a ≡ −4a²cd + a = −a·f ≡ 0 (mod f); b := (Nc+a)/f,
e := (N+4a²d)/f; 4abd·f = 4ad(Nc + a) = N(f+1) + 4a²d = f(N + e)·… — directly: 4abd = (4acdN + 4a²d)/f = ((f+1)N + 4a²d)/f = N + e;
ce = (cN + 4a²cd)/f = (cN + a(f+1))/f = b + a. a ≤ b ⇔ Nc + a ≥ af = 4a²cd − a ⇔ cN ≥ 4a²cd − 2a. Converse by ef = N + 4a²d
(SE Lemma 1.1(i)). (ii): e·f = 4a²d + 1, na + c ≡ 4a²cd + c = c(4a²d+1) ≡ 0 (mod f); 4abcd = (n+f)b = nb + na + c. Converse:
4acd > n is forced (c(4abd − 1) = n(a+b) > nb·… gives 4acd·b > nb), and ef = 4a²d + 1 with e = (a+b)/c. All correct.
Brute force (`scripts/review_zl_joint.py`, own per-n loops over (a, b, d) for P and (a, c, d) for Q, compared as SETS of
tuples, not counts): X = 100: 685 + 1010 data, 0 mismatches; X = 300: 3301 + 4909, 0 mismatches (same totals as the author).
The divisibility f | na + c was asserted for every (a, d, f, c) in the joint loop: never failed.
Minor: "a ≤ b ⇔ b ≥ a" in (ii) is vacuous as written (presumably meant "⇔ c(4a²d+1) ≥ af·… " or simply "require b ≥ a").
**Verdict: SOUND** (cost-model Consequence is Assessment, correctly labelled).
