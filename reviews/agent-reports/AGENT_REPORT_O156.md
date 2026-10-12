# AGENT REPORT O156 — hostile triage of BRAINSTORM memos, half A

Deliverable: `reviews/triage-brainstorm-A.md` (branch side-agent/triage-a). ES is not solved; nothing here proves any
case of it.

* **Scope.** All 24 memos `BRAINSTORM/[a-i]*` (addcomb … invol_windmill_signature). None was by O146 or O154 (checked
  headers + git log), so none was excluded.
* **Verdicts.** AGREE ×24, no DISAGREE. No "COLLAPSES to Bx" reduction in this half is invalid. The un-barriered
  remainder is the escapes the memos themselves mark UNCLEAR: parity identities (windmill), two-variable identities
  on binary forms, and Fermat-type GoN. For the last of these I made the precise obstruction explicit: the
  congruence modulus depends on the unknown.
* **Overclaims found (minor; no verdict changes):**
  * anal_dirichlet Prop A.2 needs f(p) ≤ p^{o(1)} (known: p^{3/5+o(1)}), so as proved it holds on Re s > 3/5;
  * gon_lll's "genus half is a theorem" has an uncited least-prime-non-residue-in-class step;
  * ident_invariants Lemma 3.1 is scoped to the diagonal f = f';
  * hardness_law's fixed exponent vs anal_euler's 1/log p decay (reconciled in the triage);
  * elliptic under-claims: non-torsion per point is PROVED via Mazur.
* **Independent checks** (`scripts/triage_*`):
  * the Cayley P2/P4 identities (sympy);
  * Thm A.1 of graph_cayley_moves: 2·10⁵ random mixed-index real chords, 0 third points in Ω;
  * the k = 21 hard-prime identity example (p = 774508921 ≡ 361 mod 840, exact solution);
  * the windmill GF(2) signature test **restricted to n ≡ 1 (24)**: still null, so the memo's E1/E2 design did not
    hide a class-restricted identity.
* **Top 5:**
  1. windmill parity / cross-slice coupling: theory-only. Construct a coupling or prove a bounded-complexity
     obstruction; this is the last un-barriered family.
  2. Two-variable Type I identities on u² + kv²: a well-posed obstruction question via Pythagorean specialisation or a
     two-variable Thm C trap.
  3. GoN + aggregation: expected outcome is an obstruction lemma, "no lattice encoding with point-independent
     modulus".
  4. ES over F_q[t] at fixed q: a side question.
  5. The untested unit-residue (ε_p mod q) regression: a 30-minute sanity check.

  Promise scores are ≤ 2 throughout. Nothing in half A deserves a full research agent at promise ≥ 3. Items 1–2 are
  each worth one focused, bounded task.

Stopping here for parent review.
