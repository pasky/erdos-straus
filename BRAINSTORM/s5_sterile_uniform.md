# s5_sterile_uniform — one sterile-point theory for F_q[T] and ℤ, and the global input it makes unavoidable (combination (v))

## Idea
(J)56 (F_q[T], every q = 3^r except q = 3, and q = 9 at k = 1; R227 D16) and (J)54 (ℤ, least non-residue r ≥ 2³²) prove "no finite linear covering"
by the same mechanism: a union bound in Haar measure, with Coppersmith/Lenstra-type class-divisor bounds, shows that the
profinite sterile set is non-empty. The brief asks for a uniform statement and for the global input it forces.

## Uniform formulation (PROVED as a formal statement; the content is (J)51/(J)54/(J)56)
Let R ∈ {ℤ, F_q[T]}, R̂ its profinite completion, and 𝒮 ⊂ R̂ the set of points not covered by any ET/linear family.
Each family covers an open set U_f ⊂ R̂, and "finite covering" means R̂^{prime-admissible} ⊂ ⋃_{f∈F} U_f for a finite F.
* Sterility theorems: 𝒮 ≠ ∅ (within the relevant cell).
* Haar-nullity ((J)24): μ(𝒮) = 0.
* Consequence (formal): any proof of ES on the cell must use, for primes accumulating at s ∈ 𝒮, data that is **not a
  function of the image of p in R̂**.
* (Assessment, R227 repair D15) The only such data *in use* in either ring is the place at infinity: |p| over ℤ,
  deg P over F_q[T]. No classification of non-locally-constant data is proved.
* And in both rings the certificate moduli are bounded in terms of that data: O(p²) over ℤ ((J)25), degree ≤ 2 deg P
  over F_q[T].
* So the unavoidable global input is precisely the **coupling "modulus ≤ size(p)^{O(1)}"** (the box, B3). ES is a
  growing-covering problem: the covering by moduli ≤ X must cover the primes of size ≤ X^{1/2}, for every X.

## Comparison table (Assessment)
| | F_q[T], q = 3^r ≥ 9 | ℤ |
|---|---|---|
| sterile cell | x*_c type points, every c-slice for r ≥ 5 | r-generic line, non-residue cells, r ≥ 2³² |
| divisor input | function-field Lenstra (≤ 2 divisors in a class if 3 deg Q > deg F) | Cor 1.4 (Minkowski/Coppersmith) |
| failure of sterility | q = 3, A = T: covering exists ((J)4) | r = 13: covered at level 1 |
| mute-place theorem | one mute place ⇒ ES variant PROVED at every P ((J)30, Weil) | ES^{(S)}, \|S\| ≥ 4 PROVED ((J)23, sieve) |
| global input left | deg P (Weil bound needs it) | \|p\| (sieve/Bombieri–Vinogradov needs it) |

Reading. In both rings the PROVED variants (mute place / mute set) use the place at ∞ through *analytic* input (Weil
bound, sieve) with a **fixed** firing modulus. ES uses it through the box with a **moving** modulus. Sterility shows
that ES cannot drop the ∞-coupling. (J)52 suggests that dropping positivity, the ∞-*sign*, does not help (SQ_± — a CONJECTURE, so this is conditional;
R227 repair D15). So the
∞-coupling needed is the *size* coupling, not the sign.

## Prop V (PROVED, elementary; a precise "unavoidable input" statement)
**(R227 repair D14.)** As first written Prop V is vacuous/false: ℤ → ℤ̂ is injective, so every property of p is
"determined by its image". Corrected statement: let P be **locally constant** on R̂ (depends on p mod one fixed N) and
true at every admissible prime of the cell; then P does not imply that p has a certificate *from a fixed finite family
F*. Proof: U_F is a finite union of residue classes, hence clopen; s ∉ U_F gives a neighbourhood s + NR̂ disjoint from
U_F, containing infinitely many primes (Dirichlet/Kornblum). It does **not** show that P fails to imply ES (ES may use
families outside F). This is B1. Read "not a function of the image of p in R̂" below as "not locally constant on R̂".
Let P be any property of primes that is (i) determined by the image of p in R̂ and (ii) true at every prime admissible
for the sterile cell. Then P does not imply ES on that cell, because the primes in small neighbourhoods of a sterile
point have no certificate in any fixed finite family. *Proof:* a certificate in a fixed family is an open condition, and
s ∉ ⋃U_f; Dirichlet/Kornblum gives primes in every neighbourhood. ∎ This is B1 restated profinitely. Its use here is
the uniform form across both rings.

## Literature
(J)24, (J)26, (J)51, (J)54, (J)56 in this ledger; Cohn–Heninger arXiv:1008.1284; Bernstein (2006); Kornblum (Dirichlet
for F_q[T]).

## Barrier screen
This memo *is* the B1/B3 barrier, made uniform. T1 is not involved: sterile points are not squares.

## Cheap numerics
None new. The certified inequalities are (J)54's and (J)56's own (`scripts/se_certify.sh`, FF_STERILE_SMALL scripts).

## Assessment
PROVED (formal) plus Assessment. The uniform lesson: **the global input that an ES proof cannot avoid is the
size/degree coupling between the prime and its certificate modulus; sign data (positivity) is avoidable (conditional on CONJECTURE SQ_±; R227 D15) and
congruence data is insufficient (sterility).** It is a precise statement of what a proof must contain, not a route.
Spark: q = 3 (CONJECTURE 0.2) is the only ring where sterility is open. A covering for q = 3, A = T^k would be the
first case where a finite covering exists in one ring and provably not in its "siblings", which would be a sharp
test of whether char-3 small-field accidents (like q = 3, A = T) persist.
