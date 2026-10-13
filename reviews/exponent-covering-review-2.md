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
  II1 (−e mod 4ab, e | a+b, (e,4ab)=1): σ² ≡ −e (mod 4ab) ⇒ e ≡ 3 (mod 4); with ab = 2^v q, q odd, (−e/q) = 1 ⇒ (q/e) = 1 by
  reciprocity; a ≡ −b (mod e) ⇒ (ab/e) = (−1/e) = −1 ⇒ (2/e)^v = −1 ⇒ v ≥ 1 ⇒ 8 | 4ab ⇒ e ≡ 7 (mod 8) ⇒ (2/e) = 1, contradiction.
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

## 3. Numbered defects

**1 (MAJOR — overclaimed label/paraphrase; no mathematical change needed).** §0 bullet 3 ("the only integer obstruction points
of k·2^m + 1 are k = 4^j − 1 at μ = 0 (PROVED)") and §6 bullet 1 ("the complete list of integer obstruction points (Cor 1.5 …)").
Cor 1.5 classifies integer points in Sq^× (unit-square points) only. An integer point ν(ℓ) can also be an obstruction by lying in
the sterile part S′ \ Sq^× — whether such points exist is exactly the open "no sterile non-square point" half of EC_k (§3, §5.3).
Repair: "the only integer *unit-square* obstruction points are …", and in §6 "complete list of integer unit-square points".

**2 (MINOR — proof hygiene in Thm 1.2 square part).** "r is odd when M is even … there are odd integers s′ ≡ s (mod M) with s′² in the
class … no ET class contains an odd square: Schinzel–Yamamoto … ET Prop 1.6 … class-level form". (a) What is actually needed and true
is that every ET class is *primitive* (all seven families: verified by derivation from the defining conditions and numerically,
`review_ec2_t1.py`), so any square point is a unit square at the primes of M and the class is a primitive quadratic-residue class.
(b) The right citation is ET p. 7 (Mordell [44] / Schinzel [68]: primitive square classes are not solvable by polynomials), not
Prop 1.6 (which is about f_I, f_II of an odd square n and, as the author notes, does not apply verbatim to composite n).
(c) `ec_t1check.py 3000` is EVIDENCE, not part of a proof; the proof should rest on (b) or on a class-level reciprocity lemma for all
seven families (I re-derived II1, II2 above; I1–I4, II3 still to be written out). Repair: state "ET classes are primitive" as a
lemma, cite ET p. 7 / Schinzel, keep the computation as a control.

**3 (MINOR — false for one small m).** §0 bullet 5 and §2 example: "27·2^m + 1 is ≡ 529 (mod 840) for m ≡ 2 (12)". For m = 2,
n = 109 ≡ 109 (mod 840). True for m ≡ 2 (12), m ≥ 14 (needs m ≥ 3 for the 2-part). Repair: add "m ≥ 3" (as already done for 315,
15015). (The §2 Legendre table itself is correct: `review_ec2_facts.py`.)

**4 (MINOR — "certified by an independent checker").** §0 bullet 6 / §4: `ec_cert.py` is written by the author in the same session
as the generator; it is a separate program, not an independent check in the review sense. Now independently confirmed (§1 above);
suggest wording "certificate checker `ec_cert.py`; independently re-certified in R189".

**5 (MINOR — wording in Cor 1.5 proof, ℓ < 0).** "s a power of 2: k = 4^j − 4^i odd forces i = 0, i.e. ℓ = 0" — in the ℓ < 0 branch
|ℓ| = 2i ≥ 2, so the correct conclusion is "no solution"; also k + 2^{|ℓ|} is odd, so s = 1 directly. Repair: "k + 2^{|ℓ|} is odd
and has no odd prime factor, so equals 1: impossible."

**6 (MINOR — undersold; suggested upgrade).** §5.3 "(for general Theorem-M procedures it is the usual H-conditional transfer … not
checked here)". The direct argument of §2.2 above proves, modulo the Mordell–Schinzel theorem as quoted in ET p. 7, that no finite
union of polynomial-solvable classes and non-primitive classes covers (4^j − 1)·2^m + 1 for m ≥ m₀ (the bad exponents are
m ≡ 0 mod L and there n_m is a unit square mod M). Repair: add this as a remark (CONDITIONAL on/citing Schinzel [68], which I could
not access).

**7 (MINOR — terminology).** "Proth numbers 3·2^m + 1" (§0, §5.3): Proth numbers are k·2^m + 1 with odd k < 2^m; the family meant is
the k = 3 subfamily. Repair: "numbers 3·2^m + 1 (the k = 3 Proth family)".

**8 (MINOR — garbled sentence, outside main scope).** Prop 2.1: "exists only if (i) … or (ii) F̄ avoids Sq^× because of (i) after all" —
(ii) is (i). Repair: delete (ii) or state what is meant (e.g. a one-prime obstruction at q = 2).

## 4. Other checks (all ✓, `scripts/review_ec2_facts.py`)
* 109, 27·2²⁶ + 1, 27·2⁵⁰ + 1 are prime; 315·2^m + 1 ≡ 1 (mod 2520) and 15015·2^m + 1 ≡ 1 (mod 120120) for m ≥ 3 (120120 = 2³·3·5·7·11·13).
* §4.3 (k = 9): 9·2⁵ + 1 = 17², ord₁₇2 = 8, ord₃₈₇₃₇2 = 72, M = 464844 = 4·3·38737, class residue ≡ −287 (mod 38737),
  287 | 4·3²·38737 + 1 (I1 condition), the class is used only for m ≡ 41 (72); first primes with v₂(ord_q 2) = 3 and (−287/q) = −1 are
  241, 353, 433 (then 977, 1297) as claimed.
* Lemma 1.1 and Thm 1.2 (a)⇔(b) re-read: correct (C is a finite union of clopen sets; n_m ≡ c mod 2^s for m ≥ s).
* Not checked: §4.2 survey numbers (EVIDENCE), §5.1 S-unit and §5.2 claims, §3 literature claims (Bertók–Hajdu), §5.4 literature search.

## 5. Bottom line
The infinite-family claims of Thm 4.1 are **CERTIFIED by my independent check** for all eleven k (including the required k = 27,
315, 15015): exact polynomial identities, integer coefficients after n = r + Mt (no denominators at all), positivity for all n ≥ 1,
full coverage of Z/L verified by per-prime-power exponent arithmetic with ord | L asserted, brute force for the few m < m*, plus
brute force for all n_m ≤ 10⁸ and exact checks at random m up to 40 000. Cor 1.5 and its "no finite ET/divisor covering of
(4^j − 1)·2^m + 1" consequence are SOUND by an independent direct argument. Only label/wording repairs are required (defects 1–8).

## Repairs applied (round 1, after merging main with R185 repairs)
Applied by the reviewer, marked "(R189 repair)": defect 1 (EXPONENT_COVERING §0 ×2, Cor 1.5 title, §6; AGENT_REPORT_O185 items 2, 4),
defect 4 (§0 checker attribution; report item 3 and "What was done"), defect 7 (§0, §5.3; report item 4), defect 3 in AGENT_REPORT_O185
item 3 (m ≥ 14). Already fixed by "(R185 repair)", skipped: defect 2 (primitivity + Mordell/Schinzel in Thm 1.2), defect 3 in
EXPONENT_COVERING (§0, table), defect 5 (Cor 1.5 proof rewritten), defect 6 (scope = polynomial-solvable + divisor classes in §0/§5.3),
defect 8 (Prop 2.1 clause (ii)). No mathematical content changed; Thm 4.1 remains CERTIFIED.
