from scipy.optimize import linprog

obj_fun = [5,6,6,8,11,9,4,7,12,7,8,5]

ineq_coef = [
    [1,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1]
]
eq_coef = [
    15000,12000,23000
]

ineq_equa = [
    [1,0,0,0,1,0,0,0,1,0,0,0],
    [0,1,0,0,0,1,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0,1,0,0,0,1]
]
eq_equa = [
    10000,5000,20000,15000
]

X = linprog(c = obj_fun, A_ub = ineq_coef, b_ub = eq_coef, A_eq = ineq_equa, b_eq = eq_equa, method = 'highs')

print("La configuration la plus optimale est la suivant : ")

print("\nConcernant l'usine A")
print(f"Transport de l'usine A vers Point de vente 1 : {int(X.x[0])}")
print(f"Transport de l'usine A vers Point de vente 2 : {int(X.x[1])}")
print(f"Transport de l'usine A vers Point de vente 3 : {int(X.x[2])}")
print(f"Transport de l'usine A vers Point de vente 4 : {int(X.x[3])}")

print("\nConcernant l'usine B")
print(f"Transport de l'usine B vers Point de vente 1 : {int(X.x[4])}")
print(f"Transport de l'usine B vers Point de vente 2 : {int(X.x[5])}")
print(f"Transport de l'usine B vers Point de vente 3 : {int(X.x[6])}")
print(f"Transport de l'usine B vers Point de vente 4 : {int(X.x[7])}")

print("\nConcernant l'usine C\n")
print(f"Transport de l'usine C vers Point de vente 1 : {int(X.x[8])}")
print(f"Transport de l'usine C vers Point de vente 2 : {int(X.x[9])}")
print(f"Transport de l'usine C vers Point de vente 3 : {int(X.x[10])}")
print(f"Transport de l'usine C vers Point de vente 4 : {int(X.x[11])}")

print(f"\nEnfin, le cout minimal du transport pour les 3 usines et 4 points de vente est {X.fun} Dhs")