#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 9.1 - Teste de Miller-Rabin

def modulo(b, m): #b (mod m)
    return b%m

def potenciacaoModular(a, e, n):
    r = 1
    while(e != 0):
        if(e%2 != 0): #Verifica se 'e' e impar.
            print('%d %d %d S') %(r, a, e)
            r = modulo(r*a, n)
            e = (e-1)/2
        else: #Caso 'e' nao seja impar.
            print('%d %d %d N') %(r, a, e)
            e /= 2
        a = modulo(a*a, n)
    print('%d %d %d N') %(r, a, e)
    return r

def testeMillerRabin(n, b): #Teste de Miller-Rabin
    k = 0
    q = n - 1
    while(q % 2 == 0): #Divide por 2 enquanto 'q' for par.
        k += 1
        q /= 2
    print('%d %d') %(k, q)
    r = potenciacaoModular(b, q, n)
    print('%d %d') %(q, r)
    x = q
    if(r == 1 or r == n - 1):
        return 'INCONCLUSIVO'
    for i in range(1, k):
        r = modulo(r*r, n)
        x *= 2
        print('%d %d') %(x, r)
        if(r == n-1):
            return 'INCONCLUSIVO'
    return 'COMPOSTO'

s = input()
for i in range(0, s):
    n, b = input()
    print testeMillerRabin(n, b)
    print '---'
