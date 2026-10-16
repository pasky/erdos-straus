# CAP_BOUNDED — a bounded cap for every prime? (task O250)

Status: in progress (O250). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP ((J)34, Def 1.1), CAP_POINTWISE ((J)64), CAP_DOWN ((J)66: Lemma 1.1, Lemma 3.1, Thm 1.2,
Prop 1.3, Prop 4.1), CAP_INTERPOLATION ((J)63), SYNTHESIS_SPARKS7 ((J)78 §2), BRAINSTORM/z12_grh_lattice_gap,
BRAINSTORM/s7_certified_caps. Scripts `scripts/z22_*`, memos `BRAINSTORM/z22_*.md`.
Normalisation: e*(n) as in CAP_POINTWISE (den z = r², r odd, gcd(r, n) = 1, rad r | y, v_ℓ(r) ≤ e); ES(n) ⟺ e*(n) = 0.
Window notation (CAP_DOWN Lemma 3.1): p prime ≡ 1 (4), window m ≡ 3 (4), gcd(m, p) = 1, K = K_m = (p + m)/4 = x,
b_s = v_s(K). A window certificate is an exponent vector δ on the primes of 2pK with
`  ∏_{s | 2pK} s^{δ_s} ≡ −1 (mod m),  δ_s ∈ [−b_s, b_s] (s | 2K),  δ_p ∈ {−1, 0, 1},  or (odd s | K) δ_s ∈ b_s + 2·[1, e]`
(d = D₁ = pK·∏ s^{δ_s}); its cap is max over odd s of (δ_s − b_s)/2 for δ_s > b_s. Lemma 3.1 = all ES^{(y,e)}
solutions with p ∤ x.

Goal (task): (A) e*(p) ≤ C absolute; or (B) cap 0 on an explicit positive-density Chebotarev set by a forced
mechanism; or (C) e*(p) = O(log p) / O(p^ε) unconditionally.

## 0. Iteration log

(Z22-1) *Brief's idea: a smooth K, or a K divisible by all primes ≤ y.* Choose the window so that K ≡ 0 (mod P(y)),
P(y) = ∏_{s ≤ y} s (q ≡ −p (mod 4P(y))). Counting: the cap-C box over the primes ≤ y has (C+3)^{π(y)} elements, the
group has q ≥ P(y) ≈ e^y elements, so covering needs C ≳ y — independent of p! Barrier hit: the box is then a FIXED
finite set of rationals a/b (independent of p), and "−1 ∈ box mod q" ⟺ q | a + b: a fixed finite set of q, hence a
congruence covering of p mod 4P(y) (B1), which T1 kills at p ≡ 1 (mod 4P(y)): there every s ≤ y is ≡ ±1 … more
precisely q ≡ −1 (mod s) and (s/q) = +1, so no box element is −1. Hypothesis satisfied: "bounded support" (the
certificate uses only primes from a set fixed in advance). → The support must grow with p; §1 makes this a theorem
(conditional, any cap) for bounded windows.
(Z22-2) *Uniform (self-generated) elements.* Use only elements polynomial in K, p, 2 (exponents δ_s = j·b_s on all
odd s | K). Classification (§2): at cap 0 they give only the classical windows m | p + 4, m | (p+1)/2, m | p + 2,
m | 2p + 1; at cap e ≥ 1 the only new relation is K^o ≡ −1, i.e. m | p^o + 4^o (o odd), with cap ≤ b_max(o − 1)/2.
This decouples the cap from the window SIZE (q can be ≈ p^o). Barrier hit: p^o + 4^o ≡ 1 (mod 4) for every p, and at
p = a² it is a sum of two coprime squares — the existence of a prime factor ≡ 3 (mod 4) is a Landau-type event, never
congruence-forced (T1/B5).

## 1. Bounded windows are dead at every cap (conditional), via a Jacobi transfer

**Lemma 1.1 (Jacobi transfer; PROVED, elementary).** Let p ≡ 1 (mod 4) be prime, m ≡ 3 (mod 4) positive with p ∤ m,
K = (p + m)/4. Then (Jacobi symbols mod m):
(a) (s/m) = (s/p) for every odd prime s | K; (b) (2/m) = (2/p) if K is even; (c) (p/m) = (m/p); (d) (−1/m) = −1.
*Proof.* s | K and s | m would give s | 4K − m = p; so s ∤ m, and s ≠ p (else p | m). (a) Reciprocity for coprime odd
positive s, m with (m−1)/2 odd: (s/m) = (−1)^{(s−1)/2}(m/s) = (−m/s); 4K = p + m gives −m ≡ p (mod s), so (s/m) =
(p/s) = (s/p). (b) 8 | p + m, so m ≡ −p (mod 8), and (2/·) is even under x ↦ −x mod 8. (c) Jacobi reciprocity,
p ≡ 1 (4). (d) m ≡ 3 (4). ∎
**Corollary 1.2 (parity law; PROVED).** Every window certificate satisfies
`  ∏_{s | 2K} (s/p)^{δ_s} · (m/p)^{δ_p} = −1`
(take Jacobi symbols mod m of ∏ s^{δ_s} ≡ −1). So it puts an odd total exponent on {primes of 2K that are
non-residues mod p} ∪ {p, if (m/p) = −1}. (At δ_p = 0 this is CAP_POINTWISE's forcing read backwards, and at odd
squares it is CAP_DOWN §3's T1 argument.)

**Theorem 1.3 (bounded windows fail at every cap, infinitely often; CONDITIONAL on Dickson's prime k-tuples
conjecture).** For every M ≥ 3 there are infinitely many primes p ≡ 1 (mod 8) for which no window m ≤ M carries a
certificate at any cap (e = ∞ included). Equivalently, every ES^{(y)} solution of 4/p with p ∤ x has x > (p + M)/4.
*Proof.* Let Λ := lcm(1, …, M + 1) and L := 16·Λ·∏_{ℓ ≤ M+1} ℓ, so v_ℓ(L) ≥ v_ℓ(m + 1) + 1 for every prime ℓ ≤ M + 1
and v₂(L) ≥ v₂(m + 1) + 2, for every m ≤ M. For each window m ≤ M, m ≡ 3 (4), put L_m := L/(m + 1) and consider the
linear forms f(t) = Lt + 1 and f_m(t) = L_m t + 1. They are distinct and the family is admissible: for ℓ ≤ M + 1 every
form is ≡ 1 (mod ℓ) (ℓ | L_m); for ℓ > M + 1 the ≤ M/4 + 1 < ℓ forms have at most one root each. Dickson gives
infinitely many t with p := f(t) and all R_m := f_m(t) prime. Fix such t. Then p ≡ 1 (mod 8) and p + m = (m + 1)R_m,
so K_m = ((m + 1)/4)·R_m, R_m > M + 1 is prime, and gcd(m, p) = 1 (p ≡ 1 (mod m)), K_m < p. Symbols mod p of all
generators: every prime ℓ ≤ M + 1 has (ℓ/p) = 1 (p ≡ 1 (mod 8ℓ)); this covers 2, the primes of (m + 1)/4, and the
primes of m, so (m/p) = 1. For R_m: R_m ≡ 1 (mod 4) and R_m ≡ 1 (mod m) (all primes of m divide L_m), and
p = (m + 1)(R_m − 1) + 1 ≡ −m (mod R_m), so (R_m/p) = (p/R_m) = (−m/R_m) = (m/R_m) = (R_m/m) = 1. Hence the left side
of Corollary 1.2 is +1 for every exponent vector: no certificate exists at window m, at any cap. The windows of
ES^{(y)} solutions with p ∤ x are exactly m = 4x − p (CAP_DOWN Lemma 3.1; x > p/4 always). ∎
*Remarks.* (1) Scope: Lemma 3.1's full family (δ_p ≠ 0 included); Type I (p | x) is not covered. CAP_INTERPOLATION
Prop 4.1 (Linnik) and redteam-automorphic-2 Thm 2.2(iii) are the cap-limited / cap-0 analogues for covering
arguments; the point here is "every cap, e = ∞ included, and every exponent vector": for these p the window
picture is literally that of n = 1 (K_m ≡ (m + 1)/4 on all small primes, R_m ≡ 1 (mod m)). (2) Unconditionally the
same computation shows: if p ≡ 1 (mod L), a certificate at window m ≤ M must put an odd exponent on a prime factor of
the rough part R_m := K_m/((m+1)/4) that is a non-residue mod p. (3) Consequence for goal (A): a proof of e*(p) ≤ C
must, for some p, use windows m → ∞ together with non-residue primes from the rough part of K_m — at a single prime
window the worst case over K is exactly the forced level (q − 3)/4 (CAP_DOWN Prop 4.1(a)). That is the B2 lottery.
*Check (`scripts/z22_dickson_check.py M TMAX N`, exhaustive cap ≤ λ(m) + 2 per window, δ_p included):* M = 11:
p = 807 330 585 601, 1 482 496 646 401, 2 412 770 976 001 (all R_m prime): 3/3 windows dead each (least forced
window 19, 23, 31). M = 19: p = 4 714 845 095 999 745 907 201, 11 787 094 675 874 034 316 801: 5/5 windows dead
(least forced window 47). Control (`z22_dickson_control.py 11 300`): among 300 primes p = Lt + 1 with some R_m
composite, 284 have a live window ≤ 11 — the rough parts are what carries the certificates.

## 2. Uniform (self-generated) certificates: classification and the odd-order witness

Write K = 2^t K′ (K′ odd). Call a certificate **uniform** if δ_s = j·b_s for every odd s | K (one integer j),
δ₂ = a (|a| ≤ t), δ_p = ε ∈ {−1, 0, 1}. Admissible j: j ∈ {−1, 0, 1} (cap 0), j ≥ 3 odd (cap (j − 1)·max b_s/2, since
jb_s ≡ b_s (mod 2)), j ≥ 2 even only if K′ is a perfect square. These are exactly the certificates that use nothing
about K beyond K itself, 2^t and p ("self-generated" in the strongest sense; every forced argument so far — CAP_POINTWISE
Thm 1.1's −K = h², h a power of K — is of this kind up to reduction of exponents).

**Proposition 2.1 (classification; PROVED, elementary).** Mod m, p ≡ 4K = 2^{t+2}K′, so a uniform vector has value
2^a K′^j p^ε ≡ 2^w p^J with w := a − j(t + 2), J := j + ε. Hence a uniform certificate exists at m iff m divides the
integer N := numerator of 2^w p^J + 1 (cleared of powers of 2 and p; (w, J) and (−w, −J) give the same N up to
units). The possibilities are:
(a) cap 0, K odd (t = a = 0): N = p + 4 ((j, ε) = (±1, 0)) or p + 1 ((0, ±1)); the others give p² + 4 or 5, which have
no divisor ≡ 3 (mod 4).
(b) cap 0, K even: N ∈ {2^c p + 1 (0 ≤ c ≤ t), p + 2^c (1 ≤ c ≤ 2t + 2), p² + 2^c (c odd ≤ 2t + 2), 2^c + 1}.
(c) cap ≥ 1, K odd: N = p^j + 4^j (j odd ≥ 3, ε = 0); ε = ±1 gives p^{j±1} + 4^j, a sum of two coprime squares, with
no divisor ≡ 3 (mod 4). If K is a square also N = p^{j±1} + 4^j, j even.
(d) cap ≥ 1, K even: N = p^J + 2^c with J = j + ε ∈ {j − 1, j, j + 1} and c = −w ≥ 2j ≥ 6.
*Proof.* Substitution K′ ≡ p·2^{−(t+2)} and the bounds |a| ≤ t: for j ≥ 1, w ∈ [−t − j(t+2), t − j(t+2)] ⊂ (−∞, −2j];
for j = 0, w = a. Sums of two coprime squares have only prime factors ≡ 1 (4) (and 2), while m ≡ 3 (mod 4). ∎
**Corollary 2.2 (no uniform certificate is congruence-forced at p ≡ 1 (8); PROVED).** For p ≡ 1 (mod 8) every N in
(a)–(d) that depends on p is ≡ 1 (mod 4), except 2p + 1 and p + 2 (≡ 3 (mod 8)) and p + 1 ((p + 1)/2 ≡ 1 (4)). For
N ≡ 1 (4) a divisor m ≡ 3 (4) exists iff N has a prime factor ≡ 3 (mod 4) — a Landau-type event, not determined by any
congruence on p. For 2p + 1 and p + 2 the relation needs t ≥ 1, i.e. m ≡ −p ≡ 7 (mod 8), while N ≡ 3 (mod 8):
again not forced (it needs a prime factor ≡ 7 (8) or a pair 3·5 (8)). ∎
So the self-generated level, which forces −1 ∈ ⟨S⟩ (the subgroup), forces no bounded-exponent *uniform*
representation; the forced cap of CAP_POINTWISE/CAP_DOWN comes from reducing exponents modulo orders, which is where
q (not o) enters.

**Proposition 2.3 (odd-order witness: the cap does not depend on the window size; PROVED).** Let q ≡ 3 (mod 4) be a
prime with q ∤ p, q ≡ 4 − p (mod 8) (K_q odd) and (q/p) = −1. Let o be the odd part of ord_q(p/4) (equivalently the
least odd o with q | p^o + 4^o; it exists iff (q/p) = −1). Then the window q carries the uniform certificate
δ_s = o·b_s (j = o), and **e*(p) ≤ (o − 1)/2 · max_{s | K_q} v_s(K_q).** In particular e*(p) ≤ max_s v_s(K_q) whenever
q | p² − 4p + 16 = (p − 2)² + 12 (o = 3), and e*(p) = 0 if q | p + 4 (o = 1, the classical window).
*Proof.* K ≡ p/4 (mod q), (K/q) = (p/q) = −1 and the 2-part of F_q^* is {±1}, so ord_q(K) = 2o with o odd and
K^o ≡ −1, i.e. ∏ s^{o b_s} ≡ −1: a uniform certificate with j = o, admissible (o odd), of cap (o − 1)b_s/2 at s. ∎
*Reading.* Prop 1.3 of CAP_DOWN bounds the cap by the order of one non-residue prime s | K (≤ (q − 3)/4); Prop 2.3
bounds it by the odd order of the single element p/4, which is small exactly for the prime factors of p^o + 4^o
with o small — windows that can be as large as p^o. A bounded cap for every p would follow from: **(U) for every
prime p ≡ 1 (8) some p^o + 4^o, o ≤ O₀ odd, has a prime factor q ≡ 3 (mod 8) with K_q of bounded multiplicity.**
(U) is a simultaneous Landau-type statement; heuristically each fixed o fails with probability ≍ (o log p)^{−1/2}, so
(U) with a fixed O₀ should fail for infinitely many p (the failure density ∏_o (o log p)^{−1/2} is not summable over p
for any fixed O₀). Assessment: Prop 2.3 is a second explicit witness (useful numerically, §5), not a route to (A).

## 3. Goal (C) outside explicit thin sets: the forced cap plus Linnik's large sieve

Let q₃(p) := least prime q ≡ 3 (mod 4) with (q/p) = −1, and 𝒫(y) := {p ≡ 1 (mod 8) prime : (q/p) = +1 for every
prime q ≡ 3 (4), q ≤ y} (an explicit Chebotarev-defined set).

**Lemma 3.1 (PROVED; CAP_DOWN Thm 1.2 + Prop 1.3).** For every prime p: e*(p) = 0 if p ≢ 1 (mod 8) (p ≡ 3 (4) and
p ≡ 5 (8) are classical), and e*(p) ≤ (q₃(p) − 3)/4 if p ≡ 1 (8). Hence {p : e*(p) > C} ⊆ 𝒫(4C + 3). Moreover
𝒫(y) ∩ [1, y] = ∅, since q₃(p) ≤ (p + 1)/2 (Pollack, JNT 187 (2018) Thm 1; CAP_DOWN Cor 2.2).

**Theorem 3.2 (PROVED relative to Montgomery's arithmetic large sieve and the prime number theorem for primes
≡ 3 (mod 4)).** Let 𝒜(N, y) := {n ≤ N : every prime factor of n is ≡ 3 (mod 4) and ≤ y}. For Q ≥ 2:
`  #(𝒫(y) ∩ [1, Q]) ≤ (N + Q²)/|𝒜(N, y)|     for every N ≥ 1.`
Consequently:
(a) for A > 1: #{p ≤ X : e*(p) > (log X)^A/4} ≤ X^{2/A + o(1)} — a power saving for every A > 2;
(b) for ε > 0: #{p ≤ X : e*(p) > p^ε} ≪_ε (log X)^{⌈4/ε⌉} — a polylogarithmic exceptional set.
*Proof.* For p ∈ 𝒫(y) with p > y, every n ∈ 𝒜(N, y) is a product of quadratic residues mod p and p ∤ n, so 𝒜
avoids the (p + 1)/2 classes {0} ∪ {non-residues} mod p; with ω(p) = (p+1)/2, ω/(p − ω) > 1, and the large sieve
|𝒜| ≤ (N + Q²)/Σ_{r ≤ Q} μ²(r)∏_{ℓ|r} ω(ℓ)/(ℓ − ω(ℓ)) (only r prime kept) gives the display; p ≤ y is excluded by
Lemma 3.1. (a) y = (log X)^A, N = X², k := π(y; 4, 3) ≥ y/(3 log y) (large y), r := ⌊log N/log y⌋: products of r
distinct primes from {q ≡ 3 (4), q ≤ y} lie in 𝒜, so |𝒜| ≥ (k/r)^r ≥ ((log N)^{A−1}/(3·2^A))^{r} = N^{1 − 1/A − o(1)}.
With Lemma 3.1 (e*(p) > (log X)^A/4 ⇒ q₃(p) > (log X)^A): the count is ≤ 2X²/N^{1−1/A−o(1)} = X^{2/A+o(1)}.
(b) y = X^{ε/2}, N = X², r := ⌈4/ε⌉: products of r distinct primes ≡ 3 (4) from (N^{1/r}/2, N^{1/r}] (≤ y) give
|𝒜| ≫_ε N/(log N)^r, so #{p ≤ X : q₃(p) > X^{ε/2}} ≪_ε (log X)^r. A prime p ∈ (X^{1/2}, X] with e*(p) > p^ε has
q₃(p) > X^{ε/2}; summing over X, X^{1/2}, X^{1/4}, … gives (b). ∎
*Remarks.* (1) Linnik's large-sieve theorem for the least non-residue (≪_ε 1 exceptions to n₂(p) ≤ X^ε) is the model;
the restriction to q ≡ 3 (mod 4) costs the polylog (𝒜 has density only ≍ (log N)^{−1/2} even without smoothness;
a sharper lower bound for |𝒜| would improve (b)). (2) Pointwise the unconditional record stays p^{1/4+ε}
(ineffective, CAP_DOWN Cor 2.1) and (p − 5)/8 (effective); under GRH (log p)^{2+ε}. Theorem 3.2 says the GRH-quality
bound holds unconditionally outside X^{1+o(1)}·X^{−(1 − 2/A)} primes, and p^ε outside a polylog set. (3) Compared with
CAP_INTERPOLATION Remark 3.2(b) (reviewer sketch: power saving for e ≥ (log N)^{1+ε} via the class large sieve), (a)
is weaker in range (A > 2) but complete, and its exceptional set is explicit and Chebotarev-defined (𝒫(4e + 3)).
(4) Bounded C: 𝒫(4C + 3) has positive relative density 2^{−π(4C+3; 4, 3)} among p ≡ 1 (8), so the forced level never
gives "bounded cap outside a thin set"; by Thm 1.3 nor does any bounded-window method (conditionally), and by
CAP_DOWN Prop 4.1(a) the worst case at a single window is exactly (q − 3)/4.

## 4. Many generators: what a bounded or logarithmic cap would need (Assessment, with one exact step)

**Lemma 4.1 (character-sum form of the box count; PROVED, standard).** At a prime window q with generator set S and
exponent sets D_s (as in the header), the number of certificates is
`  #{δ ∈ ∏ D_s : ∏ s^{δ_s} ≡ −1} = (1/(q−1)) Σ_χ χ(−1) ∏_{s∈S} Σ_{δ∈D_s} χ(s)^δ.`
The trivial and the quadratic character together give |Box|/(q−1)·(1 + (−1)^{ν}·∏_{s NR}(1 − 2ω_s)), ω_s := share of
odd exponents in D_s, ν := #{s ∈ S non-residue mod q}; for the cap-C box at b_s = 1, ω_s = (C + 2)/(C + 3) and this is
the parity law of Cor 1.2 in averaged form. ∎
*Reading.* A cap ≤ C at q follows deterministically as soon as the non-quadratic characters cancel, i.e. no
χ ≠ 1, χ² ≠ 1 has χ(s) close to 1 for most s ∈ S: |∏_s Σ_δ χ(s)^δ| ≤ ∏_s min(|D_s|, 2/‖θ_s‖) with χ(s) = e(θ_s).
For K divisible by all primes ≤ y (window q ≡ −p (mod 4P(y)), q ≍ P(y)^{O(1)}), |Box| = (C + 3)^{π(y)} exceeds q once
C ≳ y^{O(1)} = (log q)^{O(1)}, and the needed cancellation is a **Diophantine genericity of the discrete logs of the
primes ≤ y modulo q − 1** (no k ≠ 0 with ‖k·ind(s)/(q−1)‖ ≲ 1/C for all s ≤ y). That is precisely the "balanced
exponent lattice" input isolated in BRAINSTORM/z12_grh_lattice_gap; GRH controls Frobenius classes in fixed Kummer
fields (bounded-index quotients F_q^*/(F_q^*)^ℓ), never the archimedean size of discrete logs, and for a fixed small
generator set the good q are prime factors of explicit integers (iteration Z22-1). So (C) with O(log p)^{O(1)} — let
alone (A) — needs an input of a new kind; the forced level (one character, CAP_POINTWISE) is all that reciprocity
supplies. (Assessment.)
