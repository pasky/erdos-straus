Title: 1235421934.pdf

URL Source: https://projecteuclid.org/ebooks/perspectives-in-logic/Metamathematics-of-First-Order-Arithmetic/chapter/Chapter-V-Bounded-Arithmetic/pl/1235421934.pdf

Number of Pages: 132

Markdown Content:
All pure mathematics follows formally from twenty premisses. (Bertrand Russel, The Principles of Mathematics) 

# Part C 

# Bounded Arithmetic Chapter V 

# Bounded Arithmetic 

In the previous chapters we have encountered some weak fragments of arith-metic. First we have seen that some properties of numbers can be proved and several concepts can be formalized even in very weak fragments. Often we have used IΣ\ as a base theory where a weaker theory was possible. In this chapter we shall consider the possibility of formalizing syntax and some basic combinatorial concepts in weaker fragments. Section 3 will be devoted to this aim. Let us stress that the reason for trying to formalize certain con-cepts in weak fragments is not only our curiosity. In fact weak fragments are often needed in the study of strong theories. Recall the concept of a definable cut, Chap. Ill, Sect. 3. Cuts in fragments of PA which are closed under + and * define interpretations of bounded arithmetic (IΣQ and some stronger systems), but usually they do not interpret even IΣ\. Thus we need weak fragments in order to understand the theory of cuts. The second reason, which is perhaps the main reason for this research into weak fragments, is their close connection to computational complexity. It is obvious that there is some connection. In IΣQ we have induction for classes of bounded formulae. It is well-known that bounded formulae define easily-computable sets; for instance they are computable in linear space. This is however only a superficial observation. Some deeper connections will be shown in Chap. ΓV. It seems that more such relations are yet to be discovered. Some knowledge of complexity belongs to a general background of all working mathematicians. Even so, we have decided to include Sect. 2 as a short introduction in complexity theory, since concepts like the Polynomial Hierarchy are quite often disregarded in textbooks. Section 1 has a similar introductory role. We shall survey the most impor-tant weak fragments and prove some basic results on them. Note that some results on such theories (especially Q and I Open) have been proved in Chap. I, Sect. 1. The last section, Sect. 5, deals with classical metamathematical questions in the context of bounded arithmetic: unprovability of consistency, partial conservativity, interpretability. We will also have to develop some proof theory in Bounded Arithmetic. 268 V. Bounded Arithmetic 

In the proofs we shall not favor a particular proof technique; we shall mix proof theory with model theory, since our aim is not the study of one of these fields, but the study of weak fragments. An exception is Sect. 4, where we prefer model theory, since the same subject has been treated using proof theory in another book, [Buss 86, Bounded Arith.]; this section however contains several results not included in Buss's book. This chapter needs very little from the previous chapters and hence can be read almost independently. It requires only basic acquaintance with fragments of Peano arithmetic, Chap. I, Sects. 1 and 2. In Sect. 5 we shall work with definable cuts, thus we need Chap. Ill, Sect. 3. 

# 1. A Survey of Weak Fragments of Arithmetic 

## (a) Fragments of Arithmetic 

The weakest fragment that we consider in this book is Robinson's arithmetic Q. It was defined in Chap. I, Sect. 1. The fragments of arithmetic which use the language LQ are extensions of Q by adding a schema of induction for a restricted class of formulae and, possibly, an axiom saying that a certain function is total. Though Q proves only very few interesting statements about numbers, (it does not prove for instance the commutativity of addition), we shall see that quite strong theories are interpretable in it, (Sect. 5). Sometimes it is more convenient to start with a stronger theory. Usually one takes P " which is just the axiomatization of the nonegative part of the discretely ordered ring. These axioms are provable in /open and they are listed in Theorem 1.10, Chap. I, where we only have to add The next step in the hierarchy is iopen Several basic properties of natural numbers are provable already in this theory, see Chap. I, Sect. 1. In spite of this fact it is a very weak theory. There are models of I Open in which the following equations do have solutions i.e. the irrationality of y/2 and Fermat's last theorem for exponent 3 are not provable. Such independence results are possible, because there are re-cursively defined models of J ope n It seems that the properties such as the, property of having recursive models determine the border-line between very weak fragments and other fragments of arithmetic. J Open is an interesting 1. A Survey of Weak Fragments of Arithmetic 269 

object for research. However the methods needed for it axe different from those needed for stronger systems, therefore we shall not consider it here. Let us only mention here that one can prove independence results also for some strengthenings of J Open (as it is defined here). Then it is more conve-nient to define I Open to be a ring, not only the nonegative part of it, and add properties such as normality (which means that it is integrally closed in its fraction field and which implies that yJΪL is irrational). The next natural step in the hierarchy is IΣo; let us recall that this is 

Q with induction schema for all bounded formulae in language LQ. First we state two theorems which show that there is an essential difference between the structure of models of IΣQ and J Open> since none of these theorems holds for /open-1 The proofs require some facts which will be proved later. l l Theorem. There is no recursive nonstandard model of IΣo; in fact, in each nonstandard countable model M of IΣQ both + M aad *M Άre n o * recursive. 

Proof. Let A, B a recursively inseparable pair of subsets of N. Let φ and be ΣΌ formulae such that 

neAUN\=(3y)φ(n,y), neB = N 

Since A and B are disjoint, we have Hence, for every fc, 

M N (Vs, y, z < k)->(φ(x, y) & φ(x, z)) .Since this is a Σo formula, by overspill we get some a £ M nonstandard such that (Vtf, y, z < a)-i(φ(x, y) & ψ(x, z)) holds in M. Let C be defined by Then A Q C and C Π B = 0. Let C" be an initial segment of C. We shall code it by an element d of M in such a way that b belongs to C" iff the b-th 

prime divides d'. Clearly this coding can be expressed by a Σ\ formula. Using a similar overspill argument as above one can show that there is a c £ M

which codes the whole C, i.e.       

> 1Let us note that R. Kaye has defined a fragment of arithmetic for which 1.1 holds, but
> for which 1.2 fails. 270 V. Bounded Arithmetic

where pn is the n-th prime. Now assuming that +M is recursive, we can show that C is recursive: given π, search for r, s £ M, r <jvf s, such that 

> times

If r = 0, then p n divides c, hence n E C If r φ 0, then n £ C. Since this is a contradiction with recursive inseparability of A and 2?, +jvf cannot be recursive. In order to show that *JV/ is not recursive, code C by 2 C. This is possible, if we take c sufficiently small nonstandard. Then the procedure for testing n G C will search for u,v6 M, u < υ such that  

> pntimes

and decide according to the truth of u = 1. D

1.2 Theorem. Let M be a countable nonstandard model of IΣo Then there exists a nonstandard initial segment of M which is a model of PA. Proof. This is Theorem ΓV.3.39 strengthened form IΣχ to IΣo. Thus one only needs to check that the proof can be carried out in IΣo. We shall use a different argument. By Theorem IV.3.39, it suffices to prove that every countable model M 1= IΣQ has a nonstandard initial segment which is a model of IΣ\. We shall construct a semiregular short cut I and apply Theorem IV.2.16 to deduce that it is a model of IΣ\. We have to use some properties of IΣo which will be proved later in Sect. 3 (coding of sequences, definition of the graph of exponentiation). Let M be a countable model of IΣQ. Let g(x,y) be defined as follows 

g(x + l,y) = <7 y+1 (*,y) (y + 1 iterated Xx(g(x ty))). 

One can show that g(x,y) = z can be defined by a Σo formula and the inductive clauses can be proved in IΣo Let d £ M be a nonstandard number such that 2 2 exists in M. By overspill we can find a nonstandard c such that 

g(Cyc) exists in M. Take an enumeration /o, / i , . . . of functions coded in M

whose domain is [0, c] such that each function occurs in it infinitely often. Define a nested sequence of intervals 

[a o,g(c,ao)) 2 [a\,g(c- l,αχ)) D ...                               

> with αo = c, as follows. Suppose the sequence has been defined up to [α t,g(c—
> i,α, )). Decompose this interval into
> [ai,g(c -i -l , α f)) U [g(c -i-I,α, ),y 2(c -i-l , α , )) U ••U[g ai (c -i-lfαf-),ff β'+ 1 (c -,β, ) ) . 1. A Survey of Weak FVagments of Arithmetic 271

By the Pigeon Hole Principle (we can use it, since / t is coded in M) one of the intervals in the subdivision does not intersect the range of /,• restricted to the domain [0, α, ). This will be the next interval in the sequence. Let / be the cut determined by αo>αi>— The construction ensures that it is a cut (the successor function occurs infinitely often) it is semiregular (the range of 

fi restricted to α, is bounded by α l + i in /), nonstandard (since c E I) and short (since I < d). DBy the definition of Chap. 0 we allow only variables as the bounds in formulae of ΣQ. Let / be a function symbol. Extend LQ by / and let us denote by ΣQ the class of bounded formulae in the extended language where we allow the bounds at the quantifiers to be terms in the extended language 

£θ(/) Consider the following two theories: 

IΣl{f) + "/ i s monotone" 

IΣo(f) + "/ is monotone" . 

In the first one we extend the induction schema of IΣQ to Σ^ formulae, while in the second one we allow induction only for bounded formulae in 

L>o(f) where the bounds at the quantifiers are only variables. We have already considered a special case with / equal to exp. 

1.3 Proposition. The theories IΣζ(f) + "/ is monotone" and IΣo(f) + "/ is monotone" are equivalent. This proposition shows that it is not important which bounds are allowed at bounded quantifiers. The proof is almost identical with the proof of Lemma 1.1.30. It turns out that the graphs of exponentiation and several other important functions are definable by ΣQ formulae. IΣo does not prove that exponentia-tion (defined by such a formula) is a total function (see Theorem 1.4 below), but it does prove the inductive properties of it whenever the values exist. Thus instead of working in IΣo(exp) (with the inductive properties for exp) 

we can take IΣo with an axiom saying that exp defined by a Σo formula is a total function. Then I£o(exp), and hence IΣQ Xp (exp), will be conserva-tive extensions. (These extensions are conservative in a stronger sense: the new function symbol is definable in the subtheory.) The same holds for other monotone functions with Σo definable graphs. This shows that extension of 

IΣo by an axiom saying that a certain (Σo definable monotone) function is total has the same effect as an extension of the language. Hence it is natural to consider such theories to be versions of the intuitive concept of Bounded Arithmetic. 272 V. Bounded Arithmetic 

It is useful to realize that IΣ((f) has a Πι(f) axiomatization: replace the induction schema by the following version (Vz)(γ>(U)&(Vy < x)(ψ(y) - ψ(S(y))) -» φ)) 

for Σ$(f) formulae and omit the axiom (Q3). Let us recall some definitions from Chap. III. 

# (1) \x\ = no&(x + ir; 

(2) ωo(x) = 2x;       

> ωi+1 {x) = 2 U' (I XI-1), for x> 0 and ω, +i(0) = 0;

# (3) 2g = x, 

Further we consider the following axioms: (1) Λ<=4f(V*)(3y)("y = «*+!(*)"); (2) JSip = # (Va)(3y)("y = 2 s "); (3) ίuperexp =d} (Vx)(3y)(«y = 2*") Here we use the quotation marks to denote a ΣQ formula with the same meaning. At this point it is not obvious that such formulae exist. This will be proved in Sect. 3. In IΣQ we can also prove that ωj+i grows faster than ωt , 2X grows faster than each ω{ and 2% grows faster than 2X. Hence if ω{+ι 

is total, then ω t must be total too, etc. Thus we get the basic hierarchy of theories 

IΣ 0 C IΣo+Ωi C IΣ0+Ω2 C - . C IΣ^+Exp C IΣ O + Superexp .The most basic theorem about such systems of Bounded Arithmetic is the following one, which is usually referred to as Parikh's Theorem. 

1.4 Theorem. Let φ be a Σζ formula and let π be a Ilζ formula. Suppose that 

l + T Γ h (V*)(/(*) < fix + 1)), 

Then for some term t{x) of L(f) IΣξ(f) + π h (V*)(3y < ί(*))^(*. y). 

Proof. Suppose that the conclusion is false for any term t. Let c be a new constant. Thus for every term £, the following theory is consistent 1. A Survey of Weak Fragments of Arithmetic 273 

Since we can bound any finite set of terms by a single one, (for example 

IΣ^(f) h tχ(x), ..., tn(x) < tι(x) + + tn(x))i the following theory is also consistent 

IΣ{(f) + π + (Vy < ii(c))-.tf(c, y) + (Vy < t2(c))->ψ(c 9 y) + 

here we use an enumeration of all terms of L(f). Let M be a model of this theory and let K be defined by 

K = {aeM\Mta< *, (c), for some i} . 

Since / is monotone, K is a substructure of M. Since JJCjf (/) + π has a 

Πl(f) axiomatization K is a model of it. By the construction we have K 1=(Vy)-«V>( C

> y) which is a contradiction with the assumption of the theorem. D The theorem can easily be generalized by relaxing the assumptions about the theory. The essential assumptions are that the theory has a Π\(f) axiom-atization and proves some basic properties of terms. The theorem naturally transfers to the systems where / is not a function symbol but it is only de-fined by a bounded formula and an axiom saying that it is a total function is added. Let us consider two important examples. For IΣo this means that every 

ΣQ definable provably total function is bounded by a polynomial. We shall code sequences (say of O's and l's) by binary expansions of numbers; the length of a sequence x is thus \x\. Hence any provably total function can increase the length of a sequence only linearly. This prevents us defining polynomial time computations in IΣo and complicates also the formalization of other concepts. It can be easily seen that the axiom Ω\ just captures the polynomial increase of the lengths. Simple computations yield that for every term t with ω<ι there exists a polynomial p such that and vice versa, for every polynomial p there exists a term with u >2 such that Hence IΣo + Ω\ is a theory in which it is more comfortable to work. In par-ticular IΣo + Ω\ is stronger than IΣo. More generally we have the following corollary. 

1.5 Corollary. Let / and g be Σo definable monotone functions. Suppose g

grows faster than any function definable by a term in £(/) (in the standard model). Let ί?(/), resp. Ω(g), be formulae saying that /, resp. g, is a total 274 V. Bounded Arithmetic 

function for some ΣQ definition of the graph of /, resp. of g. Suppose that 

IΣo + β ( / ) proves that / is monotone. Then IΣo + •#(/) does not prove 

Ω(g). Proof. Let φ(x>y) be the Σo definition of f(x) = y and let ψ(x>y) be the definition of g(x) = y. (Hence e.g. Ω(g) is (\/x)(3y)ψ(x, y).) Let π be a formula in Lo(f) defined by π =df (Vz, y)(^(x, y) Ξ f(x) = y). Now suppose that IΣo + Ω(f) does prove Ω(g). Then also since T Γ implies β ( / ) . By Theorem 1.4 

IΣξ(f) + 7 τ h (VaO(3y < *(* 

for some term in Lo(f) Λ But this is a contradiction with the assumption that 

g grows faster than any function definable by a term in Lo(f). Ώ

1.6 Corollary. The hierarchy 

IΣo Q IΣo+Ωi C IΣo+Ω 2 C .. C IΣ 0 + Exp C IΣo + Superexp 

is proper. DThe sentences which separate the levels of this hierarchy are 772- We shall see in Sect. 5 that we can separate IΣo+Exp from IΣQ + ΩΠ by a Π\ sentence and the same is true for IΣo + Superexp and IΣo + Exp. Such separations remain, however, an open problem for the theories below IΣo +Now we turn our attention to hierarchies of theories obtained by restricting the quantifier complexity of the formulae allowed in the schema of induction. 

1.7 Definition. (1) Eo is the class of open formulae in XQ; (2) for n > 0, En is the class of bounded formulae in Lo in the prenex normal form where the first quantifier is 3, there are at most n alternations of quantifiers and the bounds at the quantifiers are terms in Lo (which must not contain variables of the current and the following quantifiers). 

Example. (3x < α)(3y < a)(xy = ahx >\hy >T) is an £χ formula. 1. A Survey of Weak Fragments of Arithmetic 275 

The theories IE{ axe defined in the usual manner: Q plus the induction schema restricted to J E7, formulae. Thus IEo is just / o p en There is a big gap between IEo and IE\. In particular Theorems 1.1 and 1.2 hold for IE\ and there are other reasons to consider IE\ to be relatively strong. On the other hand we are not able to prove that IE2 is stronger than IE\\ worse than that, we even do not know whether IE\ is weaker than IΣQ, 

These questions are connected with difficult open problems in complexity theory and they are probably very difficult too. We can resolve same of these problems, if we assume some conjectures about complexity classes. This will be shown in Sect. 4. We shall use a different hierarchy of theories there. We shall extend language LQ to a language L2 by adding more function symbols, we shall use a stronger theory instead of Q and also we modify the definition of the classes of bounded formulae, (see Sect. 4). In this way we obtain a straightforward connection between the Polynomial Hierarchy (these complexity classes will be defined in the following section) and the hierarchy of bounded formulae. The language Li contains a binary function symbol # whose intended in-terpretation is 2^1*^1. Other functions of Li can be bounded by polynomials. We have the following estimates 

ω2(x)<(x#x) 4.

Hence each function defined by a term in L2 can be estimated by a function defined by a term in Lo(ω 2) a^d v*ce versa. Thus if we use this language for defining a system of bounded arithmetic we should expect that we obtain something equivalent to IΣQ + Ω\. This system will be denoted by T2. There is an equivalent system 52 based on a modified schema of induction 52. The classes in the hierarchy of bounded formulae in L2 will be denoted by Σ\, i = 0,1, — The corresponding fragments will be denoted by TJ and 5£. Thus we have for instance: IE{ C Γ^. We shall concentrate on subsystems of T2

and 52; we have mentioned the hierarchy IE{ only for sake of completeness. 

* * 

In the previous part of the book we have encountered several principles which can be used instead of induction. Let us mention here at least the most important one: the least number principle. We know that LΣ{ (the least number principle for Σ{ formulae) is equivalent to IΣ{ (induction for 

Σ{ formulae). We can expect that a similar situation occurs in Bounded Arithmetic, if we replace the Arithmetical Hierarchy by the hierarchy of bounded formulae. For most principles this is really so, for instance induction 

and the least number principle axe equivalent also for the classes 27?, for i > 1. In Bounded Arithmetic we have also some principles whose counterparts for Σ{ have not been considered, since they are trivially equivalent to indue-276 V. Bounded Arithmetic 

tion. These are the schema PIND:        

> ^ ( 0 ) & ( V * ) ( V( L » / 2 J ) -φ(x)) -> (Vx)φ(x) ,

and schema LIND 

¥>(U)&(Vy < \x\)(φ(y) -» ψ(S(y))) -» γ>(|*|) The intuitive idea behind these schemata is the following. We can, in a sense, verify the conclusion φ(a) using the inductive property of φ in only \a\ steps. 

Such a verification procedure is thus polynomial in the size of input α, while it is exponential for the ordinary induction. The schema PIND is used to define 52 and its fragments 5^. Another important schema is the Pigeon Hole Principle, see Chap. I, 2.20. For higher fragments, the strength of PHP is given by Theorem 1.2.23. If we consider this principle for Σ"o formulae, then it is at least as strong as 

IΣQ. Whether it is derivable in IΣQ is an important open problem. We have some evidence that Σo-PHP might be stronger than IΣQ; we can prove some mathematical results using Σo-PHP which we are not able to derive in IΣQ 

itself. In particular we have 

Q + Σo-PHP h (\/x)(3p)(p >xk"pisa prime") ,

i.e. Σo-PHP proves that there are infinitely many primes, while we are not currently able to derive it in IΣQ. If Σo-PHP is stronger than IΣo then a philosophical question arises: what is a more basic principle, Induction or the Pigeon Hole Principle? 

* * * 

We have not exhausted all weak fragments that have ever been considered. You can find more in the literature listed in Bibliographical Remarks and Farther Reading. 

# 2. A Brief Introduction to Complexity Theory 

We shall outline some basic concepts of complexity theory. We shall present a little more than is needed for understanding the following sections, but we shall prove only those results which are in some sense connected with the following text. Prom the point of view of logic, the most interesting subject in complexity is the quantifier hierarchies such as the Polynomial Hierarchy. 2. A Brief Introduction to Complexity Theory 277 

## (a) Time and Space Complexity Classes 

There axe two basic computational models in complexity theory: Turing machines and Boolean circuits. Here we consider only the first one, and also we shall use only one type of it. By a Turing machine we mean an off-line multitape Turing machine, which is a finite automaton connected with a finite number of infinite (say in one direction only) tapes. The automaton is also called a finite control. The tapes consist of cells on which a symbol of a finite alphabet can be written. The automaton operates heads on tapes. A head can read and rewrite the symbols and move to the next cell (left or right). One of the tapes is distinguished as 

the input tape; the automaton cannot write on this tape. The automaton has a distinguished initial state and a subset of final states. A more up-to-date description would be in terms of a very restricted programming language (instead of the finite automaton) operating with linear arrays of symbols (instead of tapes). A Turing machine is used to define a language (i.e. a set of strings in a finite alphabet) or a mapping from the set of strings in an alphabet to another such set. The first type is called an acceptor, the second type is called a transducer. An acceptor is a Turing machine which has an input tape and several additional tapes called work tapes, and it has a distinguished subset of final states called accepting states. A word w is accepted if the machine reaches the accepting state when started in the initial state with w on the beginning of the input tape and with the rest of the tapes blank. The language 

accepted by the machine consists of all words accepted by it. A transducer is a similar device except that it has one more distinguished write-only tape. It computes a partial function F in an obvious way: to compute F(w), start with w on the input tape and read F(w) on the output tape when it reaches a final state. In one step, the machine reads the tapes, rewrites them, moves the heads by one cell and changes the state of the finite control. The time of the computation on w is the number of steps needed to reach an accepting state. The space is the number of cells used on the work tapes. At first it may seem that Turing machine time is a very bad approximation of the time needed by actual computers, because the actions of a Turing machine are very restricted. It turns out, however, that Turing machines are quite time efficient due to the fact that they have several tapes. In the case of the space complexity measure this is even more true and having more than one work tape is no advantage. 

2.1 Definition. Let / : N —» N be a function. We say that a language L is 

accepted in time (resp. space) /(n), if there exists a Turing machine M which accepts L and such that for every n and any w, \w\ = ny the time (resp. 278 V. Bounded Arithmetic 

space) of M on w is at most f(n). We define 

Time(f(n)) = {L \ L accepted in time /(n)}, 5pace(/(n)) = {L \ L accepted in space /(n)}.. Note that we do not fix the alphabet on work tapes. Hence if we increase the size of the alphabets we can obtain a faster and more space efficient machine. This is the idea behind the following theorem. 2.2 Theorem, (a) For f(ή) such that lim f(n)/n = oo and c > 0, T/me(max(n, /(n))) = 77me(max(n, cf(n)) .(b) For any /(n) and any c> 0, Interesting complexity classes are obtained by taking the unions over natural classes of bounding functions. 

2.3 Definition. 

LinTime = (JcGJV Time(cn) (Linear Time) 

P = \J ceN Time(n c) (Polynomial Time) 

E = {J ceN Time(c") 

Exp = \J ceN Time(2 ne ) (Exponential Time) 

LogSpace = Space(log n) (Logarithmic Space) 

LinSpace = Space(n) (Linear Space) 

PSpace = \J c£N Space(n c) (Polynomial Space) Note that by Theorem 2.2 we have LogSpace = Uc€iV Space(c. log n) and 

LinSpace = \J c€N Spacemen). 

We have the following trivial inclusions 

LinTimeCPC EC Exp LogSpace C LinSpace C PSpace 

Below we shall explain why these inclusions are in fact strict. We have also trivially Time(f(n)) C Space(f(n)), but there is a nontrivial result which gives more: 2.4 Theorem. For / ( n ) > n, Time(f(n)) C Space(f(n)/ log /(n)). 2. A Brief Introduction to Complexity Theory 279 

In the other direction only the trivial inclusion 

Space(f(n)) C (J Time{c^) 

c6N 

is known. (An /(n) space bounded machine cannot compute in time longer than c*^ n\ because it would run into a cycle.) Thus for instance, LogSpace CP, but it is a famous problem whether the inclusion is strict. The complexity classes above are defined for languages. We shall talk about the complexity of subsets of nonnegαtive integers using the standard binary coding. We can talk also about the complexity of relations, since we can code fc-tuples of words by single words using an additional symbol for separating them. Using transducers instead of acceptors we can define corresponding classes of functions, (Note that there is no simple reduction of a function class to the corresponding language class.) We shall not need the function classes corresponding to the classes of languages defined above except for the function class corresponding to P; it will be denoted by Dξ. Let us mention an alternative notation: the subsets of natural numbers which belong to LinSpace are also known as Grzegorczyk's class E+ .

# (b) Nondeterministic Computations 

A nondeterministic Turing machine is a Turing machine in which the finite automaton is nondeterministic (above we have considered only deterministic machines). This means that in some states there is more than one possible action of the machine. Thus there might be many possible computations on a given input word w. A word w is accepted by a machine if there exists (at least one) computation leading to an accepting state. When counting the computation resources needed for a given input word (time and space) we consider the worst case. Now we can define nondeterministic counterparts of the deterministic classes. They will be denoted simply by prefixing N. For example: Λ/P = I ) NTime(n c) (Nondeterministic Polynomial Time). Nondeterminism adds much power to the computations. We can guess 

a solution to a problem and then check its correctness. This suggests the following, more logical, definition of Λ/P: 

L £ NP = (3Λ(x, y) e P)(3p-polynomial)L = {x | (By, \y\ < p(\x\))R(x, y)} , 

see Theorem 2.11 below. As an example consider the complexity of the set of composite numbers. We can guess a proper divisor of a number k and check that it really is a 280 V. Bounded Arithmetic 

divisor of k. This proves that this set is in Λ/P; it is an open problem whether it is in P. The most important problem in complexity theory (and one of the most important problems in contemporary mathematics) is the question whether P = Λ/P. It is a part of a more general problem about the relation of nondeterministic classes to deterministic ones. We have the following trivial inclusions 

Time(f(n)) C NTime(f(n)) C Space(f(n)), 

but for converse simulations we have only exponential bounds. For space classes the situation is a little different: 2.5 Theorem. NSpace(f(n)) C Space(f(n) 2), provided f(n) can be computed in space /(n). Hence NPSpace = PSpace. 

The next natural step is to consider the role of the universal quantifier. Traditionally this is done by taking complements of the nondeterministic classes. Thus we introduce another prefix for complexity classes, co, to de-note the class of the complements of the sets in a given class. (It is superfluous in connection with deterministic classes, since they are closed under comple-ments.) The problem whether Λ/P = coNP arises quite often in connection with problems in logic. It seems likely that the time classes are not closed under complements. On the other hand, quite surprisingly, a proof has been found recently showing that nondeterministic space classes are closed under complements. 

2.6 Theorem. coNSpace(f(n)) = NSpace(f(n)), provided f(n) > log 2 n can be computed in nondeterministic space f(n). 

However, it is still open whether Space(f(n)) = NSpace(f(n)), in particu-   

> lar whether LogSpace =NLogSpace.

## (c) Degrees and Λ/P-completeness 

A set (language) A is polynomiαlly reducible to a set B if there exists a polynomial time computable function F (i.e. F E U\ ) such that F~ ι{B) = A. Clearly, this relation is a quasiordering, hence defines a structure of degrees. The smallest degree is P. 2.7 Theorem. There exists the largest degree contained in Λ/P. The sets in this degree are called NP-complete. Not only do Λ/P-complete sets exist, but they occur very naturally. There are hundreds of naturally de-fined Λ/P-complete problems. This fact is important for the P = Λ/P problem: 2. A Brief Introduction to Complexity Theory 281 

we know that Λ/P-complete sets are not in P, if P φ NP (which is accepted by most people almost as an axiom). Another consequence is that the statement "P φ NP" is equivalent to a J7 2 formula. Examples of A/P-compete Problems. (1) CLIQ UE - the set of pairs (G, k) where G is a graph containing a clique (i.e. a complete subgraph) of size k. (We assume that graphs are suitably coded as strings in a finite alphabet.) This is a typical Λ/P-complete set, since it is connected with an optimization problem: find the largest clique in a given graph. We shall talk about optimization problems at the end of Sect. 4. (2) HAMILTONIAN GRAPHS - the set of graphs that contain a cycle containing all vertices. (3) The set of triples (α, 6, c) of integers α, 6, c > 0 such that the equation (c.l) ax + by = c

is solvable in natural numbers. The last example shows that there are Λ/P-complete problems expressible by bounded formulae, since, clearly, we can bound any solution a?,y to (c.l) by c. This sets some limitations on the provability of Matiyasevic's theorem in weak fragments. Consider the formula 

φ(a, 6, c) = df (Vs, y < c)(ax 2 + byφc). 

By Matiyasevic's theorem there exists an open formula ψ(a y 6, c, z) such that 

N f= v ( α , 6, c) = (3z)V>(α, 6, c, z), where z = z\, ..., z^. Suppose this equivalence was provable in IΣQ + Ω\. 

Then in particular, 

IΣ 0 + Λi h φ(a, 6, c) -> (3i)tf(α, 6, c, z). Hence, by Theorem 1.4, we can add bounds to the variables z with the following form 

\z 1\,...,\z k\<p(\al\bl\c\), 

where p is a polynomial. Thus φ(a, b, c) would be equivalent to which would prove that y>(α, 6, c) defines a set in Λ/P. It can easily be proved that if the complement of an Λ/P-complete set is in Λ/P then Λ/P = coNP. 282 V. Bounded Arithmetic 

Hence if NP φ coNP, then the bounded formula φ(a, b, c) is not equivalent to an existential formula in IΣQ + Ω\. 

Let us mention only one more result about the degrees. 

2 8 Theorem. If P Φ NP, then the degrees below NP are dense; in particular, there is a degree strictly between P and Λ/P-complete sets. 

(d) Oracle Computations 

An oracle Turing machine is a Turing machine with a special tape, called 

an oracle tape, and special oracle states. In an oracle state the machine can perform exactly two actions. Given a set A, an oracle, the machine computes in the usual manner except when it reaches an oracle state. Then it asks whether the current word on the oracle tape belongs to A and acts according to the answer. Thus if the non-oracle states are deterministic, the computation is deterministic (provided A is fixed). In order to limit the amount of information provided by an oracle in the case of linear time computations, we shall assume that before the next query is asked, the previous one is erased. Let C be a complexity class and let A be a set (an oracle). We denote by 

C(A) the class defined in the same way as C except that the Turing machines are augmented with the oracle A. We say that C(A) is C relativized to A. 

We can also take a class A of oracles, in particular a complexity class, and consider 

C(A)= df U C(A). 

> A€A

Almost all statements about relations between complexity classes relativize, which means that they remain true if we add an oracle. On the other hand there is the following result which shows that the P = NP problem cannot be solved without going deep into the combinatorial structure of polynomial time computations. 

2.9 Theorem. There are oracles A an B such that P(A) = NP(A) and 

P(B) φ NP(B). 

Similar "independence" can be shown for other open problems about complexity classes. 2. A Brief Introduction to Complexity Theory 283 

## (e) The Linear Time Hierarchy and the Polynomial Hierarchy 

2.10 Definition. 

Eft" = df LinTime; Σ& =df NLinTimeiΣ^); 

LinH =df \J { Σf n {Linear Time Hierarchy)', 

-Ef+i =df NP(Σξ)i PH = df U, Σf (Polynomial (Time) Hierarchy); 

•ξ - functions computable in polynomial time; Πf_l_l =df Π^(Σf) - functions computable in polynomial time with oracles 

# from Σf. 

In particular, we have Σ"{ 1Λ = NLinTime and Σ% = NP. As usual we write 

Πf for coΣf and similarly for the classes of the Linear Time Hierarchy. We have also the same diagram of inclusions as for the Arithmetic Hierarchy, but it is an open problem whether any of these inclusions is strict, both for the Polynomial Hierarchy and for the Linear Time Hierarchy. We shall show that the "logical" definition of NP extends to all classes of the Polynomial Hierarchy and that there is a similar representation for the classes of the Linear Time Hierarchy. In order to simplify the formulae, let us write 

(3 Un x)φ{ov(3x,\x\<e(\y 1\,...,\y i\))ψ, 

where £(|yi|,..., \yi\) is a linear function (with positive coefficients) and yi,..., yι axe the free variables of φ. V'* n has the dual meaning; 3P and V? axe defined in the same way except that we use polynomials instead of linear functions. 

2.11 Theorem, (a) ΣJ tn is the class of sets defined by formulae of the form          

> ( a / ί n x i ) ( V / t n χ2)(Q lia χi)R(w, xlt x2,..., xi),

where R is in Lin Time, and Q is 3 if i is odd and V if i is even, (b) Σf is the class of sets defined by formulae of the form (3^i)(VP* 2 ) (Q pχi)R(w, *i, *2,..., xi) ,where R is in P and Q is 3 if i is odd and V if i is even. 

Proof. We shall sketch a proof of (a), since (b) is similar and, in fact, simpler. For i = 0 it is trivial. Consider t = 1. Thus we have a nondeterministic Turing 284 V. Bounded Arithmetic 

machine M running in linear time and an oracle for a set in LinTime. We would like to express the set accepted by the oracle machine by a formula 

(3 lin xι)R(w,xι) with R in LinTime. We shall use x\ to code the following information: (1) the nondeterministic decisions of the machine Λf, (2) the queries asked by the machine, and (3) the answers of the oracle. 

R will be computed by a machine which simulates M deterministically using 

xi and using the subroutine for the oracle. Note that the total time needed to run the subroutines is linear on the input size, since the sum of the lengths of the oracle queries is linear. Consider a general i. We use x\ to code the same information. By the induction assumption, the oracle answers are determined by a formula 

# (e.l) ( 3 * * 1 ) 0 ^ ) (Q^x'i^BHw 1,x' ly 4,...,zU). 

We need to express that the oracle answers coded by x\ are correct. This can be done by a conjunction of instances of (e.l) and its negation where 

w1 runs through the oracle answers. The negations of (e.l) are equivalent to formulae starting with a universal quantifier, hence their conjunction can be easily expressed as a single formula of the form 

# ", 4,4, --,4-ύ 

The nonnegated instances of the formula (e.l) can also be expressed by a single formula. Again the trick is that the sum of the lengths of the oracle queries is linear, hence also the sum of the lengths of the variables 

x' λ can be bounded using a linear function. We omit the details. The converse implication is easy. D*We shall show that LinH consists of sets definable by ΣQ formulae (in the language LQ] we consider only subsets of natural numbers). Later, in Sect. 4, we shall show that PH consists of sets definable by bounded formulae in £2. That is why these complexity classes are so important for us. We shall denote by ΣQ the subsets of natural numbers definable by Σo formulae. 

2.12 Lemma. LinTime C Σjf. Proof. We shall assume that a suitable coding of sequences can be expressed using ΣQ formulae. This will be done with details in Sect. 3. (Note that our task in Sect. 3 will be harder, since we shall develop coding of sequences in the theory IΣQ.) Furthermore we need the function nuon which counts the number of ones in a binary expansion of a number. A ΣQ formula defining this function is also constructed in Sect. 3. 2. A Brief Introduction to Complexity Theory 285 

Our goal is to express, by a ΣQ formula φ(w), that a machine M accepts a word w provided that M runs in linear time. To this end we need to code the computation of M by a sequence s whose length is linear in the length of w. 

This is because the polynomial bound on the size of numbers, as it is in £Ό, imposes a linear bound on their length and vice versa. We code sequences essentially by bits in binary expansions (see Sect. 3 for details). Suppose M has k heads. The sequence s will consist of (k + l)-tuples, one for each computation step. The first member of the (k + l)-tuple will code the state of M. The remaining members will be pairs, one for each head. They will code the currently read symbol and the direction in which the head will move. Clearly the length of (the code of) s is linear in the length of w. The sequence s does not contain information about the positions of heads on tapes explicitly, but this can be defined from 5 by a ΣQ formula. The position of a head in a computation step is the number of its moves to the right minus the number of its moves to the left prior to this step. The number of moves to the right (similarly to the left) is the number of occurrences of the symbol coding these moves in s. This can be easily reduced to the function nuon. 

Now for a given head and a given computation step (as coded in 5), we can determine using ΣQ formulae whether the currently read cell has been visited before, and if it has, then we can determine the last visit. In order to state that s is an accepting computation, we have to impose conditions on (k + 2)-tuples c,c +,α,C2,...,cfc, where c is en element of θ, c + is its successor, a is the symbol in the input word w read in the step corresponding to c and C2,..., c & are elements of s

which correspond to the last visits of work heads of the cells read in c, (some of them may be missing if some heads visit some cells for the first time). Since the automaton of M is finite and all the alphabets are finite, there are finitely many possibilities for such a (k + 2)-tuple and they can be listed. Finally, of course, we add that the last state is an accepting state. D   

> 2.13 Lemma. LinH CΣ(f.

Proof. This follows from Lemma 2.12, Theorem 2.11 and the observation made above that the growth rate of bounds in Theorem 2.11 and those of ΣQ 

are the same. DBefore showing the converse inclusion, we prove an important result. 

## (f) Nepomnjascij's Theorem 

We need to introduce another type of complexity class, classes defined by simultaneous resource bounds: 286 V. Bounded Arithmetic 

TimeSpace(f(n), g(n)) is the class of sets which can be accepted by Turing machines running simultaneously in time /(n) and space g(n). Note that this class is in general smaller than Time(f(n)) Π Space(g(n)). 

2.14 Theorem. Let ε be a rational number, 0 < ε < 1, and let α be a positive integer. Then TimeSpace(n α ,n €) C LinH. Proof. First we shall sketch an idea of the proof in which we shall assume that the numbers nα needed in the proof, with α rational, are integers and that they are computable in time nα (which is not always true). Let ε, 0 < ε < 1, be given. We shall prove by induction on k that 

TimeSpace(n k^' e\n e) C LinH. For k = 1 it is trivial. Suppose it holds for k. Let M be a Turing machine. We shall call α configuration the complete description of the machine state in a computation step, i.e. the state of the finite control, the position of heads, the content of the work tapes; only the input word is not included. We assume that configurations are naturally encoded as strings over a finite alphabet. Suppose M runs in space ne. Let an input word w and two configurations c\ , C2 of M be given. Then we can test in 

TimeSpace{n k(ι~€\n e) whether M will reach CΊ from c\ in n*^ 1"*) steps: just simulate M. Hence, by the induction hypothesis, this condition on tt>,ci, can be tested in LinH. Now let M1 be a machine running in time nί*"*" 1^1"and space ne. To show that Mf accepts a set in LinH we shall simulate Mf by an oracle nondeterministic Turing machine K running in linear time. Let w

be an input word. First, K constructs nondeterministically nι~e + 1 strings. Then it checks that: (1) the first string is the initial configuration of M'\ 

(2) every pair of consecutive strings are configurations of M1 such that M1

can reach the second one from the first one in n^ 1""*) steps; (3) the final string is an accepting configuration. Here (1) and (3) can be done deterministically in linear time (always assuming a reasonable coding of configurations). For (2) it will use the oracle shown to exist above. We need only to show that K runs in linear time. The key idea of the whole proof is that the total length of the n}~ € + 1 configurations is linear in n. This is because M1 runs in space n e; hence the strings representing configurations of M1 have lengths linear in n e .We have omitted several details, but we shall only comment on the one mentioned above. The problem is how to compute rnk^1"e^n. The point is that, due to nondeterminism, we do not have to count the number of steps during the simulation at all. More precisely, in the inductive construction we need only a relation R(w, cχ 5 C2) in LinH such that (1) if M will reach c<ι from c\ in n^ 1""*) steps on input w then R(w, c\, C2), and 2. A Brief Introduction to Complexity Theory 287 

(2) if R(w,cι,C2) then M will reach C 2 from c\ on input w (using possibly even more than n^ 1""*) steps). The simulating machine can guess the intermediate configurations that are evenly (as much as possible) distributed. DWe shall use this theorem directly only in a very special case (the next corollary). However the idea of using quantifiers in order to code longer than linear computations is very useful. We shall use it in Sect. 3 to construct a 

ΣQ definition of the function nuon. 

2.15 Corollary. LogSpace C LinH. Proof. We know that LogSpace C P, but the proof of this fact gives more: 

LogSpace C I ) TimeSpace(n , log n ) . 

k

Hence, by Theorem 2.14, LogSpace C LinH. D

2.16 Theorem. ΣQ definable sets are just the sets in the Linear Time Hierar-chy, i.e. ΣJ* = LinH. Proof. By Lemma 2.12, it remains to prove Σ$ C LinH. By Theorem 2.11 and since the bounded quantification is in both cases of the same growth rate, we only need to show that the open arithmetical formulae define sets in LinH. It can be easily shown that LinH is closed under set operations, hence the question reduces to atomic formulae. The relations = and < are easily computable in linear time and so is addition. We do not know whether multiplication of two numbers is computable in linear time (probably it is not), but we can show that it is computable in logarithmic space. This can be proved by analyzing the school algorithm for multiplication. Suppose we multiply a number of length n with a number of length m in binary. First we produce m numbers of length at most n + m and then we add them. This needs space of the order mn. However to add these numbers we do not have to write them down. We only have to remember the current row and the column and we can always compute the entry at this place. To remember the position, we need about log m+log n bits. Furthermore, we have to remember the carry, which is of length at most logm. Thus the total space needed to compute the product is logarithmic in the length of the numbers. It is also easily seen that we do not need to compute the multiplication as an operation; we only need to compute its graph. Hence, by Corollary 2.15 the graph of multiplication is in LinH. D288 V. Bounded Arithmetic 

## (g) The Diagonal Method for Separating Complexity Classes 

The most important problems in complexity theory can be stated as problems about separating some complexity classes (which means showing that they are different). In Bounded Arithmetic the most important problems are also about separating fragments of Bounded Arithmetic. There are two kinds of such problems. The first kind concerns fragments defined by restricting the quantifier complexity of an induction schema. For instance we do not know whether IE{ = IE, +i, Sι2 = Sι2+1 and T% = TJ* 1 . In the problems of the second kind, the meaning of "separation" is Π\ nonconservation. The typical problem here is whether IΣQ + Ω\ is Π\ conservative over IΣQ. For each fragment of Bounded Arithmetic there is a naturally assigned complexity class: the class of sets which are definable by formulae for which the induction schema is provable in the fragment. Thus ΣQ , i.e. LinH, corresponds to IΣQ, PH corresponds to IΣQ + ί?i, etc. The separation problems for fragments and those for the corresponding complexity classes seem to be connected, though we know very little about it (a connection is shown at the end of Sect. 4). (Let us note that one can consider different schemas of induction and different base theories, thus the correspondence between fragments and complexity classes is not one-to-one.) Here we would like to discuss a method on which almost all separation results in complexity rely. It is called diagonalization. Its applicability is limited; a rule of thumb is that we can separate only complexity classes defined using bounds to the same resources. The method turns out to be useless for time-space and determinism-nondeterminism problems. A natural question to ask now is what corresponds to this method in fragments of arithmetic. In metamathematics of arithmetic diagonalization is well-known: it is the essence of Gδdel's theorems. It seems that it has similar limitations in fragments of Bounded Arithmetic. In particular, no fragments have been separated for which the corresponding problem in complexity theory is open. We need some technical concepts before stating the basic results which use diagonalization. A function / is space constructible if there exists a Turing machine with one work tape which on each standard input of length n (say a word consisting of n O's) uses a space of exactly f(n). A function / is time constructible if there is a Turing machine which uses a time of exactly f(n) on each standard input of length n. These concepts are needed to avoid having possible pathological functions as space or time bounds; the usual bounding functions are easily shown to be space and time constructible. 

2.17 Theorem, (i) Let / and g be space constructible, f(n) > log 2 n and suppose liminf/(n)/flf(n) = O. Then 

Space(g(n))\Space(f(n))^iH. 2. A Brief Introduction to Complexity Theory 289 

(ii) Let / and g be time constructible and suppose liminf/(n)/flf(n) = O. Then 

Time(g(n)log 2g(n))\Time(f(n)) φ%. 

Thus we have LinTime C P C E ^ Exp and LogSpace C Lin Space C

PSpace. An interesting consequence of LogSpace ^ PSpace is that at least one of the inclusions in the following sequence is strict: 

LogSpace CPCNPC PSpace .

But for each of them it is an open problem. The idea of the proofs of both statements is essentially the same. Take a suitable coding of Turing machines as strings in an alphabet Σ. Let # b e a symbol not in Σ. Construct a Turing machine M which works as follows. On each input it will simulate a machine computing the bound g{n) and stop if the bound is achieved, so M is space (resp. time) bounded by g. If an input 

w is a code of a machine K followed by a string of #'s, at the same time (say, on an extra tape) M will simulate K on w in space (resp. time) limit <7(|ιt;|). If the simulation of K is finished before M runs out of space (resp. time), then M accepts w iff K does not. This situation must happen for each 

K which has a space (resp. time) bound /(n), since the bound g(n) for M is larger for a sufficiently long w. Thus the language accepted by M is different from the language accepted by each such K. The reason for g{n) log 2 g(n) 

instead of just g{n) in (ii) is that we have to simulate by M machines with an arbitrary number of tapes and this is not possible without an increase in time. The proof of the corresponding results for nondeterministic classes is more difficult. The problem is how to arrange that M accepts the input iff K does not. In the case of nondeterministic space classes we could use the fact that they are closed under complements (Theorem 2.6), but this cannot be used in the case of nondeterministic time classes. There is, however, a nice trick for avoiding this problem. This trick works even in more general situations. 

2.18 Theorem. Let C be a class of languages in an alphabet Σy with 0 € 17, let L be a language in the alphabet Σ, let r be a mapping assigning a word in the alphabet 17 to each language in C and let z be a mapping from C to natural numbers. Suppose that for every K G C (a) r(K)~0 2(κ> > eL = r(K)£K, 

(b) (Vj,0 < j < z(K))(r(K) - t y ' G ί Ξ r(K) - O^ 1 6 K). 

Then L £ C. (O ? denotes the string of j O's.) 290 V. Bounded Arithmetic 

Proof. Suppose L = K for some K € C. Then 

r(K) - 0 ' + 1 G ί Ξ r(UΓ) - 0 * + 1 Ghence by (b), 

r(K) eL = r(K) — 0zW G X. Thus by (a) which is a contradiction. •In the usual diagonalization we have only the simple condition r(K) €

L = r(K) ^ if, which is, however, sometimes more difficult to satisfy than (a) and (b) above. This is because we can take z to be an exponentially growing function. Then in order to determine whether r(K) ^ Qz(κ> £ L, we need to decide whether a much smaller word r(K) belongs to K. Theorem 2.18 can be used not only for nondeterministic classes, but also for classes with a larger quantifier prefix. We shall show only a very special case of such a theorem. 

2.19 Theorem. For every i > 0, Σf n § Σ? .

Proof. Let i be given. We shall apply Theorem 2.18 with C = Σf n. We shall also use the representation of Σ^ n and Σf given by Theorem 2.11. Thus every K £ Σι™ is defined by a formula          

> (g.l) ( 3 K n s i ) ( V / < n z2) . . . (Q Hn Xi)R(w, Xl ,x 2,...,xi),

where R is in LinTime. The diagonal language L will be defined by a formula of the form (3a>i,|a:i| < M 2)(Vs 2,|a:2l < H 2 ) . . .(Qx» \xi\ < \w\ 2)S(w,x lt x2,...,Xi), 

with 5(iί;,a;i,a:2> >χi) computable in time |ιt;| 4, for |«i|,..., |*»| < |tt>| 2,by a two tape deterministic Turing machine. We shall use the result that an f(n) time bounded multitape Turing machine can be simulated by a

cf(n) log 2 f(n) time-bounded two tape Turing machine, with c a constant. (We do not need such a good simulation; a simple polynomial simulation is sufficient, but then |iϋ| 4 must be replaced by a polynomial of higher degree.) Thus in order to simulate a linear time Turing machine, we need asymptoti-cally less than n 2 time. Let K € Σf n be defined by a formula (g.l) with tι(\w\\...,li(\w\) as the implicit linear bounds for the quantifiers. We take r(K) to be a word which contains a code of the machine computing R and the codes of the 2. A Brief Introduction to Complexity Theory 291 

linear bounds, and moreover assume it is sufficiently long. Namely we want, for n > |r(ΛΓ)|, 

h(n + 1) < n 2 ,... , 4 ( n + 1) < n 2 ,and that a computation of the predicate for |a?i|,..., |rr t | < |w| 2, \w\ > n be possible in time (|tu| — I ) 4 . Furthermore we construct r(K) so that it does not contain occurrences of 0. Clearly each such a K can be computed in exponential time. There is a fixed exponential bound f(n) such that each such K can be computed within this bound by a two tape Turing machine for sufficiently long inputs. Again, sufficiently long means longer than \r{K)\. We define z(K) = /(|r(UΓ)|). Now we define the machine M which determines the predicate S. Given an input (w ^ ft 7, x\ , a?2,..., s, ), where the last symbol of w is not 0, M will compare j and /(|w|) K j > f(\ w\) then what it does is not important. If 

j = /(|iϋ|), then M will try to interpret w as a code of a machine and linear bounds which determine a language K defined by a formula of the form (g.l). Again it is important only to consider the case where w is such a code. Then 

M will (deterministically) decide whether w G K. This is possible in time |tt> ^ ft 7!2, since j = /(|w|). M accepts such an input iff w £ K. (Thus in this case Z I , . . . , Z J are not used at all.) Clearly this ensures condition (a) of Theorem 2.18. Now suppose that j < f(\w\). In this case M will also try to interpret w as a code of a machine and linear bounds, but now it will compute the predicate for u = w ^ ( P + 1 . This can be done in time \w ^ ft 7!4, if w = r(K) (where 

K is the language determined by the code w) and |ajχ|,..., \x{\ < \w ^ ft 7!2.Hence we have   

> ,xι, X2,.

if and only if This proves that condition (b) of Theorem 2.18 is satisfied. Thus £ is a language which belongs to PH but not to LinH. D292 V. Bounded Arithmetic 

We say that LinH (PH resp.) collapses if for some i, LinH = Σf n (PH = Σf 

resp.). This is equivalent to Σf n = ϋf n (Σf = Πf resp.). We conjecture that neither LinH nor PH collapses and that LinH is a proper subclass of PH. But we have only the following result. 

2.20 Corollary. Either LinH § PH or LinH does not collapse. 

Proof. Suppose LinH = Σf n. Then LinH § PH, since, by Theorem 2.19, 

Σf n C Σf C PH. D

Let us define Σ"j, for / a function, to be the class of sets definable by formulae of the form < c/(M))(V*2, l*2l < c/(M)). -. {Qx» \*i\ < cf(\w\)) 

where c is a constant, R(w, xι,X2, ... ,xί) is computable in time c/(|κ;|) for every xi,...,x, , \xχ\ < c/(|tι;|),..., |s, | < c/(|iϋ|) and where Q is 3 if i is odd and V if i is even. Let 

TH(f(n)) =df\jΣ{ (Time Hierarchy / ) . 

> i

The proof of Theorem 2.19 can be generalized to prove a statement similar to Theorem 2.17 for classes Σf and Σf where g grows faster then / for each fixed i. For classes TH(f(ή)) this is an open problem (as we have mentioned above we do not know whether LinH = PH). Our last theorem shows that we can separate PH from slightly subexponential hierarchies. The bound 2 L n ' J

can be further decreased by iterating our method. 

2.21 Theorem. For ε > 0, PH g TH(2 - n # J ) . First we shall prove some lemmas. Let L be a language and suppose that 0 is not in the alphabet of X; let / be a function such that /(n) > n for all 

n. We define 

L[f] = d / {w - of(M)-M \weL}. 

2.22 Lemma. Let /, g be time constructive functions. (a) If /(n) > g{n) for n>n 0, then for every i > 0, Σ? C Σ{. 

(b) For every i > 0, L € Σ{ iff L[f) € Σ?". Proof, (a) is trivial, (b) follows easily from the definition of Σ{ and from the characterization of Σf n (Theorem 2.11 (a)). •2. A Brief Introduction to Complexity Theory 293 

2.23 Lemma. Let f,g be time constructible functions; let g be growing faster than every polynomial. Suppose TH(gf(n)) = PH. Then TW(//(n)) C PW. 

Proof. Let the assumption of the lemma be satisfied. Let L G 7~W(//(n)). Using Lemma 2.22 (b) we get first L[ff(n)] € LinH and then L[f] € TH(f). 

Since TH(gf(n)) = PW, we get L[f] G PW. Using Lemma 2.22 (b) again we have L\pf(n)] G LinH for some polynomial p. Hence L € TH(pf(n)). Since y grows faster than any polynomial we have 

TH(pf(n))CTH(gf(n)) = PH. 

Hence LePH. D

Proof of Theorem 22.1. Let ε > 0 be given. Let Suppose PH = TH(2 L n β j ). Then we have 

PH C TH(gf(n)) C TW(2 unβj ) = PH, since it can be easily computed that #/(n) grows faster than any polynomial but is smaller than 2 LΠ *J. Thus TH(gf(n)) = PW. By Lemma 2.23 we have 

TH(ff(n)) C PH. We have the following inclusions: 

PH C Exp C r/me ^ " Λ C 7H (tf^Λ C TH(ff(n)) C PW, 

where ε/2 > ε' > 0. The first inclusion is a natural simulation, the second one follows from Theorem 2.17 (ii), the third one is trivial and the fourth one follows from a simple computation and Lemma 2.22 (a). Thus we get a contradiction. DWe have defined several complexity classes, only a few of which will be mentioned in the following sections. The larger variety should help the reader to understand better the environment in which we are working, if we consider weak fragments. This short survey, however, cannot replace a textbook on such a broad subject. 294 V. Bounded Arithmetic 

# 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣ 0

# (a) Introduction 

In this chapter we shall present some basic constructions available in First we want to show that it is not necessary to add the relation xy = z to /ΣΌ, since it is definable there. To this end we have to develop the theory of sequences a little. Once we have the exponentiation relation we will be able to define a more efficient way of coding sequences. The second important task is to describe a formalization of syntax in IΣQ. A formalization of syntax in IΣ\ has been presented in Chap. I, Sect. 1 (b). However IΣQ is a much weaker theory and it is not always possible to use classical techniques here. Usually formalization is very tedious work and the reader can find very few interesting ideas there. We cannot skip this part completely however as we have to persuade the reader that such a formalization is possible in a theory which at first looks very weak. Therefore we have decided on a compromise: instead of describing a particular formalization we develop some tools which can be easily applied to most standard situations. Clearly the reader of this book is not looking for formulae, but he is interested in ideas and techniques. In this section we shall consider only combinatorial problems related to the formalization of syntax. More about the formalization will be presented in Sect. 5. The weaker the theory the more difficult it is to prove theorems. This applies to coding and formalization as well. Many concepts can be more easily handled in IΣQ + Ω\ than in IΣQ. Since much research is going on in 

IΣQ + Ω\ (or equivalent theories) it is worthwhile mentioning these simpler formalizations. Much of our intuition about natural numbers relies on exponentiation. Thus in order to persuade the reader about the possibility of a suitable for-malization of (some of) the usual reasoning on numbers in JΣΌ, we prove the properties of exponentiation in great detail. After introducing the exponen-tiation we shall use more sketchy arguments. Besides exponentiation we shall define one more important ΣΌ-definable function: "the number of ones in the binary expansion". With these two concepts in hand, formalization of syntax will proceed quite smoothly. The last subsection presents a general theorem which can be applied to formalize various syntactical concepts in IΣQ. 

In some estimates we shall use explicit numerals. The reason is that these numbers are easily computable and small. 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 295 

# (b) Sets and Sequences 

Since IΣQ contains I Open, we know, by Chap. I, Sect. 1, that we can prove some elementary number theoretical facts. In order to be able to interpret other combinatorial objects, we need to formalize the concept of the sequence. Our task would not be so difficult, if we could start with the exponentiation 

relation in our language. But so fax we do not know that this relation has a suitable definition in IΣo. An obvious requirement is that the defining formulae of the concepts be I7o, otherwise we cannot use IΣo Therefore we cannot use the usual definition of the exponentiation relation in JΣΊ, which is not bounded. Our approach is similar to that of [Nelson 86]. It is based on the observation that it is possible to talk about the digits in the binary expansion of a number, though (at first) we are not able to define that the digit in question is the i-th digit. The point is that we can define that a number is a power of 2 and then we can index the digits of a number by powers of 2. Namely, the i-th digit will have index 2*. Then, clearly, we can easily talk about the relative position of digits. To code a sequence of numbers we shall use a pair of numbers. The first number will be the number determined by the concatenation of binary expansions of the numbers to be coded. The second one will be a binary code of the markers which determine beginnings and ends of the coded numbers. In fact we code sequences of arbitrary 0-1 words in such a way, but we shall use this possibility only after we define the exponentiation relation. Let us consider an example. Suppose we want to code a sequence of 0-1 words 0011, 101, 010. Then we take two numbers whose binary expansion is the following 

11101010, 

10001001001. 

The first one is the concatenation of the words above (where we have to omit the first two 0's) and the second one is a sequence of markers which determines the partition. If this pair is considered to be a code of a sequence of numbers then it will code (3,5,2). Now we proceed formally in  

> 3.1 Definition (x is a power of 2).

The relations being a prime and p divides x used in this definition axe easily definable by ΣQ formulae. The following is also easy to prove. 296 V. Bounded Arithmetic 

3.2 Lemma (i) iW(ϊ); (ii) x > 1 -• (Pow(x) = (3y)(x = 2ybPow(y)))\ 

(iii) Pow{x) & Pow(y) --> Pow(xy) k (x \ y V y \ x); 

(iv) Pow(z) & Pow(y) & (2v + Ί)x = (2tι + T)y -> α; = y; (v) Pow(x) & Pow(y) & x^ = y -> Pow (z); (vi) x > 0 -• (3y)(a: < y < 2a: & Pow(y)). The last lemma allows us to define: 

3.3 Definition (y is the least power of 2 larger than x). lpw(x) = y = min{y; y < 2 x + l & x < y & Pow(y)} .

3.4 Lemma (/ΣΌ) (i) ^ ( 0 ) = ϊ ; (ii) x > 0 -> Zyw(α ) < 2x. D

After we define the exponentiation and the length function |aj|, it will be clear that lpw(x) = 2' XL Recall that we have a pairing function defined, say, see 1.1.18. 

3.5 Definition (p is a sequence). Seq(p) ΞΞ (3u, v < p)(p = (u, υ) & -iS I υ & /pw(tι) < r ) . Here u is the sequence of 0-1 words of length at least 1 and υ is the sequence of markers. At present we axe not able to define the i-th element in the list, but we can easily define that a number occurs in it. 

3.6 Definition. 

* € K V ) = (3y,y'<t;)( 

&y' >2kx 

Szv = υ22y'; 3t*i,«i<y)(= 

ί/ + y'y + y + 

3^2? υ2 ^ v){Pow{y)hPow{y l)2y'y + xy + u\ 

> vl)

Now we shall prove only the most basic properties of this coding, since we do not need more for defining and proving properties of exponentiation. 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 297 

We show that the empty set has a code and that we can always add another element (number) in the sequence. 

3.7 Lemma (IΣQ). 

(i) (V*)(not*€(0, ϊ)); 

(ii) (Vp, *)(&?(!>)-_ 

-> (3« < 9p(z + l) 2)(Seq(q) & (V*)(x eq = (xe PVx = *)))). 

Proof, (i) is trivial, (ii) Let p be a sequence, p = (u, v). Letfc= max(2, lpw(z)). 

Define 

t/ = Uk + 2 , 

Suppose tx > 0. Then we have 

u' < u * 2(z + T) + * < 3(z + ϊ)tι, vr < v * 2(z + T) + T < 3(z + ϊ)v . Since the pairing function is a quadratic polynomial, we have 

q<9(z+ϊ) 2p. 

We leave to the reader to prove this bound for u = 0. Now we are going to prove Seq(q). It is clear that υ1 is odd. To prove lpw(u f) < υ\ recall that we have z < lpw(z) < k and u < lpw(u) by definition and lpw{u) < v by the assumption that Seq(p). Thus 

u1 < uk + k < lpw{u)k < vk < υ1.Since Pow(lpw(u)k) y we have 

lpw(υ!) < lpw(u)k < υ 1,thus Seq(p). 

To show z 6 q put y = 1, y1 = k, v\ = u\ = 0. The verification of the inequalities is straightforward then. Now assume x £ p. We want to show a: G #. Let y,y /)wi,vi,W2» v2 D e 

witnesses of x being in p. Then 

u1 = U2y fyk + xyk + u\k + z,t/ = 2υ 2y;i/fc + y 7

yA; + yk + v λk + T. Thus the witnesses for x being in q are respectively 

yk, y\ u\k + z, vifc + T, u2 , ι>2. 298 V. Bounded Arithmetic 

We only have to check that 

u\k + z <yk 

and 

The inequalities are derived as follows 

u\k + z < u\k + k = (ui + ϊ)fc < yk ,

and similarly the second one. Now assume x G q. We want to show x £ p or x = z. Let us use y, y', ui, vi, U2y v 2 for witnesses of x being in q. We consider two cases. 

Case 1 , υ\ = 0. Since t > is odd and y' is even, y must be odd. As Pow(y), 

we have y = 1. Thus 

vk = v' - ϊ = 2v 2t/ + 1 / = (2v 2 + T y , hence, since v is odd, k = y f. Then life + £ = v! = I Z2& + X + l«l , but u\ = 0, since t*i < y = 1, and x < y 1 = k, z < k. Thus a: = z by the uniqueness of the remainder (see 1.1.15(4)). 

Case 2,v\ > 0. Then we have 

vk = v 1 - T = (2v 2y' + y' + T)y + vi - ϊ . Since vi — 1 < y, it is not possible that y | fc. As y is a power of 2, we have 

k I y, (by Lemma 3.2 (iii)). Hence k \ (vι — 1). Thus we have υ = 2v 2y'yk~ ι + y'yfc"" 1 + (vi - ϊ)*:"" 1,which is not a formula in the language of arithmetic, but clearly can be expressed by such a formula. Similarly we have 

uk = u 2 y'y + xy + wi - z.Since z < k and fc | y, it must be z <u\. Thus we can write 

u = u 2y'yk-' 1 + xyk" 1 + (tii - z)*" 1 .

All the inequalities for new witnesses follow immediately from the inequalities for the original witnesses. Thus x G p. D3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 299 

# (c) The Exponentiation Relation 

Our aim is to construct a ΣQ formula Exp(x,y,z) and to prove in IΣo * n e 

following formulae: (c.2) Exp(x, y + Ί,z) = (3υ)(Exp(x, y, v) k z = υx). 

Before starting the construction of the formula, let us observe that (c.l) and (c.2) imply some natural properties of Exp. 

3.8 Lemma 

(i) Exp (m, n, fc) = m" = k; 

(ii) Exp(x, y, z) k Exp(x, y, z1) -> z = *'; (iii) Exp(x yy,z)kv < y -> (3w < z)Exp(x,v,w). Proof, (i) - follows from (c.l),(c.2) and a similar fact for multiplication. (ii) We would like to prove it by induction over y. We can use x as a parameter, but what to do with z and zft ! The way out is to take the following formula instead of (ii): (Vz,z' < v)(Exp(x yy,z)kExp(x,y,z /) -> z = z1),and we can use v as a parameter of the induction. (iii) is quite similar. DThe problem with the natural definition which uses recursion is that the size of the sequence that codes the course of values cannot be bounded by a polynomial, which is a necessary requirement for a ΣQ formula. To overcome this difficulty we shall use sequences in which elements grow faster and hence they are shorter. The trick is to use the recursion on (binary) notation instead of the ordinary recursion. 

Example. Let y = 1101 in binary; then we compute 

> χ

o = 1 ? χι _ ^ χn _ χ2^ χiio _ (χ2* xγ^ 

First we define an auxiliary formula (this is similar but not the same formula as in 1.1.49). 

3.9 Definition. 

Exseq(x,s) = Seq(s)k(1,0) G θ&(Vy,z < s)[(z,y) E s-+ 

-> (z = ϊ & y = 0) V (y > 0b(3v,w < s)((y = 2υkz = w 2

k (w, v) e s) V (y = 2v + T& z = w 2x k (w, v) G s)))]. 300 V. Bounded Arithmetic 

3.10 Lemma (/ΣΌ) 

x > 2& Exseq(x,s)k(z,y) G s -» (2:,y) < 1z 2.

Proof. Using induction on y we get y < z and z >1. Then an easy computa-tion gives 

{z,y)<{z,z)<Az 2. D

3.11 Lemma (IΣΌ) 

> 16

)(z > 2SzExseq{x,s)k(z,y) 

Proof. The sequence with a single element (1,0) has number 30. Further we need the inequality (*) * 1 6 > 9 ( 4 * 4 + 1) 2, f o r z > 2 . We prove the lemma by induction over y with x and s as parameters. If 

y = 0, then z = 1, hence if the sequence t consists of a single element (1,0), we have t < 302 16 . Now assume that y1 > 0 and for every z < s there exists a t satisfying the condition. We want to find t1 for y1 and some z1 such that 

iz\y f) £s- By t h e definition of Exseq there exists (z,y) £ 5 such that either (i) 2/ = z2 and y' = 2y, or (ii) z' = z2x and y' = 2y + T. By the induction assumption we have some t for (z,y). By Lemma 3.7 we can extend t to t' by adding (z 1 ,y') to it and so that 

t'<9t((z',y') + lf. 

Clearly t satisfies Exseq(x,s). By lemma 3.10, we have 

If z = 1 then y = 0, hence y' = 1, z' = a; > 2, and we have, by (*), 

t' < 9 * 30 * (4(z') 4 + ϊ ) 2 < 30(z') 16 

If z > 2, then in case (i) we have, by (*), 

t' < 9 * 30z 16 * (4z 4 + T) 2 < 30z 32 = 3U(/) 1 6 ,3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 301 

and in case (ii) we have 

*' < 9 * 30* 16 * (4* V + T) 2 < 30* 3 V 6 = 30(/) 16 •

Now we are ready to define the exponentiation. 

> 3.12 Definition.

Exp(x, y, z) = (z = ϊ & y = 0) V (x < T& z = x &y > 0) V (3^ < 30z 16 )(Exseq(x, s) k (*, y) β s) .We have written the formula so that it is bounded, however Lemma 3.11 permits us to drop the bound at the existential quantifier, which will be useful below. It is easy to check that the formula satisfies ( c l ) . To prove (c.2) we first derive the recurrent formulae which correspond to the recursion on notation and then derive (c.2) from them. 

> 3.13 Lemma.

(c.3) Exp(x, y, z) -> Exp(x, 2y, z2) & Exp(x, 2y + T, z2x) 

(c.4) Exp(x, 2y, z) -> (Bit; < z)(w 2 = zkExp(x, y, w)) 

(c.5) Exp(x,2y + Ί,z) -> (3w < z)(w 2x = zkExp(x,y,w)). Proof, (c.3) The lemma is trivial for x < 1 or y = 0. Suppose x > 1, y > 0 and Exp(x,y,z). Let s be a witnessing sequence for Exp(x,y,z) i.e. 

Exseq(x,s) and (z,y) € s. By Lemma 3.7, we can extend this sequence to si (s2 respectively) by adding another element (j? 2,2y) ((z 2xr2y + 1) respectively). Then we have Exseq(x,Si), for i = 1,2. Now we do not have to worry about the size of si and 52, since, by Lemma 3.12, we can replace s\ 

and 52 by suitably bounded ones. (c.4) Again we can assume x > 1, y > 0. Let 5 be a witness for 

Exp(x, 2y, z). Then by definition of Exseq we have some w such that z = w2

and (w,y) E 5. Again Lemma 3.12 takes care of the size of 5. The proof of (c.5) is quite similar. D

3.14 Lemma 

Exp(x, y + T, z) = (3v < z)(Exp(x, y, v) & z = vx) .Observe that by Lemma 3.8 (ii) this is equivalent to (c.2). 302 V. Bounded Arithmetic 

Proof. Suppose that the formula is not true for some z, y and z. By IΣQ, we can assume that it holds for every y' < y and every J < z. Consider two cases: (i) y is even, say y = 2p. Then, by (c.4) and (c.3), 

Exp(x,y + T,z) = (3w < z){w 2x = zkExp(x yp,w)) 

= (3w < z)(Exp(x, 2p,w ) & w2x = z) .Thus taking υ = w2 we get a contradiction, (ii) y w odd, say y = 2p + 1. Then, similarly, 

Exp(x,y + Ί,z) = (3w <z)(w 2 =

Now by the induction assumption this is equivalent to (3iϋ, u < z)(Exp(x, jp, u)&ωa; = u; & iϋ = z) 

again by Lemma 3.7, we get 

(Bw yu < z)(Exp(x,2p + Ί, u x) & ux = tί; & ιy 2 = z) 

The contradiction is obtained now by taking υ = u2x. O

Now we can sum up what we have proved. 

3.15 Theorem. The clauses (c.l) and (c.2) are provable in IΣQ for the ΣQ 

formula of Definition 3.13. DOne can derive from (c.l) and (c.2) other natural properties of exponen-tiation in IΣo such as, for instance, 

Exp(x,yuzι)tzExp(x, y2,z2) -+ Exp(x,y\ + y 2,

Exp(x,y\,z)kExp{z, y2, w) -* Exp(x yyiy 2, w) 

Thus it is natural to ask whether the clauses (c.l) and (c.2) are sufficient for deriving all the other properties or we have to use sometimes also the explicit definition of the exponentiation relation. The answer is given by the following easy theorem. 

3.16 Theorem. Let E be a new ternary relation symbol. Let IΣo(E) be the theory IΣo with the induction schema extended to bounded formulae containing E and with additional axioms ( e l ) ' E(x,0,z)=z=Ί; 

(c.2)' E(x, y + 1, z) = (3υ)(E{x, y,v)bz = vx). 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣo 303 

Then IΣQ(E) proves Thus whatever we can prove about the exponentiation in IΣo, it can be derived from (c.l) and (c.2) (using the fact that it is defined by a bounded formula). 

Proof. By induction over y we prove the following formula in IΣQ(E): 

(to < u)(E(x, y, z) = Exp(x, y, z)) . DLet us note that what we have described is not the only possible approach. In fact it is even possible to find a Σo formula for exponentiation which does not use any concept of coding sequences, based on the representation of the power xy in the form - l)υ + y] + 1, for some υ, see [Pudlak 83, A definition]. 

# (d) Developing IΣQ + Ω\ 

For a moment we shall digress to IΣQ + Ω\ . Recall that the theory IΣo + Ω\ 

is the theory in the language LQ with the following axioms 

Q + IΣ 0 + Ωι 

where Ω\ is 

(Vx)(3y){y=ω 2(x)). 

Let us note that often another function ω(x) = x'^' is used instead of u>2. The function u >2 can be expressed using the exponentiation and the length functions as follows. 

(x) = 22

Thus formula y = ω2(x) is just an abbreviation which uses the definition of exponentiation and the length function. Hence in order to able to state Ω\ 

we must first construct a definition of exponentiation. If we want to work only in IΣo + Ω\ and do not need the definition of exponentiation in IΣo, 

we can use a simpler definition of exponentiation. 

3.17 Definition. 

Λiz) = (x = 0kz = 0)V (x =Tkz = Ί) 

V (3s)[Seq(s)k(z,y) G 6&(Vυ < s)((v,0) Gs = v = ϊ ) & (Vi < y)(Viϋ < s)((w, i + T) G s = (3v < s)((v, i)eskw = vx))] .304 V. Bounded Arithmetic 

Here the defining formula is not bounded. One can show that s can be bounded by a polynomial in 102(2), and that there is no better bound. This has the following effect. If, for instance, we define the length function, which we need for the axiom Ωχ y by 

|«|l = y = (3z)(Ex Pl (2,y,z)kx + ϊ< z < 2(x + ϊ)), 

then already the statement implies Ω\. (Of course, this would be an awkward way to define IΣo + Ω\.) 

The bound to the size of s in Expι(x yy,z) can be proved in IΣo + Ω\. 

Since induction for formulae with such a bound is also provable in IΣo + Ω\ 

(Proposition 1.3), Exj>ι(x,y, z) is equivalent to Exp(x,y,z), (and to any bounded definition satisfying the inductive clauses). The simplified definition of exponentiation in IΣo + ΦL does not save us much work, since we still have to prove a lot of things. But for further concepts Ω\ helps very much. Most of the syntactical concepts are naturally defined by recursion. The natural way to formalize definitions by recursion is to state that there exists a sequence (or a set) that codes the preceding values of the function. (This is called the course of values definition.) These sequences are usually of polynomial length, which is just captured by Ω\. To get around with sequences of linear length requires additional tricks. We shall mention simpler definitions of the function number of ones and the property 

being a term in IΣQ + Ω\ in subsections (e) and (g). 

# (e) The Number of Ones in a Binary Expansion 

We need another important ΣQ definable function, the number of occurrences of 1 in the binary expansion of a number x. We shall denote this function by nuon(x). As nuon(x) < x, the function is provably total in IΣQ. Using complexity considerations, it is easy to show that nuon is ΣQ definable, since it is computable in LogSpace. However, again, we need a Σo definition which captures its properties in IΣo, thus we have to define it explicitly. The basic properties of nuon(x) are the following: (e.l) nuon(0) = 0; 

(e.2) nuon(2x) = nuon(x) 

(e.3) nuon(2x + ϊ ) = nuon(x) + T. 

Again, one can easily show in IΣo that any two Σo definitions satisfying the clauses above are equivalent. 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 305 

Our next goal is to define nuon(x) by a ΣQ formula and prove (e.1-3) in 

IΣQ. We shall proceed faster than in the previous section. From now on we shall use the usual notation for exponentiation instead of Exp(x,y,z). Thus if xy is used in a formula without any comment, it means that the existence of this number is somehow guaranteed. 

3.18 Definition. 

(i) sgm(x,i, j) = y = (3xι,x 2 < x)(x = x\2J +y2* + x 2&X2 < 2* 

ky<2i" i) for i < j , otherwise 0; (ii) bit(x, i) = sgm(x, i, i + T); (iii) |z| = min{y | x < 2y). 

Here sgm(x,i,j) is the part of x between the i-th and (j — l)-th digit; 

bit(x,i) is the 2-th dyadic digit of x (see 1.1.31); \x\ is the length of the binary representation of x. (The length function has been defined before, formula (iii) gives an explicit definition of it in terms of the exponentiation.) We leave to the reader to check that formula (ii) is equivalent to a ΣΌ formula and that 2^1 has the same meaning as lpw(x). 

3.19 Definition.         

> Nuonseq(s,x,y) = Seq(s)&(Vz < s ) ( ( z , 0 ) G s=z = 0 ) & ( y , \x\) E s &

& (Vi < \x\)(\/z < s)((z, i + T) G s = (3υ < θ)((υ, i) G sSzz = v + bit(x,i))) .

3.20 Lemma. There exists an absolute constant K such that IΣQ proves 2l*l 2exists -• (3θ < 2K*\ x\*)(3y < x) Nuonseq(s,x,y) .(The antecedent should be written more precisely as 

(3z)Exp(2, \x\\z). Proof. The formal proof in IΣQ would be similar to the proof of Lemma 3.11. Here we only check the size of s in the standard model. The sequence s

contains \x\ elements of the form (z,i) where z < i < \x\. Thus its length is at most ΛΓ*|x|*||x|| < ϋΓ* |x| 2 . D

3.21 Lemma 

Nuonseq(s,x,y)&Nuon3tq(tι,2x,yι) -> y\ = yNuon3eq(s, x, y) & Nuonseqfa, 2x + 1,2/2) — • 2 /2 = V +306 V. Bounded Arithmetic 

Proof. Using induction over i = 0,..., \x\ show that 

# •

In IΣo + β i we can define nuon(x) = y by = y = (3s)iV since by Lemma 3.20 we know that 5 can be bounded by a function which is total in IΣQ + /?i, (the subscript is used to distinguish different formulae). Then we can use Lemma 3.21 to prove clauses (e.l-e.3). Unfortunately we cannot use this formula in IΣo a s there is no polynomial bound to such an s. 

We have to use a more complicated construction. The idea is similar to that of Nepomnjascij presented in Sect. 1 of this chapter. Namely, we cut x into segments x, such that on each segment x t we can use nuon\{x{), because the witnessing sequences are bounded by a polynomial in in x (i.e. the pieces are small enough). Then nuon(x) is computed as the sum of the values nuon\(xi). 

We need the following function, whose graph is ΣQ definable in IΣQ:     

> lf(x) = Q if x = 0,

= \x x\ otherwise.                 

> 3.22 Definition. Let nuon(0) = 0 and, for x > 0, let
> nuon(x) = y = (Ξί) [Seq(t) & (V* < *)[(*, 0) €t=z= 0]

&(V < *)(Z/(i) <\x\< / / ( • + T) -> (y,< + T) G t) &(Vi < x)(V2 < t)[lf(i) < \x\ -+ ((z,i + 1) G * 

*, //(i), //(i + 1)))))]] . 

In order to show that this formula is ΣQ over IΣQ we have to find a polynomial bound for t and for the sequences s in nuon\. First observe that, for a sufficiently large constant c, Thus we need only those t's which are smaller than this bound. Now we have to estimate 

sgm(x,lf(i),lf(i + l)). 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 307 

The length of this number is bounded by lf(i + l)—lf(i). Using the inequality 

a < 2l αl < 2α, for a > 0, we get, for i > 0, which tends to 2e(i -f 1) as i —* oo. Thus we have, for some constants c1, c" and i > 0, 

# , l/(i), I/(i + 1)) < 2W 

Now, by Lemma 3.20, nuon\(sgm{x,lf{i),lf{i + ϊ))) is witnessed by a se-

quence s such that 

for some constant K\ which is a bound polynomial in x. The sequence t

consists of CJΓTΓ elements. The elements have form (2, ϊ) with thus the length of (z, i) is linear in ||x||. Hence the length of t is linear in |x|, i.e. t is bounded by a polynomial in x. 

The proof above has been done in the standard model. The proof in IΣQ 

would be more complicated, but very similar to the proof of Lemma 3.11. We sketch briefly this argument. First we can estimate in IΣQ 

for k < ί, hence we get (1 + \/i) % < 5 and we can use (e.4). Secondly we need to estimate elements (z,i) of the sequence t for \i %\ < \x\. This is done by showing that nuon\{a) < |α|, whenever defined (by induction on the length of α), from which we get (2, %) < p(\x\) for some polynomial p. For a given x

take the largest j such that \p\ < \x\. By induction over j we show that the sequence t can be bounded by q(i %) for a suitable polynomial which we shall specify later. Suppose that such a bound holds for j and let x be such that j + 1 is the maximal such that Kj + l} 7"*" 1! < \x\. Let x1 = sgm(x,Q,ji). Thus we have some t' for x1 with tf < q(p). To obtain t for x, we only need to add 308 V. Bounded Arithmetic 

an element (zj + 1 ) to t. Since (zj + 1) < p(W\) and j + 1 is about we have, for a suitable polynomial r, (zj + 1) < r(j). Thus, by Lemma 3.7 The induction can now be completed, if we ensure that which can be done by taking polynomial q sufficiently large with respect to r'. Thus we have shown: 

3.23 Lemma. In IΣQ the formula defining nuon(x) = y is equivalent to a ΣQ 

formula. •

Remark. There are, of course, other possible ways to divide the binary ex-pansion of x for the definition of nuon. The reasons why we have chosen the partition determined by the function lf(i) are the following: (1) it does not depend on x, hence we can easily use induction; (2) it grows smoothly, (while e.g. i * |i| makes big jumps). 

> 3.24 Lemma.

(i) The formula nuon(x) = y defines a function in IΣQ. 

(ii) The formula nuon(x) = y satisfies (e.l-e.3) provably in IΣQ. Proof. The proof of (i) is omitted. The proof of (e.l) follows from the defini-tion. To prove (e.2) and (e.3) we would like to simulate the proof of Lemma 3.21. Now we cannot code the sequence of the values of nuon(x f) for all ini-tial segments x1 of a; by a number, but we can define these values by a ΣQ 

formula. Namely, let t be a witness of nuon(x) = y, let k < \x\ + 1. Then the value z = nuon{x') for the initial segment x1 of x of length k is defined by 

φ(z,k,t,x) = (3z»(|ή < h < \(i + l) ί

fzz = v + nuonι(sgm(X) |i*|, A?))). Similarly as above one can show that φ is ΣQ in IΣQ. NOW let t1 be a witness for nuon(2x) = yf. Since, by Lemma 3.21, nuon\{2ά) = nuon\(a), we have, by induction on fc, 

φ(z,k,t,x) = φ(z,k,t ι,2x) .But we have also hence y = y1. The proof of (e.3) is similar. •3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 309 

3.25 Lemma. 

nuon(x2\ y\ + y) = nuon(x) + nuon(y) . Proof. First we show that M y), and then use (e.l-e.3) and induction PIND (which is derivable from the ordinary induction, see Sect. 4) over y. DAlso here there is an alternative way to define the concept nuon. This was suggested by S. Buss, (unpublished). The idea is to count ones in the straightforward way as in nuon\ except that we include in the sequence of 

Nuonseq only the bits which have been changed. Thus e.g. the following sequence 1,10,10,11,100,101,101,110, 111, 1000, will be replaced by 1,10, ,1,100,1, ,10,1,1000. Then we need at most 2π bits to count up to the number n (plus bits needed to separate the members of the sequence). 

## (f) Coding Sequences 

Using the function nuon we are now able to define a very efficient coding, which is close to the information theoretical lower bound. Before defining 

nuon we were able to say that an element x belongs to a sequence and that an element x precedes an element y in sequence s. Now we can define that x

is the i-th element of s. 

3.26 Definition. 

(s)i = x if (3tι,υ < s)(3y,y f < v)(3uι,vι < y)(3u 2,V2 < v)(Seq(s) &cs = {u,v)kPow{y)&Pow(y')ky' >2kx<y' 

& u = U2y'y + xy + uι&εv = vfiy'y + y'y + y + v\ 

&i = nuon{yι)) .= 0 otherwise. Thus (s)i = x is defined by the same formula a s i G θ (Definition 3.6) except that we have added the condition i = nuon(υ{). The meaning of this condition 310 V. Bounded Arithmetic 

is clear: i is the number of markers before the beginning of the occurrence of a: in u. Next we define the length of a sequence and concatenation of two sequences. 

3.27 Definition. 

(i) lh(s) = nuon(v) — 1, if Seq(s) &(3u < s)s = (u,v) 

= 0 otherwise, (ii) For s,t such that Seq(s), Seq(t) y s = (w,v) and t = (u ; ,t/) where otherwise we set s ^ t = U. Note that these functions are defined by Σo formulae. We shall state the most important properties of concatenation. The role of the empty sequence is played by (1,0). 

3.28 Lemma (IΣo). For all x,y,z such that Seq(x), Seq(y) and Seq(z) 

(i) (T,U)-x = x-(ϊ,0) = x; (ii) x s-^y = x <~* z —v y = z\ 

(iii) y^x = z^x-^y = z] 

(iv) x ^ (y ^ z) = (x ^ y) ^ z; 

(v) ZΛ(T,O) = 0, /Λ(* - y) = ZΛ(x) + lh(y). Proof. The proofs are just tedious verifications. Therefore we prove only (ii) to illustrate the proof technique. Let x = (tι(a?),υ(a?)), y = (tι(y),υ(y)), z = (u(z),v(z)). Suppose x ^ y =  

> x <^> z, t h e n

(t (ίr) - l ^ l ^ l - 1 + υ(y) = (*(*) - l)2l v WI-χ + v(z). Since the function a ι—• 2l α'~ 1 is nondecreasing, we have υ(y) = v(2r). Further we have 

> w

(a:)2l υ(2/>l~ 1 + u(y) = u(x)2l t; WI-" 1 + tι(z) . Since, by the definition of Seq, \u(y)\ < |v(y)|, \u(z)\ < \v(z)\ and since 

v(y) = v(z), we have u(y) = u(2r) by the lemma about division with reminder Theorem 1.1.10(6). DSince x,y ι-> x ^ y is a total function in JΣΌ, it must be bounded by a polynomial in x,y. We shall state an explicit bound now. The proof is just an easy computation. 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 311 

3.29 Proposition (IΣQ). S ^ t < 64s*. The maximal element of a sequence s is trivially definable by a Σo formula, it will be denoted by max(s). We shall use max(s) and lh(s) to write down an explicit bound to the size of t which codes the same sequence of numbers as s. We cannot bound s itself, since numbers in s can be represented by 0-1 sequences with many 0's before the first 1. This is a drawback of our definition. 

3.30 Proposition. 

Seq(s) -* (3t)(Seq(t)klh(t) = JΛ(θ)&(V0 < i < ZΛ(*))((t) t = (*),-) & |*| < (2| max(s)| + 4) * lh(s) + 2). 

Proof. By induction on j , j = lh(s), lh(s) — l,...,0, we shall prove the following formula 

(3t)(Seq(t) & lh(i) = lh(s) - j & (V0 < i < lh(s) - j)((t)i = (s) j+i )k \t\ < (2| max(s)| + 4) * (lh(s) - j) + 2). For j = lh(s) put t = (0,1) = 1. Suppose it is true for 0 < j < lh(s), i.e. we have some t1 for j . Then let t be t' extended by (s)j-i as described in the proof of Lemma 3.7. It is not difficult to check that (t), = (t')i-i for 

i = 1,...,/Λ(θ) - j , and (t)o = (s)j-i. Hence (t) t = (θ)j_i+ t . Further we have 

t < 9if ((a)j-ι + I ) 2 < 9ί ;(max(3) + I ) 2 .An easy computation gives us 1*1 < 4 + \t'\ + 2|max(θ)| < (2|max(s)| + 4)(/A(J) - J + 1) + 2. Thus the formula is proved. Taking j = 0 we obtain our proposition. DSuppose a finite sequence of numbers is defined by a Σo formula. In 

IΣQ + Exp such a sequence always has a code. When does it have a code in IΣo, i.e. which comprehension principles hold in IΣQΊ The answer is that there is only one essential restriction: the length of the code must be linear in the parameters. We state an example of a replacement schema which is valid in 

3.31 Proposition. For every ΣQ formula φ(x,y) IΣo proves (V* < u)(3y < v)φ(x,y)k(3z)(z = (v + 2) u) -* -> (3s)(lh(a) = uk(Vx< u)(φ(x, (s) x)&(s) x < υ)) .

Proof. By induction on it; similar to the proof of Proposition 3.30. 312 V. Bounded Arithmetic 

# (g) Syntactical Concepts 

We shall use natural representation of syntactical objects as particular se-quences (words) in a finite alphabet. Since we have concatenation, we do not have problems with the properties which can be derived form definitions based on rudimentary formulae. Recall that x is a part of y is defined by 

x Q P y = (3u, v < y)(y = u<^x^v), 

which is a ΣQ formula. (Rudimentary formulae are the formulae in the lan-guage { = , ^ } with bounded quantifiers of the form 5a: Cp y and Vx Cp y.) 

Thus, for instance, once we have the concept of a formula, we can define the concept of being a subformula and prove its properties. Similarly there are no problems with defining that a variable does (not) occur in a formula etc. What is not quite obvious is that we can define the concept of terms and formulae by ΣQ formulae. Actually, it is sufficient to define only terms, since terms are essentially trees and other syntactical concepts can be represented as particular labelled trees with some additional properties (these properties usually defined by rudimentary formulae). We shall consider a simplified situation: We have four symbols, a variable v, brackets (,), and a binary operation symbol o. Then the terms are the smallest set satisfying: (1) v is a term; (2) if s and t are terms, then (s o t) is a term. A formula Term(x) defining the concept of terms must satisfy the following clauses: (g.l) Γerm(v) (g.2) Term(x) & Γerm(y) -> Term(( ^ z ^ o ^ y ^ ) ) ; (g.3) Term(x) -> x = v V (3p 9 q)( Term(p) & Term(q) 

The first two express formally (1) and (2), (g.3) corresponds to the clause that "Term is the smallest set satisfying (1) and (2)". In fact we can prove that any two Σb formulae satisfying (g.1-3) are equivalent in IΣQ. It is exactly the same situation as with exponentiation and function nuon of subsection (e). In IΣQ -I- Ω\ we can use the following simple definition: 

Termι(x) = (3s)(Seq(s)kx G sk(Vy G s)(y = v 

From now on we agree to omit the sign for concatenation whenever there is no danger of confusion. The proof of (g.1-3) for Ttrm\ in IΣQ + Ω\ is easy. 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 313 

Our approach in IΣQ will be based on counting brackets. The occurrences of brackets (or other symbols) can be easily coded by occurrences of ones in the binary expansion of a number. Thus we can again use function nuon. 

Since this transformation is easy, we shall use less formal descriptions of formulae. 

3.32 Definition, (well-bracketing, sub-well-bracketing, term) (i) WB(x) = (1) the number of "(" in x equals to the number of " ) " in x\ 

(2) the number of " ) " in each proper initial segment of x is less than the number of "(" in it; (3) x is nonempty. (ii) SubWB(x,y) = WB(x)k WB{y)kx Cp y. 

(Hi) Term(x) = WB{x)k{iy)(SubWB(y,x) -> y = v V (3p,q)(SubWB(p,x)kSubWB(q,x)ky = (p o q))). 

3.33 Lemma. WB{x), SubWB{x,y) and Term(x) are ΣQ over IΣQ. Proof. These formulas use ΣQ defined predicates and functions (for counting brackets use the function nuon); the quantification can be made bounded. D 

3.34 Lemma. IΣo proves (g.1-3) for the definition of Term(x) above. 

Proof, (g.l) is obvious. To prove (g.2), assume Term(x) and Γerm(y) and let 

z = (x o y). The condition WB(z) is easy. Let u be a sub-well-bracketing of 

z. Clearly it is now sufficient to show that u is either a part of x or a part of y or u equals to z. If u is not a part of x nor a part of y, it must contain the first occurrence of "(" or the occurrence of o between x and y or the last occurrence of " ) " . (1) Suppose u contains the first occurrence of "(", then it must contain also the last occurrence of " ) " , otherwise condition (1) of WB(u) would be violated. (2) The case with the last occurrence of " ) " is symmetric. (3) Suppose u contains o between x and y. Then u is not v, hence it contains an end segment of x or an initial segment of y. In the first case it must contain the first occurrence of "(" and in the second case it must contain the last occurrence of " ) " , since otherwise condition (2) of WB(u) 

would be violated. Hence again u = z and condition (g.2) is proved. Now we prove (g.3). Suppose Terτn(x). If x = v, then there is nothing to prove. If not, then x = (p o q) for some p,q such that SubWB(p 1x) and 

SubWB(q,x). To prove that p and q are terms, we have to check that each sub-well-bracketing y of p or of q has the required form. But each such y is also a sub-well-bracketing of x, hence by definition it must have this form. 

D314 V. Bounded Arithmetic 

Note that we can think of WB as a definition of arbitrary finite trees and Term as a definition of finite binary trees. The last property of terms that we prove is sometimes called unique readability. 

3.35 Lemma (/ΣΌ). 

Term(x) & Term(y) & Term(p) & Term(q) & (x o y) = (p o q) -> -> x = pky = q. Proof. Assume the antecedent is true. Then p and q are sub-well-bracketings of (x o y). It follows now from the proof of Lemma 3.34 that neither p nor q

can contain the occurrence of o between x and y. Hence the only possibility is that x = p and y = q. Ώ

Now we consider substitution. We have defined terms in a very restricted language; the following proposition holds for terms in the usual general sense. 

3.36 Proposition. The relations the term u is the result of substituting s for all (some, respectively,) occurrences of the variable v in t are ΣQ definable. 

Proof. We need to express that t is of the form     

> p1^y^P2^Ύ^...^ pn_i "-N v ^ pn,

where v does not occur (may occur, respectively) in pi,P2> >Pn> and u is of the form This can be done by introducing two 0-1 sequences w\, W2 such that w\ marks occurrences of v in t and tϋ2 marks occurrences of s in u (not necessarily all). Then we state that the word between the i-th and i + 1-st marked occurrence of v in t is equal to the word between the i-th and ί + 1-st marked occurrence of s in u. To express that an occurrence is the i-th one we use, of course, our function nuon. DSince the definition of substitution is quite straightforward, the usual properties are easily provable in IΣo and we shall not present them here. In IΣQ + Ω\ we can define the total ternary operation where t(v/s) stands for the result of substituting s for all occurrences of variable v. This is because we can bound the length of t(y/s): \t(γ/s)\ < const* \t\ * | s | . 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 315 

Since the bound is, essentially, the best possible and it is not linear, this function is not total in IΣQ. This causes some problems, when we develop metamathematics in IΣQ. For example, we cannot replace occurrences of a variable by a term in a proof. The purpose of this section is to study combinatorial concepts needed for formalization. It should be clear by now that these concepts are quite simple and can be handled in /i7o, unless they are functions growing more than polynomially. In the next section we prove a general theorem which covers some standard cases. Let us consider the concept of a proof as an example. Suppose we for-malize proofs as sequences of formulae. Then we need to write down that each element of the sequence is a formula which follows from the preceding ones by a rule. The relation that a rule defines on formulae, is usually con-structed from notions whose definability and properties have been shown in 

IΣQ (concatenation, substitution, occurrence etc.). On the other hand the provabiHty predicate which we obtain in this way does not have the basic closure properties in JΣΌ. This is because it is a Σ\ concept. 

## (h) Formalizations Based on Context-Free Grammars 

After working for some time in a formal system one gets a feeling, usually quite a clear one, of what can be formalized. Repeating the same tricks in formalizations again and again becomes boring. Then comes a dream: to prove a general theorem which would take care of all situations. Usually it remains only a dream, because if we want to state a comprehensible and memorable theorem, we have to give up a lot of its possible applications. We are going to state and prove a theorem which is such a compromise. We shall use the concept of a context-free grammar. A grammar is de-termined by two alphabets and rewriting rules. A rewriting rule is a pair of words (u yv). By an application of the rule (u,v) to a word w we mean the replacement of an occurrence of u in w by v. The rules can be applied in arbitrary order to arbitrary occurrences of subwords. One pf the alphabets consists of so called nonterminal symbols the other consists of terminal sym-bols. We are interested in the words which consist of terminal symbols only and which can be derived from a specified initial nonterminal symbol using rewriting rules. This is the language determined by the grammar. A context-free grammar is a grammar in which the first word of the rewriting rule is always a single symbol. In context-free grammars we can interpret nontermi-nal symbols as concepts (e.g. "noun", "verb" in natural languages, or "term", "procedure" in programming languages). The rules can be thought of as a kind of inductive clauses, which determine the structure of the words in the language. We know that it is important to have proofs of inductive clauses 316 V. Bounded Arithmetic 

in IΣQ. This is exactly what our theorem will do. Examples will be shown at the end of the section. Let us state a formal definition of context-free grammars and introduce the standard notation. A context-free grammar is a quadruple G = (TV, T, P, 5b), where N and T are finite sets, NΠT = 0, 5 0 G N, P C N x(NU T)+, where  

> +

denotes nonempty words in a given alphabet. (The standard definition also allows the derivation of empty words, but it would cause us some technical complications, therefore we consider only languages without empty words; the results that we shall prove do not depend on this restriction.) The elements of N (T respectively) are called nonterminal symbols (terminal symbols, 

respectively), So is the initial nonterminal symbol, P is a set of rewriting rules. Let u,w G (N U T ) + ; we shall write 

u =Φ- w, 

(or u =Φ w to indicate which grammar we are using), if there are A € N and 

v G (N U T ) + such that A occurs in u, (A, v) G P and w results from u by replacing an occurrence of A by υ. The relation =*• denotes the transitive closure of =>. Thus u =Φ> w means that u = w or u can be rewritten to w

by applications of the rules of the grammar. Note that the rewriting process is nondeterministic: we can choose rules and occurrences of letters. The set of all words w G T+ such that So => w is the language generated by C?. The languages generated by context-free grammars are called context-free languages. 

We shall add another unessential restriction that there is no rule of the form (A, B) G P with A, B G N. In order to simplify notation, we shall omit the sign for concatenation in the rest of this section. Our aim is to formalize the property of being derivable from A\ this is the meaning of ΨA( W) below. 

3.37 Theorem. Let G be a context-free grammar. Then one can construct a family of Σo formulae φj^ for A G N with the following property: If 

A =» WiiBi 1Wi 2Bi2 ... Bini ^ιw int , i = 1,..., k,are all the rules of G with A on the left side and tu,t, tu^,..., u>; n. G Γ*, ..., Sin. - i G N, then IΣo proves 

> k

(g.l) φA(x) =

(where we admit n t = 1). 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 317 

Proof. Let a context-free grammar G = (N, T,P,So) be given. We consider an auxiliary grammar G = (iV, T,P, 5o) denned by adding a new terminal A

for each nonterminal A E N of G and two new terminal symbols [,], and by replacing each rule of GA=> w 

by 

A 4> A[w] ,

(A[w] is the concatenation of A, [,iϋ and ].) The idea behind this is that G codes the syntactical trees of derivations in G. The words w E (N U T ) + which are derivable from some A in G can be defined by the following clauses: (1) it; is a well-bracketing with respect to [ and ]; (2) w is of the form A[u] for some A E N\ 

(3) each occurrence of [ is preceded by some A, for A E N] 

(4) if (g.2) is a sub-well-bracketing of u>, then (g.3) A => wiBxw 2 . . . wn-ιB n-iw n ,

> G

with wx,..., wn E T*, B i , . . . , B n _ i E iV. We know that such clauses are expressible by a ΣQ formula, so we have a ΣQ 

formula φ(x) which defines words derivable in G. Moreover the following is provable in IΣo: 

(5) φ(x) —> x is of the form (g.2) for some rule (g.3); 

(6) 

for each rule (g.3) of G. Condition (5) follows immediately from (1), (2) and (4); (6) can be proved in the same way as Lemma 3.34. Next we need the function which maps words of (N U T ) + on words of 

(N U T)* so that it only omits the letters which do not belong to N U T(* denotes the set of all words, including the empty word). A ΣQ definition of this function can be constructed using the same idea as we used for substitution. (In fact this function is the substitution of empty words for each A, A E N and for each bracket [ and ].) Let us denote this function by 

Forget(x). It is provable in IΣQ that Forget is a homomorphism of the free semigroup (N U T ) + into (N U T)*. In particular, it is provable in IΣo that:                   

> ( 7 ) Forget(A[wι&ι[v{\w 2. . . wn- l 2 l n - l [ υ n- i \ w n] )
> =υ>ιForget(Bi[υi\)w2 . . .Wn-ll

318 V. Bounded Arithmetic Recall that we do not allow rules of the form (A, B), for A,B € N. Thus in (g.3) either n > 3 or at least one W{ is nonempty. This together with (7) can be used to show in IΣQ that: (8) φ(x)^lh{x)<l*lh(Foτgtt{x)), 

which implies a polynomial bound to x in terms of Forget(x). 

Now we can define our formulae ψ^\ 

(9) φA(x) = (3y)(* = Forget(Ay)bφ(Ay)). 

Hence by (8) these formulae are Σo over IΣQ. The rest of the proof is easy. To prove (g.l), first suppose ΨA(X) in /ΣΌ Then, by (9), for some y and A, 

x = Forget(Ay) and φ(Ay). By (5), Ay is of the form (g.2). Hence by (7) 

x = w\y\W2 ... wn-ιy n-iw n ,Where y, = Forget(Bi[υi]) , i = 1,... ,n - 1. Thus, by definition (9), φBi{yi) f° Γ * = 1,... ,n — 1. To prove the converse implication, suppose that  

> X=

and for some rule (g.3). Applying (9) and (7) we get x = Forget(Ay), for Ay of the form (g.2). Then, by (6), we have also φ(Ay), thus ΨA( X) holds true. D 3.38 Corollary. A =Φ- w iff ^A(W ) is true. Hence context-free languages are in Σ$. Proof. By induction on the length of w. (Repeated application of (g.l) pro-duces a syntactical analysis of w.) Π

This corollary is only a by-product. The meaning of the theorem is that it not only produces a Σo formula, but also it gives inductive clauses which determine the concept in J ΓΣΌ in a, similar way as (c.1-2) determine exponen-tiation and (e.1-3) determine function nuon. 

As our first example, we consider the definition of numerals. We cannot use  

> ntimes

in IΣo, since the code of such an expression is exponential in n, thus IΣQ 

does not prove that 5 n ( 0 ) exists for every n. In IΣQ we use dyadic numerals 3. Exponentiation, Coding Sequences and Formalization of Syntax in IΣQ 319 

which are defined by 0 = 0 , _ ϊ = 5(0), 2n = (1 + 1 ) * (n), 2n + 1 = (T+1) * ( n ) + ϊ , f o r n > 0 . Using a context-free grammar G we first formalize positive numerals. G has one nonterminal SO, terminals T, +, *, (,) and rules 

So =* ϊ I (ϊ + ϊ) * (So) I (T + T) * (So) + ϊ , 

(this is the standard way of writing three rules at once). Let y?s o(a?) be the formula given by Theorem 3.37. Then IΣQ proves 

> φSo

(x) = x = T v (3y)(φ Sli (y) & * = ' ( ϊ + ϊ ) * (y)Ί 

where we use c . . . ' to denote a string of characters. Hence, if we define 

Num(x) = x = 0 V φs o(x)»then Num(x) satisfies natural clauses which determine this concept. The value val(x) of a numeral x is easily Σo definable, since the binary expansion of val(n) is encoded in n. Thus the function num(x), the a -th numeral, is also Σo definable, namely by 

num(x) = y = Num(y) & val(y) = x.In logic we usually reduce the definition of such a concept to terms and thus we do not have to use the full generality of Theorem 3.37. Therefore our second example will be the so called Polish notation, which is notation without brackets, thus we cannot reduce it directly to the concept of terms. Let us define variable-free formulae in the language consisting of 0, T -constants, add, mult - binary operations, = - a binary predicate, non -a unary connective, et, vel - binary connectives. The grammar will have two nonterminals 5o,5χ, the rules are 

So =*• = 5 i 5 i I nonSo 

# 5χ =» ϋ I T 

The meaning of So is "formula", the meaning of Si is "term". Theorem 3.37 gives us a Σo formula defining variable-free formulae such that the inductive clauses (given by the rewriting rules) are provable in We have developed several tools for defining syntactical concepts in IΣo 

Their application to the definition of terms and formulae in the full language of arithmetic, to the definition of proofs etc. is quite routine now, so we can end this section here. 320 V. Bounded Arithmetic 

# 4. Witnessing Functions 

# (a) Introduction 

Suppose a sound theory T proves a sentence (Vx)(3y)<^(a:,y). If T is weak and φ is simple, then we have some additional information on the functions which witness the existential quantifier in this sentence, i.e. functions / for which we have (Vx)φ(x,f(x)). A classical result says that if T is IΣ\ and φ

is bounded, then there is such an / which is primitive recursive, see Theorem IV.3.6. Parikh [Parikh 71] has noted that / is linear time computable if T is 

IΣQ and φ is bounded. Buss [Buss 86, Bounded Arith.] has defined a theory 52 (a conservative extension of IΣo + J2χ), fragments 5^ and subsets Σ% of bounded formulae in the extended language. His theorems characterize the classes of functions in the polynomial hierarchy using the above phenomenon. In particular, if φ is a Σ\ formula and T is S\> then / is polynomial time computable. The converse of this special case is also true: if / is polynomial-time computable, then there exists a Σ\ formula which defines / and for which it is provable in S\ that / is total. We start this section with the definitions of these classes of formulae and fragments of bounded arithmetic. The next step will be positive results about definability of functions of certain complexity in these fragments. It turns out that this is quite important information about the fragments. For instance, knowing that T^ defines functions of df + 1 , for i > 1, it is easy to prove Buss' theorem for T£. The main part is subsection (d) where witnessing theorems of Buss and of Krajίcek and Takeuti are proved. In subsection (e) we shall show a reduction of the problem of finite axiomatizability of bounded arithmetic to the problem of collapsing the polynomial time hierarchy. Since the fragments of bounded arithmetic have been extensively studied in [Buss 86, Bounded Arith.], we concentrate on results and proofs not included in that book. In particular, as Buss uses proof theory, we shall give proofs of the witnessing theorems based on model theory. We shall refer to Buss's book for basic facts provable in these fragments; however the readers with some training in bounded arithmetic, for example those who have worked through Sect. 3, should be able to make their own proofs without consulting that book. 

# (b) Fragments of Bounded Arithmetic 

We shall extend the usual language of arithmetic LQ by adding two unary function symbols \x\ and LZ/2J, and one binary operation x # y. The intended interpretation of |a;| is 4. Witnessing Functions 321 

\x\ = Γlog 2(x + l ) π = the length of the binary expansion of 

x if x > 0, otherwise 0, i.e. the same as in Sect. 3. Here ryn denotes the least integer z > y; ι_yj denotes the integer part of y, thus the interpretation of I_X/2J is clear. The intended interpretation of the smash function is 

x#y = 2' aj '*' ί/ ' = the power of 2 whose binary expansion has length |a?|*|y| + l . Observe that the set of the lengths of numbers in a sound arithmetical theory containing the smash function is closed under multiplication, hence under any polynomial increase (for standard polynomials). This is important, since it enables us to formalize many standard constructions, in particular polynomial time computations. We shall denote this extension of LQ by Li- In this section we shall work in the language Li and in an extension £2 of L2. Now we recall the basic system of open axioms for the extended language. It is called simply BASIC and it plays a similar role to Q in the usual language. 

4.1 Definition. BASIC is the following theory: (1) y<χ-*y<Sχ\ 

(2) xφSx; 

(3) 0<s; 

(4) x<ykx_φy = Sx<y; 

(5) x ^ 0 - ^ 2 x ^ 0 ;  

> (6) y<χVχ<y\

(7) x <ySzy <χ —> x = y; (8) x <y&εy < z —> x < z\ 

(9) |0|=U; (10) x φ U-> 12*1 = S{\x\) &|5(2*)| = S(\x\); 

(11) |1| = 1; 

## (13) ]«#y| = 5(|*| •Ivl); 

(14)0#y = l; (15) x φ 0 -» 1 # (2x) = 2(1 # x) & 1 # (5(2*)) = 2(1 # x); 

(19)x<x y; (20)x<ykx φy-> S(2x) < 2y&S(2x) φ 2y; 

(21) x + y = y + x; 

(22) x + 0 = x; 

(23) x + Sy = S(x + y); 322 V. Bounded Arithmetic 

(25) x + y<jc + z = y<z\ 

(26) x * 0 = 0; (27) x * (Sy) = xy + x\ 

(28) xy = yz; (29) x(y + z) = xy + xz\ 

(30) x>l-+(xy <xz = y<z);        

> (32) y = L Z / 2 J = (2y = z V 5(2y) =s),

where T and 2 are numerals as defined in Sect. 3. This system is probably not quite optimal. One can play with it in order to find a shorter or nicer system. For instance, if we redefine 

\x\ = Γ log 2 (z + I)" 1 - 1 if x > 0, 0 otherwise, then x#y = 21*1*101 becomes associative and distributive with respect to multiplication, hence one would obtain a more homogeneous axiomatic sys-tem for such functions. We shall not do it here, as we want to concentrate on more interesting questions. We shall use the bounded quantifiers (Va; < r) and (3x < r ) ; note that r is a term in the language L2, not just in LQ (not containing rr, of course). Moreover we also need the so-called sharply bounded quantifiers. They have the form i.e. the outermost function in the bounding term is the length function. Their relation to ordinary bounded quantifiers in bounded arithmetic is similar to the relation of bounded quantifiers to unbounded quantifiers in PA. The classes Σ\ and Σtf of bounded formulae are defined as follows. 

4.2 Definition. 

(1) ΠQ = ΣQ consist of formulae with sharply bounded quantifiers only; (2) Σ\ +1 and i7^ + 1 are the least sets satisfying 

# (a) ΣlπfCΣf^ and 2* Π^CΠ^ 

(b) α € Σ * + 1 =» (3x < τ)a € Σ * + 1 , (V* < |τ|)α-G *

a E Π b^χ =• (V* < τ)a e 7Tf +1 , (3* < |r|)α 6 (c) a , β € l ή + 1 = ϊ ξ

# a,β G ilf +1 ^ f+1 

(d) a € Σ * + 1 , ,9 G 27? +1 =>-,β, β-+ a4. Witnessing Functions 323 

(3) a is in Δ\ with respect to a theory T, if a is equivalent to a Σ\ formula and a Π* formula in T. (4) ΣQ(Σ%) is defined as the closure of Σ\ under connectives and sharply bounded quantification; note that this class is sometimes denoted also Later on we shall see that, for ϊ > 1, Σ\ (resp. Πf) formulae define just the sets in Σf (resp. Πf). The most important formalizatipns of induction for bounded formulae are the usual schema of induction and the following ones. 

4.3 Definition. 

(1) PIND(a(x)) is the formula α(0)&(Va:)(α(La:/2j) -> a(x)). -> (Vx)α(s); (2) LIND{a(x)) is the formula α(0)&(Vy < \x\)(a(y) -+ α(5(y))). -+ a(\x\); 

(3) LMIN(a(x)) is the formula (3s)α(*) -> α(0) V (3*)(α (4) P/ΛΓDΓ {LINDΓ, LMINΓ, respectively) is the schema (or the set) 

PIND(a(x)) (LIND(a(x)\ LMIN(a(x)), respectively) for a(x) € Γ. Here we assume that a(x) may contain other free variables, which are called parameters. We have written LIND in the form which contains only one additional quantifier and this quantifier is sharply bounded. Thus if a is 

Δ\, then LIND(a(x)) is also Δ\\ if a(x) is in Πξ U Σ\, then LIND(a(x)) is 

# 4# 

Now we are ready to define the hierarchy of subtheories of bounded arith-metic. 

4.4 Definition. 

(1) For t > 0, S | is BASIC + PINDΣf. 

(2) For i > 0, Γj is BASIC + IΣ%. 

(3) 5 2 i s U i S έ ; Γ 2 i s U , Γ 2<.The most important fragment of 52 is 5^. It serves as a basic theory modulo which results on fragments of 52 are proved. Its role is similar to 324 V. Bounded Arithmetic 

the role of IΣ\ in PA. In particular we shall show in the next subsection that all polynomial time computable functions are definable and provably total in S\. As for weaker fragments: 5° is too weak (it does not prove the existence of the predecessor, see [Takeuti, Sharply Bounded]); the strength of 

T% is not quite known. We shall not repeat the formalization of elementary mathematical concepts in 5^ which has been done in [Buss 86, Bounded Arith.]. One can use some techniques from Sect. 3, mainly those which were mentioned in connection with IΣQ + Ω\. (Those which reduced the size of the quantified numbers by using more quantifiers are useless for S^ since we need Σ\ definitions.) Here we briefly mention a definition of coding in S\. 

First we re-define Pow(x) (x is a power of 2) by an open formula in L*i\ 

In order to see that this works, we shall show in BASIC that Pow satisfies the following recursive condition: 

Pow(x) -> (x = ϊ V (By < x)(x = 2y & Pow(y))) .One can easily show -ιPow(O). Suppose x > 1. Then, by axiom (32) of 

BASIC, x = 2y or x = S(2y), for y = LZ/2J and y > 0. By the definition of Pow and (15), we have 2x = x # ϊ = 2(y # ϊ ) , hence (by (1), (6), (7) and (30)) we have x = y # 1. Since y > 0, we get from (15) that x is even. Hence we must have the first possibility x = 2y (BASIC proves that S(2u) φ 2v). 

Thus 2y = x = y # 1 , i.e. Pow(y). 

Now we can re-define bit(x,i) (the i-ih digit of x) by a Σ\ formula:          

> bit(x, i) = z = z < l k (3y, u2< x)(3uχ < y)(Pow(y) &\y\ =i

&x = 2u2y + zy + t*i), if i > 0, = 0 otherwise. Since the decomposition above is unique (see Theorem 1.1.30), we have also a Π\ definition: 

bit(x,i) = z = (Vu> < l)(Vy,tι 2 < *)(Vtii < v)(Pow(y)b\y\ = i

& x = 2u<ιy + wy + uι —>w = z), if i > 0 ,= 0 otherwise. Thus we have a Δ\ definition of bit in S£. Similarly we can define function 

sgm, (see 3.18). The function bit codes 0-1 sequences. If we want to code arbitrary sequences, we can proceed as follows. A sequence will be a triple 

p = (tz,υ,to) (more precisely ((tί,υ),ιo), thus every number is a sequence), 4. Witnessing Functions 325 

where u is the code of the sequence, v is its maximal element and w is the  

> length of the sequence, i.e.

max(p) = v,

lh(p) = w. 

The function the i-th element of p is defined by 

(p)i = s = a: < υ&(Vj < \v\)(bit(xj) = bit(u,iv + j)), if i < w ,(p) a = 0 otherwise. Hence all these functions are Δ\ . Finally we observe that we can bound u by 

\u\ < \υ\.w .Thus for some term bound we have (a.l) p < bound(max(p), 

4.5 Proposition. (1) For i >l,S ι2=Sl + PINDΠf = 5^ + LINDΣ\ = 5^ + LINDΠf. 

(2) Fbr i > 1, 25 = S$ tf 

Proof We shall show only S£ = ^2 + ί ^ ^ ^ i ^ e proofs of the remaining equivalences are the same as for fragments of PA, see Theorem 1.2.4. First we shall derive LINDΣ% in 5^. Let ^(a?) be Γf. Let ψ(x) be y>(|x|). Then by (10) and (32) of BASIC, the inductive clause of LIND(φ(x)) φ(x) 

implies the inductive clause of PIND(φ(x)) 

Thus LINDΣ\ is reduced to PINDΣ\. 

Now we shall derive PINDΣ 1? in 5^ + LINDΣξ. Let y>(z) be_a Σ* formula for which we want to prove PIND. Thus we assume ψ(0) and  

> (VX)(Ψ(LX/2J)

—> ¥>(#)). Let msp(x,y) be the number whose binary rep-resentation consists of the first y digits of x (and, say, it is x if y > \x\). This function has a 2^ definition in 5^ (use the function &gm). The idea of the proof is to show, using LIND, that all end segments of x satisfy φ, hence also x itself satisfies φ. Formally, we apply LIND to φ(msp(x, y)) with y as the induction variable and a: as a parameter. Thus PIND(φ(x)) is reduced to 326 V. Bounded Arithmetic 

LIND(φ(msp(x,y))) since msp(x,0) = 0, L.msp(x> 5(y))/2j = msp{x,y) and 

msp(x, \x\) = x. Π

4.6 Theorem. For i > 1, S%2 h 

> PTΌO/.

Recall the meaning of 1 ^ : for every α G 17* and β € JT^ The idea of the proof is the following. The schema of induction tells us that we cannot define a proper subset of numbers which contains 0 and is closed under the successor. The schema PIND implies that there is no subset of numbers containing 0 and closed under the successor and the function 2x. We already know (Theorem II.3.5) that for every cut we can define a subcut closed under addition, hence also closed under 2x. We shall use this construction to reduce induction to PIND. There is a small technical complication, since we have to use only bounded formulae, while the original construction uses unbounded quantifiers. Let a and β be given. Put 

>a) =df (Vx < a)(a(x) -> /?(min(z + y, a))) .Thus φ is Π\. Working in £J, assume a(x) = β(x), α(0) and (Wx)(a(x) -> 

a(S(x))). Furthermore assume that α(α) fails for some α. We have ψ(0>a) 

trivially and ψ(y,a) -+ ψ(S(y),a), since (Vx)(a(x) -• a(S(x))). We shall prove ψ(y y a) -* ψ(2y, a). Assume φ(y, a) and α(x) for some x < α. By φ(y, a) 

we have α(min(x + y><*)). Thus x + y < α, since - α(α). Hence a(x + y,ά). 

Applying φ(y, a) once again (with x+y instead of x) we get α(min(x+2y, α)). Hence we have φ{y<,a) -+ φ(2y,a). Since     

> x= 2LS/2J V I =S(2LX/2J) ,

the formula , α) -• ψ(S(y), a) & V(2y, a)) 

implies Hence using PIND(φ) we get ^(α, α). Since α(0), this implies α(α). We have derived a(a) from its negation, hence it must be true. Thus we have shown induction for α. ΠNote that, for i > 2, a weaker version of this theorem can be derived also from Corollary 4.28 below using the Σ"j\ χ conservativity of 5 ί + 1 over 32 (Corollary 4.34). 4. Witnessing Functions 327 

## 4.7 Theorem. 

## (1) Fori>0, 5£CTJC5£ f l ;

(2) 52 = T*ι and they are conservative extensions of IΣo + Ω\. Proof. (1) To prove the first inclusion, observe that TJj trivially proves 

LINDΣ\ and apply Theorem 4.5(1). The second inclusion is a corollary of Theorem 4.6. (2) The equivalence of theories 52 and T2 follows from (1) of the preceding proposition. In order to show that IΣo+Ω\ is contained in 52 we have only to prove axiom Ω\ in 52, which follows easily from the bound ω2{x) < (x # a;) 4.Let us prove the conservativity of 52 over IΣQ + Ω\ . We already know that  

> LZ/2J

and \x\ are definable in IΣo + Ω\. As we have a Σo definition of the exponentiation relation, we can define the graph of the function x#y. This function is provably total in IΣo+Ω\ , because of the bound x # y < ωiixΛ-y)* 

The axioms of BASIC are easy too. To prove induction for bounded formulae in language L2 in IΣo + β i , recall that by Proposition 1.3 we can eliminate terms as bounds in the formulae used in induction. Then we use the definitions of the new operations to translate the formulae into the language Lo and apply IΣo* Π

4.8 Theorem, (a) For i > 1, and a(u,x) G

Sι2 h (3uO(Vs < |y|)(α(tι, x) = bit(w, x + T) = T). (b) For i > 1, S$ h LIND(Σ%(Σξ)). 

Note that (a) is a version of the ΣQ(Σ^) comprehension schema in where we use bit(w,x) as a convenient coding of 0-1 sequences. 

Proof, (a) Consider a more general schema for a € ΣQ(Σ^): 

(b.l) Sι2 h (3tι;)(V*i < \tn I).. .(Vx n < |yn|)(α(u, xU...,x n

We should show that (b.l) holds for a G Σ\ and that the set of formulae 

a satisfying (b.l) is closed under boolean operations and sharply bounded quantifications. Suppose α G Σ\. Take the formula β(z,u) defined by (3tι>)(M < |yi| * I2/2I * * \Vn\ & nuon(w) = z 

.(V* n < \yn\)(Ut(w,Ί+(χ u(χ 2,...,χn))) = T - * 328 V. Bounded Arithmetic 

Let us work in S£. This formula is true for z = 0 and fails for z = |yi| * \y<ι\ *• * \yn\ + lj since nuon{w) < \w\. Since a is i?^, nuon is ZiJ and we can bound w> say by y\ # 2/2 # . . . # y n, the formula /? is also Σ"f. Hence we can use LINDΠf to find the smallest z for which β{z, u) fails. Then take w such that β(z-l,w). If * - i = |yil*lifel* *|ynl, then all bits of w are 1, hence we have (b.l) for this w. Now suppose that If (b.l) were not true for this w, then we could add another 1 in the binary representation of w which codes an instance of α(u, x\, a?2> »χn)- But this would contradict the condition that z — 1 is the last parameter for which 

β(z — l,tϋ) is true. Hence w codes exactly the set determined by α. The case of propositional connectives and sharply bounded quantifiers is easy. (b) follows immediately from (a). DIn Bounded Arithmetic there is a counterpart of the collection axiom for Peano Arithmetic, see 1.2.1. We shall call it the bounded collection axiom. 

Sometimes it is also called replacement axiom. 

4.9 Definition, (i) BB(a(x,y)) bounded collection is the following formula (Vx < |*|)(3y < J)α(x,y). - (3w)(Wx < \t\)((w) x < ska(x,(w) x)). 

(ii) BBΓ is the schema BB(a) for a £ Γ. Using (a.l) above, we can bound the variable w in the bounded collection axiom; thus it has the following form (equivalent in ^(V*<|t|)(3y <*)«(*, y).-> 

< \t\)((w) x <

where r is a suitable term (τ(s,t) = bound(s 

4.10 Theorem. For i > 1, Sj h BBΣ\. Proof. Let &{x,y) be a Σ\ formula. Assume Then we obtain 

(3w < τ(s,t))(Vx <4. Witnessing Functions 329 

by 

LΠfD(βw < r( where the induction variable is z. The formula is 27^, since coding is Δ^. We use the elementary facts that the empty sequence has a code, each sequence can be extended by an arbitrary element and the estimate of the size of a sequence. DNote that the implication converse to that above is already provable in 5^ (using only the fact that (w) x is a definable function in S^)- The bounded form of the bounded collection axiom enables us to interchange sharply bounded quantifiers with bounded quantifiers. However we cannot push inside all sharply bounded quantifiers without extending the language, since the coding function is not defined by a term in Li. Therefore we need to extend the language. 

4.11 Definition, (i) The language Li augmented with the binary operation 

(x)z> will be denoted by Li\ the corresponding classes Σ^Πf etc. will be denoted by Σ$,2Γ*, etc. (ii) We say that a formula is strictΣ\ if it is of the form < *2) - - (Q*i < U)ψ ,where Q is 3 if i is odd and V if i is even, and φ is sharply bounded. We shall not introduce new notation for theories obtained by extending the language and adding the definition of the coding relation. It will always be clear from the context which theory we mean. 

4.12 Corollary. For i > 1, every Σ\ formula is equivalent to a strict Σ\ 

formula, provably in S\ (augmented with the definition of (x) 2). Proof. We can shift all sharply bounded quantifiers beyond bounded (but not sharply) quantifiers using the bounded collection schema. Successive quantifiers of the same kind can be merged using the coding function. D

4.13 Corollary. For i > 1 and α(z,y) in Σ^ 

Si h (ΞuOOte < |*|)[(3y < s)a(x,y) = ((w) x <sba(x,(w) x))] .

(This is sometimes called strong replacement.) Proof. Let a(x, y) in Σ\ be given. By Theorem 4.8, we can code the set of a 's such that (3y < s)a(x,y) using some υ and formula bit(v,x) = 1. Now take α'(x, y) to be α(x,y) V bit(υ,x) = 0. 330 V. Bounded Arithmetic 

Then we have (Vx < \t\)(3y < s)a'(x,y), hence we can apply bounded col-lection; the sequence w given by it satisfies the clause of the theorem. D

## (c) Definability of Turing Machine Computations in Fragments of Bounded Arithmetic 

Recall that for i > 1, D? denotes the set of functions computable in polyno-mial time using oracles for Σ?_^ sets; in particular, D^ are just the polynomial time computable functions, since ΣQ oracles are superfluous. In this subsec-tion we shall show that functions from Dξ have suitable definitions in 5^, and the same holds for D? and T^"" 1, if i > 1. This means that for functions from D? we have ZiJ +1 definitions in the corresponding theories and that basic properties of the functions are provable in these theories. We shall only show that the defining formulae have appropriate complexity and that they de-fine total functions. Other properties follow from the construction and their proofs are omitted. We shall consider deterministic Turing machines, possibly with oracles. Let an oracle Turing machine M be given, let e be the code of it, let A be an oracle. We formalize the computation of M on input a as two sequences 

w and q, where (tϋ) t is the instantaneous description of the state of M, the position of the heads and the content of the tapes, and (<j), is the query asked in step i. 1 The computation is determined by a constant firstq (let us set it equal to 0) and five functions firstw, nexiwQ, nextwi, nextq^, nextqi as follows: 

(w) 0 = firstw(a), (q) 0 = firstq 

(w)i+l = nexiwQ((w% ($),-), (q) i+1 = nextq o((w) iy (q)i\ if (?)* ϊ A

(w)t+l = nexiwι((w)i, (ςf) t ), (q)i+i = nextq x{{w) u (ςr) t ), if (q)i € A.We can think of (w){ as a sequence which encodes the current situation on the tapes and encodes the state of M. Then the functions above are only local transformations of these sequences; hence it is not difficult to write down 

Δ\ definitions for them using our Δ\ definition of coding. If the oracle A is defined by a formula φ{x), we thus get a formula expressing that (w,q) is a computation of M on input α. If M is a machine without an oracle, we shall write simply Comp M(w, a). We shall assume that    

> W.l.o.g. we can assume that Masks a query in each computation step; if it does not need information it asks some default fixed query. 4. Witnessing Functions 331

(w){ = (tu)t+i iff M stops in the i-th step. Thus computations of length n

exist for every n, and we have a simple condition for testing the termination. Furthermore we shall assume that this (w){ is the output of M. We shall identify oracles with their defining formulae; thus we shall talk about Σ\    

> oracles instead of Σf oracles .
> 4.14 Lemma.

(i) CompM(w,a) is Δ\ in 5^. (ii) If φ(x) is Σ\, i > 1, then Comp M^φ{x) (w,q,ά) is 27§(2#). (iii) There exists a term σ such that        

> S\ hCorny MiΨ (x)( w><1, a)-* W-><1 < σ(α, lh(w)) .

Proof, (i) and (ii). We have 

CompM(w,a) = (w)o = firstw(a) & (Vi < /Λ(w ) and 

^(w,q,a) = (u )o = firstw(a)k(Vί < lh(w) - 1) We already know that all the functions used in these formulae are Δ\ defin-able. (iii) The length of w and q is polynomial in the number of steps of the computation and the length of input, whence we get the bound. DNow we prove the relation between the classes of formulae Σ% and the classes of sets Σ? which we have promised. Note, however, that the relation is not quite direct for i = 0. 

4.15 Theorem. 

(i) Every set definable by a ΣQ formula is in LogSpace. 

(ii) Every set in P is definable by a Δ\ formula. (iii) For i > 1, the sets in Σf (resp. Πf) are just the sets definable by Σ\ 

(resp. Π\) formulae. ("Definable" means here "definable in the standard model".) 

Proof (i) All the functions and predicates of the language of 52 are LogSpace 

computable and sharply bounded quantification preserves LogSpace compu-tations. 332 V. Bounded Arithmetic 

(ii) Let X be in P. Let M be a Turing machine which always stops after 

p(\a\) steps on input a and outputs 0 iff a belongs to X. Then we can define X b y 

(3w)(lh(w) < p(\a\) & Comp M(w, a) & (w)p(|α|) = ° ) ' or by (VtιO(7Λ(tιO < p(|α|) & Comp M(w, a) -> (uθ p(|«|) = 0). By Lemma 4.14, the inner parts of the formulae are Δ\; by the same lemma the bound lh(w) < p(\a\) implies that w can be bounded by a term in α, hence the formulae are equivalent to Σ\ and ϋ\ formulae respectively, thus they are Δ\ .(iii) By Corollary 4.12 every Σ\ formula is equivalent to a strict Σ\ formula in the language extended by the coding relation; thus it can be written in the form where Φ is sharply bounded in the extended language and where Q is 3 if i

is odd and V if i is even. Since the coding relation also belongs to P, formula 

Φ defines a predicate in P. The bounds are just of the order needed for the definition of Σf and the relations yj < tj are in P as well. Thus, by Theorem 2.11, each set definable by a Σ\ formula is in Σf. 

To prove the converse let X be in Σf. Thus X is defined by where P is in P. By (ii) we can define P by a Δ\ formula. Similarly to above we can replace the bounds \yj\ < Pj(\x\) by bounds of the form yj < tj for suitable terms ί i , . . . , t{. Thus we obtain a Σ% formula defining X. D

4.16 Theorem. (1) Let M be a Turing machine. Then 5^ proves that for every input a and every 6, there exists a unique computation of M which has |6| steps. Formally: (i) S\ \- (3w)( Comp M(w, a) & lh(w) = \b\) 

(ii) S£ H CompM(w, a) & Compj if(w',a) klh(w),lh(w') = \b\ -» w = w'. 

(2) Let i > 1, let M be an oracle Turing machine and let φ(x) be in I7J\ Then T% proves that for every input a and every b, there exists a unique computation of M with oracle ψ(x) which has |δ| steps. Formally: (i) 23 h (3w, q)( Comp M>φ{x) (w, q, a) & lh(w) = \b\) 

(ii) 23 h Comp MiV (x) (w, q, a) & Comp Mφ{x) (w', q', α) 4. Witnessing Functions 333 

Proof. Let M and φ be given, φ in Σ\. Let ψ be defined by 

φ(w, q, α, b) = ZA(u ) = |6| + 1 & (w) 0 = firstw(a) & (g) 0 = ./irrfg & (V; < |δ|) = nexiq o((w)j,(q)j)) 

The meaning of the formula is that 10,(7 is like a computation in which we follow the advice of the oracle if its answer is negative, but not always do we follow it if its answer is positive. This formula is Δ^ if i = 0, and Σ^ if 

i > 0. Hence we can prove, using respectively LINDΣ\ or LINDΣ\ on 6, that for given α, b there exists at least one pair it;, q such that φ(w, q, α, b). Using 

IΣ\ we now minimize the number of steps where w and q do not follow the positive advice. Let Φ be the Σ\ formula defined by #(tι, α, 6) = (3u>, q < σ(α, |δ|))(V>K 5, α, 6) & (Vj < |6|) where σ is the term from Lemma 4.14 (iii). For a and b there exists at least one u satisfying Φ(u,a, 6), since for w,q satisfying ψ(w,q,a,b) the existence of u follows by LINDΔ\. By IΣf we have the least u for which Φ(u,a,b) 

holds (this is the place where we use the full strength of T). Let w, q be the witnesses of !?(ι/,α, 6) for this u. We shall show that for this w,q also the implication complementary to the one in ψ holds for all j < \b\: 

Suppose not, then we have φ((q)j) and (ly^ +l = nexiwo((w) j,(q)j)&(q)j+ 1 = nextq o((w)j,(q)j) ,for some j < |6|. Hence δit(iί, |6| — j) = 1. Take «/ and ^ 7 of length |6| such that for fc = 0 , . . . , j , and 334 V. Bounded Arithmetic 

for k = j + 1,..., |b| - 2. The existence of such w1 and q1 is again easily provable by LINDΣ\. Let υ! be determined by 

bit(u\ k) = 1, for fc = 1,..., |δ| - j - 1, 

bii(u', k) = K*(u, fc), for k = |6| - j + 1,..., |6|. Then we have !P(i/,a, 6), since υ! corresponds to w',q\ but υ! < u, which is a contradiction. Thus we have shown 

> i

φ){w, q, a) & lh(w) = |6|. To prove uniqueness we apply LINDΔ\ to (V? < |i|)((«oj = (w')j & (q)j = (g')i) 

4.17 Theorem. Dξ functions are definable by formulae which are Λ\ in S\\ 

for i > 0, O^ +1 functions are definable by formulae which are / ^ + 1 in Tg. Furthermore, for each such formula the corresponding theory proves that the formula defines a total function. 

Proof. Let i > 1. Let / be a D? + 1 function defined by an oracle machine M

and a Σf oracle A. By Theorem 4.15, A can be defined by a Σ\ formula φ{x). 

Let p(x) be a polynomial time bound for M. Then (similarly as in Theorem 4.15) f(a) = 6 can be defined by   

> f¥

( ) ) p ( | β | ) = 6), or by where σ is the term from Lemma 4.14. Using the same lemma to estimate the complexity of CompM tφ(x) a n < i ^ e existence and uniqueness of the com-putation (Theorem 4.16) we see that it is a ^ + 1 definition in T-j. For i = 0 the proof is similar. The fact that the formulae define total functions in the corresponding theories follows from Theorem 4.16. DIn order to be able to use the definitions of functions for other construc-tions in T, we need more properties of formulae defining the functions. In particular, we shall use the following properties: 4. Witnessing Functions 335 

(1) if t(x) is a term and φ is the definition of the corresponding Dξ function, then t(x) = y is equivalent to φ(x,y) in S\\ 

(2) D? functions are provably closed under composition, i.e. if y?(x, y) de-fines /(x) and φi(x,y) define # t (x), then for some definition χ(x,y) of X), , ffn(x)) Tj (resp. S£, if t = 1) proves (3) D? functions are closed under definitions by cases determined by Σ\_^ 

formulae (it is clear what is the corresponding formula); (4) P? functions are closed under bounded recursion. The last condition can be formalized as follows. Let /(x), g(z, x), i(y, x) be functions in D?; then the function Λ(y,x) defined by the following recursion must also belong to D?: Λ(0,x) = / ( x ) , ft(y, x) = min(y(Λ( Ly/2j, x), x),fc(y,x)). We require that this schema be provable in T% (resp. S\, if i = 1) for the defining formulae of f,g and h. To prove these conditions one has only to check that the proofs in the standard model can be carried out in the fragments of Bounded Arithmetic. We omit the proofs since they are not difficult and contain no essentially new ideas. So far we are able to talk about a single function form some class D?. Later we shall need formalization of Turing machine computations such that we can talk about Turing machines and oracles in the theory, i.e. we want a formula defining the computation which has parameters also for Turing machines and oracles. In the model theoretical language it means that we want to consider also nonstandard Turing machines and oracles. A simple solution is to take a universal Turing machine, which is explicitly defined and thus has a formalization in S^ by Theorem 4.17. Then the code of an arbitrary Turing machine will be the word which must be written on the input of the universal one in order to simulate it. A natural universal Turing machine simulates each machine M in such a way that the running time is at most polynomially longer than the running time of M. More precisely, the simulation time is bounded by a polynomial in the original running time and the size of M. In particular, if M runs in polynomial time so does the simulation of M.This was about Turing machines. Oracles can be presented in a similar fashion. Using a universal Turing machine we can represent every predicate 

P(x) in P in the form μo(e,x,t e (s)) for some fixed Δ\ formula μo Here e is the code (the index) of P and te is a suitable term determined by the running time of a Turing machine for P. This is still not quite what we need, since the dependence of te on e is not explicit. Thus we shall make an additional natural assumption that the predicate with code e is decidable in time n e .336 V. Bounded Arithmetic 

Then our representation of predicates in P will be of the form Note that for e standard the existence of 2' x' is provable in S\- For the representation of predicates in Σ^ we have only to add quantifiers. Also there is no need to use two indices, one for the machine and one for the oracle. We shall present our conclusions as a theorem. 

4.18 Theorem. There are formulae μo^O € &\, N € Σ\, Ui £ Σ^(Σ^) for 

i > 1, such that (i) each predicate which is in P, provably in 5^, can be represented in 5^ as μo(e, x, 2' ίC ' ), for some numeral e"; (ii) for i > 1 and for every φ(x) G Σf, there exists an e such that (iii) for every function / which is polynomial time computable, provably in 

S^, the relation f(x) = y can be represented in 5^ by ^θ(e, X) y, 2' ίB ' ) , for some numeral e (iv) for i > 1 and for every function / which is in Πf +1 , provably in T^, the relation f(x) = y can be represented in T-J by z/i(e, x, y, 2'*' ), for some numeral e.Let us state (i) more precisely. A predicate P in P is determined by a 0-1 polynomial time computable function /. For this function we have a defining formula φ(x,y) which is Δ* and satisfies some basic conditions in Sj. Thus 

P(x) is defined by φ(x, 0). The precise statement of (i) is that for some number e The statement (iii) should be understood in the same way. In order to simplify notation we shall define We should keep in mind that it is not a bounded formula. However, if we prove the existence of 2'*'*, then we can work with it as if it were a Δhi+1 

formula. 4. Witnessing Functions 337 

## (d) Witnessing Functions 

In this subsection we shall develop the model theory of fragments of 52 and prove some theorems of the type mentioned at the beginning of this section. We shall use the fact proved above that Turing machine computations are definable in fragments of S2. First we shall show that a substructure of a model M of T\ that is closed under the functions of D?, ^ is Σ^ elementary in M and is a model of T^. The same holds for substructures of models of 5^ and the functions of Dξ. This is applied to prove witnessing Theorems 4.27 and 4.29 forfragmentsT^. Then we prove a witnessing Theorem 4.32 for fragments 5£*~ . The theorem has a stronger conclusion than in the original form used by Buss; it states that (yx)φ(x y f(x)) is provable in the weaker theory T£, if i > 0. This allows us to prove immediately the well-known conservation result for such pairs of theories. As the model-theoretical proof of Theorem 4.27 is rather difficult, we first prove an auxiliary Theorem 4.31 about extensions of models of S^" 1.

4.19 Definition. Let M be a structure for the language of 52, let A C M, 

i > 0. Assume that each {e} t (a;) defines a function in Λf. The D? closure of A is the set 

{{e}i(a)\aeAke€N}. 

We say that A is D? closed if A is its own closure. We want to use the fact that polynomial time predicates are absolute in every D^ closed substructure of Λf, a model of 5^. As we do not have symbols for all polynomial time predicates in our language, we have to formalize this statement. Before the next definition let us note that every formula can be transformed to an equivalent formula which has only &, V and -1 as connectives, and all negations occur only at atomic formulae. What is important is that this transformation preserves the quantifier complexity. We shall say that such a formula is in negation normal form. 

4.20 Definition. Let i > 0, let T be 5^ if i = 0 and T\ otherwise. For a formula 

φ in negation normal form and a model M t= T, we define inductively that φhas D?, j Skolem functions in M: 

(1) every open formula has Πf +1 Skolem functions in M

(2) if φ and φ have Πf +1 Skolem functions in M, then Vxφ, φ&εψ and φ V φ

have Πf +1 Skolem functions in M

(3) if φ(x, y) has Πf +1 Skolem functions in M, then (3y)y?(x, y) has Πf +1 

Skolem functions in Λf, if for some / in Πf +1 

M 1= (Vx)((3j/Mx, y) ^ Ψ(x, /(x))). Here /(x) is represented by {e} t ((xi, (x2, ..., xn) •))> where e G N and 338 V. Bounded Arithmetic 

4.21 Lemma. Let T be as above, let M 1= T, let K C M be D? +χ closed, and let φ(x) have Πf +1 Skolem functions in M. Then for a € A", 

Proof. By induction on the complexity of <^. D

4.22 Corollary. If φ(x) and -><p(x) have D? +2 Skolem functions in M N T, T as above, then <p(x) is absolute for Πf +1 closed substructures of M, i.e. if A

is a Πf 11 closed substructure of M and a is a string of elements of A then 

M\=φ(a) iff AN<^(a). The natural definitions of polynomial time computable predicates have Dξ Skolem functions in M. In particular we shall need that the formula x = (y) z

and its negation have D^ Skolem functions in M. Now let P{x) be an arbitrary polynomial time computable predicate. Then it can be defined by (d.l) (3w)(\w\ < P(\x\)kComp(w,x)k(w) p{]xl) = 1). It is clear that w and the existentially quantified numbers in Comp can be computed in polynomial time, thus (d.l) has Dξ Skolem functions in M. 

The same is true for the negation of (d.l), hence (d.l) is absolute. Thus in our formalization, polynomial time predicates are absolute in the situa-tion considered above. The same argument works, of course, for polynomial time computable functions. This enables us to work with polynomial time computable predicates as if they were present in the language. 

4.23 Lemma. Let M be a model of 5^, let if be a D^ closed substructure. Then 

K t= LIND-strictΣ] => K N S | . 

Proof. First we shall show using LIND for strictΣ\ formulae that in K every 

Σ\ formula is equivalent to a strictΣ\ one. Thus we will have LINDΣ\ in K. 

This is proved by induction on the number of quantifiers. Several quantifiers of the same kind are replaced by a single one using the coding relation. A sharply bounded universal quantifier is exchanged with the next existential bounded quantifier using an instance of BBΣ\, for which LIND-strictΣ\ is sufficient (see the proof of Theorem 4.10). We must check that the properties of the coding function that we are using are provable already in LIND- strict Σl\. We need the following properties: 4. Witnessing Functions 339 

(1) (Vxo Xj)(3y)({y)o = *o & & (y)j = Xj), for every j

(2) (3s)(lh(s)=0); 

(3) (Vx  

> 1S

the I* 8* element of the sequence t). Again it is clear that these formulae have D^ Skolem functions in M. Since they are true in M they are true also in K by Lemma 4.22. Similarly we shall show that LINDΣ\ implies PINDΣ\ in K. We repeat the proof of 

S% + LINDΣf h PINDΣ hi,(Proposition 4.5 (1)) where we needed from S\ only the following properties of the function msp: S(b) < \α\ -> Lraap(α,5(6))/2J = msp(α,b); msp(α J\α\) = α. 

These formulae are true in M and have D^ Skolem functions, hence they are true in K too. D4.24 Lemma. Let i > 0, let T be S£ if i = 0 and TJ otherwise. Then each 

} ) formula has D^, ^ Skolem functions in each M 1= T. Proof. We shall use induction on the depth of the formula. For open formulae the lemma is true by definition. Consider a Σ\ formula of the form where we assume that <^(a, x) has Π£j_i Skolem functions. We apply binary starch using Σ\ oracle 

(3x)(p<x<qkφ(*,x)) 

to find an x satisfying x < t(a) &y?(a;,a), for a given a. At the beginning we set p : = 0 and q : = *(a). First we ask whether (3x < t(a))y>(a, x). If it is not true, then the output is, say, 0. Otherwise we continue as follows. In each subsequent step we set either p:=ί>, q:=Λ/2(p+qU if (3x)(p < x < 340 V. Bounded Arithmetic 

> OΓ

p := L1/2(P + q) J, q := <?, otherwise. By Theorem 4.16 the computation of length |t(a)| always exists. In order to prove its correctness we need only to show that in the j - t h step of the computation the following two conditions are satisfied: 

(3x)(p<x<qbφ(a,x)). 

This is proved by induction on j . Once the computation is given, the condition that we are proving is Σ\ , hence we need only LINDΣ\. If the formula has the form where φ is 77^, we proceed similarly, but we use thorough search instead of binary search. The case of the universal bounded quantifier and connectives &, V is trivial. D

4.25 Corollary. Let T be as above, let M 1= T, and let A" be a D? + 1 closed substructure of M. Then K is ΣQ(Σ\) elementary. 

Proof. By Lemma 4.21 and Lemma 4.24. DSince LINDΣ\ is a Σ\(Σ\) formula, we get that K is a model of S|. But we can prove more. 

4.26 Theorem. Let i > 0, let T be S% if i = 0 and Ί% otherwise. Let K be a D? + 1 closed substructure of some model M of T. Then K is a model of T^. 

Proof. Let i > 0, let M t= T, let K C M be D? + 1 closed. We shall show that for every α(:r, b) in Σ\ , a formula equivalent to /(α(x, b)) (induction for α(x, b)) has Πf +1 Skolem functions, though this is not (known to be equivalent to) a

Σl(Σ\) formula. Then, by Lemma 4.22, 1(a(x,b)) must hold in K. We shall consider the following equivalent formula -iα(ϋ, b) V (3a? < α)(α(*, b) & -*a(x + T, b)) V α(α, b ) . Again we shall use binary search. We start with p := 0 and q := α, and repeat: 

P := L(P + $)/2J, $ := q, if α( L (p + g)/2J, b), 

p := p, ς := L(P + q)/2j, otherwise. 4. Witnessing Functions 341 

If α(0,b) and -ια(α,b), then this algorithm finds in polynomially many-steps (in the length of numbers α,b) some c such that c < α, α(c,b), and -iα(c + l,b). It uses Σ\ oracle a{x). The existence of the computation follows from Theorem 4.17. We must show the correctness of the algorithm, which means that the value obtained by the computation witnesses the existential quantifier in the induction instance provably in T^. We want to show that the following conditions are satisfied in the j-th step of computation: (1) «-p<2-'; (2) α(p,b); (3) -•*(«, b ) . We cannot prove by induction that (2) & (3) holds in each step, since this formula has too large complexity. So we prove (1) and (2) using LINDΣ\ and then we prove separately (3) using LINDΠ\. DNote that we are not able to prove the theorem with 5£ instead of Tg, since we are not able to formalize D?, ^ functions in S|. As a corollary we get a version of the theorem of Buss for fragments T^. It will be a corollary of a stronger result which we shall prove later, but we have to prove it now, since we shall need it for the proof of the stronger one. Moreover the proof is much easier then the proof of Buss's theorem. 

4.27 Theorem. Let i > 0, let φ(x,y) be Π\ or strictΣ^ +1 and suppose 

T}l-(Vx)(3y)φ(x,y). 

Then for some / in Π? + 1 

Moreover, if T is S | if i = 0 and Ί% otherwise, then T h (Va:)y>(a:, / ( * ) ) , i.e. more precisely, for some e E iV, 

T \- (Vx)(3y)({e} i+1 (x) = ykφ(x, y)). 

Proof. Since for every e, T proves that {e}i+ι(x) = y defines a function, we can use the functional notation. First suppose that φ is Π^ . By way of contradiction, suppose that T does not prove (yx)φ(x, {e}i+ι{x}) for any e. Then also, for any fc, T does not prove 342 V. Bounded Arithmetic 

since otherwise, using φ(x,y) as an oracle, we could combine these Turing machines into one producing y for a given x. By compactness, there is a model M for 

T + - y ( c , {0} ί + i(c)) + -v(c, {ϊ}i+i(c)) + • , where c is a new constant. Let K be the closure of {c} under Df + 1 functions in Άf, i.e 

K={αeM\(3ee N)(M N { e } i + i ( c ) = α)} .Then, for every o E l f , M N -ip(c, α). By Corollary 4.25, K is Σf elementary in M, hence Λ Γ t = (Vy)-«p(c,y). By Theorem 4.26, if t= T^', thus Tj does not prove (\/x)(3y)φ(x, y). 

Now suppose that φ(x,y) is j < r ί c t ^ + 1 . Then for some Π\ formula 

Φ(X,ZQ,ZI) and some term t, ψ(x^y) is (3^i < t)ι/?(a:,y,0i). Hence 

(Vx)(3y)φ(x, y) = (Vx)(Ξz)V»(x, ( % , (z) T ) & ( z T < ί ) . By the first part of the proof z can be witnessed by some {e} t +i(a;), hence y can be witnessed by ({e}i+ι(x))-Q, which is a Π^ + 1 function. D4.28 Corollary. Let i > 1, let Φ(x) be strictΔ hi+1 in Tj. Then T\ proves induction for Φ(x). Proof, The assumption of the theorem means that Φ{x) is strictΣ^^ and for some Φ(x) strictΣ* +v T\ h Φ(x) = -i^(x). We can represent Φ and ί? by where </?,^ are in Π*i. Thus we have By Theorem 4.27 we get some e such that 

Ά I" V(«, {β} +i(*)) V ψ(x, {e} w(x)) ,hence We have not gained any reduction of complexity, but this was not our aim, our aim is to witness the induction formula for Φ(x) using a D?V 1 function. Suppose we have Φ(0) and ^Φ(α), and we want to construct some x < α 

such that Φ(x) & -iφ(z -f-1). We shall use binary search in a similar way as in 4. Witnessing Functions 343 

Theorem 4.26. We use φ(x,y) as a Π\ oracle and {e} 1+1 (x) as a subroutine in order to ask questions of the form φ(x, {e} ι + i(x)). The computation goes as follows: 

step 0: p := 0, q := α, u := {e} ί + 1 (0), υ := {e} i + i(α) 

step j+1: r := {e} f +i(L.(p + <?)/2J) if <P(L.(P + g)/2j, r) then p := L(J> + g)/2j, u := r    

> else ς f := L(P + ^ ) / 2 J , υ := r.

The correctness is proved by LINDΠ*? showing that in the j-th. step we have (1) q-p<2-ia; 

(2) φ(p,tήbφ(q,v). D

A 3Πf formula consists of a prefix of existential quantifiers followed by a 

Π\ formula. 

4.29 Theorem. Let i > 0, let <p(x, y, z) be a 3Π^ formula and suppose Then for some / o , . . . , fn in D? + 1 

(d.l) N N (Vx, zo, ." , Zn)(φ(xM*)> zo) V V («, Λ(s, 2?o), Moreover, this is provable in 5^, if i = 0, and in T^, if i > 0. 

Proof. Let T be S£, if % = 0, and TJ, if i > 0, let φ(x, y, z) be a 3J7f formula. Suppose T does not prove the formula in (d.l) for any choice of / o , . . . , fn-

Take some enumeration of functions in Πf +1 such that (1) the n-th function fn depends on < n arguments; (2) each / € Π?, ^ occurs in the enumeration infinitely many times. (For instance, {e} t +i(((zi,Z2)> --i^e))? where ( - , - ) is the pairing func-tion, has this property, assuming natural coding of Turing machines.) By compactness, 

T + -v(c,/o(c),<io) + -^(c,/i(c,d o ),di) + •where c, do> ^1? are new constants, is a consistent theory. Let M be a model of this theory and let 344 V. Bounded Arithmetic 

Since all projections occur in the enumeration and each function occurs in the enumeration infinitely many times, we have (3) c,do,d ud2,...eK, 

(4) K is D? + 1 closed. By (3), we have 

\/aeK3deK M£-^φ(c,a,d). 

Since -*φ is VJCf, using Corollary 4.25 we get Now we would like to strengthen Theorem 4.27 by taking the weaker assumption SJf 1 h (Vx)(3y)φ(x, y) instead of Ί% h (Vx)(3y)φ(x, y). The proof above does not work for S^" 1"1 > since we are not able to show that a Πf +1 

closed substructure is a model of Sϊ^ 1 ^ ι s worthwhile to realize the reason, then we shall better understand the forthcoming proofs. Let (3y < t)ψ(x, y) 

be a £f + 1 formula, where φ is ϋ\. In a Πf +1 closed substructure the quantifier 3y can be witnessed by different elements of the form {e} t +i(α). Since e runs over standard numbers, we can obtain a cut (for instance contained in some segment [0,6]) for which (3y < t)φ(x,y) holds, hence the induction fails. Therefore we shall take closures under some functions with nonstandard indices. 

The basic idea of the proof is the same as above: if (3y)</?(c,y) is not witnessed by a Πf +1 function, we construct a submodel in which it does not hold. Thus we must be careful when adding {e}i+i(c) for e nonstandard. We shall use overspill. If (3y)</?(c,y) is not witnessed by any {e} t +i(c), for e standard, then this must be also true for all e up to some small nonstandard 

r\. Thus we ensure the failure of (3y)φ(c,y) by taking the closure only under functions with such small indices. However it is not so easy to ensure the induction. Now we sketch the idea of the model-theoretic proof of this strengthening. It is essentially the proof of Wilkie with some changes. Let i > 0, let T be 

S\ if i = 0 and T^ otherwise. Suppose that for every e € N, T does not prove φ(x, {e}, + 1 (x)). Take a model M t= T with some c G M, such that M t = -*φ(c, {e} t +i(c)). By overspill this is true also for all e < r\. We shall construct substructures ^consisting of some elements of the form {ef} t +i(c), for e < r i , thus we shall have -i(Vx)(3y)v?(x, y) in the substructures. So we have only to ensure LINDΣ\+ V We shall do it in ω steps (we use only countable models) adding LIND for one formula and one string of parameters at a time. Let us take the formula Φ(x) = (3y < t)φ(x,y) considered above, and let a

be already in our substructure K. We want to extend K so that it satisfies the following instance of LINDΣ\ +χ :

(d.2) -iff(ϋ) V (3j < \a\)(*(j) k -,*(j + T)) V 4. Witnessing Functions 345 

We take a suitable Γ2 < ri, and try to find a witness g$ for Ξy in \P(0) of the form {e} t +χ(c), e < Γ2 If we succeed, we try to find a witness g\ for #(1) of the form {e} t +i((c, (O,<7o)))> e < r2> and s o on. The bound Γ2 is chosen so small that we never construct {e}, +i(c) with e > ri Suppose, for example, that for some j < |α|, we have found < fy , but there is no witness 

gj+χ of the form {c} t -+ i((c,(j,^))) for # ( i + *)• τ h e n w e t a k e the D ? + 1 

closure of (c, (j,gj)) and if in M, and we have (d.2). We repeat this extension process for other formulae and other parameters. In order to preserve (d.2) we use a similar argument as we used for -i(Va;)(Ξy)</?(:r, y). In our particular case, Φ(j) is preserved by Σ\ elementary extensions, since it is 3/7*, while 

-*Ψ(j + 1) will be preserved because we shall add only elements of the form {e}, +i(c), for e < Γ2 The following key lemma formalizes one step of the above construction. 4.30 Lemma. Let i > 0, let T be 5^ if i = 0 and TJ otherwise. Let M be a model of T, K substructure of Af, α, b £ JK", let Φ(x, y) be strictΣj+ι and let 

Ψ(y) be strictΠ^. Suppose that (1) if is a Πf + 1 closure of one element of M; (2) K is not cofinal in M; (3) K\=*(b). 

Then there exists a substructure K* such that K C K* C M, (l)-(3) holds for Λ Γ* and (4) K* t=-i#(ϋ,b) V(3j < |a|)(<P(i,b)&^(i+T,b)) V#(|α|,b). 

Proof. Let the assumptions be satisfied. Let if be generated by an element c. Since if is not cofinal in M, there is some d £ M such that 

xeK=>\x\<\d\. 

Since every x G if is computed in polynomial time from c, and by overspill, we have 

## (d.3) Mr <|<f|, 

for some ΓQ nonstandard. Recall that {e} t + i(a;) = y = ' ' " where z/ t+ i is ^*_ f_1. By (d.3), we can write { e } 1 + i ( x ) = y as a Z\* +1 formula with an additional parameter d, since 

M t= i/ t + i ( e , * , y , 2 W ) = (V* < d)(« = = (3z < d)(z =346 V. Bounded Arithmetic 

Let ,b) = (3z<t(x))φ(x,z), 

where ψ(x, z) is 17* and φ(z) is Σ\; we shall omit the parameters b from now on. Consider the following formula (d.4) (Ve < |r|)({e}, + 1 (c) < s -» φ([e} i+1 (x))). 

Since K 1= !?, K is i?J elementary in M, and every element of K is of the form {e}ί+χ(c), for e standard, this formula is true in M, for every r standard. Also this formula is equivalent to a Δ^ +1 formula in M. Since 5^ h I^ξ, (Theorem 4.7) and for i > 1, Tj h i ^ + 1 (Corollary 4.28), we can use overspill to deduce that (d.4) holds in M for some r nonstandard. Let (d.5) n =min(|ro|,||r||,|c|). Now we construct a Turing machine with an oracle which searches for the witness of the existential quantifier in condition (4) of the lemma. The machine works on input c as follows: 1: j : = - l ; g := 0; 2: find the first e < r\ such that 

3: if such an e dots not exist or j = \a\ — 1, then print (j,g)] 

4: otherwise j := j + ϊ ; g := {e},*4.i((c, (j,g)))', go to 2 where we define 

(-1,0) = 0. Let eo be the code of this Turing machine. We shall estimate eo Recall that it is also the exponent in the time bound of this Turing machine and this makes this estimate nontrivial. To run some {e}j+i with e < r\ on input c

we need at most \c\ e < \c\ Vί steps. In 2: we do it r\ times. The time needed to check the Πf condition of 2: is a standard polynomial in \c\. (Note that we have to evaluate also the implicit parameters b, for which we need time a standard polynomial in \c\.) Finally the cycle given by 4: is repeated \a\ + 1times. Thus the total running time is bounded by where p(x) is some standard polynomial. We have ri < \c\ and \a\ + 1 is also bounded by some standard polynomial in |c|, since it is an element of K. 

Thus we can bound the above expression by |c| 2 r i . Since the program of the Turing machine has standard length, we can bound its code by eo < 2rχ .4. Witnessing Functions 347 

Suppose the machine prints (j,g) on its output. We define K* as follows. If K N -iί(U) V Φ(α), then K = K*> otherwise UΓ* is the D? + 1 closure of 

c* = (c,(j,g)) = (c,{e o}i+i(c)). Now we have to check conditions (2)-(4). We shall assume that K 1=Φ(0) & iΦ(α), hence M f = Φ(0), as if is 27? elementary in M. We have hence the length of each element x of K* is bounded by 

# 1*1 < kl** 2ri , keN. 

Since ri < |ro|, the last expression is bounded by 

> \c\ r°<\d\,

thus K* cannot be cofinal in M. 

To prove (3), suppose that it fails for K*, which means that for some ei e N and h = {ei} i+ i(c*), 

K* \=h<s&-*ψ(h). 

By Corollary 4.25, K* is 27^ elementary in M, thus this formula holds also in Λf. Now c* has been constructed from c using a machine with code eo < 2rχ. Since e\ is standard, the Turing machine which runs first eo and then e\ has a code 62 polynomial in r\, hence, by (d.5), e<ι < |r|. But this is in contradiction with (d.4). It remains to prove condition (4) for K*. We shall show that 

K*\=j<\a\kΦ(j)k-,Φ(j+T), 

where (j,g) is the output of the machine eo The first inequality is clear, since the machine stops before reaching \a\. Also Φ(j) is easy, because, by the program lines 2: and 4:, hence also in K* by elementariness. By way of contradiction suppose that 

K f= Φ(j + 1). This means (again using elementariness) that, for some e G N,   

> M)F {e

In particular e<r\. Recall that c* = (c,(j,g)), thus the machine should not stop at jj which is a contradiction. D348 V. Bounded Arithmetic 

4.31 Theorem. Let i > 0, let T be S\ if i = 0 and T\ otherwise. Let M be a countable model of T, K a substructure of M, b G if, and let Φ(y) be θtrictiT^ +1 . Suppose that (1) K is a D?, 1 closure of one element of M; (2) K is not cofinal in M; (3) i f N # ( b ) . Then there exists a substructure if* such that K C if* C M and (4) if* (5) if* Proo/. We shall construct a countable chain of substructures 

K = i f 0 C i f i C i f 2 C . . . C M , and airtctJTj +1 formulae Take some enumeration of strictΣ\ +1 formulae with parameters from M. In the j-th step, j > 0, we ensure LIND in Kj for the first formula Φ(α, b) from this enumeration for which LIND fails in ifj_i, and whose parameters b are in Kj-ι. Suppose we consider -.φ(0,b) V(3x < |α|)(Φ(x,b)&^(x+T,b)) VΦ(|α|,b) in the j-ίh step. We apply Lemma 4.30 to K^ Φ and \Pj. Thus we obtain . Then we define lPj+i by 

# Jf Kj+1 1=

if i f i + i N k < \a\ kΦ(k) k ->Φ(k + 1), for some fc € if j+ι 

= Ψj , otherwise. Here Φj+i is not written in the strictΠ^ +1 form; however to show that they are equivalent to such formulae, we need only properties of the coding relation that are expressible by equalities and hence preserved from M to D^ closed substructures. Since Φj+ι will be true in all if m, for m > j + 1, also 

LIND(Φ(a,b)) will hold in these models. Consider for instance the second case, where Kj+ 1 \= k < \a\ kΦ(k) k^Φ(k + 1). Then Φ(k) will be preserved by extensions, since all the structures are D? + χ closed, hence Σ\ elementary, while -iΦ(fc + ϊ ) will be preserved by the definition of the extensions. Let if* be the union of this Σ\ elementary chain. Then all formulae Φj are true in if*, hence it satisfies condition (4) and if* N LIND-strictΣ hi+ι .By Lemma 4.23 this implies that if* is a model of 5£ + 1 . D4. Witnessing Functions 349 

Now we are ready to prove Buss's witnessing theorem. The original theo-rem was proved with T = S*^ 1; the next theorem is a strengthening (since T2 is a subtheory of S^"*" 1

) which * s also due to Buss. 

4.32 Theorem. Let i > 0, let φ{x,y) be Σ^ +v Suppose that Then for some / in df +1 ,where Γ is S\ if i = 0 and T\ otherwise. 

Proof. First observe that we can bound y by some term t: 

This follows from Theorem 1.4. By Corollary 4.12 we can assume that φ is 

strict Σ^^. Suppose that the conclusion is false. By compactness, there exists a countable model M of T such that for every e standard and moreover, 2l cl , k 6 iV, is not cofinal in M. Let K

be the Πf 1 j closure of the element c in Λί. Then K is not cofinal in M and since, by Corollary 4.25, it is Σ\ elementary in M. Let Φ be (Vy < t)-*φ(c, y), then it is equivalent to a θtncί J7^ +1 formula already in predicate logic. Thus we can apply Theorem 4.31 to get some which is a contradiction. The most interesting case is with i = 0; we state it explicitly. 

4.33 Corollary. Let φ(x,y) be a Σ\ formula. Suppose that 

S\\-{Vx){3y)φ{x,y). 

Then for some / polynomial time computable function 350 V. Bounded Arithmetic 

4.34 Corollary. For i > 1, S^ 1 is a Σ^ +ι conservative extension of T\, i.e. for φ{x) in Σ\+ v

Proof. Add a dummy existential quantifier to φ(x) and apply Theorem 4.32. 

D

Recall that Δ? sets are sets computable in polynomial time using oracles from Σf^. Let us note that it is an open problem whether Σf^ΠΠf^ = ^ J Thus Λ\ definable sets need not be in Δ?. 

4.35 Corollary. Let i > 1, let φ(x) be a Δ\ formula with respect to S£. Then 

φ(x) defines a Δ? subset of N. Proof. For φ(x) we can find some formulae α(x, y), β(x, y) in Π^i and terms t, s such that S^ I- ψ(x) = (3y < <)α(«, y) = -(3y < β)^(«, y). Hence 

St2\-(3y<t)a(x,y)W(3y<s)β(x,y). 

The last formula can be easily transformed into a Σ*? formula; thus we can apply Theorem 4.32 to obtain some / in D? such that 

N \r (V*)((/(«) < t & α(», /(*))) V (/(*) < s & β(x, f(x)))). 

Hence we can decide φ(x) by computing f(x) and using a Πf_ 1 oracle. DAgain the most interesting particular case of the last corollary is the one with i = 0; it can be stated as follows 

S%\-X e NPΠcoNP =*S\\-XeP. 

# (e) On the Finite Axiomatizability of Bounded Arithmetic 

In this subsection we shall consider the question of the finite axiomatizability of Bounded Arithmetic. First we shall show that the fragments S^ and Tj are finitely axiomatizable for t > 1. Thus the finite axiomatizability of 52 is equivalent to the statement that the hierarchy of these theories is infinite. 4. Witnessing Functions 351 

Then we shall reduce the finite axiomatizability of 52 to the non-collapsedness of Polynomial Hierarchy. 

4.36 Theorem. For t > 1, each of S\ and T\ is finitely axiomatizable. Proo/-sketch. The basic idea of the proof is the same as for fragments IΣ n,

see Theorem 1.2.52. However, since this theorem is important, we give at least a sketch of the proof. In Theorem 4.18 we showed that there axe Σ\ formulae μ t which are in a sense universal; more precisely, for every φ(x) in Σ\ there exists an e such that Furthermore, 21*' provably exists in S^; this follows from the bound For induction and PIND we need formulae which have an induction variable and parameters. One parameter is sufficient since the pairing function and the decoding functions are Δ^ definable. For the same reason, we can extend the result above to formulae with two free variables: Another easy modification of the result above reads as follows: 

S\ h z > 2K* y)F -* (φ(x,y) = μ, (e,(x,y),z)). Now we only need to show that there exists a finite subtheory T of 5^ such that for all φ(x,y) in Σ\ the above equivalence is provable in T. Once we have such a T, we can finitely axiomatize S% by T plus BASIC plus 

(Ve,y,z)PIND(z > 2^^' -+ μi (e,(x,y),z)), 

where x is the induction variable (thus bounded in PIND), and e, y,z are parameters of induction. Similarly we can axiomatize T^. To find such a T we have to analyze formulae μ t and ι/, of Theorem 4.18 more closely. The concept that we want to use is just Tarski's conditions for the definition of the satisfaction of Σ\ formulae. Tarski's conditions describe the satisfaction of formulae of a given class via relating the truth of a formula with the truth of its components. For each closure condition of the class of formulae there is one Tarski condition. The classes Σ\ were defined in Definition 4.2; furthermore we have to use the inductive conditions for the value of terms. 352 V. Bounded Arithmetic 

Now we shall describe the conditions more explicitly. (1) For each function symbol of L 2 we shall have an integer constant, e+, e*, etc., such that etc. (2) For relation symbols = and < we construct binary functions e= and e< such that and similarly for <. The functions are Δ\. 

(3) For each of the conditions of the definition of the class Σ\ we have a function and a condition. Consider for instance the condition Then we have a binary Δ\ definable function e|y| such that = (Vy,z)(n,(ei, x,y, 2 W 1 ) & z < \y | -> μi (e 2,(x, z), 

The function computed by the machine with the code eiyj does the following. If ei is the code of a machine for a term t and e 2 is tne code of a machine for a formula φ(x), then eιyι(ei,e 2 ) is the code of a machine which decides the formula (Vz < \t\)φ(x, z). 

Let T consist of the above conditions plus finitely many sentences needed to formalize functions e = , e<, eiyi, . . . (existence, uniqueness, Δ\ definition). Then we can easily show, using induction on the depth of φ 6 Σf, that there exists an e such that 

> τ

It remains to prove the above Tarski conditions in 5^. A formal proof would, perhaps, require a whole section. But in fact it is not hard to see that they must be provable. Let us look at the last considered condition, which concerns the sharply bounded universal quantifier. Formula μ t has been defined as being true if the Turing machine with code e accepts input x. 

The condition describes what the machine with code e of the form eιy|(ei, e 2 )will do: first it will simulate machine e\ on x and obtain y (the value of the 4. Witnessing Functions 353 

term), then it will simulate machine t*ι on inputs (x,z) with z < \y\. Thus we need only to choose the codes of the machines in a suitable way. D

4.37 Corollary. 52 is finitely axiomatizable if and only if 52 = 5 2 for some i. 

We are not able to decide whether 52 is finitely axiomatizable. We shall only show that it is not, assuming a plausible conjecture that the Polynomial Hierarchy does not collapse on its finite level. This does not seem to be a surprising result because of the relation between the classes of formulae 

Σ% and complexity classes Σf. But the relation is not so straightforward. Induction and definability are different things. We shall show that induction is related to optimization and we shall use this fact in our proof. 

4.38 Theorem. Let i > 0 and suppose 27? +2 φ JTf +2 . Then TJ φ Sι2+1 .

4.39 Corollary. If the Polynomial Hierarchy does not collapse then (i) 5 | φ 5 | + 1 for i > 1 and TJ φ T^ +1 for i > 0. (ii) 52 and T*ι are not finitely axiomatizable. (iii) IΔQ + Ω\ is not finitely axiomatizable. (iv) IΔQ is not finitely axiomatizable. 

Proof, (i) and (ii) follow using the inclusions T 2 C S | Q T\ Q 5 2 .(iii) IΔQ + i?χ is contained in 52 in such a way that the functions of 52 axe definable in IΔQ + Ω\. 

(iv) Just recall that Ω\ is a single axiom. DBefore proving Theorem 4.38 formally we shall sketch the main steps of this proof. We shall consider only the case i = 0. Let C(x,y) be a polynomial time predicate. Consider the optimization problem of finding maximal y such that y < x and C(x,y). In order to simplify notation we shall assume that the bound y < x is implicit in C(x, y) 

and that C(x,Q) holds for all x. We shall call y a feasible solution to x if C(x, y). Let ψ be defined by (e.l) φ(x,y,z) = C(x,y)k(\y\ < \z\ - ^C(x,z)). 

Since C is polynomial time computable, φ is Σ\. NOW the meaning of 

(yz)φ(x,y,z) is that y is the feasible solution to x of maximal size. In 5 2

the schema LINDΣ^ proves that for every x there exists a maximal feasible solution y. If T® = 5 2 , then this is true also in Γ^, i.e. 

Ί$\-(Vx)(3y)(Vz)<p(x,y,z). 

Now we can apply Theorem 4.29. We obtain some functions /oj/io j/n computable in polynomial time such that 354 V. Bounded Arithmetic 

(e.2) N 1= (V*, * 0 , ,*n)GK*,ΛOO,*θ) V φ(x 9/i(s,* 0),* α)V • V φ{x, f n(x, *0, , *n-l)> The rest of the proof is only complexity theory. We want to show that such functions cannot exist for all polynomial time predicates C. If n were always 0 (as in Buss's theorem) then our goal would be simple. In such a case, for example, we could construct a maximal clique in a graph using a polynomial time computable function /o This is impossible unless P = Λ/P. In fact we can take any NP problem, not only optimization problems. Let C(x,y) be defined, say, by 

y = 0 or y is a Hamiltonian circuit in graph x.Then fo(x) would be 0, if x is not Hamiltonian and fo(x) would be aHamiltonian circuit in x otherwise. But in general n need not be 0. So we modify our problem as follows: 

x will be a string of graphs and y will be a string of 0's and Hamiltonian circuits in corresponding graphs. Now we assume that for this particular C

we obtain (e.2) with n = 1, (this is sufficiently instructive). Consider an x, a two element string x = ( G i , ^ ) , where both graphs are Hamiltonian. Then there are two possibilities: (1) fo(x) is not a feasible solution or fo(x) = (2/1,2/2) where yi = 1 /2 = 0; (2) /o(s) = (2/1,2/2) and 2 /1 is a Hamiltonian cycle in Gi or y is a Hamilton cycle in G2; In case (2) /o has produced nontrivial information. In case (1) it is not so, but /1 must produce information: if we take zo = (2/'>0)> where yf is some Hamiltonian cycle in C?i, then we have ->φ(x,fo(x),zo), since either /o(#) is not a feasible solution or ZQ is a better one. Hence we get i.e. fι(x,zo) is an optimal solution. This means that fι(x,zo) = (1/1,1/2) where both y\ and 1 /2 Άre Hamilton cycles. Let us draw an arrow G\ —> G% 

in case (1) and an arrow G2 -> Gi in case (2). This indicates that by having a Hamiltonian circuit for the tail we can construct a Hamiltonian circuit for the head. Consider all Hamiltonian graphs of size m. The above argument shows that there is an arrow at least in one direction between any pair of them. An easy counting argument shows that there exists a set of polynomial size of such graphs which covers the rest. For each of these graphs, we choose a Hamiltonian circuit in it. Let H be the set consisting of these pairs. H has also polynomial size. Using H we can decide in polynomial time whether a graph G is Hamiltonian: try / 0 and f\ on all pairs (G, H) and (Jϊ, G), where H runs through H. Computations which use additional polynomial size 4. Witnessing Functions 355 

information axe called computations with polynomial advice. There is a well-known argument (see [Karp-Lipton 80]) showing that if every NP problem can be computed using polynomial time computation with polynomial advice, then Σξ = Πξ .Now we prove Theorem 4.38 in detail. We shall divide the proof into several lemmas. Let i > 0 be given. A formula C(x, y) will be called a Πf optimization problem if C(x,y) is a Π\ formula such that C(x,0) and C(x,y) —> y < x is provable in predicate logic. We shall say that y is a length optimal solution to x if the following formula holds: 

4.40 Proposition. For every Π\ optimization problem C, S^ 1 proves that C

has a length optimal solution to every x. Proof. Let ψ(x, y) be defined by 

ψ(x,u) = (3y<x)(C(x,y)&ε\y\>u). 

By LINDΣ!? +1 we have 

-V(*,0) V (3u < \x\)(ψ(x,u)k^ψ(x,S(u))) V φ(x, \x\). 

Since ψ(x, 0) is always true, it just expresses the existence of a length optimal solution. •It is an easy exercise to prove that, in fact, the existence of length optimal solutions to Πf optimization problems is equivalent to PIND Σ^ ^ over a sufficiently strong base theory, say S^ 

We are going to use Theorem 4.29. It is convenient to refer to the conclusion of the theorem, see formula (e.2) above, as a kind of interactive way of computing a witness to 3y in (Vx)(Ξy)(V^)y?(a;, y, z). Let x be given and suppose we want to construct y. Assume (e.2) holds true. First consider /θ(x). If (Vz)y?(x,/o(x),z), then take y = /o(z), otherwise there is some ZQ 

such that ^φ(x, /O(X),ZQ). We shall call this z$ a counterexample to fo(x) 

By (e.2), it must be n > 0 and we have       

> fn(x, zo,..., 2n_ i ) , zn)) .

Hence we can repeat the reasoning above and we get that either fι(x,zo) 

witnesses y or the disjunction can be reduced further by taking a counterex-ample z\ to /i(a:, ZQ ). However this process can be repeated at most n times, since when we obtain (Vx, zn)φ(x, fn(x, 

we can stop. 356 V. Bounded Arithmetic 

Let C(x, y) be a Πf optimization problem. Assume that TJ = S^ 1. Then Γ2 proves that C has always length optimal solutions. This statement can be expressed in the form (Vx)(By)(Vz)φ(xjy,z) with φ in 17* +1 , see (e.l). Hence, by Theorem 4.29, we get that an optimal solution can be computed using Πf +1 functions and a fixed number of counterexamples. This is our first lemma. 

4.41 Lemma. If T | = S^" 1"1, * - 0, ^ e n * o r e v e r v H\ optimization problem its length optimal solutions can be computed using Πf +1 functions and a fixed number of counterexamples. The computations with counterexamples do not define a function complex-ity class, since we allow the asking of counterexamples only for the particular optimization problem that we want to solve. If we allowed asking arbitrary queries of the same logical complexity, we would obtain just the class Π ^ But it is easy to prove that optimal solutions can be computed by such func-tions. Thus our next step is a reduction to a different function class. 

4.42 Definition. A function / belongs to ϋ/^/poly if there exists some g in D? and a polynomial p(x) such that for every k there is αj. < p(k) such that for every x, \x\ = fc, Here ak is called a polynomial advice] it is some extra information given for free for each size of input; the dependence on the size of input is quite arbitrary. 

4.43 Lemma. Let i > 0. Suppose that for every Π\ optimization problem its length optimal solutions can be computed using D? \ 1 functions and a fixed number of counterexamples. Then for every φ(x, y) in Πf there exists an / in Π^^/poly such that 

N t= (Vx)((3y < x)φ(x,y) - V>(*,/(*))) 

Proof. Let φ be given. Define a Πf optimization problem p(u,v) by 

p(u,υ) = lh(v) < /Λ(u)&(Vt < lh(v))(φ((u) t,(v) 

Let /o(u), > /n(w, VQ, ..., v n _i) be some functions in Πf +1 which interac-tively compute length optimal solutions for p. Let k be given. We shall con-struct a polynomial advice for inputs of size k. Once we describe the advice, the definition of the function g will be clear. Let 

Vι = {x;\x\ = kk(3y<x)φ(x,y)}. 4. Witnessing Functions 357 

Choose some function w(x) such that, for x G Vί, We shall use the following notation. If m < lh{u) then 

w{u I m) denotes the sequence (u;((u)o),... ,w({u) m)). To each n + 1-tuple u of ele-ments of Vι, we assign a pair (/, y), 0 < / < n, using the following procedure: 

Step 0: compute fo(u); if p(u,fo(u)) and lh(fo(u)) > 0, then put / = 0 and y = (fo(u))o and stop, otherwise go to step 1; 

Step m (m < n): compute fm(u, w(u | 0),..., w(u \ m — 1)); if 

ρ(u, fm(u, w(u I 0),..., w(u I m - 1))) and (u, w{u I 0),..., w{u I m - 1))) > m,then put / = m and y = (/m(ti,u>(u I 0),...,w(u I m - l ) ) ) m ,otherwise go to step 7?ι + 1; 

Step n: If we have reached this step, then it necessarily holds that />(u, /n (u, u;(ti I 0),..., u;(u I n - 1))) and /Λ(/n(tι, u;(tι I 0),..., w(u I n - 1))) = n + 1, thus we put / = n and 

y = fn(u,w(u I 0),...,u>(tx I n - 1 ) ) , and stop. Let us call y a witness for x if φ(x,y). The meaning of the above procedure is the following. Let u be an n + 1-tuple and let /, y be assigned to it. Then having witnesses for (tί)θ) ? (u)/-!.* w e c a n compute the witness y for (w)/. For an n-element subset Q of V\ and α: 6 Vχ\Q, we shall say that pair (Q, x) is ^oorf if for some arrangement {XQ, . . . , α:/_i, x/_|_i,..., xn} °f Q? / is assigned to u by the above procedure, where u is the sequence , . . . , xn).358 V. Bounded Arithmetic 

Define a sequence of subsets of V\ 

having N\ , N2 ,..., respectively, elements. The j+ 1-st element in the sequence is defined as follows. Find an n-element subset Qj C Vj such that 

## \{x E Vj iQ^x) is good }| > - ^ f , 

and take 

Vj+1 := Vj\{x 6 Vj\ (Qj,x) is good } . 

We must show that it is always possible to choose such a Qj. By the procedure above, for each n + 1-element subset {XQ, . . . ,ar n} of Vj we can construct a good pair (Q, x) such that by taking u to be the sequence (#o> >#n) Hence there are at least ^

good pairs. On the other hand there are ( n J ) n-element subsets Q of Vj, so at least one such Q must form good pairs with at least 

# :^>cr=^ elements. Hence from which we get 

n ( n \ 2 I' n \ 3

Hence we get Nt < n + 2 after t steps, for * < log 2 (^l).(lGg 2 ((n + lj/n))-1 < 0(log 2 (2 Λ )) = O(k) .We take the polynomial size advice to be the sequence of pairs (a;, w(x)), 

where x runs trough all elements of 

Ql U 02 U . U Q* LI V5 4. Witnessing Functions 359 

Now let x be such that i.e. x € V\. Then either x E Vt and so a witness for x is in the advice, or 

(Qj,x) is a good pair for some j < t. But then we can construct a witness for x from the witnesses for the elements of Qj (using D? ^ functions in the procedure above). D

4.44 Lemma. Let i > 0. Suppose that for every ψ(x, y) in Πf there exists an / in Π^^/poly such that 

N t= (Vz)((3y < x)φ(x,y) -+ φ(x,f(x))). 

Then Σ? +2 =Πf +2 .Proof. Let A(b) be in J7f+2 Without loss of generality we can assume that it can be represented in the form where 7 is J7J\ Let ψ(x, y) be a Πf formula such that 

φ{{b,x),y) = \x\ = |6| ^ (y < bk Ί{b,x,y)). 

Let / be a function in Ώ?^/poly guaranteed by Lemma 4.43 for φ> and let function g in Πf +1 and polynomial p be guaranteed by Definition 4.42 for /. Then we can write A{b) in the following Σf +

A(b) = (3α)(α <KI(ft,fc)l)&(V*)(H = \b\ ^ 7(b,x,g(a,(b,x))))). 

The right to left implication is trivial, the left to right implication follows by taking an advice α. DThis finishes the proof of Theorem 4.38. There is a similar reduction of the question S£ = T 2? to a problem, in complexity theory. First we shall define that for an optimization problem C7(a;, y), y is an optimal solution to x if Secondly, we define interactive computations with an unbounded number of counterexamples as the the natural extension of the concept above. Of course,        

> 1Note that gis Ilf. Λdefinable by Theorem 4.17. 360 V. Bounded Arithmetic

there is an implicit polynomial bound to the number of counterexamples, since we consider only polynomial time oracle computations. Note that the number of feasible solutions to x may be exponential in |z|, thus polynomial number of counterexamples apparently cannot help to solve some difficult optimization problems (such as the TRAVELLING SALESPERSON), while it gives trivial algorithms if we ask only for length optimal solutions (as in CLIQUE for instance). We have the following counterpart of Theorem 4.29. 

4.45 Theorem. Let i > 0, let Sι2 h (VaO(3jr)(Vs < t)φ(x,y,z\ for φ in 2 # + 1 

and t a term. Then, for a given x we can compute y using Πf +1 computations with (an unbounded number of) counterexamples. This theorem can be proved using the proof theoretical method which Buss used for his witnessing theorem. We are not going to prove it here. The counterpart of Lemma 4.41 is the following. 

4.46 Corollary. For i > 1, if 5£ = T^, then the optimal solutions for ev-ery ilf_i problem can be computed using Πf +1 computations with (an un-bounded number of) counterexamples. We conjecture that the conclusion of Corollary 4.46 is false, hence also 

# that S%2 φ Tj. 

The research on witnessing functions is still going on and we can look for new nice results. The task of proving that Bounded Arithmetic is not finitely axiomatized without assumptions on complexity classes seems still too hard. What might be more accessible is to prove nonconservation results for S2 and 

T2 using such assumptions. 

# 5. Interpretability and Consistency 

# (a) Introduction 

In the last section we were mainly interested in the strength of theories obtained by restricting the quantifier complexity of bounded formulae in the scheme of induction. The main theme of this section is investigation of the strength of theories obtained from IΣQ by adding functions of a different growth rate. (These functions have graphs definable by ΣQ formulae, so the strength is increased by assuming that they are total.) We shall 5. Interpret ability and Consistency 361 

consider typical questions of metamathematics: interpretations, provability of consistency, conservativity, etc. First we shall consider the definition of truth for Σo formulae in Bounded Arithmetic. As a consequence we obtain that IΣQ -f- Exp is finitely axiom-atizable. Another consequence (which uses further technical results) is the existence of an interpretation of IΣQ -f Ωn in Q, n = 1,2,..., which in turn implies that Q and these theories are equiconsistent in IΣQ + Ω\. For fur-ther results we need a formalization of a weaker form of the cut-elimination theorem in IΣQ + Exp. The usual form of this theorem is improvable in this theory. On the other hand GδdeΓs incompleteness theorem can be strength-ened further for such fragments. For instance IΣQ -f Exp does not prove the consistency of Q. This and several other results of this kind will be shown in subsection (f). Finally we shall consider the question of limited use of exponentiation in IΣQ. 

## (b) Truth Definitions for Bounded Formulae 

In Chap. I, Sect. 1 we have shown that truth for ΣQ formulae can be defined by a A\ formula in IΣ\. Because of diagonalization there is no such Σ"o definition. However we can omit the main 3 quantifier in the Σ\ formula and thus we obtain a Σo formula with an additional parameter. Then we estimate how large the parameter must be; put another way, we are looking for a suitable bound to the 3 quantifier in the Σ\ definition of Σo truth. Sometimes we shall call the ΣQ formula obtained in this way a truth definition for ΣQ 

formulae, though it is not quite precise. The construction will be essentially the same as in Chap. I, only we have to compute the bounds more precisely. Before constructing a formula with a parameter which defines the truth for Σo formulae, we shall briefly consider this problem from the point of view of complexity theory. Assume that there is a definition of Σo truth described above; suppose that it has the quantifier complexity k and the bound to the parameter is some function /. Then we have the following relation between complexity classes Σjf C Σ^ (see Sect. 2 for definitions). Thus the corresponding question is: for which function g and constant k

do we have Σ^ C Σ% ? Recall that Σ^ are just the sets in the Linear Time Hierarchy (Theorem 2.16), hence the best that we can achieve (to our present knowledge) is 

## ^ C [ J T/7ne(c n) = E. 

c€N 

This result can be used to write a definition of truth for Σo formulae based on a Σo formula with an exponential bound to the length of the parameter, but again we not only need a formula, but also proofs of its properties in IΣo 

Furthermore we need an estimate of the constant c. Therefore we present an explicit construction. 362 V. Bounded Arithmetic 

We shall use the notation introduced in Sect. 3. Thus for instance max(s) is the maximal element of sequence s. In this subsection we use only the stan-dard arithmetical language LQ. The formalization of syntax is as described in Sect. 3; thus if x is the Gδdel number of an expression, \x\ is its length. Our approach is to consider a bounded formula literally as a program. The computation of terms needs no explanation; the interpretation of bounded quantifiers is as search procedures. The crucial thing is to estimate the size of the numbers that will occur in such a computation. Let us consider an example first. Let a(x) be a bounded formula 

(By < x2)(3z < y 2)(3u < z2)β(x,y,z,u), 

where β is also a bounded formula. To compute the truth value of a(x) we use three FOR loops, one for each bounded variable. Note that the third loop has the range 0 to x2 .

5.1 Proposition (IΣQ). (1) For a term t and a string of numbers s, t(β)<(max(β) +2)1*1. (2) The maximal value needed to compute the truth of a bounded formula α on a string s is bounded from above by Note in passing that, by (1), the value of a closed term t is bounded by 2^' < 2£, hence it can be defined as a total function in IΣQ, while for general terms in Lo we need IΣo + Ω\. Nevertheless the estimates above axe provable in IΣQ provided that the upper bound exists. 

Proof. (1) is easily proved by induction on the length of t. 

(2) This is also proved by induction on the length of α. We shall compute only the induction step for a quantifier. Let α(s) be (3y < tf(s))/?(y,s) (for V it is the same). Assume we have bound for β(y, s). By (1) we know that ί(s) < (majc(s) + 2)1*1, hence for α(s) we get (max(s, (max(s) + 2)1*1) + 2) 2 "" = (((max(s) + 2)1*1) + 2) 2 "" 5. Interpretability and Consistency 363 

We shall estimate the exponent: which proves the induction step. DFirst we define the graph of the val function which defines the value of arithmetical terms. Also here we need an additional parameter. The meaning of Value(y, x,z,u) is: y is the value of term x computed on string z, u is the parameter. Let Var(x,i) be a formalization of the concept of the i-th 

variable. 5.2 Proposition. There exists a ΣQ formula Value(y, x,z,u) and a polynomial 

p such that it is provable in IΣQ that: (1) Term(xι)bTerm(x2)b\xi\,\*2\ <vk\u\ > p(\ max(z)\,v) -> 

-* (Vαr(xι,i). -+ Vαlue(y,x uz,u) = (*)ί = y) k(Vαlue(y,O*,z,u) -> y = 0) 

b{Vαlue( yι ,S\xι),z,u)b Vαlue{y 2,xι,z,u) -> y i = S(y 2)) 

&( Vαlue(y,xι+ mx2,z,u) & Vαlue(yι,x\,z,u) 

& Vαlue(y 2,x 2,z,u)->y = yι+ y2)

& ( Vαlue(y, x\ **x 2, z, u) & Vαlue(y\ , x\ , z, u) 

& Vαlue(y 2,x 2, z,u)-^y = yι* y2)

(2) ψerm(x)k \x\ < vSz |uχ|, |tι 2| > p(|max(z)|,v) 

Vαlue(y 2,x,z,u 2) -> y\ = y 2 .

Proof. Vαlue(y,x,z,u) is defined as (3s < ιt)(/?(y,x, z,s), where is a Σ"o formula expressing the following conditions: (1) s is a sequence of pairs (αo? &θ)> > ( α m? &m); (2) for every i < m, either α, is a variable, or α, is αj-f- α*., where 0 < j , fc < i, etc. for S, 0 and *; (3) if α t is the j-th variable, then δ, = (z)j\ if α t is αj+ αjt, then 6, = bj 4 - ^ ; etc. for S,0 and *; (4) y = b m and rr = α m .Olearly, if s satisfying these conditions exists, then it determines y uniquely and the conditions of the proposition are provable. (Namely, using induction, one can prove that every sequence of pairs for a subterm of t is a subsequence of some sequence of pairs for t.) Thus we only have to find an upper bound to the size of s. Assume s is given. By Proposition 1 (1), 364 V. Bounded Arithmetic 

Since the pairing function is a polynomial, (α t , 6 t ) is bounded by a polynomial in v and (max(z) + 2) υ , hence (α,-, 6, ) < (max(2r)-f2) 9(v) for some polynomial 

q. By Proposition 3.30, \s\ < r(|(max(^) + 2) q^\,v) for some polynomial r, which gives the required bound \s\ < p(\ max(2r)|, υ), p a polynomial. The details can be worked out in a similar way as we did in Sect. 3. D5.3 Corollary. The value of an LQ term is definable by a XQ formula (in fact by a bounded formula in £2). 

Proof. Define 

val(x, z) = y =df Value(y, x, 2,2 P '' m a x W Ί ί B l ' ) . •The meaning of Γ(x, 2:, u) in the following theorem is: the Σ$ formula x is satisfied by a string of numbers z and u is some bound. 5.4 Theorem. There exists a ΣQ formula Γ(x, z,u) and a constant c such that it is provable in IΣQ that: |tι| > (max(z) + 2)°" &ε\x\ <v.-> (x = t =* s-* (Γ(a?,z,ti) =                

> (3y)( Value(y,t,z tu)b Value(y, 5,z,tι))))&
> & ( x = (ari —^ #^2) ~^ (-^(^j ^ ) w) = (F(x\iZy u) —> ^ ( a ; 2 j 2 : )l ί ) ) ) ) &

&(x = -. a?i -* (Γ(a?,z,u) = -iΓ(a;i,z,u)))& & (a? = (3 uι <• t)a?i -> (Γ(x, z, u) = (Ξy, y')( 7a/tte(i/, *, z, ti) & y < y ;

where we assume that w is the j-th variable for some j and sequence z' is obtained by replacing its j-th entry by y; the conditions (Tarski's conditions) for <* and bounded V* are similar and therefore omitted. 

Proof. The proof is similar to the one above. We define Γ(x,z,u) as (3s < u)ψ(s), where ψ(s) says that s is a sequence consisting of pairs of some sub-stitution instances of subformulae and their truth values satisfying Tarski's conditions. Let s be the sequence of pairs (αo,i>o)? Λαm>b m). We shall require the following condition. Let α, be of the form (Ξtu < t)φ{w) or 

(Vw < i)φ(w). Then we include all formulae φ(n) for n < vαl(t,z) in Go* >αm Here n denotes the dyadic numeral introduced in Sect. 3(g). (If the value of (3*w <• t)φ(w) turns out to be TRUE, then it suffices to in-clude just one φ(n), but this is not a real advantage.) By Proposition 1 (2), the values needed to compute the truth value of a formula x are bounded by 5. Interpret ability and Consistency 365 

Thus the α t 's axe Gδdel numbers of subformulae of x with some variables replaced by numerals n for n < (max(2) + 2 ) 2 M .The length of such formulae is estimated by 

c 1 * | ( m a x ( z ) + 2 ) 2 " 1 | * M , 

where c\ is a constant, since the length of a numeral is linear in its value. The length of (α t , δ, ) is thus for some constant C 2 Now we estimate the number m of such pairs. We have at most I a; I variables in x, and each variable can be replaced by a numeral n

with the bound abpve for n. This gives ((max(z) + 2) 2 * + 1)'*' possibilities and there are at most \x\ subformulae, hence m < |x| * ((max(z) + 2 ) 2 M + l)l x l. Thus we can estimate the length of s by c3 * |(max(*) + 2 ) 2 M | * \x\ 2 * ((max(*) + 2 ) 2 W + 1)1*1 < (max(z) + 2 ) c M ,where C 3 and c are suitable constants. Hence if u is larger than or equal to this bound, then there exists some sequence s that witnesses the truth of x. 

The provability of Tarski's conditions is shown as above. DFor a string of variables z\ y..., zn we denote by (21,..., zn) the code of the sequence z\ ,..., zn.

5 5 Corollary. (1) For every bounded formula α(^χ,..., zn) in L$ there exists a constant k such that 

IΣo h u > 2 ( » « < * I . - Λ > + 2 ) * ^ («(,!,...,*„) = Γ(a 9(z u...,zn),u)). 

(2) Let M be a model of IΣQ, let α, b,d G M, let a(x) be a Σo formula. Suppose d is nonstandard and 5 > 2^ a+2 ) . Then 

Proof. (1) First apply Proposition 5.2 to prove the statement for a atomic using induction on the complexity of terms in it. Then for general a use induction on the logical complexity of a and Theorem 5.4. (2) This is an immediate consequence of (1). D366 V. Bounded Arithmetic 

5.6 Theorem. IΣQ + Exp is finitely axiomatizable. 

Proof. Let T be a finite fragment IΣQ such that T proves Tarski's conditions of Theorem 5.4 for Γ. Then for every a bounded, T proves the formula of Corollary 5.5(1). Let φ be defined by 

φ(x,y,p,u) = Γ(a;,(y,p),t/). (Here we are misusing notation: to be quite precise, we should distinguish between a pair and a two element sequence, but we do not want to introduce new notation.) Let T1 be T plus the least number principle for φ{x^y^p yu), 

where y is the induction variable and x, p and u are parameters, plus Exp. Let 

> a

(yiP) D e a-11 arbitrary bounded formula for which we want to prove the least number principle (clearly it suffices to have just one parameter). We shall argue in T1. Let p be given and suppose that for some yo w e have α(yo,p). Since we have Exp, we can take 

u > ,where k corresponds to α. Hence, for y < yo, 

a(y,p) = Γ(α, (y,p), u) = φ(a, y,p, u) .Thus we can take the least y for φ(a, y,p, u). Ώ

# (c) An Interpretation of IΣQ in Q

Q is a very weak theory, e.g. the associativity of + is not provable in it. However from the point of view of interpret ability it is quite strong. We shall show that IΣQ + Ω n is interpret able in Q for every n. Moreover the form of interpretation is very natural: we take the same operations and only restrict the domain. The domain of interpretation is, roughly speaking, an initial seg-ment of the original numbers. This suggests an attractive finitist's program, which was pursued by Edward Nelson [Nelson 86]. Namely, the consistency of 

Q seems quite evident; further it is also evident that interpretation preserves consistency, thus if we develop mathematics only in theories interpretable in Q, we are safe-guarded against inconsistencies. Later on we shall see that we can even interpret in Q some consequences of IΣQ + Exp which are not available in IΣQ + Ωn (Theorem 5.27 (i)). 1          

> 1Let us remark, for those who are interested in minimal foundations of mathematics, that one can use an extremely weak system for set theory instead of Q, since Qis interpretable in it. The system has only two simple axioms: (Vx)(V»)(3^)(Vn)(« 6 z= (« 6 xV u = y)). 5. Interpret ability and Consistency 367

The main reason why we consider interpretation of Bounded Arithmetic in Q is, however, different. The interpretability of systems of Bounded Arith-metic gives us equiconsistency of them with Q, and this equiconsistency is provable in Bounded Arithmetic too. Hence Gδdel theorem implies that such a system does not already prove consistency of Q. 

The rest of the subsection is almost entirely devoted to the proof of the following theorem. In the whole subsection we shall use only interpretations given by restricting the domain. Such an interpretation is determined by a formula with one free variable. 

5.7 Theorem. For every n, there exists a global interpretation of IΣo + Ωn

inQ. By a global interpretation we mean the usual concept of interpretation. The word global is used here to stress the fact that we have one translation of the language (but in fact only the domain will be different) such that the translations of each one of the infinitely many axioms are provable. On the other hand, local interpretation means that we can choose a different translation for every finite subset of axioms. Nelson uses local interpretations in his book. We shall use a local interpretation as an intermediate step. We shall say that a formula I(x) is inductive in a theory T if Recall that I is a cut in T if it satisfies moreover provably in T. We shall say that J(x) is a subcut of I(x) in T if moreover 

T h J(x) -> I(x) .Let Q + be Q augmented with the following axioms: 

(associativity of +) (x + y) + z = x + {y + z) (left distributivity) x(y + z) = xy + xz (associativity of *) {xy)z = x(yz) .

5.8 Lemma. There exists an inductive formula I(x) which determines an interpretation of Q+ in Q. 

We shall not prove this lemma. It can be proved using similar tricks as we shall use below, but it is technically more complicated, since we start with a very weak theory Q. A complete proof can be found in [Nelson 86]. 368 V. Bounded Arithmetic 

5.9 Lemma. Let I(x) be an inductive formula in Q. Then there exists a subcut 

J(x) of I(x) in Q. Proof. We shall use the following three easy theorems of Q: 

(i) * < 0 , (ii) x < y = S{x) < S(y), 

(iii) 0<x. 

Let I be inductive in Q. Let K be defined by 

K(x) = I(x)k(yy,z)(z <yky <x^z<x). 

We shall show that K is inductive. K(0) follows easily from (i) and from 1(0). 

Suppose K(x). Then, clearly, I(S(x)) and it remains to prove the second part of the condition for K(S(x)). Let z < y < S(x). If z = U, then, by (iii), z < x. 

Otherwise,__by (Q3), z = S(z'), for some z1. Then, by (i), (Q5) and (Ql), y

cannot be 0. Thus y = S(y f), for some y'. Thus we get z1 <y' < #, using (ii). By K(x), we have z1 < x. Using (ii) once again, we get z = S(z f) < S(x). 

Hence K is inductive. Now define First we shall show that J is inductive. J(0) follows easily from (i). Assume 

J(x) and let y < S(x). We need to show that K(y). If y = 0, then K(y), 

since K is inductive. Suppose that y = S(y'), for some y1. Then, by (ii), we get y1 < x, hence K(y ι). Since K is inductive, K(S(y')), which is K(y). Thus 

K is inductive. Now we shall prove that 

J{x)hy <x-+ J(y). Suppose J(x)&εy < x. Let z < y be arbitrary. We need to prove K(z). By J(x), we have in particular K(x), hence z < x. Thus we have K(z), since J(z). D

5.10 Lemma. Let I(x) be an inductive formula in Q ~*~. Then there exists a cut J(x) such that J is a subcut of / closed under 5, + and *, i.e. Q + proves 

J(U); 

J(x) & J(y) -+ J(S(x)) & J(x + y) & J(α y). 

Proof. By Lemma 5.9 we may assume that J is a cut. We shall use the same construction as in the proof of Theorem 3.5, Chap. III. Take 5. Interpret ability and Consistency 369 

Then Jo contains 1, since I is inductive; Jo is closed under + by associativity of +; J is contained in JQ (since Jo contains 1) and hence also in /; J is closed under + by left distributivity and since JQ is closed under +; J is closed under 5, since it contains 1 and it is closed under +; J is closed under * by associativity of *. To show that J is closed downwards, we use the assumption that / is a cut, left distributivity and JQ being closed under +. 

D

5.11 Lemma. IΣo is locally interpretable in Q. Proof. By Lemma 5.8 we can take Q~^~ instead of Q. Let y?i(x, p ) , . . . , φn(χi p) be given bounded formulae. We want to interpret Q plus induction for ¥>1 (a,p),...,¥>*»(*,P) i n Q+- L e t  

> Jj (a?,p) = ψj(

for j == 1,... ,n. Let (*, P)) Since each Ij(x, p) is inductive with respect to x in Q + , so is I(x). By Lemma 5.10 we can find a subcut J(x) closed under + and *. Since J is closed under 5, + and * and it is closed downwards, we have, for any bounded formula Since 

J(x) -> I(x) -> Ij(x) 

provably in Q + , for every j , J determines an interpretation of induction for every ψj. All but two axioms of Q (even Q + ) are open, hence they hold in the interpretation. The remaining two axioms are (Q3): x Φ 0 — » (3y)(x = S(y)) 

and (Q8): the definition of the relation <. The first one is provable using induction for bounded formulae from the others (hint: first prove x < 5(x), then x φ 0 — » (3y < x)(x = S'(y))). Hence we can simply suppose that we have enough formulae amongst φ\, ... ,φ n to prove it. The last one causes no problems, since we can trivially interpret Q in the theory obtained from 

Q by eliminating < from the language and deleting (Q8). D

Proof oί Theorem 5.7. By Theorem 3.5, Chap. Ill, we know that each cut in a sufficiently strong theory can be shortened to a cut closed under ωn, for a given n. One can easily check that IΣQ is strong enough for that. So, by the last lemma, we only have to interpret IΣo in a finite fragment T of IΣo. We take T so strong that 370 V. Bounded Arithmetic 

(1) the properties of the exponentiation relation are provable in it, (2) Tarski's conditions for the formula Γ of Theorem 5.4 are provable in it, and (3) the least number principle for .Γ(a;,(y,p),u), with y as the induction parameter, is provable in it. By the same theorem of Chap. Ill on shortening cuts we get a cut I(x) such that By Lemma 5.10, we can assume that / is closed under + and *. We claim that 

I determines an interpretation of IΣQ. It suffices to prove the least number principle for every bounded α(y,p) with just one parameter. Let p be an element in I and suppose that for some yo in / we have α(yo,p). Take 

u =where fc corresponds to a. This is possible, since       

> 2(max(2/ 0,p)) fc <22m*χ(*o,p) * ^

and the last number exists by a property of I. Now we conclude as in Theorem 5.6: for y < yo, and we can take the least y for Γ(Έ, (y,p), u). ΠThe concept of consistency Con used in the following theorem is the usual one as used in Chap. Ill, except that we must use the efficient coding of sequences as described in Sect. 3 of this section. 

5.12 Theorem. For every n, h Con(IΣ 0+Ω*) = Con(Q m).

Proof. The consistency of IΣo + Ω n implies the consistency of Q trivially. The consistency of IΣQ + Ωn can be reduced to the consistency of Q using an interpretation. We shall analyze this proof, in order to see that it can be done in IΣQ + Ω\ . Let a proof of a contradiction in IΣQ + Ωn be given. Using the interpretation constructed above we can transform it into a proof of a contradiction in Q. Again, it is clear that the interpretation as a relation can be described by a ΣQ formula. Hence we only have to check that the size of the transformed proof is polynomial in the original one. This can be proved by showing that each application of a logical rule in the original proof is replaced by only a polynomially longer sequence in the new proof. There 5. Interpret ability and Consistency 371 

is only one place where we have to modify the interpretation given above. When we prove the least number principle for a bounded formula α, we define parameter u by   

> u_2(max(y 0,p))*

Now we have to take into account how k depends on α, since a is not fixed. Thus instead of the double exponential function in the definition of /(x), we take triple exponential. Hence where cut J{y) determines an interpretation of a sufficiently strong finite fragment T of IΣQ in Q. Then we replace number A ; in the definition of u by a more explicit bound given by Theorem 5.4:   

> u=2

(max(s, 0,p)) clβ| ?

where c is the constant independent of a from Theorem 5.4. Now, using the estimate         

> 2(max(y 0,p)) c M <^^'^^

one can show that u exists and J(u) holds true, and the proofs of these facts in Q are of polynomial length in the length of a. Hence the induction axioms are replaced also by polynomially long sequences. D

# (d) Cut-Elimination and Herbrand's Theorem in Bounded Arithmetic 

There are two basic measures of the complexity of proofs: the length of proofs and the quantifier complexity of proofs. Cut-elimination and Herbrand's theorem implies that each first order tautology a has a proof whose quantifier complexity is not larger than the quantifier complexity of α. The cost for the reduction of the quantifier complexity is an increase in the size of the proof. This is the reason why this theorem is not provable even in IΣQ + Exp in full generality. Nevertheless there is a restricted version of this result which is provable in IΣQ + Exp and which has several applications. We shall prove it in this subsection. The proof will be just an analysis of a classical proof of cut-elimination. There is an alternative proof based on Hubert style calculi, but we shall use a variant of Gentzen's approach since it is simpler and more transparent. The transformations used in the proof will again be some simple manipulations with sequences, hence definable by ΣQ formulae. Thus we only have to estimate the size of constructed proofs. We shall use a slightly simplified version of Schwichtenberg's system [Schwichtenberg 77] and follow his proof of cut-elimination. The proofs will 372 V. Bounded Arithmetic 

be only briefly sketched; however we do not presuppose knowledge of proof theory. For more details the reader should consult [Takeuti 80]. It should be stressed here that the translations from this system to the system introduced in Chap. 0 and backwards are quite elementary. In particular (assuming ef-ficient coding, which was introduced in Sect. 3), it is possible to prove in 

IΣQ + # i that a sentence is provable in one system iff its translation is prov-able in the other one. We consider a system for first order logic. Its language consists of logical connectives &, V, -», quantifiers V, 3, variables, constants, function symbols and relation symbols. We do not distinguish equality as a special (or logical) relation symbol. In order to reduce the number of rules, and consequently the number of cases to be considered in the proofs, we allow negation only at atomic formulae. Thus, for a complex formula φ, the expression -*φ is an abbreviation for the equivalent formula obtained by applying De Morgan rules. For a similar reason we shall treat disjunction V differently too. We shall think of the formulae in a disjunction as forming a set rather than a sequence. In the arithmetization, all syntactical objects are represented as sequences (which in turn are represented as binary expansions). Thus what we mean is that: in proofs we allow the replacement of a disjunction by another one which has the same elements. For reasons of symmetry we shall consider conjunction &; to be also a set operation. When we write, for instance, that a formula φ has the form 7 V V >> w e mean that φ is the disjunction of a set {7l> >7m,V>l, . > n } , where 7 1 , . . . ,7m,^1, > Φn are atomic formulae, conjunctions or formulae starting with a quantifier, and we do not assume that the sets { 7 1 , . . . , 7m }> {Φl> > Φn} Άre disjoint and 7 is the disjunction of 71,.. .,7m, or 7 = 71 if m = 1, and φ is the disjunction of φ\, '. ., Φn, or 

φ = φ\ if n = 1. 

A proof is a sequence of formulae (usually called proof lines, or steps) 

where each formula is either a logical axiom or follows from preceding ones by a rule. There is one axiom schema in our system: (A) 7 V ^ V - ^ , and five rules: 

7 V φ(x) 

(V) —i /w x / x where the variable x is not free in 7, 7V(Vy)y>(y) 

7 V φ(τ) 

(3) —w /-1 \ / \ where r is a term free for x in (Cut)   

> 5. Interpret ability and Consistency 373

7 V φ, δV ->φ 

7VO The elements of the disjunctions 7 and δ axe called side formulae; 7 and δ

may consist of one formula or can even be void. In Cut, φ and -*φ are cut formulae. Let us point out that an important rule, the contraction rule, is only implicit in our system. A typical application of it, which is also needed in the proof of Herbrand's theorem, is the following: we derive by (3) 

> Ί

V(3x)φ(x)Vφ(τ) 

> Ί

V(3x)φ(x) '

In the lower sequent we do not repeat (3x)φ(x) once more, since our disjunc-tions are sets. Rule (W) is clearly redundant (and in contrast with (Cut) also harmless), but it is convenient to have it in the system. The fact that we define proofs to be sequences, not trees (the latter being common in proof theory), will be important later, when we shall consider systems weaker than IΣQ + Exp. 

We shall follow the notation of Chap. IV, Sect. 4 by writing Proof (d, 7) for the relation d is a proof of 7. By writing 7(0;) and then 7(τ), we denote the substitution of r for all free occurrences of x in 7. We shall use two measures of the complexity of proofs. The length, denoted lh(d), is the length of the sequence which codes the proof d. Of course, Ih is defined also for formulae and terms. We assume that the number of symbols used in the coding sequences is finite, thus the Gόdel number of a proof d is bounded by c"*w, for some constant c. Further we define, for a formula φ, rank(φ) as the number of connectives and quantifiers in φ plus 1. The cut-rank of a proof d, denoted by c-rank(d), is 0 if there is no cut in it; otherwise it is the maximum of the ranks of the cut formulae. 

5.13 Lemma (IΣo+Exp). (i) Suppose Proof (d, 7V (Vy)ψ(y)); then there exists 

d' such that Proof (d',7 V φ{x)) and c-rank(d') < c-rank(d), lh(d') < lh{d). 

(ii) If Proof (d{x),~f{x)), then for any term r, Proof (d(τ),η(τ)) and c-

rank{d{x)) = c-rank(d{τ)), lh{d{τ)) < lh(d(x)) * /Λ(τ). (iii) Suppose Proof(d,φo&cφι), then there exist d^,dχ such that 

Proof (di,φi) and c-rank\di) < c-rank(d), lh(di) < lh(d), for i = 0,1. (We take x and r in (i) and (ii) so that there are no clashes of variables.) Intuitively, the statements are clear; formally they can be proved by in-duction on the length of the proof. The proofs are easy, therefore we omit them. 

5 14 Reduction Lemma (IΣQ + Exp). Suppose d is a proof of Θ such that the last inference is a cut with a cut formula φ. Suppose that the part of the proof before the last inference has cut-rank less than rank(φ). Then there exists d!, a proof of Θ, such that c-rank(d f) < c-rank(d) and lh(dl) < ίft(d) 3.374 V. Bounded Arithmetic 

Proof. Let the last inference be 7 V φ, 6 V1. First suppose that φ is atomic. Then rank(φ) = 1, hence there is no other cut in the proof. The proof d contains a proof do of 7 V φ of rank 0. Consider how φ enters the proof do- If it is by (W) or as a side formula in (A), then we can omit it and derive 7 V δ by (W). If it is by (A) of the form 

σ V φ V -»<p, then we first derive σ V ί V ^ from δ V -up by weakening (W) and then use this proof instead of the proof line σVφV-*φ. We remove φ also from the proof lines below σVφV-*φ and extend them by forming disjunctions with δ. Thus we transform the proof of 7 V φ into a proof cf of 7 V δ. 

2. Suppose φ is (Ξa )^(a:). Our strategy is the same as above, but now 

φ can be introduced also by rule (3). (Note that φ can be introduced in d several times by (3); see the example above describing the contraction.) Consider such a derivation in d: σ V ψ(τ) 

where it is possible that the lower disjunction is just σ. In d we have a proof of £ V -itp, which is δ V (yx)(-*ψ(x)). By Lemma 5.13 (i) and (ii) we get a proof of δ V -*φ(τ). Now we apply cut to σ V φ{τ) and δ V -*ψ(τ) to get σVί. This cut has smaller rank, hence, after all these changes, we get a proof d1 of 7 V 6of a smaller rank. 3. If ψ is a conjunction <po &γ?i, then we do the same procedure as in 2 except that we now use Lemma 5.13 (iii). 4. By duality there are no other cases. If, for instance, φ is a disjunction, then -»φ is a conjunction. 5. It remains to compute the size of the transformed proof df. This will also be a proof that the above considerations can be carried out in IΣQ + Exp. 

The proof d! is constructed in such a way that for certain proof lines of d we add a proof of δ V -\φ or a proof of δ V ""^ί 7")? O Γ a proof of δ V ψ{ or just extend the disjunction by δ and remove φ from it. The largest increase in the size occurs when we need the proof of 6 V ~ i ^( r )i there we have the following upper bound from Lemma 5.13: 

lh(d) * lh(τ) < lh(d) 2 .

As there are at most lh(d) places where we do such extensions, the bound is 

lh(d) 3. D5.15 Lemma (IΣQ + Exp). Ή Proof (d,-y) and c-rank(d) > 0, then there exists 

d! such that Proof(d',j), c-ranJb(d') < c-rank(d) and /Λ(ίf) < 222 "" W.5. Interpret ability and Consistency 375 

Proof. Take the initial segment of proof d down to the first cut whose rank is equal to c-rank(d). Replace this subproof by a proof whose rank is less than 

c-rank(d) using Lemma 5.14. Repeat this procedure until no cut with rank equal to c-rank(d) remains. We start with a proof of length lh(d)] then in each step the length is raised to the 3, and there are at most lh(d) cuts that we have to eliminate. This gives Now we shall define several concepts of provability and consistency. The basic concepts have already been defined in Chap. Ill; we repeat their defi-nition for the reader's convenience. 

5.16 Definition. 

(0) d is a proof of x inT Proof τ(d,x) =df (3s < d)((Vi < lh( S))T{(s)i)t 

& Proof (d, ( 5 ) 0 &# . . . & (*)/ A ( β ) _i ->* *)) (1) Provability in the theory T Pr τ(x)= df (3d)Proof τ(d,x). 

(2) Restricted provability in the theory TRPr τ(k,x) =df (3d)(c-rank(d) < k & Proof τ(d, x)). 

(3) Cut-free provability in the theory T CFPrφ) =df RPr T(0,x). 

(4) Herbrand provability in the theory T HPrχ(x) =df "there exists a propositional proof of a disjunction of instances of the open part of 

He(/\ S -> x), for some finite S C Γ " , (see 0.18 for the definition of the function JTe). 376 V. Bounded Arithmetic 

(5) Consistency of the theory T Conχ =df 

(6) Restricted consistency of the theory T RCon τ(k) =df -*RPr τ(k,Q = 1). (7) Cut-free consistency of the theory T CFConγ =df 

(8) Herbrand consistency of the theory T HCon τ =df ^HPr τ(0 = T). (If we omit the subscript, it means proυability or consistency in pure logic.) The theories that we shall use will be either finite or have naturally defined polynomial time computable sets of axioms. For such theories T the predicate 

"φ is an axiom of T" can be expressed by a Σ\ formula. Then Proof γ(d,x) 

is also a Σ^ formula. Denote by Superexp an axiom saying that the ΣQ definable function 2* is total (see Definition IΠ.3.3). 

5.17 Theorem 

(i) IΣ 0 + Superexp h (Vx)(Pr*(x) -> CFPr (x)). 

(ii) For every Jb, IΣ 0 + Exp h (Vz)(£Pr #(fc,z) -> CFPr m{x)). Proof. Both statements follow immediately from Lemma 5.15. DLet us note that it is provable in IΣo + Exp that each propositional tau-tology has a cut-free proof. This can be shown by formalizing a completeness proof for the propositional fragment of our systemjconsisting of the schema (A) and rule (&). Let a propositional tautology φ be given. Construct a proof of φ by applying rule (&) backwards, i.e. we split conjunctions into parts un-til only disjunctions of atomic and negated atomic formulae are left (recall that negations can occur only at atomic formulae). We must show that these disjunctions are of the form (A) which just means that they are tautologies. This is true because rule (&) is sound also in the opposite direction. In each step of this construction we add two formulae of length at most lh(φ) and the construction has at most lh(φ) steps. Thus the total size of the proof is estimated from above by lh(φ) * 2lh ^φ\ Therefore, the construction can be carried out in IΣQ + Exp. 5. Interpretability and Consistency 377 

We conclude this subsection by showing that in IΣQ + Exp the cut-free provability and the Herbrand provability are equivalent. Then we derive corollaries about the provability of the consistency of Q. 

5.18 Middle Sequent Theorem. Let φ be a first order tautology in prenex normal form. Then there exists a proof doiφ which is cut-free and such that it can be divided into two parts d1 and dn such that d! is quantifier free, while 

dft contains only applications of the quantifier rules. The idea of the proof is simple. First one shows that axiom schema (A) and rule (W) can be restricted so that the newly introduced formulae must be quantifier-free. This increases the length of proofs only polynomially and no new cuts are needed. Now take such a cut-free proof of φ and switch quantifier and non-quantifier rules to obtain the required form of a proof. The only thing that we have to take care of are possible collisions of variables in rule (V). Therefore we must first transform the proof into a regular proof, which is a proof in which each application of rule (V) has its own variable that is generalized (eigenυaήable). To do such a renaming we have to transform the proof into tree form, which means that each premise is used only once. This may cause at most an exponential increase. Hence it is provable in IΣo + Exp 

that a formula φ has such a proof whenever it has a cut-free proof. Suppose such a proof d of φ is given. Let d! be the quantifier-free initial segment of the proof, let φl be its last formula. We may also suppose that each formula, except the last one, is a premise of some application of a rule in 

d. Hence φ is obtained from φ1 by successive applications of quantifier rules. In this situation we call φ1 the middle formula of d. (Usually in proof theory sequents are used instead of our use of disjunction of formulae; therefore the theorem is referred to as the Middle Sequent Theorem.) We shall show that 

φ1 can be easily transformed into a tautological Herbrand disjunction He{φ). 

Let φ be of the form )...(3a?n)(Vy nMa?i,yi,. .

We can transform any formula in a prenex normal form into such a form by adding dummy quantifiers. Then φ1 has the following form where ί* are some terms and zj are variables. Let / i , . . . , fn be new function symbols that will correspond to the universally quantified variables of φ. Now we follow the derivation of ψ from φ\ but instead of applying the rules, we substitute terms in φ1 as follows. If generalization (V) is applied to the variable 

Zj, then we substitute /j(^,.. .,£*•) for z%-. If the rule (Ξ) is used, then we 378 V. Bounded Arithmetic 

do nothing. In order to prove that the resulting disjunction is a Herbrand disjunction, we shall show two things: (i) t\ y..., tXj are changed (i.e. something is substituted in them) only after the generalization of z%>\ 

(ii) if z) = z kjt , then j = j ' and t[ = * * , . . . , * } = ή. 

Suppose (i) is false. Then some zf^ which is generalized before z%- must occur in t\, ..., t%-. Clearly z^ is not among z\, ..., 2J. Hence before z^ can be generalized, its occurrences in t\ ,..., t%> must be killed by existentially quantifying the terms in which it occurs. But this is a contradiction, since such existential quantifications are done only after the universal quantification of Let us prove (ii). If z%- occurs in different disjuncts, they must be first con-tracted into one before we can generalize (see the restriction on (V)). Two different disjuncts may become identical in the course of the derivation d! 1

after we replace some terms and free variables in them by bounded variables. However, different t\, ... ,tj and t\, ... ,t^ can be identified in such a way only after we quantify Zj (by the same argument as in (i)). Thus (ii) must be true. Now it is clear that the procedure changes φ1 gradually into a Herbrand disjunction. Condition (i) ensures that the terms have the required form, condition (ii) ensures that we replace the same variables by the same terms, hence we preserve the property of being a tautology. In each step the size of the disjunction increases quadratically (since we substitute some substrings of a string into itself), hence the size of the resulting He{ψ) can be estimated by The converse transformation, from He(φ) into a cut-free proof of φ, is also easy. Consider a formula φ of the same form as above. First eliminate the new function symbols / i , . . . , / n in Se(φ) by replacing maximal terms starting with such a function symbol by new variables. Let us denote the resulting formula by φ1. Since He{ψ) is a propositional tautology, so is φ1. Take some proof of φf] we have shown above that there is always one that is cut-free and at most exponentially long. Now we only have to see that we can apply the quantifier rules in a suitable order to suitable terms and variables to get 

φ. The following rules lead to a proof of φ: 

(1) Whenever we have a disjunct of the form           

> *1, i*j» Vj, Zj+1, yj+1 J>*n, yn),

apply (3) to the term ty, 5. Interpret ability and Consistency 379 

(2) if the above is not possible, then consider formulae of the form 

(β χj+l)(Vyj+l) (3z n)(Vy n) 

> >2/j+l> , ^ n , 2/n)

take one of them such that the term in He(φ) to which Zj corresponds is of maximal length, and generalize Zj. 

If we repeat this rule the disjunctions clearly converge to φ. Thus we only-have to show that the rule can be applied repeatedly, until the disjunction becomes φ. For (3) there are no restrictions, for (V) we have to show that Zj 

occurs in only one disjunct and it does not occur in ti, z i , . . . , fy-i, *j—i, tj of this disjunct. The last thing is clear, since zι,...,Zj correspond to the terms /l(*l)> j/j(*l> >fy)> hence /j(*i,... ,*;•) cannot be a subterm of any of the terms Now suppose (1) is not possible and suppose Zj occurs in another disjunct. Since (1) is not possible, the disjunct must have the following form The term corresponding to zfk is fk(t\i , t' k). If Zj occurred in t'-y, z\, ..., ^ , then the term corresponding to z' k would be longer than the one corre-sponding to Zj. Hence we can have only ZJ = z' k. But then /j(tχ,... ,tj) =

fkit'if- >*jk)i ^ u s i = & >a n < i *1 = *iί »*i = t'k Hence it is the same formula. We have proved the following theorem. 

5.19 Theorem. It is provable in IΣo + Exp that: a formula has a cut-free proof if and only if it has a Herbrand proof. In symbols 

IΣ 0 + Exp h (Vx)(CFPr*(x) s= HPr m(x)) .

By formalizing a classical proof of the consistency of arithmetic we get the following result. 

5.20 Theorem. 

(i) IΣQ + Superexp h Conj Σo .

(ϋ) IΣQ + Exp h HCon mQ and for every jfe, IΣQ + Exp h RCon mQ(k). Proof. First we transform Q into an open theory Q1: we delete axiom (Q8) defining <, add the predecessor function and replace axiom (Q3) by an open 380 V. Bounded Arithmetic 

axiom. Assume -ιHCon{Q'), hence we have some propositional tautology 

Ht(pQ'), which is a disjunction of substitution instances of -»Q'. But this is impossible, since in IΣQ + Exp we can define the truth for open formulae. Thus we have IΣQ + Exp h HCOΠQ,. 

To prove (i), first reduce the consistency of IΣQ to the consistency of Q1

using the interpretations of IΣQ in Q (Theorem 5.12) and Q in Q1. Then apply cut-elimination in IΣQ + Superexp (Theorem 5.17 (i)), and the equivalence of the cut-free and Herbrand consistency (Theorem 5.19). 

RConQpc) is reduced to RConQ,(m), for some ra, by the interpretation of 

Q in Q1. Applying cut elimination (Theorem 5.17 (ii)), this is further reduced to CFCOΠQ, and by Theorem 5.19 to HCOUQ,. Thus we get    

> IΣQ + Exp )r RCOUQQS) .

Now ΛCOΠQ(O) is just CFCon^ which is equivalent to HCOΠQ in IΣQ + Exp. 

This shows the rest of (ii). D

# (e) The JTi Theorems of IΣQ + Exp 

In this subsection we prove a theorem of A. Wilkie which characterizes Πι 

sentences provable in IΣQ + Exp as the Π\ sentences interpret able in Q and consider some related problems. We start with some lemmas. Recall that 

x denotes the formalized numeral function and that we are using dyadic 

numerals of Sect. 3. 

5.21 Lemma. For every inductive formula I(x) in Q, there exists k such that 

Proof. Recall that a numeral n, for n > 0, is constructed as follows. We take no,... ,nj. such that no = l,nj. = n and n t _χ = Ln, /2j. Then no is 1 and, for i = 1,. ..,fc, n, is 2 * ή\ _ i , if n, = 2n t _i (S*n f _i) + Ϊ , ifn t = 2 n t V ι + l ; where T is 5(0) and 2 is (5(0) + 5(U)). For a given inductive J(z), take some 

J(x) which is a subcut of / and J(x) -+ J(2 * x), provably in Q. Then to show J(n) we need at most 2fc + 1 proof steps. The formulae that we use are of polynomial size in the length of n, hence the whole proof has polynomial size. Therefore 5^ can formalize this proof. Note that the rank of formulae used in the proof does not depend on n, hence is determined only by J. D5. Interpret ability and Consistency 381 

5.22 Lemma. There exists k such that for every two terms t(x\^. .. , x n ) and   

> s(xι,...,x n)in LQ:

S\ h (Vxi,..., xn)((K χl>-.., xn) = s ( z i , . . . , z n ) -> 

£Pr£(fc, t(ii,..., xn) = s(xι ,..., in))) 

k(t(xι,...,x n) φ s(xι,...,x n) -* 

(J (*1> »*n) 7* θ(iχ,.. ., in)))) . In the following proof and the next lemma we shall denote the function as-signing the dyadic numeral to a number also by numeral{x)\ the dot notation would be rather confusing in some formulae. 

Proof. Let I(x) be a cut in Q on which the operations + and * have the properties of ring operations. We can use this cut to construct proofs of instances of associativity, commutativity, etc. for numerals. Namely, by the lemma above, we first show that the numerals in question belong to I and then we apply the law in I. This cut will be the only factor that influences the cut-rank k of the resulting proof. Now the sentence can be easily proved in S% by induction. We only have to transform it into a Σ\ formula, i.e. we have to find a polynomial bound to the length of the proof of t ( i χ , . . . , i n ) = s ( i i , . . . , i n ) . By Lemma 5.21 the length of a proof of / ( i ) is polynomial in the length of x. Next we find polynomial proofs of (e.l) S(numeral(xι)) = numeral(S(xι)) ,(e.2) numeral(xι) + numeτal(x2) = numeral(x\ + £2) > (e.3) numeral(xι) * numeτal(x2) = numeral(xι * X2) .Perhaps the best way to see a polynomial bound to these statements is the following. First construct proofs of i t = t{ where t{ are terms of the form where 2 denotes 2 * (2 * * 2)). Think of ti as a modified numeral. Then  

> ktime*

follow the standard algorithms for + and * to obtain the proofs of (e.1-3) for the modified numerals. Finally transform the modified numerals back into original numeral(S{x\)), numeral{x\+X2) and numeral(x\*X2) respectively. As is easily shown by induction, the maximal of these three bounds (the 382 V. Bounded Arithmetic 

bound for the length of the proof of (e.3) is asymptotically maximal) is a bound to the proof of the equality of general terms. To prove the inequality, take a suitable term w, prove t(il,..., i n ) + S(u) = s(xι ,..., i n ) ,  

> or

θ(il,..., i n ) + S(u) = t(ii, ..., i n ) , and use the fact that 

Q h !(*)&I(y) '-> x + S(y) φx. •5.23 Lemma. There exists k such that 

Si h (Vy)ΛPr^(fc, (Vx)(x < niimertiZ #(y + 1) = (x < nuraerα/ (y) V 

x = numeral*(y + 1)))) . Proo/. We construct a cut J in Q such that (e.4) Q \- (V*. *)(/(«) -»(* < S(*) s (x < z V x = S(z)))). 

First take 3 defined by 

J(x) = df O + x = xkQtz)(S(z) + x = S(z + x)) .One can easily show that J is inductive. Now take / to be a subcut of J and verify (e.4). We shall work in S | . Let a number y be given. By Lemma 5.21 we have Q h 1(numeral {y)), hence by (e.4) 

Q h x < S(numeral(y)) = (x < numeral(y) Vx = S(numeral(y))) .By Lemma 5.22 Q h numeral(y + 1) = S(numeral(y)). Thus Q proves 

(\fx)(x < numeral(y -f 1) = (x < numeral(y) Vi = numeral(y + 1))) . All that we have used were proofs of bounded cut-rank. DFor the following lemma, we shall fix some translation of Li into Lo which determines an interpretation of BASIC on some cut in Q. Such a translation exists, since IΣo + Ω\ is interpretable in Q by Theorem 5.12. We shall say that a formula φ of LQ is essentially Σ\ (resp. Π\ ), if it is the translation of a Σ\ (resp. Π\) formula of L 25. Interpretability and Consistency 383 

5.24 Lemma (formalized Σ completeness of Q). 

(i) Let φ(x, y) be a bounded formula in £Q. Then there exists k such that 

IΣ 0 + Exp h (Vx)((3y)ψ(x,y) -» RPr Q(k,(3y)ψ(x,y))). 

(ii) Let φ(x,y) be essentially Σ\. Then there exists k such that 

S\ h (Vx)((3y)ψ(x,y) Proof. First we observe that in both cases it suffices to prove only 

(Vx)(ψ(x,y)-+RPr Q(k,ψ(x,y))), 

since (Ξy)^(i, y) will follow by an application of the rule (Ξ). (i) The task of proving φ(x,y) is similar to the task of deciding its truth: we shall prove φ(x,y) by proving numerical instances of the open part of φ. 

Thus we can bound the size of the numerals needed in this proof in the same way as in the proof of Theorem 5.4. The numerical instances of the open part of φ follow from the numerical instances of atomic and negated atomic subformulae. The existence of bounded cut-rank proofs of atomic sentences with = and their negations follows from Lemma 5.22. The atomic sentences with < and their negations are reduced to atomic sentences with = in the same way as the negations of atomic sentences with = had been. We must be a little careful when pasting the proofs of the numerical instances into a proof of a bounded sentence, since we need a proof of 

bounded cut-rank. A sentence of the form (Ξy < t)a(y) follows from some α(n), where n is less than or equal to the value of t. A proof of (Vy < t)a(y) 

is constructed from the proofs of α(0), α ( l ) , . . . , <*(m), where m is the value of t, as follows. We prove successively (Vy < ή)α(y), for n = 0 , . . . , m. For 

n = 0 it is an immediate consequence of α(0); to obtain it for n + 1 from a proof for n, use Lemma 5.23 and α(n + 1) Finally use Lemma 5.22 to show (ii) The proof of (ii) is only a modification of the proof of (i) where we replace bounded by sharply bounded. We also need an extension of Lemma 5.23 to ^2? instead of Lo, and BASIC\ instead of Q. Again the proof is essentially the same: translate the natural polynomial time algorithms for the evaluation of terms in £2 m t o a proof using equalities which hold on a suitable cut in 

BASIC. We omit the details. D5.25 Lemma. Let φ(x) be a bounded formula and suppose + Exp h (Wx)φ(x). 384 V. Bounded Arithmetic 

Then there exists k such that 

Proof. Suppose IΣo does not prove (Vz)((3y)(y = 2jp — • φ(x))> *° Γ a n y *• Then, by compactness, IΣo + {(3y)(y = 2£)&i^(c) | fc G iV} (c a new constant) is consistent. Take a model M of this theory and an initial segment of it 

K = {a G M I (5* G ΛΓ)(M N α < 2%)} .Then A T is a model of IΣo + Exp, but K 1= -vψ(c), because φ is bounded. D Now we are ready for the theorems. 

5.26 Theorem. Let φ(x) be a bounded formula. Then the following are equiv-alent: (1) There exists a cut I(x) in Q such that (2) There exists an interpretation of Q + (Wx)φ(x) in Q. 

(3) IΣ 0 + Exp h (Vx)φ(x). Proof. (1) = >- (2) follows from the existence of shortenings of cuts closed under + and *. (2) =*• (1) Let ί be an interpretation of Q + (Vx)φ(x) in Q. We shall construct a cut I(x) in IΣo such that This is sufficient, since IΣo has an interpretation in Q determined by a cut. The cut I(x) is defined by the formalization of the following formula: "There exists an isomorphism of the initial segment [0, x] onto an initial segment in the sense of interpretation t". Here we take intervals as structures with =, <, and +, * as ternary relations. An isomorphism is a number which codes a sequence of pairs. We leave it to the reader to write down an explicit formula for / and check that it is a cut in IΣo Let us only note that the extension of an isomorphism with domain [0, x] to an isomorphism with domain [0, S(x)] 

is obtained by adding to it a pair (S(x), z), where z is the t, successor of the image of x. Such an extension of a sequence is possible in IΣo (birt not in 

Q). Now the fact that (Wx)φ(x) holds in the sense of i is transferred by the isomorphisms onto /. (1) => (3) Suppose 5. Interpretability and Consistency 385 

By Lemma 5.21 for some constant k. Hence 

IΣ 0 + Exp h (Vx)RPr Q(k, φ{x)) .By Theorem 5.20, IΣQ + Exp proves the consistency of Q with respect to proofs of cut-rank fc. Thus we have 

IΣ 0 + Exp h (Vx)-, 

By Lemma 5.24 (i) 

IΣ 0 + Exp h Qtx)(-*φ(x 

for some ra. We can assume that k = ra (otherwise take max(fc, m) instead of fc and m). Hence (3) follows from the last two statements. (3) =£. (1) Suppose IΣo + Exp h (\/x)φ(x). By the lemma above we have some k such that Take cuts /, J in Q such that J determines an interpretation of IΣo in Q

and J is a subcut of J such that Then we have Q h (Vaf)(/(«) -+ ^(β)). •5.27 Theorem. Let φ{x) be a bounded formula in LQ. Then the following are equivalent: (1) IΣ 0 + Exp h (Vx)φ(x). 

(2) For some fc _

Sl\-C*x)RPr Q(k,φ(x)). 

If φ(x) is the translation of a Π\ formula ψ{x) into LQ, then (1) and (2) are equivalent to: (3) For some h

Sl + RCon φQ(k)\-(yx)φ(x). 

Proof. (1) => (2) Suppose IΣQ + Exp h (Vx)φ(x), φ bounded. Then by Theorem 5.26 we have Q h (Vx)(I(x) -> φ(x)) for some cut / in Q. By ΣΊ completeness 386 V. Bounded Arithmetic 

for some j . By Lemma 5.21 for some m. Take k to be the maximum of j and m, then we have (2). (2) => (1) By definition 

(e.5) Si + RCon Q(k) h (to)ΛPr£(fc, φ(x)) 

By Theorem 5.20, RCOΠQ(TC) is provable in IΣQ + -Saψ, thus (e.5) is provable in IΣQ + Exp. Since we assume (2), we have 

IΣ 0 + Exp h (Vx)-*RPr Q(k, ^φ(x)) .By Lemma 5.24 (i) 

IΣ 0 + Exp h ( V a : ) ( ϊ Hence (2) implies (1). Now assume that ψ is the translation of a ϋ\ formula φ(x) into Lo (2) => (3) By Lemma 5.24 (ii) we have 

S\ h (V*)(-ΛPr£(I, -i^(i)) - ^ ( x ) ) . Then using (e.5) we get 

Sl+RCon mQ(k)\-(Vx)φ(x). 

from (2). But y?(a;) is equivalent to ψ(x) in 5 | , thus we have (3). (3) => (1) This is because IΣo + Exp "contains" S% and proves RConq(k). 

## D

We would like to axiomatize Π\ consequences of IΣQ + Exp over, say, 5^ (put otherwise, we want to find some nice basis). The equivalence of (1) with (3) gives only a partial answer: since RCon\{k) can be written as a formula of the form (Vx)ψ(x) with φ in J7j, the set of sentences RCon\{k), k = 0,1,... axiomatizes the Vϋf consequences of IΣQ + Exp. 

## (f) Incompleteness Theorems 

It would be paradoxical if the incompleteness theorems did not hold in weak systems. Of course formalization of syntax in weaker theories is a more difficult task, therefore we cannot apply classical proofs of the second Gδdel incompleteness theorem quite directly. It turns out that the second 5. Interpretability and Consistency 387 

incompleteness theorem can be even strengthened. A typical example is the unprovability of the consistency of Q in IΣQ + Exp. The results presented in this subsection will be corollaries of the theorems proved above and of the following theorem. Note that in the following theorem (i) holds for every finitely axiomatized sequential theory containing Q. We shall not prove this general theorem here. For finite theories in the language of arithmetic extending IΣΊ, statement (i) follows from Theorem 3.20(1) Chap. III. Statement (ii) generalizes Theo-rem 3.11, Chap. Ill, to weaker theories; however the assumption about the axiomatizability is stronger here. It is possible to use here the same assump-tion about the axiomatizability as in Chap. HI, but we shall not prove this strengthening. Recall that RCon^(k) is 

(Vz)(I(z)kc-rank(z) < k-> -.Proo/^z, 0 =

5.28 Theorem, (i) For every k there exists a cut I in Q such that (ii) Let T be a consistent theory containing Q and having a Σ\ axiomati-zation. Then for every cut J in T there exists m such that 

Proof, (i) By Theorem 5.20 (ii), for every k    

> IΣ 0+Exp hRCon %Q(k) .

By Theorem 5.26, this implies the first statement. (ii) The proof of this statement will be similar to the proof of Theorem 3.11, Chap. III. Roughly speaking, we only have to take m sufficiently large. Since this result plays a key role in the rest of this section, we shall prove it in detail. Because of the shortening techniques, we may suppose that J has some additional properties. Thus we shall assume that J is a cut in Q and it determines an interpretation of S\ in Q. In particular, it is provable in Q, hence also in T, that for any two sequences in J, their concatenation lies also in J. 

We would like to use the provability conditions of 2.16, Chap. Ill, for 

RPr j (m, x). We shall prove the first two. The third one, which is formalized 

Modus Ponens, is clearly false, since Modus Ponens increases the cut-rank. Thus we shall first take a suitable m, and then we shall follow the usual proof 388 V. Bounded Arithmetic 

of the second incompleteness theorem and check that the third condition is actually applied only to formulae of rank at most m. We shall divide the proof into several claims. Claim 1. For every sentence ψ, if T h φ, then T h CFPrγ(φ). Proof. Suppose T h φ. By cut-elimination we have a cut-free proof of φ

in T. By the ^-completeness of Q, Q h CFPrj,(φ). Since J determines an interpretation of Q in T, we get the conclusion of the claim. DClaim 2. There exists k such that 

T h RPr' TJ(x, y) -+ RPr mτJ(k,RPrγ(x,y)) .

Proof. Let us first write down RPrlj?(x,y) more explicitly: (3d)( J(d) & J(x) & J(y) & c-rαnib(d) < x k Proof τ(d, y)) .By Lemma 5.24, for some k\ S\ h rαnJb(d) < x & Proofed, y) -> By Lemma 5.21, for some 5^ h RPr Q(k 2, J(d) & J(x) k J(y)). To obtain RPrΐp(x,y) we need only the rules for & and 3 which do not increase the cut-rank. Hence for k = max(fci, k^) S\ h RPr mτ(x,y) -Here we can replace Q by T, since Q is contained in T. As T h (S2)* 7, w e S e t 

T h (RPr' T(x, y) - , ΛPr^(fc, Λ P r ^ ( i f y))) J ,which is in fact the statement of the claim. DBy 2.1, Chap. Ill, we have some δ(x) such that T h δ(x) = J ϊ5. Interpret ability and Consistency 389 

δ(x) is the numeral of the formula δ(numeral(x)). Now we can choose m. Let m be such that (1) m > fc, where k is from Claim 2;   

> \£) in ^_ rcLTbK\^iLJLrrp \x^ y))Ί

(3) m > rank(δ(x)). 

Note that we thus have also m > rank(RPrγ(m,y)) and m > Let us define also 

Δ= df δ(fn); <*=df 

Claim 3 . Γ h 4 = - I Λ P Γ J ^ Z ) . 

Proof. By definition we have T h ί(m) = -i. Thus we only need which follows from the ^-completeness of Q, hence of T. D

Claim 4. -.(T h 4 ) . Proo/. Suppose Γ h A Then, by Claim 1, T h CPPrJ^ίZ), whence T h J2Prj/(m, Z\). By Claim 3 this means that T is inconsistent, which is a con-tradiction. D

Claim 5. T h 

Proof. If α and -ior are derivable using proofs of cut-rank of at most m, then so are αVO = T and - α V 0 = T (add 0 = 1 to each proof line as a side formula). Since m > rank(RPrj?(x,y)) = rαnfc(α), we get a proof of 0 = 1 by taking the concatenation of these proofs and applying the cut rule. The closure properties of J ensure that such a proof will be also in J. D

Claim 6. T h RPr^ J(m yΔ) -* ΛPrJ J (m,α). 

Proof. By Claim 2     

> T\~ RPrm (τfϊi Δ) —•RPrrp ('

By the definition of a and ^-completeness 390 V. Bounded Arithmetic 

Claim 7. T h RPr% J(rn,Δ) -

Proof. By Claim 3 and the definition of α, T h Z\ -> -«α. By Claim 1, this implies T h JZPr5/(m,^ — •:= ΐα). If we have proofs of Δ and Δ —» -ια of cut-rank m, we can easily combine them into a proof of cut-rank m of -iα, because m > rank(Δ). Again, the closure properties of J ensure that this proof is in J too. ΠNow we can finish the proof of part (ii) of the theorem. By Claims 3, 6, 7and 5, we have in T 

^Δ -> RPr^ J(m,~A) -> (RPrjί(m,a)itRPrtf(m,=&)) -> ^RConγ(m) ,

i.e. T h ΛCθ7iy J(m) — > ^\. Hence, by Claim 4, RConγ(m) is not provable in T. D

5.29 Corollary. Cong is not provable in IΣo + Exp. Proof. By the theorem above, Q does not prove COΠQ for any cut J. Hence by Theorem 5.26 IΣQ + Exp does not prove Con%. D

5.30 Corollary. Cut elimination (unrestricted), and Herbrand's Theorem are not provable in IΣo + Exp. Proof. By Theorem 5.20 (ii) IΣo + Exp proves cut-free and Herbrand consistency of Q. If we had cut-elimination or Herbrand's Theorem in IΣo +

Exp, we could reduce the ordinary consistency of Q to the restricted one. D 

5.31 Theorem. IΣo + Exp + Con* Σ does not prove 

Proof Let J be the cut in IΣo + Exp defined by We shall show that 

(f .1) IΣo + Exp h $

Suppose not. Let us work in IΣQ + Exp, let d be a proof of a contradiction in J . Then d has cut-rank at most lh(d). We have 

> o

lh(d) < 9 o

since d must be nonstandard and d is exponentially larger than lh(d); hence such a number exists. Thus we can apply cut elimination to obtain a cut-free 5. Interpret ability and Consistency 391 

proof of a contradiction in Q (apply Lemma 5.15 ZΛ(c?)-times and use the inequality But this is not possible by 5.20 (ii). Now suppose the statement of the theorem is false. Thus 

IΣ 0 + Exp h Con IΣo -

Since COΠJ ΣQ and Cong are equivalent in IΣo + Exp, we have       

> +Exp hCon Q-> Con} Σo +Eχp .

Using an obvious Lemma 5.25, we can deduce that provably in IΣQ + Exp, aproof d of a contradiction in IΣo + Exp can be transformed into a proof df

of a contradiction in Q such that df < 2^ for a suitable standard k. Let / be a subcut of J such that 

IΣ 0 + Exp h I(x) -> J(2|). Hence a proof d of a contradiction in IΣo + Exp such that d is in J can be transformed into a proof df of a contradiction in Q such that dl is in J. Thus, by (f.l) no such proof can exist, i.e. IΣo + Exp proves Corij Σ +E xp But this is in contradiction to Theorem 5.28 (ii). D5.32 Corollary. IΣo + Exp is not interpretable in /ΣΌ 

Proof. Suppose IΣo + Exp is interpretable in JΣΌ It is well-known that if T is interpretable in 5 and S is consistent, then T is consistent too. This simple theorem can be easily formalized in IΣo + Exp, if T is finitely axiomatized. Since IΣo + Exp is finitely axiomatizable (Theorem 57o), as one can check provably in IΣo + Exp, we get       

> IΣ 0+ Exp hCon} Σo -+ Con mlΣo+Eχp ,

which contradicts Theorem 5.31. D5.33 Theorem. For every k there exists m such that RCon\{m) is not provable in IΣo + Ω n + RCoriQ(k) for any n. 

Proof. We shall use Theorem 5.28 again. Let J be a cut in Q such that 

Q\- $( 392 V. Bounded Arithmetic 

We can suppose that / determines an interpretation of IΣQ . Let J be a subcut of / such that Q h J ( z ) ^ J ( 2 2 * ) . We know that, for some m, Q+^RCon^lm) is consistent. Let M be a model of this theory. Let K be its initial segment defined by 

K = {a£M; (36 € J M)(3t € N)(a < ω<(ό))} .First we shall show that K is closed under all functions ωn. Let a £ K] 

without loss of generality we can suppose that a is nonstandard. Then, for some nonstandard 6 E J , a < u>j(δ). Let n be given. Then To prove the last inequality, use induction on j to show that for every sufficiently large x (hence for every nonstandard z). Now we need that K C IM. This follows from the definition of the cuts and from the following inequality, which is also easily provable by induction on j : 

2ωj( x) ^ 2 , for x sufficiently large. Since K is contained in IM, which is a model of JΣΌ, if is a model of IΣo+ω n,

for every n. Since Q h RCon^(k) and M t= -yRCon mJ(jrϊ), we have     

> tf NRCon Q(k) & -.

which finishes the proof. DThis theorem gives us another piece of important information about consequences of IΣQ + Exp: they are not "finitely based". Further we have this consequence. 5.34 Corollary. IΣQ + Exp is not Πι conservative over IΣQ + {Ω n; n E N}. 

In fact this is all that we know about Π\ conservativity between systems of bounded arithmetic. In particular it seems plausible that JΣΌ + Ω\ is not Πι 

conservative over /ΣΌ, but we cannot even prove that IΣQ + {Ω n\ n E N} is not Π\ conservative over JΣΌ. A Πι sentence which might separate JΣΌ + Ω\ 

from JΣΌ is the so-called Bertrand's postulate. It is the theorem (due to Sylvester) which says that there is a prime between n and 2n, for every n. 5. Interpretability and Consistency 393 

This sentence is provable in IΣQ + β i , but no proof of it has been found in 

IΣQ. Whether such a proof exists is an important open problem. 

# (g) On the Limited Use of Exponentiation 

If we are interested only in Π\ sentences, then it seems that all such sen-tences which are also truly mathematical results are provable in IΣQ + Exp 

(we consider sentences like Con(Q) to be uninteresting for an ordinary math-ematician). In fact the proofs use exponentiation at most once. This means that for instance if we construct some graph, we may consider the set of all graphs of a given size, but usually we do not consider the set of subsets, etc. Put otherwise, we use the finite power set operation only once. This phe-nomenon is worthwhile to formalize, but it cannot be done directly in first order logic. In first order theory we have either to accept axiom Exp, and then we have also all finite iterations of 2*, or we do not have exponentiation at all. A possible approach is to use higher order bounded arithmetics. We shall use a different approach. Our aim is, roughly speaking, to show that there is an infinite hierarchy according to the number of applications of the exponentiation axiom. So what does it really mean that (yx)φ(x) is provable using exponentiation only once? This means that we prove φ{x) assuming that 2X exists; formally 

IΣ 0 + ΩX h (V*)((3y)(y = 2*) -> φ(x)). 

It is convenient to consider IΣQ + Ω\ instead of IΣQ, since thus we obtain a concept which is more robust: in IΣQ + ί2i, 2* exists iff 2X exists, etc. There is an equivalent and shorter way to express that (\/x)φ(x) is provable using exponentiation only once, which is 

IΣ 0 + Ω 1\-(Vx)φ(\x\). 

Similarly, k applications correspond to the provability of (Vx)φ(\xy< *'), where 

\x\( k) denotes the k times iterated function x H+ \X\. 

Finally let us also mention a model theoretical characterization of prov-ability using exponentiation only once. Let I(x) be defined by 

I(x)= df (3y)(y = 2*). 

Let K be the class of models of the form 

K = {a e M; M 1= IΣ 0 + Ω1 hM N /(α)} ,

with the operations inherited from M. Then the sentences in question are just the sentences true in all models of K. 394 V. Bounded Arithmetic 

Let φ(x, y) be a bounded formula such that for every m 

IΣ 0 + Ω τ\- (Vy)φ(m,y) = RCon %Q(m) .

5.35 Lemma. For every k there exists m such that (Vy)^>(m, \y\( k') is not provable in IΣQ + Ω\. Proof. Let I(x) be a cut in Q such that I determines an interpretation of 

+ Ω\. Let J(x) be a subcut of I(x) such that By Theorem 5.28, there exists m such that Now suppose that (Vy)φ(nϊ, |yp ') is provable in II?o + Ω\. Then hence, by the construction of J, 

Q\-(0/y)Φ(rn,y)) J,

which is a contradiction. D

5.36 Theorem. For every k there exists a bounded formula φ(x) such that 

but 

Proof. Let m be such that (Vy)^(^ϊ, | y | ^ ) is not provable in IΣQ + Ω\. Since ΛCΌnQ(m), i.e. (Vy)ψ(m, y), is provable in JJCo + -Ssj>, it must be provable using exponentiation a finite number of times, see Lemma 5.25. Thus, for some n, Hence for some i, k < i < n, 5. Interpret ability and Consistency 395 

and Take φ{x) to be φ(m, |a?|(*"^), then the theorem follows. DThe instances of the schema PHPΣQ are Πι and they are provable using one exponentiation. Actually, most of the proofs that require exponentiation can be reduced to PHPΣo. Still it seems that PHPΣo is not sufficient to prove all sentences derivable using one exponentiation. We are not able to derive PHPΣo in IΣQ + ί?i, so it is possible that some instances could be used as more natural formulae in the theorem above for k = 0. However we do not know which. The point is that the known mathematical statements which can be derived using PHPΣo c&n be derived also from a weaker version of PHP which is already provable in IΣQ + Ω\ (Bertrand's postulate is an example). The related problems of whether IΣQ+Ω{ is Π\ conservative over IΣo+Ωj, 

for j < i, are still open. They are typical in the sense that they are related to open problems in complexity theory. For instance, the question whether 

IΣQ + Ω\ is Π\ conservative over IΣQ seems to be formally related to the open problem whether PH = LinH (though we are not able to prove any relation). New techniques will need to be developed in order to solve such problems. Solving such problems in Bounded Arithmetic might be the first step in solving the corresponding persistent problems in complexity theory.
