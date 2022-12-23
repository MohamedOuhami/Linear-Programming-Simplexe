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

X =linprog(C,A_ub = A,b_ub = B, method='highs')

print(f"""
La combinaison la plus optimale est de vendre {X.x[0]} vestes avec technique 1, 
{X.x[1]} vestes avec technique 2
 et {X.x[2]} vestes avec technique 3""")
print(f"Ceci va genere {-X.fun} Dhs")