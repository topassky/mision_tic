import random
class vector():
    def __init__(self,n):
        self.n = n
        self.V = [0]*(n+1)
    
    def construyeVector(self, m, r):
        self.V[0] = m
        for i in range(1, m + 1):
            self.V[i] = random.randint(1, r)

    def imprimeVector(self, mensaje = "vector sin nombre: \t"):
        print("\n", mensaje, end=" ")
        for i in range(1, self.V[0] + 1):
            print(self.V[i], end=", ")
        print()