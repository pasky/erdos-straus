## Content from https://math.dartmouth.edu/~carlp/esconjfl.pdf

Title: esconjfl.pdf

URL Source: https://math.dartmouth.edu/~carlp/esconjfl.pdf

Published Time: Sun, 15 Mar 2026 20:35:59 GMT

Number of Pages: 31

Markdown Content:
# Alladi 70 Conference March 20, 2026 

# The Erd˝ os–Straus Conjecture 

# Carl Pomerance , Dartmouth College Joint work with Andreas Weingartner , Southern Utah University Andreas Weingartner 

> 1

Paul Erd˝ os Ernst Straus (Drawing by LeUyen Pham, illustrator of The Boy Who Loved Math, by Deborah Heiligman) 

> 2

In 1948, Paul Erd˝ os and Ernst Straus conjectured that for every integer n ≥ 2, there are positive integers x, y, z such that 4

n = 1

x + 1

y + 1

z .

The first question: Why make this conjecture??? 

> 3

The Rhind papyrus, ca. 1500 BCE 

> 4

Apparently the ancient Egyptians were especially fond of fractions with numerator 1, so-called unit fractions . To represent other fractions, they would find some unit fractions that summed to what they wanted. For example, consider 5 ~7. We have 57 = 12 + 15 + 170 .

The Rhind papyrus gave a list of such representations, now called Egyptian fractions. 

> 5

Note that the above decomposition of 5 ~7 was found by the “greedy algorithm”, where each fraction is chosen as large as possible without exceeding the target. For example, 1~2 < 5~7 < 1~1, so we choose 1 ~2. We have 5 ~7 − 1~2 = 3~14 and 1~5 < 3~14 < 1~4, so we choose 1 ~5. What’s left is 1 ~70, and we’re done. The greedy algorithm for Egyptian fractions was first described by Fibonacci about 800 years ago. 

> 6

Note that the greedy algorithm does not always give the shortest representation. Lets try 4 ~17. The greedy algorithm gets 417 = 15 + 129 + 11233 + 13039345 ,

but 417 = 16 + 117 + 1102 is simpler. 

> 7

One might try and describe the set of rationals which have a shortest representation as a sum of k unit fractions. When k = 1, we have the unit fractions themselves. When k = 2, we have the identity 2

n = 1

n + 1

n,

which shows that each 2 ~n is in class 2 for n odd. But there are many more fractions in the class 2, for example 5 ~6 is. 

> 8

Theorem (Stewart, 1964 ). If (m, n ) = 1, we have m~n the sum of 2 unit fractions if and only if m is a divisor of the sum of two coprime divisors of n.For example, 2 and 3 are coprime divisors of 6 and 5 is a divisor of 2 + 3, so 5 ~6 is the sum of 2 unit fractions. But 5 ~7 is not, nor is 4 ~17, nor is any m~p with p an odd prime and m ∤ p + 1. 

Proof . Suppose a, b S n with (a, b ) = 1 and m S a + b. Write n = abc 

and a + b = md . Then 

mn = md nd = a + babcd = 1

bcd + 1

acd .

> 9

Theorem (Stewart, 1964 ). If (m, n ) = 1, we have m~n the sum of 2 unit fractions if and only if m is a divisor of the sum of two coprime divisors of n.

Proof, cont’d . Now suppose that m~n = 1~u + 1~v. Say (u, v ) = c,

u = ac , v = bc . Then 

mn = 1

u + 1

v = a + babc .

Let d = ( a + b, c ). Since (a, b ) = 1 we thus have md = a + b, nd = abc .So a, b are coprime divisors of n, and we’re done. 

> 10

A corollary of Stewart’s theorem is that for each fixed m,almost all n have m~n the sum of two unit fractions! Indeed, if 

n is divisible by some prime p ≡ − 1 (mod m), then since p, 1 are coprime divisors of n and m S p + 1, we have m~n the sum of two unit fractions. And the number of integers n ≤ x not divisible by any prime p ≡ − 1 (mod m) is Om(x~( log x)1~ϕ(m)). Here ϕ(m) is Euler’s function. This can be improved. If m~n is not the sum of two unit fractions, with (m, n ) = 1, then n can have prime factors in at most half of the ϕ(m) reduced residue classes mod m. And so we have an upper bound of Om(x~( log x)1~2); Elsholtz, 1998. This kind of thinking leads to an asymptotic. If m~n is not the sum of two unit fractions, then essentially n takes only primes in a subgroup of (Z~mZ)∗ that avoids −1. Using this, an asymptotic was found by Huang and Vaughan, 2011. 

> 11

So, the situation when m~n is or is not the sum of two unit fractions is basically understood. Which brings us to the sum of three unit fractions: 

mn = 1

x + 1

y + 1

z .

Note that if m ≤ 3, then the problem is trivial. So, the case of m = 4, the arena of the Erd˝ os–Straus conjecture, is the first interesting case. But why would one suspect that for every n ≥ 2 with m = 4 there is a solution? Could this really be true? 

> 12

First note that if each 4 ~p with p prime is a sum of three unit fractions, then so is each 4 ~n. Indeed, if p S n, say n = jp , then dividing a representation for 4 ~p by j gets a representation for 4~n.Further, if p ≡ 3 (mod 4 ), then 4 S p + 1 so 4 ~p is the sum of two unit fractions (therefore also the sum of three). Suppose p + 1 is divisible by a prime q ≡ 3 (mod 4 ), so write 

q = 4k − 1 and p + 1 = jq . Then p = j(4k − 1) − 1 = 4jk − j − 1 and 4

p = 4jk pjk = 1

jk + j + 1

pjk = 1

jk + 1

pk + 1

pjk .

This is an early result of Obl´ ath and it immediately implies that the number of exceptional p ≤ x for which the Erd˝ os–Straus conjecture might be false is O(x~( log x)3~2).

> 13

This generalizes as follows: Again we have primes p, q with 

q ≡ 3 (mod 4 ). Write q = 4uvw − 1 and assume that p satisfies 

pv ≡ − u (mod q). (The Obl´ ath case had u = v = 1.) Then there is some integer t with pv + u = tq = 4tuvw − t, that is, 4tuvw = pv + u + t. 

Dividing this equation by ptuvw , we get 4

p = 1

tuw + 1

ptvw + 1

puvw .

This kind of thing can go in two directions: (1) get congruences for p where we know the conjecture holds, (2) get so many congruences that there are only a few p’s left in doubt. The first is an excellent aid for an exhaustive search for counterexamples. 

> 14

Using congruences, as reported in Mordell’s famous book on Diophantine equations, one learns that the Erd˝ os–Straus conjecture holds for every prime p except possibly for the quadratic residues mod 840, that is, except for those p with 

p ≡ 1, 121 , 169 , 289 , 361 , or 529 (mod 840 ).

Using congruences such as these, about 12 years ago, Salez verified the Erd˝ os–Straus conjecture to 10 17 . Just recently, Mihnea and Dumitru extended the search to 10 18 .

> 15

Robert C. Vaughan In 1970 Vaughan used the second approach and the large sieve to get an excellent upper bound for the number of possible exceptions up to N : It is O(N ~ exp (c(log N )2~3)) for an appropriate positive constant c.

> 16

If you can’t prove it, generalize it. . .

Waclaw Sierpi´ nski Sierpi´ nski conjectured that every 5 ~n for n ≥ 2 is a sum of three unit fractions. (With Weingartner, we have verified this to 10 18 .) 

> 17

Andrzej Schinzel Schinzel then generalized further: For every m ≥ 4, we have m~n

the sum of three unit fractions for all n > Nm, a constant depending on m. With Weingartner, we have investigated this numerically for m up to 15. For example, when m = 8 we have checked up to 10 13 and the only exceptional n found are 1, 2, 3, 11 , 17 , 131 , 241. See the table on the next slide. 

> 18

m all exceptions n ≤ N Count N

4 1 1 10 18 

5 1 1 10 18 

6 1 1 10 13 

7 1, 2 2 10 13 

8 1, 2, 3, 11 , 17 , 131 , 241 7 10 13 

9 1, 2, 5, 11 , 19 5 10 12 

10 1, 2, 3, 7, 11 , 43 , 61 , 67 , 181 9 10 12 

11 1, 2, 3, 4, 37 5 10 12 

1, 2, 3, 5, 7, 13 , 25 , 29 , 31 , 37 , 73 , 97 , 193 , 433 ,

12 577 , 1129 , 1657 , 1873 , 2521 , 2593 , 3433 , 10369 , 24 10 12 

12049 , 12241 13 1, 2, 3, 4, 5, 7, 14 , 53 , 61 , 67 , 79 , 211 , 281 13 10 12 

14 1, 2, 3, 4, 5, 17 , 19 , 29 , 59 , 257 , 353 , 841 12 10 12 

1, 2, 3, 4, 8, 16 , 17 , 19 , 23 , 31 , 34 , 47 , 53 , 61 , 79 ,

15 113 , 122 , 137 , 151 , 197 , 226 , 233 , 271 , 541 , 1103 , 32 10 12 

1171 , 1367 , 4201 , 6301 , 12601 , 16831 , 20521 

> 19

Already in his 1970 paper, Vaughan proved a general upper bound for exceptions to the Schinzel conjecture: The number of n ≤ N for which m~n is not the sum of three unit fractions is 

O(N ~ exp (c(m)( log N )2~3), where c(m) > 0. With Weingartner, we were able to prove this with 

c(m) = c~ϕ(m)1~3, with c an absolute positive constant, uniformly for m ≤ ( log N )2.

> 20

But mainly my work with Weingartner deals with the exceptional set in the Schinzel variant. Schinzel’s conjecture is that for each m there is some Nm such that when n > Nm we have m~n the sum of three unit fractions. How large is this 

Nm? For example, the Erd˝ os–Straus conjecture is that N4 = 1. And empirically it seems that N8 = 241. We show that as m

gets large, exceptions become enormous. 

Theorem (Pomerance & Weingartner) . For each  > 0 there is a bound m such that if m > m there is a number 

n > exp (m1~3−) with m~n not the sum of three unit fractions. In fact, with N = exp (m1~3−), we show that most primes p in 

(N, 2N ] have m~p not the sum of three unit fractions. 

> 21

Our proof uses many ideas from a recent paper of Elsholtz and Tao on counting the number of triples x, y, z where 4~n = 1~x + 1~y + 1~z. They also do a good job of citing the many researchers who have obtained partial results. 

Christian Elsholtz Paul Erd˝ os & Terence Tao 

> 22

Let m ≥ 4 and let p be a prime. The first observation is that solutions to m~p = 1~x + 1~y + 1~z come in two types. A Type I solution has p dividing just one of x, y, z , while a Type II solution has p dividing two of x, y, z . (Since the smallest of 

x, y, z must be < p, it follows that p cannot divide all of x, y, z .) The next observation is that it is possible to give parametrizations of the two types. There is a Type I solution if and only if there are positive integers a, d, f such that 

f S ma 2d + 1, mad S p + f. 

There is a Type II solution if and only if there are positive integers a, b, e with 

e S a + b, mab S p + e. 

> 23

Lets focus on Type I solutions: 

f S ma 2d + 1, mad S p + f. 

Let N be a large function of m, say about exp (m1~3), to get a feel for the argument. We try to count primes p ∈ ( N ~2, N ] for which a Type I solution exists. We see that p is in a residue class modulo mad , so a ready tool to use is the Brun–Titchmarsh theorem. This gives the bound 

≪ Q  

> a,d ∶ad <3N~m

N τ (ma 2d + 1)

ϕ(mad ) log (2 + N ~mad ).

> 24

Then using a calculation in Elsholtz–Tao for part of the range, and another argument for another part, we find that the number of primes p ∈ ( N ~2, N ] with a Type I solution is 

≪ Nϕ(m)(log N )2(log m)2.

The trick is to then choose the relationship betwen N, m so that this is < N ~ log N , which will hold if 

N ≤ exp (( ϕ(m)~ C log 2 m)1~3)

for C large. With this choice, we have that most primes in 

(N ~2, N ] do not have a Type I solution. So, it then comes down to showing that most primes in this range also do not have a Type II solution. Similar methods show that there are fewer primes of this type, so we conclude that most primes p in (N ~2, N ] with N bounded as above have 

m~p not the sum of three unit fractions. 

> 25

One of the theorems mentioned in this talk says that in a certain range there are few exceptions, and in another range there are few solutions. Lets compare these ranges. We’ve just seen that near exp (m1~3) or smaller most primes p

will not have m~p the sum of three unit fractions. Earlier we saw that for m ≤ log 2 N most primes p near N will have solutions. This translates to N near exp (m1~2) or larger. 

> 26

This raises the question of where the transition is from almost never to almost always to always. Our proofs suggest that the average count of solutions for a given p is about (log p)3~m. We follow the thoughts of Elsholtz–Tao in the m = 4 case that there is a Poisson process at work, with the likelihood of no solution for m~p being about exp (−( log p)3~m). This suggests if 

p < exp (m1~3−) it’s unusual to have m~p the sum of three unit fractions. Once p grows to about exp (m1~3+) it is now common for there to be a solution but many times there are not. At exp (m1~2−) it’s the same situation but the exceptions are very sparse. And once p > exp (m1~2+), it is always true. 

> 27

Recall that Schinzel conjectured there is a number Nm such that if n > Nm then m~n is the sum of three unit fractions. If so, there is a perhaps smaller bound N ′ 

> m

such that m~p is a sum of three unit fractions for all primes p > N ′

> m

. The above suggests that N ′ 

> m

can be taken as exp (m1~2+o(1)), and probably the same is true for Nm, since our generalization of the Vaughan bound counts exceptional integers, not just primes. This says little about the m = 4 case where this story began. Feel free to have at it! 

> 28

For further reading on this subject, see T. Bloom and C. Elsholtz, Egyptian fractions, Nieuw Arch. Wisk. 23 (2022), 237–245. C. Elsholtz and T. Tao, Counting the number of solutions to the Erd˝ os–Straus equation on unit fractions, J. Aust. Math. Soc. 94 (2013), 50–105. C. Pomerance and A. Weingartner, Exceptions to the Erd˝ os–Straus–Schinzel conjecture, Ramanujan J., to appear. Also Combinatorial Number Theory by Erd˝ os–Graham, and Guy’s Unsolved Problems in Number Theory. 

> 29

# Happy Birthday Krishna!

