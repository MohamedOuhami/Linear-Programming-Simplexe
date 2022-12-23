import numpy as np
from scipy.optimize import linprog
import math

# Vecteur des coeffcients
C = np.array([-24,-16])
C_max = C*-1

# Matrice des contraitnes
A = np.array([
    [1,2],
    [4,2]
    ]
)

# Second membre
B = np.array([150,400])

# Solve the actual problem

X = linprog(C,A_ub = A,b_ub = B, method='highs')
result = X.x

# Nombre de lots pour chaque modele : 
model_1 = math.floor(result[0]/10)
model_2 = math.floor(result[1]/10)
result = np.array([model_1,model_2])
profit = np.dot(result,C_max)
print(f"La combinaison la plus optimale est de vendre {model_1} 'lots de 10' du modele 1 et {model_2} 'lots de 10' du modele 2")
print(f"Ceci va genere {profit * 10} Dhs")