from vector import vector
import random


n = int(input("Entre tamaño del primer vector: "))
a = vector(n) 
a.construyeVector(n//2,99)
#a.imprimeVector("vector vec1:\t")
print(a.V)
a.agregarDato(69)
a.imprimeVector("vector vec1:\t")
