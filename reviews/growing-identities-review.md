# R170 — hostile review of GROWING_IDENTITIES.md (O170, branch side-agent/growing-identities)

Reviewer: R170. Reviewed commit: merged `side-agent/growing-identities` at start of review.
From-scratch scripts: `scripts/review_gi_*.py` (no author code reused).
Status: IN PROGRESS.

## Verdict table
(filled in claim by claim below)

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
