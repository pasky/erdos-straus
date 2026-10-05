# Hostile review R49b: POINTWISE_OMEGA14.md §4 (ceiling theorem, O49b)

Reviewer branch: side-agent/review-omega14b (merged side-agent/junta-third at 88157c2).
Status: IN PROGRESS.

## Defects (numbered as found)

**D1 (MINOR, editorial but misleading).** POINTWISE_OMEGA14.md contains §5+§4 TWICE
(lines ~285–449 and ~450–611). The second copy is the *pre-self-review* version of Cor 4.6
("now a theorem (modulo (G)), not an Assessment", no `log x≫log Z` scope restriction).
Repair: delete lines 450–611 (the stale copy); keep the first.

## Claim-by-claim (written incrementally)

### Lemma 4.1 (deterministic planting) — SOUND
Immediate from Thm 1.3 (reviewed SOUND in R49). Re-checked Thm 1.3's mechanism: given x_s the
bits on any ≤k big coordinates are independent with true marginals (Lemma 1.1), and X_b|bit is
the true conditional, so (X_b)_{b∈K} has the true product law given x_s; B linear ⇒ E_νB=E B.
Absolute continuity: ν only charges bit patterns y⊆J with w_J>0 (all r_i>0), so every
configuration charged by ν has positive Haar mass; B≤F is pointwise on finite-level cells, so
no a.e. issue. Planted ⇒ some bit 1 ⇒ some E∈𝓕* holds ⇒ F=0.

### Lemma 4.2 (unique small part) — SOUND
`vℓ≡−1 (4n)` forces `v≡−ℓ^{−1} (4n)`, and `1≤v≤V=X^{1/3}≤n<4n`, so v is determined by (ℓ,n_D).
Classes `−4D mod ℓ` are distinct units (`0<D≤X²=T^{2ε}<T^{0.6}<ℓ`). Hence
`p_ℓ(x)=#{D: v(ℓ,D) exists, x≡−4D (v)}/(ℓ−1)` exactly, and regrouping by v gives the stated
identity (v=1, i.e. M=ℓ, is included; harmless). Checked by brute force (script
`review_o14b_toy.py`, part A).

### Lemma 4.3 (class-uniform primes mod 4n) — SOUND (minor bookkeeping only)
* Single-modulus use of the large-sieve-type (G): `ϑ(x;q,b)=φ(q)^{−1}Σ_{χ mod q}χ̄(b)ϑ(x;χ)`,
  `|ϑ(x;χ)−ϑ(x;χ*)|≤Σ_{p|q}log p≤log q`, and χ↦χ* is injective into primitive characters of
  conductor ≤q≤Q_G=4X. So the full (G) sum bounds `φ(q)|ϑ(x;q,b)−x/φ(q)+[q_1|q]χ_1(b)x^{β_1}/β_1|`
  up to `φ(q)log q`. Correct (crude but valid).
* Sign of exceptional term: ψ(x,χ_1)≈−x^{β_1}/β_1, χ_1 real ⇒ contributes `−χ_1(b)x^{β_1}/(β_1φ(q))`. Matches.
* Non-exceptional error: `C'e^{−log x/(κ log Q_G)}≤C'e^{−0.6/(κ(ε+o(1)))}≤1/8` for ε≤ε_0(κ,C'),
  absolute. Exceptional-case error (O9 §1 quote): prefactor `(1−β_1)log x≤0.7/(κε)` times
  `[e^{−log x/log Q_G}+log x/(Q_G log Q_G)]` — note **no κ** in this exponent; the author's display
  writes the generic κ-form. Harmless (`(0.7/κε)e^{−0.6/ε}` is even smaller), see D2.
* Range `Q_G^{6c}≤x`: `6cε<0.6` suffices; `ε≤0.05/c` OK.
* Page case `q_1≤𝓛^{1.9}`: effective `1−β_1≥c q_1^{−1/2}(log q_1)^{−2}` (Davenport ch. 14, effective)
  gives `(1−β_1)log x≥c'𝓛^{0.05}/(log𝓛)²→∞`. OK. Case `q_1>𝓛^{1.9}`: n excluded. OK.
* Partial summation: `∫_{T^{.6}}^{T^{.7}}(1+log t)/(t log²t)dt=log(7/6)+O(1/𝓛)`; boundary terms
  `O(1/(𝓛φ(q)))` need the upper bound 9/8 at `T^{0.6}`, available. `(7/8)log(7/6)=0.1349≥0.13`. OK.
