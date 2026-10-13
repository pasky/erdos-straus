# Hostile review 2 of EXPONENT_COVERING.md (O185) — R189, reviewer 2 (independent)

Scope: the infinite-ES-family claims (Thm 4.1, certificates `data/ec/cert_k*.json`) and Cor 1.5 (no finite ET/divisor
covering for 3·2^m + 1). Reviewed at author commit `676d2b33` (branch side-agent/exponent-covering).
I did not read reviews/exponent-covering-review.md and did not import any author script. All checks below use
from-scratch code `scripts/review_ec2_*.py` (run with `PYTHONPATH=scripts uv run --with sympy python …`).

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 4.1: ES for all n = k·2^m + 1, m ≥ 0, k ∈ {1, 9, 21, 27, 57, 171, 231, 315, 393, 495, 15015} | **SOUND — CERTIFIED by my independent check (all 11 certificates)** |
| Lemma 1.1 (periodicity) | SOUND |
| Cor 1.5 (integer unit-square points; no finite ET/divisor covering of 3·2^m + 1, k = 4^j − 1) | **SOUND** (math). The summary/assessment paraphrase "only integer obstruction points" overclaims (defect 1) |
| Thm 1.2 / 1.4 square part (Sq ⊂ S, Sq^× ⊂ S′) | SOUND-AFTER-REPAIRS (cite the right theorem, make primitivity explicit; defect 2) |
| side facts in §0, §2, §4 (529 mod 840, primes, k = 9 data, 2520 / 120120 congruences) | SOUND except an off-by-small-m slip (defect 3) |

No FATAL defects. One MAJOR (wording/label only), several MINOR.

## 1. Theorem 4.1 — independent re-certification

### 1.1 Certificate format (as I read it)
`{k, b=2, c=1, L, classes:[{M, r, fam, params, exps, xyz}]}`; `xyz` = three coefficient lists (ascending powers of n,
rational strings) for x(n), y(n), z(n). The `fam`/`params` fields are labels only: correctness of the theorem does not
depend on them (the certificate is self-contained: identity + integrality + positivity + coverage). I treat the
certificate as untrusted data.

### 1.2 What my checker does (`scripts/review_ec2_check.py`, different method from `ec_cert.py` at every step)
1. **Identity**: 4·x·y·z − n(xy + yz + zx) = 0 as sympy `Poly` over QQ.
2. **Integrality on r + MZ**: substitute n = r + Mt, let D = lcm of the denominators of the t-coefficients;
   Q := D·p(r+Mt) ∈ Z[t], and p is integer-valued on Z iff Q(t) ≡ 0 (mod D) for all t mod D (exhaustive). Result:
   **D = 1 for every polynomial of every class of every certificate**, i.e. all x, y, z ∈ Z[t] after the substitution —
   integrality is trivial, no binomial-basis subtleties.
3. **Positivity**: LC > 0 asserted; all real roots isolated exactly (`Poly.intervals`); R := max upper endpoint.
   R ≤ 0 for every polynomial of every class, so x, y, z > 0 for all n ≥ 1 in the class.
4. **Coverage by explicit exponent arithmetic**: for class (M = 2^s M′, r) the exponent set
   E = {m mod L : k·2^m + 1 ≡ r (mod M), m ≥ s} is computed prime-power by prime-power: for each q^e ∥ M′,
   o = ord_{q^e}(2) is computed and **asserted to divide L**, the admissible j mod o are listed, and E is the set of
   m mod L whose reduction mod each o is admissible; the 2-part requires r ≡ 1 (mod 2^s) (true for n_m, m ≥ s).
   Union of the E's = Z/L asserted. E also matches the certificate's `exps` field for every class.
5. **Threshold** m* = max over classes of (s, least m with n_m > R); ES for m < m* by my own solver
   (for each x: 1/y + 1/z = a/b ⇔ (ay − b)(az − b) = b², divisors of b² from factorisations of n and x;
   even n handled by 2/h = 1/h + 1/2h + 1/2h). Every solver output is re-verified exactly.

Logic: for m ≥ m*, n_m lies in some class (4), and that class's x, y, z are positive (3) integers (2) with
4/n = 1/x + 1/y + 1/z (1). For m < m*, brute force. Hence ES for all m ≥ 0. This is a complete proof modulo the
correctness of a few hundred lines of exact arithmetic.

### 1.3 Results
| k | L | classes | m* | brute force m < m* |
|---|---|---|---|---|
| 27 | 12 | 6 | 0 | — |
| 315 | 420 | 25 | 4 | m = 0..3 |
| 15015 | 840 | 24 | 4 | m = 0..3 |
| 1, 9, 21, 57, 171, 231, 393, 495 | 12, 72, 12, 60, 36, 84, 132, 396 | 2, 9, 6, 10, 8, 12, 16, 20 | 0, 2, 0, 0, 3, 3, 5, 3 | ok |

All 11 certificates PASS. Additional from-scratch runs (`scripts/review_ec2_spot.py 1e8 3000 40 …`, ~5 s total):
* own brute-force ES for **every** m with n_m ≤ 10⁸, all 11 k (e.g. k = 27: m ≤ 21; k = 315: m ≤ 18; k = 15015: m ≤ 12);
* certificate applied with exact integers for every m* ≤ m ≤ 3000 (all covered, all solutions valid and positive);
* 40 random m ∈ [5000, 40000] per k (n with 1 600 – 12 000 digits): class found, x, y, z exact positive integers,
  4xyz = n(xy+yz+zx) verified exactly.

**Verdict on Thm 4.1: SOUND, CERTIFIED by independent check.** The `fam` labels and the T1 control (vii) of the
author's checker are irrelevant to Thm 4.1 and need not be trusted.

## 2. Corollary 1.5 and the Proth-type claim — independent argument

### 2.1 The integer-point classification (Cor 1.5 as stated: ν(ℓ) ∈ Sq^× ⇔ ℓ = 0, k = 4^j − 1)
Re-derived. ℓ ≥ 0: the odd components are the integer N = k2^ℓ + 1; "square in Z_q for all odd q" ⇒ N = s² (a non-square
integer is a non-residue mod infinitely many primes), "unit at every odd q" ⇒ s = 2^j; s² − 1 = (2^j−1)(2^j+1) is odd, so
ℓ = 0, k = 4^j − 1. ℓ = −a < 0: components (k + 2^a)·2^{−a}; square everywhere ⇒ 2^a(k + 2^a) = □; unit everywhere ⇒ the odd
number k + 2^a has no odd prime factor ⇒ k + 2^a = 1, impossible. (The author's ℓ < 0 wording — "s a power of 2 … forces
i = 0, i.e. ℓ = 0" — reaches the same contradiction in a confusing way; defect 5.)
Brute force (`scripts/review_ec2_facts.py`): k odd ≤ 20001, |ℓ| ≤ 70 → exactly (k, ℓ) = (3,0), (15,0), (63,0), (255,0),
(1023,0), (4095,0), (16383,0). ✓

### 2.2 No finite ET/divisor covering of {(4^j − 1)·2^m + 1 : m ≥ m₀} — direct proof (no profinite machinery)
Suppose finitely many classes r_i mod M_i cover all n_m, m ≥ m₀. Put M = lcm M_i = 2^s M′ (M′ odd), L = ord_{M′}(2), and take
m = tL ≥ max(s, m₀, 3). Then n_m ≡ k + 1 = (2^j)² (mod M′) and n_m ≡ 1 (mod 2^s). Let σ ≡ 2^j (mod M′), σ ≡ 1 (mod 2^s):
gcd(σ, M) = 1 and n_m ≡ σ² (mod M). So the class r_i ∋ n_m satisfies r_i ≡ σ² (mod M_i) with σ a unit, hence it is primitive
and contains (σ + uM)² for all u (arbitrarily large squares of integers coprime to M). It is not a divisor class D_q (q | M′
and σ² ≡ 4^j ≢ 0 mod q). So it is an ET class containing arbitrarily large unit squares, which is impossible:
* **cited**: ET (arXiv:1107.1010, p. 7, checked in sources/elsholtz-tao-1107.1010.pdf): "a primitive congruence class n = r mod q
  which is a perfect square cannot be solved by polynomials ([44] Mordell, [68] Schinzel)". I could NOT access Schinzel's paper
  itself; I read "perfect square" as "r ≡ unit² mod q" (the only reading under which the 840 statement is consistent). If
  Schinzel's statement is for x, y, z ∈ Z[t] only, pass to a sub-progression mod M·D (D clearing denominators) — it still
  contains unit squares (choose u with σ + uM coprime to D).
* **re-derived** at class level for the two families the certificates use most:
  II1 (−e mod 4ab, e | a+b, (e,4ab)=1): ET's §4 reciprocity argument uses only n ≡ σ² (mod 4ab), so it is class-level.
  II2 (−4a²d mod f, 4ad | f+1): σ² ≡ −4a²d (mod f) gives (−d/f) = 1 (Jacobi); f ≡ 3 (mod 4) so (d/f) = −1; with d = 2^v d′,
  (d′/f) = (f/d′)(−1)^{((d′−1)/2)((f−1)/2)} = (−1/d′)(−1)^{(d′−1)/2} = 1, so (2/f)^v = −1, v odd ⇒ 8 | 4ad ⇒ f ≡ 7 (mod 8)
  ⇒ (2/f) = 1, contradiction.
* **EVIDENCE**: `scripts/review_ec2_t1.py 6000` transcribes the seven Prop 1.9 families from the ET PDF (not from `mordell_lib`)
  and enumerates 255 735 classes (with multiplicity) of modulus ≤ 6000: every class is primitive and none is a unit-square
  class mod its modulus.

**Verdict: SOUND.** Moreover the argument above shows more than the note claims (§5.3 says "for general Theorem-M procedures
… not checked"): no finite covering by *any* polynomial-solvable (ET Def., p. 7) classes plus arbitrary non-primitive classes
exists — n_m is a unit mod M, so non-primitive classes never contain it. This is PROVED modulo the Mordell–Schinzel theorem
as quoted by ET (suggested upgrade, defect 6).
