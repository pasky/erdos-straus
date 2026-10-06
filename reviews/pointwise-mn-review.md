# Hostile review R63 of POINTWISE_MN.md (O63, branch side-agent/mn-quarter @ f97b37d)

Reviewer branch: side-agent/review-mn. Scripts: `scripts/review_mn_*.py` (from scratch).

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Lemma 1.1 | SOUND (see §L1) |
| Prop 2.1 | SOUND (§P21) |

## §L1 Lemma 1.1

Re-derived: `gcd(M,mA)=1` since `M=mA−1`; primes of D divide A, so `−mD = −e·□` with □ a unit mod M;
every prime q | e divides mA = M+1, so `M ≡ −1 (q)`, and reciprocity gives `(q|M)=(−1)^{((q−1)/2)((M+1)/2)}`.
(b),(c),(d) follow as written; the (d) case split (8|m, or m≡4 (8) with t=1 ⇒ v_2(D) odd ⇒ 2|A ⇒ 8|mA)
is correct and covers all t=1 cases (m≡0 (4) and t=0 ⇒ (b) gives −1 directly).

From-scratch check `scripts/review_mn_jacobi.py 6000 <m>` (sympy Jacobi computed directly on −mD mod M,
not via the formula): 22 values m ∈ {4..16,18,20,21,22,24,28,30,36,40}, every odd-M atom with M ≤ 6000:
0 failures of (a),(b),(c); symbol set = {−1} exactly for m ∈ {4,8,12,16,20,24,28,36,40}, = {±1} for every
m ≢ 0 (4) tested. The "iff" direction (m ≢ 0 (4) ⇒ some +1) is not part of Lemma 1.1 as stated; it is
supplied by Prop 2.1 (checked below) — the AGENT_REPORT's phrasing "always −1 iff m ≡ 0 (4)" is fine
given Prop 2.1.

Minor: (a) is stated for "every prime ℓ | M"; for m odd, M may be even (e.g. m=5, M=4) — the lemma
hypothesis "M odd" excludes this, but §3/§6 must remember that even-M atoms exist for odd m (see Cor 6.1).

## §P21 Prop 2.1 — SOUND

Re-derived both constructions: m odd, ℓ ≡ −1 (m), ℓ ≡ 5 (8) ⇒ 2 | A, D ∈ {1,2} give ratio (2|ℓ) = −1;
m ≡ 2 (4), q ≡ 3 (4), q ∤ m, ℓ ≡ −1 (mq), ℓ ≡ 1 (4) (CRT-compatible since v_2(mq)=1) ⇒ q | A and
(q|ℓ) = (ℓ|q) = (−1|q) = −1. Firing bound 1/((ℓ−1)/2) = 2/(ℓ−1) correct.
From-scratch `scripts/review_mn_prop21.py` (primes ℓ < 2·10⁴, 16 values m ≢ 0 (4)): 60–80% of prime
atoms meet both cosets for every m tested (e.g. m=5: 374/559; smallest m=5 example is ℓ=19, the
document's ℓ=29 is also verified: classes {9,13,14,19,23,24,26,27,28} with both symbols).
Note: Prop 2.1 is an *obstruction* statement (the OMEGA13 §3 mechanism cannot be reused); it proves
nothing positive and correctly is not used as an input anywhere.
