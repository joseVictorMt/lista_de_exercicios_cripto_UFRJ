#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 6.2 - Algoritmo de potenciacao modular

def potenciacaoModular(a, e, n):
    r = 1
    while(e != 0):
        if(e%2 != 0): #Verifica se e impar.
            print('%d %d %d S') %(r, a, e)
            r = pow(r*a, 1, n)
            e = (e-1)/2
        else: #Caso x nao seja impar.
            print('%d %d %d N') %(r, a, e)
            e /= 2
        a = pow(a, 2, n)
    print('%d %d %d N') %(r, a, e)


turns = input()
for i in range(0, turns):
    a, e, n = input()
    potenciacaoModular(a, e, n)
    print '---'
