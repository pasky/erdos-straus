# Z59_CONVO — tryhard lane CONVO (wave z59): pointwise solvability of 4abcd = a + b + pc for primes p ≡ 1 (mod 24)

Status: **NOT PROVED.** No hot lead. What follows: proved reformulations and a proved local/character
analysis ("ρ-ratio criterion") that isolates exactly what a pointwise proof must supply, numerical evidence, and
the falsifier audit. Fresh attack: no FRONTIER / Z5*_* memo / lane file was read; only `data/z58/screens/`.

Notation. p ≡ 1 (mod 24) prime throughout unless stated; χ_p(·) = (·/p) Legendre. "Solution" = (a,b,c,d) ∈ ℕ⁴
with 4abcd = a + b + pc. For ρ ≡ 3 (mod 4): N_ρ := (p + ρ)/4 ∈ ℕ (since p ≡ 1 mod 4).

## §0 Mandatory falsifiers (stated at first commit; re-audited in §9)

* (F1) odd squares n = m²: no solution exists. Any proof step must fail for n = m². In this memo the only
  "existence" inputs are of the form "−1 lies in the ratio set of divisors of N_ρ modulo ρ" (§3); for n = m² all
  prime factors ℓ of m² + ρ satisfy (−ρ/ℓ) = 1, which confines that ratio set to the kernel of a quadratic character
  that is −1 at −1 (Lemma 3.3). So the step that must use non-squareness is "some prime factor of N_ρ escapes
  that kernel AND the escaping residues combine to −1"; §4–§5 show the first half is free for NR ρ while the
  second half is exactly what is not provable by any tool found here.
* (F2) d-even half: d never enters the ρ-ratio criterion except through d = N_ρ/(ab); forcing d even means
  requiring 2·ab | N_ρ i.e. ab | N_ρ/2 — only possible when 8 | p + ρ, i.e. ρ ≡ 7 (mod 8). So every "d even"
  statement here is the same criterion restricted to ρ ≡ 7 (mod 8) with N_ρ replaced by N_ρ/2; any argument
  that only needs ρ = 3 (or ρ ≡ 3 mod 8) is dead on the d-even half. (The d-even half has 22 zeros ≤ 10⁹.)
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

**Criterion 3.1.** p is solvable ⇔ ∃ ρ ≡ 3 (mod 4) such that −1 lies in the *ratio set*
R_ρ(N_ρ) := { a·b⁻¹ mod ρ : ab | N_ρ } ⊂ (ℤ/ρ)^*. (Lemma 1.1; a, b are automatically prime to ρ: a prime
ℓ | (ρ, a) with ℓ | a + b gives ℓ² | ab | N_ρ, ℓ | p + ρ, so ℓ = p; but ρ ≤ a + b and 4abd = p + ρ force ρ < p.)
Since N_{ρ+4} = N_ρ + 1, with M := (p+3)/4 the criterion reads: **∃ j ≥ 0 such that the integer M + j has
divisors a, b with ab | M + j and a + b ≡ 0 (mod 4j + 3).** (ρ = 4j + 3.) The prime p enters only through M.

**Identity 3.2 (convolution form).** For ρ with (N_ρ, ρ) = 1, writing τ_ψ(N) := Σ_{abd = N} ψ(a)ψ̄(b),
  W_ρ := #{(a,b) : ab | N_ρ, ρ | a + b} = φ(ρ)⁻¹ Σ_{ψ mod ρ} ψ(−1) τ_ψ(N_ρ),
(orthogonality applied to 1[a ≡ −b]). τ_ψ is multiplicative: τ_ψ(ℓ^e) = Σ_{i+j ≤ e} ψ(ℓ)^{i−j}.

**Lemma 3.3 (square cancellation = (F1) mechanism).** Let ρ ≡ 3 (mod 4), λ = (·/ρ) (Jacobi). For every prime
ℓ ∤ 2ρ dividing n + ρ: λ(ℓ) = (−ρ/ℓ) = (n/ℓ) [first equality: Jacobi reciprocity, ρ ≡ 3 mod 4; second: −ρ ≡ n
mod ℓ]. Hence (i) n = m²: λ(ℓ) = 1 for every prime ℓ ∤ ρ dividing N_ρ (ℓ ∤ m since ℓ | m, ℓ | m²+ρ ⇒ ℓ | ρ), so
τ_λ(N_ρ) = τ_{ψ₀}(N_ρ) and the ψ₀ and λ terms of 3.2 cancel exactly; more strongly every admissible ratio a/b
lies in ker λ ∌ −1 (λ(−1) = −1), so W_ρ = 0 (the square obstruction, visible as a spectral cancellation).
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
prime factors of N_ρ — information that no residue condition on p supplies (§5) and that the only prime-specific
input found (reciprocity, §4) does not touch.

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
Primes p ≡ 1 (mod 4L) exist for every L (Dirichlet), and p ≡ 1 (mod 24) is compatible. Hence for every finite
set of moduli there are primes in our class for which every solution uses a prime factor of ab outside any
prescribed finite set: no finite list of residue-class conditions on p ("polynomial identities") can prove the
statement — the classical Mordell barrier, here in two lines. A proof must therefore use some property of p
that is not a congruence condition. The only one exhibited here is the colouring of §4 (whose sole consequence
for the criterion, the escape lemma, is a congruence statement modulo ρ). The remaining candidate inputs —
the size/shape of the factorisations of (p+ρ)/4 for ρ ≤ R(p) — are statements about integers in the short interval
[p/4, (p+R)/4], which for squares are rigidly constrained (norms from ℚ(√−ρ)) and for primes are constrained by
nothing that is currently provable pointwise.
