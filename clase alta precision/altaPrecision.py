from vector import vector

class altaPrecision(vector):
    
    def __init__(self, n):
        vector.__init__(self, n)# Toma el vector los atributos y metodos de la clase vector
        self.V[0] = n # asigna el parametro el parametro n al vector 
    
    def mueveALaDerecha(self):
        n = self.n # Asigna el parametro n de la clase vector a m.
        for i in range(self.V[0], 0, -1):
            self.V[n] = self.V[i]
            n = n - 1
        self.V[0] = self.n - self.V[0]
        for i in range (1,self.V[0]+1):
            self.V[i] = 0
    
    def imprimeVector(self, mensaje="vector sin nombre: "):
        print("\n", mensaje)
        for i in range(self.V[0] + 1, self.n + 1):
            print(self.V[i], end = ", ")