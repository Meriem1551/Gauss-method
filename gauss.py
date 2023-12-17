import numpy as np
from readA import readMatrixA
from readB import readB
from triangulaire import lower_triangularization
from resolution import resolution
from valeur_propre import valeur_propre
from vecteurs_propres import vecteurs_propres


def Gauss_Elimination():
    R = int(input("Enter the number of rows: "))
    N = R * R
    A = readMatrixA(R)
    B = readB()
    det_A = np.linalg.det(A)
    if det_A == 0:
        print("det equal to 0, so cant solve this syteme")
    else:
        new_A, new_B = lower_triangularization(A, B, R)
        X = resolution(new_A, new_B, R)
        lambda_v = valeur_propre(new_A, R)
        V = vecteurs_propres(new_A, lambda_v, R)
        return X, lambda_v, V


X, lambda_v, V = Gauss_Elimination()
print("Result of this system is: {}".format(X))
print("Les valeurs propres sont: {}".format(lambda_v))
print("Les vacteurs propres sont: {}".format(V))
