import math

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

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

def sumarDigitos(n):
    nunu = 0
    m = n
    while m > 0:
        digito = m % 10
        nunu = nunu + digito
        m = m // 10
    return nunu

def fibo(n):
    a = 0
    b = 1
    for i in range(1, n+1):
        c = a + b
        a = b
        b = c
    return c

def esFibo(n):
    a = 0
    b = 1
    c = 1
    while c < n:
        c = a + b
        a = b
        b = c
    if c == n:
        return True
    return False

def cuboNicomaco(n):
    k = n*(n-1)+1
    cubo = k
    for i in range(1, n):
        k = k + 2
        cubo = cubo + k
    return cubo

def productoDigitosDa(n):
    nunu = 0
    m = n
    for i in range(9, 1, -1):
        while m % i == 0:
            nunu = nunu * 10 + i
            m = m // i
    if m != 1:
        return 0
    nunu = invierteNumero(nunu)
    return nunu

def invierteNumero(n):
    nunu = 0
    m = n
    while m > 0:
        digito = m % 10
        nunu = nunu * 10 + digito
        m = m // 10
    return nunu

def mcd(x, y):
    res = x % y
    while res != 0:
        x = y
        y = res
        res = x % y
    return y

def mcm(x, y):
    return x * y // mcd(x, y)

def potenciacion(x, y):
    j = 1
    pro = x
    while j < y:
        res = pro
        i = 1
        while i < x:
            res = res + pro
            i = i + 1
        pro = res
        j = j + 1
    return pro

def esPrimo(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= n//2 +2:
        if n % i == 0:
            return False
        i = i + 2
    return True

def esPar(n):
    if n % 2 == 0:
        return True
    return False

def tablaDeMultiplicar(m, n):
    print("Tablas de multiplicar del 1 al ", m)
    i = 1
    while i <= m:
        j = 1
        while j <= n:
            k = i * j
            print("\t", i, "\t*", "\t", j, "\t=", "\t", k)
            j = j + 1
        i = i + 1
        print()

def comienzaCon(x):
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd

def terminaEn(x):
    ud = x % 10
    return ud