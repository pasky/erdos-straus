## Content from https://projecteuclid.org/journals/notre-dame-journal-of-formal-logic/volume-38/issue-1/Toward-the-Limits-of-the-Tennenbaum-Phenomenon/10.1305/ndjfl/1039700698.pdf

Title: daquino381E.tex

URL Source: https://projecteuclid.org/journals/notre-dame-journal-of-formal-logic/volume-38/issue-1/Toward-the-Limits-of-the-Tennenbaum-Phenomenon/10.1305/ndjfl/1039700698.pdf

Number of Pages: 13

Markdown Content:
81 Notre Dame Journal of Formal Logic Volume 38, Number 1, Winter 1997 

# Toward the Limits of the Tennenbaum Phenomenon 

PAOLA D’AQUINO 

Abstract We consider the theory PA # and its weak fragments in the language of arithmetic expanded with the functional symbol #. We prove that PA # and its weak fragments, down to ∀E#1(N) and I E −#1 , are subject to the Tennenbaum phenomenon with respect to +, · , and #. For the last two theories it is still unknown if they may have nonstandard recursive models in the usual language of arithmetic. 

1 Introduction Let L = { 0, S, +, · , < } be the usual language of Peano Arithmetic (PA), and let N denote the standard model for L. Tennenbaum showed in [14] that in any nonstandard model of PA the operations of + and · cannot be recursive. Anal-ogous results have also been obtained for weak fragments of PA. McAloon showed in [10] that the + and · of any nonstandard models of I0 are not recursive, and Wilmers proved the same result for nonstandard models of I E 1 (see [16]). On the other hand, Shepherdson [13] constructed recursive nonstandard models of I Open 

and more recently recursive models of I Open + normality have been constructed (see [2]). 

Definition 1.1 A theory T in a language containing L has the Tennenbaum phe-nomenon for the operations + and · if for every nonstandard model M of T there is no isomorphism between M and ω such that the operations of + and · of M corre-spond to recursive operations on ω.A very natural question is: How weak can a fragment of arithmetic be and still have the Tennenbaum phenomenon? Kaye in [7] considered, as a possible candidate, the theory I E −

> 1

, where induction is applied only to E1-formulas with no parameters. He proved the following relations between I E −

> 1

and the theory ∀E1(N), the universal existentially bounded true sentences. 

Theorem 1.2 (i) ∀E1(N)  I E − 

> 1

; (ii) For every σ ∈ ∀ E1(N) if M |= I E − 

> 1

+¬σ then M is not recursive. Received May 8, 1996; revised March 9, 1997 82 PAOLA D’AQUINO So the problem is shifted to studying the Tennenbaum phenomenon for the theory 

∀E1(N). It is easy to construct a recursive nonstandard model of the theory ∀1(N),the set of true ∀1-sentences. Add x > N and consider the ring of polynomials in x

over N. This is a recursive nonstandard model of ∀1(N).In [7] it is left open if ∀E1(N) has nonstandard recursive models. A positive answer is given under the hypothesis that there exists a function of exponential growth and whose graph is E1-definable in L. But this is still an open problem. In recent work on fragments of PA the function # has played an important role (see [4], [11], [15]). Recall that # is defined by # (x, y) = x[log 2 y], and it is a poly-nomial time computable function. It has been relevant both for coding of syntax ([15]) and for some proofs of elementary number theory, such as cofinality of primes [12] and Lagrange’s Theorem [3]. Sometimes we will use the equivalent notation #(x, y) = x|y|, where |y| denotes the length of y in basis 2. In this paper we will con-sider the Tennenbaum phenomenon for various fragments of PA involving #, and re-late this to [8]. Many of Kaye’s results on the relative strength of some fragments of PA proved in [8] are purely formal and hence can be easily extended to the relative theories in the language L #.We will work in the language L # = L ∪ { #} and all the theories we will consider will have some basic obvious axioms about # (see also [5]). Two different results are proved. On the one hand we show that the # of a nonstandard model of PA # is not recursive, thus sharpening the classical result of Tennenbaum. On the other hand, we show that +, · , and # of any nonstandard model of the theories of universal existen-tially bounded sentences of L # true in N—which we will denote by ∀E#1(N)—and of existentially bounded parameter free induction—which we will denote by I E −#1 —are never recursive operations, a result currently unknown for ∀E1(N) and I E −

> 1

in L. It seems to us that these are the weakest fragments of PA for which this phenomenon has been proved. Notice that if we add to the language a symbol for the exponential function exp 

then the theory ∀Eexp  

> 1

(N) is subject to the Tennenbaum phenomenon for + and · (this is implicit in [8]). 

Remark 1.3 In order to prove that I0 (or I E 1) satisfies the Tennenbaum phe-nomenon it is sufficient to construct in any nonstandard model M of I0 (or I E 1) a nonstandard initial segment I, such that I |= PA. Let A, B be two disjoint recur-sively inseparable r.e. sets and define the following type 

τ(v) = { pn |v : if n ∈ A} ∪ { pn  |v : if n ∈ B}

where pn denotes the nth prime. Clearly, τ(v) is an r.e. set, and by Craig’s trick there is a recursive set of formulas generating the same type. So without loss of generality we can assume τ(v) to be a recursive set. It is finitely satisfiable in I and of bounded complexity, hence realized in I, say by some a ∈ I. Define 

n ∈ C iff ∃q(a = q + q + · · · + q

︸ ︷︷ ︸ 

> pn

times 

)

n  ∈ C iff ∃r < pn ∃q(r  = 0 ∧ a = q + q + · · · + q

︸ ︷︷ ︸ 

> pn

times 

+r). TENNENBAUM PHENOMENON 83 So the formulas defining C and the complement of C are the same in I and M . So if 

+ of M was recursive then C also would be recursive which is a contradiction since 

A and B are recursively inseparable. To show that the product of M is not recursive a similar argument is used. We will also use these results to prove that the function # of any nonstandard model of the corresponding fragments in the language L # is never recursive. Since the initial segment I is a model of PA, the function (x, y)  → x[log 2 y] is total over I in a suitable sense. We will have to show that this function coincides with the function #, and this will imply that I is closed under #, and hence # cannot be recursive. A slightly more delicate argument will be used for the theory ∀E#1(N). 

Notice that there are recursive binary functions which may be recursive over nonstandard models of arithmetic. For example, consider the function defined as fol-lows: 

f (x, y) =

{ 1 if x ≤ y

0 if x > y .

Since < can always be chosen recursive, then f also is recursive. 

2 The nonrecursiveness of # We will show that the Tennenbaum phenomenon holds for the function # in all of the theories for which the classical Tennenbaum phe-nomenon has been established for + and · . Our proof will also work for any function whose graph is 0-definable and which satisfies some basic properties of #. It is easy to define in a simple way the graph of + and · from xy:

a · b = c iff (xa)b = xc,

a + b = c iff xa · xb = xc.

This implies the Tennenbaum phenomenon for xy. The same argument does not seem to adapt straightfowardly to #: it seems to us that there is not an easy definition of +

and/or · in terms of #. One can easily define + from · and 2 x via 2 a+b = (2a) · (2b). Semenov showed that · cannot be defined from + and 2 x, and in fact the 2 x of a nonstandard model of PA may be recursive (see Remark 3.6). Recall that the graph of the exponential function 

(x, y)  → xy

is 0-definable, and the recursion laws of exponentiation are provable in I0 (see [1], [6]). Let θ( x, y, z) be such a formula. Actually, for the purposes of this section it is not necessary to work with a formula of low complexity since induction is allowed to all formulas, but we prefer to refer to the 0-definition of exponentiation since it will be used also in the next section. Via the formula θ we can also define the length of an element in basis 2: 

|x| = n iff ∃z ≤ x(θ( 2, n, z) ∧ x < 2z). 

We will use the standard notation enriched with the superscript # for formulas, theo-ries, and so on, in the language L #. While an axiomatization for + and · is obvious, it is less obvious which axioms we need to choose for the function #. The recursion 84 PAOLA D’AQUINO equations for # are not so immediate as for + and · . We have chosen the following axioms: 1. ∀x > 0∀y(#(x, 0) = #(x, 1) = #(0, y) = 0), 

2. ∀x > 0∀y > 0(( Po w2(y + 1) ∧ #(x, y + 1)

= x#(x, y)) ∨ (¬Po w2(y + 1) ∧ #(x, y + 1) = #(x, y))), 

where Po w2(y) stands for ∀x ≤ y(x|y → 2|x). Notice that axioms 1 and 2 are of the type ∀ followed by a 0-formula. We will denote by PA # the theory axiomatized by the usual axioms of PA with induction applied to L #-formulas and by the above axioms for #. With standard techniques it is easy to show that PA # is a conservative extension of PA. In fact, via the 0-formula defining the graph of exponentiation we can give a meaning to x[log 2 y] in any model of PA. The graph of 

(x, y)  → x[log 2 y]is defined as 

∃n < y∃v ≤ y(θ( 2, n, v) ∧ v ≤ y < 2v ∧ θ( x, n, z)). 

It can be proved in PA # that such a definition satisfies the axioms of # (see also Lemma 3.1). 

Theorem 2.1 Let M be a nonstandard model of PA #. Then # of M is not recursive. Proof: The proof proceeds as in the classical case. Let A and B be recursively in-separable r.e. sets, and let pn denote the nth prime of M . Construct the following type as before: 

τ(v) = { pn |v : n ∈ A} ∪ { pn  |v : n ∈ B}.τ(v) is an r.e. set and there is a recursive set of formulas generating the same type, so without loss of generality we can assume τ(v) to be a recursive set. It is finitely satisfiable and of bounded complexity, hence it is realized in M , say by a. Let X ={n ∈ N : pn |a}. Obviously A ⊆ X and B ∩ X = ∅. We will show that both X and 

N − X are r.e. in #. First of all notice that if x is a power of 2 then #(x, y) = #(2, z) iff |x|| y| = | z|.

As recalled in Remark 1.3 we have 

n ∈ X iff ∃u(u + · · · + u︸ ︷︷ ︸ 

> pn

times 

) = a ,

and if we use the fix element 2 a we have that X is r.e. in ·

n ∈ X i f f ∃v(v · · · · · v︸ ︷︷ ︸ 

> pn

times 

) = 2a

(think of v as 2 u). Now using the fix element 2 2a

we can show that X is r.e. in #. Consider the exponential version of 

v · · · · · v︸ ︷︷ ︸ 

> pn

times 

= 2a : that is, 2

v · · · · · v︸ ︷︷ ︸ 

> pn

= 22a

.TENNENBAUM PHENOMENON 85 We can express this equality in terms of # as follows: #(# · · · #(#

︸ ︷︷ ︸ 

> pn

times 

(2, 2v), 2v), . . . , 2v) = #(2, 22a

). 

Hence we have that 

n ∈ X iff ∃w( #(# · · · #

︸ ︷︷ ︸ 

> pn

times 

(2, w), w), . . . , w) = #(2, 22a

). 

In an analogous way it can be shown that N − X is r.e. in #. We have in fact 

n ∈ N − X iff 

> pn −1

∨

> j=1

∃s(#(# · · · (#

︸ ︷︷ ︸ 

> pn

times 

(s, 22 j

), s), . . . , s) = #(2, 22a

). 



Remark 2.2 Notice that the above proof can be reproduced in any nonstandard ini-tial segment [0 , α ] of M since in a model of PA all initial segments determined by an element are recursively saturated. We can in fact realize the type in [0 , α ], for α arbi-trarily small and nonstandard in M : that is, of the order double length || · || and still nonstandard. In the above proof take α = || b|| for some small nonstandard b, and | · |

computed in M . The existential quantifiers in the definition of both X and N − X can be bounded by 2 2a

. So if 2 2a

< α then # restricted to [0 , α ] is not recursive. We are now concerned about fragments of PA #. By I#0 we denote the theory axiom-atized by induction on bounded formulas of L # and axioms 1 and 2 for #. In [5] we showed that I#0 is bi-interpretable with the more familiar theory I0 + 1. It is more complex to find a natural axiomatization for the theory I E #1. The pre-vious axioms for # are not suitable anymore since they have a higher complexity with respect to the induction we allow. Later we will use the axiomatization of I E #1 given in [5] since all the axioms are true ∀#1. They describe the basic properties of the func-tion #. We will discuss this theory in more detail in the next section. 

3 The Tennenbaum phenomenon for weak fragments of PA # McAloon showed in [10] that any nonstandard model M of I0 has a nonstandard initial segment I

which is a model of PA. Using McAloon’s result we can prove that if M is a model of I#0 also the operation # is not recursive, but this requires an argument. Recall that the graph of the exponential function is 0-definable, and the recur-sion laws of exponentiation are provable in I0 (see [1], [6]). Let θ( x, y, z) be a for-mula defining it with the above properties. If M is a model of I#0, in particular M is a model of I0, and by McAloon’s result it has a nonstandard initial segment I which is a model of PA. In I the exponential function is total and via the formula θ we can define the graph of the function 

(x, y)  → x[log 2 y]as follows 

∃n < y∃v ≤ y(θ( 2, n, v) ∧ v ≤ y < 2v ∧ θ( x, n, z)). 86 PAOLA D’AQUINO Denote such a formula by ψ( x, y, z). In order to prove the nonrecursiveness of # it is enough to show that the function defined by ψ coincides with the function # that I

inherits from M . This is proved in the following lemma. 

Lemma 3.1 M |= ∀ x > 1, y, z(ψ( x, y, z) → #(x, y) = z).Proof: Fix x > 1 and apply 0-induction on n = y + z. Suppose the implication has been proved for all m < n. Assume ψ( x, y + 1, z) with y + 1 + z = n. We distinguish two cases. 

Case 1: If Po w2(y + 1) then # (x, y + 1) = #(x, y) · x, and |y + 1| = | y| + 1. So from ψ( x, y, z) and the recursion properties of exponentiation it follows ψ( x, y, z/x).By inductive hypothesis, # (x, y) = z/x and so # (x, y + 1) = z.

Case 2: If ¬Po w2(y + 1), then # (x, y + 1) = #(x, y), and |y + 1| = | y|. So from 

ψ( x, y + 1, z) it follows ψ( x, y, z) and by inductive hypothesis # (x, y) = z and so #(x, y + 1) = z. 

Now using Theorem 2.1 we can deduce that # of I, and so also of M , is not recursive. The situation becomes more complex for the theory I E #1 and weaker fragments. We recall that the theory I E #1 is the theory introduced in [5] and axiomatized by induc-tion on E#1-formulas and the twelve axioms listed below which describe the complex recursion laws of the function # in a simple way: that is, using only formulas of the type universal followed by an open formula. 1. ∀x(#(x, 0) = 1 ∧ #(x, 1) = 1);

2. ∀x∀y > 0# (x, 2x) = x#(x, y)) ;

3. ∀x∀y > 1(#(x, y)/ x = #(x, [y/2] )) ;

4. ∀x(#(2, 2x) > x);

5. ∀x > 0(#(2x, x) ≤ x#(x, x)) ;

6. ∀x∀y > 0∀z > 0(#(x, yz ) ≥ #(x, y)#(x, z)) ;

7. ∀x∀y ≤ x(#(2x, y) < #(2x − 1, 2y)) ;

8. ∀x∀y∀z(#(2, z) < y + 1 < #(2, z + 1) → #(x, y + 1) = #(x, y)) ;

9. ∀x∀y∀z(#(2, z) = y + 1 → #(x, y + 1) = x#(x, y)) ;

10. ∀x∀y∀z(y ≤ z → #(x, y) ≤ #(x, z)) ;

11. ∀x∀y∀z(#(xz , y) = #(x, y)#(z, y)) ;

12. ∀x > 1∀y∀z(#(x, y) = #(x, z) → ∀ w( #(w, y) = #(w, z))). 

In [5] an E#1-formula which defines the graph of exponentiation is found. At the mo-ment this is the formula of lowest complexity which defines the exponential function (at the cost of adding the polynomial time computable function # to the language). The theory I E #1 has been introduced as an adequate fragment in which the obvious recursion laws of exponentiation can be proved for the E#1-formula defining it. We refer to [5] for more details. We recall also that Matijasevic showed that the graph of exponentiation is exis-tentially definable. This is the key step in the proof that every r.e. set is existentially definable. In [9], the following definition of an = m is obtained: 

an = m iff m =

[ yn +1(Na )

yn +1(N )

]

,TENNENBAUM PHENOMENON 87 where yn +1(Na ) is the (n + 1)st solution of the Pell equation x2 − (N2a2 − 1)y2 = 1and yn +1(N ) is the (n + 1)st solution of the Pell equation x2 − (N2 − 1)y2 = 1, for 

N > nm 2. This definition is clearly existential. We will denote the formula defining the relation xy = z by ∃ ¯ wϕ( x, y, z, ¯w) where ϕ( x, y, z, ¯w) is quantifier free, and ¯w

denotes a finite sequence. Using the properties of the solutions of a Pell equation it is easy to see that the above definition satisfies the recursion laws of the exponential function in PA. Wilmers showed in [16] that any nonstandard model of I E 1 has a nonstandard initial segment which is a model of PA. So if we work in a model M of I E #1 we have a nonstandard initial segment I which is a model of PA, and on I the function 

(∗) (x, y)  → x[log 2 y]is total. As in the case of I#0, in order to show that # of M is not recursive it will be enough to show that the function ( ∗) coincides with the function # that I carries inherited from M . This will be shown in the following theorem. 

Theorem 3.2 If M is a nonstandard model of I E #1 then the operations +, · , and 

# are each nonrecursive. Proof: Let I be a nonstandard initial segment of M which is a model of PA. Our main goal is to show that the function 

(x, y)  → x[log 2 y]coincides with the function # on I inherited from M . We need to show this formally: hence, we need to express formally what we mean by x[log 2 y] to coincide with # (x, y).This time we cannot use the 0-formula defining exponentiation since in M we have available only induction on existentially bounded formulas. We will use the Mati-jasevic definition of exponentiation which we denoted by ∃ ¯ wϕ( x, y, z, ¯w) . The idea now is to show that for every instance of the ¯w’s which makes ϕ true for some a, b, c,then the #-version of it is also true: that is, # (a, b) = c. We do not attempt to show that this is true in the whole model, but it will be sufficient to show the implication 

low in the model. Consider the formula ξ( s) defined as follows: 

∀a, b, d, c < s∀ ¯ u < s∀ ¯ w < s(a + b + d + c + ¯ u + ¯ w =

s ∧ ϕ( 2, n, d, ¯u) ∧ d ≤ b < 2d ∧ ϕ( a, n, c, ¯w) → #(a, b) = c). ξ( s) says that if n, b, a, c, ¯u, ¯w are below s and n = | b| and an = c in the Matijasevic sense, then # (a, b) = c. Notice that ξ( s) is a universally bounded formula, and ξ( m)

is true for all m ∈ N. Notice also that no #-term appears in the bounded quantifiers. We need to distinguish various cases. 

Case 1: For all s ∈ M we have M |= ξ( s). In this case we have that over the whole model M the Matijasevic definition of a|b| coincides with # (a, b), and this implies that # is not recursive. 

Case 2: There is s ∈ M such that M |= ¬ ξ( s). By the least number principle ap-plied to ¬ξ( s) ∈ E#1 (see [8]) there is s0 such that M |= ¬ ξ( s0) ∧ ∀ s < s0ξ( s).88 PAOLA D’AQUINO 

Subcase 1: If I < s0, then over I we have the same situation as in Case 1 and hence also in this case # is not recursive. 

Subcase 2: If s0 ∈ I, then I |= ∀ s < s0ξ( s). One first shows that there is a non-standard α ∈ I such that whenever ¯δ are the first witnesses of u|v|, for u, v < α then 

u|v| < s0, 2 2α< s0 and ¯δ + u + v + | v| + u|v| < s0. The existence of such α can be obtained by applying overspill (in I) to a formalization of the above sentence. Now choose b < α such that 2 2b

< α , and the result is that, in the initial segment [0 , 22b

],

the functions x|y| and # (x, y) coincide. From Remark 1.3 it follows that # is not re-cursive. 

We now consider the fragment I E −

> 1

which was suggested by Kaye in [8] as a pos-sible candidate to be the weakest fragment of PA to be subject to the Tennenbaum phenomenon. As we have already recalled in Section 1, he showed strong connec-tions between the theories I E −

> 1

and ∀E1(N) (see Theorem 1.2). More precisely, he proved that if M is a model of I E −

> 1

but not a model of ∀E1(N) then + and · of M

are not recursive and left open the problem whether M is a model of ∀E1(N). We will consider the theories I E −#1 and ∀E#1(N) in the language L # and we will show that the operations +, · , and # of any nonstandard model of either theory cannot be recursive. 

Theorem 3.3 Let M be a nonstandard model of I E −#1 and assume M is not a model of ∀E1(N). Then the operations +, · , and # of M are not recursive. Proof: Kaye proved that if M is a model of I E −

> 1

but not a model of ∀E1(N) then there is a nonstandard initial segment of M which is a model of PA. We can now easily adapt the proof of the previous theorem to this case, simply taking care in Case 2. If M |= ∃ s¬ξ( s), we can no longer appeal to the least number principle for E#1-formulas since it is not equivalent to parameter free induction, but we can still be sure that there is a nonstandard s0 such that M |= ξ( s0) ∧ ¬ ξ( s0 + 1.) Otherwise by U−#1 -induction (recall that I E −#1  IU −#1 , see [8]) we would have M |= ∀ sξ( s)—notice that we have used only that s0 is nonstandard. Now just repeat the same proof as in Theorem 3.2. 

It is left to show that the theory ∀E#1(N) is subject to the Tennenbaum phenomenon for the functions +, · , and #. Kaye in [8] sketched a proof of the nonrecursive-ness of + and · of any nonstandard model of ∀E1(N) assuming the existence of a function growing at least as fast as exponentiation and whose graph is E1-definable. The existence of such a function is still an open problem. In [5] we showed that the graph of exponentiation is definable in L # using only existentially bounded quan-tifiers. We will denote such a formula by (x, y, z), and it is of the form ∃¯ t <τ( x, y, z)G(x, y, z, ¯t), with G quantifier free and τ a term of the language L #. For any model M of ∀E#1(N) we define 

N0 = M and Ni +1 = { a ∈ M : ∃c ∈ Ni , M |= (a, a, c)}.

Notice that the Ni ’s are initial segments of M . In fact, in N it is true that if (n, n, m)

for some n, m then (n′, n′, k) for all n′ < n and some k < m, and this sentence is of the form ∀E#1.TENNENBAUM PHENOMENON 89 Kaye in [8] attached to any model M of I E −

> 1

a sequence of initial segments de-fined as follows: 

M0 = M and Mi +1 = { a ∈ M : ∃b ∈ Mi , M |= χ( a, b)},

where χ( a, b) is an E1-formula, ∃ ¯ u < t(a, b)F(a, b, ¯u), with F quantifier free and t aterm, saying that b is a solution of the Pell equation x2 − (( a + 1)2 − 1)y2 = 1, and b

is in the equivalence class 0 modulo a + 1 and is greater than or equal to (a + 1)a+1.

(In N for fixed a the least b satisfying χ is the (a + 1)st solution of the equation.) Notice that χ is not functional. The following estimates on the size of the (n + 1)st solution of the Pell equation x2 − (a2 − 1)y2 = 1 will be useful later (see [9]): 

(2a − 1)n ≤ yn +1(a) ≤ (2a)n.

Kaye showed that 

Mexp = ⋂

> i∈ω

Mi 

is a model of I0 + exp . Notice that both sequences of Ni ’s and of Mi ’s may be constant. It is easily seen that ∀E#1(N)  I E −#1 . So Kaye’s construction of the Mi ’s can be reproduced in any model of ∀E#1(N). We will, in fact, show that Ni = Mi for all i.

Lemma 3.4 Let M be a model of ∀E#1(N). Then Ni = Mi for all i. Proof: We prove the lemma for i = 1 since the general case can be treated in a sim-ilar way. We want to show that whenever χ( a, b) is true then also (a, a, c) is true for some c, and vice versa. Obviously, this is always the case in N, but since we work in M model of ∀E#1(N) we need to express the above implications in the appropri-ate complexity in order to have them satisfied also in M . There is a further problem that χ is not functional, and this also needs to be taken into account. We will use the estimates given in [9] on the size of the nth solution and the Matijasevic definition of exponentiation in order to identify the smallest b > 0 satisfying χ( a, b). Consider the ∀E#1-sentence: 

∀a, b, ¯u, ¯w(( F(a, b, ¯u) ∧ ϕ( 2a + 1, a, b, ¯w)) → ∃ c < b (a, a, c)). 

It says that whenever χ( a, b) and b < ( 2a + 1)a (that is, b is the (a + 1)st solution of the equation x2 − (( a + 1)2 − 1)y2 = 1) then (a, a, c) for c < b. This implies 

M1 ⊆ N1. To prove the reverse direction consider the following ∀E#1-sentence: 

∀a, c, ¯t(G(a, a, c, ¯t) → ∃ b < c3χ( a, b)). 

This says that whenever (a, a, c) then we can find b < c3 satisfying χ( a, b), and it implies N1 ⊆ M1. Notice that the inequality b < c3 is an easy consequence of the inequalities of [9]. In fact, ya +1(a + 1) ≤ (2(a + 1)) a < ( aa)3. There is no problem in guaranteeing the existence of these objects since we work in N.The proof that Mi +1 = Ni +1, assuming Mi = Ni is very similar to the one shown above except that the ∀E#1-sentences become longer since they have to say that b and c

are in Mi and Ni , respectively, and this can be expressed without increasing the com-plexity of the sentences. 90 PAOLA D’AQUINO We can then extend many of the properties of the Mi ’s proved by Kaye to the Ni ’s (e.g., ⋂ 

> i∈ω

Ni = Nexp is a model of I0 + exp ) and we will use them in the proof of our last theorem. 

Theorem 3.5 If M is a nonstandard model of ∀E#1(N) then the operations +, · ,

and # are not recursive. Proof: Let Ni ’s be as above. If Ni = Ni +1 for all i, then M is a model of I0 + exp 

and hence +, · , and # are not recursive. For the nonrecursiveness of # just notice that M being a model of I0 + exp it has a nonstandard initial segment I which is a model of PA. It is not difficult to adapt the proof done for I#0 to this case. If Ni  = Ni +1 for all i then Proposition 6.3 of [8] and Lemma 3.4 guarantee that the initial segment Nexp is nonstandard and this is enough to deduce that the three operations on M are not recursive. Notice that only these two cases are possible. In fact, suppose that N1 ⊂ N0 and N1 = N2 =, . . . , and let a ∈ N0 − N1. Consider the following ∀E#1-sentence: 

∀a, b∀ ¯ u(G(2, b, a, ¯u) → ∃ c < #(a, a) (b, b, c)). 

It says that if b = log 2 a then bb = c < #(a, a). This is obviously true in N, and hence also in M . Clearly, a < bb = (log 2 a)log 2 a. From N1 = N2 and b ∈ N1 it follows that 

b ∈ N2 and so bb ∈ N1, but this gives a contradiction since a < bb and a  ∈ N1 (here we have used the functionality of ). 

We have shown that in the language L # the Tennenbaum phenomenon holds also for the fragment of existentially bounded free induction, a result which is still unknown for L.

Remark 3.6 We can extend this result to many unary functions f in the following sense: there are nonstandard models of PA where the function f is recursive. Let f

be a unary function satisfying the following conditions: 1. f is 1 − 1,

2. range( f ) is coinfinite, and 3. f has no cycles. We assume that f is a computable function over the integers. It will be clear later why we need the last hypothesis. Examples of such functions include 2 x and x|x|, or 

|x|.The idea is to find a recursively saturated model of Th (N, f ) and impose 

+, · , < to make this a nonstandard model of PA. First of all we try to understand what a countable model (M, g) of the theory of f looks like. Given an element a of a model of f we define the orbit Oa of a as follows: 

Oa = { f k(a) : k ∈ ω} ∪ { f −k(a) : k ∈ ω}.

Clearly, distinct orbits are disjoint. For any a there are two possibilities: 1. Oa ∩ M − range ( f ) = ∅, and this happens if a ∈ ⋂ 

> k∈ω

range ( f k ) (Z-orbits); 2. Oa ∩ M − range ( f )  = ∅ and this is a singleton {a}, and this happens if 

a ∈ ⋂

> k≤k0

range ( f k ) and a  ∈ range ( f k0+1) (N-orbits). TENNENBAUM PHENOMENON 91 Obviously, a model of f is completely determined by the number of Z-orbits, n∞,and the number of N-orbits, n1. From the hypothesis that the range of f is coinfinite it follows that n1 is always infinite. It is easy to show that the theory of f is complete. This is implied by the following lemma. 

Lemma 3.7 For any given model (M, f ), there is an elementary extension 

(M∗, f ∗) such that n ∞ is infinite. Proof: It is a simple compactness argument applied to the elementary diagram of 

(M, f ) together with the following set of sentences in an expanded language with new constant symbols di for each i ∈ ω. 

{di  = d j : i, j ∈ ω, i  = j} ∪ { f l(di )  = f m(d j ) : m, l, i, j ∈ ω, m  = l} ∪ {∃ x f k(x) = di : for all k, i ∈ ω}.

Each di generates a Z-orbit. Any finite subset of the above set of sentences has a model, since it is true in (M, f ). 

Two models of f with both n∞ and n1 infinite are obviously isomorphic and hence elementary equivalent. Via the previous lemma the theory of f is complete. It is also clear that the model with n∞ and n1 both infinite is recursive and can be represented as the union of countably many copies of N and countably many copies of Z. De-note such a model by (N, f ). We can always find an elementary extension of (N, f )

which is recursively saturated, and without loss of generality the model so obtained has countably many Z-orbits. If not, let Oα1, . . . , Oαn be the only Z-orbits of (N, f ).Consider the following type: 

{v  = f k(α i) : k ∈ ω, 1 ≤ i ≤ n} ∪ { αi  = f k(v) : k ∈ ω, 1 ≤ i ≤ n} ∪ {∃ x f k(x) = v : k ∈ ω}.

This type is finitely satisfiable in (N, f ) and hence by recursive saturation is realized in the model. In fact, n∞ is infinite if and only if (N, f ) is recursively saturated. The last step is to expand (N, f ) to a model of PA, and this is obtained via resplendency of 

(N, f ). First expand the language with the relational symbols for +, · , 0, c (0 and c

are just constant symbols). Consider the formula θ( x, y) defining the graph of f over 

N (θ ∈ 1 ∩ 1, using the hypothesis that f is computable). Let T be the theory in the expanded language containing the axioms of PA, the definition of f , and the set of sentences {∃ x f (x) = c, c  = f k(0) : k ∈ ω}. T is consistent with Th (N, f ) since N is a model of any finite fragment of T, and hence by resplendency there is an expansion of (N, f ) to a model of T. The model we get is a nonstandard model of PA where the function f is recursive. So functions such as 2 n, n!, pn n th prime may be recursive functions over nonstandard models of PA. We believe that with minor adjustments this result can be expanded to most unary recursive functions and may consider this in a later paper. If we consider functions of two variables such as xy and x[log 2 y] they are not recursive in any nonstandard model of PA, even if they are definable from 2 x and 

x[log 2 x], respectively. The complexity of the defining formula is higher than 0, and so the recursiveness of 2 x and x[log 2 x] cannot be transferred to xy and x[log 2 y], respec-tively. 92 PAOLA D’AQUINO 

Acknowledgments I would like to thank Angus Macintyre for pointing out to me the last remark. REFERENCES [1] Bennett, J. H., On spectra , Ph.D. Dissertation, Princeton University, Princeton, 1962. 2, 3 [2] Berarducci A., and M. Otero, “Recursive model of normal open induction,” The Journal of Symbolic Logic , vol. 61 (1996), pp. 1228–41. Zbl 0870.03025 1[3] Berarducci, A., and B. Intrigila, “Combinatorial principles in elementary number the-ory,” Annals of Pure and Applied Logic , vol. 55 (1991), pp. 35–50. Zbl 0747.03025 MR 92j:03051 1[4] Buss, S. R., Bounded Arithmetic , Bibliopolis, Naples, 1986 Zbl 0649.03042 MR 89h:03104 1[5] D’Aquino, P., “Pell equations and fragments of arithmetic,” Annals of Pure and Applied Logic , vol. 77 (1996), pp. 1–34. Zbl 0855.03034 MR 97a:03066 1, 2, 2, 3, 3, 3, 3 [6] Gaifman, H., and C. Dimitracopoulos, “Fragments of Peano’s Arithmetic and the MRDP theorem,” pp. 187–206 in Logic and Algorithmic, Monographie n. 30 de L’Enseignement Mathematique , Geneva, 1982. Zbl 0498.03045 MR 83j:03095 2, 3 [7] Kaye, R., Models of Peano Arithmetic , Oxford University Press, Oxford, 1991. Zbl 0744.03037 MR 92k:03034 1, 1 [8] Kaye, R., “Diophantine induction,” Annals of Pure and Applied Logic , vol. 46 (1990), pp. 1–40. Zbl 0693.03038 MR 91f:03117 1, 1, 1, 3, 3, 3, 3, 3, 3 [9] Manin, Y. I., A Course in Mathematical Logic , Graduate Text in Mathematics 53, Springer-Verlag, Berlin, 1977. Zbl 0383.03002 MR 56:15345 3, 3, 3, 3 [10] McAloon, K., “On the complexity of models of arithmetic,” Journal of Symbolic Logic ,vol. 47 (1982), pp. 403–15. Zbl 0519.03056 MR 84h:03084 1, 3 [11] Nelson, E., Predicative arithmetic , Princeton University Press, Princeton, 1986. Zbl 0617.03002 MR 88c:03061 1[12] Paris J. B., A. Wilkie, and A. Woods, “Provability of the pigeonhole principle and the existence of infinitely many primes,” The Journal of Symbolic Logic , vol. 53 (1988), pp. 1235–44. Zbl 0688.03042 MR 90d:03125 1[13] Shepherdson, J., “A nonstandard model for a free variable fragment of number theory,” 

Bulletin de l’Academique Polonaise des Sciences. S´ erie des Sciences, Mathematiques, Astronomique at Physiques , vol. 12 (1964), pp. 79–86. 1[14] Tennenbaum, S., “Non-Archimedean models for arithmetic,” Notices of American Mathematical Society , vol. 6 (1959), p. 270. 1[15] Wilkie, A., and J. Paris, “On the scheme of induction for bounded arithmetic formulas,” 

Annals of Pure and Applied Logic , vol. 35 (1987), pp. 261–302. Zbl 0647.03046 MR 89g:03087 1, 1 [16] Wilmers, G., “Bounded existential induction,” The Journal of Symbolic Logic , vol. 50 (1985), pp. 72–90. Zbl 0634.03029 MR 86h:03068 1, 3 TENNENBAUM PHENOMENON 93 

Istituto di Mathematica Seconda Universit` a di Napoli Piazza Duomo 81100 Caserta ITALY email: daquino@uniroma1.it

