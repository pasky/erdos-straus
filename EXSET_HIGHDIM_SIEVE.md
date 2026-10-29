# EXSET_HIGHDIM_SIEVE — z51 lane 1b (`hidim`)

ES remains OPEN. Internal research note; no external refereeing.

## 0. Outcome ledger (skeleton)

| Round | Question | Status | Review |
|---|---|---|---|
| 1 | Exact large-dimension literature and independent G1 audit | Pending | Pending |
| 2 | Named hypothesis ⇒ RLD-U or T1-min | Pending | Pending |
| 3 | RLD-U ⇒ recognised open statement | Pending | Pending |
| 4 | Non-Selberg weights and enumerable controls | Pending | Pending |

Labels: PROVED (internal proof), CONDITIONAL (explicit hypothesis), CERTIFIED (finite exact check), EVIDENCE, CONJECTURE, Assessment. A restatement of G1–G5 does not count as an advance. Every claimed advance receives hostile Opus review (`anthropic/claude-opus-5-5:high`, deep).

## 1. Definitions, scope, and source audit

**Scope audit (PROVED definitions; no advance claimed).** Write I_N={1≤n≤N:n≡1 (8)}, S=4ℕ∪(8ℕ+7), and

    F_l={−u mod l : u|(l+1), u∈S},  p_l=|F_l|/l,
    V(z)=∏_{3≤l≤z, l prime}(1−p_l),
    A_z(N)={n∈I_N : n mod l∉F_l for every l≤z}.

This is the **direct-endpoint family** actually computed by `scripts/z50_ajopus_chain.c`, and the one with empirical mass slope C_V≈0.74 in z51 CONTEXT. RLD-U here means |A_{N^{1/s}}(N)∖□|≤C_s |I_N| V(N^{1/s}) for fixed s>1. We do not require the additional C_s→1 assertion to discuss T1-cond.

The broader prime-word family in `EXSET_SIEVE_MASS.md` Prop. 2.3 also allows the *other* endpoint v=(n+u)/l to lie in S. It is different: at l=13 the direct set is {6}, while u=2 gives v≡7 (8), hence adds residue 11 to the broader set. Its reported slope ≈1.07 must not be substituted for 0.74. The bound for one family does not automatically imply the corresponding product-normalised bound for the other. Both have cumulative mass Θ(log z) by the same BV/Brun–Titchmarsh argument, keeping the 4ℕ line for the lower bound.

Every direct class is a nonzero quadratic nonresidue modulo l (Theorem E/reciprocity), so all odd squares survive. Class labels are distinct: divisors of l+1 lie in [1,l+1], and the only potential collision is {1,l+1}; 1∉S. The proper-divisor exclusion in the census causes no change on I_N: l=n+u would imply n≡−u (8); for u∈S this is incompatible with l≡−1 (u). Explicitly, u=0 (4) gives l=3 (4) but n+u=1 (4); u=7 (8) gives l=n+u=0 (8). Thus a hit always supplies the proper prime divisor on this fibre.

**Inputs used, not re-proved:** z48–z51 CONTEXT (z51 binds); FRONTIER §§2–4,6–7; BREADTH_Z45 through §15; PR-B index/arithmetic/covers; OAI_DUMP_IMPACT; z48 forest/lower-tail summaries; DISCOVERIES (D)17–31; EXSET_SIEVE_MASS §2; EXSET_ARITH_JANSON_OPUS §§5.5–6. Quasi-RH, if discussed, remains CONDITIONAL on OAI-003. No claim concerns a proof or disproof of ES.

**Research plan after audit.** Test standard named inputs before inventing a new one. Three distinct statements must not be conflated: (a) a prime-tuple upper bound; (b) total-variation approximation of factor/hit vectors; (c) a one-sided estimate only for the all-zero event. Only (c) is RLD-U. We will also test necessary conditions for the reverse inclusion from prime tuples into A_z(N).

## 2. Round 1 — literature and independent G1 derivation

Pending. Exact statements and dependence on dimension; ordinary tuple counts versus shifted factorisation events; weight-class audit.

## 3. Round 2 — implication up

Pending. Try named standard hypotheses first; identify precisely any extra uniformity and any circular reformulation. Square floor and private large primes must be explicit.

## 4. Round 3 — implication down

Pending. An upper bound for a full avoider set is not automatically an upper bound for a larger subfamily avoider set. Require an explicit inclusion/reduction and quantitative scales.

## 5. Round 4 — numerical controls and further attacks

Pending. Scripts `scripts/z51_hidim_*`; data `data/z51_hidim/` (<20 MB). All commands bounded in time and memory. Include odd squares, the hard primes and 14 R-zeros; numerator 8 controls wherever a mechanism transfers.

## 6. Reviews and exact remaining gap

Pending. Commit after each completed section. Do not merge without parent instruction.
