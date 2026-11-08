## Content from https://projecteuclid.org/journals/notre-dame-journal-of-formal-logic/volume-34/issue-3/Quadratic-residues-and-x3y3z3-in-models-of-rm-IE_1-and/10.1305/ndjfl/1093634730.pdf

Title: 1093634730.pdf

URL Source: https://projecteuclid.org/journals/notre-dame-journal-of-formal-logic/volume-34/issue-3/Quadratic-residues-and-x3y3z3-in-models-of-rm-IE_1-and/10.1305/ndjfl/1093634730.pdf

Number of Pages: 19

Markdown Content:
420 

Notre Dame Journal of Formal Logic 

Volume 34, Number 3, Summer 1993 

# Quadratic Residues and x3 + y3 = £

# in Models of IE X and IE 2

STUART T. SMITH Abstract It is unknown whether the fragment of arithmetic IE\ (or even the stronger system JΔo) proves that every odd prime has a quadratic nonresidue. We show that one direction of the quadratic reciprocity law holds in ΪE\ when one of the primes is standard. Thus an odd prime q which has no quadratic nonresidues must satisfy ί * J = 1 for every standard prime p. We show that if q is a prime 

Φ 2, 3 in a model of ΪE\ and n = 1, 2, 3, or 4, then q — x 2 + ny 2 for some JC, y if and only if ί ~ j = 1. This result for n = 3 enables us to prove in /ϋ^ that 

x3 + y 3 = z 3 has no nontrivial solution. 

1 Introduction A number of articles have appeared which were motivated by the question of how much induction is necessary in order to prove elementary results in number theory. More precisely, axiom systems are considered which contain the axioms for discretely ordered semirings (i.e, 1 is the least positive element) together with the induction scheme for some class of formulas in the language £ = {+, , < , 0,1}. Peano arithmetic (in which induction holds for all ^-formulas) is the best known such system, but it is too strong for our purposes, as it proves all of the results of classical number theory. We are interested in weaker systems, the so-called fragments of arithmetic. The weakest such system is open induction (IOperi), in which induction is as-sumed only for quantifier-free formulas. Shepherdson showed in [7] that IOpen is too weak to prove the irrationality of A/2, or to prove that x3 4- y3 = z 3 has only trivial solutions. The model he constructed contains no nonstandard primes, so in particular the set of primes is not cofinal. In Wilkie [13], van den Dries [2], Smith [9], and Smith [11], open induction is strengthened by the addition of algebraic axioms, such as normality or the existence of g.c.d/s, but the resulting systems are shown still to be very weak. 

Received August 10, 1992; revised November 18,1992 QUADRATIC RESIDUES 421 A much stronger system is / Δ o , in which induction is assumed to hold for all formulas having only bounded quantifiers. (See Paris and Wilkie [6].) As noted in Macintyre and Marker [5], it is unknown whether 7 Δ 0 proves the cofinality of the set of primes, or the existence of quadratic nonresidues for all odd primes. It is the latter question which interests us here. We will in fact work in IE U an intermediate system between IOpen and 7 Δ 0 .

IE U or bounded existential induction, was introduced by Wilmers in [14]. In IEγ we assume induction holds for all bounded existential formulas. (Actually, as is noted in [14], no proof is known that IE\ is strictly weaker than 7Δ 0 .) Some of the algebraic properties of models of IE\ are developed in [9], Smith [10], and Smith [12]. In Section 2 we review the definitions and elementary facts about the systems IE n.We show in Section 3 that we can use an inductive argument in IE\ on the modulus 

m to show that certain finite elements are quadratic nonresidues for m, provided m

satisfies certain congruence conditions. This enables us to prove one direction of the quadratic reciprocity law when one of the primes is standard. This in turn enables us to place limitations on odd primes which have no quadratic nonresidues, if such a thing is possible in a model of IE\. 

In Section 4 we show that a result for H is provable in IEχ for small values of 

n. Specifically, we show in IE X that if q is a prime Φ 2, 3 and n = 1, 2, 3, or 4, then 

q = x2 4- ny 2 for some x and y O ί — j = 1. Our descent argument breaks down for larger n> and in any case this result does not hold in N for n = 5, since ( ^ ) = 1 but 7 is not of the form x2 + 5y 2.In Section 5 we use the above characterization of primes of the form x2 + 3y 2

to show that in IE 2, x 3 + y 3 = z 3 has no nontrivial solutions. The proof is adapted from an argument due to Browkin which appears in Sierpinski's book [8]. 

2 Preliminaries In this section we review the definitions of the axiom systems IE n

and list some basic results. Definition 2.1 [14] Let £ be the first-order language {+, , <, 0,1}. Define 

Eo — U o = {θ(x) : θ(x) is an open formula}, £ n + i = {3y 1 < h(x) '"3y m< tm(x)θ(x, yί. ym) :

θ eU n and h, ..., tm are £ - terms}, Un+i = {Vyi < h(x) Vy m < t m(x)θ(x, yi y«) : 

θ e E n and tu...,t m are & - terms), 

Vw = {θ(x) : θ is logically equivalent to an ^-formula and to a 

Un—formula}. 

If T is an £-theory, the definition of V n relativizes to T. Thus ψ(x) is provably Vn

over T if ψ(x) is equivalent over T both to an is^-formula and to a Un-formula. We are particularly interested in formulas which are provably V x over a given theory T. For suppose ψ(x) is such a formula and suppose that φ (x) is some quantified formula which contains ψ (3c) as a subformula. Then for purposes of determining the quantifier complexity of φ we can regard ψ as though it were quantifier-free. For example, 

3y < t(x)ir and 3y < t(x)->ψ 422 STUART T. SMITH will both be equivalent over T to E\ -formulas. (Abusing terminology, we will refer to them both as Ex -formulas.) 

Definition 2.2 [14] (i) The system IE n consists of the axioms for discretely ordered semi-rings, together with the induction schema for all ^-formulas θ: 

Vy [(0(0, y) A Vx (0(χ, y) -* θ(x + 1, y))) —> Wxθ(x y y)]. 

(IE 0 will be denoted by IOpen.) 

(ii) The system LE n consists of the axioms for discretely ordered semirings, together with the following least number principle for all En -formulas θ: 

Vy [3xθ(x, y) —> 3x (0(χ, y) Λ Vz < x-0(z, y))]. Semirings which are models of IE n or LE n will be denoted by M, M\ etc. The basic properties of IE n are developed in [14]. We will need the following two facts: 

Theorem 2.3 [14] For every n > 0, we have lEn+i = » IE n <=^ LE n.

Lemma 2.4 [12] Let θ(x, y) be an E n-formula. Then 

IE n h VyΓί 3wθ(w, y) A 3zVx(0(x, y) —> x < zΛ 

—• 3 z ^ ( z , y) Λ VJC(0(JC, y) —• x < z)")l. 

77zαί w, /£„ proves that any nonempty bounded E n~definable set has a greatest ele-ment 

We also need to know that certain relations are provably Vi over 1E\ or IOpen. 

Lemma 2.5 Kaye [4] x\y is provably Vi over IOpen. Proof: Here x\y means x divides y, where 0|0 and Ofy for y φ 0. The formula x\y 

has the Ex definition 3z < y(xz = y), and is equivalent over IOpen to the ί/i-formula y = 0 v [ y > 0 Λ V z < yVr < y(y = zx + r — > r = 0)]. 

Lemma 2.6 [4] c = y mod z is provably Vi over IOpen. Proof: The formula x == ymodz has the 2?i definition (3ιt; < x + y)[x = w^z + y v y = wz + c], and is equivalent over IOpen to the formula (z = 0 Λ X = y) v [z > 0 Λ Vw < x 4- y((# = y + iϋV)/ = jc4-u)) -> z\w)]. This formula is J7i by Lemma 2.5. 

Lemma 2.7 [14] IE X \- VJC[JC > 0 -> Vy((jc, y) = 1 -> 3z < x(yz = 1 mod x))]. 

Corollary 2.8 IfM (= /£i and /? w a prime in M, then M/pM is afield. More generally, ifm e M, m > 1 and a e M is such that (a, m) = 1, ί/zen a w invertible in M/mM. 

Lemma 2.9 [9] (x,y) = z is provably Vi overlEγ. Proof: If z = 1, this follows from Lemma 2.7. The proof for arbitrary z in [9] is a generalization of Wilmers' proof for z = 1. Finally, we note that one can prove in 72^ (in fact in IOpen) that x s y mod z

defines a congruence relation, and if z > 0 then every x is congruent to a unique w such that w < z. QUADRATIC RESIDUES 423 

3 Quadratic residues Let M \= IE X and suppose m e M,m > 1. For any a e M, 

we can ask whether the congruence x2 = amodm has any solutions in M. As in the case of N, if the answer is yes and (a,m) = 1, then we say that a is a quadratic residue for m; otherwise a is a quadratic nonresidue for m. 

We note some elementary facts. 

Lemma 3.1 Let M |= ΪE\ and suppose m e M, m > 1. Then for any a,b e M, we have: (i) Ifx 2 == amodm has a solution and x 2 = bmodm has a solution, then x 2 =

abmodm has a solution, (ii) Ifx 2 = amodm has a solution where we assume also that (a, m) = 1, and if x2 = bmod m has no solution, then x 2 = abmod m has no solution. (Hi) Ifx 2 ΞΞ a mod m has a solution and m'\m, then x 2 = a mod m r has a solution. Proof: (i) and (iii) are trivial. To prove (ii), suppose c e M i s such that c2 =a modm. Since (α, m) = 1, clearly (c, m) = 1, so by Lemma 2.7, there is a d e M 

such that cd = I modm. Then d2a = d 2c2 = I modm, so if e e M were such that e2 = abmodm we would have (de) 2 = d 2ab = bmodm, contradicting our assumption on b. 

When m e M is a prime, say m = q,v/e can define the Legendre symbol ί £ Jin the usual way: 

# [ ° i f «i c '

I - J = I 1 if q\c and c is a quadratic residue for q ,^ I—1 if # {c and c is a quadratic nonresidue for q. 

The generalization of this symbol to the case where q is composite (the Jacobi symbol) does not have the properties we will need, so we will use only the Legendre symbol. As is implied by the previous paragraph, we are particularly interested in the case where m e M is prime. If m is a standard prime, say m = p e N, we have that the usual results from N hold (in addition to those listed in Lemma 3.1). Specifically, half of the elements 1, 2, , £γ- of M/pM are quadratic residues and the other half are quadratic nonresidues; also the product of two quadratic nonresidues is a quadratic residue. The proofs of these facts use counting arguments which do not go over to the non-standard case. Thus in [5] the question is raised as to whether one can prove in 7 Δ 0 that every prime has a quadratic nonresidue. (They note that if we adjoin the Δ0-Pigeonhole Principle to / Δ o , then the proof can be carried out.) In N we have the famous law of quadratic reciprocity, which says that if p and 

q are distinct odd primes then ( f ) = \Λ) unless both p and q are congruent to 3 modulo 4, in which case ί £ ] = — ( ^ ) The question arises as to what happens to this law in M \= IE X (of course it continues to hold if both primes are standard). We will show that if p is standard and q is an arbitrary prime, t h e n ί ^ j = 1 =^ ί 5- J = 1 unless both primes are congruent to 3 modulo 4, in which case (^ j = 1 =» (%.\ = _ i . in particular, we will show that many elements (if not most primes) of M have quadratic nonresidues. Our first result in this direction is the following: 424 STUART T. SMITH 

Lemma 3.2 Let M |= IE\ and suppose m e M, m = 3 mod 4. Then - 1 w α

quadratic nonresidue for m. Proof: Note that although our language £ does not contain a minus sign, the above conclusion can be expressed as    

> -«3JC(JC 2+ 1 Ξ = 0 mod m).

By the remark after Lemma 2.9, it suffices to consider those x for which x < m thus —1 is a quadratic nonresidue for m if and only if 

M \= ->3x < m(x 2 + 1 = Omodm). 

Using Lemma 2.6, we see that the set ofmeM such that m == 3 mod 4 and —1 is a quadratic residue for m is £Ί -definable. If it is nonempty, it must have a least element a e M. There is by assumption a b e M such that b < a and 

b2 + 1 Ξ 0 mod α; replacing 6 by a -b if necessary, we can assume that b is even. The above congruence implies 

b2 + 1 = ac 

for some c e M. Since b < a, we have «c = ft 2 + 1 < a2 and so c < a. Now ί) 2 + l = I mod A because b is even, hence ac == Imod4. But α Ξ= 3 mod 4, so c = 3 mod 4 as well. The equation b2 + 1 = ac implies that b2 4- 1 = Omod c, so 

M \=Ίx(x 2 + l==0modc) where C Ξ 3 mod 4. This contradicts the minimality of a. 

In particular, if M \= IEχ and q e M is an odd prime for which — 1 is a quadratic residue, then q = 1 mod 4. We would like to prove the converse, which of course holds when q is standard. The problem is that the analogous descent argument to Lemma 3.2 does not work. Even in /Δo, where we can restrict this argument to primes, there does not seem to be any contradiction to be derived from assuming that 

q == 1 mod 4 is the minimal prime for which—1 is a quadratic nonresidue. Moreover, the usual methods for finding a square root for - 1 modulo q involve functions, such as the factorial function, which are not available to us even in / Δ o .We can prove related results by a similar argument, where in general we will have to consider more cases. For example, the following result (actually its corollary) will be needed later in the discussion at the end of this section. 

Lemma 3.3 Let M (= IE\ and suppose m e M, where m = 5, 8,10,11,16,17, 20, 22, or 23 mod 24. Then —3 is a quadratic nonresidue for m. 

Proof: As in Lemma 3.2, we let a e M be the minimal counterexample for m and we let b e M be such that b < a and b2 4- 3 = 0 mod α; replacing b by a - b if necessary, we can assume that 3jb. Thus b2 + 3 = = 4,7 or 19 mod 24. Now b2 + 3 = ac for some c e M; since b < a and a > 5 (by the congruence condition in the hypothesis), then b2 + 3 < a2 and so c < a. Obviously - 3 is a quadratic residue for c; it remains only to show that c satisfies one of the congruences in the hypothesis of the lemma, and then c will contradict the minimality of a. We consider the three possible values for b2 + 3 modulo 24 in turn. QUADRATIC RESIDUES 425 (a) Suppose b2 + 3 = 4 mod 24. Since b2 + 3 = ac we have αc Ξ= 4 mod 24; thus α φ 8mod24 and α # 16mod24. If α = 5,11,17, or 23mod24 then 

c = 20 mod 24, and vice versa. If a = 10 or 22 mod 24 then c = 10 or 22 mod 24. Thus c satisfies the hypothesis of the lemma. (b) Suppose b2 + 3 = 7 mod 24, so αc = 7 mod 24; then a φ 8, 10,16, 20 or 22 mod 24. If a Ξ= 5 mod 24 then c = = 11 mod 24 and vice versa; if α = 17 mod 24 then c =Ξ 23 mod 24 and vice versa. (c) Suppose b2 + 3 = = 19 mod 24, so ac == 19 mod 24. Again a φ 8,10,16, 20, or 22 mod 24. If a = 5 mod 24 then c = 23 mod 24 and vice versa; if a ==11 mod 24 then c = 17 mod 24 and vice versa. 

Corollary 3.4 Let M \= IEγ and suppose q e M, q > 3 is prime and —3 is a quadratic residue for q. Then q = 1 mod 6. We can similarly prove: 

Lemma 3.5 (i) Let M (= IEγ and suppose m e M, where m === 3 or 5 mod 8. Then 2 is a quadratic nonresidue for m. (ii) Let M (= IE\ and suppose m e M f where m = 5 or 7mod 8. Then —2 is a quadratic nonresidue form. 

Corollary 3.6 (i) Let M \= IE\ and suppose q e M ispήme and 2 is a quadratic residue for q. Then q == 1 or 7 mod 8. 

(ii) Let M (= IEχ and suppose q e M is prime and —2 is a quadratic residue for q. Then q = 1 or 3 mod 8. We can continue in this manner, eventually salvaging one direction of the qua-dratic reciprocity law when one prime is standard. 

Lemma 3.7 Let M \= IEγ and let p e M be a standard prime such that p =1 mod 8. Let m e M, p\m, be a quadratic nonresidue for p. Then p is a quadratic nonresidue for m. Proof: We first must show that the set of m e M for which the lemma does not hold is El-definable. Because p is standard, the assumption -«3x < p(x 2 === mmodp) 

can be replaced by a finite disjunction of congruences, the choice of which varies with p. For example, if p = 17 then m is a quadratic nonresidue for p if and only if m Ξ= 3, 5, 6, 7,10,11,12, or 14 mod 17. By Lemma 2.6, this formula is provably Vi over/Ei. The set of counterexamples for m is thus Ei-definable, and we assume it is nonempty. By LE X, it contains a least element a e M . We will show that a is infinite. Clearly a > 1, so if a is finite we can write a = 2 r >s, where r > 0 and s is odd. Now 2 is a quadratic residue for p, hence so is 2 r ; in order for a to be a quadratic nonresidue for p, it must be the case that a (hence s) has an odd prime factor q which is a quadratic nonresidue for p. Since q is standard, by ordinary quadratic reciprocity we have that p is a quadratic nonresidue for q (and so for a). But then a is not a counterexample. Now for some b < α, we have 

b2 Ξ pmoda, 

where by replacing b by a - b if necessary we can assume that p\b. Thus 

b2 = p ± ac 426 STUART T. SMITH for some c e M, c > 0. But a is infinite and p finite, so the sign above cannot be negative, and we have b2 = p + ac. Furthermore, b < a and so c < a; also clearly 

p\c. Looking modulo p, we have 

0 φ b 2 = acmod p, 

where ( f ) = —1 Hence ( T ) = —1> whereas since b2 = p + ac we have that /? is a quadratic residue for c. Since c < α, this contradicts the minimality of α. The corresponding lemma for p == 5 mod 8 is more complicated, since in this  

> c a S

## e (j) = -i. 

Lemma 3.8 Let M (= 7^i and let p e M be a standard prime such that p =

5 mod 8. Letm e M, p\m, satisfy one of the following conditions: (a) m = 0 mod 8, or (b) m = 1, 3,4, 5, or 7 mod 8 and m is a quadratic nonresidue for p, or (c) m = 2 or 6 mod 8 and m fa a quadratic residue for p. Then p is a quadratic nonresidue for m. Proof: Clearly the set of counterexamples for m is Ex -definable, as in Lemma 3.7. We assume that it is nonempty and we let a denote its minimal element. We show that a is infinite. Clearly a > 1, and if a is finite we can write a = 2r s with r > 0 and s

odd. If r > 3 then a = 0 mod 8; but since /? = 5 mod 8, we have that p is a quadratic nonresidue for 8, hence for a. This contradicts the assumption that a is a counterexample to the lemma. Thus r < 2. If r = 0 or 2 then a = 1, 3,4, 5, or 7 modulo 8, so by assumption (jj = —1. Moreover, α = s or α = 4s, so (j j = - 1 . In particular, s > 1 and s has an odd prime factor q such that ί3- J = - 1 . By ordinary quadratic reciprocity, (^ J = - 1 , so p is a quadratic nonresidue for a. Again this contradicts the assumption that a is a counterexample. If r = 1 then a — 2s with s odd, so a ΞΞ 2 or 6 mod 8. By assumption, then, ί - ) = 1; but ί - j = — 1 so ( - ) = —1 as well, and the argument continues as above. Therefore a must be infinite. As in Lemma 3.7, we have 

b2 = p + ac 

for some b < a,c < a such that p\b\ therefore p\c either. Modulo 8 we have 

b2 ΞΞ 5 + αcmodδ, so α # 0 mod 8. Therefore one of cases (b) or (c) applies. We deal with them in turn, (b) If a ΞΞ 1, 3,4, 5, or 7mod 8 and (jλ = - 1 , then since b2 ΞΞ acmod p

we have ί - ] = — 1 as well. In the congruence b2 Ξ= 5 4- acmod 8 there are two possibilities: QUADRATIC RESIDUES 427 (1) Suppose b is odd. Then b2 = 1 mod 8, so ac = 4 mod 8. If a = 1, 3, 5, or 

7 mod 8 then c = 4 mod 8 and vice versa, so c contradicts the minimality of a. 

(2) Suppose b is even. Then b2 is even, so ac is odd. Thus a and c are both odd, so again c satisfies the hypotheses of case (b) and contradicts the minimality of a. 

(c)Ifα = 2 o r 6 m o d 8 a n d ί ^ j = l,thensincefe 2 = acmod p we have ( - ) = 1 as well. Now since a is even and p is odd, the equation b2 = p + ac implies that b is odd. Thus b2 = 1 mod 8, and since p == 5 mod 8 we must have ac = Amod8. Since 

a = 2 or 6 mod 8, then c Ξ= 2 or 6 mod 8 also, and so c contradicts the minimality of 

a. 

Lemmas 3.7 and 3.8 together enable us to deal with standard primes p such that 

p = 1 mod 4. When we turn to the case where p = 3 mod 4, the situation becomes more complicated; for instance, when m = q is a standard odd prime, we must distinguish between the cases q == lmodA and # = 3 mod 4. The following two lemmas provide the analogues to Lemmas 3.7 and 3.8. 

Lemma 3.9 Let M \= lEχ and let p e M be a standard prime such that p =7 mod 8. Letm e M, p\m, satisfy one of the following conditions: (a) m = 0 or A mod 8 (i.e. 4\m), or (b) m == 1, 2, or 5 mod 8 and m is a quadratic nonresidue for p, or (c) m == 3, 6, or 7 mod 8 and m is a quadratic residue for p. Then p is a quadratic nonresidue for m. 

Proof: As in the previous cases, the set of m € M for which the lemma does not hold is 

Eι -definable. Assume it is nonempty and let a e M be the minimal counterexample. We show that a is infinite. Since 1 does not satisfy any of the conditions in the hypothesis of the lemma, we have a > 1. Suppose a is finite; then, we can write a = 2 r s e N with r > 0and s odd. If r > 2 then 4\a; but p = 3mod 4 so p is a quadratic nonresidue for 4, hence for a. This contradicts the assumption that a is a counterexample to the lemma. Hence r = 0 or 1, and case (a) does not hold. Now (jλ — 1. In case (b), then, we have that s == Ior5mod8(i.e. s = Imod4) 

a n d ( ^ j = —1. Thuss > 1. Writes = t2u e N,where uissquarefreeand(ί, u) = 1. Then ί - j = —1, so M > 1. Also, since s = imodA and ί 2 = imodA, we have M =Ξ ImodA. 

Suppose w has a prime factor # such that q = ImodA and ( p) = —1. By ordinary quadratic reciprocity, p is a quadratic nonresidue for q, hence for a. This contradicts the assumption that a is a counterexample. Thus if we write u = vw e N where all of the prime factors of i; are congruent to 1 modulo 4 and all of the prime factors of w are congruent to 3 modulo 4, the previous paragraph shows that υ is a quadratic residue for /?, hence w is not. (In particular, 

w > 1.) Now υ = 1 mod 4, hence u; = 1 mod A as well; since w e N is squarefree, it has an even number of prime factors. An odd number of them must be quadratic nonresidues for p and an odd number must be quadratic residues for p. In particular, there is at least one q == 3 mod A dividing w which is a quadratic residue for p. By ordinary quadratic reciprocity, p is a quadratic nonresidue for q, hence for a; this contradicts our assumption on a. Thus case (b) does not hold for a. 428 STUART T SMITH We are left with case (c). Here we have 5 Ξ 3 O Γ 7 mod 8 (i.e. s == 3 mod 4, so in particular s > 1) and ίηΛ = 1. Again writing s = ί 2w, this time u = 3mod 4. Let u = υw as before; again υ must be a quadratic residue for p, hence so is w. But this time w = 3 mod 4 so w has an odd number of prime factors; therefore again w

has at least one prime factor q = 3 mod 4 such that (^ J = 1. As before, this leads to a contradiction. We conclude that a must be infinite. As in Lemma 3.7, we have 

b2 = p + ac 

for some b < a, c < a such that p\b, so p\c either. We consider the three cases in the lemma in turn. (a) If α Ξ 0 or 4 mod 8, then b must be odd, hence b2 = 1 mod 4. But then the equation b2 = p + ac yields 1 = 3 + 0-cmod4, which is impossible. Therefore this case does not apply. (b) Suppose a = 1,2, or 5 mod 8 and (^ j = - 1 . Since 0 φ b 2 = acmod p> 

we also have that ί ^ j = —1. On the other hand, since & 2 = p + αc, clearly p is a quadratic residue for c. Considering the equation b2 = p + ac mod 8, there are three possibilities for b2:

(1) Suppose b is odd. Then b2 = 1 mod 8, so 1 Ξ= 7+αc mod 8, hence αc = 2 mod 8. Since α Ξ= l, 2, or 5 mod 8, we have that C Ξ 1 , 2 , O Γ 5 mod 8. Thus c contradicts the minimality of a. 

(2) Suppose 2\b but 4\b. Ήien 6 2 = 4mod 8, so 4 Ξ 7 + acmod 8, hence αc =

5 mod 8. This rules out the possibility that a = 2 mod 8, hence α = 1 or 5 mod 8. We conclude that c == 1 or 5 mod 8, and again c contradicts the minimality of a. 

(3) Suppose 4\b. Then 6 2 = Omod 8, so 0 = 7 + acmod 8. Thus ac Ξ= 1 mod 8, so α # 2 mod 8. We therefore have α Ξ= 1 or 5 mod 8, so c = 1 or 5mod8. Thusc contradicts the minimality of a. 

We have shown that in case (b), the minimality of a is always contradicted by c. Now we consider case (c). (c) Suppose a = 3, 6, or 7 mod 8 and ί ^ j = l. Since 0 φ b 2 = acmod p, 

we also have that ί - j = 1. Clearly p is a quadratic residue for c as well. We againlookatthe threepossible values for b2 in the congruence fe 2 == p-\-acmodS. 

(1) Suppose fc is odd. Again ac == 2 mod 8. Since α Ξ= 3, 6, or 7 mod 8, we have that c ΞΞ 3, 6, or 7 mod 8, so c contradicts the minimality of a. 

(2) Suppose 2|fc but A\b. Then αc Ξ= 5 mod 8 as before, so a φ 6 mod 8. Therefore a ΞΞ 3 or 7 mod 8, so c = 3 or 7 mod 8; so c contradicts the minimality of 

a. QUADRATIC RESIDUES 429 (3) Suppose 4\b. Then b2 = Omod 8 so ac = 1 mod 8. Hence a φ 6mod 8, so fl = 3or 7 mod 8. We conclude that c = 3 or 7 mod 8, and again c contradicts the minimality of a. 

In all cases we arrive at a contradiction, so the set of counterexamples to the lemma must be empty. 

Lemma 3.10 Let M \= IE X and let p e M be a standard prime such that p =3 mods. Letm e M, p\m, satisfy one of the following conditions: (a) m =Ξ 0 or 4 mod 8 (i.e. 4\m), or (b) m == 1, 5, or 6 mod 8 and m is a quadratic nonresidue for p, or (c) m = 2,3, or 7 mod 8 and m is a quadratic residue for p. Then p is a quadratic nonresidue form. Proof: The proof is analogous to that of Lemma 3.9 and is left to the reader. If in the previous four lemmas we restrict our attention to the case where m is 

prime, say m — q e M, we obtain one direction of the quadratic reciprocity law. 

Theorem 3.11 Let M \= IE\ and let p yq e M bepήmes, where p is standard. If I £ j = i, then ί ^ ) = 1 unless both p andq are congruent to 3 modulo 4, in which case ( * ) = - 1 . Suppose now that IE X cannot prove that every odd prime has a quadratic non-residue. LetM \= IE\ and let q e M be a prime which has no quadratic nonresidues. (Then q must be infinite.) In particular, (y- j = 1, so by Lemma 3.2 we must have 

q = lmodi. (By Lemma 3.5 we in fact have q = Imods.) Then by Theorem 3.11, 

ίsλ = i for every standard odd prime p. 

The above condition enables us to place restrictions on the form of q. We know from [12] that any odd m e M greater than 1 can be written as m = ab + 1, where a

is odd and b is a power of 2. (Recall that the relation "y is a power of the prime x" can be expressed in IE\ via the formula Pow(x, y) defined as follows: 

x > 1 Λ x\y A Vz < y ((1 < z Λ z\y -> x\z). 

It is easy to see that x must be prime for this formula to hold.) If q — ab + 1 is an odd prime with no quadratic nonresidues, we saw above that 8|fe. Note here that there seems to be no way in IEχ of determining an exponent e of 2 such that "& = 2*" holds in some sense, whereas in / Δ o it is well-known that this can be done. Similarly, if q is as above then in particular - 3 is a quadratic residue for q, so 

q ΞΞ 1 mod 6 by Corollary 3.4. This means 3\ab; but 3\b because Pow(2, b) holds in M. Therefore 3|α. The previous paragraph shows in particular that any Fermat prime q (i.e., any prime q = b 4-1 where b is a power of 2) has quadratic nonresidues. In fact this holds for any m = b +1 such that Pow(2,b), whether or not m is prime. The corresponding result for Mersenne primes (i.e., primes q such that q + 1 is a power of 2) is even easier, since we will have q = 3 mod 4 and so - 1 is a quadratic nonresidue for q by Lemma 3.2. We leave it to the reader to find other restrictions on a; for example, a

must be congruent to either 0 or 3 modulo 5. 430 STUART T SMITH In view of the fact that at least one of a, b must be infinite, we ask whether it is possible to prove that both are infinite. For a, this would possibly involve extending the above congruence restrictions to all the standard primes and showing that no finite element of M can satisfy them all simultaneously. The situation is different for b. In N we can prove that if m = 9 mod 16, then —1 has no eighth root in Έ/mZ. The proof involves examining the order of the group of units of Z/mZ and noting that it is not divisible by 16. In IEχ one could attempt an alternative proof along the lines of Lemma 3.2; the problem is that we can no longer conclude that c < a. Thus we do not even know if IEχ proves that b > 3. 

4 Representabilίty by quadratic forms In this section we treat some cases of the following question: which elements (and in particular which primes) of a model 

M (= IEi can be expressed in the form x2 + ny 2 for a particular integer n? Some results of this type for H go back to Fermat, and the problem for primes in N has been completely solved for each n > 0 (cf. Cox [1]). The question is intimately related to quadratic reciprocity since if q = x 2 + ny 2 then 

x2 = —ny 2modq> 

implying that ί 1 ^ ) = 1. For certain values of n, this necessary condition is also sufficient, even in IE\. 

Before discussing this further, we note that when such representations of a prime 

q exist, they are essentially unique. In fact we can show this to be the case in any discretely ordered GCD domain. The following proof is taken from Sierpinski's book [8]. 

Theorem 4.1 Let R be a discretely ordered GCD domain, leta,b e Rbe positive elements of R, and let q e R be a positive prime element of R. If there exist x, y e R such that both are nonzero and q = ax 2 + by 2, then x and y are unique up to sign and up to the possibility of interchanging x and y in the case a = b = l. Proof: If such x, y exist then clearly (a, b) — 1, for if d is a common divisor of a

and b then d\q. Clearly d = ±q is impossible because ay b, x, y are all positive, therefore d = ± 1 . Similarly we can conclude (x, y) = 1. Suppose in addition to q = ax 2 -h by 2 we also have q = ax 2 + by 2 for some 

xu y\ e R. As above, we have (x ly yx) — 1. We suppose for convenience that   

> χ,y,χi,yi >o.

We note that 

(axx x + byy x) (xy 1 + yx λ) =(ax 2 + by 2)x xyx + (ax 2 + by\)xy = q(x γyx + xy). 

Therefore either q \axx\ + byy\ or else q \xy\ + yx\ (or both). Suppose the former, that is suppose q \axx\ + byy x. From our two expressions for q we can deduce that 

q2 = (axxi + byy x)2 + ab(xy x - yx x)2,

so if q \axxχ + byy x we must in fact have axx x + byy x = ±q and so xy x - yx x = 0. Therefore   

> χyi =yχi-

QUADRATIC RESIDUES 431 Since (x, y) = 1, this implies x\xχ (cf. [9]), and similarly (jti, yι) = 1 implies y\ \y. 

Therefore we must have x = X\ , y = yγ.

Now suppose the latter possibility, i.e. q\xy\ + yx\. Our two expressions for q

also give us the equation 

q2 = (axx ί - byyx) 2 + ab(xy 1 + yxj 2.

Now ab > 1; if q \xy\ + y*i, this equation implies that q2 > abq 2, which can only happen Ίϊa — b = l and 

axxx - byyi = 0. That is, xx\ — yy\ = 0, so xx\ = yy\. An argument similar to that in the previous case yields x = y\ and y = x1.

We return to the question of which primes can be expressed in the form x2 + ny 2.We begin with the case n = 1. 

Theorem 4.2 Let M (= #ϊΊ fl«d letq e M be an odd prime. Then q = x 2 + y 2 for some x,y e M <=$> ί • — J = l. 

Proof: ( = ^ ) Obviously, as remarked earlier. ( 4 = ) We adapt the proof of Theorem 20 of Gupta [3], Let q e M be an odd prime such that ί γ j = 1. Then for some u e M such that u < q, we have M2 + 1 = Omodq. Therefore M 2-hl = m# forsomem G M, wherem < q. Thus the set of elements m e M such that M f= 3w < #3υ < ^(m^ = u2 + υ 2) is nonempty. Since this set is also clearly is!-definable, it contains a minimal element mo. We must show that m 0 = 1. Suppose m0 > 1. We also have m0 < q because the above set contains an element m < q. Choose x0, y 0 e M such that x0 < q, y0 < q, and    

> moq=Xo+

)>o 

lfmo\x o and mo\yo, then m\\x^ + yl so mo\q; this is impossible since q is prime and 1 < m 0 < q. Therefore we can find xi, y\ such that 0 < X\,yi < ^ o and not both of Xi, yi are zero, and such that           

> χ0=x1mod m0and y0=yxmod m0.

We are interested in x\ + yfmodm, therefore if X\ > \m§ we can replace it by 

m0 - Xi without affecting the value of x\ modulo m0 (and similarly for y^. Thus we can assume that we have found xu yι such that 0<x uyι < \m 0 and such that 

x2 + y\ = xl + yl = Omod m 0.

The inequalities on xu yx imply 0 < x\ + y\ < -ml < m 20.

Therefore x\ + y\ — m^rn^ for some mγ e M with 0 < mλ < m 0. Thus we have: 

m\m xq = (x 2 + yl){x 2 4- y2)

= Oo*i + yoyύ 2 + (x oyι - xiyo) 2.432 STUART T. SMITH (The second term might actually be x\ y 0 — x 0y\ , depending on which expression is nonnegative.) Now modulo m 0 , we have 

XoX\ 4- yoy\ = x\ + y\ = Omodm 0 and 

Xoyi —Xiyo = *iyi — *iyi = 0modm 0.

Thus if we let α = ^ f f 0 * and ft = ^ ^ ^ (or ^ ^ ° y i ) , we have mxq =

a2 + b 2. Since mi < q we have a,b < q. But then mi contradicts the minimality of m0 . This contradiction shows that m 0 = 1. In N, we have the additional equivalence for odd primes p that (^ J = 1 <<=$• 

p ΞΞ 1 mod A, so Theorem 4.2 is usually expressed as p — x 2 4- y2 for some Λ:, y <£=£• p = 2 or p == I mod 4. As we remarked earlier, we do not know if 

q = \modA = Φ ( v ) = 1 for odd primes ^r in models of/Ei. In order to deal with other values of n, we need the following identity from [1]: 

Proposition 4.3 The following holds in any commutative ring: (x 2 + ny 2)(z 2 + nw 2) = (xz + nyw) 2 + n(xw - yz) 2

=(xz - nyw) 2 4- n(xw + yz) 2.

We used this identity for n — 1 in the previous proof when we rewrote the product 

(χ 2o+y 2o)(χ 2 + yϊ) 

Now we can extend Theorem 4.2 to the cases n = 2 and n = 3: 

Theorem 4.4 LetM\= IEχ and letq e M be a prime φ 2, 3. 

(i) q = χ 2 + 2y 2 for some x,y e M <=*• (γ\ = 1. 

(ii) q = x 2 4- Sy 2 for some x,y eM <*=$• (γ\ = 1. 

Proof: (i) We can adapt the proof of Theorem 4.2 here. We have 3

0 < x\ 4- 2y 2 < -ml < m\, 

so mi < m 0 as before. (ii) Again the proof of Theorem 4.2 applies, but this time the inequalities for 

x\ 4- 3y 2 yield 0 < x2 4- Zy 2 < -m 2 4- -m 20 = m 20,

4 4implying mi < m 0 . Equality holds only if m 0 is even and X\ = yx — |mo We will show that this cannot happen if mo is minimal. Suppose mo is even. Since 

moq =x% + 3 ^ and (XQ, y 0) = 1 by the minimality of m 0 , we must have that x0 and y0 are both odd. Therefore mo # = 1 + 3 = 0 mod 4; QUADRATIC RESIDUES 433 since q is odd, we conclude that 4|m 0, say m 0 = 4m 2. Thus 

4m 2q = x% + 3yl 

Since x0 and y0 are both odd, there are two possible cases: (a) Suppose x0 Ξ= y0 mod 4. Then 4\x 0 + 3y 0 and 4\x 0 - y 0 (or 4\y 0 - x 0). By Proposition 4.3 with « = 3, z = w = 1, we have (*o + 3%2) 4 = (*o + 3y 0)2 + 3(x 0 - )>o) 2.Therefore we conclude that   

> 2L Q

## 2 ^ Γ/^o-f-33^\ 2 Q / Λ O - V \ 2 1

# 4m 2ί = *o 2 + 3y o2 = 4 | j — J — J + 3 ( ^ — J J

and so we have /Xo + 3 y o y , fχ o-y o\2

But then m2 contradicts the minimality of m 0 .(b) If Xo = —y 0 mod 4, then 4\x 0 — 3y 0 (or 4|3y 0 — *o> depending on which one is nonnegative) and 4\x 0 + yo. This time we use the second formula in Proposition 4.3, i.e. (*o + 3% 2) 4 = (xo ~ 3)>o) 2 + 3(x 0 + Jo) 2

and then continue as before. We conclude that m 0 must be odd, so 0 < x\ + 3yf < m^ and thus mi < m 0 .The rest of the proof now proceeds as in Theorem 4.2. The previous argument indicates that we will not be able to extend these results much past n = 3, because the proof that mi < m 0 will break down. Note, however, that the result for n = 4 is true: 

Corollary 4.5 LetM \= IE γ and letq e M be an odd prime. Then q = x2 + 4y 2

for some x,y e M 4=Φ- (-jp) = 1. 

Proof: This is a corollary of Theorem 4.2; for if q = x2 + 4y 2 then q is a sum of two squares. Conversely, if the odd prime q is the sum of two squares x2 4- y2, then one of 

x, y is even, say y = 2z. Thus # = x 2 + 4z 2. Similarly, ί ^ J = 1 «=$• (~M = 1. As for n = 5, it is well known that the corresponding result fails even in N. For instance, if we let q = 7 then ( ^ ) = 1 since 3 2 = —5 mod 7, but 7 is not of the form 

x2 + 5y 2. The correct result for N is that a prime p has the form x2 4- 5y 2 if and only if /? == 1 or 9 mod 20. For a complete characterization of the primes of the form 

x2 4- ny 2 in H, where n > 0, see [1]. 5 ΓΛe Equation x 3 + y 3 = z 3 In [9] we showed that /£i proves that the equation 

xn + yn = f 1 has no nontrivial solutions for n = 4, 6, and 10. Thus Fermat's last theorem is provable in IE X for certain even exponents. In this section we show that the results in Section 3 enable us to prove that Fermat's last theorem for n = 3 is provable in IE 2. We do not know if this can be improved to IE\ .We adapt a proof by Browkin (which in turn is based on one by Carmichael) which appears in [8]. The first result we need is the following: 434 STUART T. SMITH 

Lemma 5.1 LetM (= IE 2 and suppose s,a,b e M are such that s is odd, (α, ft) =

1, and s 3 = a2 + 3ft 2. Γfte/i ίftere exist a, β e M of opposite parity such that 

(α, 3/9) = 1 and s = a 2 + 3£ 2 ,

> fl

= | α 3 - 9 α £ 2 | , 6 = |3α 2 y9-3y0 3 |. 

Moreover, if a, β e M are arbitrary satisfying the conditions in the conclusion and s, a, and b are defined as in the conclusion, then s is odd, (0, ft) = 1, and s3 = a 2 + 3b 2.Proof: We prove the second part first. Let M (= IE 2 and let α, β e M be of opposite parity such that (α, 3β) = 1. Define s, a, and ft as in the conclusion. Since a and β have opposite parity, s = α 2 + 3β 2 must be odd. Also since the usual properties of g.c.d.'s hold in IE 2, in fact in ΪE\ (c.f. [9]), we have that (a, b) = (α(α 2 —9yβ 2), 3£(α 2 - £ 2 )) = (α 2 - 9yβ 2, α 2 - β2) because (α, 3)9) = 1, (α, α 2 - ^ 2 ) = 1, a n d ( 3 ^ , α 2 - 9 ^ 2 ) = 1. N o w ( α 2 - £ 2 ) - ( α 2 - 9 £ 2 ) = Sβ 2, 9(a 2-β 2)-(a 2-9β 2) =

8α 2 , so (a 2 - 9β 2y a2 - β2) divides (8α 2, Sβ 2). But (8α 2, 8y0 2) = 8(α 2 , β2) = 8since (α, ^) = 1; since α and β have opposite parity, α 2 — 9β 2 and α 2 — β2 are odd, so (α 2 - 9/3 2, a2 - β 2) = 1. We conclude that (α, fc) = 1. Finally, a straightforward substitution shows that s3 = a 2 + 3b 2 when s, a, and 

b are as above. Now we prove the main direction of the lemma. Suppose the set of counterex-amples for s to the lemma is nonempty. The fact that s is such a counterexample can be expressed as: 

(3a<s 3)(3b<s 3)[s 3 = a 2 + 3b 2Λ    

> (fl, b) =1 Λ -«2|S]Λ

-«(3α < s)(3β < s)[s = a 2 + 3β 2A(a = a 3 - 9aβ 2 va = 9aβ 2 - a3)A (b = 3α 2y9 -3β 3vb = 3β 3 - 3a 2β) 

Λα φ βmod 2 A (a, 3β) = l ] . This is an ^2-definable set which we are assuming is nonempty; since IE 2 is equivalent to LE 2i it has a least element which we also denote by s. Let α, b e M be such that the first clause in the above formula is satisfied for this minimal choice of s. 

Since s is odd, the smallest possible value it could have is 1, in which case 

a — i, b — 0. But then a = 1, β = 0 contradict the assumption that s is a counterexample. Thus s > 1. It is easy to show in IE 2 (in fact in /£Ί) that any s > 1 has a prime factor. For the set of factors of s which are greater than 1 is E\ -definable and nonempty, therefore it has a least element, which is then obviously prime. Let q be a prime factor of s. 

Since s is odd, # is as well. Write s — qt. 

We show that 3\s, thus in particular q > 3. If 3|,s then 31s 3 = a2 4- 3fc 2, and so 3|α. Then 91s 3 and 9|α 2 , so 3|fc, contradicting the assumption that (0, ft) = 1. We conclude that 3\s. 

Since (α, 3ft) = 1 and s3 = a 2 + 3ft 2, then (s y a) = 1 and 0, 3ft) = 1. In particular, (#, a) = 1 and (#, 3ft) = 1. Now α 2 + 3ft 2 == Omodq, so 0 φ a2 =QUADRATIC RESIDUES 435 

—3b 2 modq. Therefore —3 is a quadratic residue for q. By Theorem 4.4 (ii), 

q = a 2 + 3β\ 

for some au βx e M. Clearly ax and βι have opposite parity and (oc u 3β x) = 1. By the reverse direction ofthis lemma, which we have already proved, if c = \a 3-9a 1β2\

and d = \3a 2βx - 3/3f |, then (c, d) = 1 and q3 = c 2 4- 3d 2.For convenience, we continue the argument in R, the ring obtained from M by adjoining negative elements. Thus we will not have to worry that all our expressions are nonnegative. Also, since any or all of 0, b, c, or d can be replaced by their negatives, we can drop the absolute value signs in the expressions for these elements. 

We claim that ad — be and ad + be are not both divisible by q. For 

(ad - bc)(ad + be) = (ad) 2 - (be) 2 = (a 2 + 3b 2)d 2

-b 2(c 2 + 3d 2) = t 3q3d2 - b 2q3 = q s(t 3d2 - b2). \iq\ad — be and q\ad + be, then q\2ad and q\2bc. Since q is odd, q\ad and q\bc. 

But (q, a) = (q, b) = 1, so q\d and q\c. This contradicts the fact that (c, d) = 1. Thus one of ad - be or ad + be is not divisible by q. But 

(ad - bc)(ad + be) = q 3(t 3d2 - b2). 

Therefore if q\ad — be then q3\ad -h be, and if q\ad + be then q3\ad — be. Now ί V = s3q3 = (a 2 + 3b 2)(e 2 + 3d 2). 

By Proposition 4.3, ί V = (ac ± 3bd) 2 + 3(ad T be) 2.

Choose the signs so that the expression in the second set of parentheses is divisible by q3. Then the expression in the first set of parentheses is also divisible by q3, so for the appropriate choice of signs we have 

ac ± 3bd u = r — e R q3

ad^-bc and v — — e R. q3

It then follows that ί3 = M 2 + 3ιA 

We claim that (w, υ) = 1. For uc + 3υd = ac ^3ad2 = a, ud - υc =

±<3MW) = ± b a n d ^ 6 ) = L Therefor ( M> „) = 1 as well. Now s — qt so t < s. Since t3 = u2 + 3υ 2 with (w, t>) = 1, the fact that s is the 

minimal counterexample to the lemma implies that there exist α 2 , ^2 Ξ M such that α 2 # yβ 2 mod 2, (α 2 , 3>0 2) = 1 5 and (replacing α 2 , yβ 2 by their negatives if necessary): 

t = a 2 + 3y0 2,

u = a\- 9a 2β2,       

> v=3 α 2^2-3yβ 23.

436 STUART T. SMITH We now combine our representations for t and q to derive a contradiction to the assumption that s is a counterexample to the lemma. Let 

a = 0Lχa 2 + 3 ^ 2 , 

β =Oί 2β! - β2θtχ. 

Since otχ φ β\ mod 2 and a2 Φ β 2 mod 2, we have a φ β mod 2. We have 

s = q t = (a 2 + Sβ\)(μl + 3β 2) = a2 + 3£ 2

by Proposition 4.3. Also the proof that (M, υ) = 1 provides formulas for a and b: a = uc + Zυd = (a 3 - 9α 2 β2 )(α 3 - Qotφ 2)

+ 3(3a 2β2 ~ Zβ\)^a\βι - 3/9f) = < * 3 - 9 α £ 2 ,±2? = M<J - vc = (α 3, - 9α 2 £2 )(3α 2 £i - 3yβ 3)

# - (3<* 2& - 3β 3)(a 3 - torf) 

= 3a 2β - 3β 3.

Since a\a and β\b and since (α, fe) = 1, we must have (α, )β) = 1. Replacing a, β 

by |α|, |)β| respectively, we arrive at a contradiction to the assumption that s is a counterexample to the lemma. This completes the proof. Now we can prove Fermat's last theorem for exponent 3 in IE 2.

Theorem 5.2 IE 2 h VxVyVz(x 3 + y 3 = z 3 -> (x = 0 v y = 0)). 

Proof: Let M (= 7£ 2 and suppose Λf contains a nontiivial solution to the equation 

x3 + y3 = ^ 3 . Consider the set of elements m e M satisfying 

m > 0 A3X < m3y < m3z < m(m = xyz A x3 + y3 = z3). 

We are assuming this Et -definable set to be nonempty, therefore it has a least element m. Let*, y, z e Λfbesuchthatm = xyzwidx 3+y 3 = z3. Clearly(JC, y) = (JC, Z) =(y, z) = l, for any common divisor of two of them would also divide the third and enable us to produce a smaller solution. As in the previous lemma, we find it more convenient to continue the argument in the ring R obtained from M by adjoining negative elements. Replacing z by -z in 

R yields the equation x3 + y 3 + z3 = 0, which is symmetric in JC, y, and z. Clearly at least one of x, y, z is even, and since they are pairwise relatively prime we conclude that exactly one of them is even. The aforementioned symmetry enables us to assume that z is even and that x and y are odd. Rewrite the equation as x3 + y3 = z3, where now JC, y, z e R, all are nonzero, z is even, and x, y are odd. Thus x + y and c — y are even, say x + y = 2M and x — y = 2w. Therefore 

x = u +w, y = u — w. Since (x, y) = 1 we conclude that (M, W) — 1. Also x and y are both odd, so u φ w mod 2. Substituting the above expressions for x and y in the equation JC 3 + y 3 = z3 yields (w + w) 3 + (w - w) 3 = z3, or 2M (M 2 + 3ω 2 ) = z 3 .We consider two cases, depending on whether or not 3 divides u. 

(a) Suppose 3{M, SO (3, w) = 1. Then (M, M 2 + 3w 2) = 1, and since uφw mod 2we have that M 2 -I- 3w 2 is odd. Therefore (2M, M 2 + 3w 2) = 1. But      

> 2M(M 2+ 3W 2)=Z3,

QUADRATIC RESIDUES 437 so 2M = t3 and u2 + 3w 2 = s3 for some s,t e R. (This fact is provable in IEύ cf. [9].) Since u2 + 3w 2 is odd, so is s. By Lemma 5.1, there exist a, β e R such that 

u = α 3 - 9αβ 2 , α ψ £ /3 morf 2, and (α, 3/9) = 1. Then 

t3 = 2u = 2α(α - 3β)(a + 3/8). Now α - 3)0 and α + 3)0 are odd and (α, 3)0) = 1, so the three elements 2α, a - 3)0, and α + 3)0 are pairwise relatively prime. Therefore there exist σ, τ, and pinR such that 2α = σ 3 , a -3β = τ 3 , and α + 3)0 = p 3 , and where t = στρ. But then σ 3 = τ 3 + p 3

is a solution to the equation ofthe theorem, where \στp\ 3 = | ί 3 | = |2w| = |JC + y| <

\xyz\ 3, contradicting the minimality of \xyz\. 

Actually we must justify this by showing that \στp\ > 0. But \στp\ = \x + y\' 9

if\x + y\=0 then x = -y, in which case z = 0 which contradicts our assumptions onx, y, z. (b) Suppose 3|w, say u = 3υ. Substituting for M in the equation 2u(u 2 + 3tt> 2) = z3 , we have 

6υ(9υ 2 + 3w 2) = z 3 , or 18υ(3ι; 2 + w2) = z3 .

Now u φ wmod2 so v φ wmod2. Therefore 3υ 2 + w2 is odd. Also (u,w) =

(3υ, w) = 1, so we conclude that (18υ, 3υ 2+w; 2) = 1. Thuslδi; = ί 3 and3υ 2 +iί; 2 =

s3 for some syt e R. Now s is odd because υ and w have opposite parity. Also (υ, w) = l, so by Lemma 5.1 there exist a, β e R such that it; = a3 - 9aβ 2,v = Za 2β - 3/9 3, aφβ mod 2, and (α, 3)0) = 1. Since 18υ = ί 3, we have 18(3)0)(α 2 -)0 2 ) = ί 3 , or 27 2)0(α+)0)(α-)0) = ί3.Now a+β and α—)0 are both odd and (oc, β) = 1, so 2)0, α+)β, and α—)0 are pairwise relatively prime. Therefore there exist σ, τ, and p in I? such that 2β = σ3 , α+)0 = τ 3 ,and a — β — ρ 3, and where ί = 3arp. But then σ 3 = r 3 + /o3

is a solution to the equation of the theorem, where |3στp| 3 = | ί 3 | = |l8υ| = |6w| = 3|JC + y\ < 3|jcyz| 3. In particular, |στp| < \xyz\, and |στp| > 0 as in case (a). We have thus contradicted the minimality of |xyz|. 

6 Open questions 

Question 5.1 Does IE X prove that if q = 1 mod 4 is prime then ί γ j = 1? Is this provable i n / Δ o ?

Question 5.2 Is the converse to Theorem 3.11 provable in IE\ or in 7Δ 0 ? Can anything be said about the case when p and q are both nonstandard? 

Question 5.3 Does IE X (or J Δ 0 ) prove that if m = 5mod 8 then - 1 has no fourth root modulo m? More generally, if m = 2 r s with s odd and r finite, then —1 has no 2 r-th root modulo ml 

Question 5.4 What can be said about primes of the form x2 + ny 2 for n > 4 in 

> IE XΊ

Question 5.5 Can Fermat's last theorem for exponent 3 be proved in IEγΊ 

Question 5.6 Does IE 2 prove other cases of Fermat's last theorem for odd expo-nents? 438 STUART T. SMITH REFERENCES 

[1] Cox, D., Primes of the Form x 2 + ny 2, John Wiley & Sons, New York, 1989. [2] van den Dries, L., "Some model theory and number theory for models of weak systems of arithmetic," pp. 346-362 in Model Theory of Algebra and Arithmetic, edited by L. Pacholski, Lecture Notes in Mathematics 834, Springer, Berlin, 1980. [3] Gupta, H., Selected Topics in Number Theory, Abacus Press, London, 1980. [4] Kaye, R., "Diophantine and parameter-free induction," Ph.D. dissertation, Manchester University, 1987. [5] Macintyre, A. and D. Marker, "Primes and their residue rings in models of open induc-tion," Annals of Pure and Applied Logic, vol. 43 (1989), pp. 57-77. [6] Paris, J. and A. Wilkie, "Δo sets and induction", pp. 237-248 in Open Days in Model Theory and Set Theory, edited by W. Guzicki, Proceedings of the Jadwisin, Poland, Logic Conference 1981, Leeds University, 1983 . [7] Shepherdson, J. C , "A nonstandard model for a free variable fragment of number theory," 

Bull. Acad Polon. ScL, vol. 12 (1964), pp. 79-86. [8] Sierpinski, W., Elementary Theory of Numbers, Panstwowe Wydawnictwo Naukowe, Warszawa, 1964. [9] Smith, S. T., "Fermat's last theorem and Bezout's theorem in GCD domains," Journal of Pure and Applied Algebra, vol. 79 (1992), pp. 63-85. [10] Smith, S. T., "On the diophantine equation x10 ± v 1 0 = z 2 ," Journal of Pure and Applied Algebra, vol. 79 (1992), pp. 87-108. [11] Smith, S. T., "Building discretely ordered Bezout domains and GCD Domains," forth-coming in Journal of Algebra. 

[12] Smith, S. T., "Prime numbers and factorization in IE\ and weaker systems," Journal of Symbolic Logic, vol. 57, (1992), pp. 1057-1085. [13] Wilkie, A., "Some results and problems on weak systems of arithmetic," pp. 285-296 in 

Logic Colloquium '77> edited by A. J. Macintyre, North-Holland, Amsterdam, 1978. [14] Wilmers, G., "Bounded existential induction," The Journal of Symbolic Logic, vol. 50, (1985), pp. 72-90. 

Raymond and Beverly Sackler Faculty of Exact Sciences School of Mathematical Sciences Tel Aviv University Ramat-Aviv y 69978 Israel

