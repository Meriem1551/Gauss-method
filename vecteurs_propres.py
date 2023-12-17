import numpy as np


def vecteurs_propres(A, lambda_v, R):
    if len(lambda_v) != R:
        raise ValueError("Length of lambda_v must be equal to the number of rows")

    eigenvectors_list = []  # Use a different name for the list

    for i in range(R):
        valeur_propre = lambda_v[i]
        _, vect_propre = np.linalg.eig(A - valeur_propre * np.identity(R))
        eigenvectors_list.append(vect_propre[:, 0].tolist())

    return eigenvectors_list


# Test de la fonction vecteurs_propres()
