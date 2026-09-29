# Wave 34 hostile referee report: DEPTH3, WINDMILL, SIZE_CONJECTURE §4/§0, SIGNED_REFACTOR §8

Reviewer: hostile side agent (branch `side-agent/hostile-review-wave`, merged
up to `wave33-sec77` at a36f3d8). Scope: only the newly claimed
PROVED/CONDITIONAL items. I did not edit the reviewed documents.
Test scripts are in `/tmp/hrev/`. They are reproduced in the appendix in
abbreviated form, and each is self-contained.

## Verdict table

| item | verdict |
|---|---|
| DEPTH3 Thm 1 (escapes of length ≤3) | **CORRECT** |
| DEPTH3 Lemma 5 | **CORRECT** (last paragraph is informal commentary) |
| DEPTH3 Thm 2 (CONDITIONAL on H) | **CORRECT-AFTER-REPAIRS** (presentation only; no mathematical gap found) |
| DEPTH3 Lemma 4, Corollary | **CORRECT** |
| DEPTH3 Thm 3 (sieve exponents) | **CORRECT but badly non-sharp**: the stated exponents are far below what the cited technique (Dahan Lemma 4.2) gives |
| WINDMILL Lemma 1, Prop 2, Lemma 3, Lemma 4, Prop 5, Lemma 6 | **CORRECT** |
| WINDMILL Thm 7 | **CORRECT-AFTER-REPAIRS** (one "=" should be "≤"; §0 says "exactly one" instead of "at most one") |
| SIZE_CONJECTURE Lemmas A, B, E | **CORRECT** |
| SIZE_CONJECTURE Lemma C | **CORRECT-AFTER-REPAIRS** (one unstated coprimality) |
| SIZE_CONJECTURE §0 certificates / checker closure | **CORRECT** (checker sound; independently re-verified 4 certificates) |
| SIGNED_REFACTOR §8 symmetric chart identity `e\|x² ⇔ e\|m²` | **CORRECT** |
| SIGNED_REFACTOR §8 "(2a) reads `(e/p)=sign(e)`" | **FALSE** (counterexample below; correct form given) |
| Pointers / consistency | minor stale statements (list at the end) |

---

## 1. DEPTH3.md

### Theorem 1: CORRECT

I checked every case of the proof line by line:

* **L1.** L1 is exactly `{V1(±d)} ∪ {Type II (t,p(δ-t),p(t²/δ-t))}`. The
  p-free entry of `V1(h)` is `-t(ph-t)/h`, which is negative for both signs of h.
* **Distance 2.** The symmetric form turns the positive quadrant of column
  h into (9). A (9) certificate automatically gives a Type I vertex, because
  a label-0 denominator cannot sit in a Type II vertex.
* **Distance 3.** All four sub-cases are exhaustive: the negative p-free
  entry (F4), `h>0`, `h=-c`, and Type II. The `p∤x` in (A) is automatic,
  since `e|m²` would otherwise give three p-divisible entries. It is harmless.

**Independent numerical check.** `t_thm1.py` is a from-scratch full-graph
enumerator sharing no code with `scripts/`. It uses the incidence model with
`x∈[1,2t]` and verifies every vertex with `Fraction`. For all 179 primes
`p≡1 (4)` with `13≤p<2500`, it checks the following:

* `Pos2` equals the (9)-endpoint set exactly;
* `Pos3` equals `(A∪B endpoints) \ Pos2` exactly, over 3017 layer-3
  positive vertices;
* every A-vertex `(x,-p(pc+t),w)` is an actual vertex;
* every Type II bucket used by B has ≤2 vertices.

No mismatch.

### Lemma 5: CORRECT

`yz=m(m+D)²/(DK²)`, `zw=z²(z+pD)/(Dq_z)` and `mn=z(z+D)²/(Dq_z²)` all check,
as do `m≡1/4`, `q_z≡4z (mod p)`, and `(ℓ/p)=1` for `ℓ|t`. The sentence
"hub quantities built from t cannot supply this sign" is commentary, not a
proved statement. It should not be read as a theorem about all paths.

### Theorem 2 (CONDITIONAL on H): CORRECT-AFTER-REPAIRS (presentation)

I attacked each step named in the brief.

**Lemma 1.**

* The count of `(ℓ-3)/2` residues is right: `24r+1` runs over all residues,
  and `r=0` gives the residue 1.
* A primitive g is nonzero mod ℓ, so it has at most `deg g` roots.
* The transcendental lift is fine, so `C_g` is a finite positive integer, and
  `C_X=C_P=1`.
* At `ℓ=2,3` nothing is avoided, which is fine because only finitely many ℓ
  are affected.

**Lemma 2 (fixed prime divisors, irreducibility, primitivity).**

* **Integrality.** `C_g|M` because `v_ℓ(C_g)<E_ℓ`, and `C_g|g(q̃)`.
* **ℓ∈Λ.** `f_g(y)C_g≡g(q̃) (mod ℓ^{E_ℓ})` and `v_ℓ(g(q̃))=v_ℓ(C_g)<E_ℓ`,
  so `f_g(y)` is an ℓ-unit for every y. This also gives `r_g∉Λ`, which the
  text should say explicitly.
* **ℓ∉Λ.** The leading coefficient `∏lc(g)M^{deg g}/C_g` is an ℓ-unit, and
  `deg∏f_g=Σdeg g<ℓ`. So there is a non-root.
* **Primitivity and irreducibility.** Both are correct.
* **Distinctness.** Distinctness of the `r_g` for large y is correct.

No gap.

**Lemma 3 (fibre closure).** The key points hold.

1. **Divisor sets are q-independent.** At admissible q, `s(q)=∏_{ℓ∈Λ}ℓ^{α_ℓ}∏r_g^{β_g}`
   is a genuine prime factorisation. The primes are distinct, the `r_g` lie
   outside Λ, and the Λ-exponents are frozen by `E_ℓ`. So the signed divisors
   of `s²` are exactly the values of the finitely many formal divisors, in
   bijection with exponent vectors.
2. **Integrality is q-independent.** `y=(D+s)/r` has a formal factorisation
   `κ∏ℓ^α∏r_h^β`. Its value is an integer iff all exponents are ≥0, again
   because the primes are distinct. The same holds for the reduced form `r/s`
   (exponent minima).
3. **Signs stabilise.** The sign of a formal number is `sign(κ)`, because
   every `h∈𝒫` has positive leading coefficient and `h(q)>0` for large q.
   Also `D+s` vanishes for only finitely many q unless it is identically 0,
   and that case is excluded.
4. **Rounds with enlarging (S,Λ).** Admissibility is monotone:
   * `C_g` is fixed by q*;
   * the E's only grow;
   * "prime outside Λ'" implies "prime outside Λ";
   * thresholds are maxima.

   So applying Lemma 3 to every coordinate of every member of `𝒱_j` and
   taking unions gives `𝒱_{j+1}`. The induction on distance is sound.

**§3.3 characters.**

* **ℓ∈Λ.** `(2/p)=1` since `p≡1 (8)`, and `(3/p)=1`. For `ℓ≥5`,
  `(ℓ/p)=(p/ℓ)=((24q*_ℓ+1)/ℓ)=1`.
* **g≠P.** `24^{deg g}g(q)≡H_g (mod p)`, `(24/p)=1`, and the primes of
  `C_g` and `H_g` lie in Λ. Hence `(r_g/p)=1`.
* **H_g≠0.** It holds because `24X+1∤g`.
* **The vertex.** p enters a formal vertex only through `β_P`, and `β_P`
  is its exact p-valuation. So the same-valuation pair A,B has `(AB/p)=+1`,
  and (2a) forbids positivity.

**Consistency test.** I checked the scheme against the unconditional forced
branches of Lemma 4(5).

* **Mod 5.** `q*_5≡2` is forced, since `(ℓ-3)/2=1`. If `5∉Λ`, then
  `q≡4 (mod 5)` would give `p≡2 (5)` and dist 2. But then `5|21q+1`, where
  `21X+1∈S_1` comes from `h=2`, while `5∤C_{21X+1}`. So `r_{21X+1}` would
  not be prime. The contradiction is avoided exactly as the theory predicts.
* **Mod 7.** The same happens with `23X+1` (`h=6`).

**Repairs (presentation, not mathematics).**

1. The "threshold depending only on (S,Λ)" must be allowed to depend on the
   finite list of formal expressions built in Lemma 3 (the `D+s` and signs).
   Say "depending on the construction through round k".
2. In §3.3, `p∤H_g` is automatic, because every prime of `H_g` is in Λ and
   `p=r_P∉Λ`. The appeal to "q large" is unnecessary.
3. In Lemma 2, state explicitly that the ℓ-unit property gives `r_g∉Λ`.
4. In Lemma 3, say that non-integral formal triples are discarded, and
   that the new `h_i` may coincide with old members of S ("adjoin" = union).

**Novelty relative to Schinzel / EST / BL / Dahan.** Theorem 2 is correct,
and it is **not** a restatement of Schinzel's theorem.

* Schinzel (and EST Prop 1.6, BL Cor 1.4) rule out *identities*, that is,
  methods blind to the factorisation of the numbers met.
* Theorem 2 rules out, under H, bounded-depth searches that *do* factor.
  H forces every number met to factor "formally".

However, the mechanism is the one EST state informally on p. 5 of
arXiv:1107.1010 (archived in `sources/`): "one can only use methods that
must necessarily fail when p is replaced by an odd square … rules out
… a finite set of covering congruence strategies". The profinite base point
q* makes p a local square at every prime that is ever met. This is the
H-conditional incarnation of that "odd-square" principle, with the
Bright–Loughran class as the invariant. Two related results should be cited
next to it:

* Dahan (arXiv:2608.24035) Prop 3.8 and Thm 4.14, unconditional
  obstructions for specific depth-J branches;
* Pomerance–Weingartner, for large m.

I found no prior source stating the graph-distance version, so priority
cannot be excluded or confirmed. **Assessment:** a clean, correct,
folklore-level corollary, best presented as a Proposition with the EST
odd-square remark and Schinzel/BL cited as its source of ideas. It should
not be a headline theorem. DISCOVERIES (G)7 already says "novelty
unchecked", and it should add the EST p. 5 remark.

### Lemma 4 and Corollary: CORRECT

All five table rows and items (1)–(4), (6) check by hand.

* `t≡3,4 (5)` and `t≡4,1,3 (7)` hold in the respective classes.
* The divisibilities `5|3t+1`, `5|7t+2`, `21|23t+6`, `21|11t+3`, `14|15t+4`
  hold.
* The congruences `5≡-1 (3)`, `5≡-2 (7)`, `63≡-6 (23)`, `63≡-3 (11)` and
  `m/14≡-4 (15)` hold.
* `h|t²` holds in every row.

`t_lemma4.py` verifies each certificate as an exact positive rational
identity for **all** 74416 primes `p≡1 (4)` below `2·10^6`. The primes left
over are exactly the 4519 in `p mod 840∈{1,121,169,289,361,529}`.

It also recomputes `κ₂=1.02315`, and it confirms that there are no off-axis
forced constant edges with `0<|a|,|h|≤200`.

(Lemma 4(2) "(a,h)=(d,0)": `p∤t+d` holds automatically for `d|t²`, by the
valuation lemma.)

### Theorem 3: CORRECT as stated, but the exponents are far from sharp

**The proof is fine.**

* Classes: `ℓ|ph-t ⇔ p≡-(4h-1)^{-1}` and `ℓ|t+d ⇔ p≡1-4d (mod ℓ)`.
* Coincidences only at `ℓ|4(h-h')`, `ℓ|8h(2h-1)`, or
  `ℓ|(1-4d)(4h-1)+1≠0`.
* The class 0 never coincides with a branch class for ℓ outside the moduli.
* `1+ω(ℓ)≤10<ℓ` for all sieving primes; 5, 7, 11, 13, 23, 47, 71 divide
  moduli and are excluded.
* Selberg's upper bound at dimension `1+κ` needs only a trivial level for
  integers in APs.

**But the dimension is badly underestimated.** Each branch is counted with
weight `1/φ(4h-1)`, as if it needed a *prime* `ℓ≡-1/4`. Branch h fails iff
no divisor of `m²` lies in `c=-1/4 (mod K)`.

* Let R be the set of residues mod K of the primes of m.
* If `r` and `c/r` are both in R, then `ℓℓ'` or `ℓ²` is a divisor in class
  c.
* So R avoids `cR^{-1}` and the fixed points of `r↦c/r`. Hence
  `|R|≤φ(K)/2`.
* Summing over the finitely many admissible R gives a sieve of dimension
  `≥1/2` per branch.

This is exactly Dahan's Lemma 4.2 / Thm 4.3 (`≪N(log N)^{-1-|P|/2}`), which
the Remarks already cite for `h=1`. It gives
`#{dist>2}≪N/(log N)^{1+9/2}`. For dist>5, it gives exponent `1+9`, since the
X-branch also accepts any divisor D, not just a prime.

The data agree with the larger exponent. The cumulative distance-3 counts
7572 (`<10^11`) and 44197 (`<10^12`) give a local exponent of about 6.2 for
`N/(log N)^A`, not 2.02.

**Repair.** Either restate Theorem 3 with the half-dimension (and credit
Dahan Thm 4.3), or label 2.02/3.04 as "a crude bound". The Remark
"Does the exponent `c_k` tend to infinity?" uses `c_k` without defining it.
With Dahan's trick, the natural exponent is `1+(#forced branches)/2`.

---

## 2. WINDMILL.md

* **Lemma 1: CORRECT.** Trivial parity. The matching paragraph is
  informal but right.
* **Prop 2: CORRECT.**
  * The quartic part forces a monomial A with ±1 entries.
  * Cubic monomials force `β=0`.
  * The linear part forces `π(k)=k` (since `p≠±1`), `{a,b}` stable, and
    `ε_c=1`.
  * The Type I case is the same, because the coefficient ±1 now sits on k.
* **Lemma 3: CORRECT.** For p-free `x>p/4`, `gcd(4x-p,px)=1`.
  Complementation preserves both classes. Its only fixed point, `D=s`,
  lies in the `+s` class because `r∤2s`. The counts `N^+/2` and
  `(N^--1)/2` are verified at every `x∈(t,2t]` for all 211 primes
  `p≡1 (4)` below 3000 (`t_wm.py`).
* **Lemma 4: CORRECT.**
  * The first case needs `2x-p∈{±1}`. The listed `±p` values are
    impossible anyway because `p∤x`; harmless.
  * The second case gives `m=-2t`.
  * Verified on all vertices for `p<3000`.
* **Prop 5: CORRECT.**
  * The fixed points of the swap are the three `(2x-p)(2z-p)=p²` points, all
    with odd z.
  * The z-even part equals `6f` by Lemma 4.
  * Verified at nine primes `p≡1 (24)`, 73–457: `|S_112|` is odd and the
    z-even count is `6f`. Also `f(97)=8` and `f(193)=6` as claimed.
* **Lemma 6: CORRECT.**
  * The inequality `(t+a)(pH+t)>2t((4a-1)H+a)` follows from
    `(t+a)(4t+1)-(8at-2t)=4t(t-a)+3t+a>0` and `t(t-a)≥0`.
  * Verified on all Type I vertices for `p<3000`.
* **Theorem 7: CORRECT-AFTER-REPAIRS.** I checked every inequality:
  * `A∈[4t+3,3p-4]`;
  * `f≤(x+z)/3≤2t` and `|f|≤6t`;
  * `A(x_P-x_N)≤8t<2A` forces `x_P=x_N+1`;
  * `|f_N|≥2t+3` excludes `H_N≤-5`;
  * the formula `f_P=λγ(4β-γ)-1`;
  * `gcd(f_P,w)=1` and `f_P≡-1 (λ)`, which give `f_P|β²`;
  * the quarter-discriminant `k(λγ²M-1)`, `M=4kλ-1`.

  **Jacobi step.** `(2|M)=1` when `2|k`, since `M≡7 (8)`. Also
  `(k'|M)=(M|k')(-1)^{(k'-1)/2}=(-1|k')(-1)^{(k'-1)/2}=1`, because
  `(M-1)/2` is odd. With `(-1|M)=-1`, a square `≡-k` is impossible, since
  `gcd(k,M)=1`.

  **Numerical checks.**
  * Brute force over `λ<60`, `α<β<1500` finds no `f_P|β²` (`t_vieta.py`).
  * All 41235 p-free buckets outside `[1,2t]` for `p<3000` are singletons.

  **Repairs.**
  1. In the "both nonpositive" case, `|f₂|=x₁+z-A` should read
     `|f₂|=x₁+z-A(x₂-x₁)≤x₁+z-A`. The conclusion is unchanged.
  2. §0 item 6 says "lies in exactly one signed vertex". It should say "at
     most one", as Theorem 7 and SIGNED_REFACTOR §5 do.

---

## 3. SIZE_CONJECTURE.md §4 and §0

* **Lemma A: CORRECT.**
* **Lemma B: CORRECT.**
  * `q=-M` and `p≡4 (M)`.
  * Only `f=-d` survives among `±d,±pd`, for `k≥2`.
  * `m=(d-x)/M` and the third entry `px(x-d)/(Md)` are Type II.
  * Complementation is the swap. There are `(τ(x²)-1)/2` vertices, each
    with one negative entry.
* **Lemma C: CORRECT-AFTER-REPAIRS.**
  * The two identities in (i) hold.
  * (ii): `Kx-pμ=d`, and all D share the class `-pμ≡d (mod K)`. `D|μ²`
    suffices, since `gcd(D,K)=1` gives `D|μy`.
  * `D=-4dμ` gives `y=x-d`.
  * **Repair.** The final "iff `w≡1 (mod 4)`" needs `4M|w-1`. `M|w-1`
    follows from `M|d(w-1)` only because `gcd(d,M)=1`, which holds under
    Lemma B's hypothesis. State it.
* **Lemma E: CORRECT.**
  * Anchor part: flipping `d→ℓ^{±1}d` changes the sign class, and `f'>0`
    gives a positive vertex.
  * Bucket part: the symmetric chart gives `e'|(t+a')²` and
    `e'|(t+a')m`.
  * `p∤t+a'` and `p∤m'` hold by the valuation lemma.
  * The `ℓ^j` remark holds because `j≤v_ℓ(x)` makes the division legal.
  * (The lemma restricts `a≤t`; the §0/SR §8 paraphrase drops that. The
    proof works for any p-free `x>p/4`, so this is harmless.)
* **§0 certificates / checker: CORRECT.** I read
  `scripts/sterile_certificate_check.py`, `pointwise_fibres.py` and
  `pointwise_fibres_big.py` critically. The closure loop runs over
  **every** denominator occurring in S, dispatched on its type as follows.
  * **p-divisible with label 0 (Type I).** Scan or MITM (A,B), plus an
    independent generic fibre or pruned DFS (C).
    * The interval `a∈[max(1-t,-bound),min(t,bound)]` is complete: every
      vertex has a p-free chart coordinate in `[1,2t]`, and `|e|≤x²`.
    * The MITM targets `{-h,h} mod |H|` are right.
    * DFS pruning at `E≥4t²` is valid.
  * **Type II.** The two-candidate rule is proved: the non-central
    representatives lie within `2p/(9p+3)<1/4` of `pm/K`.
    `D|m² ⇔ D|mx` given `p∤x`.
  * **p-free in `[1,2t]`.** Two methods, which must agree.
  * **Outer p-free (`z<0` or `z>2t`).** Interval (10); `x>0` is forced in
    both sub-cases.
  * **`p²|z`.** Empty.

  Closure plus connectivity plus nonpositivity gives an entire sterile
  component. The single-method Type I buckets (11 in the seed certificate)
  are disclosed.

  **Independent re-checks.**
  1. The shipped checker passes on `p165426666927637` and
     `p1960717994383909_random` (15 s).
  2. My own generic fibre code (reduced `r/s`, all signed `D|s²`, FLINT
     factorisation, no shared code) confirms closure of the 398-, 339-, 412-
     and 409-vertex certificates. The 3/17/45/48 skipped denominators, with
     `τ(s²)>2·10^6`, are all outer, Type II or double-method Type I.
  3. **Mutation test.** Deleting one leaf vertex from the 398-vertex
     certificate makes the checker fail with "fibre leaves S".
  4. The 30035-vertex and seed certificates at `p=274159709010072908384347957`
     were run with the shipped checker; see the addendum at the end.

---

## 4. SIGNED_REFACTOR §8

**The identity `e|x²⇔e|m²` is CORRECT.**

* The substitutions `x=(p+A)/4`, `m=(pH+1)/4` and `e=(AH-1)/4` reproduce
  `x=t+a`, `m=ph-t` and `e=4ah-a-h`.
* `Hx=m+e` and `AH-4e=1` hold.
* Hence `gcd(H,e)=1`, and `e|x²⇔e|H²x²=(m+e)²⇔e|m²`.
* It is also verified implicitly by `t_thm1.py`: A-vertices built from
  `d|(pc+t)²` are actual vertices.

**The sentence "In these terms (2a) reads: for `e|x²` with `e≡-1/4
(mod 4x-p)`, `(e/p)=sign(e)`" is FALSE.**

* **Counterexample 1.** `p=13`, positive vertex `(4,18,468)`: `x=4`,
  `a=1`, `h=3`, `e=8`. Here `(8/13)=-1` but `sign(e)=+1`.
* **Counterexample 2.** `p=13`, vertex `(-36,3,468)` in chart `x=3`: `a=0`,
  `h=3`, `e=-3`. Here `(-3/13)=+1` but `sign(e)=-1`.
* **Scale.** 460 of 653 chart pairs with `x∈[1,2t]` violate it at 13 small
  primes (`t_sign.py`).

**Correct statement.** Put `xw` for the p-free pair. Then `(xw/p)=(m/p)(e/p)=(e/p)`,
since `m≡1/4 (mod p)`. So

* `(e/p)=-1` iff the vertex is all-positive;
* equivalently, for `x>t`: `(e/p)=-sign(e)`, since `sign(e)=sign(h)` when
  `a≥1`;
* for `1≤x≤t`: `(e/p)=+1`.

This is verified with no violations on 18880 chart pairs for all `p<1500`
(`t_sign2.py`). The false sentence is not used in any proof: the scripts use
only the divisibility identity. It must still be corrected.

---

## 5. Consistency and pointers

1. **DEPTH3 §1.** "For `z>2t`, the fibre has at most two vertices" is stale.
   By WINDMILL Thm 7 and SR §5 it has at most one.
2. **DISCOVERIES.md (G)4.** It cites only SR §5 for the singleton bounds. It
   should add WINDMILL Thm 7 (the `2t<z<p` case).
3. **Missing ledger entries.** Neither DISCOVERIES.md nor PROJECT.md records
   WINDMILL (Thm 7, the negative parity verdict) or SIZE_CONJECTURE (size
   conjecture refuted in practice; Lemmas A–E). The only pointer is
   SR §8(ii).
4. **DISCOVERIES (G)8.** Mark the Theorem 3 exponents as non-sharp, per §1
   above, and add Dahan Thm 4.3 as the source of the half-dimension.
5. **DISCOVERIES (G)7.** Add EST p. 5 ("methods must fail for odd squares")
   as the informal antecedent of Theorem 2.
6. **SR §7.** The pointer to DEPTH3 Thm 2 and the counts (44197,
   `p<10^12`) are consistent with DEPTH3 §5: 70+1306+6196+36625=44197.
7. **SIZE §0.** The 122/126 count matches the §3.4 table.

## Appendix: test scripts (in /tmp/hrev)

| script | purpose |
|---|---|
| `graph.py` | independent full signed graph via incidence model, every vertex checked by `Fraction` |
| `t_thm1.py` | Theorem 1: Pos2 = (9) endpoints and Pos3 = (A∪B)∖Pos2, for all `p≡1 (4)`, `13≤p<2500` |
| `t_lemma4.py` | Lemma 4 / Corollary for all `p<2·10^6`; κ₂; off-axis forced edges |
| `t_wm.py` | WINDMILL Thm 7, Lemma 6, Lemma 4 and Lemma 3 counts for `p<3000`; Prop 5 and f(p) at nine primes |
| `t_vieta.py` | Thm 7 mixed-case Diophantine condition, brute force |
| `t_sign.py`, `t_sign2.py` | SR §8 sign claim (false) and its corrected form |
| `t_cert.py`, `t_skip.py`, `t_mut.py` | independent certificate closure, skipped-denominator types, mutation test |
