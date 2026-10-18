# z34_slice_residue — one residue per slice carries Astra sources, ES shots and Type A (O264, goal 1)

## Idea
Astra's source pm² + 1 = qs and López's dual Type A form cp + 1 = qa (B1_LINE §5(c)) are the same equation with
c = m². Make c the variable. Then at each slice q ≡ 3 (4), c lives in the class c_q = −p⁻¹ (mod q).

## Literature
López 2206.10319 / 2404.01508 (Type A, divisor form); ASTRA_BRIDGE Lemma 1.3, Thm 3.4; LATTICE_MEETING Prop 1.1, Thm 1.4.

## Barrier screen
B1 is the condition "c_q is a square class" (Astra sources). It is local, and it is satisfiable on half of all prime
slices for every p. B2: "c_q | h" (Type A) and "c_q ≡ (2k)², k | h" (ES shots) are divisor events in h = (q+1)/4. So no
passage from the local condition to the divisor one is possible without a B2 input.

## Result
PROVED: HARD_PAIR Thm 1.2 and Cor 1.3 (bijection between generalized sources with c | h and Type A; integral-on-arrival
Astra sources = Type A with square c; Type A failure ⟹ no integral source and p + 1 has no prime ≡ 3 (4) in its odd part).
EVIDENCE: exhaustive ≤ 10⁵ (`scripts/z34_dict.py`); 29 % of Type A solutions sit on non-split slices (outside every
Astra lattice); 314 primes have Type A without any integral source.

## Assessment
A clean dictionary entry. Not an existence mechanism.
