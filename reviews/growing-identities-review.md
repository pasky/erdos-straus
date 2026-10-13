# R170 — hostile review of GROWING_IDENTITIES.md (O170, branch side-agent/growing-identities)

Reviewer: R170. Reviewed commit: merged `side-agent/growing-identities` at start of review.
From-scratch scripts: `scripts/review_gi_*.py` (no author code reused).
Status: round 1 complete.

## Verdict table
| Claim | Verdict |
|---|---|
| Lemma 1.1 (continuant/HJ form; W-certificates ↔ 4 \| m, r(n/m) = 3) | SOUND-AFTER-REPAIRS (m1: qualifier "entries ≥ 2" must not be dropped) |
| Lemma 1.2 (two fibrations; swap) | SOUND (m2 wording) |
| Lemma 1.3 / Prop 4.1 ((m''/n) = ε) | SOUND (proof re-derived; brute force 0 failures) |
| Identity W = Σ_{D(n)}(1−(m''/n))/2, "W = (S−O)/2" | SOUND-AFTER-REPAIRS (M1: D(n) infinite; use D*(n)) |
| Consistency with DEDEKIND_ES Thm 4.5 | CONSISTENT (no discrepancy) |
| Trace-formula transcription / gi_trace.py | SOUND (5 independent test families incl. non-trivial χ, n > 1) |
| Prop 2.1 | SOUND-AFTER-REPAIRS (m4: sign/normalisation) |
| Prop 2.2 | GAP (M2: "q²-fold" should be ≍ kq; "smallest term" unproved/false at genus-0 levels; label) |
| §3 KH discussion | SOUND as Assessment (m7 label; m3/m8 details) |
| §4 census, §5 EVIDENCE | GAP (M3: data are for n ≡ 17 (24), labelled ≡ 1 (24)) |
| Overall "no positive identity; ES not solved" | SOUND (no overclaim of ES) |

### Lemma 1.1 (continuant / HJ form) — SOUND-AFTER-REPAIRS (wording only)
Re-derived by hand: `S_cS_g = [[cg−1, −c],[g, −1]]`, `S_cS_gS_f = [[cgf−c−f, −(cg−1)],[gf−1, −g]]` ✓;
`c − 1/(g − 1/f) = (cgf−c−f)/(gf−1)` ✓; det = 1 ⇒ (m,n) = 1; c ≥ 2 ⇒ m = gf−1 < n; uniqueness of HJ
expansions (entries ≥ 2) gives injectivity in both directions ✓. `S_aS_1S_b = S_{a−1}S_{b−1}` ✓ (both equal
`[[ab−a−b, −(a−1)],[b−1, −1]]`). `K⁻(a,4cd,b) = 4abcd−a−b` ✓.
From scratch (`scripts/review_gi_identities.py 300`): brute-force enumeration of the cubic vs. the set
{m ∈ [1,n): 4|m, (m,n)=1, r(n/m) = 3} for all n ≤ 300 — identical as sets of words (entries ≥ 2), 0 failures.
The restriction "entries ≥ 2" is essential: for n ≡ 1 (4), n ≤ 300, the W-certificates at
**n = 5, 17, 41, 65, 209, 241, 265 all have an entry 1** and there is no HJ-length-3 m ≡ 0 (4) at all (this
matches DEDEKIND_ES §4.2–4.3, where 17, 241, … are "solved by the boundary case"). See defect m1.

### Lemma 1.2 (fibration swap) — SOUND
Both fibrations re-derived (`f(cg−1) = n+c`; `(cg−1)(fg−1) = gn+1`) and checked by brute force: R(n) and W(n)
from the cubic agree with the g-fibred and the c-fibred sums (with the stated mod-4 conditions) for all n ≤ 300,
0 failures. The "sum over m first" form re-derived: for 4 | m, (m,n) = 1, r_m := −n⁻¹ mod m ∈ [1,m), the t's
are t = r_m (if r_m | m+1) and t = m+1 (iff r_m = 1, i.e. n ≡ −1 (m)); so exactly
`W(n) = #{4|m, (m,n)=1 : r_m | m+1} + #{4|m : m | n+1}`; the second ("boundary") term is 0 for n ≡ 1 (4).
Checked for all n ≤ 120, 0 failures. (The bound "∈ {0,1,2}" ✓.) See m2 for the vague "(+ boundary)".

### Lemma 1.3 and Proposition 4.1 (sign = Jacobi symbol at n) — SOUND (statement); identity form SOUND-AFTER-REPAIRS
Re-derived independently: for odd prime ℓ | u, tn ≡ −1 (ℓ) ⇒ (n/ℓ) = (−t/ℓ); n ≡ 1 (4) ⇒ (u/n) = (n/u);
t ≡ 3 (4) ⇒ (−t/u) = (−1)^{ε(u)}(t/u) = (u/t); u ≡ ε·2^{−j} (t) ⇒ (u/t) = (ε/t)(2/t)^j = ε(2/t)^j; hence
(m''/n) = ε·(2/(tn))^j, and j ≥ 1 with 4 | m gives 8 | tn+1, (2/(tn)) = 1. All coprimality conditions needed for
the Jacobi symbols hold since u | tn+1. t ≡ 3 (4) is forced by 4 | tn+1, n ≡ 1 (4) ✓. Hypothesis "4 | m" is used
only to get 8 | tn+1 when j ≥ 1. ✓
From scratch: all n ≡ 1 (4) ≤ 300 with **all** t ≡ 3 (4) up to 3n+12 (both classes), and n ∈ [10⁶, 10⁶+1600),
t < 400 (54 081 pairs, sympy divisors): 0 failures.
Consistency with DEDEKIND_ES Thm 4.5 (O169): with t = g, A = m = gf−1, m'' = cg−1 one has A·m'' = gn+1 ≡ 1 (n),
so (m''/n) = (A/n); Prop 4.1 (ε = −1) is exactly the "4 | tu−1 ⇒ (A/n) = −1" direction of Thm 4.5 (with
O169's letters n/A = [[v,t,u]] ↔ O170's [[c,g,f]]). **No discrepancy.** O170 does not claim the converse
direction of Thm 4.5 (on L₃, (A/n) = −1 ⇒ one of five slices), nor does it need it.
The identity `W = Σ_{D(n)}(1 − (m''/n))/2` is correct (only finitely many non-zero terms), but D(n) is infinite,
so "S = #D(n)", "W = (S − O)/2" and "|Σ_{D(n)}(m''/n)| ≤ #D(n) with equality iff ES fails" are ill-defined as
written. See defect M1 (repair is easy and makes the truncation t ≤ n+2 automatic).

### Trace-formula transcription (§2 "Input") — SOUND (implementation); text summary slightly lossy
I could not access Cohen–Strömberg (not in sources/); I implemented Cohen's formula from scratch for (n,N) = 1,
k ≥ 2 (`scripts/review_gi_trace.py`: A1 with χ(√n)ψ(N)(k−1)/12; A2 with h_w and
μ(t,f,n) = ψ(N)/ψ(N/N_f)·Σ_{x mod N, x²−tx+n ≡ 0 (N_f N)} χ(x); A3 with the condition
(τ,N/τ) | gcd(N/𝔣_χ, n/d − d); A4 for k = 2, χ = 1) and validated it against **independent** references:
(a) dim S_k(Γ₀(N)) = classical dimension formula (μ, ν₂, ν₃, cusps) for k ∈ {2,4,6}, N ≤ 40 — 0 failures;
(b) Σ_{χ even} dim S₂(q,χ) = genus X₁(q) (formula 1 + q²/24∏(1−p⁻²) − ¼Σφ(d)φ(q/d)), q ≤ 25 — 0 failures;
(c) Tr T_n | S₂(Γ₀(11)) = coefficients of η(z)²η(11z)², 14 values of n ≤ 31 — 0 failures;
(d) **non-trivial character, n > 1:** Tr T_n | S₃(Γ₀(7), (·/7)) = coefficients of η(z)³η(7z)³ for 14 values
n ≤ 29 incl. squares 1, 4, 9, 25 (tests A1 with χ(√n)) — 0 failures;
(e) Tr T_p | S₁₂(1) = τ(p), p ≤ 11 — 0 failures.
The author's `gi_trace.py` implements the same formula (read line by line: A1–A4, μ, the τ-condition, A4 —
identical to mine). Note the author's own tests never exercise a non-trivial χ with n > 1 (only dimensions);
my test (d) closes that gap. Also dim S₃(Γ₁(q)) = 0 for q ≤ 6 and = 1 at q = 7 ✓ (used in Prop 2.2).
The prose transcription of A₂ omits the N_f·q modulus and the ψ(q)/ψ(q/N_f) factor in μ (m3).

### Proposition 2.1 — SOUND-AFTER-REPAIRS (normalisation/sign)
Re-derived: for N ≡ 1 (q) the τ = q, τ = 1 summands have y ≡ d resp. d' (mod q), (τ,q/τ) = 1, so contribute
χ(d) + χ(d') = χ(d) + χ̄(d) ✓; orthogonality Σ_{χ(−1)=ε} χ(d) = (φ(q)/2)([d≡1] + ε[d≡−1]) for q ≥ 3 ✓.
Including A3's prefactor −½ the exact value is
`Σ_{χ(−1)=(−1)^k} χ̄(−1)·(τ∈{1,q} part of A3) = −(φ(q)/2)·Σ_{dd'=N} min(d,d')^{k−1}([d≡−1] + (−1)^k[d≡1])`.
Checked numerically (`scripts/review_gi_prop21.py`, q ∈ {12,20,24}, k ∈ {2,3}, 20 cases, N = qn+1): exact
agreement. The document's displayed expression lacks the sign −1 (the "−½ … ×2") — m4. The weight χ̄(−1) is a
constant ((−1)^k) on the summed family, so it does not "isolate" anything; it only fixes a global sign (m4).
The qualitative content (classes ±1 always appear together, relative sign (−1)^k, weight min^{k−1}) is correct.
Hidden point worth stating: with weight min(d,d')^{k−1} the trivial divisor d = 1 has weight 1, while an ES
divisor d ≡ −1 (q) has weight ≥ (q−1)^{k−1}; so for k ≥ 3 the "−2 per level" boundary is negligible inside A3.
The "geometric reading" (cusps of X₁(q) fixed by T_N; P vs −P) is interpretation, not proved — label it (m5).

### Proposition 2.2 — GAP (label overclaimed; headline factor "q²-fold" wrong by ≍ φ(q))
What is actually proved is only the trivial bound: the ES-relevant part of A3 is ≤ (φ(q)/2)·Σ_{d|N} min^{k−1}
≤ (φ(q)/2)·τ(N)N^{(k−1)/2}, and Deligne gives |Tr T_N | S_k(Γ₁(q))| ≤ dim S_k(Γ₁(q))·τ(N)N^{(k−1)/2}.
(i) **"q²-fold" is off by a factor ≍ φ(q).** By Prop 2.1 the character-summed identity carries the factor
φ(q)/2 on the ES side, so the cancellation below Deligne needed to see one unit of the ES class is
dim S_k(Γ₁(q))/(φ(q)/2) ≍ (k−1)q·∏_{p|q}(1+1/p)/12 (equivalently: per character, dim S_k(q,χ) ≍ kq/12 against
an A3 of size ≤ 2τ(N)N^{(k−1)/2}). Concretely dim S₃(Γ₁(20)) = 14 vs φ(20)/2 = 4 (ratio 3.5, not q² = 400);
dim S₃(Γ₁(24)) = 20 vs 4. The qualitative conclusion (cancellation growing linearly with the level is needed)
survives; the stated exponent does not. → M2.
(ii) **"The ES term is the smallest term" is not proved and is false in general.** Whenever S_k(Γ₁(q)) = 0
(k = 3, q = 4; k = 2, q ∈ {4,8,12}) and N is not a square, the identity reads A2 = −A3 (k = 3) resp.
A2 + A4 = −A3 (k = 2) exactly, e.g. q = 4, k = 3, N = 4421: (A1,A2,A3,A4) = (0, 2, −2, 0). In my 20 sample cases
(`review_gi_prop21.py`) A3 is the smallest of A2, A3, A4, but |Tr| < |A3| happens (q = 20, k = 2, N = 4821:
|Tr| = 12, |A3| = 20). "Smallest" is a typical-size heuristic → Assessment.
(iii) "There is no independent way to evaluate the cusp trace at a single N" is an Assessment, not a theorem.
(iv) "At weight 1 the elliptic term vanishes formally": Cohen's formula (as transcribed) is valid only for k ≥ 2;
there is no Eichler–Selberg formula computing traces on S₁ (dim S₁ is not given by any such closed formula), so
setting k = 1 in it proves nothing. The weight-1 sentence is Assessment (m6).
Repair: split Prop 2.2 into "Lemma (PROVED): trivial bounds above" + "Assessment: …", replace q² by
dim S_k(Γ₁(q))/(φ(q)/2) ≍ kq, delete "smallest" or qualify it ("typically; equality |A2| = |A3| at genus-0
levels"). Same fix in the Summary bullet and in AGENT_REPORT item 3.

### §3 Kronecker–Hurwitz discussion — SOUND as Assessment, but not labelled as such in the document
From scratch (`scripts/review_gi_kh.py`): Σ_{t²≤4N} H(4N−t²) = 2σ(N) − Σ_{d|N} min(d,N/d) (H(0) = −1/12) for all
N < 400 ✓. The mechanism description (ℋθ, holomorphic projection to M₂(Γ₀(4)), shadow correction) is the
standard Zagier/Mertens picture; Mertens 2014 not in sources/ — not checked against the paper. Inaccuracies:
Σ_t H(4N−t²) is the **4N-th** (not N-th) coefficient of ℋ(τ)θ(τ); λ(N) and σ(gN+1; −1, g) are undefined
(the document's own notation is τ_{−1,g}). The "no finite-dimensional target ⇒ no re-summation" inference is a
heuristic, not a proof (§3 has no label; the Summary places it inside a "PROVED relative to Cohen" bullet) — m7.
The O167 Lemma 10.1 paraphrase is lossy: O167's set has γ₂₁ = cp and γ₁₂ = M (or, second normalisation,
γ₂₁ = p, γ₁₂ = cM, congruences mod M) **plus the non-congruence condition c | M/4**; the doc's
"{γ₂₁ = n, γ₁₁ ≡ γ₂₂ ≡ −1 (mod γ₁₂)}" drops both c and 4 | M (m8).

### §0 controls — SOUND
W(k²) = 0 is in fact PROVED by Prop 4.1 for every odd k. T2(k²) = 0 for all odd k ≤ 45 re-checked from scratch
(`scripts/review_gi_t2.py`; sanity T2(5,7,13,17,73) = 2,3,2,4,6 > 0).

### §4 census and §5 EVIDENCE — GAP (mislabelled residue class; numbers reproduce for the wrong class)
`scripts/review_gi_census.py` (from scratch; independent W(n) cross-check: class −1 count = W(n) at
10009, 10177, 10273, 9801 ✓; no non-trivial pair with n+2 < t ≤ 3n+2 ✓).
* §4 says "primes p ≡ 1 (24) in [10⁴, 1.06·10⁴]: (12,11), (26,10), …". The author's `gi_sign_census.py` takes
  `range(10001, 12000, 24)`, i.e. **p ≡ 17 (mod 24)**. I reproduce all 8 pairs exactly for p = 10169, 10193,
  10289, 10313, 10337, 10433, 10457, 10529 (all ≡ 17 (24); the last two exceed 1.06·10⁴ too). The actual
  primes p ≡ 1 (24) in [10⁴, 1.06·10⁴] are 10009, 10177, 10273, 10321, 10369, 10513 with (class +1, class −1) =
  (19,13), (26,14), (21,11), (29,11), (40,7), (29,14). The square data (33,0), (38,0), (24,0), (26,0) reproduce.
* §5 says "n ≡ 1 (24), 4001 ≤ n ≤ 6000 … 29 primes (16.2, 11.2, 27.4; 4.2); 55 composites (15.2, 9.2, 24.4; 4.9);
  8 odd squares 63²…77² (25.1, 0, 25.1; 9.4)". I reproduce the prime/composite rows exactly **for n ≡ 17 (24)**.
  For n ≡ 1 (24) the true figures are: 28 primes (22.8, 7.2, 30.0; sd 6.6), 50 composites (22.8, 6.2, 29.0; 8.0),
  5 squares 65², 67², 71², 73², 77² (29.8, 0, 29.8; 8.7). The squares row of the doc reproduces for the 8 odd
  squares 63²…77², but these are not ≡ 1 (24) (63², 69², 75² ≡ 9 (24)), 63² = 3969 < 4001, and no odd square
  is ≡ 17 (24): the doc compares primes ≡ 17 (24) with squares from other classes.
* The qualitative conclusion (sign-blind total of the same size at primes and squares) survives with the
  correct class (30.0 vs 29.8); but at p ≡ 1 (24) — the class the brief is about — the class −1 share is
  markedly lower (mean 7.2 of 30.0) than in the doc's (wrong-class) data (11.2 of 27.4). → M3.

## Numbered defects

No FATAL defects.

**M1 (MAJOR) — §4 Prop 4.1 "Consequently…" and *Reading*; Summary bullet 1; AGENT_REPORT item 2.** D(n) is
infinite (m'' = 1 ∈ D(n) for every t ≡ 3 (4)), so S = #D(n) = ∞ and "W = (S − O)/2", "|Σ_{D(n)}(m''/n)| ≤ #D(n)
with equality iff ES fails" are meaningless as written. *Repair:* define D*(n) := D(n) \ {m'' = 1}. Lemma (easy,
add it): every (t, m'') ∈ D*(n) has t ≤ n + 2. Proof: m·m'' ≡ 1 (t) so m ≡ m'' ≡ ε (t); 4 | m ⇒ m ≠ 1 ⇒ m ≥ t − 1;
m'' ≠ 1 ⇒ m'' ≥ t − 1; so (t−1)² ≤ tn + 1, t ≤ n + 2. Hence D*(n) is finite, W(n) = (S* − O*)/2 with
S* = #D*(n), O* = Σ_{D*(n)}(m''/n), and the "truncation t ≤ n + 2" of the census is automatic, not a cutoff.
(Checked: no non-trivial pair with t > n+2 for all n ≤ 300 up to t ≤ 3n+12, and sampled n ≈ 10⁴ up to 3n+2.)

**M2 (MAJOR) — Prop 2.2, Summary bullet 2, construction-log item 2, AGENT_REPORT item 3.** (i) The required
cancellation is dim S_k(Γ₁(q))/(φ(q)/2) ≍ kq (per character: dim S_k(q,χ) ≍ kq/12), not "q²-fold"; e.g.
dim S₃(Γ₁(24)) = 20 vs φ(24)/2 = 4. (ii) "ES term is the smallest term" is not proved and fails at the
genus-0 levels the Prop itself mentions (A2 = −A3 exactly when S_k(Γ₁(q)) = 0, N non-square). (iii) The weight-1
sentence uses Cohen's formula outside its range k ≥ 2. *Repair:* PROVED part = the two trivial bounds; everything
else → Assessment; replace q² by kq (or by the exact ratio).

**M3 (MAJOR) — §4 census paragraph and §5 census paragraph.** The data are for n ≡ 17 (mod 24) (author's
`range(10001, 12000, 24)` and evidently the same in the /tmp driver), labelled "≡ 1 (24)"; the square rows use
odd squares ≡ 1 or 9 (24) incl. 63² outside [4001, 6000]. *Repair:* replace by the correct-class figures above
(or relabel as ≡ 17 (24) and compare with a class-matched control), commit the /tmp driver as a script.

**m1 (MINOR) — Lemma 1.1 vs Summary/AGENT_REPORT item 1.** "W-certificates ↔ m ≡ 0 (4) with n/m of HJ length 3"
holds only for certificates with all entries ≥ 2. Boundary certificates (an entry = 1) exist and are the only
ones at n = 5, 17, 41, 65, 209, 241, 265 (n ≤ 300, n ≡ 1 (4)). *Repair:* keep "(entries ≥ 2)" in every
restatement and add: "boundary words (an entry 1) ⟺ DEDEKIND_ES §4.2".

**m2 (MINOR) — Lemma 1.2, "(+ boundary)".** State it exactly: W(n) = #{4|m, (m,n)=1 : r_m | m+1} + #{4|m : m | n+1},
r_m := −n⁻¹ mod m ∈ [1, m); second term = 0 for n ≡ 1 (4). (Checked n ≤ 120.)

**m3 (MINOR) — §2 Input.** The prose A₂ omits the modulus N_f·q and the factor ψ(q)/ψ(q/N_f) in μ; A₃'s "…" hides
the condition (τ, q/τ) | gcd(q/𝔣_χ, d − d'). The code is right; write the formula out fully (it is the object
all of §2 rests on).

**m4 (MINOR) — Prop 2.1 display.** Value is −(φ(q)/2)·Σ_{dd'=N} min^{k−1}([d≡−1] + (−1)^k[d≡1]) (sign −1 from
A3's −½ × 2). Say that the weight χ̄(−1) is the constant (−1)^k on the family.

**m5 (MINOR) — Prop 2.1 "geometric reading".** Interpretation (cusps fixed by T_N, P ↔ −P, odd-weight line
bundles) inside a PROVED item; mark as Assessment.

**m6 (MINOR) — Prop 2.2 weight 1.** See M2(iii).

**m7 (MINOR) — §3 heading / Summary bullet 2.** Label §3 "Assessment"; fix "N-th" → "4N-th coefficient of ℋθ";
define λ(N) = Σ_{d|N} min(d, N/d); replace σ(gN+1; −1, g) by τ_{−1,g}(gN+1).

**m8 (MINOR) — §3 O167 Lemma 10.1 paraphrase.** Restore γ₂₁ = cp (or γ₁₂ = cM in the 2nd normalisation) and the
condition c | M/4.

**m9 (MINOR) — Lemma 1.3 *Reading*.** "This is PARITY_FIXED_P Lemma 1.3 in slice a = 1": O165 Lemma 1.3 is about
primes ℓ | p + 4a²d (Type II) / p² + 4c²d with the character χ_{−4d}; Prop 4.1 uses the same reciprocity
mechanism on a different family (tn + 1). Say "analogue of", not "is".

**m10 (MINOR) — §5 items 1 and 4.** "Main term Σ_t τ'(tn+1)/φ(t) of size log²n with non-principal remainder of the
same size" and "exact moments … involving h(−p), h(−4p) … of size ≍ √p" are unlabelled and unsupported here
(no derivation, no script, no citation). Label CONJECTURE/Assessment or cite (O169?). The two HJ formulas in
item 4 (12s(m,n) = Σ(a_i−3) + (m+m*)/n and r − s = (m+m*)/n − 1 − 12s(m,n)) are correct: re-checked from scratch
for all coprime m < n < 90 (`review_gi_identities.py`).

## Overall
The mathematics that carries the document (Lemmas 1.1–1.3, Prop 4.1, the Prop 2.1 orthogonality computation,
the trace-formula code) is correct and independently verified. The defects are a well-definedness slip in the
headline identity (M1, easy repair), an overstated/mislabelled barrier proposition (M2), and EVIDENCE computed
for the wrong residue class (M3). None affects the honest bottom line (no positive identity; ES not solved).
