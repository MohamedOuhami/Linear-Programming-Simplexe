import numpy as np
from scipy.optimize import linprog

# Vecteur des coeffcients
C = np.array([-3,-2,-4])

# Matrice des contraitnes
A = np.array([
    [1,1,1],
    [2,3,0],
    [3,1,3]
]
)

# Second membre
B = np.array([4,7,7])

# Solve the actual problem

X =linprog(C,A_ub = A,b_ub = B, method='simplex')
print(X)