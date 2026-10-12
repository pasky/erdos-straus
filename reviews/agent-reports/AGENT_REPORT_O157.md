# AGENT REPORT O157 — triage red-team B (brainstorm memos j–z + corr/adv/tech)

Deliverable: `reviews/triage-brainstorm-B.md` (26 memos; raw sub-reviewer parts in `reviews/triage-B-parts/`,
spot-check scripts `scripts/triage_{corr,adv,tech,logic,nonab,padic,prob}.py`). Memos not edited.

Headlines:
* **No false negative that actually escapes.** 9/26 memos get DISAGREE, but always for *scope overreach*: "COLLAPSES
  to B2/B3/B4" is asserted for a whole angle when only a fixed-Θ₀ / fixed-form / power-error instantiation collapses.
  Thm 2.2(iii) needs Θ₀ fixed independently of p; Prop 2.3 bounds main terms, not errors; B4 covers only transparent
  coset covers. Every residue reduces to the already-open hatches H-A/H-B/H-D/H-F. Recommend that ledger citations
  read "PARTIAL → H-x" instead of "COLLAPSES".
* **16 concrete errors** in memos, all re-checked (table §0.3). The load-bearing ones are nonab_frobenius_redei D2,
  padic_adelic_scaling Prop B, rational_to_integral M3(b), prob_lll Prop 3.2, adv_stacked_primes D3,
  logic_divisibility_lgp's CRT step, and technique_transfer's frame/subgroup "⇔".
* **Brief template error:** B2 says Σ_{p≤N} f(p) ≍ N log³N. Over primes, ET give N log²N (log log for the upper
  bound; the average f(p) is ≍ log³p). Fix it in the template.
* **One structural crack (H-D), §0.4.** In groups with trivial abelianisation (A₅), some conjugacy classes contain no
  squares. So "Frob_p ∈ C" passes T1 for free and is not congruence data. No ES mechanism attached.
* **Top-5 (all 2/5; nothing deserves a full agent now):**
  1. corr_parity_layers (H-B sign/size layers);
  2. the small-e "−1 ∈ Σ_e((p+e)/4)" cluster (three memos dismissed it beyond B4's scope);
  3. nonab_frobenius_redei;
  4. padic_functionfield_igusa (the F_q[T] analogue loses the square obstruction at q ≡ 1 (4); a test bed);
  5. adv_stacked_primes (liminf question for primes that are QR to all q ≤ y(p)).
* No PROVED by-product in this half is a plausibly new theorem about ES. Minor plausibly-new items are listed in §2.

Process note: the per-memo paragraphs were drafted by 7 deep-mode sub-reviewers (some committed their parts
directly). O157 re-verified the key counterexamples itself (incl. the F₅[T] one with sympy, p=433/e=19, p=73 frame,
the ET normalisation against DISCOVERIES (D)32) and calibrated the verdicts in §0.1/§2. ES is not solved.
