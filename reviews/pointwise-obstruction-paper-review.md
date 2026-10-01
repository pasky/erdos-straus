# Referee report: "Formally generic primes block the pointwise signed-graph approach to the Erdős–Straus conjecture"

Manuscript: `paper/pointwise-obstruction.tex` on branch `side-agent/pointwise-obstruction-paper`
(reviewed at commit `8057728`, 1665 lines; compiled cleanly with pdflatex: no undefined
references, no overfull boxes). Line numbers refer to that file. Theorem numbers are from the
compiled PDF (e.g. Theorem 2.10 = `thm:outer`, Prop. 4.6 = `prop:schinzel`, Thm. 4.11 = `thm:astra`).

Referee stance: hostile. Every key proof was re-derived by hand, the algebra was checked
in SymPy, and small cases were checked with an independent brute-force engine that shares no
code with the project. Citations were checked against the archived PDFs, and the replay
instructions were executed.

## Verdict: **MINOR REVISION**

**Correctness.** No stated theorem is false, and no theorem overclaims its hypotheses.
ES is never claimed proved or disproved (l. 222–228, l. 81). Every conditional result
names its hypothesis in its header. One proof (Theorem 2.10, case 2t<z<p) uses an
unproved inequality three times. The inequality is true; I prove it below in three lines
(D1). One citation is wrong (D2), and a few others are imprecise. The companion result
(Theorem 4.11) is credited prominently and accurately. But it is stated as a numbered
theorem whose proof lives only in an unpublished repository (D4). There are also
submission blockers (TODO/Anonymous, D5). None of these needs new mathematics.

---

## 1. What I verified independently

### 1.1 Proofs re-derived by hand (all correct unless noted)
- **Lemmas 2.1–2.4 (fibres, valuations, labels, small anchor).** Correct. (In the 2.2
  proof, "j≥2" is redundant; see D17.) Lemma 2.4: R≥3/(3t+1) for m≥3t+1 gives
  2/R ≤ 2t+2/3. Correct.
- **Theorem 2.5 (BL dichotomy) derivation.** Correct. Both valuation patterns have
  v_p(u1u3)=1, so BL Lemma 3.4 gives the Legendre symbol with exponent 1. BL Thm 1.2 and
  Thm 1.5 (stated for all odd n, any non-natural integer solution) give the two directions.
  Corollary 2.6 is correct.
- **Lemma 2.7 (chart).** Correct, including (3) (Type II with label pH≡0 is impossible) and
  (4) (e ≥ 2ah because h(a−1)+a(h−1) ≥ 0).
- **Lemma 2.8 (seed, hubs, bridge).** Correct. The fibre counts 3τ(t²) and τ(t²) follow
  from the divisor-pair counting. Uniqueness of the two-term identity: from
  (4a−p)(4b−p)=p², only 4a−p ∈ {−1,−p²} is integral.
- **Lemma 2.9 (Type II ≤ 2).** Correct: |x−pm/K| ≤ 2p/(9p+3) < 1/4.
- **Theorem 2.10 (outer anchors), including the Vieta–Jacobi step.** The case z<0 gives
  length < 1/3 exactly as written. The case z≥p gives p²/((3t+1)(9t+2)) < 1, since
  (4t+1)² − (3t+1)(9t+2) = −11t²−7t−1. For 2t<z<p I re-derived every display: x+z=Hf,
  A(x+z)=4z²+f, w=λ(α+β)², f_P=λγ(4β−γ)−1, the quadratic
  X²−4kλγX+k(λγ²+1), the quarter-discriminant k(λγ²𝓜−1), and the Jacobi computation
  (−k|𝓜)=−1 (2 | k ⇒ 𝓜≡7 mod 8; odd part via reciprocity with (𝓜−1)/2 odd). The
  both-nonpositive bound 2t+d−3u+1<1 is correct. **There is one gap: D1.**
- **Corollary 2.11, Theorem 3.1 (depth ≤ 3), Lemma 3.2 (fresh non-residue),
  Lemma 3.3 (forced exits; all five table rows re-derived), Corollary 3.4, Lemma 3.5.**
  All correct. In Theorem 3.1 every case of the shortest path was re-checked, including
  why the second bullet contradicts minimality.
- **Theorem 3.6 (sieve exponents).** Correct. There are 9 divisors of 36. The branch
  moduli are K = 3,7,11,15,23,35,47,71,143 for both families. All classes are distinct
  because K_hK_d−1 = 4(4hd−h−d) ≠ 0. Lemma 3.5 gives each branch density ≥ 1/2, so
  κ ≥ 1+B/2 = 11/2 (B=9) and 10 (B=18). The proof is a sketch at the sieve step (D8).
- **§4: Lemma 4.3, Lemma 4.4, Lemma 4.5 (formal fibres), Prop. 4.6, Thm. 4.7, Lemma 4.8,
  Thm. 4.9.** All correct.
  - Lemma 4.5, necessity of (A): the resultant argument is sound.
  - Lemma 4.5, (B): exactness follows from (F2) through den(K) | den(D+s).
  - Prop. 4.6: C_P=1 holds automatically. The congruence 24^{deg g}g(q) ≡ H_g (mod p) holds.
    Every prime met is a residue, so BL gives nonpositivity. Dirichlet suffices; no
    prime values are needed.
  - Thm. 4.9: a denominator prime of c_y is excluded both inside Λ (Λ-units) and outside
    Λ (because ℓ > Σdeg). Admissibility is monotone in j. Two cosmetic points are in D21.
- **§5: Lemma 5.1 (leaf), Lemmas 5.2/5.3/5.4/5.6 (dead hub A/B/C/E), Lemma 5.7,
  Prop. 5.8(1)(2)(3)(4).** All correct.
  - Lemma 5.3: the congruence table ±4^j ≡ −4 (mod 𝓜) leaves only D=−pd for odd 𝓜 ≥ 9.
  - Prop. 5.8(3): the AGL₄(ℤ) argument gives a group of order 4, but the polynomials are
    undefined in the paper (D10).
  - Prop. 5.8(4): the three x=y fixed points have z = p, (p+1)/2, p(p+1)/2, all odd.

### 1.2 SymPy identity checks (`reviews/pointwise-obstruction-review-scripts/sym.py`, all pass)
SymPy confirms:
- the chart identities Hx−m=e and (4a−1)H−4e=1, and the reciprocal identity;
- the Vieta relations x+z=Hf and A(x+z)=4z²+f;
- in the mixed case: w, z²=λβ²w, f_P=λγ(4β−γ)−1, the β-quadratic and the
  quarter-discriminant;
- the both-nonpositive expression 2t+d−3u+1;
- the four path/seed vertices of Lemma 2.8;
- Lemma 5.3 entries and the Lemma 5.4 identity (with p=4dw+𝓜);
- the astra positive point (6q+7, (24q+1)(762q+32), (6q+7)(762q+32)/857), with
  e=27·32−7=857 and 857 | (6·713+7)(762·713+32).

### 1.3 Independent brute force (`gp.py`, `t1–t6.py`; no project code)
G_p was enumerated from all z ∈ [1,3p/4] and their full divisor fibres.
- **t1, all p≡1 (4), p<1200 (95 primes): 0 violations.** Checked:
  - Lemma 2.2, labels (Lemma 2.3), anchors (Lemma 2.4);
  - BL positivity ⇔ (AB|p)=−1 at every vertex;
  - Type II buckets have ≤ 2 vertices, never mix signs, and satisfy the |m|≥2t range;
  - outer theorem (every p-free z<0 or z>2t in ≤ 1 vertex);
  - Cor. 2.11 (crossing locations);
  - the unproved inequality x+z ≤ 6t (D1);
  - fibre sizes 3τ(t²) and τ(t²); the bridge path;
  - Lemma 5.1; repeated denominators (Prop. 5.8(1)).
- **t2, p<6000:** BFS distance agrees with the prediction of Theorem 3.1 ((9) ⇒ 2;
  (A)∨(B) ⇒ 3) at all 383 primes. At p=297049: (9) fails, (A) holds, (B) fails, and BFS
  gives distance 3.
- **t3:**
  - Mordell residue classes recomputed: exactly {1,121,169,289,361,529} mod 840.
  - Lemma 3.3 exits verified for every p≡1 (4) below 3·10⁵: 0 failures.
  - p=97 has 8 positive solutions; p=193 has 6.
- **t4:** Prop. 5.8(4) at p = 13, 17, 29, 37, 41, 97, 193. The total is odd and the
  z-even part equals 6f(p) exactly. (A first version with a z cutoff gave false
  mismatches; it was fixed by exact two-sided enumeration.)
- **t5:**
  - Lemmas 5.3/5.4 on 437 dead-hub instances (k=2..7, x<4·10⁴): fibre = predicted set,
    count (τ(x²)−1)/2, descent buckets exactly {V_d, D_d}.
  - Lemma 5.6 on 157 anchor instances and on buckets with h<40, p<1500.
  - Lemma 3.2(1)(2) character conditions on every positive exit.
  - Prop. 5.8(2) parity N⁺ even, N⁻ odd, with the counts N⁺/2 and (N⁻−1)/2.
  - The X-branch vertex (−pt, t+d, t(t+d)/d).
  - 0 failures in all of the above.
- **t6:**
  - Exactly [297049] fails (9) below 3·10⁵ in Mordell's classes, matching Evidence 6.1.
  - There are 1271 primes ℓ ≤ 17631 outside Λ, matching Thm. 4.13. These include all 404
    primes ℓ ≤ 7795 = Σ_{S_e} deg that (E3) strictly requires.
  - 24q₀+1 is a non-residue modulo exactly 870 of the 2036 primes of Λ, confirming
    Remark 4.14 from `certificate.json.gz`.

### 1.4 Data claims traced to sources
Every number in Thm. 4.13 matches the `report` block of `certificate.json.gz`:
- |Λ| = 2036, max ℓ = 3.3688·10¹⁶, E_max = 17, log₁₀M = 12087.8;
- |S| = 13521, |S_e| = 6402, Σdeg_e = 7795;
- 8412/1549/5726 denominators; 9961 fibres; 0 mismatches.

These also match FORMAL_CLOSURE.md: 5009/1393 split, 533,011,471 candidates, the 31/9
split and 80-vertex first layer of Evidence 4.15.

DEPTH3.md matches Evidence 6.1/6.2: 179468/70, 14036239/1306, 114455512/6196,
1046544177/36625 (sum 44197), 1113907, 5304, 14.7, 17.3.

SIZE_CONJECTURE.md matches Evidence 5.5 (398/339/3469/30035/10155/2811, "13 of 14",
243, 146). All four Evidence 5.5 primes are prime and ≡1 (4). The ratios size/ln p
recompute to the table values.

---

## 2. Attribution check (against the PDFs in `sources/`)
Details are in `reviews/pointwise-obstruction-review-scripts/citecheck_subagent.md`. I
re-read the disputed items myself in the PDF text: BL Cor 1.4, the ET Prop 1.6 remark and
ET p. 8, and Elsholtz §3.

| Citation | Verdict |
|---|---|
| BL Lemma 3.10 (finiteness) | OK. The exclusion u_i≠−u_j is vacuous for odd n. |
| BL Thm 1.2, Thm 1.5, (3.1), Lemma 3.4, Cor 1.3, App. A, Thm 1.1, Thm 1.6 | OK. Permutation invariance should cite Prop 2.6 (D12). |
| **BL Cor 1.4 as "the polynomial-identity obstruction"** | **WRONG.** Cor 1.4 is BL's recovery of ET Prop 1.6 (odd-square vanishing for natural solutions with a divisibility pattern). See D2. |
| ET Prop 1.6 and the remark after it (PDF p. 6) | OK for "covering congruences". The remark lists covering congruences and the circle method; polynomial identities are on p. 8 (D3). |
| ET (2.1), (2.6), (2.7), (2.18), (2.21), Prop 2.2 | OK under the coordinate map (x,y,z)=(abdn,acd,bcd). The letter `e` clashes (D9). |
| Dahan Lemma 4.2, Thm 4.3 | OK as "adapted". |
| Dahan Prop 3.8, Thm 4.14 | Imprecise (D14). |
| Jiang Thm 3.2; v2 withdrawn | OK (positive solutions only, as stated). |
| Mihnea–Dumitru 10¹⁸ | OK (primes ≤ 10¹⁸; names correct). |
| Monks–Velingker Thm 2.1(i) | OK (`sources/lit2026/monks-velingker-2008-erdos-straus.pdf`, p. 2). |
| Elsholtz 2010, "fragility of windmill partitions" | Supported by §3 (author's version p. 14–15: "in the general case the boundaries … do not induce such a balanced three-partition"). Needs a pinpoint (D13). |
| Schinzel 2000 | PDF not archived. ET p. 8 confirms the square-class statement. |
| Halberstam–Richert | Book not archived. The sieve theorem is uncited by number (D8). |
| Mordell, Ch. 30 | Not verifiable here. The six classes are confirmed by MV p. 2, Jiang p. 1 and MD p. 1. |
| Vaughan; Bourgain–Gamburd–Sarnak | **Missing from the bibliography** (D11). |

Novelty claims are modest and appropriately hedged (l. 242–246: "its novelty is
unconfirmed").

## 3. Astra companion credit
Details are in `astra_credit_subagent.md`. I spot-checked the git histories and the
astra docs myself.

- **Prominence: good.** Astra is credited in:
  - the abstract (l. 58–64);
  - Thm C(1), with the paragraph after it saying astra is stronger in two respects;
  - the header of Thm 4.11;
  - Remark 4.12 ("The proof of Theorem 4.11 is the companion's");
  - the acknowledgements.
- **Accuracy: verified against `../erdos-straus-astra`.** All of the following match:
  - the 159 forms: 84 offsets and 75 rows; q is the a=0/h=0 overlap; p is added;
  - n≡507 (857), q≡713 (857); the a=7, h=32, e=857 point;
  - the restricted-tuple admissibility;
  - the 800-form history: (Q+16)^393600, a=10/h=33/e=1277, n≡1248 (1277), 302 nodes;
  - 315,642 monomials, 287 digits, 91 support primes;
  - SHA-256 `62a88612…c2f2`, which is identical at `43913c4` and at `a036064`.
- **Astra's checker re-run** on a copy gives `VERIFIED_PRIMARY_PACKET_EVENTUAL`, with
  `simultaneous_primality_proved: false` and `explicit_threshold_proved: false`. Both
  limitations are correctly conveyed by the paper.
- **Priority.** Astra's whole-component result is commit `f0f2e12`
  (2026-09-30 18:40, 800 forms). It precedes this project's Theorem F certificate
  (`19c712c`, 20:01). So "first" is correct. The 159-form reduction (`43913c4`,
  2026-10-01 10:58) came after Theorem F. Imprecisions are listed in D6 and D7.

## 4. Replay
Executed under `ulimit -v 8000000` and `timeout`, with ≤4 cores. Details are in
`replay_subagent.md`; I re-ran the sterile checks myself.

| Item | Result |
|---|---|
| `pointwise_seed_check.py`, `pointwise_fibres_check.py`, `pointwise_incidence.py 297049`, `depth3_check.py`, `depth3_validate.py 13 30000` (0 mismatches), `depth5_branches.py 13 3000000` | All OK, each under 20 s, **but only with the `scripts/` prefix** (D16). |
| `formal2_verify_extra.py …` | `OK: true`, 4 min 32 s (the paper says 4 min). |
| `review_fc_global.py` | All checks pass, 28 s. |
| `review_fc_fibres.py --all --jobs 4` | 9961/9961 fibres equal, 8 min 21 s. |
| `formal2_verify.py` (2 h 50 min) | Not run in full. Startup and usage are OK. Note: it imports `formal2.build_qt` from the generator. |
| `.cpp` files | They compile, but the appendix gives no build command. `windmill_singleton` **segfaults without its argument**. |
| `formal2_iter.py --help` | Raises `KeyError`. Subcommand help works. |
| `sterile_certificate_check.py` | p=1654…637 and p=1960…909: OK, 16 s together. p=4750…253: OK, about 10 s. p=2741…957 (30035 vertices): OK, 4 min 30 s, 1.6 GB RSS. The batch over all seven certificates did not finish in 20 min, and the paper gives no runtime. |
| Astra checker | OK (on a copy). |

---

## 5. Numbered defect list

Severity scale: **Moderate** = must fix before submission (a proof gap or a false
citation, fixable without new mathematics); **Minor**; **Cosmetic**.

**D1. Moderate: proof gap in Theorem 2.10, case 2t<z<p.**
- l. 500: "Then $0<f\le(x+z)/3\le2t$"
- l. 507: "$|f_N|\le x_N+z\le6t$"
- l. 509: "If $H_N\le-5$ then $|f_N|\le6t/5$"
- l. 523: "so as above $H_1=-1$"

All four steps use x+z ≤ 6t for vertices sharing a p-free z ∈ (2t,p). This bound is never
proved, and it does not follow from Lemma 2.4 or Monks–Velingker. It is true:
- From (eq:vieta) and f=(x+z)/H, (x+z)(A−1/H)=4z². So x+z ≤ 4z²/(A−1/3) if H ≥ 3, and
  x+z ≤ 4z²/A if H ≤ −1.
- g(z)=4z²/(4z−p−1/3) is convex on (2t,p).
- At z=2t+1 the bound reads 16t²+16t+4 ≤ 24t²+16t. At z=p−1 it reduces to p ≥ 5.

I checked the bound numerically for all p<1200. **Fix:** insert the derivation as a
sentence before the bullets.

**D2. Moderate: wrong citation.** l. 236–237: "The polynomial-identity obstruction is
Schinzel's \cite{Schinzel}; see \cite[\S1]{ET} and \cite[Cor.~1.4]{BL}."
BL Cor 1.4 is the odd-square vanishing statement for natural solutions with
n | u₁, gcd(n,u₂u₃)=1 (or the Type II analogue). BL recover it from ET Prop 1.6. It says
nothing about polynomial identities. **Fix:** replace with "\cite[p.~8]{ET}". If wanted,
cite BL Cor 1.4 separately as the Brauer–Manin proof of ET Prop 1.6.

**D3. Minor: attribution mixes two ET passages.** l. 123–128: "…informally familiar from
Elsholtz--Tao \cite[\S1, remark after Prop.~1.6]{ET}. … This rules out covering
congruences and polynomial identities." ET's remark after Prop 1.6 (PDF p. 6) names
"a finite set of covering congruence strategies, or the circle method". Polynomial
identities are treated on PDF p. 8 ("a primitive congruence class … which is a perfect
square, cannot be solved by polynomials (this also follows from Proposition 1.6)").
**Fix:** cite both places.

**D4. Moderate: the companion theorem's status and citability.**
- l. 1101: `\begin{theorem}[companion computation \cite{AS}; \status{conditional} on Dickson]`
- l. 1140–1145: "We have \emph{not} independently re-derived the eventual closure
  argument of \cite{AS}."

The paper's status vocabulary defines \status{conditional} as "proved from a named
hypothesis" (l. 148–150). Theorem 4.11 is not proved in this paper and is not re-verified
by it. Its only source is a git repository at a revision hash, and the bibliography entry
is still a TODO (l. 1619–1623). A journal cannot accept a numbered theorem whose sole
proof is an unpublished repository. **Fix:**
- give the theorem a distinct label, e.g. "\status{reported} [AS]; finite packet
  re-checked here; eventual argument not re-verified";
- cite a citable astra preprint once one exists.

Until then, keep it as "Theorem 4.11 ([AS])" and make clear that "Conjecture 1.2 is false
under H" rests on Theorem 4.13 alone. Thm C's last line (l. 205) already allows this.

**D5. Moderate (submission blocker): placeholders.**
- l. 37: "% TODO(submission): author metadata"
- l. 39: "\author{Anonymous}"
- l. 1583/1588: "\emph{[TODO: final citation and authorship form of \cite{AS} to be settled.]}"
- l. 1623: "\emph{[TODO(parent): final citation form.]}"

**Fix:** settle authorship and the [AS] citation before any circulation.

**D6. Minor: the scope of "independently" and of the shared tools.**
- l. 1137–1138: "The construction also uses the outer-anchor bounds
  (Theorem~\ref{thm:outer}) and Type~II rigidity."
- l. 538–540: "The cases $z<0$ and $z\ge p$, and the bound of two vertices for $2t<z<p$,
  were found first; the Vieta--Jacobi step closes the remaining case."
- l. 1586: "reached the conditional disproof independently, first, and in the stronger
  linear form."

Both repositories share their early history, including SIGNED_REFACTOR.md: commit
`f3bea2f` (2026-09-08), present in both, contains the z<0 and z≥p cases. Astra invokes
"the exact outer-anchor theorem" only for anchors "eventually negative or ≥p"
(AFFINE_SEED_CLOSURE.md:126, :234; ONE_PRIME_FIBRES.md:180). It does not use the
Vieta–Jacobi case, which is this project's WINDMILL Thm 7. **Fix:**
- "uses the cases z<0 and z≥p of Theorem 2.10 and Type II rigidity, which predate the
  separation of the two projects";
- at l. 538, say by whom and where those cases were found;
- at l. 1586, "first (in an 800-form version, later reduced to 159 forms)". The 159-form
  reduction postdates Theorem 4.13.

**D7. Minor: overstatement of what astra's positive witness covers.**
- l. 1151: "And it shows that ES holds at the primes concerned."
- l. 214–215: "it exhibits an ES solution at the same primes, so its primes are
  counterexamples to \emph{reachability}".

The witness exists only on the subprogression n≡507 (857), and the existence of infinitely
many such sterile primes needs Dickson for the restricted tuple (stated correctly at
l. 1119–1122). **Fix:** "at the primes of the subprogression n≡507 (mod 857)".

**D8. Minor: the sieve step of Theorem 3.6 is a sketch.**
- l. 722: "\status{proved}, given a standard upper-bound sieve"
- l. 749–758: "By the prime number theorem in progressions, this is a sieve problem of
  dimension κ … So an upper-bound sieve of dimension κ at level $N^{1/2}$ \cite{HR}
  gives …"

**Fix:**
- State ω(ℓ) = 1+#{b : ℓ mod K_b ∉ R_b} for ℓ outside the exceptional set.
- Verify Σ_{w≤ℓ<z} ω(ℓ) log ℓ/ℓ ≤ κ log(z/w)+O(1) (PNT in progressions modulo
  lcm K_b = lcm(3,7,11,15,23,35,47,71,143)), ω(ℓ)<ℓ and |r_d| ≤ ω(d).
- Cite a specific theorem with these hypotheses (e.g. HR Thm 2.2, the Ω₁/Ω₂(κ)/R
  upper bound; I could not check the number because the book is not archived).

Also: Theorem 3.6 (l. 723–726) and Thm A(4) (l. 178) count {p ≤ N : dist(p)>2}, but dist
is only defined for primes p≡1 (4). Add "p≡1 (mod 4)".

**D9. Minor: notation clash with ET.**
- l. 313: "for Type~I, $4m-1=pe$ is \cite[(2.1)]{ET}". Here `e` is ET's e, which equals
  the paper's H. In Lemma 2.7, e means (4a−1)h−a.
- l. 404: "$e=a^2d$ in the coordinates of …". Here `e` is the chart e, but a and d are
  ET's a and d. They are not the paper's a (offset) or d (divisor).

**Fix:** write e_ET, a_ET, d_ET, and state the map: pm=abdn, x=acd, the third entry is
bcd; H=e_ET and A=f_ET.

**D10. Minor: undefined objects in Prop. 5.8(3).** l. 1443–1447: "The integral affine maps
of $\Z^4$ preserving the Type~II polynomial $k(4abc-p)-a-b$ … The same holds for the
Type~I polynomial $k(4abc-1)-p(a+b)$." The four-parameter model is never defined (Type II
(x,y,z)=(abc, pkbc, pkac), Type I (pabc, kbc, kac); WINDMILL.md §2.1). "Integral affine
maps" must mean AGL₄(ℤ): without invertibility the ±1 entries step fails, and the maps do
not form a group. **Fix:** define the model and write AGL₄(ℤ).

**D11. Minor: missing references.**
- l. 1575–1576: "Vaughan-type bounds $E(N)\ll N\exp(-c(\log N)^{2/3})$" has no citation.
  Add R. C. Vaughan, *On a problem of Erdős, Straus and Schinzel*, Mathematika 17 (1970),
  193–198, doi:10.1112/S0025579300002886.
- l. 1381: "in the style of Bourgain--Gamburd--Sarnak" has no citation.

**D12. Minor: two loose sentences after Theorem 2.5.**
- l. 351–352: "The symbol is invariant under permuting the $u_i$ \cite[\S1]{BL}." Cite
  BL Prop. 2.6, which is where §1 points.
- l. 356–358: "An elementary proof by quadratic reciprocity, in the style of
  \cite[Prop.~1.6]{ET}, is also possible; we do not need it." This is an unsupported
  claim, especially for the nonpositive direction. Delete it or give a reference.

**D13. Cosmetic: pinpoint for Elsholtz.** l. 1475: "Elsholtz \cite{Elsholtz} notes the same
fragility of windmill partitions for general forms." The content is supported, but only by
§3 (generalisation to p=sx²+tyz: "the boundaries … do not induce such a balanced
three-partition"). Add "\cite[\S3]{Elsholtz}".

**D14. Minor: Dahan references are imprecise.**
- l. 762–763: "The case $h=1$ alone gives the exponent $3/2$; compare
  \cite[Thm.~4.14]{Dahan}." The direct analogue is Dahan Thm 4.3 with |P|=1, an upper
  bound with exponent 1+1/2. Thm 4.14 is a *lower* bound ≍N(log N)^{-3/2} for a
  different obstruction (shift c=7).
- l. 1090–1092: "Related unconditional obstructions for specific branches are
  \cite[Prop.~3.8, Thm.~4.14]{Dahan}." Prop 3.8 is a finite computed list of 14 primes
  below 5·10⁹ that fail the a=1 family. It is not an obstruction theorem.

**Fix:** rephrase both.

**D15. Minor: an unproved count presented as a formula.** l. 1349–1353: "the component of
$x$ is typically exactly the hub fibre plus $2^r-1$ descent vertices. It has size
$(3^{r+1}-1)/2+2^r-1$ when $x$ is a guard prime times $r$ primes." The count needs
unstated hypotheses:
- x is squarefree;
- the guard prime is ≡3 (mod 4) and the other r primes are ≡1 (mod 4), so that the
  divisors w>1 of x/guard are exactly the w ≡ 1 (mod 4);
- the descent buckets close with no further vertices.

"Typically" signals evidence, not a lemma. **Fix:** state the hypotheses and label the
count \status{evidence}, or prove closure.

**D16. Minor: replay appendix.**
- l. 1593: "All commands run from the repository root". The bare names on l. 1597–1602
  (`pointwise\_fibres\_check.py`, `depth3\_validate.py 13 30000`, …) do not run from the
  repository root.
- No interpreter line is given (`PYTHONPATH=scripts uv run --with python-flint python`).
- No build command is given for the `.cpp` files. `windmill_singleton` needs its T
  argument; it segfaults without one.
- `formal2_iter.py --help` raises KeyError.
- No runtime is given for the sterile checker.
- l. 1172 names `certificate.json.gz`, but the replay block (l. 1214–1219) feeds
  `lam_final.json`/`closure_final.json.gz`. Explain how the three files relate.

**Fix:** prefix `scripts/` everywhere and give one full command line per item.

**D17. Cosmetic.** l. 285: "If $i<j$ and $j\ge2$". Since i ≥ 1, i<j already implies
j ≥ 2.

**D18. Minor: the title and abstract tone versus the conditional content.**
- l. 38: title "…block the pointwise signed-graph approach…"
- l. 51: "We explain why this pointwise programme is blocked."

The block is conditional on H or Dickson. Unconditionally, Conjecture 1.2 is open
(l. 223), and formally generic primes are not known to exist. The abstract later states
the conditionality correctly. **Fix:** add "conditionally on Schinzel's Hypothesis H" to
the first sentence that claims the block, or retitle "…would block…" / "Under Hypothesis
H, formally generic primes block…".

**D19. Cosmetic: Jaroma's identity.** l. 95: "signed solutions exist for every odd $n$
(Jaroma's identity, see \cite[\S1]{BL})". BL §1 only asserts existence and cites its
reference [14]; it does not display the identity. Cite Jaroma directly or display the
identity; say n ≥ 3.

**D20. Minor: misplaced "this" in the discussion.** l. 1555–1560: "The whole seed component
is closed by explicit finite certificates under Dickson or H (Theorems 4.11 and 4.13);
their nonpositivity is checked directly. This is the Elsholtz--Tao odd-square principle in
graph form." By Remark 4.14 the class of Theorem 4.13 is *not* a square class: 870
non-residues, which I confirmed. So the last sentence must refer only to Prop. 4.6 and
Thm. 4.9. **Fix:** move it before "The whole seed component…".

**D21. Cosmetic: Theorem 4.9 bookkeeping.**
- l. 1058: "and the triples to $\cV_{j+1}$". Say V_{j+1} ⊇ V_j.
- l. 1056–1057: "(B) is decided by $q^*$". Say this is done after raising E_ℓ to the
  (F2) precision.

**D22. Cosmetic: the "classical anchor criterion" (l. 566) has no reference.** Cite
ET Prop. 2.3 (Type I criterion n=4acd−f, f | 4a²d+1) and its Type II analogue.

---

## 6. Summary for the editor
The mathematics is sound. I re-derived every proof the editor asked about and found one
genuine gap (D1). It closes with a three-line convexity estimate, and I checked it
numerically.
- The exponents 11/2 and 10 are correct.
- The depth-≤3 classification matches brute-force BFS exactly.
- The Mordell corollary and the forced-exit table are correct.
- The formal-fibre lemma, Prop. 4.6 and Theorems 4.7/4.9 are complete.
- The outer-anchor Vieta/Jacobi argument is correct apart from D1.
- Dead-hub Lemmas A/B/C/E are correct.

The astra companion is credited first and prominently, and its numbers are accurate. Its
theorem should not sit in the paper as a numbered result with an in-house status label
until a citable source exists (D4). The submission blockers are D1, D2, D4 and D5. The
rest are routine.

## Addendum: sterile certificate p=274159709010072908384347957 (30035 vertices)
`OK … sterile component of 30035 vertices, entire and closed; denominators {'anchor': 512, 'typeI': 0, 'typeII': 59559, 'outer': 0, 'typeI_single_method': 0}`. The run took 4 min 30 s wall time with 1.6 GB RSS. So the headline certificate of Evidence 5.5 replays. The other three Evidence 5.5 certificates also replay (see §4). I did not run the seed-component certificate (`…_seed.json.gz`) or the two variant certificates; they are presumably what made the subagent's batch run exceed 20 min. The appendix should state their runtimes.

---

# Round 2: check of Revision 1

Reviewed: branch `side-agent/pointwise-obstruction-paper` at `1a82a4f` (paper
commits `4ceffcb` and `9ab210d`; the author's mapping is the "Revision 1" section of
AGENT_REPORT_B.md). The diff from the round-1 version `8057728` touches only
`paper/pointwise-obstruction.{tex,pdf}`, `WINDMILL.md` and `AGENT_REPORT_B.md`. Line
numbers below refer to the revised tex.

**Build.** I recompiled from scratch with pdflatex. The first two passes leave one
"Label(s) may have changed" warning. The third pass is clean: 29 pages, no warnings, no
undefined references, no overfull or underfull boxes. `pdftotext` finds no "TODO"
in the PDF.

## R2.1 D1, re-derived

New text (l. 528–541):

> Every vertex at $z$ satisfies x+z ≤ 6t (eq:sixt). Indeed, $x$ is the p-free
> denominator in [1,2t] given by Lemma 2.4 (since z∉[1,2t]), and z ≤ p−1 = 4t.

**This is correct, and it is simpler than my repair.**
- In this case every vertex at z is Type I, (z, x, pm).
- Lemma 2.4 says some p-free denominator lies in [1,2t]. Since z > 2t, that
  denominator is x.
- So x ≤ 2t, and with z ≤ 4t this gives x+z ≤ 6t.

**Correction to my round-1 D1.** I wrote that the bound "does not follow from Lemma 2.4
or Monks–Velingker". That was wrong: it follows from Lemma 2.4 in one line. D1 was an
omitted one-line justification (the setup sentence lost "x ≤ 2t"), not a real gap. I
withdraw the "Moderate" severity of D1 in favour of "Minor".

**The added convexity check is also correct.**
- (x+z)(A−1/H) = 4z². Since A−1/H ≥ A−1/3 for both H ≥ 3 and H ≤ −1, x+z ≤ g(z).
- g(z) = 4z²/(4z−c), with c = p+1/3, equals z + c/4 + c²/(4(4z−c)). It is convex for
  4z > c.
- The endpoint inequalities read 16t²+16t+4 ≤ 24t²+16t and p ≥ 5, as stated.

**All later uses of the bound are now justified.**
- f ≤ (x+z)/3 ≤ 2t (l. 541).
- |f_N| ≤ x_N+z ≤ 6t (l. 547). The bound 6t/5 for H_N ≤ −5 follows.
- The both-nonpositive bullet (l. 571–572) cites (eq:sixt).

**WINDMILL.md Theorem 7.** The setup already stated "1 ≤ x ≤ 2t (SIGNED_REFACTOR §3)"
and z < p. The added parenthetical "x+z ≤ 6t because x ≤ 2t by the setup and
z ≤ p−1 = 4t" is correct and sufficient. There was no gap there.

## R2.2 Item-by-item status

| item | status | check |
|---|---|---|
| D1 | **FIXED** | Re-derived above. My severity was overstated. |
| D2 | **FIXED** | l. 253–256: the polynomial-identity obstruction now cites ET p. 8. BL Cor 1.4 is cited correctly, as the Brauer–Manin recovery of ET Prop 1.6. |
| D3 | **FIXED** | l. 131–135: Prop 1.6 (vanishing), p. 6 (covering congruences), p. 8 (square classes). Matches the PDF. |
| D4 | **FIXED** (status) | A new status **reported** is defined (l. 168–171). Thm C(1) and Thm 4.11 carry "reported [AS] … finite packet re-checked here; eventual-closure argument not re-verified". Thm C now says part (2) alone gives "false under H". The same is said at l. 1162–1166 and in §7 (l. 1667–1671). The *citability* of [AS] is still open; see D5. |
| D5 | **PARTIAL** | Both TODOs are now `%` comments, and none is in the PDF. But `\author{Anonymous}` remains, and [AS] is still "unpublished computational campaign, 2026". This is a parent/user decision and remains a submission blocker. It is not a mathematical defect. |
| D6 | **FIXED** | Verified against the git histories. The newest commit common to both repositories is `7aed9ca` (2026-09-08 23:45). SIGNED_REFACTOR.md at that commit already contains the character theorem, "Type II fibres have at most two vertices", the z<0 and z≥p singleton cases, and "at most two" for 2t<z<p. Both sterility results are from late September 2026, so "they separated before either sterility result was found" (l. 231–235) is correct. "Vieta–Jacobi … found later, in this project only" (l. 577–581) holds: astra has no 2t<z<p singleton statement. Remark 4.12 (l. 1207–1210) correctly limits astra's use to z<0/z≥p and Type II rigidity. The timeline paragraph and acknowledgements match the commits (`f0f2e12` < `19c712c` < `43913c4`). |
| D7 | **FIXED** | Subprogression scope in Thm C (l. 225–227), Remark 4.12 (l. 1224) and §7 ("under Dickson for the restricted tuple"). |
| D8 | **FIXED** | ω(ℓ) explicit; ω ≤ 19 < ℓ for ℓ > 19; \|r_d\| ≤ ω(d) for the progression mod 840; Mertens in progressions gives Ω₂(κ). "p≡1 (4)" is added in Thm A(4) and Thm 3.6. The HR theorem number (2.2) is recalled, not checked against the book, and the paper says "e.g.". Acceptable. |
| D9 | **FIXED** | The subscripted ET coordinates and maps are verified against the ET PDF. Type I (abdp, acd, bcd) is Prop 2.2. Type II (abd, acdp, bcdp) is (2.22). 4m−1 = pe_ET is (2.1). 4m−1 = f_ET is (2.18). 4x−p = f_ET is (2.6). e = (f_ET·e_ET−1)/4 = a_ET²d_ET follows from (2.7). |
| D10 | **FIXED** | Model defined, and I checked both equations: 1/(abc)+1/(pkbc)+1/(pkac) = 4/p ⇔ k(4abc−p) = a+b, and the analogous Type I identity. The renaming c→d_ET, k→c_ET matches ET (2.3) 4abcd = na+nb+c and (2.15) 4abcd = a+b+nc. AGL₄(ℤ) is stated. |
| D11 | **FIXED** | Vaughan (Mathematika 17 (1970), 193–198) and BGS (arXiv:1607.01530) added and cited. |
| D12 | **FIXED** | BL Prop 2.6 cited; the "elementary proof" sentence is deleted. |
| D13 | **FIXED** | \cite[\S3]{Elsholtz}. |
| D14 | **FIXED** | Thm 4.3 is the h=1 analogue; Thm 4.14 is described as a two-sided estimate for c=7; Prop 3.8 as a finite list of 14 primes. |
| D15 | **PARTIAL** | Hypotheses stated and correct: squarefree x; ℓ_i ≡ 1 (4𝓜) implies the Lemma 5.3 hypothesis; guard ≡ 3 (4) means w ≡ 1 (4) ⇔ guard ∤ w; so 2^r−1 descents, all with d ≥ guard. Closure is labelled evidence. **New small inaccuracy (l. 1433–1436):** see R2.3(a). |
| D16 | **FIXED** | Re-run below; every listed command works as printed and the runtimes match. |
| D17 | **FIXED** | |
| D18 | **FIXED** | The title now begins "Under Hypothesis H, …". The abstract says "conditionally on Schinzel's Hypothesis H, this pointwise programme is blocked", and that the astra result is reported, not re-proved. |
| D19 | **FIXED** | The identity checks: 2/(n−1)+2/(n+1)−4/(n(n²−1)) = 4/n. BL ref. [14] is J. H. Jaroma, Crux Math. 30 (2014), as cited. |
| D20 | **FIXED** | §7 item 3 now separates Prop 4.6/Thm 4.9 (odd-square principle) from the certificates, and states that Thm 4.13 is not a square-class instance. |
| D21 | **FIXED** | V_{j+1} ⊇ V_j; (B) is decided after the (F2) precision is raised. |
| D22 | **FIXED** | ET Prop 2.3, fifth bullet, is literally "n = 4acd − f and f \| 4a²d+1". With z = acd and D = a²d this is D ≡ −1/4 (mod f), D \| z². ET Prop 2.7 is the Type II list. |

## R2.3 New issues introduced by the revision (all minor or cosmetic)

**(a) Minor, l. 1433–1436:** "In most computed instances no further vertex appears
(\S3.4 of the source notes: $122$ of $126$ guarded instances were sterile). The
component then has $(3^{r+1}-1)/2+2^r-1$ vertices."

"Sterile" is not the same as "no further vertex". SIZE_CONJECTURE §3.4 reports sterile
guarded components with sizes 395–397, 1156–1161, 3407–3415, 10096–10098 and
30035–30039. The formula gives 395, 1156, 3407, 10096 and 30035, the lower ends. So
some sterile components have a few extra vertices. **Fix:** "122 of 126 guarded
instances were sterile, with components of the predicted size or at most 8 vertices
larger. The formula is attained in the typical case, e.g. 30035 = 29524+511 at r=9."

**(b) Cosmetic, l. 1428:** the guard prime is called $q_0$, which clashes with the frame
base point $q_0$ of §4. Rename it, e.g. $g_0$ or $\ell_0$.

**(c) Cosmetic, AGENT_REPORT_B.md:** it says the build is "clean: two pdflatex passes".
From scratch, three passes are needed for stable labels. Harmless.

**No new overclaim found.** I grepped every changed passage for priority, novelty,
status and scope words: "first", "independent", "proved here", "reported",
"separated", "only".
- "Independently" now refers to the certificates (l. 228–230, 1229).
- "First" refers to the 800-form version.
- All four "false under H" statements rest on Thm 4.13.
- The new title is conditional.
- The sieve proof claims no more than the cited sieve gives.

## R2.4 Replay of the new appendix

Run from the repository root, `PY` as defined, `ulimit -v 8000000`, ≤4 cores:

| command | result | time |
|---|---|---|
| `PY scripts/depth3_validate.py 13 30000 --jobs 4` | 1610 checked, 0 mismatches | 36 s |
| `g++ … depth3_allp.cpp`; `/tmp/d3allp 13 100000000 4` | 179468 tested, 70 candidates | 2 s |
| `PY scripts/depth3_batch.py allp.txt --jobs 4` | `SUMMARY {'3': 70}` | 2 s |
| `g++ … depth3_sieve.cpp`; `/tmp/d3sieve 6 1 100000000 4 hard` | 217 survivors | 1 s |
| `PY scripts/depth3_batch.py surv.txt --jobs 4` | `SUMMARY {'3': 217}` | <1 s |
| `PY scripts/formal2_realq.py … --mod-bound 13 --power-cap 30 --n 40` | runs; first layer 80/80 formal | 5 s |
| `g++ … windmill_singleton.cpp`; `/tmp/wm_single 2500000` | 2939478 candidates, 0 hits | <1 s |
| sterile `p2192882958603411108997` | OK, 3407 vertices | 10 s |
| sterile `p691188894734138813322041_typeI` | OK, 409 vertices | 37 s |
| sterile `p274159709010072908384347957_seed` | OK, SEED component 10155 vertices (11 Type I buckets single-method, consistent with "almost all") | 21 min, 1.9 GB RSS |

The round-1 runs of the other certificates and of the formal-closure checks still apply,
since those scripts and data are unchanged. The appendix's runtimes match: "23 min" for
the seed certificate, against my 21 min.

## R2.5 Final verdict: **ACCEPT** (mathematics and exposition)

All 22 items are FIXED except two that are PARTIAL:
- **D5** (authorship and [AS] citation) is a parent/user decision. It must be settled
  before submission.
- **D15** has one new sentence that conflates "sterile" with "exactly the predicted
  size" (R2.3(a)). This is a one-line wording fix.

No mathematical defect remains. The one round-1 "gap" (D1) turned out to be a one-line
omission, and my round-1 claim that it did not follow from Lemma 2.4 was mistaken. The
revision introduced no overclaim.
