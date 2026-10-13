# R165 — hostile review of O165 `PARITY_FIXED_P.md` (branch side-agent/parity-fixed-p)

Reviewer: R165. Status: round 1 complete. **ES is not solved anywhere; nothing here changes that.**
From-scratch scripts: `scripts/review_pf_*.py` (none of the author's `pf_*` code reused).

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (II{a,d} hits ↔ (h,k,d), (4dhk−1) \| hn+k; bijection) | **SOUND** (from-scratch bijection check n ≤ 120) |
| Lemma 1.2 (Type I p-free up to one congruence) | **SOUND** (minor D1, D2) |
| Lemma 1.3 spin lemma (i),(ii) + "Consequence" | **SOUND** (20302 instances, 0 violations) |
| Prop 2.1 (≤ 5/8+o(1) χ_{−4d}-obstructed, relative to Burgess + Brun depth 2) | **SOUND-AFTER-REPAIRS** (minor D3, D4; Burgess-in-progressions step, ranges and uniformity all check) |
| (★) and §3.4 modular-hyperbola dictionaries | **SOUND** (four independent counts agree, p < 80) |
| §3.4 "Weil falls short by p^{1/2}" | **GAP** (heuristic exponent count; labelled Assessment, wording repair D6) |
| §3.2 mass conservation consequence "polylog family" | **GAP** (relies on heuristic f(p) ≍ 𝓛³; D7) |
| Main finding "H-B collapses into H-A" | **SOUND-AFTER-REPAIRS as Assessment** (correctly labelled mechanism-level; overclaims D5 MAJOR, D9) |
| R(p) at p ≈ 10⁸ | **SOUND**: R(100004521) = 44, R(100000007) = 62 recomputed independently |

No FATAL defects. One MAJOR (D5: the sign layer beyond χ_{−4d} is asserted to be sieve-bounded but is not
proved, and needs a varying-modulus input). The rest are MINOR. The author's agent was alive, waiting at its
checkpoint, when I finished (tmux window present, branch unchanged since b7840ad1), so I applied **no** R165
repairs to `PARITY_FIXED_P.md`.

## Claim-by-claim

### C1. Lemma 1.1 (row II{a,d} hits ↔ triples (h,k,d) with (4dhk−1) | hn+k) — **SOUND**

Re-derived: with q = 4ad, f = qh−1, g = N/f ≡ −n (mod q) so g = qk−n; fg = n+qa ⇔ qhk − hn − k = a ⇔
a(4dhk−1) = hn+k. h ≥ 1 since f ≥ 1; k ≥ 1 since qk = g+n > 0. Converse: 4adk = n + (k+a)/h > n gives g ≥ 1. Maps are
mutually inverse. Side remark m | hn+k ⇔ m | 4dh²n+1 is correct (4dhk ≡ 1 mod m, gcd(4dh,m)=1).
From scratch (`scripts/review_pf_dict.py`, `logs/review_pf_dict.txt`): with independent a-priori bounds
a,d ≤ n+2, h,k ≤ n+1 for the LHS and a *larger* box a,d ≤ 2n+6 for the RHS (so RHS elements outside the LHS box would
show up as mismatches), the two sets agree exactly for all n ≤ 120.

### C2. Lemma 1.2 (Type I p-free up to one congruence) — **SOUND** (minor presentation defects D1, D2)

Re-derived. gcd(f, cd) = 1: a prime r | gcd(f,cd) divides 4cdk = f+p, so r = p, excluded by p ∤ f. Then f is odd
(f ≡ −p mod 4), so gcd(f, 4c²d) = 1 and f | 4c²d(4dk²+1) ⇒ f | 4dk²+1. Forward direction needs no coprimality.
From scratch: LHS (box dk ≤ 40) and RHS (c ≤ 40+p/4+2, which covers every c = (f+p)/4dk with f ≤ 4dk²+1) agree for
all odd primes p ≤ 60.

### C3. Lemma 1.3 (spin lemma) and its "Consequence" paragraph — **SOUND**

(i) −4a²d ≡ p (mod ℓ), ℓ ∤ 2a ⇒ (−d/ℓ) = (p/ℓ) = (ℓ/p) (p ≡ 1 mod 4); and for odd ℓ ∤ d the Kronecker symbol
(−4d/ℓ) = (−d/ℓ). (ii) −4c²d ≡ p² ≢ 0 (mod ℓ). χ_{−4d} = (−4d/·) is a character mod 4d (−4d ≡ 0 mod 4) with
χ(−1) = −1, so a hit f ≡ −1 (mod 4ad) has χ(f) = −1. Consequence: N = p+4a²d is coprime to 2ad whenever p ∤ ad
(gcd(N,a) = gcd(p,a), gcd(N,d) = gcd(p,d), N odd), so for (d/p) = −1 the QNR prime factor is indeed automatic,
and for (d/p) = +1 the event is "even, nonzero number of QNR prime factors (with multiplicity)". Type I: χ(−p) =
−(−d/p) = −(d/p), test passed iff (d/p) = −1 — correct.
From scratch: 20302 (ℓ, slice) instances over p ≡ 1 (4), p < 400, a < 6, d < 30, both Type II (i) and Type I (ii)
(with c = a): 0 violations.

### C4. §3.3 (★) and §3.4 hyperbola dictionary — **SOUND** (as dictionaries)

(★): (A,B,C) with 4ABC − A − B = p ↦ (j,f) = (A, 4AC−1): B(4AC−1) = p+A, so f | p+j and f ≡ −1 (mod 4j); inverse
B = (p+j)/f. Conversely f ≥ 4j−1 > j forces j = (−p mod f). §3.4: (4AC−1)(4BC−1) = 4C(4ABC−A−B)+1 identity, and the
inverse map from (x,y) is as stated. From scratch, four independent counts — pairs (j,f), b-form, (A,B,C)-triples,
and hyperbola points (x ≡ 3 mod 4, C | (x+1)/4) — agree for every odd prime p < 80.

### C5. Proposition 2.1 (≤ 5/8 + o(1) of II{1,d}, (d/p)=+1 slices are χ_{−4d}-obstructed) — **SOUND-AFTER-REPAIRS** (minor: D3, D4)

Re-derived step by step.
* Reduction: ℓ | N_d odd, ℓ ≠ p ⇒ ℓ ∤ d, so Lemma 1.3(i) applies; obstructed ⇒ no ℓ ∈ 𝒫 divides N_d. ✔
* Σ_{ℓ∈𝒫} 1/ℓ ≥ 1/2 − o(1): Σ_{n≤z, n odd} (n/p) = S(z) − (2/p)S(z/2) = o(z) by Burgess (z/2 ≥ p^{1/4+ε/2}); every odd
  QNR n ≤ z < p has a prime factor in 𝒫; union bound z/4 − o(z) ≤ Σ_{ℓ∈𝒫}(z/(2ℓ) + 1) and π(z) = o(z). ✔ (the text
  compresses the union-bound step and leaves a draft fragment "…— to avoid the prime 2"; D3).
* Greedy 𝒫′ with μ ∈ [1/2 − o(1), 5/6] exists since 1/ℓ ≤ 1/3. Bonferroni 1[X=0] ≤ 1 − X + X(X−1)/2 holds for all
  integers X ≥ 0. ✔
* Counting in progressions: r | N_d ⇔ d ≡ c_r := −p·4̄ (mod r) (r odd, c_r ≢ 0). #{d ≤ p/4 : d ≡ c_r, (d/p)=1} =
  ½(p/(4r) + O(1)) + ½ Σ_t ((c_r + rt)/p), and ((c_r+rt)/p) = (r/p)((t + c_r r̄)/p) is a character sum over an
  *interval* of length L = p/(4r) ≥ p^{1/2−2ε}/4 (r ≤ z² = p^{1/2+2ε}). Burgess is uniform in the shift and gives
  O(L·p^{−δ(ε)}) once L ≥ p^{1/4+ε'}, i.e. for ε < 1/12 (the text's "p^{1/2−3ε} ≥ p^{1/4+ε}" needs ε ≤ 1/16 —
  state it). Relative error p^{−δ} uniform in r ✔. The O(1) rounding terms are not mentioned in the text, but there
  are ≤ π(z)² ≤ p^{1/2+2ε} = o(p) of them, so they are harmless (D3). Pólya–Vinogradov would *not* suffice for the
  pairs — Burgess is genuinely needed there and is correctly invoked.
* Final optimisation: 1 − μ + μ²/2 is decreasing on [0,1], value 5/8 at μ = 1/2. ✔ |𝓑| ~ p/8 by Pólya–Vinogradov. ✔
* Uniformity: the o(1) depends only on ε (fixed) via the Burgess exponent; no parameter-dependent constants. ✔
"PROVED relative to Burgess" is accurate (Burgess is an unconditional theorem, so this is simply PROVED).

From-scratch exhaustive check (`scripts/review_pf_prop21.py`, `logs/review_pf_prop21.txt`; ALL d ≤ p/4, a = 1):
obstructed fraction 0.589 (p = 1002121 ≡ 1 mod 840), 0.567 (p = 10001881 ≡ 1 mod 840), 0.284 (p = 1000037),
0.311 (p = 10000121). Consistent with ≤ 5/8; for p ≡ 1 (mod 840) (2,3,5,7 all QR) the bound is nearly attained at these
sizes, so 5/8 is not a loose bound in practice. Note the author's EVIDENCE line (pass rates 0.39–0.60) samples
**all a** with 4a²d ≤ p (box-weighted), not the a = 1 family of the proposition (D4).

### C6. R(p) recomputation at p ≈ 10⁸ — **SOUND** (matches)

`scripts/review_pf_R.py` (b-form, complete range b ≤ (4p+1)/3, which suffices since j ≤ (p+1)/3; cross-checked against
direct (A,C) enumeration for p = 101, 1009, 10007, 100003): **R(100004521) = 44, R(100000007) = 62**, identical to the
author's log. Dyadic profiles have 0–8 hits per block, as stated (`logs/review_pf_R.txt`).

### C7. §3.4 "Weil falls short by p^{1/2}" and §3.2 mass conservation — **GAP (heuristic, label repair)** (D6, D7)

The hyperbola dictionary is PROVED (C4). The density of 𝓗 = {xy ≡ 1 mod 4p} is φ(4p)/(4p)² ≈ 1/(8p) ✔, and
box counts with error O(p^{1/2+ε}) (Weil/Kloosterman) are standard ✔. But the quantitative "short by p^{1/2}" is a
heuristic exponent count, not a derived statement: the success set {xy = 4Cp+1, 4C | x+1, 4C | y+1} is a subset of 𝓗
cut out by an *arithmetic* condition depending on the point's height C = (xy−1)/4p, not a union of boxes or of
smooth regions, so box-equidistribution — at any error level — does not count it at all. "Strip area ≈ block
length" and "O(1) expected 𝓗-points per curve-block" are not defined or derived. The correct, defensible statement
is qualitative: Weil asymptotics need boxes of area ≫ p^{3/2+ε} (≫ p^{1/2} points of 𝓗), whereas the target is an
arithmetically defined subset with 𝓛^{O(1)} points; so Weil gives nothing, and no box-counting improvement alone
would. Section 3.4 is tagged "PROVED dictionary + Assessment", so this is a wording/label issue, not a false theorem.

§3.2: "number of certificates ≤ M·f(p)" is trivially PROVED; but the consequence "a polylog-length family, with no
power-length bilinear ranges" uses the *heuristic* f(p) ≍ 𝓛³. Unconditionally (Elsholtz–Tao f(p) ≪ p^{3/5+o(1)})
the argument only gives X ≤ p^{3/5+o(1)}𝓛^{O(1)}, which does not exclude power-length families. Label the
consequence Assessment/heuristic (D7). (ET's bound is quoted correctly: f(n) ≪ n^{3/5+O(1/log log n)}.)

Also checked I2 (`scripts/review_pf_i2.py`): the identity (p+2c√−d)(1+2cdt+pt√−d) = p + (2c+tN)√−d and N | N′ hold,
but c′ = c + tN/2 is an integer **only for even t** (N odd); 441/441 odd-t cases give non-integral c′ (D8).

### C8. "Main finding": H-B collapses into H-A — **SOUND-AFTER-REPAIRS as an Assessment; overclaimed in two places** (D5, D9)

What is right: it is labelled Assessment and "mechanism-level, not a theorem" in §5, and the Remark 2.4 caveat is
kept. The core observation — a fixed-p route needs *upper* bounds on bad classes, and upper-bound sieves carry no
parity barrier; the hit count Σ_{fg=N_θ} 1[q_θ | f+1] has unit coefficients over the consecutive integers p+j, so no
Möbius/Liouville-type Type II sum is requested — is correct and well argued. Prop 2.1 is a genuine T1-passing
illustration.

What is overclaimed:
* §5 / Assessment 2.2 say the prime, Q, Q′ classes are "bounded above by sieves without parity breaking" and that
  "sieves give" these bounds. Proved: only the χ_{−4d}-character, only on a = 1, only ≤ 5/8 (Prop 2.1), plus the
  prime class. The Q class is a union over up to 2^{ω(4ad)} quadratic characters, most of which have conductor
  r | d, r up to ≈ p — Lemma 1.3's reciprocity does not move those to the fixed modulus p, so the sieve has
  d-dependent sifting sets (Remark (3) concedes the union bound fails). Q′ (higher-order characters mod a varying
  q) has no reciprocity reduction at all. In the corr memo table, Q ≈ 63 % and Q′ ≈ 2 % of slices at p ≈ 10⁶, so
  what is needed is #(prime ∪ Q ∪ Q′) ≤ (1 − δ)·#slices — a quantitative upper bound that is open. The obstacle there
  is uniformity over varying moduli, not parity; the conclusion "parity is not the binding constraint" survives, but
  "H-B collapses into H-A" should read "into H-A plus an open varying-modulus upper-bound sieve for the sign layer
  (parity-free)".
* "No step of a fixed-p ES argument needs to distinguish λ(n) = +1 from −1" and "no FI Type II input is even
  *requested* by the problem" are universal claims over all possible arguments. An argument that restricts to a
  structured sub-family (e.g. θ with N_θ = P₂ or y-smooth, to make the divisor layer tractable) would reintroduce a
  lower-bound sieve, and with it parity. Scope these to "the natural/unweighted formulation (★)".

## Numbered defects

**D5 (MAJOR) — §2 Assessment 2.2 ¶1 and §5 "Main finding" ¶1: sign-layer upper bounds overclaimed.** "The layers
prime, Q, Q′ are multiplicative-class sets, bounded above by sieves without parity breaking" / "which sieves give
without parity breaking". Only χ_{−4d} on a = 1 (≤ 5/8) and the prime class are proved. The full Q class (a union
over ≤ 2^{ω(q)} characters, conductors up to ≈ p, d-dependent) and Q′ (higher order, no reciprocity) are not
handled, and what is needed is ≤ (1−δ)·#slices with Q alone ≈ 63 % (corr memo table). *Repair:* replace with
"…are bad classes for which only **upper** bounds are needed, so parity is not the obstacle. Proved here: χ_{−4d}
on a = 1 (Prop 2.1) and the prime class. Bounding the full Q ∪ Q′ layer below 1 − δ needs a sieve whose sifting
sets vary with the modulus q_θ — an open, parity-free uniformity problem." Change "collapses into H-A" to "collapses
into H-A plus a parity-free varying-modulus sign-layer bound". Update the §0/report item 4 and I5/I7 to match.

**D9 (MINOR) — §2 Assessment 2.2 ("No step of a fixed-p ES argument needs to distinguish λ(n) = +1 from −1") and §5
("no Friedlander–Iwaniec Type II input is even *requested*").** These are universal over all arguments. *Repair:*
"In the natural unweighted formulation (★) no step needs to …". Add a sentence noting that restricting to structured
sub-families (N_θ = P₂, smooth N_θ) would reintroduce lower-bound sieves and parity.

**D6 (MINOR) — §3.4 last four sentences and I4.** "falls short by p^{1/2}", "strip area ≈ block length", "O(1)
expected 𝓗-points per curve-block" are not derived, and the success set is arithmetic, not a union of boxes.
*Repair:* use the qualitative form in C7: Weil needs boxes of area ≫ p^{3/2+ε}, i.e. containing ≫ p^{1/2} points
of 𝓗, while the target is an arithmetically defined subset with 𝓛^{O(1)} points. So box equidistribution, even
with a better error term, does not see it. Keep it labelled Assessment.

**D7 (MINOR) — §3.2 last two sentences.** "polylog-length family, with no power-length bilinear ranges" follows
only from the heuristic f(p) ≍ 𝓛³. *Repair:* add "(heuristic; unconditionally ET only give X ≤ p^{3/5+o(1)}𝓛^{O(1)})"
and label the consequence Assessment.

**D3 (MINOR) — Prop 2.1 proof.** (a) The draft fragment "Σ 1/ℓ ≥ 1/2 − 1/2·[(2/p) = −1] − o(1)… — to avoid the
prime 2, use odd n" should be cleaned up, and the union-bound step z/4 − o(z) ≤ Σ_ℓ (z/(2ℓ)+1) should be written
out. (b) State ε < 1/16, which is what "p^{1/2−3ε} ≥ p^{1/4+ε}" needs; the actual length is ≥ p^{1/2−2ε}/4. (c)
Mention that the O(1) rounding errors in #{d ≤ p/4 : d ≡ c_r (r)} sum to ≤ π(z)² = O(p^{1/2+2ε}) = o(p). (d) "PROVED
relative to Burgess" can simply be PROVED, since Burgess is unconditional.

**D4 (MINOR) — §2 EVIDENCE line after Prop 2.1.** The numerics (`pf_spin.py`) sample box-weighted slices over
**all** a with 4a²d ≤ p, not the family a = 1, d ≤ p/4 of Prop 2.1. *Repair:* say so, or cite the exhaustive a = 1
numbers: obstructed 0.589 / 0.567 at p = 1002121 / 10001881 (≡ 1 mod 840) and 0.284 / 0.311 at p = 1000037 /
10000121 (`logs/review_pf_prop21.txt`). Note that at p ≡ 1 (mod 840) the 5/8 bound is nearly attained.

**D10 (MINOR) — Remark (2) after Prop 2.1, and I7.** "the 'prime' class (≤ (2+o(1))|𝓑|/log p)": restricting to
(d/p) = +1 means counting primes N ∈ (p, 2p] with (N/p) = +1, i.e. a prime-character sum of length ≍ the
conductor. That is Siegel-zero sensitive and not available unconditionally (Brun–Titchmarsh mod p at x = 2p is
useless). Provable: ≤ (4+o(1))|𝓑|/log p (all d, PNT mod 4), which equals (2+o(1))/𝓛 of *all* slices, as I7
correctly says. Also "proportion → 0 like (log p)^{−1/2}" is only an upper bound O((log p)^{−1/2}) (Selberg), and
the proof is not given. *Repair:* fix the constant, write "≪ (log p)^{−1/2}", and mark it "sketch".

**D11 (MINOR) — §3.3 vs §3.4/§5 consistency.** The heuristic M(B) ≈ (log 2/4)·log(B/4) grows like log B.
Summing over blocks gives ≈ (log p)²/8 ≈ 44 at p ≈ 10⁸, in good agreement with R = 44. So "O(1) expected events per
dyadic block" (§3.4, §5) should read "≍ log B per block (single digits in practice)", and "no block's count grows with
p" should say "for fixed B".

**D8 (MINOR) — I2.** c′ = c + tN/2 is an integer only for even t, since N = p² + 4c²d is odd (checked:
`scripts/review_pf_i2.py`). *Repair:* "t even".

**D1 (MINOR) — Lemma 1.2, the "m-form" (Type I(p) ⟺ ∃ m, k | m, f | 4mk+1, p ≡ −f mod 4m).** The p ∤ f condition is
silently dropped. (⇐) still yields a solution of the Type I equation, possibly non-primitive, and (⇒) is fine.
*Repair:* add "(p ∤ f for primitive solutions)" or note that the forward map does not use it.

**D2 (MINOR) — Lemma 1.2 proof, first sentence.** It is garbled ("as 4cd | f+p, resp. as 4dk | f+p and c = (f+p)/4dk...
directly: …"). *Repair:* "a prime r | gcd(f, cd) divides 4cdk = f + p, so r = p, excluded; f ≡ −p (mod 4) is odd,
so gcd(f, 4c²d) = 1."

Cosmetic: in (★) the letter f denotes the Lemma 1.1 modulus m = 4dk − 1 (with (a,d,k) = (B,C,A)), not the row-II
divisor f. State the identification (j,f) = (A, 4AC−1).

## Scripts / logs (R165, from scratch)
* `scripts/review_pf_dict.py` → `logs/review_pf_dict.txt`: Lemmas 1.1, 1.2, 1.3, (★), §3.4.
* `scripts/review_pf_prop21.py` → `logs/review_pf_prop21.txt`: exhaustive a = 1 obstruction fractions.
* `scripts/review_pf_R.py` → `logs/review_pf_R.txt`: R(p) at p ≈ 10⁸ plus dyadic profile.
* `scripts/review_pf_i2.py`: the I2 composition identity.
