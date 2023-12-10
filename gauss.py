import numpy as np
from readA import readMatrixA
from readB import readB
from triangulaire import lower_triangularization


def Gauss():
    R = int(input("Enter the number of rows: "))
    N = R * R
    A = readMatrixA(R)
    B = readB()
    det_A = np.linalg.det(A)
    if det_A == 0:
        print("det equal to 0, so cant solve this syteme")
    else:
        new_A, new_B = lower_triangularization(A, B, R)
    # print(new_A)
    # print(new_B)


Gauss()
