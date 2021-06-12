from altaPrecision import altaPrecision
import random

n = random.randint(15,30)
Vector_aletatorio = altaPrecision(12)
print("inicio del vector")
print(Vector_aletatorio.V)

Vector_aletatorio.construyeVector(5,99)
print("contrucción del vector")
print(Vector_aletatorio.V)


Vector_aletatorio.mueveALaDerecha()
print("mueve a la derecha")
print(Vector_aletatorio.V)

print("---------------------------")
Vector_aletatorio.imprimeVector("Vector desde clase alta precisión")




