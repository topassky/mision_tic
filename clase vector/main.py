from vector import vector
import random

n = random.randint(15,30)
Vector_aletatorio = vector(n)

"""Usamos un ciclo para llenar el vector con número del 1 al 99999"""
for i in range(1, n + 1):
    
    """Se genera aleatoriamente un número entero entre 1 y 99999"""
    Vector_aletatorio.V[i] = random.randint(1,9999)
    """Se actualiza el valor de la primera posición del vector indicando cuantas posiciones
    son usadas (En este caso es igual al tamaño del vector)"""
    Vector_aletatorio.V[0] = n

Vector_aletatorio_nuevo = vector(Vector_aletatorio.V[0])

for i in range(1, Vector_aletatorio.V[0]+1):
    Vector_aletatorio_nuevo.V[i] = Vector_aletatorio.V[i]
    Vector_aletatorio_nuevo.V[0] = Vector_aletatorio.V[0]

print(Vector_aletatorio.V)
print(Vector_aletatorio_nuevo.V)


