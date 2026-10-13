# bsD_drinfeld_rank_k — the only place where a degree-k "definite" forcing geometry exists: F_q(T) and rank-k Drinfeld modules (O177)

**ES is not solved here.** Labels as in DISCOVERIES.md. No script.

## Idea
bsD_eichler_degree_k Prop 2: over number fields, Diff-parity and the supersingular class set exist only in degree 2
because Br ℝ = ℤ/2. Over K = F_q(T) the place ∞ has Br(F_q((1/T))) = ℚ/ℤ, so **definite central division algebras
of any degree k** exist (invariant 1/k at ∞), and Hilbert/ABHN reciprocity then forces Σ_{finite} inv_v = −1/k ≠ 0: a
genuine order-k existence engine ("some finite place ramifies with invariant in a prescribed coset"). Its geometric
avatar is Gekeler's Deuring correspondence for **supersingular Drinfeld modules of rank k**: their endomorphism rings
are maximal orders in the division algebra of degree k over K ramified exactly at 𝔭 and ∞ (invariants ∓1/k), with a
finite, non-trivial class set (mass formula). Could the F_q[T] analogue of ES (FUNCTIONFIELD_ES) use it?

## Literature
Gekeler, *On finite Drinfeld modules*, J. Algebra 141 (1991) (supersingular rank-r modules, endomorphism algebras,
mass formula); Laumon–Rapoport–Stuhler, *D-elliptic sheaves and the Langlands correspondence*, Invent. Math. 113
(1993) (division algebras of degree d with prescribed invariants at ∞ in the function-field setting);
FUNCTIONFIELD_ES.md Prop 4.1 (Type II sign over F_q[T]: degree parity replaces the archimedean sign, T1 has no
analogue for odd q); KUDLA_ES §1. From memory; page details unverified.

## Analysis
* **Dictionary (Assessment).** Over F_q[T] an ES_q Type II certificate still produces a *binary* Gram matrix
  [[f, 1], [1, f′]] (polynomials) and hence a **quaternion** algebra: only the 2-torsion part of Br(K_∞) is touched.
  Whether B_T is "definite" (ramified at ∞) is decided by degrees/leading coefficients, not by positivity — which is
  exactly why the odd-square obstruction disappears for odd q (FUNCTIONFIELD_ES Prop 4.1, "degree parity replaces the
  archimedean sign"). Consistent with Diff-parity = definiteness (bsD_eichler_degree_k (ii)).
* **To use the order-k engine** one needs certificates whose natural algebra has degree k: k-ary data whose
  "norm" is the ES integer (e.g. certificates factoring through a degree-k étale algebra with a norm form). The ES_q
  equation A/P = 1/X + 1/Y + 1/Z has no such structure in the ET charts (all charts are bilinear/quadratic).
* **Char-p twist.** In F_q[T] the groups (F_q[T]/M)^× contain large p-groups (1 + T·F_q[T]), whose characters are
  Artin–Schreier–Witt, not Kummer — so even the order-k ray characters of ES_q are of a different nature (p-power
  order) than the tame order-k invariants at ∞ (prime to p when p ∤ k). The engine and the target live in different
  parts of the character group.

## Barrier screen
* B5/T1: absent over F_q[T] for odd q (known); the engine would *add* a reciprocity, not remove one.
* B2/H-A: the existence step inside a Drinfeld class set is again "∃ object with given Gram", genus-vacuous as in
  DIFF_DEEP Thm 1.1 unless certificates are degree-k data.
* Hypothesis that would have to fail: "ES certificates are quadratic" — not available in the ET charts.

## Assessment
Spark only (Assessment): the function-field place ∞ is the **unique** setting where an order-k definite forcing
geometry exists, but ES_q certificates are quadratic and do not touch it. Promise 1 (worth a later look only if a
degree-k chart of ES_q is found).
