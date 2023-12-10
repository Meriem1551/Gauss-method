import numpy as np


def resolution(A, B, R):
    X = np.zeros(R)
    for i in range(R - 1, -1, -1):
        tmp = np.dot(A[i, i + 1 :], X[i + 1 :])
        X[i] = (B[i] - tmp) / A[i, i]

    return X
