import numpy as np

# Definir una matriz cuadrada 
A = np.array([[4, -2, 1],
              [1, 1, 2],
              [3, 6, 7]])

# Calcular los valores y vectores propios
valores, vectores = np.linalg.eig(A)

# Imprimir los valores propios
print("Valores propios:")
for valores in valores:
    print(valores)

# Imprimir los vectores propios
print("Vectores propios:")
for vectores in vectores:
    print(vectores)
