100 Data Science Programming Problems
=====================================


General Programming
-------------------

1. Write a function that converts a dictionary of equal length lists into a list of dictionaries.

    ```
    {'a': [1, 2, 3], 'b': [3, 2, 1]}
    => [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
    ```

1. Write the inverse function to the previous problem, convert a list of dictionaries into a dictionary of equal length lists.

    ```
    [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
    => {'a': [1, 2, 3], 'b': [3, 2, 1]}
    ```

1. Given two lists of characters with the same length, write a function that returns a list of booleans, also of the same length.  The value in the return list should be True if *either* of the characters in the two lists at that index are vowels, otherwise it should return false.

   ```
   (['a', 'b', 'c', 'd', 'e'], ['v', 'w', 'x', 'y', 'z'])
   => [True, False, False, False, True]
   ```

1. Write a function that takes a string, and returns a dictionary that keys a list of words in the string according to the first letter in the word.

   ```
   "a special string bearing an important salutation"
   => {'a': ['a', 'an'], 'b': ['bearing'], 'i': ['important'], 's': ['special', 'string', 'salutation']}
   ```

1. Write a function that reads lines from two files, and writes out a new file.  You may assume that each line in the input files contain a single word.  The output file should have the words concatenated with a comma, but the two words on each line should be in alphabetical order.  If the input files have different lengths, write single words to the output file until the longer file is exhausted.

    ```
    File 1:  File2:
    This     And
    is       another
    a        file
    file
    of
    words

    Output File:
    And, This
    another, is
    a, file
    file
    of
    words
    ```

1. Given a list of equal length lists, transpose it.

    ```
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    => [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    ```

1. Given a list of numbers representing the coefficients in a polynomial (largest powers first), write a function that returns a pretty string representation of the polynomial.

    ```
    [1, 1, 1] => "x^2 + x + 1"
    [2, -1, -2] => "2x^2 - x -2"
    [0, 9, -10] => "9x - 10"
    ```

    Pay attention to edge cases!

Data Manipulation - Numpy
-------------------------

1.  Given an integer numpy array of 0's and 1's, write a function that creates a new array where 0's are replaced with the word `"red"` and 1's are replaced with the word `"blue"`.

    ```
    np.array([0, 0, 1, 0, 1]) => np.array(["red", "red", "blue", "red", "blue"])
    ```

1.  Given two equal length arrays, `x` with general numeric data, and `b` with only 0's and 1's, compute the mean of the data in `x` at the positions where `b == 0` and the mean of the data in `x` at the positions where `b == 1`.

    ```
    x = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 1, 0, 0, 1])
        => {0: 3.5, 1: 4}
    ```

1. Write a function that consumes a two-dimensional numpy array (so, a matrix), and a label which is either "row" or "column".  The function should return a one-dimensional numpy array (vector) with either the row or column averages.

    ```
    X = np.array([[0, 1], [2, 1]])
    row_or_column_means(X, "row")
        => np.array([0.5, 1.5])
    row_or_column_means(X, "column")
        => np.array([1.0, 1.0])
    ```

1.  Given an array `x`, and a matrix `M` (two dimensional array) with the same number of columns as the length of `x`, find the row in `M` that makes the smallest angle with `x`.

1.  Given a number `n`, create a matrix of zeros, but with ones on the diagonals immediately below and above the main diagonal.  For example, when `n=5`, you should create the following matrix

    ```
    [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0]
    ]
    ```

1.  Given a matrix `M`, create a new matrix containing only the *columns* of `M` where at least one of the entries is negative.

1.  Write a function that swaps two rows of a matrix:

    ```
    def swap_rows(M, i, j)
    ```

1.  Write a function that creates a square matrix with a checkerboard pattern of 0's and 1's of any given size.

    ```
    [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    ]
    ```

1.  Write a function that takes *any* number of matrices, and determines if they can be multiplied in the order passed.

1.  Write a function that converts an  array of shape `(n, 2)` representing Cartesian coordinates of `n` points into a new `(n, 2)` array containing the polar coordinates of those points.

    ```
    np.array([[0, 1], [1, 0], [1, 1]])
        => np.array([1, np.pi], [1, 0], [np.sqrt(2), np.pi / 2])
    ```

1.  Given a `(n, 3)` matrix of points (each point is represented by one row, and has three coordinates), and an additional vector with three coordinates, return an `(n, 2)` matrix representing the projection of the original points onto the plane orthogonal to the vector.

    ```
    project_orthogonal_to_vector(matrix, vector)
    ```

    Is this problem fully specified?  Do you have to make any choices to accomplish this task?

1.  Write a function that takes two numpy arrays of shapes (n, k) and (m, k), representing points in k-dimensional space, and returns an array of shape (n, m) giving the Euclidean distance between each point in the first array and each point in the second. Try to write it without any loops.


Data Manipulation - Pandas
--------------------------

1. You have a pandas DataFrame `berries` which contains columns `type` and `size`.  Select all the (rows representing) blueberries larger than 0.5 cm in size.

1. You have a pandas DataFrame `berries` which contains columns `type` and `size`.  Create a dataframe containing the largest berry of each size.

1. You have a pandas DataFrame containing observations of stock prices over time, it contains columns `stock`, `day` and `price`.  Create a data frame that contains the stock price for each stock on the *day after* they achieve their maximum price.


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

1. You visit a website that provides amusing data-science jokes. Each time you visit it displays a joke randomly chosen from a finite set. Over the course of four visits, you see three unique jokes and one repeat. Using maximum likelihood estimation, estimate the total number of jokes on the website.


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

1. You are running a popular role-playing game. In it, the players create characters that have randomly generated values for 6 different attributes, each found by summing the rolls of three 6-sided dice, so each attribute will range from 3 to 18 (higher is better).

To save time you have each person generate their own characters before you get together, but you are worried some of them might cheat. Design a frequentist a/b test to investigate this. Consider the ways in which someone might cheat (in particular, cheaters don't want to get caught and might care more about some attributes than others).


Algorithms
----------

1. Given the following data:

  - A function `f: np.array => float` that maps a numpy array to a floating point number.
  - A function `df: np.array => np.array` that maps a numpy array to another numpy array, this is the gradient of `f`.
  - An initial point `_0x`, stored as a numpy array.
  - A learning rate `learning_rate`, a floating point number.
  - A `tolerance`, floating point number.

    Write an iterator `gradient_descent` (i.e. like a function, but uses `yield`) that generates the sequence of points by applying gradiend descent to the function `f`, starting at the initial point `x_0`, with the learning rate `learning_rate`, until the convergence tolerance `tolerance` is met.

    ```
    gradient_descent(f, df, x_0, learning_rate=0.01, tolerance=0.01)
    ```

2. In the same situation of the previous problem, except with the extra data

  - A function `ddf: np.array => np.array` that maps a numpy array to a matrix, this is the second derivative of `f`.

    Write an iterator that generates a sequence of points by applying Newton's method.  Try *not* to explicitly invert a matrix, use `np.linalg.solve` instead.

3. Write a class that implements *peicewise linear regression*.  This is a linear regression, but instead of fitting a single line to the data, it fits various lines of changing slope that join up continuously.  

![Piecewise Linear Regression](img/pw-regression.png)

The points where it changes slope are called *knots*.  Your class should have the following structure:

    ```
    class PWLinearRegression(object):
        """
        Fit piecewise linear regression on data.
        
        Parameters
        -------
        Knots : Array
            Knot locations.
        """
        def __init__(self, knots):
            pass
            
        def fit(self,x, y):
            """
            Fit piecewise linear model.
            
            Parameters
            ----------
            x : 1D numpy array of data inputs
            y : 1D numpy array of data responses
            """
            pass
            
        def predict(self, x):
            """
            Make predictions with fit model.
            
            Parameters
            ----------
            x : int, float, 1D array/list type of model prediction inputs.
            
            Returns
            -------
            Predicted response of x shape.
            """
            pass
        ```

Feel free to use any numpy or sklearn methods.


Plotting
--------

1.  Using your function that creates sample data from a simple linear model, superimpose the true linear model onto a scatterplot of the generated data. 

1. Create a (2, 3) grid of plots.  Inside each plot display the coordinates of the plot, like so:

    ```
    +----------+----------+----------+
    |  (0, 0)  |  (0, 1)  |  (0, 2)  |
    +----------+----------+----------+
    |  (1, 0)  |  (1, 1)  |  (1, 2)  |
    +----------+----------+----------+
    ```

1. Given a list pairs of ordered pairs, like so:

    ```
    [[(0, 1), (1, 0)], [(1, 1), (2, 2)], [(-1, 0), (0, -1)]]
    ```

    Plot each of them as vectors (as in, a picture of an arrow) whose tail is at the first coordinate, and whose head is at the second.


SQL
---

The following problems use tables with the following table schemas for a database keeping records of checkouts for library patrons and books.  This is only a selection of tables in the database, there are possibly many more.

#### Users

| column    | type    |
|-----------|---------|
| user_id   | int     |
| join_date | date    |
| branch_id | int     |
| name      | string  |

#### Books

| column       | type   |
|--------------|--------|
| book_id      | int    |
| author_id    | int    |
| genere_id    | int    |
| publish_date | date   |
| name         | string |

#### Checkouts

| column        | type      |
|---------------|-----------|
| user_id       | int       |
| book_id       | int       |
| checkout_time | timestamp |
| return_time   | timestamp |

The `return_time` field may be `null` in the case that the book has not yet been returned.


1. Write a query that returns all the users (by name) that have checked out a book within the last month.

1. Write a query that returns all the users (by name) that have a currently checked out book.

1. Assuming that the checkout time for a book is one month, write a query returning all users (by name) that have an overdue book.  Summarize this data to produce a list of possibly stolen books (you will have to come up with a reasonable interpretation of what this means).

1. Amend the prior query to return a table of all (user, book) pairs that are possibly stolen.  Identify the users and books by name in the query results.


Web Programming
---------------

1. Write a function `redbubble_creators` which takes a search string, and returns all the artists whose products appear on the first search result page when that search string is used.

    ```
    redbubble_creators('zelda')
    redbubble_creators('eno')
    ```
1. Add an optional argument, `type`, which will subset the returned artists from the previous query to only those that have a product form the given category.

    ```
    # Zelda stickers
    redbubble_creators('zelda', type='sticker')
    # Eno shirts
    redbubble_creators('eno', type='shirt')
    ```
1. Add an optional argument, `pages`, that will return search results from the given query appearing on the first `n` pages.

    ```
    # Zelda stickers on the first five pages
    redbubble_creators('zelda', type='sticker', pages=5)
    ```
1. Read the leaderboard for [Super Metroid](http://deertier.com/Leaderboard/AnyPercentRealTime) completion times into a data frame.

1. Using the leaderboards for [Ocarina of Time](http://zeldaspeedruns.com/leaderboards/oot/any), scrape data and then plot the progression of the world record over time.  That is, for each possible day, calculate the fastest submitted time up to that day.  Note that the leaderboard itself does not contain all submitted times, only the fastest submitted time for each user.  Following the hyperlink for each user in the leaderboard table will show you all the times submitted for that user, some of which may have stood as a world record in the past. 
