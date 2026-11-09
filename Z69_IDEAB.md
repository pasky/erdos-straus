# Z69_IDEAB — independent ideation on Erdős–Straus (lane IDEAB, wave z69)

**ES is OPEN. Nothing here claims otherwise.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.

Status: Phase 1 in progress (written from own knowledge only; no repo memo / FRONTIER / git grep consulted;
only `z69_lanes.md` header+IDEAB and `z58_lanes.md` Common rules + falsifier table were read).

## §0 Falsifier table — placeholder
The mandatory falsifier table (F1 odd squares, F2 numerator 8 / C-even, F3 composites, F4 known zeros) is filled in
for the Phase-3 idea in §3, after Phase 1 is committed (the table's notation (★), R, 𝔊*, 𝔐 is campaign-internal and
I have deliberately not looked it up yet). During Phase 1 each idea carries its own "squares / six classes" line.

## §1 Phase-1 idea list (independent)

### 1.0 Working reformulations (all PROVED, elementary; derived here from scratch)
Let p ≡ 1 (mod 4) be prime (p ≡ 3 mod 4 is trivial). Every solution has p | exactly one or exactly two denominators.

* **(R1) two-divisor form.** Put e = 4x − p > 0 (e ≡ 3 mod 4), x = (p+e)/4. Then (ey − px)(ez − px) = p²x², hence
  ES(p) ⟺ ∃ e ≡ 3 (4) and δ | x² with δ ≡ −x (mod e) [**Type II**, p | y,z] or δ ≡ −4x² (mod e) [**Type I**, p | z only].
  Equivalently with coprime a,b | x: e | a+b (II) or e | a+pb (I).
* **(R2) six-parameter form (Elsholtz–Tao style).** II: 4abd = p+e, ce = a+b. I: 4abd = pe+1, ce = a+b.
  So both types ask for the *same* thing on two different numbers: N/4 has coprime divisors a,b with e | a+b, where
  N = p+e (II) or N = pe+1 (I).
* **(R3) one-equation forms.** II ⟺ pc = 4abcd − a − b ⟺ (4acd−1)(4bcd−1) = 4c²dp + 1.
  I ⟺ (4acd − p)(4bcd − p) = p² + 4c²d ⟺ (4acd − p) | (4a²d + 1).
* **(R4) residue-class ("identity") forms.** Fixing all but one parameter gives the congruence classes that polynomial
  identities cover:
  K1 (II, d free): p ≡ −e (mod 4ab), e | a+b.  K2 (II, b free): p ≡ −4a²d (mod 4k−1), ad | k.
  K3 (I, c free): p ≡ −f (mod 4ad), f | 4a²d+1.
  Two memorable special cases: **F1** ∃ q ≥ 1: (−p mod 4q) divides q+1;  **F2** ∃ k ≥ 1: (−p mod (4k−1)) divides k.
* **(R5) reciprocity lemma (why squares die).** In any Type I/II solution with gcd(a,b)=1 the Jacobi symbol of p at
  the odd part of ab is −1 when p ≡ 1 (8) (computation: (−e/a) = (a/e) for e ≡ 3 (4), so (p/ab) = (ab/e) = (−a²/e) = −1);
  in form K2 the modulus u = 4k−1 itself satisfies (p/u) = −1. So every "coprime-type" solution carries a
  quadratic-non-residue witness for p; n = m² has none (its solutions all come from m). Also: for odd prime q | x_e,
  (q/e) = (p/q). The six classes mod 840 are exactly the unit squares mod 840, i.e. p that look like squares at 2,3,5,7.
* **(R6) Euclid/continued-fraction form.** II ⟺ ∃ u ≡ 3 (4) and integers b,c ≥ 1 with a := bu − pc > 0 and
  4ac | u+1. Since then 0 < b/c − p/u = a/(cu) < 1/(2c²), b/c is automatically a convergent of p/u. For c = 1:
  **p/u = a − 1/(4d − 1/b)**, i.e. p is the numerator of a length-3 Hirzebruch–Jung (minus) continued fraction
  [[a, 4d, b]]; in SL₂ terms −p is the upper-right entry of TᵃL^{−4d}Tᵇ.
* **(R7) modular-hyperbola form.** c = 1, II ⟺ ∃ u,u* ∈ [1,p) with uu* = 1 + 4dp and u ≡ u* ≡ −1 (mod 4d): a point of
  the modular hyperbola mod p congruent to (−1,−1) modulo (4 × its own branch index).

### 1.1 The ideas
Format per idea: **Key lemma** (precise) · **Squares** (where non-squareness enters / why it fails on m²) ·
**Six classes** (how p ≡ 1,121,169,289,361,529 mod 840 are treated) · **Assessment**.

**I1. Profinite exceptional set ("converse Schinzel", uniform covering).**
Let U ⊂ Ẑ be the (open) union of all identity classes K1∪K2∪K3 and C = Ẑ^× ∖ U (closed). Schinzel/Mordell: C ⊇ S :=
{unit squares of Ẑ}. ES for p ≡ 1 (4) ⟺ no prime lies in C.
*Key lemma (CONJECTURE UC):* C ∩ {α ≡ 1 mod 4} = S; equivalently (compactness) for every modulus m and every unit class
r mod m containing no square, **finitely many** identity classes cover all of r mod m. UC ⟹ ES, since a prime is not a
square in Ẑ. UC is strictly stronger than ES (ES only says primes ∉ C, and primes are merely dense).
*Squares:* they are exactly the allowed exceptional set; non-squareness enters as "p ∉ S, so some finite level (m, r)
separates p from S". *Six classes:* p in a square class mod 840 is handled at the level m = 840·q^j with q the least
non-residue prime of p; UC predicts a **bound on the least identity modulus that is uniform over all n ≡ r (mod m)**
— a sharply testable prediction (and falsifiable: one non-square integer n with no coprime-type solution kills UC as stated
and forces a description of the true C).
*Assessment:* cleanest "structural" strengthening I know; the test is cheap. Top-5.

**I2. Structure theory of C when UC fails.** If some non-square integers n lie in C (no K1/K2/K3 class contains n),
describe C∩ℤ algebraically (e.g. "n = m²k with k from an explicit set", or "n divisible by …").
*Key lemma (form):* C ∩ ℤ ⊂ {n : n has property 𝒫} with 𝒫 visibly false for primes (as "is a square" is).
*Squares:* inside C by construction. *Six classes:* a prime in the six classes is excluded from C iff 𝒫 fails for it;
so the whole problem is transferred to *naming* 𝒫. *Assessment:* only meaningful after the I1 experiment; paired with I1.

**I3. Hirzebruch–Jung / continuant formulation (R6).** ES(c=1) ⟺ p = K⁻(a,4d,b) := 4abd − a − b ⟺ the lens space
L(p,u) (u = 4db−1) is surgery on a 3-chain with framings (−a,−4d,−b) ⟺ Dedekind sum identity
12·s(u,p) = (u+u*)/p + (a+4d+b−9).
*Key lemma (needed):* for fixed prime p the set {u mod p : HJ-length(p/u) = 3 with middle term ≡ 0 (4)} is non-empty;
a route would be exact formulas for the number of u with HJ-length ≤ 3 (Heilbronn/Porter-type statistics are asymptotic
only for *typical* length ≍ log p, so the length-3 stratum is a thin "cusp" of the distribution).
*Squares:* n = m² has length-3 expansions only with middle term ≢ 0 (4) or with gcd(u,n) > 1 — R5 is the reason.
*Six classes:* no special treatment; the method would have to see (p/u) = −1.
*Assessment:* pretty, probably only a restatement; gives access to Dedekind-sum reciprocity. Mid.

**I4. Modular hyperbola + Weil (R7).** Points (u,u*) of uu* ≡ 1 (mod p) are equidistributed in boxes of area ≫ p^{3/2+ε}
(Kloosterman/Weil) — an *individual-p* tool.
*Key lemma (needed):* a count, with error o(main), of points with (u,u*) ≡ (−1,−1) mod q, q = 4·(branch index).
*Obstruction found while writing it down:* the event has probability ≍ 1/p per point (the modulus is tied to the branch),
so detecting it needs all ≍ p harmonics; Weil saves only √p. Summing over the natural 2-parameter family gives main term
≍ log² p against error ≍ √p. *Squares:* the count is identically 0 on squares, so any asymptotic "main term" must be
cancelled by real characters there — the main term is not the naive one. *Six classes:* none.
*Assessment:* dead as stated (binary-problem barrier); recorded so it is not re-tried naively.
