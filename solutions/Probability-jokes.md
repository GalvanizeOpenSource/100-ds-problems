You visit a website that provides amusing data-science jokes. Each time you visit it displays a joke randomly chosen from a finite set. Over the course of four visits, you see three unique jokes and one repeat. Using maximum likelihood estimation, estimate the total number of jokes on the website.

Suppose there are $n$ jokes. In you visit four times, there are $n^4$ possible responses.

The number of ways you can can three unique jokes with one repeat is:

 * $n$ ways to choose which joke is repeated, times
 * $4 \choose 2$ ways to choose the position in the sequence of the repeated joke, times
 * $n-1$ ways to choose the first of the remaining jokes, times
 * $n-2$ ways to choose the second of the remaining jokes.

So the likelihood is $6n(n-1)(n-2) \over n^4$. We can calculate that for various numbers of total jokes:

number jokes| ways to choose one repeat | likelihood
------------|---------------------------|-----------
1           | 0                         | 0
2           | 0                         | 0
3           | 36                        | 0.4444
4           | 144                       | 0.5625
5           | 360                       | 0.5760
6           | 720                       | 0.5555
7           | 1260                      | 0.5247
8           | 2016                      | 0.4921

The likelihood has a maximum at 5 jokes, so if we use maximum-likelihood estimation, we would guess that as a solution.

Note that these numbers are not probabilities. One might approach this as a Bayesian, with a prior probability of the initial number of jokes, but for large values of $n$ the likelihood is proportional to $1/n$, so if we use a uniform (or even $1/n$) prior the expectation value of the posterior (the sum of the posterior times the number of jokes) won't converge.