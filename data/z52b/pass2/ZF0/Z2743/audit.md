# Z2743 — identify an actual weakly holomorphic input, and the data it loses

**PROVED construction relative to the standard unary theta transformation and Borcherds Theorem 13.3; Assessment of its ES use. ES is OPEN.**

BRAINSTORM/bsC_valence_borcherds.md does not specify an input form or principal part. Its decisive existing statement is Prop.1: “full Heegner divisors — which are non-empty for genus reasons and contain ≫p^{1/2−ε} non-certificate points”. That is an orbit obstruction, not the requested input identification. I downloaded the original Borcherds paper https://arxiv.org/pdf/alg-geom/9609022 and read Theorem 13.3 (pp.48–49): signature (2,b−), input weight 1−b−/2 and representation ρ_L, integral coefficients at exponents≤0, lift weight c₀(0)/2, divisor multiplicities determined by negative coefficients. No converse theorem for a lattice splitting two hyperbolic planes is used in signature (2,1).

Use L=U⊕⟨2M⟩, signature (2,1), discriminant module Z/(2M) with Q(r)=r²/(4M) mod Z. The input belongs to M^!_{1/2}(ρ_L). With the convention that a negative index n corresponds to Heegner discriminant D=4Mn, the certificate slice M=4cd,D=−4Mcp,r=0 calls for the formal principal part
 q^(−cp)e₀.
Its lift, if that principal part is admissible, gives the WHOLE Heegner divisor of discriminant −4Mcp and residue root 0, not the representative condition C_form+1=B_form/2 from the certificate. In general the principal-part obstruction is pairing with every weight-3/2 cusp form for the dual Weil representation; a single prescribed polar term need not extend. Adding polar terms to kill the obstruction changes the divisor. Labeling c(−cp,0) by the number of certificates is tautological and still gives equal multiplicity to the entire Heegner divisor.

Here is a completely explicit, genuinely weakly holomorphic input which does contain the target polar term, rather than leaving existence of an input unverified. Take c=d=1, p=5, so M=4 and D=−80. Put
 Θ₄(τ)=Σ_{r mod8}Σ_{n≡r(8)}q^(n²/16)e_r,
 J=j−744=q^(−1)+196884q+21493760q²+864299970q³+20245856256q⁴+…,
 P₅(J)=J⁵−5a₁J³−5a₂J²+(5a₁²−5a₃)J+(5a₁a₂−5a₄),
 where (a₁,a₂,a₃,a₄)=(196884,21493760,864299970,20245856256).
By direct expansion P₅(J)=q^(−5)+O(q). Since L has the same discriminant form as ⟨8⟩, Θ₄ transforms under exactly ρ_L. Thus
 F=(P₅(J)−2J)Θ₄ ∈ M^!_{1/2}(ρ_L)
is a valid integral Borcherds input. It has no poles on the upper half-plane. Its e₀ principal part is exactly q^(−5)e₀: the 2q^(−1) from Θ₄,₀=1+2q⁴+… is cancelled by −2J.

The FULL principal part, verified by exact integer series arithmetic, is
 q^(−5)e₀
 +(q^(−79/16)+q^(−31/16)−2q^(−15/16))(e₁+e₇)
 +(q^(−19/4)+q^(−11/4)−2q^(−3/4))(e₂+e₆)
 +(q^(−71/16)+q^(−55/16)−2q^(−7/16))(e₃+e₅)
 +2q^(−4)e₄.
There are 20 nonzero polar component/exponent pairs. The only nonzero constant component is −4e₄, so c₀(0)=0 and the Borcherds product has weight 0. This input produces the desired full D=−80 divisor together with divisors at D=−79,−31,−15,−76,−44,−12,−71,−55,−7,−64; negative coefficients give poles, so a positive-weight holomorphic valence argument does not follow. Even removing all unwanted polar terms, when the cusp obstruction permits it, would still not isolate the certificate points within D=−80.

**Assessment:** the exact principal index is identified and an actual weakly holomorphic input is constructed, but its Fourier index labels a Heegner orbit, not individual certificate-shaped representatives. This completes the missing first step without claiming existence of a certificate-encoding principal part. The class-field/orbit issue in the prior memo remains; its separate converse-theorem caveat is not needed for this conclusion.

Reproduce: `timeout 20s uv run python scripts/z52d_p2_ZF0_Z2743_input.py`. The resulting polynomial coefficients, full polar part, and constant terms are in `input.json`; original Theorem 13.3 is in `borcherds_original.txt`. We do not compute a cusp basis to decide whether the *isolated* q^(−5)e₀ principal part is admissible, nor enumerate individual CM points: neither is needed to distinguish the actual input just constructed from a certificate-specific divisor.
