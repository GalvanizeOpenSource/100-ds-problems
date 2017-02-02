100 Data Science Programming Problems
=====================================

Data Manipulation
-----------------

1. Given an array of 0's and 1's, write a function that creates a new array where 0's are replaced with the word `"red"` and 1's are replaced with the word `"blue"`.

1. Given two equal length arrays, `x` with general numeric data, and `b` with only 0's and 1's, compute the mean of the data in `x` at the positions where `b == 0` and the mean of the data in `x` at the positions where `b == 1`.

1. Given a vector `x`, and a matrix `M` with the same number of columns as the length of `x`, find the row in `M` that makes the smallest angle with `x`.

1. Given a number `n`, create a matrix of zeros, but with ones on the diagonals immediately below and above the main diagonal.  For example, when `n=5`, you should create the following matrix

```
[
  [0, 1, 0, 0, 0],
  [1, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 0]
]
```

1. Given a matrix `M`, create a new matrix containing only the *columns* of `M` where at least one of the entries is negative.

Probability
-----------

1. You have a suffled deck of 60 cards.  Three of these cards in the deck are marked with a diamond, and three of the cards are marked with a star.  You draw an initial hand of five cards, after which you *must* discard any of the star cards for an additional three cards from the top of the deck.  This process is repeated until you find yourself with a hand that does *not* contain any star cards.  Write a simulation to approximate the probability that your initial hand results in a resolved hand containing a diamond card. 

1. Use a built in function which simulates draws from a uniform distribution (for example `numpy.random.uniform` in python, or `runif` in R) to generate samples from the exponential distribution with a given parameter.  To start, consider reading about the *inverse sampling method*.

1. Write a function that samples random data from a true simple linear model with a given intercept, slope, and residual standard deviation.  To generate `x` data, your function should accept a function that can be called to generate this data:

```
def generate_simple_linear_data(x_sampler, intercept, slope, residual_sd):
```

The function should return the sampled `x` and `y` values.

Statistics
----------

1. Write a function that 

1. Write a function that computes the p-value from a one tailed exact binomial test for a population proportion.  Your function should have the following signature:

```
def binomial_exact_test(n_samples, n_positive_samples)
```

You may utilize a built in function that computes the pmf or cmf of the Binomial distribution.

1. Write a linear regression class with the following methods:

```
class LinearRegression(object):

    def __init__(self):
        self.coeffs_ = None

    def fit(X, y):
        pass

    def predict(X):
        pass
```

To fit the regression, use a linear equation solver to explicitly solve the matrix equation `X^t X = X^t y`.

1. Fit a logistic regression to `X_train` and `y_train`, then compute and return the proportion of data in `X_test` and `y_test` that are correctly classified when threasholding the predicted probabilities with `threas`.

```
def logistic_accuracy(X_train, y_train, X_test, Y_test, thres)
```

1. Fit a logistic regression and return the maximal profit that can be achieved by classifying predicted probabilities for observatings from a a test set.  The profits/costs of true/false positives and true/false negatives are supplied in a two by two `profit_matrix` (profits are positive numbers, costs are negative numbers).

```
def logistic_profit(X_train, y_train, X_test, Y_test, profit_matrix)
```

Plotting
--------

1.  Using your function that creates sample data from a simple linear model, superimpose the true linear model onto a scatterplot of the gerenated data. 

SQL
---
