# GROWING_IDENTITIES — exact identities with growing level (task O170, SPARK, hatch H-E)

Status: internal research note. **ES is not solved here, nor any infinite case of it.** Labels as in
DISCOVERIES.md. Scripts `scripts/gi_*`. Inputs read: STRONG_APPROX_ES.md (O167, branch side-agent/strong-approx;
§7, Thm 9.1, Cor 9.3), EXACT_FORMULA.md (O131; Prop 4.1 = signed decomposition with KH-type boundary),
CONDITIONAL_ES.md Lemma 1.1, PARITY_FIXED_P.md (O165, branch side-agent/parity-fixed-p; Lemmas 1.1–1.3).

Goal (brief): an exact identity (weighted ES count at n) = Σ_{g ≤ G(n)} (explicit expression in n, g) whose right
side has a provable sign at primes n ≡ 1 (24) and vanishes at odd squares. Thm 9.1 (finite Eisenstein
combinations are T1-dead) does not apply when the level grows with n.

## Summary (checkpoint 1)

* **Exact growing-level identities found (PROVED, elementary):** continuant/Hirzebruch–Jung form of Type I
  (a = 1) and Type II (Lemma 1.1; the HJ-length-3 description covers the certificates with all entries ≥ 2 —
  boundary words with an entry 1 are extra, cf. DEDEKIND_ES §4.2 (R170 repair)); two inequivalent growing-level divisor sums for the same cubic (Lemma 1.2);
  the T1-respecting identity `W(n) = Σ_{D*(n)} (1 − (m''/n))/2` over a finite sign-blind set (R170 repair: D*(n)
  excludes the trivial m'' = 1, which makes it finite with t ≤ n + 2), in which the
  "sign at ∞" (class −1 vs +1 mod the level) is *exactly* the Jacobi symbol at n (Prop 4.1).
* **Trace formulas (PROVED relative to Cohen's Eichler–Selberg formula, implemented and checked):** ES is the
  sign-odd part of the split-hyperbolic term (Prop 2.1). *Assessment (R170 repair):* this term is typically
  small compared with the a-priori size of the trace (not always: at genus-0 levels A₂ = −A₃ exactly), and
  certifying positivity through the identity needs the cusp trace ≍ kq-fold (dim S_k(Γ₁(q))/(φ(q)/2)) below
  Deligne at a single N (Prop 2.2). *Assessment (§3):* KH's re-summation mechanism needs the shift to be a
  theta-series variable; ES shifts gN + 1 are multiplicative.
* **No positive identity.** Every identity found either (i) is a relabelling of the divisor-in-class count,
  (ii) puts ES in a subdominant term, or (iii) reduces positivity to the H-B spin event (O165). ES is not solved.

## 0. Notation

For integers g ≥ 1, r and N ≥ 1 put `τ_{r,g}(N) := #{m ≥ 1 : m | N, m ≡ r (mod g)}`.
* `R(n) := #{(c,f,g) ∈ ℕ³ : cfg − c − f = n}` — all points of the Type I a = 1 cubic (no mod-4 condition).
* `W(n) := #{(c,f,g) ∈ ℕ³ : cfg − c − f = n, fg ≡ 1 (mod 4)}` — Type I, slice a = 1 (CONDITIONAL_ES Lemma 1.1:
  W(n) > 0 ⇒ ES(n)). By Lemma 1.1 (1⇔2), `W(n) = Σ_{t ≥ 1} #{m | tn+1 : m ≡ −1 (t), 4 | m}`.
* `T2(n) := #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc}` (Type II, ordered; O131 uses a ≤ b).

Computation: `scripts/gi_counts.py N` (exact enumeration of the cubics; n ≤ 2000 in a few seconds).
Control: W(m²) = T2(m²) = 0 for all odd m ≤ 44 (T1), W(n) = 0 for even n (fg odd ⇒ n odd).

## 1. Exact rearrangements with growing level (PROVED, elementary)

**Lemma 1.1 (continuant form).** Put `S_x := [[x, −1],[1, 0]] ∈ SL₂(ℤ)` and let `K⁻(x₁,…,x_r)` be the (1,1)
entry of `S_{x₁}⋯S_{x_r}` (negative continuant; `K⁻(x) = x`, `K⁻(x,y) = xy − 1`, `K⁻(x,y,z) = xyz − x − z`).
Then
* `R(n) = #{(c,g,f) ∈ ℕ³ : K⁻(c,g,f) = n}`, `W(n)` = same with `gf ≡ 1 (4)`;
* `T2(n) = #{(a,b,c,d) : K⁻(a, 4cd, b) = cn}` (since `K⁻(a,4cd,b) = 4abcd − a − b`);
* `S_c S_g S_f = [[n, −(cg−1)],[gf−1, −g]]`, so a Type I (a = 1) certificate is an SL₂(ℤ) word of length 3 with
  (1,1) entry n; for c,g,f ≥ 2 the word is the Hirzebruch–Jung expansion `n/m = [[c,g,f]] = c − 1/(g − 1/f)`
  with `m = gf − 1`. Hence (entries ≥ 2): **W-certificates with c, g, f ≥ 2 ↔ residues m ∈ [1,n), 4 | m,
  (m,n) = 1, such that n/m has Hirzebruch–Jung length exactly 3.** Words containing a 1 reduce by
  `S_a S_1 S_b = S_{a−1}S_{b−1}`. *(R170 repair)* The restriction is essential: boundary certificates (an entry
  = 1; DEDEKIND_ES §4.2) exist, and for n ≡ 1 (4), n ≤ 300, they are the **only** W-certificates at
  n = 5, 17, 41, 65, 209, 241, 265 (no HJ-length-3 m ≡ 0 (4) there; R170 `scripts/review_gi_identities.py`).
*Proof.* Direct multiplication; uniqueness of HJ expansions with entries ≥ 2. ∎

**Lemma 1.2 (fibration swap).** Fibring the cubic `cfg − c − f = n` by g, resp. by c, gives
`R(n) = Σ_{g ≥ 1} τ_{−1,g}(gn + 1) = Σ_{c ≥ 1} τ_{−1,c}(n + c)`,
and with the mod-4 condition `W(n) = Σ_{t} #{m | tn+1 : m ≡ −1 (t), 4 | m} = Σ_{c} #{e | n+c : e ≡ −1 (c),
(n+c)/e · (e+1)/c ≡ 1 (4)}`. The two growing-level sums are **not** termwise equal (g = 2: τ(2n+1) vs
τ_odd(n+2)). *Proof.* For fixed c: `f(cg−1) = n + c`, e := cg − 1. For fixed g: Lemma 1.1 of CONDITIONAL_ES. ∎
This is the exact form of the brief's "swap the order of summation": summing over m first (the divisor) gives
`#{t : t | m+1, tn ≡ −1 (m)} ∈ {0,1,2}`, i.e. *(R170 repair, exact form)* with r_m := −n⁻¹ mod m ∈ [1, m),
`W(n) = #{4 | m, (m,n) = 1 : r_m | m + 1} + #{4 | m : m | n + 1}` (the second, boundary term is t = m + 1, i.e.
r_m = 1; it vanishes for n ≡ 1 (4); checked n ≤ 120 by R170); the
modulus of the inner congruence is the summation variable, so nothing telescopes — every exact re-summation of
the cubic is again a divisor-in-class count (B2), now with the level as the summation variable.

**Lemma 1.3 (the T1-respecting rewrite: a character at the place n).** Let n ≡ 1 (mod 4). For every
Type I (a = 1) certificate, `tn + 1 = m·m''` with `4 | m`, `m'' ≡ −1 (t)`, one has t ≡ 3 (4) and the Jacobi
symbol `(m''/n) = −1`. Consequently
`W(n) = Σ_t Σ_{m'' | tn+1, m'' ≡ −1 (t), 4 | (tn+1)/m''} (1 − (m''/n))/2`,
and at n = k² every summand vanishes, `(m''/k²) = 1`.
*Proof.* tn ≡ −1 (4) forces t ≡ 3 (4). Write m'' = 2^j u, u odd, ε(x) := (x−1)/2. For a prime ℓ | u,
−t ≡ n⁻¹ (mod ℓ), so (−t/ℓ) = (n/ℓ); hence (n/u) = (−t/u), and (u/n) = (n/u) (reciprocity, n ≡ 1 (4)).
From m'' ≡ −1 (t): u ≡ −2^{−j} (t), so (u/t) = (−1/t)(2/t)^j = −(2/t)^j, and
(−t/u) = (−1)^{ε(u)}(u/t)(−1)^{ε(t)ε(u)} = −(2/t)^j. So (m''/n) = (2/n)^j (u/n) = −(2/(tn))^j. If j ≥ 1 then
2^{j+2} | tn + 1, so tn ≡ 7 (8) and (2/(tn)) = 1. Hence (m''/n) = −1. ∎ (Checked: all 4901 certificates of
n ≡ 1 (4), n ≤ 3000, `scripts/gi_spin_check.py`, 0 violations.)
*Reading.* This is the analogue, for the family tn + 1, of PARITY_FIXED_P Lemma 1.3 (same reciprocity mechanism;
O165's lemma concerns primes ℓ | p + 4a²d resp. p² + 4c²d with the character χ_{−4d}) (R170 repair). The only T1-respecting factor available is a
genus character **at the place n** (the "main term with genus data at the place p" asked for in O167 §11);
but here it is identically −1 on certificates, i.e. it carries no information beyond the class condition.

## 2. Eichler–Selberg: where ES sits in a trace formula (dictionary PROVED relative to Cohen's formula)

**Input.** Cohen's form of the Eichler–Selberg trace formula (Cohen–Strömberg, *Modular Forms*, Thm 12.4.11):
for k ≥ 2, χ mod q with χ(−1) = (−1)^k, `Tr(T_N | S_k(Γ₀(q),χ)) = A₁ + A₂ + A₃ + A₄` with A₁ the identity term
(only for N a square), A₂ the elliptic term `−½ Σ_{t² < 4N} (ρ^{k−1} − ρ̄^{k−1})/(ρ − ρ̄) Σ_f h_w((t²−4N)/f²) μ(t,f,N)`
(Hurwitz class numbers of t² − 4N, twisted by `Σ_{x mod q, x² − tx + N ≡ 0} χ(x)`), A₃ the split-hyperbolic
term `−½ Σ_{dd' = N} min(d,d')^{k−1} Σ_{τ | q, …} φ((τ, q/τ)) χ(y_τ)` (y_τ ≡ d mod τ, ≡ d' mod q/τ), and A₄ the
k = 2, χ = 1 term. Implemented in `scripts/gi_trace.py`; transcription checked: dim S₂(Γ₀(N)) = genus X₀(N)
for N ≤ 30, Σ_{χ even} dim S₂(q,χ) = genus X₁(q) for q ≤ 18, dim S₃(Γ₁(7)) = 1, Tr T₂|S₁₂(1) = −24,
Tr T_n|S₂(11) = a_n(11a), n ≤ 10.
*(R170 repair, full form of the terms used.)* For (N, q) = 1: A₂'s inner factor is
`μ(t,f,N) = ψ(q)/ψ(q/q_f) · Σ_{x mod q, x² − tx + N ≡ 0 (mod q_f·q)} χ(x)`, q_f := (q, f), with f running over
f² | t² − 4N, (t² − 4N)/f² ≡ 0, 1 (4), and h_w = h/(w/2); A₃'s τ-sum runs over τ | q with
`(τ, q/τ) | gcd(q/𝔣_χ, d − d')`, y_τ defined mod q/(τ, q/τ). (Independently re-implemented and tested by R170,
incl. a non-trivial χ with N > 1: Tr T_n | S₃(Γ₀(7), (·/7)) = coefficients of η(z)³η(7z)³; `scripts/review_gi_trace.py`.)

**Proposition 2.1 (ES slice = odd part of the cusp-fixed-point term).** Let q ≥ 3 and N ≡ 1 (mod q) (the Type II
divisor form of O131 §1: q = 4cd, N = 4c²dn + 1, certificate = divisor of N in the class −1 mod q). In A₃ the τ = q and τ = 1
summands contribute `χ(d) + χ(d') = χ(d) + χ̄(d)`. Summing over the characters of parity (−1)^k with weight
χ̄(−1) (a constant, = (−1)^k, on this family — it only fixes the global sign) gives, in these summands
(including A₃'s prefactor −½; R170 repair of sign/normalisation),
`−(φ(q)/2)·Σ_{dd'=N} min(d,d')^{k−1} ( [d ≡ −1 (q)] + (−1)^k [d ≡ +1 (q)] )`
(the τ = 1 and τ = q summands each give half; checked numerically by R170, `scripts/review_gi_prop21.py`).
So the ES class −1 appears **always together with the class +1**, with relative sign (−1)^k, and with the weight
min(d,d')^{k−1}. The class +1 contains the trivial divisor d = 1 (O131 Prop 4.1's "−2 per level", = O128
Prop 8.3's sign at ∞). Separating −1 from +1 needs both parities of k, i.e. two identities with different
weights min^{k−1}. (With weight min^{k−1} the trivial divisor d = 1 has weight 1, while an ES divisor
d ≡ −1 (q) has weight ≥ (q−1)^{k−1}; R170 note.) *Geometric reading (Assessment — interpretation, not part of
the proved statement; R170 repair):* A₃ is the contribution of the cusps of X₁(q) fixed by the Hecke
correspondence T_N; the curve identifies P with −P, so it sees only the classes ±d. The sign — which is
exactly the ES information (O128 Prop 8.3) — is invisible to the curve and visible only to odd-weight line
bundles. *Proof.* Orthogonality of characters of fixed parity: `Σ_{χ(−1)=ε} χ(d) = (φ(q)/2)([d≡1] + ε[d≡−1])`. ∎

**Proposition 2.2 (trivial bounds; PROVED — R170 repair: everything beyond the two bounds is Assessment).** In
the identity `Σ_{χ(−1)=(−1)^k} χ̄(−1)·Tr(T_N | S_k(q,χ)) = Σ_χ χ̄(−1)(A₁ + A₂ + A₃ + A₄)` (left side
= (−1)^k Tr(T_N | S_k(Γ₁(q))) restricted to the parity-(−1)^k part), the ES-relevant part of A₃ is, by Prop 2.1,
(φ(q)/2) times a class sum of absolute value ≤ `τ(N)·N^{(k−1)/2}`, while Deligne's bound for the cusp trace is
`dim S_k(Γ₁(q))·τ(N)N^{(k−1)/2}`.
*Assessment (R170 repair).* There is no known independent way to evaluate the cusp trace at a single N, so a
positivity proof for the ES class through this identity would need the cusp trace to better than
**dim S_k(Γ₁(q))/(φ(q)/2) ≍ kq-fold cancellation below Deligne at one N** (e.g. dim S₃(Γ₁(24)) = 20 vs
φ(24)/2 = 4; earlier text said "q²-fold", which is off by ≍ φ(q)). The ES term is *typically* small compared
with A₂, but not always: when S_k(Γ₁(q)) = 0 and N is not a square the identity reads A₂ = −A₃ (k = 3), resp.
A₂ + A₄ = −A₃ (k = 2), exactly. Cohen's formula is valid only for k ≥ 2; setting k = 1 (where ρ⁰ − ρ̄⁰ = 0)
proves nothing — heuristically the weight-1 analogue is the weight-1 Eisenstein identities of O131 §3 (finite
level, killed by STRONG_APPROX Thm 9.1). At fixed genus-0 level (S_k(Γ₁(q)) = 0: k = 2, q ≤ 10 or 12; k = 3, q ≤ 6)
the identities are exact class-number relations, but a finite menu of levels (B2).
*Assessment.* KH/Eichler–Selberg identities are exact with a growing *range* (t² < 4N) but at fixed level;
ES enters them only as the boundary (split-hyperbolic) term, which is typically small (not always, see above;
R170 repair), and carries the sign
information only through odd weight. This is the trace-formula form of B3 (main term ≫ certificate).

## 3. What made Kronecker–Hurwitz work, and why the ES sum over g lacks it (Assessment; R170 repair: label)

KH: `Σ_{t² ≤ 4N} H(4N − t²) = 2σ(N) − λ(N)`, `λ(N) := Σ_{d|N} min(d, N/d)`, H(0) = −1/12 (re-checked N < 400 by
R170, `scripts/review_gi_kh.py`; R170 repair: λ defined) re-sums a family of *shifted* arguments 4N − t² of growing length. It
works because the shifts are the coefficients of a theta series in the **same** modular variable:
`Σ_t H(4N−t²)` is the 4N-th coefficient (R170 repair: was "N-th") of `ℋ(τ)·θ(τ)` (weight 3/2 mock × weight 1/2), and holomorphic projection
lands in the finite-dimensional M₂(Γ₀(4)) (Zagier; Mertens 2014 for the twisted versions); λ is the shadow
correction. The ES family `Σ_g τ_{−1,g}(gN+1)` (R170 repair: notation of §0) has the shift entering **multiplicatively** (argument gN + 1,
modulus g): extracting the coefficients ≡ 1 (mod g) of a level-g form and rescaling by g is a U_g-type
operator, landing at level ≍ g². Summing over g ≤ N is therefore a sum over **unboundedly many levels**, not a
product of two forms of fixed level: no finite-dimensional target space, hence no holomorphic-projection
re-summation. (Sums over a growing *modulus* of level-g data are Poincaré-series/Kloosterman objects; in that
language (O167 Lemma 10.1, second normalisation; R170 repair: c and c | M/4 restored) Type II(p) is the set of
`γ' = [[f, cM],[p, f']] ∈ SL₂(ℤ)` with `f ≡ f' ≡ −1 (mod M)` and the non-congruence condition `c | M/4` — and the Kloosterman modulus is n itself, fixed.)

## 4. The sign at ∞ *is* the genus character at the place n (PROVED, elementary)

Props 2.1 (trace formula), O128 Prop 8.3 (Siegel–Weil / local+spinor), O131 Prop 4.1 (Eisenstein) all meet the
same wall: geometric counts see the classes ±1 (mod level) together; ES is the −1 class. The following makes
the separating datum explicit in slice a = 1.

**Proposition 4.1.** (R170 repair: identity restated over the finite set D*(n).) Let n ≡ 1 (4), t ≡ 3 (4), `tn + 1 = m·m''` with 4 | m, and `m'' ≡ ε (mod t)`, ε = ±1.
Then the Jacobi symbol `(m''/n) = ε`. Consequently, with the sign-blind set
`D(n) := {(t, m'') : t ≡ 3 (4), m'' | tn+1, 4 | (tn+1)/m'', m'' ≡ ±1 (mod t)}`,
and `D*(n) := D(n) \ {m'' = 1}`,
`W(n) = Σ_{(t,m'') ∈ D*(n)} (1 − (m''/n))/2`,
i.e. **ES (Type I, a = 1) at n ⟺ D*(n) contains a quadratic non-residue mod n** (Jacobi sense), and the
trivial elements (m'' = 1 etc., class +1) are automatically residues.
*Proof.* As in Lemma 1.3 with −1 replaced by ε: m'' = 2^j u, u ≡ ε·2^{−j} (t), (u/t) = (ε/t)(2/t)^j; since
t ≡ 3 (4), (−t/u) = (u/t); primes ℓ | u have (−t/ℓ) = (n/ℓ); so (m''/n) = (2/n)^j (n/u) = (ε/t)(2/(tn))^j = ε,
using (−1/t) = −1 and tn ≡ 7 (8) when j ≥ 1. *Finiteness (R170 repair):* D(n) is infinite (m'' = 1 ∈ D(n) for
every t ≡ 3 (4); these terms contribute 0), but every (t, m'') ∈ D*(n) has t ≤ n + 2: m·m'' ≡ 1 (t) gives
m ≡ m'' ≡ ε (t); 4 | m ⇒ m ≥ t − 1; m'' ≠ 1 ⇒ m'' ≥ t − 1; so (t − 1)² ≤ tn + 1. Hence D*(n) is finite. ∎ (`scripts/gi_sign_check.py`: n ≡ 1 (4), n ≤ 4000, all
t ≡ 3 (4): 512464 class-(+1) pairs all with symbol +1, 7044 class-(−1) pairs all with symbol −1.)

*Reading.* `|Σ_{D*(n)} (m''/n)| ≤ #D*(n)` with equality iff ES fails in this slice; at odd squares equality
holds for the trivial reason (m''/k²) = 1. So the T1-respecting growing-level identity the brief asks for
exists in the form `W = (S − O)/2`, S = #D*(n) a sign-blind (geometric, X₁(t)-visible) count, O a
character sum with the **quadratic character mod n** over the sign-blind set — the level of O is n·t, growing
with n, so STRONG_APPROX Thm 9.1 does not apply. But the positivity statement "O < S" is literally the
H-B spin event of PARITY_FIXED_P Lemma 1.3 (a non-residue among the divisors of a sign-blind family), i.e.
the Legendre-symbol-on-prime-factors problem. The removed trivial m'' = 1 (one per t ≡ 3 (4)) is the
"−2 per level" boundary of O131 Prop 4.1; on D*(n) the bound t ≤ n + 2 is automatic (not a cutoff). Census of
D*(n) (EVIDENCE; R170 repair — the earlier list was for primes p ≡ 17 (24), mislabelled ≡ 1 (24); corrected data
from R170 `scripts/review_gi_census.py doc4`): primes p ≡ 1 (24) in [10⁴, 1.06·10⁴]: (class +1, class −1) =
(19,13), (26,14), (21,11), (29,11), (40,7), (29,14) for p = 10009, 10177, 10273, 10321, 10369, 10513 (for comparison,
the first 8 primes ≡ 17 (24) above 10⁴: (12,11), (26,10), (11,17), (18,19), (25,12), (20,8), (13,16), (21,15));
odd squares 99², 101², 105², 107²:
(33,0), (38,0), (24,0), (26,0). So the sign-blind total S is of the same size at primes and at squares, and
at squares the whole of it sits in class +1. ES is the statement that the genus character at n is not
constant on the sign-blind set — no exact identity tested evaluates O independently of the lottery.

## 5. Construction log (each entry: barrier hypothesis targeted → outcome)

1. **Swap the order of summation (brief idea (a)).** Target: Thm 9.1's "fixed level". Outcome (Lemma 1.2):
   summing over the divisor first gives a count of t in a congruence class modulo the summation variable;
   the fibrations by g and by c give two different growing-level divisor-in-class sums that agree only in
   total. No telescoping: every re-summation of the cubic K⁻(c,g,f) = n is a divisor-in-class count (B2) with
   the level as a summation variable. The character expansion over t (principal + non-principal) gives a main
   term Σ_t τ'(tn+1)/φ(t) of the right size (log²n) with a non-principal remainder of the same size; no exact
   cancellation was found or is suggested by the structure. (Assessment/heuristic — the size claims are not derived
   here; R170 repair: label.)
2. **Kronecker–Hurwitz / Eichler–Selberg (ideas (b), (c)).** Target: fixed level (the trace formula has a
   growing t-range). Outcome (§2): ES = sign-odd part of the split-hyperbolic (cusp fixed point) term (PROVED);
   *Assessment (R170 repair):* typically small (not at genus-0 levels, where A₂ = −A₃); the cusp trace would have
   to be known ≍ kq-fold (not q²-fold) below Deligne at one N; heuristically weight 1 corresponds to O131's finite
   Eisenstein identities (Cohen's formula itself needs k ≥ 2). KH's re-summation mechanism (theta series in the shift
   variable + holomorphic projection into a finite-dimensional space) has no analogue for multiplicative shifts
   gN + 1 (§3).
3. **Main term with genus data at the place p (O167 §11).** Target: n-locality of Thm 9.1. Outcome (§4): the
   genus character at n exists and is *exactly* the sign that separates ES (class −1) from the sign-blind
   geometric count (class ±1); the resulting T1-respecting identity W = (S − O)/2 has level growing with n, but
   O < S is the H-B spin event — the same problem.
4. **Continuants / Hirzebruch–Jung / Dedekind sums.** Target: "congruence-only data" (B1) — HJ data are
   archimedean (sizes of partial quotients), Dedekind sums have exact reciprocity and (Assessment, not derived or
   cited here — R170 repair: label) exact moments over m ≡ 0 (4) involving class numbers h(−p), h(−4p) (genus data
   at p, not quasi-polynomial in p). Outcome: W-certificates with all entries ≥ 2 are the m ≡ 0 (4) with HJ
   length 3 (Lemma 1.1; boundary words with an entry 1 are extra — R170 repair). Dedekind sums determine only the
   *difference* r(n/m) − r(n/(n−m)) of HJ lengths (Riemenschneider duality + Hirzebruch's formula
   12s(m,n) = Σ(a_i − 3) + (m + m*)/n give r − s = (m+m*)/n − 1 − 12 s(m,n)), not the length, and their exact
   moments are (Assessment) of size ≍ √p (class numbers) — a main term a power larger than the certificate count with
   capped multiplicity (B3). (Both formulas checked for all coprime 1 ≤ m < n < 120, `scripts/gi_hj_check.py`; re-checked from scratch
   for n < 90 by R170.)

**Census of the sign-blind total #D*(n) (EVIDENCE; R170 repair — corrected residue class; data from R170
`scripts/review_gi_census.py doc5`; n ≡ 1 (24), 4001 ≤ n ≤ 6000).** Means (class +1, class −1, total; sd of
total): 28 primes (22.8, 7.2, 30.0; 6.6); 50 composites (22.8, 6.2, 29.0; 8.0); 5 odd squares 65², 67², 71², 73²,
77² (29.8, 0, 29.8; 8.7). (The earlier figures 29 primes (16.2, 11.2, 27.4; 4.2), 55 composites (15.2, 9.2, 24.4;
4.9) are for n ≡ 17 (24), not 1 (24); the earlier squares row (25.1, 0, 25.1; 9.4) is for all 8 odd squares
63²…77², which include 63² < 4001 and squares ≡ 9 (24).) Note that at n ≡ 1 (24) the class −1 share is lower
(7.2 of 30.0) than at n ≡ 17 (24) (11.2 of 27.4). The sign-blind total is of the same size at primes and squares (it is governed by local densities that
do not see the difference — cf. O128 Prop 8.3); at squares the class −1 mass reappears in class +1. No exact
conservation law: the totals fluctuate (sd ≈ 4–9), so "S is local" is a heuristic, not an identity.
