# AGENT REPORT O153 — brainstorm WILDCARD (branch `side-agent/bs-wildcard`)

Deliverables:
* `BRAINSTORM/wildcard_list.md`: 18 angles, W1–W18, each with a one-line barrier pre-screen.
* Three full memos (below).
* Scripts `scripts/bs_wild_{seeds,units,hardness,squares}.py`. Logs `logs/bs_wild_*.txt`: tiny; the f_II dump
  stays in /tmp.

Nothing is LIVE. ES is not solved, and no case of it is claimed.

**List (wildcard_list.md).** Fifteen angles collapse at pre-screen with a named barrier:
* every-interval smooth numbers (B4, via PIGEONHOLE Lemmas 2.1/2.3);
* 4→3-term merging (B3, FIBRED);
* entropy/OT and Gowers norms (B6/B2);
* CSP phase transitions (ES(p) is a 1-DNF);
* Vojta/Nevanlinna (gives upper bounds only);
* SOS/cutting planes;
* proof mining;
* half-integral weight (Eisenstein only, cancels at squares);
* Siegel's lemma (signed solutions);
* quantum;
* weighted zero-sum (Kneser);
* tensor rank (field invariant);
* Euclidean quaternion descent;
* dynamical zeta (= H-A).

W1–W3 were selected for full memos.

**W1 `canonical_invariants.md` (units ε_p, class groups, Cornacchia representations as algebraic seeds) —
COLLAPSES.** The single strongest reason: every ES solution has coordinates ≤ (9/8)p⁴ (Lemma A, PROVED), while
log ε_p ≍ √p for almost all p. So unit seeds can be used "as numbers" only on a power-sparse set (EVIDENCE: 721,
2184 and 4394 primes up to 10⁵, 10⁶ and 4·10⁶ have ε ≤ p⁴, ≈ √X·log²X). Otherwise they enter only through
residues, i.e. Frobenius data (B2). Representation seeds carry only √−d mod p plus a Planck-scale Hecke angle
(Prop C). An experiment over 5·10⁶ shows no detectable effect of e | v or e | u on e-slice success once
(p/e) = +1 is fixed. Unit seeds are the one angle that passes T1 at its first step (ℚ(√m²) has no unit); they die
at B3.

**W2 `hardness_law.md` (f_II versus χ_p / L(1,χ_p) and congruences; Siegel-zero dichotomy) — PARTIAL (EVIDENCE) /
COLLAPSES as a route.** The strongest finding (EVIDENCE, 148 863 primes p ≡ 1 (24) in [10⁶, 2·10⁷]):
* `log(f_II/log³p) ≈ −0.37·log L₅₀(χ_p)`, with R² 0.27; the effect saturates by y ≈ 50;
* an additive model in p mod prime powers ≤ 97 explains 51% of the log-variance out of sample;
* the residual sd is 0.148, against a pure-Poisson floor of 0.106.

So `f ≈ (congruence factor)·log³p·(near-Poisson)`, and χ_p-structure can cost at most `(log log p)^{O(1)}`.
The dichotomy collapses:
* the GRH horn is empty ((I)2);
* an exceptional χ_D (D unrelated to p) is orthogonal to the slice event (B2/B6);
* an exceptional χ_p itself is the *easy* regime.

**W3 `noncounting_shapes.md` (compactness, overspill/ultraproducts, minimal counterexample, Fermat/Lagrange
descent) — COLLAPSES, with a PROVED profinite dictionary.**
* Prop 1: ES(p) ⟺ p ∉ K := Ẑ \ ⋃ C(a,b,e), with no positivity threshold.
* Prop 2: `(Ẑ^×)² ⊆ K` (from ET Prop 1.6; class-level check for odd m ≤ 151).
* Prop 3: limit points of failures lie in K ∩ Ẑ^×.
* The strongest reason: primes accumulate at every point of Ẑ^×, including (Ẑ^×)² ⊆ K. So any shape that sees p
  only profinitely or first-order is provably blind; membership of p in K is decided at moduli ≍ p (B3/B1).
* Minimal counterexample is idle (ES(3p) is always true; ES(N_e) is irrelevant to N_e's divisor classes).
* Quaternion-norm descent dies at the shape constraint: the j-coefficient must be ±1, which leaves the slice
  `p + 4a²d` (B2).

**For the parent.** Points to verify first:
* W2's numbers: re-run `scripts/bs_wild_hardness.py` on an independent f_II dump.
* W3 Prop 1's (⇒) direction: it rests on the e-slice equivalence of LONGSHOT_PIGEONHOLE Lemma 1.1.

Literature marked "(from memory, unverified)": Hooley 1984, Heath-Brown 1983, Granville–Soundararajan 2003,
Graham–Ringrose, Montgomery, and norm-Euclidean quaternion orders.
