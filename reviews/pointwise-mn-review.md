# Hostile review R63 of POINTWISE_MN.md (O63, branch side-agent/mn-quarter @ f97b37d)

Reviewer branch: side-agent/review-mn. Scripts: `scripts/review_mn_*.py` (from scratch).

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Lemma 1.1 | SOUND (see §L1) |

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
