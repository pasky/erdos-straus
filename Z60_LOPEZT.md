# Z60_LOPEZT — tryhard lane: the two-branch divisor statement (4/p, Type II sub-family)

Fresh attack (no FRONTIER / Z5*/Z6* memos read). Data used: `data/z58/screens/` only.

## §0 Problem, exact reformulations, and the four mandatory falsifiers

**Statement S(p).** For a prime p ≡ 1 (mod 24) (large), there is y ≥ 1 and a divisor f | p + y with f ≡ −1 (mod L_y),
L_y = y if 4 | y, L_y = 4y otherwise. Branches (corrected brief):
* **B4** (4 | y, modulus y): fails alone at the primes 193, 2521, 66529 (≤ 10¹⁰ per brief; verified ≤ 2·10⁵ by `scripts/z60_lopezt_branches.c`).
* **BN** (4 ∤ y, modulus 4y): fails alone at the 14 primes of `data/z58/screens/star_prime_zeros.txt` (409 … 8 813 281); verified ≤ 2·10⁵.
* Both branches together: fails at every odd square and, among odd non-squares ≤ 10¹⁰, only at 105 and 4545 (verified ≤ 6·10⁴).

### §0.1 Exact equivalences (PROVED, elementary)

Lemma 0.1 (BN identity). If p + y = f g with f = 4yk − 1 (k ≥ 1), then p = 4ykg − y − g and
  4/p = 1/(ykg) + 1/(pgk) + 1/(pyk).
Proof: 4ykg = p + y + g; divide by p·ykg. ∎ (No condition on y is needed; BN restricted to 4 ∤ y is only the brief's bookkeeping. The modulus-4y divisor condition for 4 | y is strictly stronger than B4.)

Lemma 0.2 (B4 identity). If 4 | Y, Y = 4Y', p + Y = f g with f = Yk − 1 (k ≥ 1), then p + g = Y(gk − 1) and
  4/p = 1/(Y'(gk−1)) + 1/(pY'k) + 1/(pY'k(gk−1)).
Proof: fg = Ykg − g = p + Y ⇒ p + g = Y(gk−1) = 4Y'(gk−1). Then 1/(pY'k) + 1/(pY'k(gk−1)) = g/(pY'(gk−1)), and adding
1/(Y'(gk−1)) gives (p+g)/(pY'(gk−1)) = 4/p. ∎
(Numerically found: among the Type I/II parametrizations of all solutions of 4/p for 681 B4-hits with p < 1500, the choice c = g in the
Type II form below always worked, with (a, b, m) = (1, gk−1, k).)

Lemma 0.3 (complete Type II parametrization; p prime). Solutions 4/p = 1/x + 1/(py') + 1/(pz') (p ∤ x) are exactly
  p = 4abd' − (a+b)/m with m | a + b,   x = ab d', y' = a d' m, z' = b d' m   (a, b, d', m ≥ 1).
Equivalently: ∃ a, b, c ≥ 1 with c | a + b and 4ab | p + c.
Proof: 4xy'z' = py'z' + x(y'+z'). Put d = gcd(y',z'), y' = da, z' = db, gcd(a,b)=1: x(4dab − a − b) = p d ab; since
gcd(4dab−a−b, ab) = 1, ab | x, x = ab x', and x'(4dab − a − b) = p d. If p | x' then 4dab − a − b ≤ d, impossible. So
4dab − a − b = mp and then d = x' m (as x'·mp = pd); substituting, 4x'mab − (a+b) = mp ⇒ p = 4x'ab − (a+b)/m, with d' := x'. ∎
  * BN ⟺ Type II with m = 1 (a = y, b = g, d' = k).
  * B4 ⟺ Type II with a = 1 (c = g, b = gk − 1, m = k, d' = Y').
So S(p) is a strict sub-family of "4/p has a Type II solution", hence of ES itself; nothing here is easier than ES for large primes.

Lemma 0.4 (complete Type I parametrization; p prime). Solutions 4/p = 1/x + 1/y + 1/(pz') with p ∤ xy are exactly
  m p = 4abw − 1, a + b = d' m,   x = w d' a, y = w d' b, z' = abw.
Equivalently ∃ a, w, c with c | 4a²w + 1 and 4aw | p + c; equivalently ∃ m ≡ 3 (mod 4): (mp+1)/4 = a·b·w with m | a + b.
(Proof as in 0.3; the gcd step uses gcd(ab, a+b) = 1 and p ∤ ab.)
For p ≡ 1 (4), every ES solution is Type I or Type II (p divides 1 or 2 of x, y, z; not 0 since 4xyz = p(xy+yz+zx); not 3 since 4 ≤ 3 fails).

**Unified forms of S(p)** (PROVED, by Lemmas 0.1–0.2 and their converses):
  (U1) ∃ a ≥ 1, ε ∈ {1, 4}: p + εa has a divisor ≡ −1 (mod 4a).        [ε = 1: BN; ε = 4: B4 with Y = 4a]
  (U2) ∃ y, e ≥ 1: 4ye | p + y + e (BN) or 4ye | p + y + 4e (B4).
  (U3) ∃ t ≥ 1: 4tp + 1 (BN) or tp + 1 (B4) has a divisor D ≡ −1 (mod 4t).
  (U4) ∃ (t, a, b) ∈ ℕ³: p = 4tab − a − b (BN) or p = 4tab − 4a − b (B4).
Converse checks: (U3) BN: 4tp+1 = DE with D ≡ −1 (4t) forces E ≡ −1 (4t), so D = 4ta−1, E = 4tb−1, p = 4tab − a − b.
(U3) B4: tp + 1 = DE, D = 4ta − 1 ⇒ E ≡ −1 (t), E = tb − 1 ⇒ p = 4tab − 4a − b ⇒ p + 4a = b(4ta−1): Y = 4a, f = D. ✓
This is the brief's "T-form" (L_T = T for 4 | T is the BN case with t = T/4; L_T = 4T otherwise is the B4 case t = T).

### §0.2 The four falsifiers — what any proof must respect

**(F1) odd squares n = m².** Lemma 0.5 (PROVED). If D | tn + 1 or D | 4tn + 1 with D ≡ −1 (mod 4t), then the Jacobi symbol (n/D) = −1.
Proof: D ≡ 3 (mod 4) so (−1/D) = −1, and tn ≡ −1 (resp. 4tn ≡ −1) mod D gives (t/D)(n/D) = −1. Claim (t/D) = +1: write
t = 2^s t₀, t₀ odd. If s ≥ 1 then 8 | 4t | D+1, so (2/D) = 1. For t₀: D ≡ −1 (mod t₀) gives (D/t₀) = (−1/t₀) = (−1)^{(t₀−1)/2},
and reciprocity with (D−1)/2 odd gives (t₀/D) = (D/t₀)(−1)^{(t₀−1)/2} = +1. ∎
Hence for n = m² (gcd(m, D) = 1 automatically) no witness exists. **Any proof must produce a D with (p/D) = −1**: the step
that uses non-squareness is the one that supplies a prime q | D with (p/q) = −1. For p ≡ 1 (mod 24) that is a quadratic residue
modulo every prime below z, every witness D must contain a prime q > z — no finite covering system can work on this class.

**(F2) numerator-8 analogue.** The same derivation for 8/p gives Type II: p = 8abd' − (a+b)/m; the two branches become
  ∃ t: 8tp + 1 or tp + 1 has a divisor ≡ −1 (mod 8t)   (equivalently p = 8tab − a − b or p = 8tab − 8a − b).
The brief: this fails at 45 primes ≡ 1 (4) ≤ 10⁸ (last 3 869 153). The expected number of witnesses with D ≤ X is
≍ (log X)² in both cases, with a smaller constant for 8. So a "generic" counting argument cannot distinguish 4 from 8; a
proof must either be quantitative with explicit constants that fail for 8 below 3.9·10⁶, or exploit a 4-specific
covering structure. (This is a check on explicitness, not a structural obstruction: heuristically both have finitely many zeros.)

**(F3) n = 105, 4545.** Non-squares where S fails; both composite. Any argument "for all large non-squares" is false below 4545;
an argument using primality must point to the step where p prime (not merely non-square) is used, or carry a threshold.

**(F4) single-branch zeros.** BN alone fails at 409 … 8 813 281; B4 alone at 193, 2521, 66529. A proof using one branch only
must have threshold > 8 813 281 (BN) or > 66 529 (B4), with a stated reason.

(Status tags below: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE.)

## §1 The witness-modulus form (U5) and the inversion symmetry of the two branches (PROVED)

Fix a witness modulus g ≡ 3 (mod 4), g ∤ p. Let Q := (g+1)/4 and R_g := { −a mod g : a | Q } ⊂ (ℤ/g)^× (all distinct, since a ≤ Q < g).

Lemma 1.1. (BN with this g) ⟺ p mod g ∈ R_g.   (B4 with this g) ⟺ p^{−1} mod g ∈ R_g.   Hence
  **(U5)  S(p) ⟺ ∃ g ≡ 3 (mod 4) with p^{±1} mod g ∈ R_g = −Div((g+1)/4).**
Proof. BN: g | p + a with g ≡ −1 (mod 4a) ⟺ a | Q and p ≡ −a (mod g). B4 (U3 form, t = Q/a): g | tp + 1 ⟺ tp ≡ −1 ⟺
p ≡ −t^{−1} ≡ −4a (mod g) (as 4ta = g + 1 ≡ 1) ⟺ p^{−1} ≡ −(4a)^{−1} ≡ −t (mod g), and t | Q. ∎
Remarks. (i) R_g ⊂ {QNR mod g}: (−a/g) = −(a/g) = −1 by Lemma 0.5's argument (g ≡ −1 mod 4a ⇒ (a/g) = 1).
(ii) The g-range: BN witnesses have g ≤ (4p+1)/3, B4 witnesses g ≤ 2p + 1 (t = 1: g | p + 1; t ≥ 2: g(1 − 1/t) ≤ p + 1/t).
(iii) The numerator-8 analogue is literally: ∃ g ≡ 7 (mod 8) with p^{±1} mod g ∈ −Div((g+1)/8). Since Div((g+1)/8) ⊂ Div((g+1)/4),
S₈ ⟹ S₄. `scripts/z60_lopezt_u5.c` (which implements (U5) directly) reproduces: S₄ zeros ≤ 6·10⁴ among odd non-squares = {105, 4545},
no prime zeros ≤ 2·10⁵; S₈ prime zeros ≤ 4·10⁶: exactly 45, last 3 869 153 (`data/z60/lopezt/s8_zeros_le4e6.txt`) — matching the brief,
which certifies the derivation of the 8-analogue.
**Sharpened (F2):** every S₄-witness that is not an S₈-witness has either g ≡ 3 (mod 8), or g ≡ 7 (mod 8) with v₂(a) = v₂((g+1)/4)
(a the divisor used). A proof of S₄ must produce such witnesses for (at least) the 45 primes in the file, or carry a threshold > 3 869 153.

Lemma 1.2 (no finite covering, even inside p ≡ 1 (24)). For any M, let L = lcm{4m : m ≤ M}·24. Every prime p ≡ 1 (mod L) has no
witness with g ≤ M: for such p, p ≡ 1 is a square mod g, but R_g consists of non-residues. By Linnik there are such primes with
p ≤ L^{C} = e^{O(M)}, i.e. infinitely many primes p ≡ 1 (24) whose every witness has g ≥ c·log p. More generally, if p is a
quadratic residue modulo every prime ≤ z, every witness g has a prime factor q > z with (p/q) = −1. ∎
Consequence: no argument that exhibits a witness from finitely many congruence conditions on p can prove S(p); the witness must be
built from a prime factor of some tp + 1 / 4tp + 1 that is not determined by p modulo any fixed modulus.

## §2 Where S sits inside ES: the (a, m)-lattice of Type II, and Type I (PROVED)

Lemma 2.1 (Type II, two-parameter divisor form). For p prime, 4/p has a Type II solution ⟺
  **∃ a, m ≥ 1 (WLOG gcd(a, m) = 1): mp + a has a divisor g ≡ −1 (mod 4am).**
Proof. (⇐) g = 4amd' − 1, b := (mp + a)/g. Then mp = 4abmd' − a − b, so m | a + b; with c := (a+b)/m, p = 4abd' − c and
  1/(abd') + 1/(p·ad'm) + 1/(p·bd'm) = (pm + a + b)/(p·abd'm) = (p + c)/(p·abd') = 4/p.
(⇒) Lemma 0.3 gives p = 4abd' − (a+b)/m, i.e. mp + a = b(4amd' − 1). If d = gcd(a, m) > 1 then gcd(g, d) = 1 and g | (m/d)p + a/d
with g ≡ −1 (mod 4(a/d)(m/d)), so (a/d, m/d) also works. ∎
**S(p) is exactly the union of the two axes**: m = 1 (BN: p + a has a divisor ≡ −1 mod 4a) and a = 1 (B4: mp + 1 has a divisor ≡ −1
mod 4m). In the (U5) language, for a modulus g ≡ 3 (4) with Q = (g+1)/4 the full Type II residue set is
R^{II}_g = { −a·m^{−1} mod g : am | Q } (ratios of divisors of Q, negated); S uses only {−a} ∪ {−m^{−1}}.
Off-axis witnesses are genuinely new: n = 105 has the Type II witness (a, m, g) = (3, 2, 71) (213 = 3·71, 71 ≡ −1 mod 24) although
S(105) fails; n = 4545 has no Type II witness at all (exhaustive: m < 2n suffices since g | n + 4a²k forces m ≤ a + n, a ≤ n/4 + 1).
So there is no algebraic map from off-axis Type II witnesses to axis witnesses (F3 is consistent with this: 105 is rescued by Type II
off-axis, 4545 only by non-Type-II solutions, which for composite n exist outside the prime classification).

Lemma 2.2 (Type I divisor form). For p prime, 4/p has a Type I solution ⟺ **∃ a, w, m ≥ 1: 4aw | mp + 1 and m | 4a²w + 1.**
Proof. (⇒) Lemma 0.4: mp + 1 = 4abw and a + b = d'm; then 4a²w + 1 = 4aw(a + b) − mp ≡ 0 (mod m). (⇐) b := (mp+1)/(4aw);
gcd(m, 4aw) = 1 from m | 4a²w + 1, and 4aw(a + b) = 4a²w + mp + 1 ≡ 0 (mod m), so m | a + b; then x = wd'a, y = wd'b, z = pabw with
d' = (a+b)/m is a solution. ∎   (Both lemmas checked against brute-force enumeration of all solutions for every n ≡ 1 (4), n < 700:
`scripts/z60_lopezt_typecheck.py`, 0 mismatches on primes; on composites the ⇐ directions hold as identities.)

Summary of the landscape (for prime p ≡ 1 mod 4):
  ES(p) ⟺ [∃ a, m: mp + a has a divisor ≡ −1 (4am)]  ∨  [∃ a, w, m: 4aw | mp + 1, m | 4a²w + 1];
  S(p)  ⟺ [∃ a: p + a has a divisor ≡ −1 (4a)]  ∨  [∃ m: mp + 1 has a divisor ≡ −1 (4m)].
All three divisor conditions force (p/g) = −1 for the witness modulus (Type I: (−1/m)(4a²w/m)… the same reciprocity computation),
so every family is empty at odd squares; the step "p is not a square" is used nowhere else.
