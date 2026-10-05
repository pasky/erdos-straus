# Hostile review of POINTWISE_TRANSFER.md (task R42)

Reviewer branch `side-agent/review-transfer` (merged `side-agent/avoid-transfer` @ 97894d8).
Status: round 1 complete. (Note: `git merge --ff-only` failed because main had moved; a normal merge of the author branch was used.)

## Summary verdicts

| Claim | Verdict |
|---|---|
| Thm 1.1 (abstract transfer, modulo G+H) | **SOUND** — every step re-derived against [SN]; dropping single-value / codegree hypotheses legitimate (atoms only inside the sandwich); constants check; general target class and exceptional-zero cases A/B correct |
| Lemma 1.2, Lemma 3.2 (twist criteria) | **SOUND** (re-derived; from-scratch toy incl. 2-adic/non-squarefree conductors) |
| Cor 1.3 | **SOUND** |
| §3.3 exceptional zero, §3.1, §3.4 | **SOUND** (Assessment parts appropriately labelled); one MINOR wording |
| §4.1–4.5 comparisons | SOUND as hedged ([memory] items flagged; Iwaniec/Costello–Watts secondary statement checked) |
| §4.6 Bonferroni benchmark (Assessment) | **GAP** — the hub example is beaten by hub-quarantine + Linnik, so it does not show an advantage of Thm 1.1 (MAJOR-1) |
| Lemma 5.1 | **SOUND** (re-derived; from-scratch check m = 4..12, M ≤ 2500) |
| Completeness of (5.1) for Type II, m ≠ 4 (left open by author) | **Holds** — 4-line proof (ET Prop 2.6 argument) + brute force over all solutions, m ∈ {4,5,6,7,8,11}, primes n ≤ 400/250 |
| Cor 5.2 (m/n, mod G+H+ET Prop 1.4) | **SOUND**; ET Prop 1.4 is stated in ET for general k, nothing extra assumed; can be strengthened to "all Type II solutions" |
| Cor 5.3 (generic families) | **SOUND-AFTER-REPAIRS** (minor wording: Remark (i) exponent for α<2, one justification line) |
| Cor 5.4 | SOUND; MINOR side conditions on Instance (2) |
| Labels / novelty | Honest. Only overreach: §4.6/§5.3(c) "genuine range" Assessment (MAJOR-1) |

No FATAL defects.

## Defects

**MAJOR-1 (§4.6 example; §5.3(c) "genuine range"; report "this is the real reason
the sandwich wins").** In the multi-hub example every event contains a hub
condition `X_{ℓ_h}=σ_h`; quarantining the `H` hubs (add them to `Q`, pick the
target class `≢ σ_h`) removes all events, giving `log p ≪ log Q + H log T` by
Linnik, whereas Corollary 1.3 costs `≳ (H/128) log T log(4NT) + k² log T log²(4NT)`.
So on this example quarantine (the first step of the [SN] pipeline itself) beats
Theorem 1.1 for every admissible `H`; the example only shows that *plain*
Bonferroni is bad. *Repair:* add "quarantine + Bonferroni + Gallagher" as the
benchmark in §4.6; either exhibit a system where Thm 1.1 beats it (e.g. heavy
shared sub-cells on *pairs* of primes arranged so that every killing prime set is
large while all `w_ℓ ≤ 1/(64k)` — needs an actual computation), or state plainly
that no example is known where Thm 1.1 beats this combination, and soften
§5.3(c) ("ES is of exactly this type") to an unverified Assessment.

**MINOR-1 (§5.1 hedge "we do not claim every Type II solution of m/n arises this
way").** It does, for prime `n` (more generally whenever `gcd(x,n)=1`): with
`w = gcd(x,y',z')`, `x=wX`, `y'=wY`, `z'=wZ`, the equation `m·wXYZ = nYZ+XY+XZ`
forces `X|YZ`, `Y|XZ`, `Z|XY`, hence `X=su`, `Y=sv`, `Z=uv`, and dividing by `suv`
gives `s(m·uvw−1)=nv+u`. *Repair:* insert this proof (or cite ET Prop 2.6's
argument, numerator-free) and state Cor 5.2 as a bound for all Type II solutions
of `m/p`. Verified by `scripts/review_tr_typeII.py`.

**MINOR-2 (Cor 5.2 label, §7).** "modulo ET Prop 1.4 with κ = m" reads as if an
extension of ET were needed; ET Prop 1.4 is stated for any positive integer
`k ≪ (AB)^{O(1)}` (checked in `sources/elsholtz-tao-1107.1010.pdf`). *Repair:* say
"modulo ET Prop 1.4 (stated there for general k; used with k = m)".

**MINOR-3 (§5.2 Remark (i)).** "Any family whose mass is ℒ^α gets exponent
1/(α+3)" contradicts the corollary for `α < 2` (exponent `1/5`). *Repair:* "1/max(α+3,5)".

**MINOR-4 (Cor 5.3 proof, last line).** `ℒ^β ≫ log p·log ℒ ≫ log p·log log p`:
the second step needs `log log p ≤ β log ℒ + O(1)` (from `log p ≪ ℒ^β`), not from
`p > T`. Add the line. Also the `σ` clause should use `log(S^♮+1)` (or `max(σ,0)`).

**MINOR-5 (Remark 3.1).** Say explicitly that with `δ_*` in place of `δ_L` the
(LLL) hypothesis is no longer used (only (Tw)).

**MINOR-6 (Cor 5.4 Instance (2)).** Requires `q ∤ h` (else the class is non-unit
and deleted) and `w_q = 1/(q−1) ≤ 1/64`, i.e. `y ≥ 64`; state these.

## Scripts (from scratch, independent of the author's)
* `scripts/review_tr_sandwich.py` — exact Haar toy: sandwich, energy bound, twist
  identity and Lemma 1.2/3.2 chains, with 2 ∈ 𝒫 (`e₂=3`).
* `scripts/review_tr_typeII.py` — all solutions of `m/n`, Type II ⇒ form (5.1).
* `scripts/review_tr_lemma51.py` — Lemma 5.1 (i)–(iii), m = 4..12, M ≤ 2500.
Author replay `scripts/transfer_mn.py` also re-run: passes.

## Notes per claim

### Theorem 1.1 (abstract transfer) — step-by-step re-derivation

Checked against [SN] = `paper/es-subexp-note.tex`: `lem:lll`, `cor:lll`, `lem:brw`,
`lem:size`, `lem:l1`, `lem:twist`, `lem:tail`, `cor:el`, `thm:transfer`.

* Step 1 (atoms). The sandwich of `lem:brw` is run over the distinct atoms (cells),
  which *are* single-value events in the sense of [SN] §6 Setting, so `lem:brw`,
  `lem:size`, `lem:tail` apply verbatim to the atom list; nothing about the
  original events is needed except `F` itself. Dropping the single-value hypothesis
  is therefore legitimate; its cost is only `m_a` in place of `m`. Checked
  `m_a ≤ Σ_{j≤k}C(N,j)T^j ≤ Σ_{j≤k}(NT)^j ≤ 2(NT)^k` (NT ≥ 2). OK.
* Codegree: [SN] `lem:tail` uses only support size (remark after its proof);
  [SN] never had a codegree hypothesis in the sandwich. OK.
* Step 3 arithmetic: `2^{k₀} ≥ 400 m_a²(S+1)/δ_L` ⇒
  `m_a²·S·4·2^{−k₀} ≤ Sδ_L/(100(S+1)) ≤ δ_L/100 ≤ δ/100`. The bracketed bound
  `k₀ ≤ 2k log₂(NT)+log₂(1/δ_L)+log₂(S+1)+12` follows from `log₂1600 < 10.7` plus
  the ceiling. OK.
* Step 4: `lem:l1` with η = 1/99 needs `𝔼[F−B] ≤ 𝔼B/99`; `𝔼B ≥ 0.99δ` gives it.
  `A ≤ 1+2/99`. OK. Moduli: product of cells on `I∪J` has modulus `∏_{I∪J}ℓ^{e_ℓ}`,
  so `d ≤ T^{3k+2t}`. OK.
* Step 5 (twist, non-squarefree `f`, 2 ∈ 𝒫 allowed): for `f | ∏ℓ^{e_ℓ}` the
  ℓ-part of `f` divides `ℓ^{e_ℓ}`, so `ψ_ℓ` is a function of `X_ℓ`; for a cell on
  `I`, `f | d ⇔ primes(f) ⊆ I`, else a nontrivial `ψ_ℓ` with ℓ ∉ I averages out.
  So `μ_ψ = 𝔼[Bψ]` holds without squarefreeness / oddness. `0.21δ ≤ 0.2122μ < μ/4`. OK.
* Step 6 (general class `a`, prime `ℓ'`). Re-derived the character expansion of
  `f(n)=B(n)1[n≡a'(Q')]`: `c(χ) = χ̄_{Q'}(a')·𝔼_D[Bχ̄_D]/φ(Q')`. Properties (a),(b)
  of `thm:transfer` use only `|c(χ)|`; (c) gives `|c(χ)| = |μ_ψ|/φ(Q')`. Case A:
  `c = ±μ/φ(Q')`; with sign −1 the main terms give `(1+x^{β₁−1}/β₁)μx/φ(Q') ≥ μx/φ(Q')`
  and every error is then bounded as in Case 0 (`|R₁| ≤ μx/(400φ)`, Gallagher
  error `≤ μx/(200φ)`). OK. Mixed characters (χ₁ with conductor meeting both
  `Q'` and `D`) fall in Case B, where only `|c(χ)| ≤ |μ_ψ|/φ(Q')` with
  `ψ` = primitive character inducing `χ_D` is used; `gcd(f,Q')=1`, `f | d_i`,
  so (Tw) covers it. OK.
  `ℓ' > R ≥ max(T,Q,max d_i)` ⇒ `ℓ' ∤ QD`, `ℓ' ∉ 𝒫`; `p ≡ 1 (ℓ')` ⇒ `p > ℓ' > T`
  ⇒ `p` coprime to all free primes, so `B(p) ≤ F(p)` applies. `log Z ≤ log 2 +
  log R + log Q + (3k+2t)log T ≤ 2log Q + 2(3k+2t)log T + log 2` (as
  `log R ≤ max(log Q,(3k+2t)log T)`). `A ≤ 1.03 ≤ 2^{1/4} ≤ Z^{1/4}`. OK.
  `thm:transfer` needs `Q ≥ 2`: `Q' ≥ ℓ' ≥ 3`. OK.
* Verdict: **SOUND** (modulo G+H, as labelled). Minor presentation points below.

### Lemma 1.2, Lemma 3.2 (twist criteria)

Re-derived: `|𝔼_{X_{ℓ₀}}[ψ₀1_{Forb}]| ≤ ℙ_{X_{ℓ₀}}(Forb) ≤ Σ_{i∋ℓ₀}ℙ_{X_{ℓ₀}}(E_i | X_{−ℓ₀})`,
and `F'` does not depend on `X_{ℓ₀}`, so `𝔼[F'ℙ_{X_{ℓ₀}}(Forb)] ≤ Σ_{i∋ℓ₀}ℙ(F'=1,E_i)`.
`lem:lll` (second part) is valid for arbitrary (non-cell) events `B=E_i` on a
coordinate set; the LLL inequality restricted to a subfamily is weaker, so it
passes. Including `j=i` in `∏_{j∼i}` only enlarges `η`. Then
`𝔼F' ≤ δ/(1−η)` and `|𝔼Fψ| ≤ ηδ/(1−η) ≤ δ/5` for `η ≤ 1/6`. Lemma 3.2:
`𝔼[F'ℙ(Forb)] = 𝔼F' − 𝔼F` exactly since `F = F'(1−1_{Forb})`. Both **SOUND**.

### Corollary 1.3
`x_i = 2ℙ(E_i) ≤ 2w_ℓ ≤ 1/(32k)`; `Σ_{j∼i}x_j ≤ 2Σ_{ℓ∈supp E_i}w_ℓ ≤ 1/32`;
`1−x ≥ e^{−1.1x}` on `[0,1/32]` (0.96875 ≥ 0.96621); `log₂e^{2.2S} = 3.17S`;
`η_ℓ ≤ e^{1.1/32}/(64k) < 1/6`. The final simplification uses `log₂(S+1) ≪ S+1`
and `12 ≪ k log(4NT)`. **SOUND.**

**From-scratch toy check** `scripts/review_tr_sandwich.py` (numpy, <1 min):
Haar space `(ℤ/8)^××(ℤ/3)^××(ℤ/5)^××(ℤ/7)^××(ℤ/11)^×` (1920 points; 2 is a free
prime with `e_2 = 3`, so conductors 4, 8 and composite `f` such as `8·5·11` occur),
random *general* events (≤ 4 classes, width ≤ 2), own Efron–Stein truncation.
Passing: `B ≤ F`; BRW identity; `𝔼[F−B] ≤ m_a²Σℙ(C_j)En(F^{(j)};t)`; Lemma 3.2 chain
`|𝔼Fψ| ≤ δ^{(ℓ₀)}−δ` for all 63 real primitive `ψ` and all `ℓ₀ | f`; Lemma 1.2
(`η ≤ 1/6` ⇒ `|𝔼Fψ| ≤ δ/5`) in the 11/30 sparse systems where it applies.
Consistent with the author's toy (seed with `max|𝔼Fψ|/δ = 1` reproduced: (Tw) can fail).

### Lemma 5.1 and the completeness question for m ≠ 4

Re-derived (i)–(iii) by hand: (i) `v^{−1} ≡ muw (M)` since `m·uvw = mA ≡ 1`;
every `D | A²` is `u²w` with `uvw = A` (per prime `q^a ‖ A`, `q^d ‖ D`, take
`α = max(0,d−a)`, `γ = d−2α`, `β = a−α−γ ≥ 0`). (ii) `−mD ≡ 1 ⇒ D ≡ −A`, preserved
by `D ↦ A²/D` (D is then a unit), `D ≤ A ⇒ 0 < D+A ≤ 2A < mA−1 = M` for `m ≥ 4`.
(iii) `q^a | mD+1 ⇒ D ≡ −A (q^a) ⇒ A²/D ≡ −A ⇒ q^a | m(A²/D)+1`. All **SOUND**.

**Completeness (the point the author left open) — it holds, with a 4-line proof.**
Let `m/n = 1/x + 1/(ny') + 1/(nz')` with `gcd(x,n) = 1` (for prime `n > m ≥ 4`
this is every solution with exactly two denominators divisible by `n`; three is
impossible since then `m ≤ 3`). Put `w = gcd(x,y',z')`, `x = wX`, `y' = wY`, `z' = wZ`.
Then `m·wXYZ = nYZ + XY + XZ`, so `X | nYZ ⇒ X | YZ` (`gcd(X,n)=1`), `Y | XZ`,
`Z | XY`. Since `X,Y,Z` have no common prime, at each prime one exponent is 0 and
the other two are equal; hence `X = su`, `Y = sv`, `Z = uv` (s,u,v pairwise coprime).
Dividing by `suv`: `m·suvw = nv + s + u`, i.e. `s(m·uvw − 1) = nv + u` — exactly
(5.1). (This is ET Prop 2.6's argument, numerator-independent as the author
suspected.) **From-scratch brute force** `scripts/review_tr_typeII.py` (stdlib,
~1 min): enumerated *all* solutions of `m/n` for `m ∈ {4,5,6,7}` and primes
`n ≤ 400` (`m ∈ {8,11}`, `n ≤ 250`): 641/534/341/328/123/89 Type II solutions, **every
one** has the form (5.1) (search over `w | gcd`, both orderings of `y',z'`) and
`n mod M ∈ R_m(M)`. For composite `n` coprime to `m` (n ≤ 150), all failures have
`gcd(x,n) > 1` (e.g. `4/9 = 1/3+1/18+1/18`), consistent with the proof.

**Consequence.** For prime `p`, `W_m(p) > T` ⇔ `m/p` has no solution with exactly
two denominators divisible by `p` and `m·uvw − 1 ≤ T` (`uvw = w·√(XYZ)`
in the notation above). So Cor 5.2 is a statement about *all* Type II solutions
of `m/p`, not about a sub-family. The author's hedge in §5.1 ("we do not claim
every Type II solution of m/n arises this way") is unnecessarily weak: see
defect MINOR-? (upgrade, not an error). Cor 5.2 is correct either way since it
only concerns `W_m` as defined.

### Corollary 5.2 (m/n, Sierpiński analogue)

Re-ran [SN] `lem:qmass`, `lem:iterq`, `def:system`, `lem:system`, `thm:assembly`,
proofs of `thm:main`/`thm:uncond` with `4 ↦ m`:
* `gcd(A_M, M) = 1` from `mA_M − M = 1`; all `R_m(M)` classes are units. OK.
* Mass: `1/φ(r_Π) ≤ g/φ(M)`, `g = gcd(M, mD+1)`; `D ↦ A²/D` preserves `g`
  (Lemma 5.1(iii)); `D = sr²`, `A = srh`, `M = msrh − 1 ≥ (m−1)srh`;
  `g | msr²+1` and `g | msrh−1` ⇒ `g | msr(r+h)`, `gcd(g,msr)=1` ⇒ `g | r+h`. The
  `Σ_h g/h ≤ (3+log X)τ(msr²+1)` step is numerator-free (`X = (T+1)/m`). OK.
* **ET Prop 1.4 for general κ.** Checked against `sources/elsholtz-tao-1107.1010.pdf`
  (text p. 5): "For any A, B > 1, and any positive integer k ≪ (AB)^{O(1)}, one has
  Σ_{a≤A}Σ_{b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)." So Prop 1.4 *is* stated for
  general `k`; `κ = m` is literally ET's statement (with `a = s`, `b = r`; the
  restriction to squarefree `s` only drops nonnegative terms). Nothing new is
  assumed. The label "modulo ET Prop 1.4 with κ = m" is accurate but suggests an
  extension; MINOR wording.
* Reduction uses Lemma 5.1(ii) (needs `m ≥ 4`, given). Hard-prime condition:
  `lcm(1..⌊ℒ²⌋) | Q_Π` since `z = ℒ² ≤ T` and `Π ⊇ {ℓ ≤ z}` with maximal `e_ℓ`. OK.
* Exponent: `k ≤ ℒ/(2log ℒ)`, `log Q_Π ≪ (ℒ²/log ℒ + k²S*_m)ℒ ≪ ℒ⁷/log ℒ`,
  `kℒ²(S*_m + kℒ) ≪ ℒ⁷`. Unconditional: `τ(msr²+1) ≤ τ*(T+2)`; same as [SN]. OK.
* With the completeness proof above, Cor 5.2 actually says: for infinitely many
  primes `p`, every solution of `m/p` with exactly two denominators divisible by
  `p` has `m·uvw − 1 > exp(c_m(log p)^{1/7})` (in the (5.1) coordinates).
* Verdict: **SOUND** (modulo G+H+ET Prop 1.4, as labelled).

### Corollary 5.3 (generic witness families)

* Weight: `φ(M) = φ(m_Π)φ(r_Π) ≤ m_Π φ(r_Π)` and `m_Π | gcd(M, r−1)`. OK.
* Reduction: `r_Π = 1` ⇒ `r ≡ 1 (M)` ⇒ `1 ∈ R(M)`, excluded. OK. Supports ≤ k. OK.
* Exponent: terms are `π(z)ℒ ≍ ℒ³/log ℒ`, `k²S^♮ℒ ≍ ℒ^{α+3}/(log ℒ)²`,
  `kℒ²S^♮ ≍ ℒ^{α+3}/log ℒ`, `k²ℒ³ ≍ ℒ⁵/(log ℒ)²`. Max is `≪ ℒ^β/log ℒ`,
  `β = max(α+3, 5)`. Correct (even slightly generous for `α < 2`).
* `ℒ^β ≫ log p·log log p`: needs `log ℒ ≫ log log p`, which follows from
  `log p ≪ ℒ^β` (not from `p > T`, which gives the opposite inequality). The text
  says `ℒ^β ≫ log p·log ℒ ≫ log p·log log p`; correct but the second step deserves
  the one-line justification `log log p ≤ β log ℒ + O(1)`. MINOR.
* Remark (i) "Any family whose mass is ℒ^α gets exponent 1/(α+3)": false for
  `α < 2`, where the corollary gives `1/5`. MINOR (contradicts the corollary's own β).
* `log S^♮ ≤ σ(T)` clause: should read `log(S^♮+1)` or `max(σ,0)`. MINOR.
* Verdict: **SOUND** modulo the minor wording points.

### §3.3 exceptional zero, §3.1, §3.4

* Case A/B split re-derived (see Step 6). The "Case B cannot be done Case-A-style"
  argument: without (Tw), `|μ_ψ| ≤ δ+ε`, `μ = δ−ε` (`ε = 𝔼[F−B]`), so the main
  term is `≥ λδ − (2−λ)ε`, requiring `ε ≲ λδ` with `λ` possibly `≍ Z^{−1/2}(log Z)^{−2}`;
  since `ε/δ ≈ 2^{−k₀}` and `log Z ≥ 10kbk₀ log T > k₀`, impossible. Correct, and
  correctly labelled as a limitation *of the argument*. GRH-for-quadratic remark
  correct (conductor `≤ Q_G` would already suffice; "`≤ x`" is just stronger). **SOUND.**
* Remark 3.1: correct — after replacing `δ_L` by `δ_*`, the (LLL) hypothesis is not
  used at all in Thm 1.1 (only (Tw)). The text says "still assuming (Tw)" but
  does not say (LLL) can then be dropped; MINOR wording.
* §3.4 loss accounting matches `t = 10kbk₀` and `k₀` bound. OK (Assessment).

### §4.6 Bonferroni benchmark (Assessment) — the example does not show what is claimed

Re-derived: for odd `j`, `Σ_{i≤j}(−1)^iC(N,i) = −C(N−1,j)` (N ≥ 1), so
`B_j ≤ F`, `𝔼|B_j| = δ + 𝔼[C(N−1,j);N≥1]`; multi-hub Poisson estimate correct;
plain Bonferroni needs `j ≳ S' ≍ q₀/k`. **But** every event of the example
contains a hub condition `X_{ℓ_h} = σ_h`. Quarantining the `H` hubs (put them in
`Q`, choose the target class `≢ σ_h (ℓ_h)`) kills *every* event; Linnik then
gives `log p ≪ log Q + H log T`. Corollary 1.3 on the same system costs
`≍ k log T log(4NT)(H/(128k) + k log(4NT)) ≥ (H/128) log T log(4NT) + k² log T log²(4NT)`,
which is *larger* than `H log T` for every admissible `H` once `log(NT)` exceeds a
constant. So on this example the natural competitor "quarantine + Linnik"
(which is just the [SN] pipeline's own first step) beats Theorem 1.1; the
example shows only that Bonferroni *without quarantine* is bad. The text
mentions "Quarantining the hubs costs H log T" without drawing this
conclusion, and §5.3(c) then cites §4.6 as evidence that the theorem's
"genuine range" is systems with uncontrolled codegrees. → defect MAJOR-1.
