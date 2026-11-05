# Z59_CONVO — tryhard lane CONVO (wave z59): pointwise solvability of 4abcd = a + b + pc for primes p ≡ 1 (mod 24)

Status: **NOT PROVED.** No hot lead. What follows: proved reformulations and a proved local/character
analysis ("ρ-ratio criterion") that isolates exactly what a pointwise proof must supply, numerical evidence, and
the falsifier audit. Hostile line-by-line review (deep subagent) applied: 0 fatal, 4 major + 3 minor fixed.
Fresh attack: no FRONTIER / Z5*_* memo / lane file was read; only `data/z58/screens/`.

Notation. p ≡ 1 (mod 24) prime throughout unless stated; χ_p(·) = (·/p) Legendre. "Solution" = (a,b,c,d) ∈ ℕ⁴
with 4abcd = a + b + pc. For ρ ≡ 3 (mod 4): N_ρ := (p + ρ)/4 ∈ ℕ (since p ≡ 1 mod 4).

## §0 Mandatory falsifiers (stated at first commit; re-audited in §9)

* (F1) odd squares n = m²: no solution exists. Any proof step must fail for n = m². In this memo the only
  "existence" inputs are of the form "−1 lies in the ratio set of divisors of N_ρ modulo ρ" (§3); for n = m² with
  (m, ρ) = 1 all prime factors ℓ of (m² + ρ)/4 satisfy λ_ρ(ℓ) = 1 (Lemma 3.3(i)), which confines that ratio set to the kernel of a quadratic character
  that is −1 at −1 (Lemma 3.3). So the step that must use non-squareness is "some prime factor of N_ρ escapes
  that kernel AND the escaping residues combine to −1"; §4–§5 show the first half is free for NR ρ while the
  second half is exactly what is not provable by any tool found here.
* (F2) d-even half. Two different predicates must be kept apart: (a) the *full* d-even family (any c, d even),
  and (b) the screen's C-even (★) sub-line = c = 1 AND d even (numerator-8 line, `r8_zeros_1e10.txt`). For (a):
  d never enters the ρ-ratio criterion except through d = N_ρ/(ab); forcing d even means
  requiring 2·ab | N_ρ i.e. ab | N_ρ/2 — only possible when 8 | p + ρ, i.e. ρ ≡ 7 (mod 8). So every "d even"
  statement here is the same criterion restricted to ρ ≡ 7 (mod 8) with N_ρ replaced by N_ρ/2; any argument
  that only needs ρ = 3 (or ρ ≡ 3 mod 8) is dead on the d-even half. (The brief's 22 d-even zeros ≤ 10⁹ are over
  all odd primes; my 15 are the p ≡ 1 (4) ones — consistent, see §6.) For (b) see §9.
* (F3) 4545 = 3²·5·101 (non-square, no solution): its relevant quadratic character (·/4545) has conductor 505,
  so any argument that uses only "χ_n is a non-trivial quadratic character" (reciprocity) and no further
  arithmetic of n is refuted by 4545. §4 shows the forcing lemma here is purely a residue statement (no
  reciprocity needed), so it cannot by itself distinguish p from 4545.
* (F4) zeros of single lines: c = 1 line ⇔ ρ = a + b exactly (Lemma 1.2); a = 1 line ⇔ N_ρ has a divisor
  ≡ −1 (mod ρ). Both fail at specific primes ≤ 10¹⁰ (14 and 3 of them); an argument working with one fixed ρ,
  or with a = 1 only, or with ρ = a + b only, is false there. §6 checks all of them against the criterion.

## §1 Reformulations (PROVED)

**Lemma 1.1.** Let n ≥ 1. (a,b,c,d) ∈ ℕ⁴ solves 4abcd = a + b + nc iff ρ := 4abd − n satisfies ρ ≥ 1 and
ρc = a + b. Hence n is solvable iff ∃ a,b ≥ 1 and a divisor ρ of a + b with 4ab | n + ρ (then d = (n+ρ)/(4ab),
c = (a+b)/ρ). Equivalently, iff ∃ ρ ≥ 1, and a, b with ab | (n+ρ)/4 and ρ | a + b.

*Proof.* 4abcd − nc = a + b ⇔ c(4abd − n) = a + b; since a + b > 0 and c > 0, 4abd − n = ρ ≥ 1 and ρc = a+b.
Conversely given ρ | a + b, 4ab | n + ρ put d, c as stated; 4abcd = c(n + ρ) = nc + a + b. ∎

For n ≡ 1 (mod 4) prime and 4 | n + ρ we need ρ ≡ 3 (mod 4).

**Lemma 1.2 (lines).** c = 1 ⇔ ρ = a + b. a = 1 ⇔ ∃ ρ: N_ρ has a divisor k ≡ −1 (mod ρ) (take b = k).
d even ⇔ 8ab | p + ρ.

**Lemma 1.3 (other equivalent forms).** For n = p: (i) f := 4acd − 1 divides pc + a with cofactor b;
(ii) f divides p + 4a²d with cofactor ρ (since 4ad(pc + a) − pf = p + 4a²d and 4ad·b − p = ρ):
p + 4a²d = fρ; (iii) solvable ⇔ ∃ a, c ≥ 1: pc + a has a divisor ≡ −1 (mod 4ac).
*Proof.* (i) is the equation solved for b. (ii): 4ad(pc + a) = 4ad·b·f ⇒ p + 4a²d = 4ad·b·f − p(4acd − 1) =
f(4abd − p) = fρ. (iii) is (i) read with f = 4acd − 1 ranging over divisors ≡ −1 (mod 4ac). ∎

## §2 Character necessary condition (PROVED; CERTIFIED numerically)

**Lemma 2.1.** p prime ≡ 1 (mod 8). For every solution: f = 4acd − 1 ≡ a·b⁻¹ (mod p) and χ_p(ab) = −1.

*Proof.* f·b = 4abcd − b = pc + a ≡ a (mod p). Also a, b < p: from 4abd = p + ρ ≤ p + a + b, if b ≥ p then
4ab ≤ a + 2b, i.e. a(4b − 1) ≤ 2b, forcing a < 1; symmetrically for a. For every prime ℓ | f:
(2c)²·(−dp) ≡ 1 (mod ℓ) [as f | 4c²dp + 1, since (4cda−1)(4cdb−1) = 4c²dp + 1], so the Jacobi symbol
(−dp/f) = 1. With d = 2^e d', d' odd, f ≡ −1 (mod 4d) gives (−1/f) = −1, (2/f) = 1 if e ≥ 1 (f ≡ 7 mod 8),
(d'/f) = (f/d')(−1)^{(d'−1)/2} = (−1/d')(−1/d') = 1. So (−d/f) = −1 and (p/f) = −1. By reciprocity
(p ≡ 1 mod 4) (f/p) = −1, and (f/p) = χ_p(a b⁻¹) = χ_p(ab). ∎

Check: `scripts/z59_convo_check_lemmas.py` — all solutions with ab ≤ 3000 for all primes p ≡ 1 (24) < 20000
satisfy f ≡ a/b and χ_p(ab) = −1; Lemma 1.1 enumeration agrees with a direct divisor search of 4c²dp + 1 (c,d ≤ 6,
p < 3000); no solution for m² (m ≤ 149 odd, ab ≤ 2000). Output `bad 0`.

Consequence: every solution has ab divisible by a prime q' with χ_p(q') = −1, so ab ≥ q(p) := least quadratic
non-residue of p. (For n = m² the same computation gives (m²/f) = 1 ≠ −1: this is the square obstruction.)

## §3 The ρ-ratio criterion and its convolution (character) expansion (PROVED)

**Criterion 3.1.** p is solvable ⇔ ∃ ρ ≡ 3 (mod 4), 3 ≤ ρ ≤ (p+4)/3, such that −1 lies in the *ratio set*
R_ρ(N_ρ) := { a·b⁻¹ mod ρ : ab | N_ρ } ⊂ (ℤ/ρ)^*. (Lemma 1.1. Every solution datum has ρ ≤ a + b ≤ ab + 1 ≤
(p+ρ)/4 + 1, i.e. ρ ≤ (p+4)/3 < p; for such ρ, gcd(N_ρ, ρ) = 1, since an (odd) prime ℓ | (ρ, N_ρ) divides p + ρ,
hence p, impossible as ℓ ≤ ρ < p. So all divisors of N_ρ are units mod ρ and R_ρ is well defined.)
Since N_{ρ+4} = N_ρ + 1, with M := (p+3)/4 the criterion reads: **∃ j ≥ 0 such that the integer M + j has
divisors a, b with ab | M + j and a + b ≡ 0 (mod 4j + 3).** (ρ = 4j + 3.) The prime p enters only through M.

**Identity 3.2 (convolution form).** For ρ with (N_ρ, ρ) = 1, writing τ_ψ(N) := Σ_{abd = N} ψ(a)ψ̄(b),
  W_ρ := #{(a,b) : ab | N_ρ, ρ | a + b} = φ(ρ)⁻¹ Σ_{ψ mod ρ} ψ(−1) τ_ψ(N_ρ),
(orthogonality applied to 1[a ≡ −b]). τ_ψ is multiplicative: τ_ψ(ℓ^e) = Σ_{i+j ≤ e} ψ(ℓ)^{i−j}.

**Lemma 3.3 (square cancellation = (F1) mechanism).** Let ρ ≡ 3 (mod 4), λ = (·/ρ) (Jacobi). For every prime
ℓ ∤ 2ρ dividing n + ρ: λ(ℓ) = (−ρ/ℓ) = (n/ℓ) [first equality: Jacobi reciprocity, ρ ≡ 3 mod 4; second: −ρ ≡ n
mod ℓ]. For ℓ = 2 | N_ρ with n ≡ 1 (mod 8): 8 | n + ρ forces ρ ≡ 7 (mod 8), so λ(2) = (2/ρ) = 1 = (n/2)_Kronecker.
Hence (i) n = m² with m odd and gcd(m, ρ) = 1: then gcd(N_ρ, ρ) = 1 and λ(ℓ) = 1 for every prime ℓ | N_ρ
(ℓ ∤ m, as ℓ | m, ℓ | m² + ρ ⇒ ℓ | ρ), so τ_λ(N_ρ) = τ_{ψ₀}(N_ρ) and the ψ₀ and λ terms of 3.2 cancel exactly;
more strongly every ratio a/b lies in ker λ ∌ −1 (λ(−1) = −1), so W_ρ = 0 (the square obstruction, visible as a
spectral cancellation). [If gcd(m, ρ) > 1, Identity 3.2 does not apply as stated; the non-existence of solutions
for n = m² in all cases follows instead from the Jacobi computation in Lemma 2.1, which does not use primality:
(−dn/f) = 1 and (−d/f) = −1 force (m²/f) = −1, impossible.]
(ii) n = p: τ_{ψ₀} − τ_λ = 2#{(a,b,d): abd = N_ρ, λ(ab) = −1} ≥ 0, and it is > 0 iff N_ρ has a prime factor ℓ
with λ(ℓ) = −1, which is forced when λ(N_ρ) = (p/ρ) = −1 (as λ is multiplicative and N_ρ ≡ p/4 mod ρ).
*Proof.* Direct. ∎

**Corollary 3.4 (ρ = 3 exactly).** (ℤ/3)^* has only ψ₀, λ, so W_3 = ½ Σ_{abd=N_3}(1 − λ(ab)): ρ = 3 works iff
N_3 = (p+3)/4 has a prime factor ≡ 2 (mod 3). (For p ≡ 1 mod 24, λ(N_3) = +1 so this needs ≥ 2 such factors
with multiplicity; it happens for 55% of p ≡ 1 (24) ≤ 3·10⁶ — `scripts/z59_convo_rho.c`.) Also for every ρ:
ρ | p + 4 ⇒ ρ works (a = N_ρ, b = 1, since N_ρ ≡ −1 mod ρ).

**What is left (the honest core).** For ρ > 3 the characters of order > 2 (and, for composite ρ, the other
quadratic characters) are not controlled by anything about p except the single product relation
Π_{ℓ|N_ρ} ψ(ℓ)^{e_ℓ} = ψ(p/4). The criterion therefore needs, for some ρ, the residues mod ρ of the *individual*
prime factors of N_ρ. Residue conditions on p do sometimes supply a hit (e.g. p ≡ 73 (mod 168) gives 7 | p + 4,
hence ρ = 7 works with (a,b,c,d) = ((p+7)/4, 1, (p+11)/28, 1)), but no *finite* family of fixed pairs, nor any
S-supported ab, can cover all primes p ≡ 1 (24) (Lemmas 5.1–5.2); and the only prime-specific input found
(reciprocity, §4) controls one quadratic character per ρ and nothing more.

## §4 The only prime-specific input found, and why it is not enough (PROVED + CERTIFIED examples)

**Lemma 4.1 (global colouring).** Let p ≡ 1 (mod 4) be prime. For every ρ ≡ 3 (mod 4) and every prime ℓ ∤ 2ρp
dividing N_ρ: λ_ρ(ℓ) = (p/ℓ) = χ_p(ℓ). *Proof.* Lemma 3.3 gives λ_ρ(ℓ) = (p/ℓ); quadratic reciprocity with
p ≡ 1 (mod 4) gives (p/ℓ) = (ℓ/p). ∎
So across *all* ρ the quadratic "colour" of a prime factor of N_ρ is one fixed function of ℓ, the Legendre
symbol mod p. This is where primality enters: for n = m² the colouring is identically +1 (⇒ no solutions,
Lemma 3.3(i)); for p prime it is a non-trivial character of conductor p.

**Escape lemma 4.2.** If (p/ρ) = −1 then N_ρ has an odd number (with multiplicity) of prime factors ℓ with
χ_p(ℓ) = −1. *Proof.* λ_ρ(N_ρ) = λ_ρ(p)λ_ρ(4)⁻¹ = (p/ρ) = −1 and λ_ρ is completely multiplicative; apply 4.1. ∎
(Note the proof of 4.2 uses only N_ρ ≡ p/4 (mod ρ) — it is a residue statement; reciprocity only re-labels.)

**Why this cannot close the argument — (F3) is a counterexample to "escape ⇒ solution".** The odd non-square
n = 4545 = 3²·5·101 has the same structure with the Jacobi colouring (·/4545) (conductor 505), and for every
ρ ≡ 3 (4), ρ < 60, prime to n with (4545/ρ) = −1 the escape happens yet ρ fails (`data/z59/convo/escape_examples.txt`):
ρ = 11: N = 17·67 (residues 6, 1 mod 11; ratio set {1, 6, 2} ∌ 10); ρ = 23: N = 2·571; ρ = 43: 31·37; ρ = 47:
2²·7·41; ρ = 59: N = 1151 prime. 4545 has no solution at all. The same failure pattern occurs at primes:
p = 8 803 369 (≡ 1 mod 24; record of §6) has (p/ρ) = +1 for every ρ ≡ 3 (4), ρ ≤ 39, and the NR values
ρ = 43, 59, 67, 83, 103 all escape (N_ρ = 379·5807, 3·733619, 719·3061, 3·7·104803, 2²·29·18973) and all fail;
the first working ρ is 107 (N = 3²·11²·43·47). So an argument must control *which* residues mod ρ the escaping
prime factors have, not just their quadratic colour — i.e. information about the factorisation of the specific
integers (p+ρ)/4 beyond any character of bounded order.

## §5 CRT-design barrier (PROVED) — why residue information alone is useless

**Lemma 5.1.** Let L ≥ 1 and n ≡ 1 (mod 4L) (n any positive integer). Then no solution datum (a, b, ρ) of
n (Lemma 1.1) has ab | L.
*Proof.* 4ab | 4L | n − 1 and 4ab | n + ρ give 4ab | ρ + 1, so ρ ≥ 4ab − 1. But ρ | a + b gives ρ ≤ a + b,
and 4ab − 1 > a + b for all a, b ≥ 1 ((4a − 1)(4b − 1) ≥ 9 > 5). ∎
Primes p ≡ 1 (mod 4L) exist for every L (Dirichlet), and p ≡ 1 (mod 24) is compatible. Hence no finite family of
fixed pairs (a, b) suffices (take L = lcm of the products ab in the family).

**Lemma 5.2 (finite prime support).** Let S be a finite set of primes and p ≡ 1 (mod 8·Π_{q∈S, q odd} q) prime.
Then every solution has ab divisible by a prime outside S. *Proof.* Each q ∈ S is a residue mod p ((2/p) = 1 as
p ≡ 1 mod 8; (q/p) = (p/q) = 1 for odd q). If ab were S-supported then (ab/p) = 1, contradicting Lemma 2.1. ∎
These two lemmas are the classical Mordell-type barrier for families with fixed (a, b), resp. S-supported ab.
They do *not* by themselves exclude identity families in which a, b, c, d depend polynomially on p (those
are not fixed-(a,b) families); I make no claim about such families beyond what Lemma 5.2 implies. They do not exclude all
congruence-based arguments (single classes can force hits, e.g. p ≡ 73 mod 168 via 7 | p + 4). What this lane
actually established is narrower: the methods tried in §7 fail, the one-character escape implication is false
(§4), and bounded ρ is conditionally insufficient (Thm 7.7). Heuristic remark only: inputs about the factorisations
of (p+ρ)/4 for ρ ≤ R(p) are statements about integers in a short interval, which for squares are rigidly constrained
(norms from ℚ(√−ρ)); I found no pointwise tool that constrains them for primes.

## §6 Numerics (CERTIFIED = exhaustive exact-integer computation by the named script; EVIDENCE = trend)

* Minimal working ρ over all primes p ≡ 1 (24), p ≤ 10⁸ (719 781 primes; `scripts/z59_convo_rho2.c` mode 0,
  output `data/z59/convo/minrho_1e8.txt`): every p has a working ρ ≤ 107 (CERTIFIED for p ≤ 10⁸). Records:
  73→7, 1129→11, 1201→23, 21169→31, 67369→35, 87481→63, 1430641→71, 8803369→107. Distribution of min ρ: ρ = 3 for
  59.8%, ρ = 7 for 32.7%, ρ ∈ {11, 15} for 5.9%, ρ ∈ (16, 32] for 1.5%, ρ ∈ (32, 64]: 585 primes, ρ ∈ (64, 128]: 10 primes. (EVIDENCE: min ρ grows
  very slowly, far below log²p; no pointwise bound is proved.)
* Least non-residue route (`scripts/z59_convo_nr.c`, `data/z59/convo/nr_small.txt`, p ≤ 2·10⁵): when the least
  prime non-residue q of p is 5 or 7 a solution with q | ab and ab ≤ 42 always exists (Mordell's classes); for
  q ≥ 11 the least ab with q | ab, where it exists within the search limit ab ≤ 2·10⁶, reaches 49 170 (p = 186 841;
  observed finite maximum, EVIDENCE only). In 30 cases (`min_ab_qdiv=0` in the data file) no solution with q | ab
  was found below the limit; e.g. p = 2521 (q = 11) provably has none: all its solutions (ab ≤ (p+1)/3 = 840)
  are (a,b,c,d) = (2,29,1,11), (2,159,7,2), (4,161,3,1) up to a ↔ b. In fact all 30 absences are complete
  (CERTIFIED): every solution has ab ≤ (p+1)/3 < 66 667 for p ≤ 2·10⁵, far below the search limit 2·10⁶. So the
  least non-residue need not divide ab (Lemma 2.1 only forces *some* non-residue prime factor); the least-q
  restriction is not universal. No unboundedness claim is made.
* d-even half (`scripts/z59_convo_rho2.c` mode 3 = all primes p ≡ 1 (4), ρ ≡ −p (8), N_ρ/2): primes ≤ 3·10⁶
  with no d-even solution: 5 17 53 101 113 241 1061 1129 1249 2081 3169 3221 3361 5281 35569 (15 primes; the
  p ≡ 1 (24) ones: 241 1129 1249 3169 3361 5281 35569). The brief's 22 d-even zeros ≤ 10⁹ (last 35 569)
  are over **all odd primes**: a direct check over all odd primes < 40 000 (ρ ≥ 1 any residue, 8ab | p + ρ, ρ | a+b)
  gives exactly 22 = my 15 plus 3, 11, 19, 131, 491, 739, 2531 (all ≡ 3 mod 4). Consistent; RECONCILED
  (cross-model review; reproduced here).
* Falsifier primes (mode 2, full criterion): c = 1 zeros 409, 577, 5569, 9601, 23929, 83449, 102001, 329617,
  712321, 1134241, 1724209, 1726201, 5212561, 8813281 have min ρ = 7, 3, 7, 19, 7, 11, 7, 3, 23, 3, 7, 23, 11, 3
  (so solutions exist with ρ < a + b, i.e. c ≥ 2); a = 1 zeros 193, 2521, 66529 have min ρ = 7, 23, 31 (so the
  witnesses have a, b ≥ 2: N_ρ has no divisor ≡ −1 (mod ρ) for any ρ, but has a ratio ≡ −1).

## §7 Constructions tried for the pointwise statement (all failed as attempted; these are records of failed attempts, not impossibility theorems for the methods named)

1. *Least non-residue identities* (fix q with (p/q) = −1, look for identity families with q | ab): §6 shows the
   least-q restriction is not universal (p = 2521 has no solution with 11 | ab), and separately Lemma 5.1 rules
   out any universal finite menu of fixed pairs. (No unboundedness of the q-divisible minimum is claimed.) Failed.
2. *Escape + group combinatorics in (ℤ/ρ)^** (§3–4): escape is free when (p/ρ) = −1, but hitting −1 needs
   residues of individual prime factors; with N_ρ = (two primes) every ρ can fail (examples §4). Dead without
   factorisation control of (p+ρ)/4.
3. *Norm-form / Pell representations of p* (p = u² − 2v² has infinitely many representations): with d = 2,
   a = v/2 one gets p + 4a²d = u², and the criterion becomes "u² has a divisor ≡ −p (mod 4v)". The cofactor
   ρ = u²/f ≤ (p + 2v²)/(4v − 1) ≈ v/2 + p/(4v) must be ≡ −p (mod 4v), hence ≥ 4v − p once v > p/4; the two are
   incompatible for v ≳ 2p/7: only the finitely many representations with v ≲ p can work, so the infinite unit orbit gives nothing. Same for p = x² + ky² (finite).
4. *Vieta jumping*: in the d = 1 slice (4bc − 1)ρ = 4b² + p is quadratic in b only, and the involution is
   b ↦ cρ − b, i.e. a ↔ b. The equation is linear in each of a, b, c, d separately; no non-trivial involution,
   no descent.
5. *Highly composite N_ρ by position*: among N_ρ = M + j (consecutive integers) some j ≤ K has K | M + j, but
   then ρ = 4j + 3 is as large as ~4K while divisors of K give ≤ Π_{ℓ^e ∥ K}(2e + 1) ratios; for p ≡ 1 (mod 4K) this is
   exactly Lemma 5.1. Dead.
6. *Short-interval divisor sums*: Σ_{ρ ≤ R} W_ρ has main term from ψ₀ − λ (positive, Lemma 3.3(ii)), but the
   non-quadratic characters in Identity 3.2 are a sum over ρ ≤ R of divisor sums of N_ρ twisted by characters
   mod ρ; bounding it pointwise in p is a level-of-distribution statement for the single short interval
   [p/4, (p+R)/4] — not available (and it must fail for p = m², where the same sum cancels the main term
   exactly). Dead with present technology.

### 7.7 A conditional no-go for bounded ρ (CONDITIONAL on Schinzel's Hypothesis H; construction CERTIFIED)

**Theorem 7.7.** Let R ≥ 3, F := {ρ ≤ R : ρ ≡ 3 (mod 4)}, Q := lcm(24, ρ(ρ+1) : ρ ∈ F). For t ≥ 1 put
p = Qt + 1 and P_ρ := 1 + (Q/(ρ+1))·t (ρ ∈ F). If p and all P_ρ are prime, then p ≡ 1 (mod 24) and **no ρ ∈ F
works** in Criterion 3.1, i.e. every solution of 4abcd = a + b + pc has 4abd − p > R. Under Hypothesis H
there are infinitely many such t; hence (conditionally) for every R there are infinitely many primes p ≡ 1 (24)
with no witness ρ ≤ R (min ρ > R, with min ∅ := ∞): no uniform bound on the witnessing ρ can suffice, and any
pointwise proof must use ρ (equivalently 4abd − p) growing with p.

*Priority.* This is an independent rederivation of an exact prior result: `DISPROOF_AVENUES.md` §3,
Proposition 3.1 (Type II e-slice row) uses the same N = (p+e)/4, e(e+1) | Q, prime P ≡ 1 mod e and
2 ≤ x + y ≤ (e+5)/4 < e, conditionally on Dickson's conjecture (which already suffices here; only linear forms
occur). The freezing mechanism goes back to `B1_LINE.md` Thm 4.2. No priority is claimed.

*Proof.* 24 | Q gives p ≡ 1 (24). Since ρ + 1 | Q, N_ρ = (Qt + 1 + ρ)/4 = s_ρ·P_ρ with s_ρ := (ρ+1)/4 ∈ ℕ.
Since ρ | Q/(ρ+1) (ρ(ρ+1) | Q), P_ρ ≡ 1 (mod ρ). P_ρ > s_ρ for t ≥ 1 (as Q/(ρ+1) ≥ ρ ≥ s_ρ), so P_ρ ∤ s_ρ and
the divisors of N_ρ are x and xP_ρ with x | s_ρ. If ab | N_ρ then (a, b) = (xP^i, yP^j) with xy | s_ρ,
i + j ≤ 1, and a + b ≡ x + y (mod ρ). But 2 ≤ x + y ≤ s_ρ + 1 = (ρ + 5)/4 < ρ, so ρ ∤ a + b.
Admissibility for H: the |F| + 1 forms Qt + 1 and P_ρ(t) are distinct, linear (hence irreducible) with positive
leading coefficients, and all equal 1 at t = 0; so for every prime ℓ the residue t ≡ 0 (mod ℓ) makes their product
≢ 0 (mod ℓ): there is no fixed prime divisor. ∎
Numerical confirmation (`scripts/z59_convo_schinzel.py`): R = 7: t = 16, 110, 176, 390, 396 give p = 2689,
18481, 29569, 65521, 66529 with min ρ = 15, 19, 11, 11, 31 (> 7); R = 15: p = 2402401, 9609601, 12307681,
12603361 with min ρ 23, 23, 19, 19; R = 23: p = 1621531850401, 4062963310561 with min ρ 31, 31. (66529 is one of
the three a = 1 zeros.)

## §8 Summary of claims

| claim | status |
|---|---|
| Lemma 1.1–1.3 reformulations (ρ-form, p + 4a²d = fρ, pc + a has divisor ≡ −1 mod 4ac) | PROVED (+ checked) |
| Lemma 2.1: every solution has f ≡ a/b (mod p) and (ab/p) = −1 | PROVED (+ checked, p < 2·10⁴) |
| Criterion 3.1 (ratio set of divisors of N_ρ mod ρ contains −1); consecutive-integer form | PROVED |
| Identity 3.2 (character expansion), Lemma 3.3 (square cancellation; ψ₀ − λ ≥ 0 for primes) | PROVED |
| Cor 3.4 (ρ = 3 works iff (p+3)/4 has a prime factor ≡ 2 mod 3; ρ \| p + 4 ⇒ ρ works) | PROVED |
| Lemma 4.1 (global colouring λ_ρ(ℓ) = (ℓ/p)), Lemma 4.2 (escape) | PROVED |
| "escape ⇒ solution" is false (4545; and failing NR ρ at primes, e.g. 8 803 369) | CERTIFIED |
| Lemma 5.1 (no solution with ab \| L when n ≡ 1 mod 4L); Lemma 5.2 (ab not S-supported when p ≡ 1 mod 8·ΠS) | PROVED |
| min ρ ≤ 107 for all primes p ≡ 1 (24), p ≤ 10⁸ | CERTIFIED (computation) |
| Thm 7.7: under Hypothesis H (Dickson suffices), no uniform bound on witnessing ρ | CONDITIONAL; prior (DISPROOF_AVENUES §3 Prop 3.1) |
| **The pointwise statement for large primes p ≡ 1 (24)** | **NOT PROVED** |

The lane produced no proof and no hot lead. The sharpest structural output: (i) the problem is exactly
"for some j, the integer (p+3)/4 + j has two divisors a, b, ab | it, with a + b ≡ 0 mod 4j + 3"; (ii) the only
prime-specific input (the global quadratic colouring) controls one character per ρ and is provably insufficient
(4545 refutes the one-character implication "escape ⇒ solution"; this does not rule out other bounded-order
character arguments); (iii) no finite menu of fixed pairs (a,b) and no S-supported ab suffices (Lemmas 5.1–5.2) —
this does not exclude all congruence arguments; (iv) under Dickson/Hypothesis H, no uniform bound R on the witnessing
ρ suffices (Thm 7.7; this does not say ρ must tend monotonically to ∞). The methods of §7 failed as attempted.
For p = m² (gcd(m,ρ) = 1) all prime-factor residues lie in ker λ_ρ; non-coprime squares are excluded by Lemma 2.1.

## §9 Falsifier re-audit (end)

* (F1) squares: every PROVED positive statement here is either an equivalence (holds for all n) or a necessary
  condition; the only existence statements (Cor 3.4, ρ | p + 4) have hypotheses that fail for n = m², m odd
  (N_3 = (m² + 3)/4 is odd as m² + 3 ≡ 4 mod 8, and every prime factor ℓ ≠ 3 of it is ≡ 1 mod 3, Lemma 3.3(i)
  with ρ = 3 — if 3 | m, then 3 ∥ N_3 contributes only non-units mod 3;
  ρ | m² + 4 with ρ ≡ 3 mod 4 impossible since such ρ has a prime factor ≡ 3 mod 4, modulo which −4 ≡ m² would be a residue). ✓ No false proof.
* (F2) (a) full d-even family: the criterion restricts to ρ ≡ −p (mod 8) and N_ρ/2; Cor 3.4 (ρ = 3) is unavailable for
  p ≡ 1 (8) there. Its zeros recomputed and reconciled with the 22 (§6). (b) The actual F2 screen, the C-even (★)
  sub-line (c = 1 and d even), with its 12 zeros in [10¹⁰, 1.1·10¹⁰] (`r8_zeros_1e10.txt`): `scripts/z59_convo_screens.c`
  (`data/z59/convo/screen_r8.txt`) finds full-family witnesses with min ρ ≤ 15 and d-even witnesses with min ρ ≤ 31
  at all 12, every d-even witness having c ≥ 2 (e.g. 10156800001: (a,b,c,d) = (17,53,10,2818202), ρ = 7, per the
  cross-model review; my engine's first d-even witness there has ρ = 7, c = 10). So the full d-even family survives
  these 12 while its c = 1 sub-line fails; nothing in this memo is confined to (b). Nothing is claimed for either. ✓
* (F3) all 285 non-square composite zeros ≤ 8·10⁶ (`composite_zeros_le8e6.txt`), unrestricted divisibility form
  (no unit inverses): 284 have a witness with min ρ ≤ 51, and 4545 alone has none (exhaustive over ρ ≤ (n+4)/3;
  `data/z59/convo/screen_composite.txt`). 4545 is the counterexample that kills "escape ⇒ solution" (§4); it does
  not refute arguments exploiting the full primitive conductor p. ✓
* (F4) the actual screens: all 14 (★) = c = 1 zeros and all 38 𝔊* zeros (`gstar_zeros.txt`) have full witnesses
  with min ρ ≤ 23 (`data/z59/convo/screen_gstar.txt`; the 14 values listed in §6 reproduce). The 14 need c ≥ 2; the
  38 need not (37 has (1,2,1,5), c = 1). Additional screen: the a = 1 zeros 193, 2521, 66529 (min ρ 7, 23, 31);
  Thm 7.7 even produces 66529 inside its family. No argument here is confined to one line. ✓
Verdict: no hot lead; nothing survives as a proof. These are bounded checks, not proof that any mechanism survives
beyond the tested ranges.

## Prior results (attribution, from the cross-model review)

Being unprimed explains rediscovery but confers no novelty. Exact forms and the square/QNR obstruction:
`Z57_BFII.md` Lemma 1.1(a)–(e), Prop 2.2, Cor 2.3; `Z58_CONVF.md` Lemmas 1.1–1.3 (their e/σ = this memo's ρ).
ρ = 3 exact criterion: `Z58_CONVF.md` Lemma 1.5 proof. Even-d / numerator-8 distinction, 4545 and screen
behaviour: `Z58_WILDCARD.md` §0, Lemma 4.1. a = 1 / (★) exceptions: `B1_LINE.md` §§0, 2, 3.6 (and López).
(ab/p) = −1 for Type II and 4ab ∤ p − 1: `JOINT_BUDGET.md` Remark 4.4, Prop 4.3 (= Lemmas 2.1, 5.1 here); no
finite witness-modulus covering: `Z57_BFII.md` §3. Theorem 7.7: `DISPROOF_AVENUES.md` §3 Prop 3.1 (exact), mechanism
from `B1_LINE.md` Thm 4.2. Incremental here: the independent min-ρ census to 10⁸, the least-non-residue census
(incl. 2521), and the ρ-character packaging (Identity 3.2 / Lemma 3.3).

## Cross-model review

Review: `data/z59/xreview/REVIEW_CONVO.md` (verdict ACCEPT-WITH-FIXES; all numbered algebra CORRECT, numerics
reproduced). Fixed: (1) barrier prose narrowed in §3, §5, §7, §8 — residue conditions can force hits (p ≡ 73 mod 168),
Lemmas 5.1–5.2 only exclude finite fixed-pair / S-supported menus, 4545 refutes only the one-character escape
implication, §7 records failed attempts not impossibility, bounded-ρ obstruction kept conditional and non-monotone;
(2) F2 split into full d-even vs C-even (★) sub-line with the 12 R8 zeros actually screened; 15-vs-22 reconciled
(all odd primes; extra 3, 11, 19, 131, 491, 739, 2531, reproduced); F3 run on all 285 composite zeros; F4 run on the
14 (★) and 38 𝔊* zeros (`scripts/z59_convo_screens.c`); (3) prior attribution added, Thm 7.7 marked as an exact
rederivation of `DISPROOF_AVENUES.md` Prop 3.1 (Dickson suffices); (4) §7.1 "not bounded for q ≥ 11" removed;
the 30 least-q absences upgraded to complete via ab ≤ (p+1)/3.
