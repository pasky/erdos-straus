# Hostile review: FORMAL_CLOSURE.md (Theorem F, conditional failure of the seed-component conjecture)

Reviewed at `wave33-sec77` (HEAD `7ee2622`). Reviewed files were not edited.
Own code (does **not** import `scripts/formal2*.py` / `formal_closure*.py`; reads only the JSON data):

* `scripts/review_fc_common.py`: data loading, own CRT for `q0`, own `C_g`, formal polynomials.
* `scripts/review_fc_global.py`: all-vertex and all-S checks, (C3), connectivity. Output: `reviews/review_fc_global.json`. Runtime 45 s.
* `scripts/review_fc_fibres.py`: own formal-fibre engine. It was run on **all 9961** non-dead denominators, not just a sample (`--all`). Output: `reviews/review_fc_fibres_all.json.gz`. Runtime 12 min on 8 cores.
* `scripts/review_fc_realq.py`: tests the *logic* of §1.1 against brute force at real q, and brute-forces SR §5/WINDMILL Thm 7 at small p. Output: `reviews/review_fc_realq.json`.

## Verdict summary

| item | verdict |
|---|---|
| §1 Basic fact, §1.1 fibre recipe ("divisors of s(q)² = values of formal divisors", (A), (B), E_ℓ) | **CORRECT** (minor unstated steps, see L2–L4) |
| Proposition 1: induction, dead denominators, signs | **CORRECT** |
| (C4) ⇒ nonpositivity; "formal set = exactly the seed component" | **CORRECT** |
| Proposition 2 (H ⇒ infinitely many admissible q) | **CORRECT** ("= DEPTH3 Lemma 2" is loose, see L5) |
| §2.3: aux polynomials need not be prime (BH exponent 6402) | **CORRECT** (argument should say more, see L3) |
| Certificate: S, C_g, E, q0, X,P∈S, C_X=C_P=1, seed present | **CORRECT** (verified) |
| Certificate: all vertex identities, formal integrality, negative entry, dead classification | **CORRECT** (verified, all 7883) |
| Certificate: (C1) closure, i.e. fibres of non-dead Z recomputed independently | **CORRECT**: 9961/9961 equal |
| Certificate: (C2) c_r primes ⊂ Λ, aux ⊂ S, precision for (B) | **CORRECT** (verified for every candidate passing (A)) |
| (C3) no fixed prime divisor | **CORRECT**: all 1271 primes ℓ∉Λ, ℓ≤17631 checked, not just a spot check |
| **Theorem F overall** | **CORRECT** (conditional on H, as stated) |

I found no error that affects the theorem. The remarks below are about presentation.

## 1. Logic

**Fibre recipe.** At z=Z(q), every vertex is (z,y,w) with 1/y+1/w=N(q)/(P(q)Z(q)).

* For **any** pair of integers (r(q),s(q)) with that ratio, (ry−s)(rw−s)=s². So reducedness at q is indeed irrelevant.
* With s=c_s∏(g/C_g)^α, s involves only P and the polynomials of Z, all of which are entry polynomials.
* At admissible q, s(q)=c_s∏r_g^α with r_g pairwise distinct primes, each larger than |c_s|. So the divisors of s(q)² are exactly ±d∏r_g^j with d|c_s² and j≤2α. Primes of c_s outside Λ are harmless: they are fixed, and r_g eventually exceeds them.
* D=−s is the only divisor giving a zero denominator. D(q)=−s(q) forces formal equality, by unique factorisation at admissible q.
* y=w (D=±s self-paired) needs no special treatment.

**(A) necessity.** I re-derived it. If D+s=h^j·k with j<β and h∤k, then integrality forces r_h^β | C_h^j r_h^j·k(q), where r_h=h(q)/C_h.

* r_h is Λ-free and den(k)=den(D+s) is Λ-supported (Gauss). So for every prime π: v_π(d_k k(q)) ≥ v_π(r_h).
* With u·h+v·d_k k=Res (u,v∈Z[X]), this gives r_h | Res≠0. That is impossible once r_h is large.

Only r_h→∞ and Λ-freeness of r_h are used, not primality. This also holds for composite (aux) r_h, which justifies §2.3.

**(B) sufficiency/necessity given (A).**

* (D+s)(q)=K·∏r_h^β, with K=k(q)∏C_h^β∈Z. K is integral because its denominator is Λ-supported and r_h is Λ-free.
* gcd(c_r, r_h)=1, because c_r is Λ-supported by (C2) and r_h is Λ-free (E_ℓ>v_ℓ(h(q0)) for the aux h, which are in S).
* Hence y∈Z ⇔ c_r | K ⇔ c_r | (D+s)(q).
* With F=den·(D+s)∈Z[X], this is F(q)≡0 mod ℓ^{v_ℓ(c_r)+v_ℓ(den)}. So E_ℓ≥v_ℓ(c_r)+v_ℓ(den) suffices. The E_ℓ formula is right.
* It must hold for every candidate that passes (A), including those rejected by (B). I checked exactly this (below).
* Nothing q-dependent is hidden:
  * all denominators of formal numbers are C_g's, so Λ-supported;
  * "z p-free" just means the exponent of P is 0, and p∤c for large q;
  * r(q)≠0 because 4z≠p.

**Proposition 1.** Every neighbour of the value of V∈𝒱 shares the value of some entry Z of V.

* Dead Z: z is p-free and outside [1,2t]. So, by SR §5 (z<0) and WINDMILL Thm 7 (z>2t), its fibre is {v}.
  * I re-read the Thm 7 proof, including the Jacobi step: (−k|M)=−1 with M=4kλ−1. I also re-derived the SR §3 fact used in the setup (two p-free denominators of a vertex cannot both lie outside [1,2t]).
  * Brute force: for all p≡1 (4), p<400, every p-free z∈[−4000,−1]∪[2t+1,4000] has ≤1 signed vertex. That is 287,662 buckets with 0 violations.
* Non-dead Z: the recipe above together with (C1).
* Signs: every g∈S has lc>0 and C_g>0, so the value of a formal integer has the sign of its constant for large q. Then (C4) gives nonpositivity.
* "Exactly the seed component": each formal vertex is an actual vertex at admissible q (nonzero integer entries, identity in Q(X)). 𝒱 is one component under shared formal denominators, and distinct formal denominators have distinct values. I verified the single-component claim independently.

**Proposition 2.**

* f_g=g(My+q0)/C_g has integer coefficients, because C_g | M (v_ℓ(C_g)<E_ℓ).
* Primitivity:
  * at ℓ∈Λ, the constant term is an ℓ-unit;
  * at ℓ∉Λ, y↦My+q0 is invertible over Z_(ℓ), so the content of g is preserved.
* Irreducible, lc>0.
* No fixed prime divisor:
  * ℓ∈Λ: f_g≡g(q0)/C_g is a unit mod ℓ.
  * ℓ∉Λ, ℓ≤Σdeg: by (C3), since ℓ∤M and ℓ∤C_g.
  * ℓ>Σdeg: the product is primitive, hence nonzero mod ℓ, with at most Σdeg<ℓ roots. This also covers primes dividing leading coefficients.
* The values r_g are distinct for large y, since distinct primitive positive polynomials are non-proportional.
* r_X=q and r_P=p, since C_X=C_P=1.

**§2.3.** Only entry polynomials enter s, and hence the divisor enumeration. The y,w are formal over entry polynomials only. Aux values are used only through (A), which needs r_h→∞, and through gcd(c_r,r_h)=1, which needs Λ-freeness. Neither needs primality. An aux value that shares a prime with s(q), or with another r_g, only makes r(q)/s(q) non-reduced, which is irrelevant. It cannot share a prime with c_r, because c_r⊂Λ and r_h is Λ-free. (C3) for the entry subfamily is implied by (C3) for S. **Correct.**

### Minor remarks (no effect on validity)

* **L1.** §3 lists `lam_final.json` and `closure_final.json.gz` as the files, but the compact `certificate.json.gz` (q0 mod ℓ^E, S, vertices) is not mentioned. I used it as the primary certificate. It agrees with the others:
  * its S and C_g are identical to `closure_final`'s;
  * its vertex set is identical as a set;
  * `qt≡q0 (mod ℓ^{E_ℓ})` for all 2036 ℓ;
  * the `lam_final` residues are given to precision ≥E_ℓ.
* **L2.** §1.1 does not fix the normalisation of the constants of (r,s). Any common integer scaling gives the correct fibre, but (C2) ("primes of c_r in Λ") depends on it. With gcd(c_r,c_s)=1, which is what I used, (C2) holds for all 9961 fibres. This should be stated.
* **L3.** The step "(B) ⇔ c_r | (D+s)(q)" silently uses gcd(c_r, r_h)=1 (via (C2) and Λ-freeness of aux values) and integrality of K. The "Basic fact" (ℓ∤g(q) for fixed ℓ∉Λ) is false for composite aux values. It is not used for them, but §2.3 should say why: c_r⊂Λ. §2.3's requirement "(C3) for aux h" is unnecessary but harmless.
* **L4.** The (A) proof's "v_π(n)≤v_π(Res)" needs v_π(d_k k(q))≥v_π(n). That follows from gcd(n, C_g d_k)=1, which is unstated.
* **L5.** "Proposition 2 (= DEPTH3 Lemma 2)": DEPTH3's version puts every prime ≤Σdeg and every prime dividing a leading coefficient into Λ. FC replaces this with (C3). FC's own proof is correct (see above), so "=" should read "cf.".

## 2. Independent computation

**Global** (`review_fc_global.py`). q0 was rebuilt by my own CRT from `q0_mod`: 12088 digits, E_max=17.

* **S:** 13521 polynomials, Σdeg 17631; 9411 linear and 4110 quadratic.
  * All are primitive, irreducible (flint) and have lc>0.
  * C_g was recomputed from q0 and matches in 13521/13521 cases.
  * v_ℓ(g(q0))<E_ℓ for every g and ℓ.
  * X, P ∈ S with C_X=C_P=1.
* **Entry polynomials:** recomputed from the vertices: 6402 of them, Σdeg 7795. The flags match.
* **Vertices:** all 7883 are distinct.
  * The identity P(ab+bc+ca)=4abc holds exactly in Q[X] for all of them.
  * All are formal integers over S with nonzero integer constants.
  * Every vertex has a negative-constant entry.
  * The seed (6X,−12XP,−12XP) is present.
* **Denominators:** 8412 p-divisible, 1549 anchors, 5726 dead, matching the claim.
  * Every p-free one is classified as dead (negative, or eventually >12X) or anchor.
  * No dead Z occurs in more than one formal vertex. A violation would have contradicted Thm 7.
* **Connectivity:** one component.
* **(C3):** all 1271 primes ℓ∉Λ with ℓ≤17631 have a residue that is a root of no g∈S. 0 failures.

**Fibres** (`review_fc_fibres.py --all`). The engine was written from scratch. For each non-dead Z:

1. Compute N=4Z−P and cancel factors of PZ to get r/s. Factor r=κ∏h^β.
2. Recompute C_h for each h from q0, checking v_ℓ(h(q0))<E_ℓ.
3. Take coprime integer constants c_r, c_s, and enumerate all formal divisors D of s².
   * If r has a nonconstant factor h0, the constant of D is pinned by its monomial via D(θ)=−s(θ), and must be an integer divisor of c_s². This is exact.
   * Otherwise all d|c_s² and both signs are enumerated.
4. For each D, test (A) exactly in Q[X] and (B) at q0 modulo c_r. For **every** candidate passing (A), check v_ℓ(c_r)+v_ℓ(den(D+s))≤E_ℓ for every ℓ|c_r.
5. Require both D and s²/D to be accepted, and factor y and w over S with integral constants.

Results:

* 9961/9961 fibres are **equal** to the certificate's vertex sets: 8412 p-divisible and 1549 anchors, including the seed's neighbours and the largest fibre (2551 vertices).
* 17921 vertex incidences were compared.
* 533,011,471 candidates passed (A). Of the 9961 fibres, 8491 have c_r≠±1, so (B) is non-trivial there.
* 0 precision failures, 0 primes of c_r outside Λ, 0 aux factors outside S, 0 aux precision failures, 0 non-S or non-integral y/w, 0 exceptions.

This covers the requested stratified sample of ≥200 (it is the full set).

**Logic vs. ground truth** (`review_fc_realq.py`). This tests the recipe itself, not the code.

* I took 16 non-dead fibres (pdiv and anchors, 11 with c_r≠±1), including Z=6X and fibres of size 121 and 81.
* For each, I chose a real q ≡ q0 modulo ℓ^{E_ℓ} for the Λ-primes relevant to that fibre (M'≤10^45), with all s-polynomial values prime and distinct.
* The actual fibre of z=Z(q) was computed by brute force over all divisors of s(q)² and compared with the certificate's formal vertices evaluated at q.
* 16/16 equal (221 vertices).

## 3. Specific questions

* **Fixed prime divisor at ℓ∈Λ:** impossible, because v_ℓ(g(q0))<E_ℓ for all g∈S (verified), so f_g≡unit mod ℓ.
* **C_X=C_P=1 and X,P∈S:** verified.
* **Seed present:** verified.

## Conclusion

Theorem F holds as stated: conditional on H for the 13521-member family, or for the 6402 entry polynomials by §2.3. The certificate satisfies (C1)–(C5) by fully independent recomputation. The remaining issues L1–L5 are about how the argument is written up, not about the mathematics.
