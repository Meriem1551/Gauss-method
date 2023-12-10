import numpy as np


def lower_triangularization(A, B, R):
    for k in range(R - 1):
        for i in range(k + 1, R):
            w = A[i][k] / A[k][k]
            for j in range(R):
                if j < i:
                    A[i][j] = 0
                else:
                    A[i][j] -= w * A[k][j]
            B[i] -= w * B[k]
    return (A, B)
