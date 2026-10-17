# z24_balanced_primes_W — GRH + a Linnik statement for balanced primes ⇒ e*(p) ≤ (log log p)^{2+o(1)} (O252; FORCED_WINDOW §4)

**Idea.** Make z12_grh_lattice_gap's "missing input" a named hypothesis and prove the conditional theorem.
**Result.** Covering ⟺ balanced relation lattice up to a factor 2 (Prop 4.1, PROVED). Call q (y, L)-balanced if the squares of
the odd primes ≤ y generate U_q and their relation lattice has cube covering radius ≤ L (p-independent property).
**Hypothesis W(y, X, L):** every class a ≡ 3 (8) mod 8P (P = ∏ odd primes ≤ y) contains, for every p, a balanced q ≤ X with
(q/p) = −1. **Thm 4.3 (CONDITIONAL on GRH + W):** e*(p) ≤ L − 1. With L at random-lattice size and y = log₂p·log₃p:
e*(p) ≤ (log log p)^{2+o(1)} (Cor 4.4). Lower bound for any covering method: (log log p)^{1−o(1)} i.o.
**Barrier screen.** Not ES-in-disguise (W never mentions certificates or cap 0; p enters via one quadratic character). The
difficulty is the P-loss: unbalanced primes form a density-zero set that the trivial bound cannot keep out of a class mod
P ≈ X^{1/2}. W is false as an all-q statement (Prop 5.2) — it must be "some q per class".
**Numerics (EVIDENCE).** y = 7 (48 classes mod 840) and y = 11 (480 classes mod 9240): every class contains a q with
(L_min + 1)/|U_q|^{1/k} ≤ 1.37 resp. 1.47; worst single q ≈ 6 (z24_balanced).
**Label.** CONDITIONAL theorem (GRH + W); exponent 2 + o(1) is CONDITIONAL on W at random-lattice L (Assessment for that L).
