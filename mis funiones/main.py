import misfunciones

n = 4

#factorial = misfunciones.factorial(4) 
#print(factorial)

def sumaDigitos(n):
    nunu = 0
    m = n
    while m > 0:
        digito = m % 10
        nunu = nunu + digito
        m = m // 10
    if nunu%2 == 0:
        return 0
    return 1

resultado = sumaDigitos(1006)


resultado = misfunciones.sumarDigitos(1005)
#print(resultado)


resultado =  misfunciones.fibo(5)
#print(resultado)


resultado =  misfunciones.esFibo(4)
#print(resultado)


resultado =  misfunciones.cuboNicomaco(3)
print(resultado)

"""
resultado = misfunciones.productoDigitosDa(28)
print(resultado)

resultado = misfunciones.invierteNumero(28)
print(resultado)


resultado = misfunciones.mcd(12, 8)
print(resultado)


resultado = misfunciones.esPrimo(23)
print(resultado)


misfunciones.tablaDeMultiplicar(12, 9)

resultado = misfunciones.comienzaCon(23)
print(resultado)


resultado = misfunciones.terminaEn(23)
print(resultado)
"""


