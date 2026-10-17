# z25 memo 1 — amplification laws are total reductions (O253)

Verdict: OBSTRUCTION (Assessment + PROVED Prop 2.1 in AMPLIFY_EXCEPTION.md). Promise 1/5.

* An input-only law "p₀ ∈ E ⟹ F(p₀) ⊆ E" is literally the family of reductions ES(q) ⟹ ES(p₀), q ∈ F(p₀).
* If F(p₀) has the growth needed to contradict Vaughan (Thm 1.1, condition (1.1)), F(p₀) must meet the set of
  integers covered by the small-modulus ET classes used in Vaughan's sieve (otherwise F(p₀) is inside the sieve's
  avoider set and obeys the same bound). So the law, made explicit, converts an explicit *small-modulus* witness at
  some q into a witness at p₀. Amplification does not bypass ES(p₀); it moves the whole difficulty into the
  reduction step.
* Combined with Thm 3.2 (T1 adversary): a small-modulus witness at q is invisible to p₀ whenever p₀ is a square
  modulo that modulus, which for p₀ ∈ 𝓜 holds for all {2,3,5,7}-smooth moduli. So the reduction must be
  non-congruential or must find, at q, a witness whose modulus contains a non-residue prime of p₀.
* Mirror (B6): averages over p say nothing at one p *unless* a total reduction from a large set exists; an (A)-law
  is exactly such a bridge, and a bridge from Vaughan's covered set is ES(p₀) with a detour.
Next step (if any): look for reductions using *sizes* (x, y, z, d) rather than residues — none found here.
