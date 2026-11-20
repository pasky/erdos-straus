# Exact residue decoding from negative-Pell powers

(§0 block: z74 Opus xreview fix)
```
Result: U_(1+4a) is an n-adic isometry permuting residues mod n^k (slope ∈4+nℤ_(q)); two remainders decode U_s mod N
        from coordinates without dividing by y; coordinates reduced mod a fixed N cannot decode uniformly.
Label: PROVED (hypothesis: an integral negative-Pell witness at n exists). Replay CERTIFIED
       (scripts/pell_residue_interface_audit.py; independently recomputed). (z74 Opus xreview fix: label wording)
Scope: as PELL_REMAINDER_SELECTOR.md (same permutation theorem, different proof); no ES-forcing rule; not about ES.
Review: cross-model (Claude Opus), data/z74/xreview/REVIEW_PELLNOGO_OPUS.md — ACCEPT-WITH-FIXES (§0, label wording).
Triage: METHOD-CX
STATUS delta: none
```

**PROVED (hypothesis: an integral negative-Pell witness at n is given; this is a hypothesis, not a CONDITIONAL label — z74 Opus xreview fix).** The same permutation is proved by digit lifting in `PELL_REMAINDER_SELECTOR.md`. Let `n≥5` be odd and `ε=x+y√n`, `x,y>0`, `x²−ny²=−1`. For every `k≥1`, `F(a)=U_{1+4a}`, where `ε^s=X_s+Y_s√n` and `U_s=Y_s/y`, permutes the classes mod `n^k`. No fundamentality or coprimality of y to n is needed. The precise slope statement is `(F(a)−F(b))/(a−b) ∈ 4+nℤ_(q)` for every `q|n`, `a≠b`; it is a localized congruence, not a claim of integer divisibility by `a−b`.

**Proof.** All powers, including negative ones, have integral coordinates (`ε⁻¹=−x+y√n`). In fact `U₀=0,U₁=1,U_{s+2}=2xU_{s+1}+U_s` in both directions, by the characteristic polynomial of ε. For `q^e||n`, `x²≡−1 mod q^e`, so x is a unit and `q≡1 mod 4`, in particular `q≥5`. For `s>0`, binomial expansion gives

```
U_s/s = Σ_{0≤2h+1≤s} binom(s−1,2h) x^(s−2h−1) (ny²)^h/(2h+1).
```

For `h≥1` we have `q^h>2h+1`, hence `v_q(2h+1)≤h−1` and `he−v_q(2h+1)≥e`. Thus `U_s/s≡x^(s−1) mod q^e` in `ℤ_(q)`, **even if `q|s` or `q|y`**. Also `X_s≡x^s mod q^e`. Both extend to `s<0` using `X_{−s}=(-1)^s X_s`, `U_{−s}=(-1)^(s+1) U_s` and `x²≡−1`; no quotient is taken at `s=0`.

For distinct `m,j≡1 mod 4` put `h=(m+j)/2`, `d=(m−j)/2`. The unit `ε^d` has norm `+1` since d is even; subtract the √n-coefficients of `ε^h ε^d` and `ε^h ε^(−d)`. This gives `U_m−U_j=2X_h U_d`, hence the divided difference is `X_h U_d/d≡x^(m−1)≡1 mod q^e`. Swapping m and j preserves the quotient. In particular `v_q(F(a)−F(b))=v_q(a−b)` for every `q|n`; congruence mod `n^k` is preserved **and reflected**, giving the permutation and, compatibly, a bijective isometry on the `n`-adic completion. More precisely `F(a+n^k d)≡F(a)+4n^k d mod n^{k+1}` for any integer d and `k≥0` (exact equality if `d=0`). Thus starting at `a=0 mod 1`, to hit D lift by the unique digit `d≡4⁻¹ (D−F(a))/n^k mod n`. This works unchanged for composite n. Choose `0≤a<n^k` to use positive powers only.

**No division by y: three distinct interfaces.**

* Given the **index**, compute `U_s mod N` with the recurrence (matrix powering) using only `x mod N`, even at `p|y`.
* Given the actual **coordinates** and `N=n^k`, write `rem(A,B)` for the least nonnegative remainder, `B>0`. The following two remainder operations need neither `Y_s/y` nor a modular inverse of y:

  `r=rem(Y_s,yN)`,  `D=rem(−Nr,yN+1)`.

  Indeed `r=yd` for the unique `0≤d<N` congruent to `U_s mod N`; `−Nyd≡d mod yN+1`, and d is already the least representative. If nonnegative dividends are required use `(yN+1)N−Nr` instead. These are **variable-modulus** operations, not regular or rational functions.
* Given only coordinates reduced mod N, universal recovery is false. At `p=5` the anchor `(2+√5)^5=682+305√5` has `5|y`; for all `s≡1 mod 4`, `(X_s,Y_s)≡(x,0) mod 5`, while `U_s≡s mod 5` runs through every class. In fact anchors `(2+√5)^{5^L}` have `v₅(y)=L` by the binomial lemma on the original anchor, so no fixed extra precision `5^L` works uniformly over anchors. This rules out a decoder using only residue-ring operations at such fixed precision, not every algorithm on the full integers.

**What it makes.** For sorted ES denominators `A≤B≤C`, `A≤3n/4`, `B≤2nA/(4A−n)`, and `C=nAB/(4AB−n(A+B))≤nAB≤9n⁴/8<2n⁴<n⁵`. Thus *every* ES triple is reproduced exactly by three independently chosen powers of the same anchor: decode the least residues mod `N=n⁵`. Even one power suffices with digit extraction: encode `A+NB+N²C` modulo `N³` and unpack in base N. In both cases **least remainders are essential**; the exact rational function `Y_s/y` generally returns a much larger integer. There is no contradiction to a fixed polynomial/rational-menu obstruction, and no source of a good residue in this bijection. Enumerating the first decoded denominator and testing its residual for a two-unit split is a complete search without a prespecified denominator, but just permutes the ordinary search. A modular ES identity alone does not make an exact witness: `(n²,n²,n²)` passes the cleared equation mod `n⁵` but fails over the integers. No new ES-forcing rule follows here.

**Screens.** An odd square `n>1` has no such positive integral anchor; the proof includes composite nonsquares admitting one. No numerator-8 claim or consequence for ordinary zero counts. Replay: `(ulimit -v 600000; timeout 30 env UV_OFFLINE=1 uv run --no-project python scripts/pell_residue_interface_audit.py)`.
