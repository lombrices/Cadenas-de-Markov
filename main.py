import numpy as np

# Matriz de transicion
p = np.array([
    [0.6, 0.2, 0.2], 
    [0.3, 0.4, 0.3],  
    [0.2, 0.3, 0.5]   
], dtype=float)

for i in range(0,3):
    s=p[i,0]+p[i,1]+p[i,2]
    if(s!=1.0):
        print("Las filas de la matriz de transicion deben sumar 1")
        exit(0)

v0 = np.empty(3)

x=0.0
y=0.0
z=0.0
print("A continuación ingrese las probabilidades iniciales para cada producto, debe ingresarlas como decimal con un punto\n")
while(x+y+z != 1.0):
    print("Las probabilidades deben sumar 1\n")
    x=float(input("Ingrese la probabilidad inicial de que el cliente elija una Big Mac: "))
    y=float(input("Ingrese la probabilidad inicial de que el cliente elija un Mc Flurry: "))
    z=float(input("Ingrese la probabilidad inicial de que el cliente elija Papas Fritas: "))

v0 = np.array([x, y, z])

print("v0="+str(v0))


p_transpose = p.T
p_transpose -= np.eye(p.shape[0])


A = np.vstack([p_transpose, np.ones(p.shape[0])])
b = np.zeros(p.shape[0] + 1)
b[-1] = 1  

# Resolver el sistema
pi = np.linalg.lstsq(A, b, rcond=None)[0]

print("La probabilidad estacionaria es:", pi)
