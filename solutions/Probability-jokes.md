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

Note that since we only care about the relative likelihoods for different values of $n$, we can ignore constants. So in general, if we visit our joke site $v$ times and get $u$ unique jokes, there are $n$ ways we can choose the first unique joke, $n-1$ the second, and so on, to $n-u+1$. Calculating the actual number of ways to choose the jokes is more complicated, but it involves multiplying that by a constant *that is independent of $n$*. So the overall likelihood is proportional to $$\frac{\prod_{i=0}^{u-1}(n-i)}{n^v}$$

We can write some code to find the maximum for any number of visits and unique jokes.

```python
import numpy as np

def joke_relative_likelihood(n, visits, unique):
    return np.arange(n, n-unique, -1, dtype='float64').prod() / n**visits

def print_relative_likelihoods(visits, unique, nmax=10):
    for n in range(unique, nmax+1):
        print(f"{n:5} {joke_likelihood(n, visits, unique):10.10f}")

def find_maximum_likelihood(visits, unique):
    if unique == visits:
        return np.Inf
    if unique > visits:
        raise ValueError("There can't be more unique jokes than visits")
    n = 1
    prev_likelihood = 0
    while True:
        likelihood = joke_relative_likelihood(n, visits, unique)
        if likelihood < prev_likelihood:
            return n-1
        prev_likelihood = likelihood
        n += 1
```

Note that these numbers are not probabilities. One might approach this as a Bayesian, with a prior probability of the initial number of jokes, but if we only have a single repeat (as in the original problem), for large values of $n$ the likelihood is proportional to $1/n$, so if we use a uniform (or even $1/n$) prior the expectation value of the posterior (the sum of the posterior times the number of jokes) won't converge. That's not all that surprising given we only visited the site four times.

Writing code to find the probabilities and expectation value (given a prior) is left as an exercise to the reader.