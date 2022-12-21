import numpy as np
from scipy.optimize import linprog

# Vecteur des coeffcients
C = np.array([-3,-4,-5])

# Matrice des contraitnes
A = np.array([
    [0.5,1.5,2],
    [2,1.5,0.5],
    [0,0,0]
]
)

# Second membre
B = np.array([12,15,0])

# Solve the actual problem

X =linprog(C,A_ub = A,b_ub = B, method='simplex')
print(X)