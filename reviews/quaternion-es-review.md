# R130 — hostile review of O130 (QUATERNION_ES.md, AGENT_REPORT_O130{,b}.md, scripts/quat_*)

Reviewer: side-agent/review-quaternion. Reviewed: QUATERNION_ES.md as merged from `side-agent/quaternion-es`.
From-scratch scripts (none reuse the author's code or `geo_common`):
* `scripts/review_quat_hilbert.py` — my own Type I enumeration over (a,c,d) (f = 4acd − p | 4a²d+1) and my own
  Hilbert symbol (Serre's formulas, incl. ℓ = 2). Log `logs/review_quat_hilbert_3000.txt`.
* `scripts/review_quat_brute.py` — raw brute force of `4/p = 1/x+1/y+1/z`, split into Type I / II, compared with
  the parameterisations of Lemma 1.1 and Prop 3.2. Log `logs/review_quat_brute_200.txt`.
* `scripts/review_quat_symbolic.py` — my own quaternion multiplication in (α,β), symbolic in d,m,a,b,c,p.
  Log `logs/review_quat_symbolic.txt`.
* `scripts/review_quat_fixed_de.py` — §3.4 pairs and the 40/93, 120/450 counts. Log `logs/review_quat_fixed_de.txt`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (K-factorisation) | SOUND |
| Lemma 1.2 (Λ_{d,m}, disc 4dm−1) | SOUND |
| Prop 1.3 (Λ ⊂ B_{p,∞}, reduced disc pe) — algebra/ramification part | SOUND-AFTER-REPAIRS (minor: p ∤ e used silently) |
| Prop 1.3 — "Gross–Zagier parameter x = 2" | GAP in the citation (GZ hypotheses fail); the arithmetic identity is trivial and correct |
| Remark after 1.3 (minimal hypotheses for B_{p,∞}) | SOUND-AFTER-REPAIRS (add v_p(pe) odd) |
| Prop 2.1 + isogeny reading | SOUND |
| Prop 2.2 | SOUND (mathematically trivial); one heuristic sentence over-labelled |
| Lemma 3.1 | SOUND (symbolically verified) |
| Prop 3.2 + ideal reading | SOUND |
| §3.3 | SOUND as Assessment; cited facts correctly stated |
| §3.4 (EVIDENCE) | SOUND — every number reproduced |
| §4 (ET Prop 1.6, square-mimicking) | SOUND (minor: same p ∤ e point) |
| Prop 5.1 | GAP — "PROVED modulo cited shape" cites a shape (GZ coprime-fundamental F(n)) that does not apply; conclusion repairable by a direct local argument (given below) |
| Novelty of x = 2 dictionary | UNVERIFIABLE (no hits; see §N) |
| Labels / scope of negative statement | Mostly honest; scope paragraph in §6 adequately limited |

## Claim-by-claim checks

### Lemma 1.1 — SOUND
`(1+2aw)(1+2bw) = 1 − 4abd + 2(a+b)w`; comparison with `e(2cw − p)` gives `4abd − 1 = pe`, `a+b = ce`, i.e.
ET's Type I tuple with `(x,y,z) = (abdp, acd, bcd)`. The bracketed equivalence `e | a+b ⟺ e | 4a²d+1` (given
`4abd ≡ 1 (e)`) is correct: `4ad(a+b) = (4a²d+1) + (4abd−1)` and `gcd(4ad,e) = 1`.
Brute force (`review_quat_brute.py 200`): for all 45 primes 3 ≤ p < 200 the set of Type I triples from raw
Egyptian-fraction search equals the set produced by the (a,c,d)-parametrisation. Note the map tuple → triple is
not injective (ET Prop 2.2: uniqueness only after imposing gcd(a,b,c) = 1, "quotienting by dilations"); e.g.
p = 107 has 17 triples but 23 tuples. Lemma 1.1 is an existence statement, so this is harmless (see MINOR-4).

### Lemma 1.2 — SOUND
Symbolic check: with `u = i`, `v = (j − i)/(2d)` in `(−d, −d(4dm−1))` one gets `u² = −d`, `v² = −m`,
`uv + vu = 1`; Gram `trd(x_i x_j)` on `(1,u,v,uv)` is exactly the author's matrix, determinant `−(4dm−1)²`.
Closure: `vu = 1 − uv`, `u·uv = −dv`, `uv·v = −mu`, `v·uv = (1−uv)v = v + mu`, `uv·u = u(1−uv) = u + dv`; all in the ℤ-span; fine.

### Prop 1.3 (ramification part) — SOUND-AFTER-REPAIRS
Re-derivation. `(−d, −dpe)`, `pe = 4abd − 1` odd, `gcd(d, pe) = 1`.
* ℓ odd, ℓ | e, ℓ ≠ p: `4a²d ≡ −1 (e)` ⇒ `−d ≡ (2a)^{−2}` is a unit square ⇒ symbol 1. ✓
* ℓ odd, ℓ | d: `(−d,−1)_ℓ(−d,pe)_ℓ = ((−1/ℓ)(pe/ℓ))^{v_ℓ(d)}` and `pe ≡ −1 (ℓ)` ⇒ 1. ✓
* ℓ = p: `(−d,−dpe)_p = (−d/p)^{v_p(pe)}` — this equals `(−d/p)` **only if p ∤ e**, which the proof uses silently.
  It is true: if p | e then p | a+b, `b ≡ −a`, `−4a²d ≡ 1 (p)`, so `(−d/p) = +1`, contradicting GEOMETRY Prop 5.1
  (whose proof I re-checked: `p ≡ −f (4d)`, `(−4d/f) = 1`, odd character ⇒ `(−4d/p) = −1`). (MINOR-1)
* ℓ = 2 via product formula: legitimate. Independently, my script evaluates the 2-adic symbol directly.
* ∞: both entries negative ⇒ −1. ✓

Numerics (own enumeration, own Hilbert symbol, p < 3000, all ET tuples with a ≤ b — 26007 tuples, i.e. all
dilates, more than the author's 19690 normalised triples): **Ram = {p, ∞} in every case; directly evaluated
symbol at 2 is +1 in every case; p | e never occurs.** The author's "27–42% failure of other splits" was not
re-checked (unimportant EVIDENCE remark).
Index e in every maximal order: reduced disc of maximal order of B_{p,∞} is p ⇒ index pe/p = e. ✓
Deuring step: Λ ⊂ some maximal O ≅ End E (Deuring); Deuring lifting of `(E,u)` and `(E,v)` separately gives CM
curves with CM by orders containing ℤ[√−d], ℤ[√−ab] reducing to E. Correct, with the author's own hedge that the
optimally embedded orders may be larger (e.g. `d ≡ 3 (4)`: `(1+u)/2` may lie in O). See MAJOR-1 for "x = 2".

### Prop 1.3 — "Gross–Zagier parameter x = 2": GAP (citation)
What is *proved*: the identity `(D₁D₂ − 4)/4 = 4abd − 1 = pe` for `D₁ = −4d`, `D₂ = −4ab`, and that the order
generated by ℤ[√D₁/2]=ℤ[u] and ℤ[v] (with `uv+vu = 1`) has reduced discriminant `(D₁D₂ − x²)/4`, x = 2 — this
matches the standard "order generated by two quadratic orders with relative trace x" computation (verified).
What is *cited*: Gross–Zagier, *On singular moduli* (Crelle 355, 1985). Their factorisation of
`J(d₁,d₂) = ∏(j(τ₁) − j(τ₂))` with factors `F((d₁d₂ − x²)/4)` is proved under the hypotheses **d₁, d₂ < 0
fundamental and coprime**. Here `D₁ = −4d`, `D₂ = −4ab` are never coprime (both ≡ 0 mod 4) and −4d is often
non-fundamental. So GZ's theorem does not apply; the correct framework is Lauter–Viray ("On singular moduli for
arbitrary discriminants", IMRN 2015), or a direct count of embeddings of Λ. (Source PDFs not in sources/; I
state GZ's hypotheses from memory — they are the well-known hypotheses of the main theorem.) → MAJOR-1.

### Remark after Prop 1.3 — SOUND-AFTER-REPAIRS
The listed sufficient conditions (`4dm ≡ 1 (p)`, `(−d/p) = −1`, `(−d/ℓ) = 1` for ℓ ∥^{odd} e) also need
`v_p(pe)` odd (e.g. p ∤ e); for general m (not from a Type I solution) p | e is not excluded a priori. Same in
Prop 2.1(i). (MINOR-1.)

### Prop 2.1 and the isogeny reading — SOUND
Prop 2.1 is Lemma 1.1 with b eliminated; `gcd(c,p)=1` automatic: `p | c` ⇒ `a+b ≥ pe = 4abd−1`, but
`a+b < 4ab−1` for a,b ≥ 1. ✓
Isogeny reading: I re-derived all pairings `⟨x,y⟩ = ½tr(x ŷ)` on `(φ₁, φ₂, uφ₁, uφ₂)`:
`⟨φ₁,φ₂⟩ = ½tr(v̂) = 0`, `⟨φ₁,uφ₂⟩ = ½tr(\widehat{uv}) = ½tr(uv) = ½`, `⟨φ₂,uφ₁⟩ = ½tr(vū) = −½`,
`⟨φ_i,uφ_i⟩ = ½deg φ_i·tr(ū) = 0`, `⟨uφ₁,uφ₂⟩ = ½d·tr(v̂) = 0`. So Gram = `[a,1,bd] ⊥ [b,−1,ad]`, det
`(4abd−1)²/16` (symbolic check), and Hom(E',E) has det `p²/16` ⇒ index e. Separability: `p ∤ ab` since
`4abd ≡ 1 (p)`. Converse direction: from such data, a = deg φ₁, b = deg φ₂, e := index, `4abd − 1 = pe` and
`e | deg(φ₁+φ₂) = a+b` ⇒ Type I. ✓ (Sound but, as the author says, a re-encoding.)

### Prop 2.2 — SOUND (trivially); one over-labelled sentence
`4dm − 1 = pe` with fixed (d,e) ⟺ `p ≡ −e^{−1} (4d)` (gcd(e,4d) = 1 is forced), m determined. ✓ The rewriting
`X² − Y² = 4ab = 4m`, `e | X` is correct. The sentence "The Siegel-theta reading … does not absorb (ii) …
p-dependent target set" is a heuristic, not a proof, but sits under a PROVED heading. (MINOR-2.) "Exactly the
shape of GEOMETRY_ES Prop 3.2" not re-checked by me.

### Lemma 3.1 — SOUND
Own quaternion arithmetic in `(−d,−p)`: `(2ai+j)(2bi−j) = (p − 4abd) − 2(a+b)k` exactly; norms
`N(2ai+j) = 4a²d + p`, `N(1+2ck) = 1 + 4c²dp`. With ET Type II (`4abd − p = e`, `a+b = ce`) this is
`−e(1+2ck)`; the identities `ef = 4a²d + p` (f = 4acd − 1) and `ff' = 1 + 4c²dp` check by hand
(`4acd·e = 4a²d + p + e`).

### Prop 3.2 + ideal reading — SOUND
Brute force: for all 45 primes p < 200 the Type II triples of raw search coincide with those generated from
"`4d | p+e`, `a | m = (p+e)/4d`, `e | a + m/a`" (`(x,y,z) = (abd, acdp, bcdp)`). `p | e` ⇒ `4abd ≤ 2(a+b)` ⇒
a=b=d=1, p=2: ✓.
Ideal reading: R = ℤ⟨i,j⟩ has reduced disc 4dp ✓; `α, β` primitive (j-coefficient ±1) ✓; for primitive
2×2 matrices over ℤ_ℓ with det ≡ 0 (ℓ^k), Smith form `U diag(1,δ) V` shows ker/im mod ℓ^k are free rank-1
summands, so `αβ ≡ 0 (ℓ^k) ⟺ im β̄ = ker ᾱ` ✓. Small point: the restriction "ℓ ∤ 2dp" is automatic for every
ℓ | e (e odd; gcd(e,d) | p; p ∤ e) — worth saying, otherwise it reads as if some primes of e were excluded.
"Brandt/Hecke T_e adjacency" is interpretation, fine.

### §3.3 — SOUND (as Assessment)
`disc[f,4ad,de] = 16a²d² − 4def = −4dp` ✓. √−dp of degree dp with p ramified factors as `ψ∘Frob`, ψ of degree d
between E^{(p)} and E ✓; d = 1 ⟺ E ≅ E^{(p)} ⟺ j ∈ 𝔽_p ✓ (Delfs–Galbraith: not accessed, statement standard).
The two matrices preserve the shape `[A, 4d·, d·]` (checked by hand: `[[1,2d],[0,1]]`: B ↦ B + 4dA,
C ↦ C + 2dB + 4d²A; `[[1,0],[2,1]]`: A ↦ A+2B+4C, B ↦ B + 4C) ✓; infinitude of representatives ✓ (stabiliser of
a definite form is finite). "Finitely many ES-good" relies on GEOMETRY Prop 4.1 (not re-checked).

### §3.4 — SOUND (all EVIDENCE reproduced)
`review_quat_fixed_de.py`: (5,23): p = 313, m = 360, a = 10, b = 36, a+b = 2·23 (ES); p = 73, m = 84, no divisor
(no ES); `(−5/313) = (−5/73) = −1`, `(−5/23) = 1`, and m ≡ 15 ≡ (4d)^{−1} (mod 23) in both. (10,7): 457 (a = 2,5)
vs 97 (none) ✓. Type II (1,7): 73 vs 97; (1,11): 73 vs 193 ✓. Filtered counts: **40/93 and 120/450 reproduced
exactly.**

### §4 — SOUND
ET Prop 1.6 checked against `sources/elsholtz-tao-1107.1010.pdf`: "For any odd perfect square n,
f_I(n) = f_II(n) = 0" ✓. Type I(n): GEOMETRY 5.1's argument gives `(−4d/n) = −1`, impossible for n an odd square
✓. "Symbol at p is `(−d/p)^{v_p(n)}`" again assumes p ∤ e (MINOR-1). Type II: `(n/f) = (−d/f) = −1` needs
gcd(n,f) = 1, which holds since p ∤ abd. Square-mimicking: `(f/p) = −(−1/p) = −1` for p ≡ 1 (4) forces a prime
ℓ | f with `(ℓ/p) = −1` ✓ (this is GEOMETRY Prop 5.2; "Lemma CT" not looked up).
