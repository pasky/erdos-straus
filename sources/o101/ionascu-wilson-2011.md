## Content from https://csuepress.columbusstate.edu/cgi/viewcontent.cgi?article=1846&context=bibliography_faculty

Title: On the Erdos-Straus Conjecture

URL Source: https://csuepress.columbusstate.edu/cgi/viewcontent.cgi?article=1846&context=bibliography_faculty

Published Time: Fri, 02 Jul 2021 17:57:56 GMT

Number of Pages: 10

Markdown Content:
# ON THE ERD ¨OS-STRAUS CONJECTURE                     

> EUGEN J. IONASCU and ANDREW WILSON Paul Erd¨ os conjectured that for every n∈N,n≥2, there exist a,b,cnatural numbers, not necessarily distinct, so that 4
> n=1
> a+1
> b+1
> c(see [3]). In this paper we prove an extension of Mordell’s theorem and formulate a conjecture which is stronger than Erd¨ os’ conjecture.
> AMS 2010 Subject Classification: 11A07, 11A41, 11A51.
> Key words: Egyptian fractions, integers, prime numbers.

1. INTRODUCTION 

The subject of Egyptian fractions (fractions with numerator equal to one and a positive integer as its denominator) has incited the minds of many people going back for more than three millennia and continues to interest mathemati-cians to this day. For instance, the table of decompositions of fractions 22k+1 

as a sum of two, three, or four unit fractions found in the Rhind papyrus has been the matter of wonder and stirred controversy for some time between the historians. Recently, in [1], the author proposes a definite answer and a full explanation of the way the decompositions were produced. Our interest in this subject started with finding decompositions with only a few unit fractions. It is known that every positive rational number can be written as a finite sum of different unit fractions. One can verify this by using the so called Fibonacci method and the formula 1 

> n

= 1 

> n+1

+ 1 

> n(n+1)

, n ∈ N. For more than three fourths of the natural numbers n, 4 

> n

can be written as sum of only two unit fractions: the even numbers, and the odd numbers n of the form 

n = 4 k − 1, via the identities 22k−1 = 1 

> k

+ 1 

> k(2 k−1)

, and 44k−1 = 1 

> k

+ 1 

> k(4 k−1)

,

k ∈ N. It is clear that if we want to write 4

n = 1

a + 1

b + 1

c , a, b, c ∈ N,

we can just look at primes n. However, just as a curiosity, for n = 2009 = 72(41) (multiple of four plus one) one needs still two unit fractions, and there are only three such representations 42009 = 1504 + 1144648 = 1574 + 14018 = 1588 + 13444 .     

> REV. ROUMAINE MATH. PURES APPL., 56 (2011), 1, 21–30 22 Eugen J. Ionascu and Andrew Wilson 2

This follows from the following characterization theorem which is well known (see [2] and [4]). 

Theorem 1. Let m and n two coprime positive integers. Then 

mn = 1

a + 1

b

for some positive integers a and b, if and only if there exist positive integers 

x and y such that 

(i) xy divides n, and 

(ii) x + y ≡ 0 (mod m).

In what follows we will refer to the equality (1) 4

n = 1

a + 1

b + 1

c .

and say that n has a representation as in (1), or that (1) has a solution , if there exist a, b, c (a ≤ b ≤ c) natural numbers, not necessarily different satisfying (1). Since 4 

> n

> 1 

> a

, the smallest possible value of a is n/ 4. The biggest possible value of a is  3n 

> 4

, for instance 49 = 16 + 16 + 19 .If n = 4 k + 1, k ∈ N, then we can try to use the smallest value first for 

a, i.e., a = k + 1: (2) 44k + 1 = 1

k + 1 + 3(k + 1)(4 k + 1) .

Now, if the second term in the right hand side of (2) could be written as a sum of two unit fractions we would be done. This is not quite how the things are in general, but if we analyze the cases k = 3 l + r with r ∈ { 0, 1, 2},

l ≥ 0, l ∈ Z, we see that there is only one excepted case in which we get stuck: 

k = 3 l. This because Theorem 1 can be used in one situation: k = 3 l + 1 implies 1 + (3 l + 1 + 1) ≡ 0 (mod 3). On the other hand, if k = 3 l + 2 we get ( k + 1) = (3 l + 2) + 1 = 3( l + 1) ≥ 3 and the second term is already a unit fraction. In order to simplify the statements of some of the facts in what follows we will introduce a notation. For every i ∈ N let Ci be defined by 

Ci := 

{

n | (1) has a solution with a ≤ n + 4 i − 14

}

.

It is clear that Ci ⊂ C i+1 and then Erd¨ os-Straus’ conjecture is equivalent to ⋃

> i∈N

Ci = N. Thus we obtained a pretty simple fact about the Diophantine equation (1): 

Proposition 1. The equation (1) has at least one solution for every prime number n, except possibly for those primes of the form n ≡ 1 (mod 12) .3 On the Erd¨ os-Straus conjecture 23 

Moreover, 

N \ C 1 ⊂ { n | n ≡ 1 (mod 12) }.

We observe that 12 = 2 2(3), a product of a combination of the first two primes. The first prime that is excluded in this proposition is 13. The equality (2) becomes (3) 412 l + 1 = 13l + 1 + 3(3 l + 1)(12 l + 1) .

At this point we can do another analysis modulo any other number as long we can reduce the number of possible situations for which we cannot say anything about the decomposition as in (1). It is easy to see that 3 l + 1 is even if l is odd and then Theorem 1 can be used easily with x = 1 and y = 2. This means that we have in fact an improvement of Proposition 1: 

Proposition 2. The equation (1) has at least one solution for every prime number n, except possibly for those primes of the form n ≡ 1 (mod 24) .In fact, 

N \ C 1 ⊂ { n | n ≡ 1 (mod 24) }.

Let us observe that 24 + 1 = 5 2, 48 + 1 = 7 2, which pushes the first prime excluded by this last result to 73. Quite a bit of progress if we think in terms of the primes in between that have been taken care off, almost by miracle. If n = 24 k + 1, then the smallest possible value for a is 6 k + 1 and at this point let us try now the possibility that a = 6 k + 2 = n+7 4 ,(4) 424 k + 1 = 16k + 2 + 72(3 k + 1)(24 k + 1) , k ∈ N.

In the right hand side of (4), the second term has a bigger numerator but the denominator has now at least three factors. This increases the chances that Theorem 1 can be applied and turn that term into a sum of only two unit fractions. Indeed, for k = 7 l + r, we get that n = 24 k + 1 ≡ 0 (mod 7) if r = 2, 2(3 k + 1) + 1 ≡ 0 (mod 7) if r = 3, n + 1 = 2(12 k + 1) ≡ 0 (mod 7) if r = 4, and n + 2 = 24 k + 3 ≡ 0 (mod 7) if r = 6. Calculating the residues modulo 168 in the cases r ∈ { 0, 1, 5} we obtain: 

Proposition 3. The equation (1) has at least one solution for every prime number n, except possibly for those primes of the form n ≡ r (mod 168) ,with r ∈ { 1, 52, 11 2}, k ∈ Z, k ≥ 0. More precisely, 

N \ C 2 ⊂ { n | n ≡ 1, 52, 11 2 (mod 168) }.

Let us observe that 168 = 2 3(3)(7), 168 + 1 = 13 2, and the excepted residues modulo 168 are all perfect squares. Because of this, somehow, the first prime that is excluded by this result is 193 = 168 + 25. Again, we have 24 Eugen J. Ionascu and Andrew Wilson 4

even a higher jump in the number of primes that have been taken care of. As we did before there is an advantage to continue using (4) and do an analysis now on k modulo 5. For k = 5 l + r, we have n ≡ 0 (mod 5) if r = 1, 3 k + 1 ≡ 0 (mod 5) if 

r = 3, and 6 k + 1 ≡ 0 (mod 5) if r = 4, which puts n ∈ C 2 again. Therefore, we have for r ∈ { 0, 2} the following excepted residues modulo 120. 

Proposition 4. The equation (1) has at least one solution for every prime number n, except possibly for those primes of the form n ≡ r (mod 120) ,with r ∈ { 1, 72}, k ∈ Z, k ≥ 0. More precisely, 

N \ C 2 ⊂ { n | n ≡ 1, 72 (mod 120) }.

One can put these two propositions together and get Mordell’s Theorem. 

Theorem 2 (Mordell, [5]) . The equation (1) has at least one solution for every prime number n, except possibly for those primes of the form n =840 k + r, where r ∈ { 1, 11 2, 13 2, 17 2, 19 2, 23 2}, k ∈ Z, k ≥ 0. Moreover, we have 

N \ C 2 ⊂ { n | n ≡ 1, 11 2, 13 2, 17 2, 19 2, 23 2 (mod 840) }.

Proof. By Proposition 3, n = 168 k + 1 may be an exception but if 

k = 5 l + r, with r ∈ { 0, 1, 2, 3, 4} we have n ≡ 1 or 7 2 (mod 120) only for 

r ∈ { 0, 1}. These two cases are the exceptions for both propositions and they correspond to n ≡ 1 or 13 2 (mod 840). All other excepted cases are obtained the same way. 

Let us observe that 840 = 2 3(3)(5)(7) and the residues modulo 840 are all perfect squares. Not only that but 840 + 1 = 29 2, 840 + 11 2 = 31 2, and 1009 = 840 + 13 2 is the first prime that is excluded by this important theorem. While 193 is the 44th prime number, 1009 is the 169th prime. It is natural to ask if a result of this type can be obtained for an even bigger modulo. We will introduce here the next natural step into this analysis, which implies to allow 

a be the next possible value, i.e., n+11 4 , and we will be using the identities (5) 4120 k + 1 = 130 k + 3 + 11 3(10 k + 1)(120 k + 1) , k ∈ N,

(6) 4120 k + 49 = 130 k + 15 + 11 3(5)(2 k + 1)(120 k + 49) , k ∈ N.

2. THE ANALYSIS MODULO 11 

According to Proposition 4 we may continue to look only at the two cases modulo 120 and use only the two formulae above. If we continue the analysis modulo 11 in these two cases we obtain the following theorem. 5 On the Erd¨ os-Straus conjecture 25 

Theorem 3. The equation (1) has at least one solution for every prime number n, except possibly for those primes of the form n = 1320 k + r, where 

r ∈ { 1, 72, 13 2, 17 2, 19 2, 23 2, 29 2, 31 2, 7(103) , 1201 , 7(127) , 23(47) } := E, k ∈ Z, k ≥ 0.

Moreover, we have 

N \ C 3 ⊂ { n | n ∈ E (mod 1320) }.

Proof. If n = 120 k + 1 and k = 11 l + 1, we see that n ≡ 0 (mod 11) and so (5) gives the desired decomposition as in (1) right away. If k = 11 l + r and 

r ∈ { 2, 4, 5} the Theorem 1 can be employed to split the second term in (5) as a sum of two unit fractions. For instance, for r = 5 we have 1 + 3(10(11 l +5) + 1) ≡ 0 (mod 11), so one can take m = 11, x = 1 and y = 30 k + 3 in Theorem 1. Hence we have seven exceptions in this situation: 

• r = 0 corresponds to n ≡ 1 (mod 1320), 

• r = 3 gives n ≡ 19 2 (mod 1320), 

• r = 6 corresponds to n ≡ 7(103) (mod 1320), 

• r = 7 gives n ≡ 29 2 (mod 1320), 

• r = 8 corresponds to n ≡ 31 2 (mod 1320), 

• r = 9 gives n ≡ 23(47) (mod 1320), and finally 

• r = 10 corresponds to n ≡ 1201 (mod 1320). If n = 120 k + 49 and k = 11 l + r, then for r = 5 we have n ≡ 0 (mod 11). If r ∈ { 3, 5, 6, 8, 9, 10 } we can use Theorem 1. The exceptions then are: 

• r = 0 corresponds to n ≡ 72 (mod 1320), 

• r = 1 gives n ≡ 13 2 (mod 1320), 

• r = 2 corresponds to n ≡ 17 2 (mod 1320), 

• r = 4 gives n ≡ 23 2 (mod 1320), 

• r = 7 corresponds to n ≡ 7(127) (mod 1320). 

Putting Theorem 2 and Theorem 3 together we get the following 36 exceptions: 12 13 2 17 2 19 2 23 2 29 2

31 2 1201 37 2 41 2 43 2 13(157) 47 2 2521 19(139) 2689 53 2 3361 59 2 3529 61 2 29(149) 67 2 71 2

13(397) 73 2 5569 17(353) 31(199) 79 2

83 2 7561 7681 89 2 8089 8761 26 Eugen J. Ionascu and Andrew Wilson 6

The residue 1201, the first prime in this list is not really an exception because of the following identity 49240 k + 1201 = 12310 k + 308 + 15(9240 k + 1201)(15 k + 2) +(7) + 1770(9240 k + 1201)(15 k + 2) ,

which shows that 9240 k + 1201 ∈ C 8 for all k ∈ Z, k ≥ 0. We checked for similar identities and found just another similar identity for the exception 17(353) = 6001: 49240 k + 6001 = 12310 k + 1540 + 1385(9240 k + 6001)(2034 k + 1321) +(8) + 122(3 k + 2)(2034 k + 1321) ,

which shows that 9240 k + 6001 ∈ C 40 for all k ∈ Z, k ≥ 0. 

Theorem 4. The equation (1) has at least one solution for every prime number n, except possibly for those primes of the form n ≡ r (mod 9240) where 

r is one of the 34 entries in the table:                             

> 1213 217 219 223 229 2
> 31 237 241 243 213(157) 47 2
> 2521 19(139) 2689 53 23361 59 2
> 3529 61 229(149) 67 271 213(397) 73 25569 31(199) 79 283 27561 7681 89 28089 8761

Moreover, if n is not of the above form, it is in the class C3, or in C8 if 

n ≡ 1201 (mod 9240) , or in C40 if n ≡ 6001 (mod 9240) .Proof. We look to see for which values of r ∈ { 0, 1, 2, 3, 4, 5, 6} we have 1320(7 l + r) + s ∈ { 1, 52, 11 2} (mod 168) with s ∈ E (E as in Theorem 3). For instance, if s = 19 2 we get that r must be in the set {0, 1, 3} in order to have 1320(7 l + r) + 19 2 ∈ { 1, 52, 11 2} (mod 168). These three cases correspond to residues 19 2, 41 2 and 29(149) modulo 9240. Each residue in E gives rise to three exceptions. We leave the rest of this analysis to the reader. 

It is important to point out that these residues appear also in [9] but as a result of an algorithm which is only described there. Their idea is based on a result proved in [6] which basically uses sufficient conditions to solve the 7 On the Erd¨ os-Straus conjecture 27 

equation (1) 

n = 4 ab (cd − b) − c or cn + 1 = 4 ab (cd − b), n, a, b, c, d ∈ N.

The reader can verify that in the first case we have 4

n = 1

ad (cd − b) + 1

nad (cd − b) + 1

nabd 

and for the second condition 4

n = 1

ad (cd − b) + 1

abd + 1

nab (cd − b) .

Let us denote by δ(r) a divisor of r. Terzi’s program is based on three different ways of writing the first condition (above) and another way of writing the second condition 

n = 4 αβk − δ(α + β), n = 4 αβk − 4αδ (α) − βn = 4 αβk − δ(4 αβ 2 + 1) , and n = (4 αβ − 1) k − 4αδ (α).

Also, Terzi [9] provides a list of 198 exceptional residues for the modulo 120120. For two of the exceptions that they have there, 2521 and 9601, we have found the following identities 4120120 k + 2521 = 130030 k + 4004 +(9) + 11001(120120 k + 2521)(810 k + 17) + 122(15 k + 2)(810 k + 17) , k ≥ 0,

and also for k ≥ 0, 4120120 k + 9601 = 12436 + 30030 k ++ 114(120120 k+9601)(58+715 k)(470+5880 k) + 16(58+715 k)(470+5880 k) .

This shows that the program used in [9] was not exhaustive and the method was completely different of ours. We have implemented the same idea into a program, as in [9], and obtained different results than the ones stated. 3. NUMERICAL COMPUTATIONS AND COMMENTS 

We observe that the first ten of these residues in Theorem 4 are all perfect squares. In fact, all 19 squares of primes less than 9240 and greater than 11 2

are all excepted residues. There is something curious about the fact that all the perfect squares possible are excepted. This may be related with the result obtained by Schinzel in [7] who shows that identities such as (7), (8) and others in this note, cannot exist if the residue is a perfect square. The same 28 Eugen J. Ionascu and Andrew Wilson 8

phenomenon is actually captured in Theorem 2 in [11]. The good news about Theorem 2, Theorem 3, and Theorem 4, is that the first excepted residues are all perfect squares or composite and moreover their number is essentially increasing with the moduli. With our analysis unfortunately, there are a few other composite and 9 prime residues that have to be excluded. The prime 2521 is only the 369th prime and it is the first prime that is excluded by this theorem. However, a decomposition with the smallest a possible is exhibited in the equality 42521 = 1636 + 170588 + 15611746 ,

which puts 2521 ∈ C 6. The other primes are in the smallest class C as follows           

> C1C2C3C4C5C6
> 3361, 7681, 8089 3529, 5569 8761 2689 7561 2101, 2521

Clearly, one can continue this type of analysis by adding more primes to the modulo which is at this point 9240. It is natural to just add the primes in order regardless if they are of the form 4 k + 1 or 4 k + 3. We see that Erd¨ os’ conjecture is proved to be true if one can show that the smallest excluded residue for a set of moduli that converges to infinity is not a prime. One way to accomplish this is to actually show that the pattern mentioned above continues, i.e., the number of excluded residues which are perfect squares or composite is essentially growing as the modulus increases. This is actually our conjecture that we talked about in the abstract. Numerical evidence points out that for residues r which are primes, we have 9240 s + r ∈ C k(s,r ) with 

k(s, r ) bounded as a function of s. For example, 9240 s + 2521 ∈ C 12 for every 

s = 1 . . . 100000 and the distribution through the smaller classes is                       

> C1C2C3C4C5C6C7C8C9C10 C11 C12
> 10852 6444 5332 811 612 277 63 82 670544 .3% 26 .31% 21 .78% 3 .3% 2 .5% 1 .13% 0 .26% 0 .34% 0 .025% 0 .029% 0% 0 .021%

Now, if we add 13 to the factors we would have an analysis modulo 120120. It turns out that 2521 is not an modulo 120120 exception since we have (9) which shows that 120120 k + 2521 ∈ C 3374 for all k ∈ Z, k ≥ 0. We found similar identities for the residues 2689, 3529, 29(149), 5569, 31(199), 7561, and 7681 modulo 120120. This suggests that one may actually be able to obtain Mordell type results for bigger moduli, in the sense that the perfect squares residues appear essentially in bigger numbers, by implementing a finer analysis that involves higher classes than C3. It is natural to believe that this 9 On the Erd¨ os-Straus conjecture 29 

might be true, by taking into account that Vaughan [10] showed that 1

m #{n ∈ N | n ≤ m, and (1) does not have a solution } ≤ e−c(ln m)2/3

, m ∈ N,

for some constant c > 0. This is saying, roughly speaking, that the proportion of the those n ≤ m for which a writing with three unit fractions of 4 /n goes to zero a little slower than 1 

> m

as m → ∞ . The first few primes that require a big-ger class than the ones before are 2 , 73 , 1129 , 1201 , 21169 , 118801 , 8803369 , . . . , 

corresponding to classes C1, C2, C3, C4, C8, C15 , C27 , . . . . which shows a steep increase in the size of classes relative to the number of jumps. In [11], Yamamoto has a different approach from ours and obtains a lesser number of exceptions at least for the primes involved in Theorem 4. For each prime p of the form 4 k + 3 between 11 and 97, there is a table in [11] of exceptions for congruency classes r (n ≡ r (mod p)) that is used to check the conjecture using a computer for al n ≤ 10 7. In [3], Richard Guy mentions that the conjecture is checked to be true for all n ≤ 1003162753. Nevertheless, it seems that the conjecture has been checked for n ≤ 10 4, see [8]. However, with our method we extended the search for a counterexample from 1003162753 further for all n ≤ 4, 146 , 894 , 049. For our computations we wrote a program that pushes the analysis for a modulus of M = 2 , 762 , 760 = 23(3)(5)(7)(11)(13)(23). The primes chosen here are optimal, in the sense that the excepted residues are in number less than the ones obtained by other options. The first 12 exceptions in this case are 1, 17 2, 19 2, 29 2, 31 2, 37 2,41 2, 43 2, 47 2, 53 2, 3361, and 59 2. The number of these exceptions was 2299 but it is possible that our program was not optimal from this point of view. Nevertheless, this meant that we had to check the conjecture, on average, for every other ≈ 1201 integer. The primes generated, 889456 of them, are classified according to the smallest class they belong to in the next tables:                                                   

> C1C2C3C4C5C6C7C8C9C10 C11 C12
> 380547 228230 128494 61129 50853 17116 8459 9580 1836 1386 547 855 42 .8% 25 .7% 14 .4% 6.9% 5.7% 2% 0.9% 1% 0.2% 0 .15% 0 .06% 0 .096%
> C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24
> 115 124 111 26 10 27 2440000.013% 0 .014% 0 .012% 0 .003% 0 .001% 0 .003% 0 .0002% 0 .00045% 0 .00045% 0% 0% 0%
> C25 C26 C27
> 0010% 0% 0.0001%

30 Eugen J. Ionascu and Andrew Wilson 10 

So far, we have not seen a prime in a class Ck with k > 27. However, the result obtained in [7] seems to imply that the minimum class index for each prime, assuming the conjecture is true, should have a limit superior of infinity. 

REFERENCES [1] Abdulrahman A. Abdulaziz, On the Egyptian method of decomposing 2/n into unit fractions . Historia Mathematica 35 (2008), 1–18. [2] E.S. Croot III, Egyptian Fractions . Ph. D. Thesis, 1994. [3] R. Guy, Unsolved problems in Number Theory . Third Edition, 2004. [4] G.G. Martin, The distribution of prime primitive roots and dense egyptian fractions .Ph. D. Thesis, 1997. [5] L.G. Mordell, Diophantine equations . London–New York, Acad. Press, 1969. [6] L.A. Rossati, Sull’equazione diofantea 4/n = 1 /x 1 + 1 /x 2 + 1 /x 3. Bolettino della Unione Matematica Italiana, serie III, Anno IX, 1(1954). [7] A. Schinzel, On sums of three unit fractions with polynomial denominators . Funct. Ap-prox. Comment. Math. 28 (2000), 187–194. [8] A. Swett, http://math.uindy.edu/swett/esc.htm .[9] D.G. Terzi, On a conjecture by Erd¨ os-Straus . Nordisk Tidskr. Informationsbehandling (BIT) 11 (1971), 212–216. [10] R.C. Vaughan, On a problem of Erdos, Straus and Schinzel . Mathematika 17 (1970), 193–198. [11] K. Yamamoto, On the diophantine equation . Memoirs of the Faculty of Science, Kyushu University, Ser. A 19 (1965), 1, 37–47. 

Received 25 July 2010 Columbus State University Department of Mathematics Columbus, GA 31907 ionascu eugen@colstate.edu

