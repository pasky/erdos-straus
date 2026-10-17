# z28_espectrum_share — joint-factorisation lifts only transport the e-spectrum (O257; NONCONG_LIFTS Prop 1.4)

**Idea.** The most natural size-reading lift shares the source's factored number: N_θ(p) = λ·N_θ′(q) identically in q
(p = αq + β). Then the source's full factorisation k a′b′d′ is available at p. Does that give information?
**Result (PROVED, algebra).** Exactly four share relations exist ((II←II) e = αe′ − β; (II←I) e′ | α, e = α/e′ − β;
(I←II) e = 1, αe′ − β = 1; (I←I) e(α − βe′) = e′). For each, every slice with the target e is automatically
compatible, so validity at w′ ⟺ (θ, e) ∈ Spec(p): the source contributes only its e-value. A share law is total iff
f(Spec(q)) ⊆ Spec(p) (Spec = set of (type, e) of witnesses).
**Literature.** ET parametrisation (Prop 1.3); "joint factorisation" hatch H-A of the barrier map; BRAINSTORM
corr_joint_factorisation.md (different: correlations of Type I/II events at one p).
**Barrier screen.** B2: Spec(p) membership is exactly the e-slice divisor event −1 ∈ Σ_e(N). T1/B5: at square targets
every share lift fails (classical). (J)41: numerator-blind.
**Cheap numerics.** `scripts/z28_matched.py` (α = 1): at the fixtures 97, 193, 313, 3361, 5209 0 share transports among
335 matched source witnesses; over 273 Mordell primes ≤ 10⁵ 1606 share transports among 106 322 witnesses (1.5%),
never total.
**Assessment.** PROVED reduction; negative. Size information is erased by exact sharing.
