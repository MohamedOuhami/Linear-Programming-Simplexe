import numpy as np
from scipy.optimize import linprog

# Vecteur des coeffcients
C = np.array([-24,-16])

# Matrice des contraitnes
A = np.array([
    [1,2],
    [4,2]
    ]
)

# Second membre
B = np.array([150,400])

# Solve the actual problem

X =linprog(C,A_ub = A,b_ub = B, method='simplex')
print(X)