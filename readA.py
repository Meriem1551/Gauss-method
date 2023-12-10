import numpy as np


def readMatrixA(R):
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    A = np.array(entries).reshape(R, R)
    return A
