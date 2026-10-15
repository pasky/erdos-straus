# R242 — hostile review #1 of O237 (CAP_DOWN.md, branch side-agent/cap-down)

Reviewer: R242. Scope: CAP_DOWN.md §§1–7, memos BRAINSTORM/z13_*.md, report AGENT_REPORT_O237.md.
From-scratch scripts: scripts/review_r242_*.py. Labels as in DISCOVERIES.md. ES is not solved here.

## Summary verdicts

No FATAL or MAJOR defect. Three MINOR defects (wording/literature), listed at the end.

| Claim | Verdict |
|---|---|
| Lemma 1.1 (general Type II window with cap) | SOUND |
| Thm 1.2 (even windows fire) | SOUND |
| Prop 1.3 (one-prime witness, cap ≤ (q−3)/4) | SOUND |
| Cor 2.1 (n₀^{1/4+ε} for n ≡ 1 (8), n₀^{1/2+ε} for n ≡ 5 (8), squares via d = n/p) | SOUND (rel. Pollack IJNT 2014 Thm 1.4; ineffective) — see MINOR-2 (missed effective strengthening) |
| Cor 2.1 Remark 3 (divisor routes) | SOUND |
| Z7-2 (n ≡ 5 (8) barrier), §5/§6 readings | Assessment, correctly labelled |
| Lemma 3.1 (all solutions at fixed x) | SOUND |
| T1 Jacobi proof (§3) | SOUND |
| Prop 4.1(a) (sharpness) / (b) (composite windows, repaired) | SOUND / SOUND |
| Prop 6.1 (order-3 necessary condition) | SOUND (as a necessary condition; reading is Assessment) |
| §1/§5 numerics | REPRODUCED exactly by independent code |

## Per-claim notes

### Lemma 1.1 — SOUND (re-derived)
* 4/n − 1/K = m/(nK) and 1/(nA) + d/(nKA) = (K+d)/(nKA) = m/(nK): identity holds; A ∈ ℤ_{>0} iff d ≡ −K (mod m).
* For s | K: s ∤ m, else s | 4K − m = n, contradicting (i). So v_s(A) = v_s(K+d), and z = nKA/d has
  v_s(z) = b_s + v_s(K+d) − c_s, which is b_s (c_s < b_s), ≥ b_s (c_s = b_s), or 2b_s − c_s (c_s > b_s). Primes outside S
  do not occur in d, so den z = ∏_{c_s > 2b_s} s^{c_s − 2b_s}. Rad condition: c_s > 2b_s ≥ 2 gives v_s(A) = b_s ≥ 1.
* **The 2-adic question raised by the brief.** EXPONENT_CAP Def 1.1 restricts only the primes ℓ with v_ℓ(z) < 0
  (ℓ ∤ 2n, ℓ | y, even, ≥ −2e). A power of 2 in the *shot* d is not restricted by Def 1.1; what matters is
  v₂(z) = b₂ + v₂(K+d) − c₂ ≥ 0, which (ii) c₂ ≤ 2b₂ guarantees. With c₂ = t = b₂ (Thm 1.2) one even has
  v₂(z) ≥ t ≥ 0. So the 2^t factor of d is compatible with Def 1.1: den z is odd. Confirmed numerically by
  scripts/review_r242_thm12.py (independent exact check of Def 1.1 on the produced (x, y, z)).
* The hypothesis gcd(m, n) = 1 is not used (it follows from (i) when s | gcd(m, n) ⇒ s | 4K, harmless).

### Thm 1.2 — SOUND (re-derived)
* gcd(K, qn) = 1: s | K, s | n ⇒ s | q ⇒ q | n; q | K ⇒ q | n. (K/q) = (4K/q) = (n/q) = (q/n) by Jacobi reciprocity
  (n ≡ 1 (4), n > 0). (K′/q) = (2/q)^t (K/q) = −1 under (E).
* F_q^* cyclic of order 2u, u odd: a subgroup containing a non-residue has even order, hence contains −1; −K′ is a
  residue, hence of odd order o, and h = (−K′)^{(o+1)/2} ∈ H with h² = −K′. d = 2^t∏s^{2a_s} ≡ −K (mod q). Lemma 1.1
  with c₂ = t ≤ 2t, odd exponents even. e = max(a_s − b_s)⁺ ≤ (ord_q s − 1) − 1 ≤ q − 3. ✓
* Mod-8 case split ✓ (v₂(n+q) = t + 2). Wording: "exactly … are excluded" is a statement about the *scope of the
  theorem*, not a claim that the excluded windows never fire (they sometimes do, via −2^j ∈ ⟨K′⟩, |j| ≤ t); see
  defect list for the slightly stronger wording in §7 item 1.

### Prop 1.3 — SOUND (re-derived)
* (K′/q) = −1 = ∏(s/q)^{b_s} ⇒ some odd s | K′ with b_s odd and (s/q) = −1. v₂(ord s) = v₂(q−1) = 1, so o/2 odd and
  s^{o/2} = −1. d = K s^{o/2}: c_s = b + o/2 even; overflow (o/2 − b)/2 ≤ ((q−1)/2 − 1)/2 = (q−3)/4. ✓
* "s ≡ −1 (mod q)" gives o = 2, cap 0 ✓. Sharpness: Prop 4.1(a) (below).

### Cor 2.1 — SOUND relative to Pollack (checked against the primary text)
* Source read: Pollack, *Prime splitting in abelian number fields and linear combinations of Dirichlet characters*,
  author's PDF pollack-math.net/generalsplit6.pdf (now copied to sources/pollack_ijnt2014_generalsplit6.pdf); journal
  data IJNT 10 (2014) no. 4, 885–903 confirmed (World Scientific DOI 10.1142/S1793042114500055, Pollack's CV).
  Thm 1.4 verbatim: X a finite group of (primitive, by the paper's convention) Dirichlet characters, conductor f,
  exponent | n; ξ ∈ ℤ[X], ξ(0) = ±1 (coefficient of the trivial character); W := max{W_{ξ⁺}, W_{ξ⁻}}, W_η = ∏ f_χ^{a_χ};
  L ≥ length. Then the least prime q ∤ f with ξ(q) ≠ 0 is ≪_{n,ε,L} W^{1/4} f^ε. Ineffectivity: §3 Prop 3.3 uses
  Siegel's |L(1, χ)| ≫_ε f^{−ε} for real χ (printed p. 10–11); our characters are real, so the constant is ineffective.
  Label "ineffective via Siegel" is correct (Pollack himself calls the resulting n₃(p) bound ineffective, JNT 2018 §1).
* (a) n = n₀m², m odd ⇒ n₀ ≡ n (mod 8); all primes of n ≡ 1 (4) ⇒ n₀ ≡ 1 (4) a fundamental discriminant, χ_{n₀}
  primitive of conductor n₀; χ₋₄χ_{n₀} = χ_{−4n₀} primitive of conductor 4n₀. ξ = 1 − χ₋₄ − χ_{n₀} + χ_{−4n₀}:
  ξ(0) = 1, ξ⁺ = 1 + χ_{−4n₀} (W = 4n₀), ξ⁻ = χ₋₄ + χ_{n₀} (W = 4n₀), f = 4n₀, exponent 2, L = 4. For q ∤ 4n₀,
  ξ(q) = (1 − χ₋₄(q))(1 − χ_{n₀}(q)) ≠ 0 ⟺ q ≡ 3 (4), (n₀/q) = −1 ⟺ (q/n₀) = −1 (n₀ ≡ 1 (4)) ⟺ (q/n) = −1 (q ∤ m,
  as q ≡ 3 (4) cannot divide n). Thm 1.2 with n ≡ 1 (8) has no exclusion ⇒ e*(n) ≤ (q−3)/4 ≪_ε n₀^{1/4+ε}. ✓
* (b) X = ⟨χ₋₄, χ₈, χ_{n₀}⟩ (8 characters, conductors 1, 4, 8, 8, n₀, 4n₀, 8n₀, 8n₀). I expanded
  (1 − χ₋₄)(1 + χ₈)(1 − χ_{n₀}) = 1 + χ₈ − χ₋₄ − χ₋₈ − χ_{n₀} − χ_{8n₀} + χ_{−4n₀} + χ_{−8n₀}: ξ⁺ = 1 + χ₈ + χ_{−4n₀} + χ_{−8n₀},
  W = 8·4n₀·8n₀ = 256n₀²; ξ⁻ = χ₋₄ + χ₋₈ + χ_{n₀} + χ_{8n₀}, W = 4·8·n₀·8n₀ = 256n₀². ✓ Detected set q ≡ 7 (8),
  (q/n₀) = −1 satisfies (E). ✓ Dependence: only on ε (exponent 2, L ≤ 8 fixed). n₀ (not n) is the right parameter. ✓
* Remark 3 (divisor routes): for d | n with rad(n/d) | d, a Thm-1.2 solution for d has K_d prime to d, hence to
  k = n/d; den z (supported on primes of K_d) is unchanged by scaling z ↦ kz, stays prime to n, and rad den z | y | ky. ✓
  n = a², d = a²/p = p(a/p)²: non-square, squarefree part p, d ≡ p (8). ✓ (Also e*(a²) ≤ e*(a) by the same route with
  d = a; the d = a²/p choice is at least as good.)
* Novelty: the analytic input is off-the-shelf — Pollack, *The least prime quadratic nonresidue in a prescribed residue
  class mod 4*, J. Number Theory 187 (2018) 403–414 (pollack-math.net/gica4.pdf, copied to sources/), §1 states
  explicitly n₃(p) ≤ p^{1/4+o(1)} (ineffective) for the least prime nonresidue q ≡ 3 (4) of a prime p. The link
  "ES-type obstructions ↔ least quadratic nonresidue" is folklore (Mordell; Tao's 2011 blog post on Elsholtz–Tao). What
  is new (campaign sense) is Thm 1.2 (all q ≡ 3 (4) with (q/n) = −1 are capped windows when n ≡ 1 (8)) and its
  translation into a cap bound; I found no prior use of Pollack-type bounds for ES caps. See MINOR-2.

### Lemma 3.1 — SOUND
Re-derived: D₁ := my − N > 0 is an integer ≡ −N (mod m); a prime ℓ | D₁, ℓ ∤ N gives v_ℓ(my) = 0 and ℓ ∈ den z with
ℓ ∤ y, so admissible D₁ are supported on primes of N (and 2, with c₂ ≤ 2v₂(x)). Local computation as in Lemma 1.1
(no s | N divides m, by the two gcd hypotheses). scripts/review_r242_misc.py: **20 440 495** pairs (n odd < 80, x < 80,
all D₁ < 4·10⁵) — Lemma 3.1's criterion (and its cap) agrees with a direct Def 1.1 check in every case; the example
n = 5, x = 2, D₁ = 50 (y = 20, z = 4) ✓.

### T1 Jacobi proof (§3) — SOUND
(d/m) = (−K/m) = −(4K/m) = −(a²/m) = −1, while each prime s | d has (s/m) = 1 (odd s: m ≡ −a² (mod s), s ∤ a by (i),
(s/m) = (m/s)(−1)^{(s−1)/2} = 1 since (m−1)/2 odd; s = 2: K even ⇒ m ≡ 7 (8)). Numerically: 12 052 windows (a < 400
odd, m ≤ 300, gcd(K, n) = 1) — none has a Lemma-1.1 divisor at ANY cap. Scope caveat (δ_p ≠ 0 not covered) is stated. ✓

### Prop 4.1 — (a) SOUND, (b) SOUND (after the author's self-review repair)
(a) s^{c−1} ≡ −1, c − 1 ∉ {−1, 0, 1} for q > 3 (ord s = q − 1 > 2), least c = (q+1)/2, even, cap (q−3)/4. Exhaustive
check: 14 238 pairs (q ≤ 139 prime ≡ 3 (4), s < 2·10⁴ primitive root, n = 4s − q): least Lemma-1.1 cap = (q−3)/4 always.
(b) All q_i ≡ 3 (4) by CAP_POINTWISE Thm 1.1′, so o_i/2 odd and s^j = −1 (mod m) ⟺ j odd multiple of L = lcm(o_i/2);
negative j with |j| ≤ b only occur when L ≤ b (cap 0 anyway). Brute force on 600 (n, m, s) composite cases: least
j with s^j ≡ −1 (mod m) equals L (odd) in all. ✓

### Prop 6.1 — SOUND as a necessary condition
9x = ωn + r ⇒ 9ω²x = n + ω²r ≡ n (mod r), so −n/18 ≡ −ω²x/2 and Q³ ≡ −ω²x/2; with Q ∈ ⟨S⟩ and x ∈ ⟨S⟩μ₆ (x prime
to 3) one gets 2 ∈ ⟨S⟩μ₆ (mod r). The "s | a ⟺ s | x" step: gr ≡ n (mod s), r invertible mod s (else s | n), so
s | a ⟺ g ≡ −ω² ⟺ s | n + ω²r = 9ω²x ⟺ s | x (s ∤ 3). ✓ The "dictionary"/"degree-2 accident" reading is Assessment
and labelled so. (No numerics: the statement is a two-line congruence.)

### Numerics (§1, §5) — all reproduced by independent code
* scripts/review_r242_windows.py (own spf sieve, own DP over residues, exact Fraction rebuild + Def 1.1 check of every
  reported solution):
  * primes p ≡ 1 (4) ≤ 10⁶: count 39 175, least cap 0 for all, max least cap-0 window 63 at p = 87 481, max least
    cap ≤ 1 window 51 at p = 496 609. ✓
  * all non-square n ≡ 1 (4) ≤ 10⁶ with all prime factors ≡ 1 (4): count 87 759; cap 0 for all but n = 3985
    (least cap 1, at m = 19; no cap-0 window m ≤ 1000); max least cap-0 window 103 at n = 119 785. ✓
* scripts/review_r242_thm12.py:
  * least-forced-window statistics for the 39 175 primes: p ≡ 1 (8): mean q_old 13.46 → q_new 7.62, max 227 → 131,
    max Prop 1.3 cap 32 (p = 880 993), max exhaustive cap at q_new 16; p ≡ 5 (8): 21.33 → 14.64, max 199 → 191, Prop 1.3
    cap ≤ 47 (p = 636 469), exhaustive ≤ 37; least q ≡ 3 (4) nonresidue excluded for 9161 of 19 623. ✓ (all exact)
  * every (n, q), n ≤ 2·10⁵ relevant non-square (18 633 n), q ≤ 200 prime ≡ 3 (4), (q/n) = −1 (stronger than the
    author's least-window check): 186 979 non-excluded pairs — Thm 1.2 shape (−K′ ∈ H²) holds, Prop 1.3 witness
    rebuilt and Def 1.1-checked with 4e ≤ q − 3 and exhaustive cap ≤ Prop 1.3 cap, in all. Excluded pairs: 37 522,
    of which 36 446 fire at some cap and 1 076 are dead (e.g. (n, q) = (5, 67), (13, 19), (37, 19)).

## Defects

**MINOR-1 (wording overclaims the exclusion).** CAP_DOWN §7 item 1 ("every prime q ≡ 3 (4) with (q/n) = −1 fires,
except (n ≡ 5, q ≡ 3 (8), v₂(n+q) odd)"), BRAINSTORM/z13_even_windows.md ("is a firing window unless …") read as if
excluded windows never fire. They are merely *not forced*: in my scan 36 446 of 37 522 excluded (n, q) pairs (≈ 97 %)
do have a Lemma-1.1 divisor; 1 076 are dead (e.g. n = 5, q = 67: K = 18, K′ = 9). Repair: "is a *forced* window
(fires for every n in the class), except …; the excluded windows are not forced (numerically ≈ 97 % still fire, some
are dead, e.g. (5, 67))".

**MINOR-2 (missed literature; an effective, explicit strengthening is available).** Pollack, J. Number Theory 187
(2018) 403–414, Thm 1 (elementary, genus theory; proof read): for every prime p ≥ 5 there is a prime q ≡ 3 (4) with
(q/p) = −1, and for p ≡ 1 (4) the proof gives q ≤ (p+1)/2. Combined with Thm 1.2 (no exclusion for p ≡ 1 (8)) and
Prop 1.3 this gives, **effectively and explicitly, e*(p) ≤ ((p+1)/2 − 3)/4 = (p−5)/8 for every prime p ≡ 1 (8)**, and by
Remark 3 **e*(a²) ≤ (p−5)/8 for odd a with a prime factor p ≡ 1 (8)** (d = a²/p has squarefree part p and d ≡ 1 (8);
the d-solution uses q | (2-free part of a reduced-form coefficient), so q ∤ d automatically as q ≡ 3 (4)). These
supersede CAP_POINTWISE Thm 1.3(a)/(b) (n^{50308}, rad(n)^5) on those classes. Also the same paper §1 states
n₃(p) ≤ p^{1/4+o(1)} (ineffective, via [IJNT 2014]) — i.e. Cor 2.1(a) for prime n is a one-line consequence of
Thm 1.2 plus a stated literature bound; cite it. Repair: add a Cor 2.2 (PROVED relative to Pollack JNT 2018 Thm 1)
and the citation. (Spark, not checked: genus theory for discriminant −4n₀ should give an effective q ≪ n₀ for
composite n₀ too — one needs a value of a form in the genus χ₋₄ = −1 that is coprime to n₀ and O(n₀).)

**MINOR-3 (inconsistent barrier wording).** AGENT_REPORT_O237 Goal 1 says the n ≡ 5 (8) obstruction needs a 2-dim
Burgess bound "at side n₀^{1/8}"; BRAINSTORM/z13_pollack_quarter.md says "needing side n₀^{1/4}"; CAP_DOWN Z7-2 says
"nontrivial range only at side ≥ n₀^{1/4}". All three are compatible (needed: side n₀^{1/8} for q ≪ n₀^{1/4};
available: side n₀^{1/4}, i.e. q ≪ n₀^{1/2}), but the memo's phrasing inverts it. Repair: "needs side n₀^{1/8};
available bounds are nontrivial only from side n₀^{1/4}".

**Note (not a defect).** Lemma 1.1's hypothesis gcd(m, n) = 1 is implied by (i) (s | m, s | n ⇒ s | 4K); harmless.
