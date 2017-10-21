#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 8.1 - Algoritmo de Potenciacao Modular com Teorema de Fermat

def modulo(b, m): #b (mod m)
    return b%m

def potenciacaoModular(a, e, n):
    #Pequeno Teorema de Fermat
    e %= n-1
    print ('%d') %(e)

    #Potenciacao Modular
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


n = input()
for i in range(0, n):
    b, e, m = input()
    potenciacaoModular(b, e, m)
    print '---'
