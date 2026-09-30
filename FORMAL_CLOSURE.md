# The formal seed component closes: under Hypothesis H the seed-component conjecture is false

Notation of [SIGNED_REFACTOR.md](SIGNED_REFACTOR.md) and [DEPTH3.md](DEPTH3.md) §3:
`p=4t+1` prime, signed vertices `4/p=1/x+1/y+1/z`, edges = shared denominators, the
seed `σ=(t,-2pt,-2pt)`. Here `p=24q+1`, `t=6q`, `P(X)=24X+1`. Labels: **PROVED**,
**CONDITIONAL** (proved from a named hypothesis), **CERTIFIED** (exact finite computation,
re-checked by an independent script), **EVIDENCE**.

## 0. Result

**Theorem F (CONDITIONAL on Schinzel's Hypothesis H for one explicit finite family).**
There is an explicit set `S` of 13521 primitive irreducible polynomials in `Z[X]` (degrees
1 and 2, `X, 24X+1 ∈ S`), an explicit modulus `M` and class `q0 mod M` such that, if the
13521 polynomials `f_g(y)=g(My+q0)/C_g` take simultaneously prime values for infinitely
many y, then for infinitely many primes q with `p=24q+1` prime **the seed component of
p contains no all-positive vertex**. The seed component is then the set of values of an
explicit list of 7883 formal vertices, all nonpositive.

* Consequently the **seed-component conjecture** ("the seed component always contains a
  positive vertex", SIGNED_REFACTOR) is **false under H**. Under Bateman–Horn for the
  same family the counterexamples `p≤N` number `≫N/(log N)^{13521}`.
* **Refinement (PROVED, §2.3):** only the 6402 polynomials that occur in vertex entries
  need to be prime (Σdeg 7795); the other 7119 (factors of `4Z−P`) need not. So the BH
  exponent can be taken to be **6402**.
* The family is so large that no example is within computational reach, and none of this
  touches ES itself (nothing here decides whether these p have positive solutions;
  if they do — as ES predicts — those lie in other components). Informally (not a formal metatheorem): an unconditional proof of the
  seed-component conjecture must use some property of p that fails for a
  "formally generic" p of this shape, i.e. it cannot rest on congruence data plus
  the shape of factorisations alone — the Elsholtz–Tao odd-square principle, now for
  the whole component rather than a bounded ball (DEPTH3 Theorem 2). Since H is
  widely believed, the conjecture should (heuristically) be regarded as false.

The certificate is `data/formal_closure/` (§3); the checks are
`scripts/formal2_verify.py` (§3.2).

## 1. What must be certified (PROVED)

Let `𝒫` be the primitive irreducible polynomials with positive leading coefficient.
A **certificate** consists of

* a finite `S⊂𝒫` with `X,P∈S`;
* a finite set of primes `Λ`, exponents `E_ℓ`, and a class `q0 mod M=∏_{ℓ∈Λ}ℓ^{E_ℓ}`
  with `E_ℓ>v_ℓ(g(q0))` for all `g∈S`; put `C_g=∏_{ℓ∈Λ}ℓ^{v_ℓ(g(q0))}`;
* a finite set `𝒱` of **formal vertices**: triples of formal integers
  `c·∏_{g∈S}(g/C_g)^{e_g}` (`c∈Z∖0`, `e_g≥0`) satisfying `1/a+1/b+1/c=4/P` in `Q(X)`,

subject to the conditions (C1)–(C5) below. An integer q is **admissible** if
`q≡q0 (M)`, every `r_g:=g(q)/C_g` (`g∈S`) is a prime outside Λ, the `r_g` are pairwise
distinct, and q exceeds a threshold depending only on the certificate.

**Basic fact.** At admissible q, `g(q)=C_g r_g` with `C_g` Λ-supported. Hence for every
*fixed* prime `ℓ∉Λ` (e.g. any prime of any of the finitely many constants that occur)
and `g∈S`, `ℓ∤g(q)` once q is large (then `r_g>ℓ`). So the factorisation of the value of a
formal integer is `c·∏r_g^{e_g}` *for every prime*, and the ℓ-adic valuation of a
polynomial expression whose factors lie in S is that of its rational constant.

### 1.1 The formal fibre

Let Z be a formal integer. Put `N=4Z−P`, factor `N=κ∏h^{e}` over Q, and let
`r/s=N/(PZ)` after cancelling the formal gcd, `s` with positive constant. Every vertex of
the graph of p containing `z=Z(q)` is `(z,y,w)` with `1/y+1/w=r(q)/s(q)`; then
`D=r(q)y−s(q)` satisfies `(ry−s)(rw−s)=s²`, so **D divides `s(q)²`** (reducedness of `r/s`
at q is not needed). Since the polynomials of s lie in S, the divisors of `s(q)²` are
exactly the values of the finitely many formal divisors `D=±d∏(g/C_g)^{j_g}` (`d|c_s²`,
`0≤j_g≤2e_g`). The divisor `D=−s` gives `y=w=0` and is excluded. For each other D the
candidate is `y=(D+s)/r`, `w=(s²/D+s)/r`. At admissible q
(large) the candidate is integral iff

* **(A)** `g^{β_g} | D+s` in `Q[X]` for every g occurring in r with exponent `β_g`, and
* **(B)** `c_r | (D+s)(q)`, the constant of r.

(A) is q-independent: if `D+s=g^j k`, `j<β`, `g∤k`, then `n=g(q)/C_g` (Λ-free) would
satisfy `v_π(n)≤v_π(Res(g,d_k k))` for every prime π, i.e. `n≤|Res|`, impossible for
large q. (This uses only `n→∞`, not primality of `g(q)/C_g`.)
(B) at a prime `ℓ∈Λ` is decided by `q mod ℓ^{E_ℓ}` once `E_ℓ≥v_ℓ(c_r)+v_ℓ(den)`,
`den` the Λ-denominator of `D+s`. At a prime `ℓ∉Λ` of `c_r` it depends on `q mod ℓ`
unless all factors of `D+s` lie in S. **This is the "accidental-prime" gap left by the
previous agent**: factors of *rejected* candidates were not in S, so such rejections were
not justified. The certificate closes it by condition (C2):

* **(C1) closure.** For every denominator Z of every member of 𝒱 which is not *dead*,
  every candidate `D≠−s` satisfying (A) and (B) gives a triple `(Z,y,w)∈𝒱` (y, w formal
  integers over S). *Dead* means p-free and (negative, or `Z>12X` eventually: degree ≥2,
  or degree 1 with `lc>12` or `lc=12`, constant `>0`).
* **(C2)** every prime of every `c_r` lies in Λ (with the precision above), and every
  factor of every `N=4Z−P` for non-dead Z lies in S ("aux" polynomials).
* **(C3) no fixed prime divisor:** for every prime `ℓ∉Λ` with `ℓ≤Σ_{g∈S}deg g` some residue
  mod ℓ is a root of no `g∈S`.
* **(C4) signs:** every member of 𝒱 has an entry with negative constant.
* **(C5)** the seed `(6X,−12XP,−12XP)∈𝒱`, and `C_X=C_P=1`.

**Proposition 1 (PROVED).** Given a certificate, for every admissible q the seed component
of `p=24q+1` is contained in the set of values of 𝒱, and contains no positive vertex.

*Proof.* Induction on the distance from σ. Let a vertex `v` of the component be the value
of `V∈𝒱`, and `v'` a neighbour sharing `z=Z(q)`, Z an entry of V. If Z is dead, `z` is a
p-free denominator outside `[1,2t]` (sign/size are those of the leading data for large q;
`z` is p-free because `r_P=p` does not divide it), so its fibre has at most one vertex
(SIGNED_REFACTOR §5 for `z<0`; WINDMILL Theorem 7 for `z>2t`), namely `v`. Otherwise `v'`
is `(z,y,w)` with `D=r y−s` a divisor of `s(q)²`, hence the value of a formal divisor, and
by the exact decisions above (A) and (B) hold, so by (C1) `v'` is the value of a member of
𝒱. Signs: at large q the value of a formal integer has the sign of its constant (every
`g∈S` has positive leading coefficient, `C_g>0`), so by (C4) every value is nonpositive. ∎

**Proposition 2 (PROVED; = DEPTH3 Lemma 2).** Under H for `{f_g}` there are infinitely
many admissible q. (`f_g∈Z[y]` is primitive irreducible with positive leading coefficient;
for `ℓ∈Λ`, `f_g(y)≡g(q0)/C_g` is an ℓ-unit since `E_ℓ>v_ℓ(g(q0))`, which also gives
`r_g∉Λ`; for `ℓ∉Λ`, `y↦My+q0` is a bijection mod ℓ, so (C3) — automatic for
`ℓ>Σdeg g` — gives a non-root of `∏f_g`.) By (C5), `q=r_X` and `p=r_P` are prime. ∎

Theorem F follows from Propositions 1 and 2 and the certificate of §3.

**Remark (characters).** Proposition 1 never uses (2a). The character theorem only
*explains* (C4): for `ℓ∈Λ` with `24q0+1` a square mod ℓ, `(ℓ/p)=+1`, etc. We chose
square residues wherever the residue was forced to be non-generic (§2.2), but (C4) is
checked directly.

### 1.2 Is stabilisation well defined and finitely checkable? (answer: yes)

The closure depends on the pair (class of q0 at the primes that matter, construction): the
constants `C_g`, hence integrality, depend on `q0`. Different model points give different
closures (B=1500: 7807, 16548 and 27781 vertices for three random model points). For a
*fixed* certificate everything above is a finite exact computation, so "the formal seed
component stabilises" is certified by exhibiting (S, Λ, E, q0, 𝒱) and checking (C1)–(C5).
The search for such data is a fixed-point iteration (§2), not part of the proof.

## 2. Construction of the certificate

### 2.1 Engine

`scripts/formal2.py` (python-flint). Model primes `LAM`; a model point `qt` (an integer)
realises the class `q0` at LAM. `C_g` = LAM-part of `g(qt)`, `R_g=g(qt)/C_g`. Fibre of Z as
in §1.1. Candidate filter: numeric test at qt modulo
`L'=lcm_g(R_g^{β_g})·(LAM-part of c_r)` — failing it is a robust rejection (it implies the
failure of (A) or of (B) at a Λ-prime); survivors are factored (flint) to decide (A)
exactly. When `M1=L'·(…)>2c_s²` and the monomial value `E(qt)` is prime to `M1`, the
congruence pins the constant of D to ≤2 values per monomial; otherwise all constants are
enumerated and tested (no counting claim is made in that case). For primes of `c_r` outside LAM ("r-primes") the engine uses the *generic*
decision (valuation of the content) and records *fragile* candidates (only generic
failures): these need `q mod ℓ` to avoid the roots of their `D+s`. For large ℓ a root
budget is kept (counting argument); for the others (`--explicit`) the roots themselves.

Cross-checks: identical vertex counts to the old sympy engine
(`scripts/formal_closure.py`) — B=200 seed 1: 81/734/4162/4460 after rounds 1–4; model
point of the old `it1` run, B=1500: 7807 vertices, 13359 polys, 1775 r-primes — at
~100× the speed.

### 2.2 Fixed-point iteration (`scripts/formal2_iter.py`, `formal2_iter.sh`)

Start: LAM = primes ≤1500 with the residues of the `it1` model point (random units with
`24q+1` a nonzero square). Each iteration: closure; r-primes failing the counting bound
are made explicit; for each explicit r-prime, the residues mod ℓ that are roots of some
`g∈S` or activate some fragile candidate are marked. **Obstacles** = primes with no
unmarked residue, and primes `ℓ≤Σdeg` violating (C3). Each obstacle joins LAM with a
square residue minimising (#roots of S, #fragile activations).

| iter | vertices | S (entry+aux) | Σdeg | r-primes outside LAM | explicit | obstacles |
|---|---|---|---|---|---|---|
| 0 | 7807 | 13359 | 17401 | 1775 | 816 | 50 |
| 1 | 7883 | 13521 | 17631 | 1746 | 780 | 2 (1831, 1759) |
| 2 | 7883 | 13521 | 17631 | 1745 | 779 | **0** |

Iteration-0 obstacles: 25 primes 1511–2053 where the roots of S already cover all
residues (these are really (C3) failures), 14 further (C3) primes up to 2011, and 11
fragile-dense r-primes (2089, 2203, 2683, 3049, 3559, 4969, 5449, 10343, 10531, 10657,
26729): at these, anchors `t+a` with `ℓ|4a−1` and many divisors activate candidates at
every residue class. Choosing the least damaging residue (≤2 roots of S, ≤72 fragile
candidates) added 76 vertices once and then nothing: the iteration converged.

**Finalisation.** All 1745 remaining r-primes were then made model primes (residue = the
generic one found above for explicit primes; a random residue avoiding the roots of S
for the others), `|LAM|=2036`, largest `3.37·10^16`. The closure was recomputed
*exactly* at the new model point, with no genericity at all: 9 rounds (new vertices
80, 784, 5363, 747, 833, 51, 23, 1, 0), **7883 vertices, 13521 polynomials, no prime of
any `c_r` outside LAM, no positive vertex.**

### 2.3 Aux polynomials need not be prime (PROVED)

In §1.1, (A) was shown robust using only `g(q)/C_g→∞`, and for an accepted candidate
`h^β|D+s` for every h in r, so `y=k·∏C_h^β/c_r` with `k=(D+s)/∏h^β` — the aux values
cancel and y's factorisation involves only entry polynomials. The divisor enumeration
uses only s (entries and P). Hence (C2)'s requirement "aux ⊂ S" and the primality of
the aux values can be dropped, provided (C3) and `E_ℓ>v_ℓ(h(q0))` still hold for the aux
h (used for the Λ-part of `c_r`). (C3) for the smaller family is implied by (C3) for the
full one. So H is needed only for the 6402 entry polynomials.

## 3. The certificate (CERTIFIED)

Files (`data/formal_closure/`): `lam_final.json` (LAM and residues; `qt` is rebuilt
deterministically by `formal2.build_qt`), `closure_final.json.gz` (S with `C_g`, the 7883
vertices, precision data), `analyze_iter*.txt`, `closure_final.log`.

### 3.1 Numbers

| quantity | value |
|---|---|
| Λ (model primes) | 2036 primes: all ≤1500, 51 obstacle primes 1511–26729, 1745 r-primes up to `3.37·10^16` |
| precision | `E_ℓ≤17`; `M=∏ℓ^{E_ℓ}≈10^{12088}` |
| S | 13521 polynomials (9411 linear, 4110 quadratic), Σdeg 17631; coefficients ≤24 digits |
| entry polynomials | 6402 (5009 linear, 1393 quadratic), Σdeg 7795 |
| formal vertices | 7883, none positive |
| denominators | 8412 p-divisible, 1549 anchors (p-free, `0<Z≤12X`), 5726 dead |
| fibres recomputed independently | 9961 (all non-dead), 0 mismatches |
| (C3) | no fixed prime divisor for `ℓ∉Λ, ℓ≤17631` (automatic above) |
| BH exponent | 13521 (6402 with §2.3) |

`scripts/formal2_verify.py` output: `data/formal_closure/verify_report.json`
(`"OK": true`, 2 h 50 min on 14 cores, dominated by the old sympy engine on a few anchors
with ~10^8 formal divisor candidates).

### 3.2 Independent verification

`scripts/formal2_verify.py lam_final.json closure_final.json.gz` checks:

1. qt rebuilt from the residues equals the model point; LAM matches;
2. every `g∈S` is primitive, irreducible (flint), lc>0; `C_g` recomputed by trial
   division; `C_X=C_P=1`;
3. every vertex: formal integers over S, the identity `1/a+1/b+1/c=4/P` as a polynomial
   identity, some negative constant; the seed is present;
4. every denominator classified independently (pdiv/anchor/dead); dead ones occur in
   exactly one formal vertex; **every non-dead fibre recomputed by the old sympy engine**
   `formal_closure.Formal` (small primes := LAM, qt := model point; numeric pinning mod
   the full `r(qt)` is exact because every prime of `c_r` is a model prime) and compared
   with the vertex set (equality), with no prime of any `c_r` outside LAM;
5. (C3) for all primes `ℓ∉LAM`, `ℓ≤Σdeg=17631`;
6. precision `E_ℓ=max(1+max_g v_ℓ(g(qt)), v_ℓ(c_r)+v_ℓ(den))`, reported.

`scripts/formal2_verify_extra.py` (4 min) independently re-derives the generator's
metadata: entry flags; the 7883 formal vertices form **one** component containing the
seed (so the seed component at admissible q is exactly their value set: containment by
Prop. 1, and every formal vertex is a genuine vertex at admissible q, connected to σ);
every factor of every `4Z−P` (non-dead Z) is in S; every prime of every `c_r` is in Λ;
`needE` recomputed and equal to the dump's. Output: `data/formal_closure/verify_extra.json`.
(`formal2_verify.py --skip-fibres` reports `PARTIAL`, never `OK`.)

## 4. What this does and does not say

* **CONDITIONAL:** the seed-component conjecture fails under H (for a 6402-member family).
  Unconditionally it remains open; so does ES.
* The mechanism is the one of DEPTH3 Theorem 2 (every number met factors formally, every
  prime met is a square class mod p by the choice of q0), but the ball is replaced by the
  **whole** component. The new inputs that make the closure finite: WINDMILL Theorem 7
  (p-free denominators outside `[1,2t]` are leaves), the finiteness of formal divisor
  sets, and a fixed-point choice of q0 at the primes of the constants.
* No finite computation at real p can see this: the formal family has thousands of
  members. At real q the first layer is always formal, and escapes occur exactly where a
  formal prime value is composite or a constant's residue is non-generic (§5).

## 5. Real q (EVIDENCE)

**Engine vs. ground truth.** The old engine (identical output to `formal2.py`) was
validated by the previous agent (`scripts/formal_validate.py`, small model B=13, real
q≈10^10–10^11 as model point, exact fibres from `pointwise_fibres.py`): radius 2, 486/486
formal fibres contained in the actual ones and 40/40 exact where every formal prime value
involved was an actual prime; radius 3, 1409/1409 contained, 609/609 dead denominators
with singleton actual fibres, and 88/112 exact, the 24 failures all at an "accidental"
prime of `c_r` (e.g. the anchor `6X−22` with `4z−p=89`) — i.e. at non-admissible q.

**Actual seed components in the certificate's class** (`scripts/formal2_realq.py`,
`data/formal_closure/realq_mod13.jsonl`). 40 primes `q∈[10^9,10^11]`, `p=24q+1` prime,
`q≡q0` modulo `2^4·3^3·5^2·7·11·13` (powers ≤30). F(q) = formal vertices whose value at q
is integral (median 508 of 7883). Exact layered BFS from the seed:

* layer 1 (80 vertices, the t- and −pt-fibres): **always entirely formal**;
* layer 2: 352–4757 vertices (median 881), of which 227–369 are formal; **every one of
  the 40 components has a positive vertex at distance 2**;
* on every escape path (seed, formal, non-formal positive) the path leaves F(q) at a
  formal denominator `Z(q)` one of whose formal primes is not an actual prime:
  in 31/40 cases `g(q)/C_g` is not even an integer (q does not match q0 at a larger
  prime of `C_g`, e.g. `(21X+1)/23`, `(143X+6)/1289`), in 9/40 it is an integer but
  composite.

So real components agree with the formal one exactly as far as the admissibility
conditions actually hold, and escape at the first formal prime that fails to be prime;
this is the predicted behaviour, not a test of H. A search for q in this class with no
positive vertex within distance 2 (40 CPU-minutes) found none; the formal family is far
too large for any real q to satisfy a noticeable fraction of it.

## 6. Replay

```
uv run --with python-flint python scripts/formal2_iter.py init /tmp/fcl/L0.json --qt-from <it1 dump>   # or: --B 1500 --seed s
scripts/formal2_iter.sh 0; scripts/formal2_iter.sh 1; scripts/formal2_iter.sh 2      # (paths /tmp/fcl)
uv run --with python-flint python scripts/formal2_iter.py finalize /tmp/fcl/B2.json.gz /tmp/fcl/L3.json /tmp/fcl/LF.json
uv run --with python-flint python scripts/formal2.py --lam-file /tmp/fcl/LF.json --jobs 14 --dump /tmp/fcl/F.json.gz
uv run --with python-flint python scripts/formal2_verify.py data/formal_closure/lam_final.json data/formal_closure/closure_final.json.gz
uv run --with python-flint python scripts/formal2_realq.py data/formal_closure/lam_final.json data/formal_closure/closure_final.json.gz --mod-bound 13 --power-cap 30 --n 40
```
The `it1` model point is stored in `lam_iter0.json` (residues mod ℓ^k, ℓ^k≥2^64), so the
iteration can be replayed from `--lam-file data/formal_closure/lam_iter0.json`.
