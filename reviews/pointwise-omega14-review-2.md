# Hostile review R49b: POINTWISE_OMEGA14.md §4 (ceiling theorem, O49b)

Reviewer branch: side-agent/review-omega14b (merged side-agent/junta-third at 88157c2).
Status: COMPLETE (round 1).

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

### From-scratch numerics (`scripts/review_o14b_toy.py`, output `data/review_o14b/toy.txt`)
* A: Lemma 4.2 toy (V=5, X=12, ℓ∈(144,4000]): 0 uniqueness violations; R(x) computed directly as
  `Σ_ℓ #{hit classes mod ℓ}/(ℓ−1)` equals the regrouped formula for every x (err 9e−16).
* B: Lemma 4.4 at X=10^6 (no exceptional set), all odd sqfree 7-rough v≤60: `min_a W(v,a)·v/L²∈[0.148,0.161]`,
  far above the claimed 0.005 (the proof's constants are lossy, not wrong).
* C: Lemma 4.3 toy, primes in (10^6,10^7], q=4n, n≤30: `min_b φ(q)Σ1/(ℓ−1)=0.152` vs ideal
  `log(7/6)=0.154` and claimed 0.13. (Only small q; the real content is (G).)
* D: Thm 1.3/Lemma 4.1 toy LP (exact max of E B over B∈𝒱_k, B≤F, s∈{0,1}, n=8 fair bits):
  if every s has R=8≥threshold, max E B=0 (k=1,2) and also at the boundary R=thr (m=3,n=7,k=1);
  if one s has only k active bits, max E B>0 (0.25, 0.125). So "E B≤0" is exactly the
  sharp conclusion (B≡0 attains 0), and the deterministic hypothesis is what is needed.

### Corollary 4.6 (1/4 ceiling) — SOUND as scoped (MINOR scope edits D4, D5)
* Matching to O9 Thm 1.1: `B=Σc_i1[n≡b_i (d_i)]` is a combination of `n↦φ(n mod d_iQ)`, so its
  O14-level is `≤max d_i≤Z/Q≤Z`. O9's hypothesis `B≤1[W(n)>T]` on integers `n≡1 (Q)` coprime to
  the d_i implies `B≤F` on the Haar fibre (every unit class mod `lcm(Q,D,M≤T)` has such integer
  representatives, CRT), and `F=1[W>T]` exactly. `E_D B=μ=E_fibre B` since `gcd(D,Q)=1`. O13 Thm 5.1
  runs on `(Q',r')`, `gcd(d_i,Q')=gcd(d_i,Q)` possibly >1 — covered, since the level definition
  allows `n mod qQ` with `gcd(q,Q)>1`. So O9/O13 certificates are in scope and need
  `log Z≥c𝓛^4/log𝓛`, `log x≥C_2 log Z`.
* Exponent bookkeeping: `log x≥c'𝓛^4/log𝓛 ⇒ 𝓛≤C(log x·loglog x)^{1/4}`; O13 achieves
  `𝓛≍(log x)^{1/4}(loglog x)^{−1/4}`: gap factor `(loglog)^{1/2}` in 𝓛. Correct. "As certified
  bounds" is the right qualifier (the certificate only knows `p≤x`).
* The other hypotheses of O9 (A≤Z^{1/4}, twist condition) only shrink the class; irrelevant.

## Defects (continued)

**D2 (MINOR, Lemma 4.3 display).** The display writes the (G) error in its non-exceptional
κ-form and says the exceptional case has prefactor `(1−β_1)log x≤0.7/(κε)`. As quoted in
O9 §1, the exceptional-case bracket is `[x·e^{−log x/log Q_G}+x log x/(Q_G log Q_G)]` (no κ in
the exponent, different second term). The conclusion is unaffected (`(0.7/κε)(e^{−0.6/ε}+o(1))≤1/8`).
Repair: write the two cases' error terms separately, as in O9 §1.

**D3 (MINOR, Lemma 4.4, last step of exceptional removal).** `τ(q'')/q''≤𝓛^{−1.8}` (proof says
`H_exc≤4L²𝓛^{−1.8}/v`) is stated without justification; q'' ranges up to `4T^ε`, where τ(q'') is
not `𝓛^{O(0.1)}`. Repair: "by the divisor bound `τ(m)≤m^{1/20}` for `m≥m_0`, and `q''≥q_1/4>𝓛^{1.9}/4`,
`τ(q'')/q''≤q''^{−0.95}≤4𝓛^{−1.8}` for T large".

**D4 (MINOR, Cor 4.6 scope can be widened).** The restriction `log Q≤T^{0.05}` is vacuous for
O9-type transfers: they need `log x≥C_2 log Z≥log Q`, so `log Q>T^{0.05}` already forces
`log x>e^{0.05𝓛}`, far beyond the ceiling. Repair: add this sentence, so Cor 4.6 covers every fibre.

**D5 (MINOR, Cor 4.6 "Not claimed" list).** Make explicit that the corollary concerns transfers
whose positivity comes from the Haar mean `E_fibre B>0`. Excluded, and worth listing:
(a) transfers whose positivity comes from the exceptional-character term
(`Σ_pB(p)≈x(E B−x^{β_1−1}E[Bχ_1])/φ(Q)`, which can be positive with `E B≤0` if a Siegel zero
exists at that scale) — these can only work at Siegel scales, hence not unconditionally for
infinitely many T, but they are outside the theorem; (b) minorants of F that are not of bounded
level in the O14 sense (e.g. using a modulus with many primes >T^{0.6}); (c) majorant/minorant
mixtures and bilinear input (already listed). Also recommend the Status table say
"PROVED implication (scope: E_Haar B>0, transfer needs log x≫log Z)".

*Checked, no defect:* 𝓕*⊂§2's 𝓕 (needs `ε≤1/10`, imposed; `n≥V=T^{ε/3}≥N_0=𝓛²`, `D*≤T^{1/10}`), so Lemma 2.1's
`p*≤T^{−0.09}` applies to 𝓕* in Thm 4.5.

## Verdict table

| claim | verdict |
|---|---|
| Lemma 4.1 | SOUND |
| Lemma 4.2 | SOUND (brute-force confirmed) |
| Lemma 4.3 | SOUND (D2 minor) |
| Lemma 4.4 | SOUND (D3 minor) |
| Thm 4.5 (`E B≤0`, mod (G), effective Page, fundamental lemma) | SOUND |
| Cor 4.6 | SOUND as scoped; SOUND-AFTER-REPAIRS for wording (D4, D5) |
| document | D1: delete stale duplicate §5/§4 (lines ~450–611) |

No FATAL or MAJOR defects. The "please check" items (induced characters, exceptional split at
`𝓛^{1.9}`, exceptional-set removal, fibre-fixed coordinates) all check out. The labels are
appropriate: Thm 4.5 is PROVED modulo the cited theorems, and Cor 4.6 is a PROVED implication
within its stated scope. ES is not affected.
