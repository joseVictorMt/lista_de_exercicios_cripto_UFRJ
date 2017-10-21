#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 2.1 - Algoritmo Ingenuo da Divisao

def divisaoIngenua(a, b):
    q = 0 #Quociente
    r = a #Resto
    print ('%d %d') %(q, a)
    while (r >= b): #Enquanto r for maior que b.
        r -= b #Diminui r por b a cada loop.
        q += 1 #Incrementa a cada subtracao.
        print ('%d %d') %(q, r)


n = int(input())

for i in range(0, n):
    a,b = input()
    divisaoIngenua(a, b)
    print '---'
