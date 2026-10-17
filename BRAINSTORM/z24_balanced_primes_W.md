# z24_balanced_primes_W — GRH + a Linnik statement for balanced primes ⇒ e*(p) ≤ (log log p)^{2+o(1)} (O252; FORCED_WINDOW §4)

**Idea.** Make z12_grh_lattice_gap's "missing input" a named hypothesis and prove the conditional theorem.
**Result.** Covering ⟺ balanced relation lattice up to a factor 2 (Prop 4.1, PROVED). Call q (y, L)-balanced if the squares of
the odd primes ≤ y generate U_q and their relation lattice has cube covering radius ≤ L (p-independent property).
**Hypothesis W(y, L) (p-dependent; R-O252 repair: a fixed X for all p is false, take p ≡ 1 mod 8∏_{q≤X} q):** for every large
p ≡ 1 (8) there is a balanced q ≤ X(p) = C φ(8P)² log⁴ p, q ≡ 3 (8), q ≡ −p (mod P), (q/p) = −1 (P = ∏ odd primes ≤ y).
**Thm 4.3 (CONDITIONAL on W; GRH only sizes the candidate set):** e*(p) ≤ L − 1. With L at random-lattice size and y = log₂p·log₃p:
e*(p) ≤ (log log p)^{2+o(1)} (Cor 4.4). Lower bound for any covering method: (log log p)^{1−o(1)} i.o.
**Barrier screen.** Not ES-in-disguise (W never mentions certificates or cap 0; p enters via one quadratic character). The
difficulty is the P-loss: the unbalanced primes (which for fixed y include positive-density Chebotarev sets, e.g. all
generators cubes — R-O252 repair: no density-one claim) cannot be kept out of a class mod P ≈ X^{1/2} by any known bound. W is false as an all-q statement (Prop 5.2) — it must be "some q per class".
**Numerics (EVIDENCE).** y = 7 (48 classes mod 840) and y = 11 (480 classes mod 9240): every admissible class contains a q with
(L_min + 1)/|U_q|^{1/k} < 1.372 resp. 1.472 (balance only; the (q/p) = −1 part of W is not tested); worst single q ≈ 6 (z24_balanced).
**Label.** CONDITIONAL theorem (W); exponent 2 + o(1) is CONDITIONAL on W at random-lattice L (Assessment for that L).
