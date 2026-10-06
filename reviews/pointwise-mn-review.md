# Hostile review R63 of POINTWISE_MN.md (O63, branch side-agent/mn-quarter @ f97b37d)

Reviewer branch: side-agent/review-mn. Scripts: `scripts/review_mn_*.py` (from scratch).

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Lemma 1.1 | SOUND (see §L1) |
| Prop 2.1 | SOUND (§P21) |
| Thm 3.1 | SOUND (§T31; MINOR-1) |
| Prop 3.2 | SOUND (§P32) |

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

## §T31 Thm 3.1 (m ≡ 0 (4)) — SOUND (minor editorial points only)

Checked the substitution list against OMEGA13 §3 (Lemmas 3.1–3.3, Thm 3.4) and §5 (I1–I3, property (I),
Thm 5.1, ℓ_aux) line by line. Every place where OMEGA13 uses m = 4:
* Lemma 3.1(a),(b) → MN Lemma 1.1(a),(d): verified above. The *consequence* clause (r square mod every
  prime of Q ⇒ r ≢ −mD (M) for M | Q) uses only `(r|M)=1 ≠ (−mD|M)`; holds verbatim.
* Lemma 3.2(a) drift: at an a=0 square step the hit probability of class −mD mod ℓ is
  `2/(ℓ−1)·1[(−mD|ℓ)=1]`, so `E p_new = (1+(−e|ℓ))p ≤ 2p`; a ≥ 1 steps exact. ✔.
* Lemma 3.2(b) `p_0 = P_H`: needs M odd (2-adic coordinate never constrained). m ≡ 0 (4) ⇒ M ≡ 3 (4). ✔
  (This is exactly the point that fails for odd m; see Cor 6.1 / Thm 5.1.)
* Lemma 3.3(A) NT: `Q(n)=n(mn−1)`, resultant 1; roots mod p: {0, m^{−1}} for p ∤ m, {0} for p | m, so
  ρ(p) ≤ 2 < p for p ≥ 3 and ρ(2)=1 < 2: no fixed prime divisor. `∏(1−ρ(p)/p) ≍_m (log x)^{−2}`. ✔
* Lemma 3.3(B) / Ξ: pure divisor sums over M ≤ T; the M ≡ −1 (m) restriction only shrinks the sums. ✔
* Thm 3.4 normalisation: OMEGA13 normalises on `n ≡ 1 (24)` (atom M=3, D=1). For m ≡ 0 (4), m ≠ 4,
  M = 3 need not be an atom; MN states the bound on all of Ẑ^× with the factor `φ(Q)^{−1}`, which is
  correct (and weaker by O(1)). ✔
* Forced steps at 3, 5, 7 for m with 3, 5 or 7 | m: those primes never divide any M, so the steps
  are pure cost (log 105). ✔ Twist I1(b): `ℓ_0 | f | d_i` is a prime of some M, so ℓ_0 ∤ m. ✔
* I2 junta, OMEGA10 Thm 3.4, O11 Thm 3.2 assembly, `#atoms ≤ T²`: abstract, m-free. ✔
* I3 / property (I) / ℓ_aux: verbatim with `−4D ↦ −mD`. ✔

**MINOR-1 (§3 "What hard means").** "p Type-II-hard modulo Q" is a statement about Type II solutions only;
for m ≠ 4 (and esp. m = 5) the reader may read "hard" as "not covered by any known identity" (Type I
identities also exist). Repair: one sentence that Thm 3.1(ii)/Cor 6.1 concern W_m (Type II, by TRANSFER
Lemma 5.0/completeness noted in the TRANSFER review), and make no claim about Type I coverage.

## §P32 Prop 3.2 — SOUND

Checked against POINTWISE_HAAR Thm 2.1 / Lemmas 2.2–2.4: `M ≡ −1 (mod mn)` ⇒ `M ≡ −1 (m)` and
`mn | mA ⇒ n | A`; (F1) needs `mD ≤ m T^{1/5} < √T ≤ M` (true for T ≥ T_0(m)), so distinct D give distinct
residues and `P(E)=1/φ(M)`; sifted progression length `X/(mn) ≥ X^{4/5}/m`; y-rough M are odd, so no
2-adic issue even for odd m; (2.1), Δ_a, Δ_b with `4n ↦ mn` only change constants. No Jacobi input. ✔
