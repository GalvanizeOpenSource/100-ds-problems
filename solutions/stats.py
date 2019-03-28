import numpy as np
from scipy import stats
from sklearn.linear_model import LogisticRegression


def binomial_exact_test(n_samples, n_positive_samples, proposed_value):
    h0_dist = stats.binom(n=n_samples, p=proposed_value)
    # The CDF gives P(X <= value), we want P(>= value).
    p_val = 1 - h0_dist.cdf(n_positive_samples - 1)
    return p_val


class LinearRegression:

    def __init__(self):
        self.coeffs_ = None

    def fit(self, X, y):
        self.coeffs_ = np.linalg.solve(X.T @ X, X.T @ y)

    def predict(self, X):
        return X @ self.coeffs_


def logistic_accuracy(X_train, y_train, X_test, y_test, threas):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    decisions = (model.predict_proba(X_test) >= threas).astype(int)
    accuracy = np.sum(decisions == y_test) / len(y_test)
    return accuracy
