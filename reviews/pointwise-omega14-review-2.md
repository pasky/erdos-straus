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

### Lemma 4.4 (D's class-uniform mod v) — SOUND (one MINOR justification gap, D3)
* `D=κt²`, κ squarefree ⇒ `D*=κt` (v_p: `⌈(e+2f)/2⌉=e+f`, e∈{0,1}); bijection. OK.
* Kept pairs: `t≤X^{1/6}`, `κ∈(X^{2/3},X/t]` ⇒ `n=κt∈(X^{2/3}t,X]⊂[V,X]`. OK. `φ(4n)=2n∏_{p|n odd}(1−1/p)≤2n`. OK.
* Squarefree-in-AP: `N_b(K)=σ_vK/v+O(√K)` with the O(√K) **not** divided by v; partial summation
  error `O(K_1^{−1/2})=O(X^{−1/3})≤O(1/v)` since v≤V=X^{1/3}; summed over t: `O(LX^{−1/3})=o(L²/v)`. OK.
* `∫_1^{X^{1/6}}(L/3−log t)dt/t=L²/18−L²/72=L²/24`. OK; coprimality to v costs `O(ω(v)L²/y)`. OK.
* Constant: `(1/2)(6/π²)/48=0.00633>1/200`. OK.
* Exceptional removal: `q_1|4n⟺q''|n` with `q''=q_1/gcd(q_1,4)` (checked: `q_1=2^a m`). `q''|κt⇒q''/(q'',t)|κ`;
  CRT with `κ≡b (v)` (empty if not coprime); (F4) and `Σ_{t≤X}(q'',t)/t≤τ(q'')(1+L)`. OK.
* D3 below: the final step `τ(q'')/q''≤𝓛^{−1.8}` (or `≤4𝓛^{−1.8}`) is asserted as if from
  `q''≥𝓛^{1.9}/4` alone; it needs `τ(m)≤m^{1/20}` for `m≥m_0` (true, divisor bound) — note
  q'' can be as large as `4T^ε`, where τ(q'') is far bigger than `𝓛^{0.1}`, so the ratio must be
  bounded via `τ(m)/m≤m^{−0.95}`, not via τ bounded.

### Theorem 4.5 — SOUND (re-derived)
* Small coordinates may be random or fibre-fixed: Thm 1.3 only needs the big coordinates to be
  independent of each other and of x_s, with x_s drawn from its true law. On `n≡r (Q)` the Haar
  law is the product of local laws restricted to the coset, so `X_ℓ` (ℓ>T^{0.6}, ℓ∤Q) are
  independent Haar, independent of the rest. Fibre-fixed `x_q` (q|Q, q|v) are just particular
  values of x, and the lower bound on R is for **every** x. For ℓ|Q, ℓ>T^{0.6}: these are
  *small* (only mod `ℓ^{v_ℓ(Q)}` fixed — still fine, small coords may be random) and their events
  are dropped; loss `≤(log Q/0.6𝓛)·T^{−0.09}=o(1)`. Level count: a level function reads big
  primes dividing q≤D only (ℓ∤Q), fewer than `log D/(0.6𝓛)`. OK.
* `D≡−x/4 (v)` ⇒ D unit mod v ⇒ `gcd(v,n_D)=1`; v y-rough ⇒ odd. So Lemmas 4.3, 4.4 apply to
  every v, with `a=−x/4` a unit. `R≥0.13·(L²/200)·Σ_v1/v`, `Σ_{v≤V,y-rough sqfree}1/v≫log V/log y=ε𝓛/(18log𝓛)`.
  `μ*≍ε³𝓛³/log𝓛`. Arithmetic `(k+1)(1+4p*)≤μ*` for `c≤0.3c_9ε³`: OK (needs only c<0.6c_9ε³).
* Events are genuine ES events: `M=vℓ≤T^{0.7+ε/3}≤T`, `M≡3 (4)`, `D|A_M²` (via `n|A_M`), and
  `F=1[W(n)>T]` exactly (POINTWISE_OMEGA §0 has no `D<M/4` restriction). OK.
* Constants c, ε are absolute (ε from (G)'s c, κ, C' only). No hidden parameter dependence found.
