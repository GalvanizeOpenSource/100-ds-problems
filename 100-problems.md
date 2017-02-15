100 Data Science Programming Problems
=====================================

Data Manipulation
-----------------

1. Given an integer numpy array of 0's and 1's, write a function that creates a new array where 0's are replaced with the word `"red"` and 1's are replaced with the word `"blue"`.

```
np.array([0, 0, 1, 0, 1]) => np.array(["red", "red", "blue", "red", "blue"])
```

1. Given two equal length arrays, `x` with general numeric data, and `b` with only 0's and 1's, compute the mean of the data in `x` at the positions where `b == 0` and the mean of the data in `x` at the positions where `b == 1`.

```
x = np.array([1, 2, 3, 4, 5])
b = np.array([1, 1, 0, 0, 1])
    => {0: 3.5, 1: 4}
```

1. Given an array `x`, and a matrix `M` (two dimensional array) with the same number of columns as the length of `x`, find the row in `M` that makes the smallest angle with `x`.

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

1. Write a function that swaps two rows of a matrix:

```
def swap_rows(M, i, j)
```

1. Write a function that creates a square matrix with a checkerboard pattern of 0's and 1's of any given size.

```
[
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
]
```

1. Write a function that takes *any* number of matrices, and determines if they can be multiplied in the order passed.

1. Write a function that converts an  array of shape `(n, 2)` representing Cartesian coordinates of `n` points into a new `(n, 2)` array containing the polar coordinates of those points.

```
np.array([[0, 1], [1, 0], [1, 1]])
    => np.array([1, np.pi], [1, 0], [np.sqrt(2), np.pi / 2])
```

Probability
-----------

1. You have a shuffled deck of 60 cards containing the following cards of special interest.  
  - Three of these cards in the deck are marked with a diamond.
  - Three of the cards are marked with a star.  
  - The remaining cards are nothing special.
You draw an initial hand of five cards, after which you *must* discard any of the star cards for an additional three cards drawn from the top of the deck.  This process is repeated until you find yourself with a hand that does *not* contain any star cards.  Write a simulation to approximate the probability that your initial draw results in a final hand containing a diamond card. 

1. Use a built in function which samples data from a uniform distribution (for example `np.random.uniform` in python), to generate samples from the exponential distribution with a given parameter.  To start, consider reading about the [inverse sampling method](https://en.wikipedia.org/wiki/Inverse_transform_sampling).  Plot a histogram of data sampled using your code, and overlay the density function of an exponential distribution.

1. Write a function that samples random data from a true simple linear model with a given intercept, slope, and residual standard deviation.  Your function should additionally consume an array `x` containing data for the independent variable of the model:

```
def generate_simple_linear_data(x, intercept, slope, residual_sd):
```

The function should return the sampled `y` values.

Statistics
----------

1. Write a function that computes the p-value from a one tailed exact binomial test for a population proportion.  Your function should have the following signature:

```
def binomial_exact_test(n_samples, n_positive_samples, proposed_value)
```

And should compute the p-value of the following test:

```
H_0: p = proposed_value
h_a: p > proposed_value
```

Where `p` is the population proportion.

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

To fit the regression, use a linear equation solver to explicitly solve the matrix equation `X^t X beta = X^t y` for beta.

1. Fit a logistic regression to `X_train` and `y_train`, then compute and return the proportion of data in `X_test` and `y_test` that are correctly classified when threasholding the predicted probabilities with `threas`.

```
def logistic_accuracy(X_train, y_train, X_test, Y_test, thres)
```

1. Fit a logistic regression and return the maximal profit that can be achieved by classifying predicted probabilities for observations from a test set.  The profits/costs of true/false positives and true/false negatives are supplied in a two by two `profit_matrix` (profits are positive numbers, costs are negative numbers).

```
def logistic_profit(X_train, y_train, X_test, Y_test, profit_matrix)
```

Plotting
--------

1.  Using your function that creates sample data from a simple linear model, superimpose the true linear model onto a scatterplot of the generated data. 

SQL
---

Web Programming
---------------

1. Read the leaderboard for [Super Metroid](http://deertier.com/Leaderboard/AnyPercentRealTime) completion times into a data frame.

1. Using the leaderboards for [Ocarina of Time](http://zeldaspeedruns.com/leaderboards/oot/any), scrape data and then plot the progression of the world record over time.  That is, for each possible day, calculate the fasted submitted time up to that day.  Note that the leaderboard itself does not contain all submitted times, only the fasted submitted time for each user.  Following the hyperlink for each user in the leaderboard table will show you all the times submitted for that user, some of which may have stood as a world record in the past. 
